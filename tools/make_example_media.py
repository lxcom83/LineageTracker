"""Adds sample pictures (illustrations, tagged SAMPLE IMAGE), photo labels, packet front/back photos,
an unlinked Log note, and a Breeding plan to the three built-in examples.
Run AFTER tools/make_examples.py (that script rewrites two of the files). Re-runnable: everything added here
uses ids starting 'exm-' and is replaced on each run.   Usage: python3 tools/make_example_media.py"""
import json, os, time
import example_art as A

HERE = os.path.dirname(os.path.abspath(__file__)); EX = os.path.join(HERE, '..', 'examples')
LOCK = 1791560025210   # any timestamp: when a plan box was locked in

class Ex:
    def __init__(self, name):
        self.path = os.path.join(EX, f'{name}-example.json'); self.d = json.load(open(self.path))
        self.recs = {r['id']: r for r in self.d['records'] if not r['id'].startswith('exm-')}
        self.photos = []
        for r in self.recs.values():           # clear anything this script added earlier
            if r.get('photoIds'): r['photoIds'] = [p for p in r['photoIds'] if not p.startswith('exm-')]
            if r.get('photoTags'): r['photoTags'] = {k: v for k, v in r['photoTags'].items() if not k.startswith('exm-')}
            if 'photoTags' in r and not r['photoTags']: del r['photoTags']
        self.new = []
    def photo(self, pid, img):
        if not any(p['id'] == pid for p in self.photos):
            full, thumb = A.save_pair(img); self.photos.append({'id': pid, 'full': full, 'thumb': thumb})
        return pid
    def attach(self, rid, pid, label):
        r = self.recs.get(rid) or next(x for x in self.new if x['id'] == rid)
        r.setdefault('photoIds', []).append(pid); r.setdefault('photoTags', {})[pid] = label
    def note(self, nid, ref, date, text, pics=()):
        r = {'id': 'exm-' + nid, 'type': 'note', 'refId': ref, 'date': date, 'text': text, 'photoIds': []}; self.new.append(r)
        for pid, label in pics: self.attach(r['id'], pid, label)
        return r
    def setplan(self, pid, plan): self.recs[pid]['plan'] = plan
    def link(self, cross_id, edge_id): self.recs[cross_id]['planEdge'] = edge_id
    def save(self):
        self.d['records'] = list(self.recs.values()) + self.new
        self.d['photos'] = [p for p in self.d.get('photos', []) if not p['id'].startswith('exm-')] + self.photos
        json.dump(self.d, open(self.path, 'w'), indent=1, ensure_ascii=False)
        print(os.path.basename(self.path), len(self.d['records']), 'records,', len(self.photos), 'pictures,', round(os.path.getsize(self.path) / 1024), 'KB')

def node(i, per, kind, label='', ref='', qty=0, via=''):
    n = {'id': i, 'periodId': per, 'kind': kind, 'label': label}
    if ref: n['refId'] = ref; n['lockedAt'] = LOCK
    if qty: n['qty'] = qty
    if via: n['via'] = via
    return n
def edge(i, kind, a, b, d='one', per='', via='', bend=0, note=''):
    e = {'id': i, 'kind': kind, 'from': a, 'to': b, 'note': note, 'bend': bend}
    if kind == 'cross': e['dir'] = d
    if per: e['periodId'] = per
    if via: e['via'] = via
    return e

# ================================================================== PLANT EXAMPLE (Pantry Keeper squash)
def plants():
    x = Ex('plants')
    fr = {k: x.photo('exm-pk-fruit-' + k, A.img_fruit(kd)) for k, kd in [('wb', 'butternut'), ('li', 'cheese'), ('tr', 'tromboncino'), ('bc', 'buttercup')]}
    for sid, k in [('exp-s-wb', 'wb'), ('exp-s-li', 'li'), ('exp-s-tr', 'tr'), ('exp-s-bc', 'bc')]: x.attach(sid, fr[k], 'fruit')
    for lot, nm, sp, kd, col, b in [('exp-l-wb', 'Waltham Butternut', 'Cucurbita moschata', 'butternut', (214, 130, 54), 'ES-4471'), ('exp-l-li', 'Long Island Cheese', 'Cucurbita moschata', 'cheese', (176, 120, 70), 'HS-0912'),
                                    ('exp-l-tr', 'Tromboncino', 'Cucurbita moschata', 'tromboncino', (120, 150, 80), 'HS-2210'), ('exp-l-bc', 'Buttercup', 'Cucurbita maxima', 'buttercup', (62, 110, 84), 'ES-8830')]:
        brand = 'EXAMPLE SEEDS CO' if lot in ('exp-l-wb', 'exp-l-bc') else 'HERITAGE SEED SWAP'
        x.attach(lot, x.photo(f'exm-pk-{lot[-2:]}-front', A.img_packet(True, nm, sp, kd, brand, col, b)), 'packet-front')
        x.attach(lot, x.photo(f'exm-pk-{lot[-2:]}-back', A.img_packet(False, nm, sp, kd, brand, col, b)), 'packet-back')
    bed = x.photo('exm-pk-bed', A.img_bed())
    x.attach('exp-pl-rb1', bed, 'place')
    x.attach('exp-n5', fr['wb'], 'fruit')                                   # F1 fruit
    x.attach('exp-n6', x.photo('exm-pk-cut', A.img_cutopen()), 'cutopen')   # best fruit of the season
    x.attach('exp-n4', x.photo('exm-pk-harvest', A.img_harvest()), 'harvest')
    x.attach('exp-n2', fr['tr'], 'fruit')
    x.note('pk-seedl', 'exp-p', '2026-09-12', 'Potted up the combined-line seedlings, 12 to a tray, tagged PK-X. Four cells empty: those seeds did not come up.', [(x.photo('exm-pk-seedl', A.img_seedlings()), 'seedling')])
    x.note('pk-flower', 'exp-i-lf2-p03', '2025-12-27', 'First female flower on Shed Queen. Hand-pollinate tomorrow morning.', [(x.photo('exm-pk-flower', A.img_flower()), 'flower')])
    x.note('pk-log', '', '2026-09-28', 'Front garden is filling out. First fruit set on the mound row. Shared for the club newsletter.', [(bed, 'growing')])   # not linked to anything: can be shared from the Log
    # ---- Breeding plan on the Pantry Keeper project
    per = [{'id': 'y1', 'name': 'Founders', 'span': '1 year'}, {'id': 'y2', 'name': 'F1 and selfing', 'span': '1 year'}, {'id': 'y3', 'name': 'F2 selection', 'span': '1 year'},
           {'id': 'y4', 'name': 'Combine the lines', 'span': '1 year'}, {'id': 'y5', 'name': 'Bring it back', 'span': '1 year'}]
    N = [node('n1', 'y1', 'plant', 'Waltham Butternut', 'exp-i-wb1'), node('n2', 'y1', 'plant', 'Long Island Cheese', 'exp-i-li1'), node('n3', 'y1', 'plant', 'Tromboncino', 'exp-i-tr1'),
         node('n4', 'y2', 'plant', 'Line LI, F1', 'exp-i-lf1', via='e1'), node('n5', 'y2', 'plant', 'Line T, F1', 'exp-i-tf1', via='e2'),
         node('n6', 'y3', 'plant', 'Shed Queen', 'exp-i-lf2-p03', via='e3'), node('n7', 'y3', 'plant', 'Gem', 'exp-i-lf2-p07', via='e3'), node('n8', 'y3', 'plant', 'Best Line T vine', 'exp-i-tf2-p02', via='e4'),
         node('n9', 'y4', 'plant', 'Combined line', 'exp-i-cb-1', via='e5'), node('n10', 'y4', 'plant', 'Line LI, F3', 'exp-i-lf3-1', via='e6'),
         node('n11', 'y5', 'plant', 'Bring-back plants', qty=12, via='e7'), node('n12', 'y5', 'plant', 'Best vine A'), node('n13', 'y5', 'plant', 'Best vine B'), node('n14', 'y5', 'group', 'Isolation block for the saved seed')]
    E_ = [edge('e1', 'cross', 'n1', 'n2', 'one', 'y1'), edge('e2', 'cross', 'n1', 'n3', 'one', 'y1'),
          edge('g1', 'grow', 'n1', 'n4', via='e1'), edge('g2', 'grow', 'n1', 'n5', via='e2'),
          edge('e3', 'cross', 'n4', 'n4', 'self', 'y2'), edge('e4', 'cross', 'n5', 'n5', 'self', 'y2'),
          edge('g3', 'grow', 'n4', 'n6', via='e3'), edge('g4', 'grow', 'n4', 'n7', via='e3'), edge('g5', 'grow', 'n5', 'n8', via='e4'),
          edge('e5', 'cross', 'n6', 'n8', 'one', 'y3', bend=1), edge('e6', 'cross', 'n7', 'n7', 'self', 'y3'),
          edge('g6', 'grow', 'n6', 'n9', via='e5'), edge('g7', 'grow', 'n7', 'n10', via='e6'),
          edge('e7', 'cross', 'n10', 'n9', 'one', 'y4'), edge('g8', 'grow', 'n10', 'n11', via='e7'),
          edge('e8', 'cross', 'n12', 'n13', 'two', 'y5', note='Hand-pollinate both ways'), edge('r1', 'release', 'n13', 'n14')]
    x.setplan('exp-p', {'v': 1, 'periods': per, 'nodes': N, 'edges': E_})
    for c, e in [('exp-c1', 'e1'), ('exp-c2', 'e2'), ('exp-c4', 'e3'), ('exp-c5', 'e4'), ('exp-c6', 'e5'), ('exp-c7', 'e6'), ('exp-v19-cx', 'e7')]: x.link(c, e)
    x.save()

# ================================================================== CHICKEN EXAMPLE (Blue Australorp laying line)
def animals():
    x = Ex('animals')
    hb, hk = x.photo('exm-ba-hen-blue', A.img_hen('blue', -1)), x.photo('exm-ba-hen-black', A.img_hen('black', 1))
    x.attach('exa-s-blue', hb, 'adult'); x.attach('exa-s-black', hk, 'adult')
    x.attach('exa-pl-coop', x.photo('exm-ba-coop', A.img_coop()), 'place'); x.attach('exa-pl-pen', x.photo('exm-ba-pen', A.img_pen()), 'place')
    x.attach('exa-n1', hk, 'adult')
    flock = x.photo('exm-ba-flock', A.img_flock())
    x.attach('exa-n2', flock, 'group')
    x.note('ba-chick', 'exa-f1-a03', '2024-10-02', 'Day 2. Fluffy, dark with a pale chest: blue-splash likely.', [(x.photo('exm-ba-chick', A.img_chick((236, 200, 90))), 'young')])
    x.note('ba-eggs', 'exa-p', '2026-03-05', 'First eggs from the F2 pullets. Small, tinted brown, four of the six from Selected birds.', [(x.photo('exm-ba-eggs', A.img_eggs(((178, 120, 76), (190, 130, 84), (170, 112, 70), (186, 126, 80), (174, 116, 72), (182, 124, 78)))), 'eggs')])
    x.note('ba-log', '', '2026-09-10', 'The whole flock out on the grass this afternoon. Shared with the poultry club.', [(flock, 'group')])
    per = [{'id': 'g0', 'name': 'Founders', 'span': '1 year'}, {'id': 'g1', 'name': 'F1', 'span': '1 year'}, {'id': 'g2', 'name': 'F2 and outcross', 'span': '1 year'}, {'id': 'g3', 'name': 'Next season', 'span': '1 year'}]
    N = [node('n1', 'g0', 'animal', 'Arthur (Black rooster)', 'exa-r1'), node('n2', 'g0', 'animal', 'Bluebell (Blue hen)', 'exa-h1'), node('n3', 'g0', 'animal', 'Sky (Blue hen)', 'exa-h2'),
         node('n4', 'g1', 'animal', 'F1 hen A04', 'exa-f1-a04', via='e1'), node('n5', 'g1', 'animal', 'F1 cockerel A02', 'exa-f1-a02', via='e1'), node('n6', 'g1', 'animal', 'F1 hen A05', 'exa-f1-a05', via='e1'),
         node('n7', 'g2', 'animal', 'F2 hen A01', 'exa-f2-a01', via='e3'), node('n8', 'g2', 'animal', 'Duke (new rooster)', 'exa-r2'), node('n9', 'g2', 'animal', 'Outcross pullet', 'exa-x-1', via='e4'),
         node('n10', 'g3', 'animal', 'Chicks from the outcross hens', qty=10, via='e5'), node('n11', 'g3', 'animal', 'Unrelated Blue rooster, still to find'), node('n12', 'g3', 'group', 'Laying coop')]
    E_ = [edge('e1', 'cross', 'n2', 'n1', 'one', 'g0'), edge('e2', 'cross', 'n3', 'n1', 'one', 'g0'),
          edge('g1', 'grow', 'n2', 'n4', via='e1'), edge('g2', 'grow', 'n2', 'n5', via='e1'), edge('g3', 'grow', 'n2', 'n6', via='e1'),
          edge('e3', 'cross', 'n4', 'n5', 'one', 'g1'), edge('g4', 'grow', 'n4', 'n7', via='e3'),
          edge('e4', 'cross', 'n6', 'n8', 'one', 'g2', bend=1), edge('g5', 'grow', 'n6', 'n9', via='e4'),
          edge('e5', 'cross', 'n9', 'n11', 'one', 'g2', note='Keep the Blue gene without more inbreeding'), edge('g6', 'grow', 'n9', 'n10', via='e5'), edge('r1', 'release', 'n10', 'n12')]
    x.setplan('exa-p', {'v': 1, 'periods': per, 'nodes': N, 'edges': E_})
    for c, e in [('exa-c1', 'e1'), ('exa-c2', 'e2'), ('exa-c3', 'e3'), ('exa-c4', 'e4')]: x.link(c, e)
    x.save()

# ================================================================== BREEDING EXAMPLE (Olive Egger line)
def olive():
    x = Ex('olive')
    x.attach('exo-s-ara', x.photo('exm-oe-ara', A.img_hen('blue', 1)), 'adult'); x.attach('exo-s-wel', x.photo('exm-oe-wel', A.img_hen('brown', -1)), 'adult')
    x.attach('exo-s-mar', x.photo('exm-oe-mar', A.img_hen('black', 1)), 'adult'); x.attach('exo-s-aus', x.photo('exm-oe-aus', A.img_hen('black', -1)), 'adult')
    x.attach('exo-pl-coop', x.photo('exm-oe-coop', A.img_coop()), 'place')
    x.attach('exo-n2', x.photo('exm-oe-egg1', A.img_eggs(((150, 160, 100), (146, 156, 96), (154, 164, 104), (148, 158, 98), (152, 162, 102), (144, 154, 94)))), 'eggs')
    x.attach('exo-n3', x.photo('exm-oe-egg2', A.img_eggs(((118, 112, 60), (124, 118, 66), (114, 108, 56), (120, 114, 62), (116, 110, 58), (122, 116, 64)))), 'eggs')
    x.attach('exo-n4', x.photo('exm-oe-chick', A.img_chick((226, 190, 90))), 'young')
    x.note('oe-rainbow', 'exo-p', '2026-04-02', 'Egg colours side by side: Araucana blue, Welsummer brown, and the F1 olive in the middle.', [(x.photo('exm-oe-mix', A.img_eggs(((120, 190, 190), (150, 160, 100), (176, 112, 68), (118, 112, 60), (120, 190, 190), (176, 112, 68)))), 'eggs')])
    x.note('oe-flock', 'exo-g-flock', '2026-09-05', 'The laying flock, all lines together.', [(x.photo('exm-oe-flock', A.img_flock(('blue', 'black', 'brown', 'blue', 'black'))), 'group')])
    x.note('oe-log', '', '2026-09-22', 'Backcross chicks are three weeks old and feathering well. Shared for the club page.', [('exm-oe-chick', 'young')])
    per = [{'id': 'p0', 'name': 'Founders', 'span': '1 year'}, {'id': 'p1', 'name': 'First hatch (F1)', 'span': '1 year'}, {'id': 'p2', 'name': 'Second crosses', 'span': '1 year'}, {'id': 'p3', 'name': 'Next hatch', 'span': '6 months'}]
    N = [node('n1', 'p0', 'animal', 'Juniper (Araucana)', 'exo-h1'), node('n2', 'p0', 'animal', 'Basil (Welsummer)', 'exo-r1'), node('n3', 'p0', 'animal', 'Sage (Araucana)', 'exo-h2'), node('n4', 'p0', 'animal', 'Copper (Maran)', 'exo-r2'),
         node('n5', 'p1', 'animal', 'Olive (Line W)', 'exo-w1', via='e1'), node('n6', 'p1', 'animal', 'Fern (Line W)', 'exo-w2', via='e1'), node('n7', 'p1', 'animal', 'Moss (Line M)', 'exo-m1', via='e2'), node('n8', 'p1', 'animal', 'Bramble (Line M)', 'exo-m3', via='e2'),
         node('n9', 'p2', 'animal', '26C-1 chicks (W x M)', 'exo-g-k4', via='e3'), node('n10', 'p2', 'animal', 'Backcross chicks', 'exo-b1', via='e4'), node('n11', 'p2', 'animal', 'Oscar (new rooster)', 'exo-r3'),
         node('n12', 'p3', 'animal', 'Chicks from 26C-3', qty=10, via='e5'), node('n13', 'p3', 'group', 'Grow-out run')]
    E_ = [edge('e1', 'cross', 'n1', 'n2', 'one', 'p0'), edge('e2', 'cross', 'n3', 'n4', 'one', 'p0'),
          edge('g1', 'grow', 'n1', 'n5', via='e1'), edge('g2', 'grow', 'n1', 'n6', via='e1'), edge('g3', 'grow', 'n3', 'n7', via='e2'), edge('g4', 'grow', 'n3', 'n8', via='e2'),
          edge('e3', 'cross', 'n5', 'n8', 'one', 'p1'), edge('e4', 'cross', 'n7', 'n4', 'one', 'p1', bend=1, note='Backcross to the Maran'),
          edge('g5', 'grow', 'n5', 'n9', via='e3'), edge('g6', 'grow', 'n7', 'n10', via='e4'),
          edge('e5', 'cross', 'n6', 'n11', 'one', 'p2', note='Outcross to widen the gene pool'), edge('g7', 'grow', 'n6', 'n12', via='e5'), edge('r1', 'release', 'n12', 'n13')]
    x.setplan('exo-p', {'v': 1, 'periods': per, 'nodes': N, 'edges': E_})
    for c, e in [('exo-c1', 'e1'), ('exo-c2', 'e2'), ('exo-c4', 'e3'), ('exo-c5', 'e4'), ('exo-c6', 'e5')]: x.link(c, e)
    x.save()

if __name__ == '__main__':
    plants(); animals(); olive()
