import datetime
import gzip
import json
from pprint import pprint
import subprocess
import tempfile
from pathlib import Path
import tempfile
from dateutil.parser import isoparse

from web_chat import process_chat_for_web_gql

BASE_VIDEO_PATH = Path("work")
BASE_CHAT_PATH = Path("cache/vods")

def concat_videos(vod_ids, output_path):
    with tempfile.NamedTemporaryFile('w+', delete=False, suffix=".txt") as tf:
        for vod_id in vod_ids:
            video_path = BASE_VIDEO_PATH / f"{vod_id}.mp4"
            tf.write(f"file '{video_path.resolve()}'\n")
        tf.flush()

        subprocess.run([
            'ffmpeg', '-f', 'concat', '-safe', '0',
            '-i', tf.name,
            '-c', 'copy',
            str(output_path)
        ], check=True)

def concat_chats(vod_ids):
    dead_time = datetime.timedelta(seconds=0)
    stitched_chat = []
    prev_end_ts = None

    for vod_id in vod_ids:
        video_path = BASE_VIDEO_PATH / f"{vod_id}.mp4"
        chat_path = BASE_CHAT_PATH / vod_id / "chat.json.gz"

        with gzip.open(chat_path, 'rt', encoding='utf-8') as f:
            vod_data = json.load(f)

        base_ts = isoparse(vod_data['vod']['created_at'])
        if prev_end_ts is not None:
            # find time elapsed between vod parts
            dead_time += base_ts - prev_end_ts

        chat = vod_data['chat']
        fixed_chat = []
        for msg in chat:
            msg_ts = isoparse(msg['createdAt'])
            fixed_msg_ts = msg_ts - dead_time
            msg['createdAt'] = fixed_msg_ts.isoformat(timespec='milliseconds').replace('+00:00', 'Z')
            fixed_chat.append(msg)


        # overflow = [msg for msg in stitched_chat if msg['createdAt'] >= fixed_chat[0]['createdAt']]
        # if overflow:
        #     print(len(overflow))

        # remove overflowing comments
        stitched_chat = [msg for msg in stitched_chat if msg['createdAt'] < fixed_chat[0]['createdAt']]

        for msg in stitched_chat[-10:]:
            text = ''.join(m['text'] for m in msg['message']['fragments'])
            print(f"{msg['contentOffsetSeconds']:3d} {msg['commenter']['displayName']}: {text}")

        stitched_chat.extend(fixed_chat)


        # update end ts for next iteration
        video_duration = get_video_duration(video_path)
        prev_end_ts = base_ts + datetime.timedelta(seconds=video_duration)



        for msg in fixed_chat[:10]:
            text = ''.join(m['text'] for m in msg['message']['fragments'])
            print(f"{msg['contentOffsetSeconds']:3d} {msg['commenter']['displayName']}: {text}")

        off1 = chat[0]['contentOffsetSeconds']
        creat1 = chat[0]['createdAt']
        creat2 = chat[-1]['createdAt']
        print(f'{off1}  {creat1}  {creat2}  {str(dead_time):15s} {base_ts}  {prev_end_ts}  {video_duration}')

    precessed_chat, _ = process_chat_for_web_gql(stitched_chat)

    # save optimized chat
    output_basename = f"stitched_{'_'.join(vod_ids)}"
    web_chat_path = BASE_CHAT_PATH / vod_ids[0] / f'chat_web_{output_basename}.json'
    with open(web_chat_path, 'w') as f:
        json.dump(precessed_chat, f, separators=(',', ':'))
    print(f'salvato in {web_chat_path}')


def test_chat(vod_id):
    chat_path = BASE_CHAT_PATH / vod_id / "chat.json.gz"

    with gzip.open(chat_path, 'rt', encoding='utf-8') as f:
        vod_data = json.load(f)

    chat = vod_data['chat']
    offset1 = chat[0]['contentOffsetSeconds']
    creat1 = chat[0]['createdAt']
    offset2 = chat[-1]['contentOffsetSeconds']
    creat2 = chat[-1]['createdAt']
    print(f'{vod_id}')
    print(f'  {creat1} {offset1}')
    print(f'  {creat2} {offset2}')

    for msg in chat:
        # pprint(msg)
        text = ''.join(m['text'] for m in msg['message']['fragments'])
        print(f"{msg['contentOffsetSeconds']:3d} {msg['commenter']['displayName']}: {text}")
        # break


def get_video_duration(video_path):
    result = subprocess.run([
        'ffprobe', '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        str(video_path)
    ], capture_output=True, text=True, check=True)

    return float(result.stdout.strip())

def main():
    vod_ids = [
        '2422978386',
        '2422982263',
        '2423019679',
    ]

    output_basename = f"stitched_{'_'.join(vod_ids)}"
    video_output = BASE_VIDEO_PATH / f"{output_basename}.mp4"
    chat_output = Path(f"{output_basename}_chat.json.gz")

    # concat_videos(vod_ids, video_output)
    concat_chats(vod_ids)
    # test_chat(vod_ids[0])
    # test_chat(vod_ids[1])

if __name__ == "__main__":
    main()
