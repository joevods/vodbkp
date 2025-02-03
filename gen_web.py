
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


    ####################################################################################################


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
    {
        'title': 'Persona 4',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1113000/header.jpg',
        'vod_ids': [
            925584510, 926801730, 928032235, 929276824, 934352133, 935556703, 938033578, 943050852,
            944278130, 945460576, 946662799, 951624284, 952849539, 954017311, 955230012, 968946251,
            970179098, 971399932, 972724128, 977558029, 978769609, 979977559, 981222557, 986106829,
            987258052, 988439615, 989640697
        ],
    },
    {
        'title': 'STEINS;GATE',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/412830/header.jpg',
        'vod_ids': [930641620, 939427008, 948027533, 956616702, 974030391],
    },
    {
        'title': 'E3 2021',
        'img_link': 'img/Special Events.jpg',
        'vod_ids': [1054075326, 1055109647, 1055346976, 1057027263],
    },
    {
        'title': 'Q&A and Test streams',
        'img_link': 'img/Special Events.jpg',
        'vod_ids': [1453636245, 1455777735, 1456749713, 1459829401],
    },
    {
        'title': 'Resident Evil Village',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1196590/header.jpg',
        'vod_ids': [1461826645, 1462775156, 1463721001, 1466648375, 1467555718],
    },
    {
        'title': 'Outer Wilds - Echoes of the Eye',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1622100/header.jpg',
        'vod_ids': [1468505512, 1469400200, 1470305943],
    },
    {
        'title': 'Wandersong',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/530320/header.jpg',
        'vod_ids': [1480190833, 1481080107],
    },
    {
        'title': 'Zero Escape: 999',
        'img_link': 'https://cdn2.steamgriddb.com/file/sgdb-cdn/grid/afdc9ddabc55c001bb143d1f8204a733.png',
        'vod_ids': [1481954029, 1482935056, 1485592610, 1486455731, 1487323087, 1488196924],
    },
    {
        'title': 'Hatsune Miku menu Q&A',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1761390/header.jpg',
        'vod_ids': [1315836093],
    },
    {
        'title': '''Zero Escape: Virtue's Last Reward''',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/477740/header.jpg',
        'vod_ids': [
            1496354411, 1497272998, 1498121498, 1499039060, 1499947982, 1502699892, 1503607933, 1504525605, 1509119809, 1510064003,
            1511038108, 1511981394,
        ],
    },
    {
        'title': 'PowerWash Simulator Q&A',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1290000/header.jpg',
        'vod_ids': [1548283759],
    },
    {
        'title': 'Neon White',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1533420/header.jpg',
        'vod_ids': [1549213175, 1550223847],
    },
    {
        'title': 'Zero Escape: Zero Time Dilemma',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/311240/header.jpg',
        'vod_ids': [1551179985, 1552200911, 1553138054, 1556983497, 1557974994, 1558928571],
    },
    {
        'title': 'God of War Ragnarök',
        'img_link': 'https://cdn2.steamgriddb.com/file/sgdb-cdn/grid/16cb80d0e0c1f391eb90a597106fcd6f.png',
        'vod_ids': [
            1647984162, 1648093171, 1648871211, 1648890541, 1649689730, 1650712766, 1651738482, 1652548603, 1653445210, 1655309441,
            1655461991, 1656249040, 1657263624, 1658236743, 1658430353,
        ],
    },
    {
        'title': 'Stray',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1332010/header.jpg',
        'vod_ids': [1673857501,],
    },
    {
        'title': 'Game Awards 2022',
        'img_link': 'img/Special Events.jpg',
        'vod_ids': [1673998559,],
    },
    {
        'title': 'Life is Strange',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/319630/header.jpg',
        'vod_ids': [1679850923, 1680735935, 1681648490, 1682542589, 1683406181,],
    },
    {
        'title': 'Life is Strange: Before the Storm',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/554620/header.jpg',
        'vod_ids': [1686034811, 1686932888, 1687819144],
    },
    {
        'title': 'Life is Strange 2',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/532210/header.jpg',
        'vod_ids': [1690186155, 1691111323, 1692085229, 1693955590],
    },
    {
        'title': 'Life is Strange: True Colors',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/936790/header.jpg',
        'vod_ids': [1695654480, 1696567157, 1697511226],
    },
    {
        'title': 'AI: The Somnium Files',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/948740/header.jpg',
        'vod_ids': [1703356223, 1704286699, 1705246580, 1706215362, 1710213913, 1711187167, 1712173469, 1713147651],
    },
    {
        'title': 'Dead Space',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1693980/header.jpg',
        'vod_ids': [1723152058, ],
    },
    {
        'title': 'Hypnospace Outlaw',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/844590/header.jpg',
        'vod_ids': [1724103409, 1725085195, 1726085710, 1727051976],
    },
    {
        'title': 'Half-Life',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/70/header.jpg',
        'vod_ids': [1731074034, 1732156243, 1733134703],
    },
    {
        'title': 'Half-Life: Opposing Force',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/50/header.jpg',
        'vod_ids': [(1733134703, '2h16m39s'), 1734106990],
    },
    {
        'title': 'Half-Life: Blue Shift',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/130/header.jpg',
        'vod_ids': [(1734106990, '3h04m54s')],
    },
    {
        'title': 'Half-Life 2',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/220/header.jpg',
        'vod_ids': [1738098002, 1739020945, 1739995226, 1740979892, 1744893152, 1745845196],
    },
    {
        'title': 'Half-Life 2: Episode One',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/380/header.jpg',
        'vod_ids': [(1745845196, '3h29m52s'), 1746848876],
    },
    {
        'title': 'Half-Life 2: Episode Two',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/420/header.jpg',
        'vod_ids': [(1746848876, '1h28m07s')],
    },
    {
        'title': 'Hunt Down The Freeman',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/723390/header.jpg',
        'vod_ids': [1747861045],
    },
    {
        'title': 'Black Mesa',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/362890/header.jpg',
        'vod_ids': [1751718416, 1752664737, 1753583792],
    },
    {
        'title': 'Forspoken',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1680880/header.jpg',
        'vod_ids': [1754543841, 1762161147, 1768791485, 1775376476, 1775456583],
    },
    {
        'title': 'Deadly Premonition: The Director\'s Cut',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/247660/header.jpg',
        'vod_ids': [1758343522, 1760158440, 1761173567, 1764997332, 1765044056, 1766844106],
    },
    {
        'title': 'Pizza Tower',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/2231450/header.jpg',
        'vod_ids': [1767777362],
    },
    {
        'title': 'Gravity Rush',
        'img_link': 'https://cdn2.steamgriddb.com/file/sgdb-cdn/thumb/a61a12d1bc9c26992eb5c7d7929c9b5f.jpg',
        'vod_ids': [1771565090, 1772472445, 1774307569],
    },
    {
        'title': '100K follower special',
        'img_link': 'img/Special Events.jpg',
        'vod_ids': [1773361778],
    },
    {
        'title': '13 Sentinels: Aegis Rim',
        'img_link': 'https://cdn2.steamgriddb.com/file/sgdb-cdn/thumb/dded2ec516198fbc6f630933f463ba19.jpg',
        'vod_ids': [1778132534, 1779061487, 1779949016, 1780841897, 1784540372, 1785438441, 1786330368, 1787259036, 1790851211, 1791736898],
    },
    {
        'title': 'Atomic Heart',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/668580/header.jpg',
        'vod_ids': [1788236114,],
    },
    {
        'title': 'Resident Evil 4',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/2050650/header.jpg',
        'vod_ids': [1803276404, 1804149509, 1805018538],
    },
    {
        'title': 'STAR WARS Jedi: Survivor',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1774580/header.jpg',
        'vod_ids': [
            1805878705, 1806829545, 1806859534, 1809570595, 1810442951, 1811243941, 1812101592, 1815531578, 1816382128, 1817218001,
            1818064728, 1821441402, 1822279782,
        ],
    },
    {
        'title': 'The Legend of Zelda: Tears of the Kingdom',
        'img_link': 'img/3a86e24c677ab94e012855ee068b24da.png',
        'vod_ids': [
            1819509441, 1820380494,
        ],
    },
    {
        'title': 'Hi-Fi RUSH',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1817230/header.jpg',
        'vod_ids': [
            1833273341, 1834122610, 1834934737,
        ],
    },
    {
        'title': 'The Lord of the Rings: Gollum',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1265780/header.jpg',
        'vod_ids': [
            1835875243, 1840192721, 1841955066,
        ],
    },
    {
        'title': 'Gravity Rush 2',
        'img_link': 'https://cdn2.steamgriddb.com/file/sgdb-cdn/grid/40c224d103653498c3d562aceca418e9.png',
        'vod_ids': [
            1839329365, 1846961744, 1847823038, 1851162767
        ],
    },
    {
        'title': 'Summer Gaming Conferences 2023',
        'img_link': 'img/Special Events.jpg',
        'vod_ids': [
            1841094016, 1843685896,
        ],
    },
    {
        'title': 'Amnesia: The Bunker',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1944430/header.jpg',
        'vod_ids': [
            1845834773, 1846688002,
        ],
    },
    {
        'title': 'Darkest Dungeon II',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1940340/header.jpg',
        'vod_ids': [
            1852041371,
        ],
    },
    {
        'title': 'Final Fantasy XVI',
        'img_link': 'https://cdn2.steamgriddb.com/file/sgdb-cdn/grid/69744f719acb4dc62d5d5c24fed3c78c.png',
        'vod_ids': [
            1852908095, 1853802648, 1857234985, 1857287884, 1858088894, 1858945547, 1859813043, 1860055357, 1863644169, 1864472456,
            1865358501, 1866225550, 1867066885,
        ],
    },
    {
        'title': 'Diablo IV',
        'img_link': 'https://cdn2.steamgriddb.com/file/sgdb-cdn/grid/2c95cde3a47db0f2be30660b6b8a9c94.jpg',
        'vod_ids': [
            1868918065,
        ],
    },
    {
        'title': 'Ghost Trick: Phantom Detective',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1967430/header.jpg',
        'vod_ids': [
            1870054397, 1870905300, 1871835066, 1872701838
        ],
    },
    {
        'title': 'Rabi-Ribi',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/400910/header.jpg',
        'vod_ids': [
            1875239496, 1876129445, 1877056383, 1881358560, 1882235258
        ],
    },
    {
        'title': 'Dujanah',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/681240/header.jpg',
        'vod_ids': [
            1883134419
        ],
    },
    {
        'title': 'Twelve Minutes',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1097200/header.jpg',
        'vod_ids': [
            1884009276
        ],
    },
    {
        'title': 'AI: THE SOMNIUM FILES - nirvanA Initiative',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1449200/header.jpg',
        'vod_ids': [
            1887484889, 1888286523, 1889156034, 1890058779, 1890932915, 1893420212, 1894309461, 1895193903, 1896052303, 1896962336,
            1897787278,
        ],
    },
    {
        'title': 'Inscryption',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1092790/header.jpg',
        'vod_ids': [
            1905627269, 1906492198, 1907349885, 1908153041
        ],
    },
    {
        'title': 'Armored Core VI Fires Of Rubicon',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1888160/header.jpg',
        'vod_ids': [
            1908286988, 1909195064, 1911733493, 1912650313, 1912685408
        ],
    },
    {
        'title': 'Starfield',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1716740/header.jpg',
        'vod_ids': [
            1914283594, 1916249356, 1917013216, 1917875705, 1918666619, 1919498650, 1920358438, 1921221758, 1923723346, 1924510689,
            1925356265
        ],
    },
    {
        'title': 'Lies of P',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1627720/header.jpg',
        'vod_ids': [
            1929673569, 1930558585, 1931371937, 1932267758, 1933229708, 1934187838, 1934972121, 1935764322
        ],
    },
    {
        'title': 'Super Mario Wonder',
        'img_link': 'img/smw.png',
        'vod_ids': [
            1957672670,
        ],
    },
    {
        'title': 'Alan Wake + DLC + Control AWE',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/108710/header.jpg',
        'vod_ids': [
            1958415752, 1959217074, 1960034859, 1960856449,
        ],
    },
    {
        'title': 'Alan Wake 2',
        'img_link': 'https://cdn2.steamgriddb.com/file/sgdb-cdn/grid/b803d6d724c2136e8b36139dc81a40a3.png',
        'vod_ids': [
            1961674070, 1962623297, 1964201193, 1965004435, 1965872956, 1966706692,
        ],
    },
    {
        'title': 'Slay the Princess',
        'img_link': 'https://cdn.akamai.steamstatic.com/steam/apps/1989270/header.jpg',
        'vod_ids': [
            1969546347, 1969746385,
        ],
    },
    {
        'title': 'JADSEYA 2023 Award Nominees',
        'img_link': 'img/Special Events.jpg',
        'vod_ids': [
            1988746682
        ],
    },
    {
        'title': 'VA-11 HALL-A',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/447530/header.jpg',
        'vod_ids': [
            1989601616, 1990465388, 1991334745, 1992207436,
        ],
    },
    {
        'title': 'JADSEYA Propaganda & Game Awards 2023',
        'img_link': 'img/Special Events.jpg',
        'vod_ids': [
            1997957948
        ],
    },
    {
        'title': 'JADSEYA 2023',
        'img_link': 'img/Special Events.jpg',
        'vod_ids': [
            2017302012
        ],
    },
    {
        'title': 'Umineko When They Cry (Leap Year Edition)',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/406550/header.jpg',
        'vod_ids': [
            2077161325
        ],
    },
    {
        'title': 'Shadow of the Erdtree video Q&A and commentary',
        'img_link': 'img/Special Events.jpg',
        'vod_ids': [
            2237962533
        ],
    },
    {
        'title': 'Game Awards 2024 & Balatro',
        'img_link': 'img/Special Events.jpg',
        'vod_ids': [
            2325223421
        ],
    },
    {
        'title': 'Balatro',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/2379780/header.jpg',
        'vod_ids': [
            2326166483, 2329682240, 2330524316, 2331333771, 2332203317, 2352078566
        ],
    },
    {
        'title': 'Life is Strange: Double Exposure',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1874000/header.jpg',
        'vod_ids': [
            2328863720, 2329682240, 2330524316, 2331333771, 2332203317
        ],
    },
    {
        'title': 'Astro Bot',
        'img_link': 'https://cdn2.steamgriddb.com/grid/f393749d5f16cae0e767e42fc860f237.png',
        'vod_ids': [
            2334193562, 2335037686, 2336457067, 2337288843
        ],
    },
    {
        'title': 'Nine Sols',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1809540/header.jpg',
        'vod_ids': [
            2339051331, 2339898771, 2340755980, 2346087608, 2352078566
        ],
    },
    {
        'title': 'Persona 3 Reload',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/2161700/header.jpg',
        'vod_ids': [
            2341522598, 2342366201, 2343269538, 2346898155, 2347760477, 2348652676, 2349550751, 2353219656, 2354113268, 2355005141,
            2355861846, 2359616716, 2360545573, 2361429975, 2362341293, 2366024434, 2366924318, 2367817605
        ],
    },
    {
        'title': 'Umineko When They Cry',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/406550/header.jpg',
        'vod_ids': [
            2350517708, 2356841248, 2363320345, 2368739807, 2369654143
        ],
    },
    # {
    #     'title': '',
    #     'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps//header.jpg',
    #     'vod_ids': [

    #     ],
    # },
]
data = data[::-1]

import re
import datetime

for game in data:
    vids = list()
    for vid in game['vod_ids']:
        match vid:
            case (vid, timestamp):
                m = re.match(r'(\d+)h(\d+)m(\d+)s', timestamp)
                time_parts = tuple(int(g) for g in m.groups())
                t = datetime.timedelta(hours=time_parts[0], minutes=time_parts[1], seconds=time_parts[2]).seconds
                vids.append({'type':'local', 'id': str(vid), 't': t})

            case int():
                vids.append({'type':'local', 'id': str(vid)})
            case str():
                vids.append({'type':'yt', 'id': f'https://www.youtube.com/watch?v={vid}'})
            case _:
                raise RuntimeError('wtf')
            # TODO peertube

    game['vod_ids'] = vids


with open('web_test/games_info.json', 'w') as f:
    json.dump(data, f)
