
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
    # 208289146  4h5m29s  2017-12-10T05:04:30Z Darkwood Stream One
    '208289146': {
        'player_type': 'PEERTUBE',
        'player_data': {
            'node_name': 'peertube.nodja.com',
            'video_id': 'b7d3a530-f612-496f-9b2e-c0dac62a8588',
        },
        'offsets': [
            [-999, 0],
        ],
    },
    # 208289270  4h28m30s 2017-12-10T05:05:02Z Darkwood Stream Two
    '208289270': {
        'player_type': 'PEERTUBE',
        'player_data': {
            'node_name': 'peertube.nodja.com',
            'video_id': 'ab3c6a93-860a-461f-ae2f-50463b1176c9',
            },
        'offsets': [
            [-999, 0],
        ],
    },
    # 208289991  5h18m37s 2017-12-10T05:08:34Z Xenoblade Chronicles 2 Stream One (It Begins)
    '208289991': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'jJxqXJnbJfQ'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 208290083  5h19m41s 2017-12-10T05:09:04Z Xenoblade Chronicles 2 Stream Two
    '208290083': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'qQHvYNRmFy0'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 208290145  3h42m13s 2017-12-10T05:09:24Z Xenoblade Chronicles 2 Stream Three (part one)
    '208290145': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'pw_ppkVqBfg'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 208290193  1h57m9s  2017-12-10T05:09:38Z Xenoblade Chronicles 2 Stream Three (part two)
    '208290193': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'hOvQX96hYU8'},
        'offsets': [
            [-999, -15],
        ],
    },
    # 208290539  5h9m33s  2017-12-10T05:11:25Z Xenoblade Chronicles 2 Stream Four
    '208290539': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'KxEAZdO39pc'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 208290563  4h15m33s 2017-12-10T05:11:34Z Xenoblade Chronicles 2 Stream Five
    '208290563': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'qGdRylQqiBQ'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 208291607  3h58m22s 2017-12-10T05:16:42Z Xenoblade Chronicles 2 Stream Six
    '208291607': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'IGxEWpBs-60'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 212956145  4h4m50s  2017-12-27T14:56:10Z Xenoblade Chronicles 2 Stream Seven
    '212956145': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': '8sYEHVaf9RY'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 212956310  4h27m7s  2017-12-27T14:57:00Z Xenoblade Chronicles 2 Stream Eight
    '212956310': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'gxujfjwR6B4'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 212956460  4h40m55s 2017-12-27T14:57:50Z Xenoblade Chronicles 2 Stream Nine
    '212956460': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'IDxfceaRvuY'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 212956582  3h57m36s 2017-12-27T14:58:22Z Xenoblade Chronicles 2 Stream Ten
    '212956582': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'RpHTZrmd3ZA'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 212956967  3h49m59s 2017-12-27T15:00:06Z Xenoblade Chronicles 2 Stream Eleven
    '212956967': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'b-WzsCXjCR4'},
        'offsets': [
            [-999, 0],
        ],
        'parts': [
            # 212957486  21m25s   2017-12-27T15:02:36Z Xenoblade Chronicles 2 Stream Eleven (Part Was Cut Off)
            ('212957486', timedelta(hours=3, minutes=52, seconds=0)),
        ],
    },
    # 212957774  2h26m35s 2017-12-27T15:03:56Z Xenoblade Chronicles 2 Stream Twelve Pt 1
    '212957774': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'VrcYQK9dSiM'},
        'offsets': [
            [-999, 0],
            [timedelta(hours=2, minutes=29, seconds=0).total_seconds(), -116],
        ],
        'parts': [
            # 212957894  2h14m3s  2017-12-27T15:04:39Z Xenoblade Chronicles 2 Stream Twelve Pt 2
            ('212957894', timedelta(hours=2, minutes=29, seconds=0)),
        ],
    },
    # 212958187  6h40m44s 2017-12-27T15:06:02Z Xenoblade Chronicles 2 Stream Thirteen (FINALE)
    '212958187': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': '8LPdidQqIDQ'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 208290332  5h36m14s 2017-12-10T05:10:26Z Doki Doki Literature Club (Blind, Chat Minimized)
    '208290332': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'OKahXPxTGfY'},
        'offsets': [
            [-999, -10],
        ],
    },
    # 208291477  8h37m32s 2017-12-10T05:16:07Z Hello Neighbor, Sadness and Madness Stream
    '208291477': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'xwe25QqVQtQ'},
        'offsets': [
            [-999, timedelta(minutes=25, seconds=30).total_seconds()],
        ],
    },
    # 212956812  6h47m36s 2017-12-27T14:59:21Z Antichamber Blind Run, No Chat. Voted by Subs and Patrons
    '212956812': {
        'player_type': 'PEERTUBE',
        'player_data': {
            'node_name': 'peertube.nodja.com',
            'video_id': '6d6c411f-85b9-47e4-b241-cf91b52e5aa9',
        },
        'offsets': [
            [-999, 0],
        ],
    },
    # 220016251  3h55m32s 2018-01-19T02:18:45Z Recettear Stream 3
    '220016251': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': '_1uPLZdRi1Y'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 220016608  4h53m40s 2018-01-19T02:19:57Z Recettear Stream 5
    '220016608': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'z0shnq5fg2s'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 220016887  5h33m16s 2018-01-19T02:20:51Z Terraria Stream 2
    '220016887': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'PKuR9R7xPGM'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 220016966  4h25m52s 2018-01-19T02:21:06Z Terraria Stream 3
    '220016966': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'C6aistm6Tek'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 224536282  3h57m59s 2018-02-01T07:45:50Z Terraria Stream 4
    '224536282': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'gI_bqmu9X84'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 224536317  3h3m9s   2018-02-01T07:46:12Z Terraria Stream 5
    '224536317': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'S_5pxDRyRPk'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 224536351  4h14m35s 2018-02-01T07:46:31Z Terraria Stream 6
    '224536351': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'oAZ78OtOjQc'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 224536391  6h38m45s 2018-02-01T07:46:50Z Terraria Stream 7
    '224536391': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'vlu8ec2425Y'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 229255232  4h37m29s 2018-02-15T11:54:38Z Terraria Final Stream
    '229255232': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'FdL97qkAP9M'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 223198636  4h3m26s  2018-01-28T07:02:29Z Lisa The Painful RPG - Stream One
    '223198636': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'zd5M_myoLsQ'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 223198776  4h27m4s  2018-01-28T07:03:18Z Lisa The Painful RPG - Stream Two
    '223198776': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': '2iDbSLS8Q7A'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 223198851  4h16m2s  2018-01-28T07:03:43Z Lisa The Painful RPG - Stream Three
    '223198851': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': '7xAO7FCneb4'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 226452904  4h42m19s 2018-02-07T00:57:28Z Subnautica Stream One
    '226452904': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'HJbtGKy4myg'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 226453025  5h3m56s  2018-02-07T00:57:50Z Subnautica Stream Two
    '226453025': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'ZT2B1Clw_fI'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 226453175  5h10m46s 2018-02-07T00:58:18Z Subnautica Stream Three
    '226453175': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'S9nfXCMbdXw'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 226453319  2h25m20s 2018-02-07T00:58:44Z Monster Hunter World Stream One
    '226453319': {
        'player_type': 'PEERTUBE',
        'player_data': {
            'node_name': 'peertube.nodja.com',
            'video_id': '002688dc-a71c-401f-bdbd-e1f5d3d14c38',
        },
        'offsets': [
            [-999, 0],
        ],
    },
    # 226453441  5h45m36s 2018-02-07T00:59:05Z Monster Hunter World Stream Two
    '226453441': {
        'player_type': 'PEERTUBE',
        'player_data': {
            'node_name': 'peertube.nodja.com',
            'video_id': '9b9aeeb0-bee2-4ab5-9f23-e1ba38fae792',
        },
        'offsets': [
            [-999, 0],
        ],
    },
    # 226453597  4h14m28s 2018-02-07T00:59:30Z Monster Hunter World Stream Three
    '226453597': {
        'player_type': 'PEERTUBE',
        'player_data': {
            'node_name': 'peertube.nodja.com',
            'video_id': 'e3fd1a34-2478-40eb-8228-e2deaa51ef83',
        },
        'offsets': [
            [-999, 0],
        ],
    },
    # 229255412  6h31m28s 2018-02-15T11:56:04Z Papers Please Stream
    '229255412': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'ZEYMM3vvDdY'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 229255460  4h45m41s 2018-02-15T11:56:26Z Shadow of the Colossus Remake Stream
    '229255460': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'iIsRmJdJ3S4'},
        'offsets': [
            [-999, 0],
        ],
    },




    # 233955508  3h48m48s 2018-03-01T06:00:03Z Persona 5 Stream 7 Part One
    '233955508': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': '8FyW1Ptd0m4'},
        'offsets': [
            [-999, 0],
        ],
        'parts': [
            # 233955554  1h37m41s 2018-03-01T06:00:20Z Persona 5 Stream 7 Part Two
            ('233955554', timedelta(hours=3, minutes=50, seconds=23)),
        ],
    },
    # 236837895  6h49m6s  2018-03-09T12:30:43Z Persona 5 Stream 8
    '236837895': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'vIQgdV8PwEg'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 236838035  5h41m8s  2018-03-09T12:31:31Z Persona 5 Stream 9
    '236838035': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'kWGd5lQIdhA'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 236838195  1h16m30s 2018-03-09T12:32:25Z Persona 5 Stream 10 (Part One)
    '236838195': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'noNxI08B_gY'},
        'offsets': [
            [-999, 0],
        ],
        'parts': [
            # 236838252  3h23m50s 2018-03-09T12:32:46Z Persona 5 Stream 10 (Part Two)
            ('236838252', timedelta(hours=1, minutes=17, seconds=35)),
        ],
    },

    # 236838332  4h26m8s  2018-03-09T12:33:14Z Persona 5 Stream 11
    '236838332': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'qwIwEf4XmJ8'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 236838396  6h10m13s 2018-03-09T12:33:35Z Persona 5 Stream 12
    '236838396': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'S5Kp255MuW8'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 236838457  5h1m24s  2018-03-09T12:33:55Z Persona 5 Stream 13
    '236838457': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'UYpu89gFqtk'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 236838499  4h24m38s 2018-03-09T12:34:12Z Persona 5 Stream 14
    '236838499': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': '0C8Cgzl9oDE'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 236838546  4h14m5s  2018-03-09T12:34:32Z Persona 5 Stream 15
    '236838546': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'b01KBkNub0M'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 246081382  4h13m7s  2018-04-03T06:42:29Z Persona 5 Stream 16
    '246081382': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'ayI_oKZjfR0'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 246081438  5h34m24s 2018-04-03T06:42:50Z Persona 5 Stream 17
    '246081438': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': '8huxIKrFikw'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 246081478  4h38m17s 2018-04-03T06:43:08Z Persona 5 Stream 18
    '246081478': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'Lsyk2MFRrwQ'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 246081528  4h16m7s  2018-04-03T06:43:25Z Persona 5 Stream 19
    '246081528': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'gvrryWeITQ0'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 246081562  4h9m13s  2018-04-03T06:43:44Z Persona 5 Stream 20
    '246081562': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'xdUfa8ZGbm0'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 246081608  5h11m28s 2018-04-03T06:44:04Z Persona 5 Stream 21
    '246081608': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'FOZhuUOM64M'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 246081662  4h14m42s 2018-04-03T06:44:21Z Persona 5 Stream 22
    '246081662': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'z1wtNnmKvyo'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 246102266  6h23m17s 2018-04-03T09:17:55Z Persona 5 Stream 23
    '246102266': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'FqJTBEg_4ZQ'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 246081740  5h35m5s  2018-04-03T06:44:57Z Persona 5 Stream 24
    '246081740': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'nU3AG01dvHk'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 246081777  4h6m53s  2018-04-03T06:45:16Z Persona 5 Stream 25
    '246081777': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'LjCGwo6SL0I'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 246081824  4h52m4s  2018-04-03T06:45:31Z Persona 5 Stream 26
    '246081824': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'O__uX2mr1N0'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 246081873  4h5m13s  2018-04-03T06:45:53Z Persona 5 Stream 27
    '246081873': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'T8VbpLrL1JM'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 246081915  6h15m23s 2018-04-03T06:46:10Z Persona 5 Stream 28
    '246081915': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'CnJyNKfxyPQ'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 246081954  6h59m14s 2018-04-03T06:46:32Z Persona 5 Stream 29 (Finale)
    '246081954': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'v4oNnN0cJHM'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 292283444  2h37m44s 2018-08-02T18:52:19Z Useless Test Stream. Maybe Ignore. Maybe. Wait... Useless?
    '292283444': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': 'jxF_wDHJw2w'},
        'offsets': [
            [-999, 0],
        ],
    },
    # 292283857  2h51m50s 2018-08-02T18:53:23Z Hooooouse Flippppppeeeeers! First Official™ Stream in the new hoose.
    '292283857': {
        'player_type': 'YOUTUBE',
        'player_data': {'video_id': '6436bh8zg_E'},
        'offsets': [
            [-999, 0],
        ],
    },




}

# move chat n seconds later:  -n
# move chat n seconds before: +n
# chat, video n seconds later:  +n
# chat, video n seconds before: -n

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
    for vod_id, up_data in list(reversed(LINK_CHAT_TO_VIDEO.items()))[:9]:
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