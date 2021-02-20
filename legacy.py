
from main import *

def load_legacy():
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
    load_legacy()
