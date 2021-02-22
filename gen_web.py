page_template = '''<!DOCTYPE html>
<html>

<head>
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
  <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
  <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
</head>

<body>
  <!-- Always shows a header, even in smaller screens. -->
  <div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">
    <header class="mdl-layout__header">
      <div class="mdl-layout__header-row">
        <span class="mdl-layout-title">JOE VODS</span>
        <div class="mdl-layout-spacer"></div>
        <nav class="mdl-navigation mdl-layout--large-screen-only">
          <a class="mdl-navigation__link" href="">TODO</a>
        </nav>
      </div>
    </header>

    <main class="mdl-layout__content">
      <div class="page-content">
        <div class="mdl-grid">
          {cells}
        </div>
      </div>
    </main>
  </div>
</body>
</html>
'''

cell_template = '''
          <div class="mdl-cell mdl-cell--2-col">
            <div class="demo-card-square mdl-card mdl-shadow--2dp">
              <div class="mdl-card__media"><img src="{img_link}" width="100%"></div>
              <div class="mdl-card__title"><h2 class="mdl-card__title-text">{title}</h2></div>
              <div class="mdl-card__supporting-text">{links}
              </div>
            </div>
          </div>'''

link_template = '''
                <span class="mdl-chip"><span class="mdl-chip__text"><a href="vod_test.html?vod={vod_id}">Part {n}</a></span></span>'''

data = [

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
        'title': 'Special: Voting Game (Marbles on Stream)',
        'img_link': 'https://cdn.cloudflare.steamstatic.com/steam/apps/1170970/header.jpg',
        'vod_ids': [914269565, 916562698],
    },


]


cells = []
for game in data:
    game['links'] = ''.join(link_template.format(vod_id=vod_id, n=n) for n, vod_id in enumerate(game['vod_ids'], start=1))
    cells.append(cell_template.format(**game))

cells = ''.join(reversed(cells))

with open('web_test/index_test.html', 'w') as f:
    f.write(page_template.format(cells=cells))
