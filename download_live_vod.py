import requests
import subprocess
import time
import re
import sys
from pathlib import Path
from pprint import pprint

import yt_dlp

POLL_INTERVAL = 60  # Time interval in seconds to check for updates
UPDATE_LIST_TIME = 60*7  # Time in seconds to wait considering the vod as finished

def time_to(target):
    return target - time.time()

def time_from(target):
    return -time_to(target)

def ffmpeg(*args):
    cmd = ['ffmpeg'] + list(str(a) for a in args)
    subprocess.check_call(cmd)

def get_vod_info(vod_url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(vod_url, download=False)
        info = ydl.sanitize_info(info)
        return info

def vod_has_ended(content):
    result = re.findall(r'#EXTINF:(.*),', content)
    result = set(result)
    return result != {'10.000'}

def download_live_vod(vod_url, chunk_dir='./chunks', work_dir='./work', out_file_name='video.mp4'):
    # Create the output directory if it doesn't exist
    Path(chunk_dir).mkdir(exist_ok=True)
    Path(work_dir).mkdir(exist_ok=True)

    vod_info = get_vod_info(vod_url)
    m3u8_url = vod_info['url']
    vod_id = vod_info['webpage_url_basename']
    
    base_url = m3u8_url[:m3u8_url.rfind('/')]
    print(base_url)
    m3u8_entries = list()

    last_update = time.time()
    while True:
        prev_time = time.time()
        response = requests.get(m3u8_url)
        print(response)
        if response.status_code == 200:
            m3u8_content = response.text
            fragments = re.findall(r'(.*\.ts)', m3u8_content)

            new_frags = set(fragments)
            prev_frags = set(m3u8_entries)
            if not new_frags >= prev_frags:
                print(f'previous fragments changed!')
                print(f'new entries: {sorted(new_frags-prev_frags)}')
                print(f'old missing: {sorted(prev_frags-new_frags)=}')
                print(f'='*80)

            new_entries = list(f for f in fragments if f not in m3u8_entries)
            if new_entries:
                m3u8_entries = fragments
                last_update = time.time()

                # download all chunks
                for entry in new_entries:
                    chunk_url = f'{base_url}/{entry}'
                    print(chunk_url)
                    
                    chunk_file = Path(chunk_dir, entry)
                    if not chunk_file.exists():
                        ffmpeg('-y', '-loglevel', 'panic', '-i', chunk_url, '-c', 'copy', chunk_file)
                    else:
                        print(f'{entry} exists!')

        else:
            print(f"Failed to fetch M3U8 playlist. Status code: {response.status_code}")

        # if too much time since last update, exit
        if time_from(last_update) > UPDATE_LIST_TIME:
            print(f'Playlist not updated in last {UPDATE_LIST_TIME} seconds...exit')
            break
        
        if vod_has_ended(m3u8_content):
            print('Playlist seems to be finished...exit')
            break

        # get how much time to sleep for next polling
        to_sleep = time_to(prev_time + POLL_INTERVAL)
        if to_sleep > 0:
            print(f'waiting for update...')
            time.sleep(to_sleep)

    
    # m3u8_entries
    frag_list_file = Path(work_dir, 'fragments.txt')
    output_file = Path(work_dir, f'{vod_id}.mp4')
    
    with frag_list_file.open('w') as f:
        for e in m3u8_entries:
            # path = Path(chunk_dir, e).absolute().relative_to(Path(work_dir).absolute(), walk_up=True)
            path = Path('../', chunk_dir, e)
            f.write(f'file {path}\n')

    ffmpeg('-y', '-f', 'concat', '-safe', '0', '-i', frag_list_file, '-c', 'copy', output_file)
    
    input('check file before delete')
    frag_list_file.unlink()
    
    for e in m3u8_entries:
        Path(chunk_dir, e).unlink()


def main():
    if len(sys.argv) > 1:
        download_live_vod(sys.argv[1])
    else:
        print('Usage: download_live_vod.py VOD_ADDRESS')
        print('Example: download_live_vod.py \'https://www.twitch.tv/videos/1965872956\'')

if __name__ == "__main__":
    main()
