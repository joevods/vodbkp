
import json
from pathlib import Path


with open('helix_auth.json') as f:
    TWITCH_HELIX_AUTH = json.load(f)

VOD_CACHE_DIR = Path('cache', 'vods')

CHAT_FILE_NAME = 'chat.json.gz'
STICH_CHAT_FILE_NAME = 'chat_all.json.gz'
VIDEO_FILE_NAME = 'video.mp4'
VIDEO_TMP_FILE_NAME = 'video.part.mp4'
VIDEO_INFO_FILE_NAME = 'video_info.json'
CHAT_WEB_FILE_NAME = 'chat_web.json'
PART_FILE_NAME = 'skip_this'
