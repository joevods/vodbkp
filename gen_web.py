
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
        'title': 'Assassin\'s Creed Origins',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/582160/header.jpg',
        'vod_ids': [200534867, 200535068],
    },
    {
        'title': 'The Stanley Parable',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/221910/header.jpg',
        'vod_ids': [200535282],
    },
    {
        'title': 'Nioh',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/485510/header.jpg',
        'vod_ids': [200535433, 200535701, 200535800, 200535922, 201141301, 204955205, 204955356, 204955410, 204955498, 204955549, 204955646],
    },
    {
        'title': 'Titanfall 2',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1237970/header.jpg',
        'vod_ids': [201141434],
    },
    {
        'title': 'Undertale',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/391540/header.jpg',
        'vod_ids': [204955793, 204955882, 204955959],
    },
    {
        'title': 'Darkwood',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/274520/header.jpg',
        'vod_ids': [208289146, 208289270],
    },
    {
        'title': 'Xenoblade Chronicles 2',
        'img_link': 'https://cdn2.steamgriddb.com/file/sgdb-cdn/grid/6231291d604f83f0011928b2c8ba8bb8.png',
        'vod_ids': [208289991, 208290083, 208290145, 208290193, 208290563, 208291607, 212956145, 212956310, 212956460, 212956582, 212956967, 212957774, 212958187],
    },
    {
        'title': 'Doki Doki Literature Club',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/698780/header.jpg',
        'vod_ids': [208290332],
    },
    {
        'title': 'Hello Neighbor',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/521890/header.jpg',
        'vod_ids': [208291477],
    },
    {
        'title': 'Antichamber',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/219890/header.jpg',
        'vod_ids': [212956812],
    },
    {
        'title': 'Recettear',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/70400/header.jpg',
        'vod_ids': ['UnT6XByIWK0', 'ap9Wbnqsoic', 220016251, 220016608],
    },
    {
        'title': 'Terraria',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/105600/header.jpg',
        'vod_ids': [220016887, 220016966, 224536282, 224536317, 224536351, 224536391, 229255232],
    },
    {
        'title': 'LISA: The Painful',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/335670/header.jpg',
        'vod_ids': [223198636, 223198776, 223198851],
    },
    {
        'title': 'Subnautica',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/264710/header.jpg',
        'vod_ids': [226452904, 226453025, 226453175, 'UgZcS4cnSQg', 'XeZkhgA5cgc', 'eDX5kuqjEl8'],
    },
    {
        'title': 'Monster Hunter World',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/582010/header.jpg',
        'vod_ids': [226453319, 226453441, 226453597],
    },
    {
        'title': 'Celeste',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/504230/header.jpg',
        'vod_ids': [229255314, 229255369, 229255509, 229255583],
    },
    {
        'title': 'Papers, Please',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/239030/header.jpg',
        'vod_ids': [229255412],
    },
    {
        'title': 'Shadow of the Colossus',
        'img_link': 'https://cdn2.steamgriddb.com/file/sgdb-cdn/grid/d3416acbe6cd441c5fea6bf3a9816cd9.png',
        'vod_ids': [229255460],
    },
    {
        'title': 'Persona 5',
        'img_link': 'https://cdn2.steamgriddb.com/file/sgdb-cdn/grid/0ec04cb3912c4f08874dd03716f80df1.png',
        'vod_ids': [
            'BlntZtGNFdY', 'H3rMUO33axc', 'iaQ4vuxjRR8', 'LBYcGzqq-RQ', 'sVAgu6BiYCs', '8jMIBGQDSMk',
            233955508, 236837895, 236838035, 236838195, 236838332, 236838396, 236838457, 236838499,
            236838546, 246081382, 246081438, 246081478, 246081528, 246081562, 246081608, 246081662,
            246102266, 246081740, 246081777, 246081824, 246081873, 246081915, 246081954,
        ],
    },
    {
        'title': 'House Flipper',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/613100/header.jpg',
        'vod_ids': [292283444, 292283857],
    },
    {
        'title': 'Danganronpa: Trigger Happy Havoc',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/413410/header.jpg',
        'vod_ids': [292285433, 292285611, 292285884, 292286250, 292286443, 292286758, 292286961, 292287209],
    },





    # {
    #     'title': 'Beyond: Two Souls',
    #     'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/960990/header.jpg',
    #     'vod_ids': [847665636, 854135005, 855367450],
    # },
    # {
    #     'title': 'Detroit: Become Human',
    #     'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1222140/header.jpg',
    #     'vod_ids': [856597092, 857653675, 862308796, 863568767, 864760451],
    # },
    # {
    #     'title': 'Vampire: The Masquerade - Bloodlines',
    #     'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/2600/header.jpg',
    #     'vod_ids': [871023059, 872238689, 873453976, 874698946, 879931052, 881166481, 890251416, 891498659],
    # },
    # {
    #     'title': 'Hitman 3',
    #     'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/236870/header.jpg',
    #     'vod_ids': [882415406, 888955557, 892800970, 898237665, 899516736, 900813730, 902178405],
    # },
    # {
    #     'title': 'Marbles on Stream: Voting Game',
    #     'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1170970/header.jpg',
    #     'vod_ids': [914269565, 916562698],
    # },
    {
        'title': 'Persona 4',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1113000/header.jpg',
        'vod_ids': [
            925584510, 926801730, 928032235, 929276824, 934352133, 935556703, 938033578, 943050852,
            944278130, 945460576, 946662799, 951624284, 952849539, 954017311, 955230012, 968946251,
            970179098,
        ],
    },
    {
        'title': 'STEINS;GATE',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/412830/header.jpg',
        'vod_ids': [930641620, 939427008, 948027533, 956616702],
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
