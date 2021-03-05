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

from conf import *

####################################################################################################
FFMPEG = os.path.join('ffmpeg')

def ffmpeg(*args):
    return subprocess.call((FFMPEG,) + args)

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
            self.vod_comments = vod['comments']
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
            # delete duplicate chat
            if 'comments' in data['vod']:
                del data['vod']['comments']

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

    def vod_backup(self):
        # if not present download chat
        self.cache_chat()

        # if not done download video
        self.download_video()

def main():
    user = TwitchUser('andersonjph')
    for vod in user.get_all_vods():

        vod_is_part_path = VOD_CACHE_DIR.joinpath(vod.id, PART_FILE_NAME)
        if vod_is_part_path.is_file():
            print(f'{vod.duration:10s} {vod.id} ### SKIPPED ### {vod.title}')
            continue
        else:
            print(f'{vod.duration:10s} {vod.id} {vod.title}')

        vod = TwitchVod(vod)
        vod.vod_backup()


if __name__ == "__main__":
    main()
