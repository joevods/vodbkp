
from IPython import embed
import gzip
import json
from datetime import timedelta


def print_chat(chat_path):
    with gzip.open(chat_path, 'rt', encoding='utf8') as f:
        data = json.load(f)
    
    for msg in data['chat']:
        name = msg['commenter']['name']
        message = msg['message']['body']
        time = timedelta(seconds=int(msg['content_offset_seconds']))
        print(f'{str(time):7s} {name:25s}: {message}')
    # embed()

def main():
    import sys
    path = sys.argv[1]
    print_chat(path)

main()