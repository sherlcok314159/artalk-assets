import json
from pathlib import Path

emoji_name = 'gancheng'
prefix_url = 'https://cdn.jsdelivr.net/gh/sherlcok314159/artalk-assets@main/'
emoji_dir = Path(emoji_name)

items = []
for emoji_path in emoji_dir.glob('*'):
    name = emoji_path.stem
    emoji_path = str(emoji_path).replace('\\', '/')
    cdn_url = prefix_url + emoji_path
    items.append({'key': name, 'val': cdn_url})

with open(f'{emoji_name}.json', 'w') as w:
    w.write(json.dumps({'name': emoji_name, 'type': 'image', 'items': items}))
