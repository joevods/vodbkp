import datetime
import gzip
import json
import subprocess
import shutil
from pathlib import Path
from dateutil.parser import isoparse
import copy

from web_chat import emotes_db_insert_new, process_chat_for_web

# Assuming web_chat is available in your environment,
# though not strictly needed for the splitting process itself.
# from web_chat import process_chat_for_web_gql

BASE_VIDEO_PATH = Path("work")
BASE_CHAT_PATH = Path("cache/vods")
OUTPUT_BASE_PATH = Path("output_splits")

def get_video_duration(video_path):
    result = subprocess.run([
        'ffprobe', '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        str(video_path)
    ], capture_output=True, text=True, check=True)
    return float(result.stdout.strip())


def create_web_chat(base_path):
    web_chat_path = base_path / 'chat_web.json'
    if web_chat_path.is_file():
        # already exists, do nothing
        return

    # load vod data
    chat_path = base_path / 'chat.json.gz'
    with gzip.open(chat_path, 'rt', encoding='utf8') as f:
        vod_data = json.load(f)

    precessed_chat, emoticons = process_chat_for_web(vod_data)
    emotes_db_insert_new(emoticons)

    # save optimized chat
    with open(web_chat_path, 'w') as f:
        json.dump(precessed_chat, f, separators=(',', ':'))

def split_video_and_chat(vod_id, split_timestamps):
    """
    Splits a single VOD and Chat into multiple parts based on relative timestamps.
    """
    print(f"--- Processing Split for VOD: {vod_id} ---")

    # 1. Define Paths
    source_video_path = BASE_VIDEO_PATH / f"{vod_id}.mp4"
    source_chat_path = BASE_CHAT_PATH / vod_id / "chat.json.gz"

    if not source_video_path.exists() or not source_chat_path.exists():
        print(f"Error: Source files not found for VOD {vod_id}")
        return

    # 2. Load Source Chat Data
    print("Loading source chat...")
    with gzip.open(source_chat_path, 'rt', encoding='utf-8') as f:
        full_vod_data = json.load(f)

    full_chat = full_vod_data['chat']
    original_created_at = isoparse(full_vod_data['vod']['created_at'])

    # 3. Calculate Segments
    # We need a list like: [0, split_1, split_2, ..., video_end]
    total_duration = get_video_duration(source_video_path)

    # Ensure timestamps are sorted and strictly floats
    sorted_splits = sorted([float(ts) for ts in split_timestamps])

    # Create segment pairs (start, end)
    boundaries = [0.0] + sorted_splits + [total_duration]
    segments = []
    for i in range(len(boundaries) - 1):
        segments.append((boundaries[i], boundaries[i+1]))

    # 4. Process Each Segment
    for index, (start_time, end_time) in enumerate(segments):
        part_number = index + 1
        duration = end_time - start_time

        # Define Output Folders
        part_folder_name = f"{int(vod_id)+part_number}" # f"{vod_id}_{part_number}"
        part_output_dir = OUTPUT_BASE_PATH / part_folder_name
        part_output_dir.mkdir(parents=True, exist_ok=True)

        print(f"Processing Part {part_number}: {start_time}s to {end_time}s (Duration: {duration}s)")

        # --- A. Split Video (FFmpeg) ---
        part_video_path = part_output_dir / f"{part_folder_name}.mp4"

        # -ss before -i is fast seeking (keyframe interval extraction).
        # -c copy avoids re-encoding (no quality loss).
        cmd = [
            'ffmpeg', '-y',          # Overwrite output
            '-ss', str(start_time),  # Start time
            '-i', str(source_video_path),
            '-t', str(duration),     # Duration to cut
            '-c', 'copy',            # Stream copy (no re-encode)
            '-avoid_negative_ts', 'make_zero', # Ensure timestamps start at 0
            str(part_video_path)
        ]

        try:
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"  [Video] Saved to {part_video_path}")
        except subprocess.CalledProcessError as e:
            print(f"  [Video] Error processing part {part_number}: {e}")
            continue

        # --- B. Split Chat ---
        part_chat_msgs = []

        for msg in full_chat:
            offset = msg['contentOffsetSeconds']

            # Check if message belongs to this segment
            if start_time <= offset < end_time:
                # Create a copy to not mutate original list
                new_msg = copy.deepcopy(msg)

                # Adjust offset relative to the new video start
                new_msg['contentOffsetSeconds'] = offset - start_time
                part_chat_msgs.append(new_msg)

        # Prepare new JSON structure
        part_data = copy.deepcopy(full_vod_data)
        part_data['chat'] = part_chat_msgs

        # Update Metadata
        # Update duration
        part_data['vod']['duration'] = int(duration) # usually int in twitch api

        # Update created_at to match the real time this part started
        part_start_absolute = original_created_at + datetime.timedelta(seconds=start_time)
        part_data['vod']['created_at'] = part_start_absolute.isoformat()

        # Save Chat
        part_chat_path = part_output_dir / "chat.json.gz"
        with gzip.open(part_chat_path, 'wt', encoding='utf-8') as f:
            json.dump(part_data, f, separators=(',', ':'))
        print(f"  [Chat]  Saved {len(part_chat_msgs)} messages to {part_chat_path}")

        create_web_chat(part_output_dir)

    print(f"Done processing {vod_id}.\n")

def main():
    # --- Configuration ---

    # 1. The VOD ID you want to split
    target_vod_id = '2639832489'

    # 2. List of timestamps (in seconds) where the splits should happen.
    #    Example: Split at 10 minutes (600s) and 30 minutes (1800s).
    #    This will create 3 parts:
    #       Part 1: 0s -> 600s
    #       Part 2: 600s -> 1800s
    #       Part 3: 1800s -> End
    split_timestamps = [
        datetime.timedelta(hours=9, minutes=28, seconds=00).total_seconds(),
        datetime.timedelta(hours=18, minutes=19, seconds=30).total_seconds(),
    ]

    # Run the split
    split_video_and_chat(target_vod_id, split_timestamps)

if __name__ == "__main__":
    main()