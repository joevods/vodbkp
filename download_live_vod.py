from datetime import timedelta
import json
from pathlib import Path
import re
import subprocess
import time
import requests
import twitch
import yt_dlp
from IPython import embed
import sys
from tqdm import tqdm
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import shutil
import gzip

from web_chat import backup_unknown_emotes, emotes_db_insert_new, process_chat_for_web

# create a global twitch helix object
with open('helix_auth.json') as f:
    twitch_helix_auth = json.load(f)
    HELIX = twitch.Helix(*twitch_helix_auth)

def to_local_timezone(dt: datetime) -> datetime:
    """Convert a datetime object to the current local timezone."""
    if dt.tzinfo is None:
        # Assume the input datetime is in UTC if naive
        dt = dt.replace(tzinfo=timezone.utc)

    return dt.astimezone(ZoneInfo("localtime"))

def run_ffmpeg(*args, timeout=60, capture_output=True):
    command = ['ffmpeg'] + list(str(a) for a in args)

    try:
        result = subprocess.run(command, timeout=timeout, check=True, capture_output=capture_output, text=True)
        return True
    except subprocess.TimeoutExpired as e:
        print(f"FFmpeg timed out and was killed. {command}")
        return False
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg failed: {e.stderr}")
        return False

def time_to(target):
    return target - time.time()

def time_from(target):
    return -time_to(target)

def remove_folder(path):
    try:
        shutil.rmtree(path)
        print(f"Deleted: {path}")
    except FileNotFoundError:
        print(f"Folder not found: {path}")
    except PermissionError:
        print(f"Permission denied: {path}")
    except Exception as e:
        print(f"Error deleting {path}: {e}")

def sleep_with_progress(sleep_time: float, interval: float = 1.0):
    start_time = time.monotonic()
    end_time = start_time + sleep_time
    with tqdm(total=int(sleep_time), leave=None, bar_format="{l_bar}{bar} {n:.1f}/{total:.1f}s") as pbar:
        while True:
            elapsed = time.monotonic() - start_time
            remaining = max(0, end_time - time.monotonic())
            pbar.n = int(elapsed)  # Directly set the progress value
            pbar.refresh()    # Force tqdm to update
            if elapsed >= sleep_time:
                break
            time.sleep(min(interval, remaining))  # Sleep only for the remaining time if it's small

def new_comment_generator(vod_id):
    s = requests.Session()
    s.headers.update({
        'Client-Id': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp',
    })

    cursor = None
    while True:
        req_data = [
            {
                "operationName": "VideoCommentsByOffsetOrCursor",
                "variables": {
                    "videoID": str(vod_id),
                },
                "extensions": {
                    "persistedQuery": {
                        "version": 1,
                        "sha256Hash": "b70a3591ff0f4e0313d126c6a1502d79a1c02baebb288227c582044aa76adf6a"
                    }
                }
            }
        ]
        if cursor is None:
            req_data[0]['variables']['contentOffsetSeconds'] = 0.0
        else:
            req_data[0]['variables']['cursor'] = cursor

        r = s.post('https://gql.twitch.tv/gql', json=req_data)
        res_data = r.json()

        for comm_data in res_data[0]['data']['video']['comments']['edges']:
            cursor = comm_data['cursor']
            yield comm_data['node']

        if not res_data[0]['data']['video']['comments']['pageInfo']['hasNextPage']:
            break

class TwitchUser:
    def __init__(self, username) -> None:
        self.username = username
        self.user = HELIX.user(username)
        if not self.user:
            raise RuntimeError(f'Channel {username} not found')

    def get_stream(self):
        try:
            streams = list(HELIX.streams(user_id=self.user.id))
        except twitch.helix.resources.streams.StreamNotFound as e:
            return None

        if len(streams) == 1:
            return streams[0]
        elif len(streams) > 1:
            raise RuntimeError(f'More than one stream? {streams}')
        else:
            return None

    def get_vods(self):
        return [vod for vod in self.user.videos() if vod.type == 'archive']

    def get_stream_vod(self):
        stream = self.get_stream()
        if stream is not None:
            stream_vod = [vod for vod in self.get_vods() if vod.data['stream_id'] == stream.id]
            if len(stream_vod) == 1:
                return stream_vod[0]
            elif len(stream_vod) == 0:
                return None
            else:
                raise RuntimeError(f'Channel {self.username} is live but multiple vods for same stream? {stream_vod}')
        else:
            return None

class ChannelVodDownloader:
    LIVE_POLLING_TIME = 2 * 60

    def __init__(self, channel_name):
        self.channel_name = channel_name
        self.twitch_user = TwitchUser(channel_name)

    def wait_for_live(self):
        pbar = tqdm(leave=None)
        while True:
            pbar.update(1)
            stream_vod = self.twitch_user.get_stream_vod()
            if stream_vod is not None:
                pbar.close()
                print(f"{self.channel_name} is live! {stream_vod.url}")
                lvd = LiveVodDownloader(stream_vod)
                lvd.download_live_vod()
                pbar = tqdm(leave=None)
            else:
                pbar.set_description(f"{self.channel_name} is not live.")

            sleep_with_progress(self.LIVE_POLLING_TIME)

    def download_specific_vod(self, index:int):
        vods = self.twitch_user.get_vods()
        vod = vods[index]
        lvd = LiveVodDownloader(vod)
        lvd.download_live_vod()

    def print_vods(self):
        for i, vod in enumerate(self.twitch_user.get_vods()):
            dt = to_local_timezone(datetime.fromisoformat(vod.created_at))
            date = dt.strftime('%Y-%m-%d %H:%M:%S')
            print(f'{i:2d} {date} {vod.duration:10s} {vod.id} {vod.title}')

class LiveVodDownloader:
    POLL_INTERVAL = 60  # Time interval in seconds to check for updates
    UPDATE_LIST_TIME = 60*7  # Time in seconds to wait considering the vod as finished

    def __init__(self, vod):
        self.vod = vod

        self.base_url = None
        self.m3u8_url = None
        self.m3u8_content = None
        self.downloaded_fragments = set()
        self.chunk_path = Path('.', 'chunks', f'{self.vod.id}')
        self.work_path = Path('.', 'work')
        self.data_path = Path('.', 'cache', 'vods', f'{self.vod.id}')
        self.last_frag_update = 0
        self.loop_time = 0

    def get_vod_urls(self):
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.vod.url, download=False)
            info = ydl.sanitize_info(info)

        self.m3u8_url = info['url']
        self.base_url = self.m3u8_url[:self.m3u8_url.rfind('/')]

    def get_fragments_map(self):
        response = requests.get(self.m3u8_url)
        if response.status_code != 200:
            print(f'Failed to get m3u8 playlist {response.status_code=}')
            return None

        self.m3u8_content = response.text
        fragments = re.findall(r'(.*\.ts)', self.m3u8_content)

        frag_map = dict()
        for frag in fragments:
            match = re.match(r"^(\d+)(?:-(?:muted|unmuted))?\.ts$", frag)
            if not match:
                raise ValueError(f"Invalid input string format: {frag}")

            frag_val = int(match.group(1))
            frag_map[frag_val] = frag
        return frag_map

    def download_vod_fragments(self, frags_map):
        with tqdm(frags_map.items(), leave=None) as pbar:
            for num, name in pbar:
                fragment_timestamp = timedelta(seconds=10 * num)
                chunk_file = self.chunk_path / f'{num}.ts'
                temp_chunk = self.chunk_path / 'tmp_chunk.ts'
                if not chunk_file.exists():
                    chunk_url = f'{self.base_url}/{name}'
                    for _ in range(3):
                        success = run_ffmpeg('-y', '-loglevel', 'panic', '-i', chunk_url, '-c', 'copy', temp_chunk)
                        if success: break
                    else:
                        raise RuntimeError(f'Could not download {name}')
                    temp_chunk.rename(chunk_file)

                    pbar.set_description(f'{name} downloaded! ({fragment_timestamp})')
                else:
                    pass
                    pbar.set_description(f'{name} exists! ({fragment_timestamp})')

                self.downloaded_fragments.add(num)

    def vod_has_ended(self):
        parts_time = re.findall(r'#EXTINF:(.*),', self.m3u8_content)
        seconds = float(parts_time[-1])
        if seconds < 10.0:
            return True
        return time_from(self.last_frag_update) > self.UPDATE_LIST_TIME

    def check_consecutive_fragments(self):
        sorted_fragments = sorted(self.downloaded_fragments)
        if len(sorted_fragments) <= 1:
            # A single element or empty list is considered consecutive.
            return

        for i in range(len(sorted_fragments) - 1):
            if sorted_fragments[i] + 1 != sorted_fragments[i + 1]:
                raise RuntimeError(f"Warning: Gap detected between {sorted_fragments[i]} and {sorted_fragments[i + 1]}")

    def consolidate_vod_fragments(self):
        # create the final video and delete temp files
        frag_list_file = self.work_path / 'fragments.txt'
        output_file = self.work_path / f'{self.vod.id}.mp4'

        # check that all downloaded chunks have no gaps
        self.check_consecutive_fragments()

        with frag_list_file.open('w') as f:
            for e in tqdm(sorted(self.downloaded_fragments), leave=None):
                path = Path('../', 'chunks', f'{self.vod.id}', f'{e}.ts')
                f.write(f'file {path}\n')

        run_ffmpeg('-y', '-f', 'concat', '-safe', '0', '-i', frag_list_file, '-c', 'copy', output_file, timeout=None, capture_output=False)
        frag_list_file.unlink()

        remove_folder(str(self.chunk_path))

    def get_fragment_time_delta(self):
        return timedelta(seconds=10 * max(self.downloaded_fragments))

    def download_live_vod(self):
        self.chunk_path.mkdir(parents=True, exist_ok=True)

        self.get_vod_urls()

        pbar = tqdm(leave=None)
        while True:
            pbar.update(1)
            pbar.set_description('Checking update')
            self.loop_time = time.time()
            # download latest fragments
            fragments_map = self.get_fragments_map()
            if fragments_map is None:
                continue

            fragments = set(fragments_map.keys())
            new_fragments = fragments - self.downloaded_fragments
            new_fragments_map = {k:v for k,v in fragments_map.items() if k in new_fragments}

            if new_fragments_map:
                pbar.set_description(f'found {len(new_fragments)} new fragments')
                self.last_frag_update = time.time()
                self.download_vod_fragments(new_fragments_map)
                continue

            if self.vod_has_ended():
                pbar.set_description('vod is ended')
                break

            # sleep until next poll
            to_sleep = time_to(self.loop_time + self.POLL_INTERVAL)
            if to_sleep > 0:
                pbar.set_description(f'{self.get_fragment_time_delta()}. {int(time_from(self.last_frag_update))} seconds from new frags')
                sleep_with_progress(to_sleep)
                # time.sleep(to_sleep) # TODO

        pbar.close()

        self.consolidate_vod_fragments()


        self.download_chat()
        self.create_web_chat()
        backup_unknown_emotes()

    def download_chat(self):
        # create vod data folder if not existing
        self.data_path.mkdir(parents=True, exist_ok=True)

        chat_path = self.data_path / 'chat.json.gz'
        if chat_path.is_file():
            # already exists, do nothing
            # TODO log
            return

        chat = []
        for i, c in tqdm(enumerate(new_comment_generator(self.vod.id)), leave=None, desc='Downloading chat...'):
            if type(c) == dict:
                chat.append(c)
            else:
                chat.append(c.data)

        vod_data = self.vod.data
        vod_data['gql_api'] = True
        data = {
            'vod': vod_data,
            'chat': chat,
        }

        with gzip.open(chat_path, 'wt', encoding='utf8') as f:
            json.dump(data, f)

    def create_web_chat(self):
        web_chat_path = self.data_path / 'chat_web.json'
        if web_chat_path.is_file():
            # already exists, do nothing
            # TODO log
            return

        # load vod data
        chat_path = self.data_path / 'chat.json.gz'
        with gzip.open(chat_path, 'rt', encoding='utf8') as f:
            vod_data = json.load(f)

        precessed_chat, emoticons = process_chat_for_web(vod_data)
        emotes_db_insert_new(emoticons)

        # save optimized chat
        with open(web_chat_path, 'w') as f:
            json.dump(precessed_chat, f, separators=(',', ':'))

def main():
    downloader = ChannelVodDownloader('andersonjph')
    #downloader = ChannelVodDownloader('helloitsmouse')
    if len(sys.argv) > 1:
        if (m := re.match(r'https://www\.twitch\.tv/videos/(\d+)', sys.argv[1])):
            vodid = int(m.group(1))
            vod = HELIX.video(vodid)
            lvd = LiveVodDownloader(vod)
            lvd.download_live_vod()
            return

        # download a specific vod from list or show all vods
        try:
            idx = int(sys.argv[1])
        except Exception as e:
            idx = None

        if idx is None:
            downloader.print_vods()
        else:
            downloader.download_specific_vod(idx)
    else:
        # wait for live vod to download
        downloader.wait_for_live()

if __name__ == "__main__":
    main()
