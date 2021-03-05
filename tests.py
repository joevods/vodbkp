
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

from conf import *

def check_joe_dead_emotes():
    joe_emotes = dict()

    EMOTE_DB_FILE_NAME = Path('emote_db.json')
    with open(EMOTE_DB_FILE_NAME, 'r') as f:
        emotes = json.load(f)

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

        for comment in vod_data['chat']:
            for frag in comment['message']['fragments']:
                if 'emoticon' not in frag: continue
                if frag['text'].startswith('jph') or frag['text'].startswith('anders6'):
                    joe_emotes[frag['text']] = frag['emoticon']['emoticon_id']
    
    asd = set(filter(lambda x: x.isdigit(), joe_emotes.values()))
    qwe = {v:k for k,v in joe_emotes.items()}

    for a in asd:
        b = qwe[a]
        if a in emotes:
            print(f'{a:15s} {b:20s}   {emotes[a]}')
        else:
            print(f'{a:15s} {b:20s}')

def debug_chat_gz(vod_id):
    # load vod data
    chat_path = VOD_CACHE_DIR.joinpath(vod_id, CHAT_FILE_NAME)
    with gzip.open(chat_path, 'rt', encoding='utf8') as f:
        vod_data = json.load(f)
    print('vod_data')
    print(repr(vod_data.keys()))
    embed()

def check_emote_that_died_recently():
    from web_chat import check_for_dead_emotes
    check_for_dead_emotes()

def main():
    # check_joe_dead_emotes()
    # check_emote_that_died_recently()
    # debug_chat_gz('846432586')
    pass

if __name__ == "__main__":
    main()
