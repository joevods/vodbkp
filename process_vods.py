from IPython import embed

import subprocess
import os.path
import os
import gzip
import json
import re
import glob
from pathlib import Path
from datetime import timedelta
from pprint import pprint

import twitch
import streamlink

from web_chat import process_chat_for_web, emotes_db_insert_new, backup_unknown_emotes
from conf import *

####################################################################################################

FFMPEG = os.path.join('ffmpeg')

def ffmpeg(*args):
    return subprocess.call((FFMPEG,) + args)

def open_file_explorer(path):
    return subprocess.call(['xdg-open', path])

####################################################################################################

def ask_upload_info(vod_info):
    user_id = vod_info['user_id']
    vod_title = vod_info['title']
    vod_description = vod_info['description']
    vod_created_at = vod_info['created_at']
    vod_id = vod_info['id']
    cache_path = VOD_CACHE_DIR.joinpath(vod_id)

    print('Please upload file to youtube manually')
    print('='*80)
    print(f'Date streamed: {vod_created_at[:10]}')
    print(f'Original Title: {vod_title}')
    print('='*80)

    open_file_explorer(cache_path)

    video_link = input('Insert video link: ')
    video_id = video_link.strip()[-11:]

    return {
        'player_type': 'YOUTUBE',
        'player_data': {
            'video_id': video_id,
        },
        'offsets': [
            [-999, 0],
        ],
        'title': vod_title,
        'description': vod_description,
        'channel_id': user_id,
    }

def upload_youtube(vod_data, upload_data=None):
    vod_id = vod_data['vod']['id']
    video_info_path = VOD_CACHE_DIR.joinpath(vod_id, VIDEO_INFO_FILE_NAME)
    video_path = VOD_CACHE_DIR.joinpath(vod_id, VIDEO_FILE_NAME)
    vod_is_part_path = VOD_CACHE_DIR.joinpath(vod_id, PART_FILE_NAME)

    if video_info_path.is_file():
        print('    Video info: present')
    elif vod_is_part_path.is_file():
        print('    Video info: skipping')
    else:
        # no upload data provided externally, ask user
        if upload_data is None:
            upload_data = ask_upload_info(vod_data['vod'])

        with open(video_info_path, 'w') as f:
            json.dump(upload_data, f, indent=2)
        # delete video file after successfull upload
        video_path.unlink(missing_ok=True)

def create_web_data(vod_data):
    vod_id = vod_data['vod']['id']
    web_data_path = VOD_CACHE_DIR.joinpath(vod_id, CHAT_WEB_FILE_NAME)
    vod_is_part_path = VOD_CACHE_DIR.joinpath(vod_id, PART_FILE_NAME)

    if web_data_path.is_file():
        print('    Web chat: present')
    elif vod_is_part_path.is_file():
        print('    Web chat: skipping')
    else:
        precessed_chat, emoticons = process_chat_for_web(vod_data['chat'])
        emotes_db_insert_new(emoticons)

        # save optimized chat
        with open(web_data_path, 'w') as f:
            json.dump(precessed_chat, f, separators=(',', ':'))

def stich_vods(vod_id_list, offsets):
    comments = list()
    info = None

    # TODO concat video parts
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
    emotes_db_insert_new(emoticons)

    web_data_path = VOD_CACHE_DIR.joinpath(vod_id_list[0], CHAT_WEB_FILE_NAME)
    with open(web_data_path, 'w') as f:
        json.dump(precessed_chat, f, separators=(',', ':'))

####################################################################################################

def main():
    vod_file_list = glob.glob('cache/vods/*/')
    vod_file_list.sort(reverse=True)

    for base_path in vod_file_list:
        chat_path = Path(base_path, CHAT_FILE_NAME)
        # load vod data
        with gzip.open(chat_path, 'rt', encoding='utf8') as f:
            vod_data = json.load(f)

        vod_title = vod_data['vod']['title']
        vod_id = vod_data['vod']['id']
        print(f'{vod_id:10s} {vod_title}')

        create_web_data(vod_data)
        upload_youtube(vod_data)

    backup_unknown_emotes()

if __name__ == "__main__":
    main()

    # stich_vods(['930641620', '930887527'], [0, 10435])
    # stich_vods(['934352133', '934539426'], [0, 8662.699])
