import json,hashlib,pathlib,sys
r=pathlib.Path(__file__).parent
def load(p):return json.loads((r/p).read_text(encoding='utf8'))
m=load('manifest.json');c=load('catalog.json');s=load('sources.json')
assert m['schemaVersion']==1 and c['schemaVersion']==1
ids=[g['id'] for g in c['games']];assert len(ids)==len(set(ids))
for p,meta in m['files'].items():
 raw=(r/p).read_bytes();assert hashlib.sha256(raw).hexdigest()==meta['sha256'],p
sourceIds={x['id'] for x in s['sources']};total=0
for g in c['games']:
 assert g['dataFile']==m['gameFiles'][g['id']]
 assert (r/g['localIconAsset']).exists() and (r/g['localCoverAsset']).exists()
 for key in ['iconUrl','coverImageUrl']:
  assert g[key] is None or g[key].startswith('https://')
 d=load(g['dataFile']);assert d['gameId']==g['id'];cheatIds=set()
 for cheat in d['cheats']:
  assert cheat['id'] not in cheatIds;cheatIds.add(cheat['id']);total+=1
  assert set(cheat['verification'].get('sourceIds',[]))<=sourceIds
  for item in cheat.get('inputs',[]):assert set(item['platformIds'])<=set(g['supportedPlatformIds'])
print(f'PASS: {len(ids)} games, {total} sample cheat entries, {len(sourceIds)} sources, assets and hashes checked')
