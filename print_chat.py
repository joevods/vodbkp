import argparse
import gzip
import json
import re
from datetime import timedelta
from glob import glob


def print_chat(chat_path, user_filter=None, regex_filter=None):
    pattern = re.compile(regex_filter, re.IGNORECASE) if regex_filter else None

    with gzip.open(chat_path, 'rt', encoding='utf8') as f:
        data = json.load(f)

    for msg in data['chat']:
        try:
            # Determine format type
            if msg['commenter'] is None:
                name = '---UNDEFINED---'
                message = ''.join(f['text'] for f in msg['message']['fragments'])
                time = timedelta(seconds=int(msg['contentOffsetSeconds']))
            elif 'display_name' in msg['commenter']:
                # old v5 API format
                name = msg['commenter']['display_name']
                message = msg['message']['body']
                time = timedelta(seconds=int(msg['content_offset_seconds']))
            elif 'displayName' in msg['commenter']:
                # new GraphQL format
                name = msg['commenter']['displayName']
                message = ''.join(f['text'] for f in msg['message']['fragments'])
                time = timedelta(seconds=int(msg['contentOffsetSeconds']))
            else:
                raise RuntimeError()

            # Apply filters
            if user_filter and name.lower() != user_filter.lower():
                continue

            if pattern:
                if not pattern.search(message):
                    continue
                # Highlight matched parts in yellow
                message = pattern.sub(lambda m: f"\033[93m{m.group(0)}\033[0m", message)

            print(f'{str(time):7s} {name:25s}: {message}')

        except Exception as e:
            print("Error parsing message:", msg)
            raise e


def get_ordered_vods():
    """Return sorted list of numeric VOD IDs from cache/vods/*/chat.json.gz."""
    return sorted(int(x[11:-13]) for x in glob('cache/vods/*/chat.json.gz'))


def main():
    parser = argparse.ArgumentParser(description="Print Twitch chat messages from cached VOD files.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-i", "--index", type=int, help="Index in the sorted VOD list (can be negative).")
    group.add_argument("-v", "--vod", type=int, help="Direct numeric VOD ID.")
    parser.add_argument("-u", "--user", help="Filter messages to only those from the specified username.")
    parser.add_argument("-m", "--match", help="Only print messages whose text matches this regex (case-insensitive).")

    args = parser.parse_args()

    ordered_vod_nums = get_ordered_vods()

    vod_ids = []
    if args.vod is not None:
        vod_ids = [args.vod]
    elif args.index is not None:
        try:
            vod_ids = [ordered_vod_nums[args.index]]
        except IndexError:
            parser.error(f"Index {args.index} out of range (0–{len(ordered_vod_nums)-1})")
    else:
        # Default: print last 10 VODs
        vod_ids = ordered_vod_nums[-10:]

    for i, vod_id in enumerate(vod_ids):
        if len(vod_ids) > 1:
            print(f"\n\033[96m{'=' * 20}  VOD {vod_id}  {'=' * 20}\033[0m\n")
        path = f'cache/vods/{vod_id}/chat.json.gz'
        print_chat(path, user_filter=args.user, regex_filter=args.match)


if __name__ == "__main__":
    main()
