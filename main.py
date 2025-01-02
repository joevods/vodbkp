from IPython import embed

import subprocess
import os.path
import os
from pathlib import Path
import gzip
import json
import re
from datetime import timedelta
from pprint import pprint

import requests
import twitch

from web_chat import process_chat_for_web, emotes_db_insert_new, backup_unknown_emotes

####################################################################################################
# CONFIG
####################################################################################################
with open('helix_auth.json') as f:
    TWITCH_HELIX_AUTH = json.load(f)

VOD_CACHE_DIR = Path('cache', 'vods')
TMP_DOWNLOAD_DIR = Path('remote_vod/work/')

CHAT_FILE_NAME = 'chat.json.gz'
STICH_CHAT_FILE_NAME = 'chat_all.json.gz'
VIDEO_FILE_NAME = 'video.mp4'
VIDEO_TMP_FILE_NAME = 'video.part.mp4'
VIDEO_INFO_FILE_NAME = 'video_info.json'
CHAT_WEB_FILE_NAME = 'chat_web.json'

####################################################################################################

FFMPEG = os.path.join('ffmpeg')

def youtube_dl(*args):
    return subprocess.call(('yt-dlp',) + args)

def ffmpeg(*args):
    return subprocess.call((FFMPEG,) + args)

def open_file_explorer(path):
    return subprocess.call(['open', path])

####################################################################################################

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

####################################################################################################

class TwitchUser:
    def __init__(self, username):
        self.helix = twitch.Helix(*TWITCH_HELIX_AUTH)
        self.user = self.helix.user(username)
        self.username = username

    def get_all_vods(self):
        return self.user.videos()

    def get_vod_by_id(self, id):
        return self.helix.video(id)

class TwitchVod:
    def __init__(self, vod):
        if type(vod) == dict:
            self.vod_data = vod
            self.vod_comments = self.vod_data['comments']
        else:
            self.vod_data = vod.data
            self.vod_data['gql_api'] = True
            self.vod_comments = new_comment_generator(self.vod_data['id'])

        self.user_id = self.vod_data['user_id']
        self.vod_id = self.vod_data['id']
        self.vod_url = self.vod_data['url']
        self.vod_title = self.vod_data['title']
        self.vod_description = self.vod_data['description']
        self.vod_created_at = self.vod_data['created_at']

        self.cache_path = VOD_CACHE_DIR.joinpath(self.vod_id)
        self.chat_path = self.cache_path.joinpath(CHAT_FILE_NAME)
        self.video_info_path = self.cache_path.joinpath(VIDEO_INFO_FILE_NAME)
        self.web_data_path = self.cache_path.joinpath(CHAT_WEB_FILE_NAME)

        self.tmp_path = TMP_DOWNLOAD_DIR
        self.video_path = self.tmp_path.joinpath(f'{self.vod_id}.mp4')
        # self.video_tmp_path = self.tmp_path.joinpath(f'{self.vod_id}.part.mp4')

        self.upload_data = None

    def cache_chat(self):
        if self.chat_path.is_file():
            print('    Chat is cached')
        else:
            chat = []
            for i, c in enumerate(self.vod_comments):
                if i % 100 == 0:
                    print(f'    Downloading chat: {i:7d} msgs', end='\r')

                if type(c) == dict:
                    chat.append(c)
                else:
                    chat.append(c.data)
            print(f'    Downloading chat: {i:7d} msgs')

            data = {
                'vod': self.vod_data,
                'chat': chat,
            }

            with gzip.open(self.chat_path, 'wt', encoding='utf8') as f:
                json.dump(data, f)

    # def download_video(self):
    #     # remove old part if exists
    #     self.video_tmp_path.unlink(missing_ok=True)

    #     # skip if video already uploaded
    #     if not self.video_info_path.is_file() and not self.video_path.is_file():
    #         print(f'    Downloading video...{self.vod_url}')
    #         res = youtube_dl('-o', str(self.video_tmp_path), str(self.vod_url))
    #         assert res == 0, f'Error downloading {self.vod_id}'

    #         # rename video file
    #         self.video_tmp_path.rename(self.video_path)

    def upload_youtube(self, upload_data=None):
        if self.video_info_path.is_file():
            print('    Video is uploaded')
        else:
            # no upload data provided externally, ask user
            if upload_data is None:
                print('Please upload file to youtube manually')
                print('='*80)
                print(f'Date streamed: {self.vod_created_at[:10]}')
                print(f'Original Title: {self.vod_title}')
                print('='*80)

                open_file_explorer(self.tmp_path)

                video_link = input('Insert video link: ')
                video_id = video_link.strip()[-11:]

                upload_data = {
                    'player_type': 'YOUTUBE',
                    'player_data': {
                        'video_id': video_id,
                    },
                    'offsets': [
                        [-999, 0],
                    ],
                    'title': self.vod_title,
                    'description': self.vod_description,
                    'user_id': '112295341',
                    'channel_id': self.user_id,
                }

            with open(self.video_info_path, 'w') as f:
                json.dump(upload_data, f, indent=2)
            # delete video file after successfull upload
            self.video_path.unlink(missing_ok=True)

        with open(self.video_info_path, 'r') as f:
            upload_data = json.load(f)

        self.upload_data = upload_data

    def create_web_data(self):
        # load vod data
        with gzip.open(self.chat_path, 'rt', encoding='utf8') as f:
            vod_data = json.load(f)

        precessed_chat, emoticons = process_chat_for_web(vod_data)

        # save optimized chat
        with open(self.web_data_path, 'w') as f:
            json.dump(precessed_chat, f, separators=(',', ':'))

        emotes_db_insert_new(emoticons)

    def vod_backup(self):

        # create vod cache and download folder if not existing
        self.cache_path.mkdir(parents=True, exist_ok=True)
        self.tmp_path.mkdir(parents=True, exist_ok=True)

        self.cache_chat()

        self.create_web_data()
        self.upload_youtube()


####################################################################################################
def stich_vods(vod_id_list, offsets):
    comments = list()
    info = None

    # concat video parts
    # ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mp4

    for vod_id, offset in zip(vod_id_list, offsets):
        chat_path = VOD_CACHE_DIR.joinpath(vod_id, CHAT_FILE_NAME)

        with gzip.open(chat_path, 'rt', encoding='utf8') as f:
            vod_data = json.load(f)

        vod = vod_data['vod']
        info = info or vod
        chat = vod_data['chat']
        print(f'{vod["duration"]:10s} {vod["id"]} {vod["title"]}')

        # shave off comments from previous part
        comments = [c for c in comments if c['content_offset_seconds'] <= offset]

        for chat_line in chat:
            chat_line['content_offset_seconds'] += offset
            comments.append(chat_line)

    # make sure comments are sequential
    for c1, c2 in zip(comments, comments[1:]):
        if c1['content_offset_seconds'] > c2['content_offset_seconds']:
            pprint(c1)
            pprint(c2)
            raise RuntimeError()

    data = {
        'vod': info,
        'chat': comments,
    }
    stich_chat_path = VOD_CACHE_DIR.joinpath(vod_id_list[0], STICH_CHAT_FILE_NAME)
    with gzip.open(stich_chat_path, 'wt', encoding='utf8') as f:
        json.dump(data, f)

    # create and save optimized chat
    precessed_chat, emoticons = process_chat_for_web(comments)
    web_data_path = VOD_CACHE_DIR.joinpath(vod_id_list[0], CHAT_WEB_FILE_NAME)
    with open(web_data_path, 'w') as f:
        json.dump(precessed_chat, f, separators=(',', ':'))

    emotes_db_insert_new(emoticons)


def print_processed_vods():
    import glob
    vod_file_list = glob.glob('cache/vods/*/video_info.json')
    vod_file_list.sort()

    for path in vod_file_list:
        with open(path) as f:
            vod = json.load(f)
            print(f'{path[11:21]} {vod["title"]}')

def main():
    user = TwitchUser('andersonjph')
    # for vod in user.get_all_vods():
    for vod in sorted(user.get_all_vods(), key=lambda x:x.id):
        if vod.id in ['1653443620', '1877892163', '1918636039']:
            print(f'{vod.duration:10s} {vod.id} ### SKIPPED ### {vod.title}')
            continue
        else:
            print(f'{vod.duration:10s} {vod.id} {vod.title}')

        vod = TwitchVod(vod)

        vod.vod_backup()

    backup_unknown_emotes()


if __name__ == "__main__":
    main()
    # print_processed_vods()
    # backup_unknown_emotes()


    # stich_vods(['930641620', '930887527'], [0, 10435])
    # stich_vods(['934352133', '934539426'], [0, 8662.699])
