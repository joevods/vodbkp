
from pprint import pprint
from pathlib import Path
import json
import re
import requests
import datetime
import random
from dateutil.parser import isoparse


EMOTE_UNKNOWN  = ''
EMOTE_ALIVE    = 'alive'
EMOTE_ARCHIVED = 'archived'
EMOTE_DEAD     = 'dead'

EMOTE_DB_FILE_NAME = Path('cache', 'emote_db.json')
EMOTE_CACHE_PATH = Path('cache', 'emotes')
EMOTE_ALL_CACHE_PATH = Path('cache', 'all_emotes')

####################################################################################################
# EMOTE
####################################################################################################

def get_archive_resource(url):
    r = requests.get(f'https://archive.org/wayback/available?url={url}')
    if r.status_code == 200:
        archive_data = r.json()
        try:
            archive_url = archive_data["archived_snapshots"]["closest"]["url"].replace('/https://static-cdn.jtvnw.net', 'if_/https://static-cdn.jtvnw.net')
        except KeyError:
            return None

        r = requests.get(archive_url)
        if r.status_code == 200:
            return r.content

    return None

def get_twitch_emote(e_id):
    # check if emote is on twitch site
    r = requests.get(f'https://static-cdn.jtvnw.net/emoticons/v2/{e_id}/default/light/1.0')
    if r.status_code == 200:
        return r.content
    return None

def exist_twitch_emote(e_id, s=requests):
    r = s.head(f'https://static-cdn.jtvnw.net/emoticons/v2/{e_id}/default/light/1.0')
    return r.status_code == 200

def cache_emote(data, e_id, archived_emote=False):
    EMOTE_CACHE_PATH.mkdir(parents=True, exist_ok=True)
    EMOTE_ALL_CACHE_PATH.mkdir(parents=True, exist_ok=True)

    emote_path = EMOTE_ALL_CACHE_PATH.joinpath(f'{e_id}.png')
    with open(emote_path, 'bw') as f:
        f.write(data)

    if archived_emote:
        emote_path = EMOTE_CACHE_PATH.joinpath(f'{e_id}.png')
        with open(emote_path, 'bw') as f:
            f.write(data)

def get_emote_from_cache(e_id):
    emote_path = EMOTE_ALL_CACHE_PATH.joinpath(f'{e_id}.png')
    with open(emote_path, 'br') as f:
        return f.read()

####################################################################################################

def emotes_db_insert_new(new_emotes):
    with open(EMOTE_DB_FILE_NAME, 'r+') as f:
        emotes = json.load(f)
        f.seek(0)

        for e, _ in new_emotes:
            if e not in emotes:
                emotes[e] = ''
        json.dump(emotes, f, indent=2)
        f.truncate()

def backup_unknown_emotes():
    with open(EMOTE_DB_FILE_NAME, 'r') as f:
        emotes = json.load(f)

    unknown_emotes = [e for e, s in emotes.items() if s == EMOTE_UNKNOWN]
    for e_id in unknown_emotes:
        emote_data, emote_status = try_get_emote_data(e_id)
        print(f'Emote {e_id:45s}: {emote_status}')
        emotes[e_id] = emote_status

        # cache emote
        if emote_status != EMOTE_DEAD:
            archived_emote = (emote_status == EMOTE_ARCHIVED)
            cache_emote(emote_data, e_id, archived_emote)

    with open(EMOTE_DB_FILE_NAME, 'w') as f:
        json.dump(emotes, f, indent=2)

def try_get_emote_data(e_id):
    # check if emote is on twitch
    emote_data = get_twitch_emote(e_id)
    if emote_data is not None:
        return emote_data, EMOTE_ALIVE

    url = f'https://static-cdn.jtvnw.net/emoticons/v1/{e_id}/1.0/'
    archive_data = get_archive_resource(url)
    if archive_data is not None:
        return archive_data, EMOTE_ARCHIVED

    url = f'https://static-cdn.jtvnw.net/emoticons/v2/{e_id}/default/light/1.0'
    archive_data = get_archive_resource(url)
    if archive_data is not None:
        return archive_data, EMOTE_ARCHIVED

    return None, EMOTE_DEAD

# check if emote died since we cached it
def check_emote_that_died_recently():
    with open(EMOTE_DB_FILE_NAME, 'r') as f:
        emotes = json.load(f)

    alive_emotes = [e for e, s in emotes.items() if s == EMOTE_ALIVE]
    print(f'Emotes to check: {len(alive_emotes)}')

    s = requests.Session()
    for i, e_id in enumerate(alive_emotes):
        if i % 10 == 0:
            print(f'{i}/{len(alive_emotes)}', end='\r')

        if not exist_twitch_emote(e_id, s):
            # emote is dead, cache locally
            print(f'Emote died: {e_id:20s}')
            emotes[e_id] = EMOTE_ARCHIVED
            emote_data = get_emote_from_cache(e_id)
            cache_emote(emote_data, e_id, True)

    # write updated emote db
    with open(EMOTE_DB_FILE_NAME, 'w') as f:
        json.dump(emotes, f, indent=2)

def check_for_manually_added_emotes():
    with open(EMOTE_DB_FILE_NAME, 'r') as f:
        emotes = json.load(f)

    emote_cache_path = Path('cache', 'all_emotes')
    for emote_path in emote_cache_path.glob('*'):
        e_id = emote_path.stem

        if e_id not in emotes or emotes[e_id] == EMOTE_DEAD:
            print(f'Found manually added emote: {e_id}')
            emotes[e_id] = EMOTE_ARCHIVED
            emote_data = get_emote_from_cache(e_id)
            cache_emote(emote_data, e_id, True)

    # write updated emote db
    with open(EMOTE_DB_FILE_NAME, 'w') as f:
        json.dump(emotes, f, indent=2)


####################################################################################################
# MISC
####################################################################################################

def gen_color(username):
    # TODO avoid white like colors ???
    # color depends from username
    rnd = random.Random(username)

    return f'#{rnd.randrange(256):02X}{rnd.randrange(256):02X}{rnd.randrange(256):02X}'

####################################################################################################
# PROCESS CHAT
####################################################################################################

def consistent_format_check(chat_msg):
    msg_keys = set(('_id','channel_id','commenter','content_id','content_offset_seconds','content_type','created_at','message','replies','more_replies','source','state','updated_at'))
    if not set(chat_msg.keys()) <= msg_keys:
        return 'msg keys'

    commenter_keys = set(('_id','bio','created_at','display_name','logo','name','type','updated_at'))
    if chat_msg['commenter'] is not None and set(chat_msg['commenter'].keys()) != commenter_keys:
        return 'commenter keys'

    # optionals: 'bits_spent', 'emoticons', 'user_color', 'user_badges'
    message_keys = set(('bits_spent', 'body', 'emoticons', 'fragments', 'is_action', 'user_badges', 'user_color', 'user_notice_params'))
    if set(chat_msg['message'].keys()) > message_keys:
        return 'message keys'

    if chat_msg['state'] != 'published':
        return 'state'

    if chat_msg['source'] not in  ['chat', 'comment']:
        return 'source'

    if chat_msg['content_type'] != 'video':
        return 'content_type'

    badges_keys = set(('_id', 'version'))
    if 'user_badges' in chat_msg['message']:
        for b in chat_msg['message']['user_badges']:
            if set(b.keys()) != badges_keys:
                return 'user_badges'

    return None

# TODO shitty link regex
LINK_RE = re.compile(r'((?:(?:[A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www\.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)(?:(?:\/[\+~%\/.\w_-]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[\w]*))?)')

def process_chat_for_web_gql(chat_list):
    emoticons = set()
    msg_list = list()

    base_seconds = chat_list[0]['contentOffsetSeconds']
    base_datetime = isoparse(chat_list[0]['createdAt']) - datetime.timedelta(seconds=base_seconds)

    for c in chat_list:
        # TODO check consistence of chat msg

        timestamp = (isoparse(c['createdAt']) - base_datetime).total_seconds()
        timestamp = round(timestamp, 3)

        if c['commenter'] is not None:
            username = c['commenter']['displayName']
        else:
            username = '--deleted--'
            banned_comment = ''.join(f['text'] for f in c['message']['fragments'])
            # print(f'DELETED USER: {banned_comment}')
            continue

        usercolor = c['message']['userColor'] or gen_color(username)

        badges = [{'id': b['setID'], 'v':b['version']} for b in c['message']['userBadges']]

        fragments = []
        for f in c['message']['fragments']:
            if f['emote'] is not None:
                e_id = f['emote']['emoteID']
                e_name = f['text']
                fragments.append({
                    'e':{
                        'id': e_id,
                        'n': e_name,
                    }
                })
                emoticons.add((e_id, e_name))
            else:
                # text or link fragment
                chunks = LINK_RE.split(f['text'])

                assert len(chunks) % 2 == 1, f'chunks not odd {chunks}'
                while len(chunks) >= 2:
                    txt, lnk, *chunks = chunks
                    if txt:
                        fragments.append({'t': txt})
                    fragments.append({'l': lnk})
                    # print(f'link by {username:25} at {datetime.timedelta(seconds=int(timestamp))} {lnk}')

                txt, *chunks = chunks
                if txt:
                    fragments.append({'t': txt})
                assert chunks == []

        parsed_msg = {
            'b': badges,
            'u': { # user
                'n': username,
                'c': usercolor,
            },
            'f': fragments,
            't': timestamp,
        }
        msg_list.append(parsed_msg)

    return msg_list, emoticons

def process_chat_for_web_oldv5(chat_list):
    emoticons = set()
    msg_list = list()

    for c in chat_list:
        # check consistence of chat msg
        if (inconsistency := consistent_format_check(c)) is not None:
            print(inconsistency)
            pprint(c)
            break

        timestamp = round(c['content_offset_seconds'], 3)
        if c['commenter'] is not None:
            username = c['commenter']['display_name']
        else:
            # some vods have missing users (banned site-wise???)
            username = '--deleted--'
        usercolor = c['message'].get('user_color') or gen_color(username)
        badges = [{'id': b['_id'], 'v':b['version']} for b in c['message'].get('user_badges', [])]

        # rarely some messages don't have fragments
        # TODO parse anyway using emotes location
        if 'fragments' not in c['message']:
            print(f'MESSAGE WITHOUT FRAGMENTS: {c["message"]["body"]}')
            continue

        fragments = []
        for f in c['message']['fragments']:
            if 'emoticon' in f:
                e_id = f['emoticon']['emoticon_id']
                e_name = f['text']
                fragments.append({
                    'e':{
                        'id': e_id,
                        'n': e_name,
                    }
                })
                emoticons.add((e_id, e_name))

            else:
                # text or link fragment
                chunks = LINK_RE.split(f['text'])

                assert len(chunks) % 2 == 1, f'chunks not odd {chunks}'
                while len(chunks) >= 2:
                    txt, lnk, *chunks = chunks
                    if txt:
                        fragments.append({'t': txt})
                    fragments.append({'l': lnk})
                    # print(f'link by {username:25} at {datetime.timedelta(seconds=int(timestamp))} {lnk}')

                txt, *chunks = chunks
                if txt:
                    fragments.append({'t': txt})
                assert chunks == []

        parsed_msg = {
            'b': badges,
            'u': { # user
                'n': username,
                'c': usercolor,
            },
            'f': fragments,
            't': timestamp,
        }
        msg_list.append(parsed_msg)

    return msg_list, emoticons

def process_chat_for_web(vod_data):
    if 'gql_api' in vod_data['vod']:
        # new gql api vod data
        return process_chat_for_web_gql(vod_data['chat'])
    else:
        # old api vod data
        return process_chat_for_web_oldv5(vod_data['chat'])


####################################################################################################