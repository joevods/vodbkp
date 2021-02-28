
import json


data = [
    {
        'title': 'Nier Automata',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/524220/header.jpg',
        'vod_ids': ['W2sQ9T2K_jE', 'WtBXfkVPrQk', 'iSsJtK8Be5Q', 186190506, 186190862, 186191227],
    },
    {
        'title': 'Mark of the Ninja',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/214560/header.jpg',
        'vod_ids': [186191227],
    },
    {
        'title': 'The Evil Within',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/268050/header.jpg',
        'vod_ids': [186707033, 186427206, 186427462, 186427659, 186428043],
    },
    {
        'title': 'The Evil Within 2',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/601430/header.jpg',
        'vod_ids': [186706175, 186706335, 186706473, 186706642, 186872271, 187173913, 187498472],
    },
    {
        'title': 'Hyper Light Drifter',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/257850/header.jpg',
        'vod_ids': [187498472, 187695687],
    },

    {
        'title': 'Resident Evil 7',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/418370/header.jpg',
        'vod_ids': [186708744, 186871988],
    },
    {
        'title': 'The Stanley Parable',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/221910/header.jpg',
        'vod_ids': [200535282],
    },
    {
        'title': 'Undertale',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/391540/header.jpg',
        'vod_ids': [204955793, 204955882, 204955959],
    },
    {
        'title': 'Celeste',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/504230/header.jpg',
        'vod_ids': [229255314, 229255369, 229255509, 229255583],
    },
    {
        'title': 'Beyond: Two Souls',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/960990/header.jpg',
        'vod_ids': [847665636, 854135005, 855367450],
    },
    {
        'title': 'Detroit: Become Human',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1222140/header.jpg',
        'vod_ids': [856597092, 857653675, 862308796, 863568767, 864760451],
    },
    {
        'title': 'Vampire: The Masquerade - Bloodlines',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/2600/header.jpg',
        'vod_ids': [871023059, 872238689, 873453976, 874698946, 879931052, 881166481, 890251416, 891498659],
    },
    {
        'title': 'Hitman 3',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/236870/header.jpg',
        'vod_ids': [882415406, 888955557, 892800970, 898237665, 899516736, 900813730, 902178405],
    },
    {
        'title': 'Marbles on Stream: Voting Game',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1170970/header.jpg',
        'vod_ids': [914269565, 916562698],
    },

]
data = data[::-1]

for game in data:
    vids = list()
    for vid in game['vod_ids']:
        if type(vid) == int:
            vids.append({'type':'local', 'id': str(vid)})
        elif type(vid) == str:
            vids.append({'type':'yt', 'id': f'https://www.youtube.com/watch?v={vid}'})
        else:
            raise RuntimeError('wtf')
        # TODO peertube
    
    game['vod_ids'] = vids


with open('web_test/games_info.json', 'w') as f:
    json.dump(data, f)
