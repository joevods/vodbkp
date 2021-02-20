from IPython import embed

import subprocess
import os.path
import os
from pathlib import Path
import gzip
import json
import re

import twitch
import streamlink

from web_chat import process_chat_for_web, emotes_db_insert_new, backup_unknown_emotes

####################################################################################################
# CONFIG
####################################################################################################
with open('helix_auth.json') as f:
    TWITCH_HELIX_AUTH = json.load(f)

VOD_CACHE_DIR = Path('cache', 'vods')

CHAT_FILE_NAME = 'chat.json.gz'
VIDEO_FILE_NAME = 'video.mp4'
VIDEO_TMP_FILE_NAME = 'video.part.mp4'
VIDEO_INFO_FILE_NAME = 'video_info.json'
CHAT_WEB_FILE_NAME = 'chat_web.json'

####################################################################################################

FFMPEG = os.path.join('ffmpeg')

def ffmpeg(*args):
    return subprocess.call((FFMPEG,) + args)

def open_file_explorer(path):
    return subprocess.call(['xdg-open', path])

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
            self.vod_comments = vod.comments

        self.user_id = self.vod_data['user_id']
        self.vod_id = self.vod_data['id']
        self.vod_url = self.vod_data['url']
        self.vod_title = self.vod_data['title']
        self.vod_description = self.vod_data['description']
        self.vod_created_at = self.vod_data['created_at']

        self.cache_path = VOD_CACHE_DIR.joinpath(self.vod_id)
        self.chat_path = self.cache_path.joinpath(CHAT_FILE_NAME)
        self.video_path = self.cache_path.joinpath(VIDEO_FILE_NAME)
        self.video_tmp_path = self.cache_path.joinpath(VIDEO_TMP_FILE_NAME)
        self.video_info_path = self.cache_path.joinpath(VIDEO_INFO_FILE_NAME)
        self.web_data_path = self.cache_path.joinpath(CHAT_WEB_FILE_NAME)

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

            # create vod cache folder if not existing
            self.cache_path.mkdir(parents=True, exist_ok=True)

            with gzip.open(self.chat_path, 'wt', encoding='utf8') as f:
                json.dump(data, f)

    def download_video(self):
        # remove old part if exists
        self.video_tmp_path.unlink(missing_ok=True)

        # skip if video already uploaded
        if not self.video_info_path.is_file() and not self.video_path.is_file():
            print(f'    Downloading video...')
            stream_url = streamlink.streams(self.vod_url)['best'].url
            res = ffmpeg('-v', 'error', '-i', stream_url, '-c', 'copy', str(self.video_tmp_path))
            assert res == 0, f'Error downloading {self.vod_id}'

            # rename video file
            self.video_tmp_path.rename(self.video_path)

    def upload_youtube(self, upload_data=None):
        if self.video_info_path.is_file():
            print('    Video is uploaded')
        else:
            # no upload data provided externally, ask user
            if upload_data is None:
                print('Please upload file to youtube manually')
                print('Title:')
                print(self.vod_title)
                print('Description:')
                print(f'Date streamed: {self.vod_created_at[:10]}')

                open_file_explorer(self.cache_path)

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

        precessed_chat, emoticons = process_chat_for_web(vod_data['chat'])

        # save optimized chat
        with open(self.web_data_path, 'w') as f:
            json.dump(precessed_chat, f, separators=(',', ':'))

        emotes_db_insert_new(emoticons)

    def vod_backup(self):
        # if not present download chat
        self.cache_chat()

        # if not done download video
        self.download_video()

        # upload video
        self.upload_youtube()

        # create page from template
        self.create_web_data()

####################################################################################################

def main():
    user = TwitchUser('andersonjph')
    for vod in user.get_all_vods():
        print(f'{vod.duration:10s} {vod.id} {vod.title}')
        vod = TwitchVod(vod)
        # vod.vod_backup()
        # backup_unknown_emotes()

if __name__ == "__main__":
    main()
