
from IPython import embed
import gzip
import json
from datetime import timedelta


def print_chat(chat_path):
    with gzip.open(chat_path, 'rt', encoding='utf8') as f:
        data = json.load(f)
    
    for msg in data['chat']:
        try:
            if msg['commenter'] is None:
                name = '---UNDEFINED---'
                message = ''.join(f['text'] for f in msg['message']['fragments'])
                time = timedelta(seconds=int(msg['contentOffsetSeconds']))
                # print(f'{str(time):7s} {name:25s}: {message}')

            elif 'display_name' in msg['commenter']:
                # old v5 api format
                name = msg['commenter']['display_name']
                message = msg['message']['body']
                time = timedelta(seconds=int(msg['content_offset_seconds']))
                print(f'{str(time):7s} {name:25s}: {message}')
            elif 'displayName' in msg['commenter']:
                # new graphql format
                name = msg['commenter']['displayName']
                message = ''.join(f['text'] for f in msg['message']['fragments'])
                time = timedelta(seconds=int(msg['contentOffsetSeconds']))
                print(f'{str(time):7s} {name:25s}: {message}')
            else:
                raise RuntimeError()
        except Exception as e:
            print(msg)
            raise e

    # embed()

def main():
    import sys
    numvod = sys.argv[1]
    path = f'cache/vods/{numvod}/chat.json.gz'
    print_chat(path)

main()