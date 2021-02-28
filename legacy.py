
from main import *

import glob
import json
import gzip
from datetime import timedelta

####################################################################################################

LINK_CHAT_TO_VIDEO = {
    # celeste 1
    '229255314': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'l2wYIuBv9ks'},
        'offsets': [
            [-999, 0],
        ],
    },
    # celeste 2
    '229255369': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'UQYXXmx3L1o'},
        'offsets': [
            [-999, 0],
        ],
    },
    # celeste 3
    '229255509': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'mPbVz65d9WI'},
        'offsets': [
            [-999, 0],
        ],
    },
    # celeste 4 part1 + 2
    '229255583': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'dDX_b5Ptarc'},
        'offsets': [
            [-999, 0],
        ],
        'parts': [
            ('229255651', timedelta(hours=1, minutes=48, seconds=5)),
        ],
    },
    # Undertale 1
    '204955793': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'z5lDuR_ocrc'},
        'offsets': [
            [-999, 0],
        ],
    },
    # Undertale 2
    '204955882': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'JZWInD1jLhA'},
        'offsets': [
            [-999, 0],
        ],
    },
    # Undertale 3
    '204955959': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'J8yiXL92nqw'},
        'offsets': [
            [-999, 0],
        ],
    },
    # Resident Evil 7 Stream One
    '186708744': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'WAZI9FHMcUw'},
        'offsets': [
            [-999, 0],
        ],
    },
    # Resident Evil 7 Stream Two
    '186871988': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'ibxRqOpM_Wk'},
        'offsets': [
            [-999, 0],
        ],
    },
    # The Stanley Parable
    '200535282': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'i_ArI2hI_88'},
        'offsets': [
            [-999, 0],
        ],
    },
    # Nier Automata 4
    '186190506': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'Z3_7G5cgKEM'},
        'offsets': [
            [-999, 0],
        ],
    },
    # Nier Automata 5
    '186190862': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': '5QryAXDcWEU'},
        'offsets': [
            [-999, 0],
        ],
    },
    # Nier Automata 6 + mark of the ninja
    '186191227': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'IGA6IlPA0CQ'},
        'offsets': [
            [-999, 0],
        ],
    },
    # Evil Within 1 Stream One
    '186707033': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'LjTUE94Hp2U'},
        'offsets': [
            [-999, 0],
        ],
    },
    # Evil Within 1 Stream Two
    '186427206': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'uLSO37CuLV4'},
        'offsets': [
            [-999, 0],
        ],
    },
    # Evil Within 1 Stream Three (part one)
    '186427462': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'snRSFEvw-bk'},
        'offsets': [
            [-999, 0],
        ],
    },
    # Evil Within 1 Stream Three (part two)
    '186427659': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'vaEV8XELUtA'},
        'offsets': [
            [-999, 0],
        ],
    },
    # Evil Within 1 DLC Stream
    '186428043': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'CJGqagrWGIs'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 186706175  5h27m57s 2017-11-01T02:21:53Z The Evil Within 2 Stream One
    '186706175': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'sBOk3GhC1eM'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 186706335  4h15m23s 2017-11-01T02:22:41Z The Evil Within 2 Stream Two
    '186706335': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': '3gLvKu-RFnw'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 186706473  2h7m7s   2017-11-01T02:23:26Z The Evil Within 2 Stream Three (Part One)
    '186706473': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': '8Aztjiv_324'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 186706642  2h50m20s 2017-11-01T02:24:16Z The Evil Within 2 Stream Three (Part Two)
    '186706642': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': '2OY6C2UVzgU'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 186872271  2h2m40s  2017-11-01T20:39:51Z The Evil Within 2 Stream Four
    '186872271': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'k8qv_aO_yrk'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 187173913  5h30m5s  2017-11-03T00:55:01Z The Evil Within 2 Stream Five
    '187173913': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': '68lhOmCk9hw'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 187498472  1h16m30s 2017-11-04T04:39:59Z The Evil Within 2 Stream Six (the end)
    '187498472': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'k8nBG7ZIcts'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 187695687  4h31m0s  2017-11-04T21:41:17Z Hyper Light Drifter Stream Two
    '187695687': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'qKdeTmiGGOU'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 200534867  49m52s   2017-11-11T23:06:01Z Assassin's Creed Origins Stream One (Part One)
    '200534867': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'jIiuo8Vmyec'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 200535068  4h3m40s  2017-11-11T23:06:50Z Assassin's Creed Origins Stream One (Part Two)
    '200535068': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': '5vRZ1yWXkV8'},
        'offsets': [
            [-999, 0],
        ],
    },

    # 200535433  4h36m17s 2017-11-11T23:08:18Z Nioh PC Stream One
    '200535433': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'iQHsmSSG5Hg'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 200535701  5h14m19s 2017-11-11T23:09:26Z Nioh PC Stream Two
    '200535701': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': '83hRgEMel9w'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 200535800  3h59m40s 2017-11-11T23:09:55Z Nioh PC Stream Three
    '200535800': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'W8n2JG7jzFU'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 200535922  5h0m9s   2017-11-11T23:10:25Z Nioh PC Stream Four
    '200535922': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'cL1SmlVKup8'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 201141301  4h19m54s 2017-11-14T06:18:09Z Nioh PC Stream Five
    '201141301': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'XeAmXe8hams'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 204955205  4h40m59s 2017-11-28T09:26:31Z Nioh PC Stream Six
    '204955205': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'TwlYrvhBRzA'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 204955356  4h44m19s 2017-11-28T09:28:03Z Nioh PC Stream Seven
    '204955356': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': '4QE19dL3a-w'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 204955410  5h9m25s  2017-11-28T09:28:35Z Nioh PC Stream Eight
    '204955410': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'Oz-VC5m6kd8'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 204955498  4h16m6s  2017-11-28T09:29:29Z Nioh PC Stream Nine
    '204955498': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'LFaSYXOz57g'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 204955549  4h54m12s 2017-11-28T09:30:03Z Nioh PC Stream Ten
    '204955549': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'vD4Q37ezp4c'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 204955646  4h13m48s 2017-11-28T09:30:58Z Nioh PC Stream Eleven (final)
    '204955646': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': '77yu0Jy3G5I'},
        'offsets': [
            [-999, 0],
        ],
    },

    # 201141434  3h40m42s 2017-11-14T06:19:21Z Titanfall 2 Campaign Stream Part One
    '201141434': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'mcbq1FRa2Z8'},
        'offsets': [
            [-999, 565],
            [timedelta(hours=3, minutes=32, seconds=0).total_seconds(), 565+10],
        ],
        'parts': [
            # 201141589  1h24m44s 2017-11-14T06:20:35Z Titanfall 2 Campaign Stream Part Two
            ('201141589', timedelta(hours=3, minutes=41, seconds=30)),
        ],
    },
}


def get_old_stream2_list():
    vod_file_list = glob.glob('chat_archive/old_streams2/*.vod')

    vod_info = []
    for path in vod_file_list:
        with open(path) as f:
            vod = json.load(f)
            vod_info.append(vod)

    vod_info.sort(key=lambda x: x['created_at'])

    return vod_info

def print_old_stream2_list(vod_info):
    for x in vod_info:
        print(f'{x["id"]:10s} {x["duration"]:8s} {x["created_at"]} {x["title"]}')

def get_old_stream2_data(stream_id):
    with open(f'chat_archive/old_streams2/{stream_id}.vod') as f:
        return json.load(f)

def get_old_stream2_chat(stream_id):
    with gzip.open(f'chat_archive/old_streams2/{stream_id}.data.gz') as f:
        vod = json.load(f)
        return vod['comments']

def process_old_stream2_with_video():
    # for vod_id, up_data in LINK_CHAT_TO_VIDEO.items():
    for vod_id, up_data in list(reversed(LINK_CHAT_TO_VIDEO.items()))[:5]:
        vod_data = get_old_stream2_data(vod_id)
        assert vod_data['id'] == vod_id
        
        comments = get_old_stream2_chat(vod_id)
        # concatenate comments of other parts if presents
        if 'parts' in up_data:
            for part_id, delta in up_data['parts']:
                part_comments = get_old_stream2_chat(part_id)
                delta = delta.total_seconds()
                for c in part_comments:
                    c['content_offset_seconds'] += delta
                assert comments[-1]['content_offset_seconds'] <= part_comments[0]['content_offset_seconds']
                comments.extend(part_comments)

        print(f'{vod_data["id"]:10s} {vod_data["duration"]:8s} {vod_data["created_at"]} {vod_data["title"]}')

        vod = {
            'id': vod_data['id'],
            'user_id': vod_data['user_id'],
            'title': vod_data['title'],
            'description': vod_data['description'],
            'created_at': vod_data['created_at'],
            'url': vod_data['url'],
            'comments': comments,
        }
        vod = TwitchVod(vod)

        upload_data = {
            'player_type': up_data['player_type'],
            'player_data': up_data['player_data'],
            'offsets': up_data['offsets'],
            "title": vod.vod_title,
            "description": vod.vod_description,
            'channel_id': vod.user_id,
        }
        vod.cache_chat()
        vod.upload_youtube(upload_data)
        vod.create_web_data()
    
    backup_unknown_emotes()


def load_legacy2():
    vod_info = get_old_stream2_list()
    # print_old_stream2_list(vod_info)

    process_old_stream2_with_video()


####################################################################################################

def load_legacy1():
    # celeste 1
    with open(Path('chat_archive', '229255314-Celeste Stream One.json')) as f:
        data = json.load(f)

    vod = {
        'id': '229255314',
        'user_id': '112295341',
        'title': 'Celeste Stream One',
        'description': '',
        'created_at': '',
        'url': '',
        'comments': data['comments'],
    }
    vod = TwitchVod(vod)

    upload_data = {
        'player_type': 'YOUTUBE',
        'player_data': {
            'video_id': 'l2wYIuBv9ks',
          },
        'offsets': [
            [-999, 0],
        ],

        "title": vod.vod_title,
        "description": vod.vod_description,
        'channel_id': vod.user_id,
    }
    vod.cache_chat()
    vod.upload_youtube(upload_data)
    vod.create_web_data()

    backup_unknown_emotes()

if __name__ == "__main__":
    # load_legacy1()
    load_legacy2()