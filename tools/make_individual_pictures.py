"""Gives every bird and plant in the three built-in examples its own sample picture (cartoon illustrations tagged SAMPLE IMAGE),
so lists, cards and detail pages are never blank in a demo or video.
Run AFTER make_examples.py and make_example_media.py. Re-runnable: everything added here has an id starting 'exi-' and is replaced each run.
Usage: python3 tools/make_individual_pictures.py"""
import json, os, re, zlib
import example_art2 as B

HERE = os.path.dirname(os.path.abspath(__file__)); EX = os.path.join(HERE, '..', 'examples')
seed_of = lambda s: zlib.crc32(s.encode()) % 100000

def load(name):
    path = os.path.join(EX, f'{name}-example.json'); d = json.load(open(path))
    d['photos'] = [p for p in d.get('photos', []) if not p['id'].startswith('exi-')]
    for r in d['records']:
        if r.get('photoIds'): r['photoIds'] = [p for p in r['photoIds'] if not p.startswith('exi-')]
        if r.get('photoTags'): r['photoTags'] = {k: v for k, v in r['photoTags'].items() if not k.startswith('exi-')}
        if 'photoTags' in r and not r['photoTags']: del r['photoTags']
    return path, d

def put(d, rec, img, label):
    pid = 'exi-' + rec['id']
    full, thumb = B.save_small(img)
    d['photos'].append({'id': pid, 'full': full, 'thumb': thumb})
    rec['photoIds'] = [pid] + [p for p in rec.get('photoIds', []) if p != pid]
    rec.setdefault('photoTags', {})[pid] = label

def save(path, d):
    json.dump(d, open(path, 'w'), indent=1, ensure_ascii=False)
    print(os.path.basename(path), len(d['records']), 'records,', len(d['photos']), 'pictures,', round(os.path.getsize(path) / 1024), 'KB')

BANDGEN = lambda g: 'BC' if (g or '').startswith('BC') else 'X' if g == 'Outcross' else g if g in ('P', 'F1', 'F2', 'F3') else 'P'

# ---------------------------------------------------------------- Blue Australorp laying line
def animals():
    path, d = load('animals')
    for r in d['records']:
        if r['type'] != 'individual': continue
        desc = (r.get('description') or '').lower(); sex = 'M' if r.get('sex') == 'Male' else 'F'; s = seed_of(r['id'])
        col = 'splash' if 'splash' in desc else 'blue' if 'blue' in desc else 'black' if 'black' in desc else None
        if r.get('strainId') == 'exa-s-blue': col = 'blue'
        if r.get('strainId') == 'exa-s-black': col = 'black'
        col = col or 'black'
        if 'chick' in desc:
            put(d, r, B.img_chicks(1, col, s), 'young')
        elif 'cockerel' in desc or 'pullet' in desc:
            put(d, r, B.img_bird(col, sex, 'young', s, BANDGEN(r.get('generation'))), 'young')
        else:
            put(d, r, B.img_bird(col, sex, 'adult', s, 'P'), 'adult')
    save(path, d)

# ---------------------------------------------------------------- Olive Egger line
def olive():
    path, d = load('olive')
    strain_pal = {'exo-s-ara': 'araucana', 'exo-s-wel': 'welsummer', 'exo-s-mar': 'maran', 'exo-s-aus': 'black'}
    for r in d['records']:
        if r['type'] != 'individual': continue
        i = r['id']; sex = 'M' if r.get('sex') == 'Male' else 'F'; s = seed_of(i); gen = BANDGEN(r.get('generation'))
        if i == 'exo-g-flock': continue                                   # keeps its flock picture
        if i == 'exo-g-k4': put(d, r, B.img_chicks(5, 'olive', s), 'young'); continue
        if r.get('isGroup'):
            put(d, r, B.img_group(['oliveW', 'oliveM', 'oliveW'], ['F', 'F', 'F'], s), 'group'); continue
        if r.get('strainId') in strain_pal:
            pal = strain_pal[r['strainId']]; put(d, r, B.img_bird(pal, sex, 'adult', s, 'P', tuft=(pal == 'araucana')), 'adult'); continue
        pal = 'oliveW' if i.startswith('exo-w') else 'oliveM' if i.startswith('exo-m') else 'backcross'
        put(d, r, B.img_bird(pal, sex, 'young' if gen == 'BC' else 'adult', s, gen), 'young' if gen == 'BC' else 'adult')
    save(path, d)

# ---------------------------------------------------------------- Pantry Keeper squash
def kind_of(code):
    if code.startswith('PK-X'): return 'hybrid'
    if code.startswith(('PK-TR', 'T-')): return 'tromboncino'
    if code.startswith('PK-WB'): return 'butternut'
    if code.startswith('PK-BC'): return 'buttercup'
    return 'cheese'

def plants():
    path, d = load('plants'); active = 0
    for r in d['records']:
        if r['type'] != 'individual': continue
        i, code, st = r['id'], r.get('code') or '', r.get('status') or ''; s = seed_of(i)
        if i == 'exp-v19-grp': put(d, r, B.img_mix_border(s), 'growing'); continue
        kd = kind_of(code)
        if st == 'Culled': put(d, r, B.img_plant(kd, 'weak', s, code, 'culled', 1), 'fruit')
        elif st in ('Selected', 'Kept for breeding'): put(d, r, B.img_plant(kd, 'fruit', s, code, 'selected', 3), 'fruit')
        elif st == 'Active':
            stage = ['growing', 'flower', 'seedling'][active % 3]; active += 1
            put(d, r, B.img_plant(kd, stage, s, code, 'plain'), {'growing': 'growing', 'flower': 'flower', 'seedling': 'seedling'}[stage])
        else: put(d, r, B.img_plant(kd, 'fruit', s, code, 'plain', 2 + s % 2), 'fruit')
    save(path, d)

if __name__ == '__main__':
    animals(); olive(); plants()
