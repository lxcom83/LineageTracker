"""Builds examples/pigs-example.json: a small Kunekune herd on pasture (invented: every name, number and company is made up).
Pictures are cartoon illustrations tagged SAMPLE IMAGE (tools/example_art3.py), so nothing needs licensing.
Re-runnable.  Usage: python3 tools/make_pig_example.py"""
import json, os
import example_art as A, example_art2 as B, example_art3 as G

HERE = os.path.dirname(os.path.abspath(__file__)); EX = os.path.join(HERE, '..', 'examples')
ANCHOR = '2026-10-01'; LOCK = 1791560025210
SP = 'Sus scrofa domesticus'; GRP = 'Pig'
R, PH = [], []
def add(**r): R.append(r); return r
def photo(pid, img):
    if not any(p['id'] == pid for p in PH):
        full, thumb = B.save_small(img); PH.append({'id': pid, 'full': full, 'thumb': thumb})
    return pid
def attach(rid, pid, label):
    r = next(x for x in R if x['id'] == rid); r.setdefault('photoIds', []).append(pid); r.setdefault('photoTags', {})[pid] = label

# ------------------------------------------------------------------ strains, places, site
for sid, name, desc in [('exk-s-gin', 'Ginger Kunekune', 'Ginger to gold coat, long tassels, very placid. Grows well on grass alone.'),
                        ('exk-s-blk', 'Black Kunekune', 'Solid black, hardy and thrifty. Good mothers.'),
                        ('exk-s-bw', 'Black-and-white Kunekune', 'Black with a white belt or patches. Coat colour is the easy way to spot who is whose.')]:
    add(id=sid, type='strain', name=name, kind='animal', group=GRP, species=SP, speciesVerified=True, origin='Example Heritage Pigs', description=desc, photoIds=[])
for pid, name, method, details in [('exk-pl-farrow', 'Farrowing hut', 'Hut', 'Dry hut with a rail so piglets cannot be squashed. Sows go in five days before they are due.'),
                                   ('exk-pl-r1', 'Sow paddock 1', 'Paddock', 'Grass paddock, rotated every six weeks.'),
                                   ('exk-pl-r2', 'Sow paddock 2', 'Paddock', 'Resting. Lime and reseed after the last rotation.'),
                                   ('exk-pl-boar', 'Boar pen', 'Pen', 'Strong fence, shade and a wallow. Two boars, side by side, never together.'),
                                   ('exk-pl-wean', 'Weaner paddock', 'Paddock', 'Weaned piglets from eight weeks until they go or move up.'),
                                   ('exk-pl-orch', 'Orchard run', 'Paddock', 'Windfall apples and shade. Gate stays shut in winter to protect the roots.')]:
    add(id=pid, type='place', name=name, kind='animal', method=method, details=details, photoIds=[])
add(id='exk-site', type='site', name='Example smallholding', lat=-34.47, lon=150.42, locLabel='Southern Highlands, NSW (example)', seasonStart=7, heat=32, frost=0, gddBase=10, manual=False, manualMode='regional')

# ------------------------------------------------------------------ record types, traits, projects
RT = [
 {'id': 'exk-rt-w', 'tplKey': 'weigh', 'name': 'Weigh-in', 'itemName': '', 'parentRt': '', 'fields': [
   {'id': 'exk-rt-w-f0', 'label': 'Weight', 'type': 'number', 'unit': 'kg', 'agg': 'latest', 'compare': True},
   {'id': 'exk-rt-w-f1', 'label': 'Body condition', 'type': 'score', 'agg': 'latest', 'compare': True}], 'repeatDays': 30},
 {'id': 'exk-rt-l', 'tplKey': 'litter', 'name': 'Litter record', 'itemName': 'Litter', 'parentRt': '', 'fields': [
   {'id': 'exk-rt-l-f0', 'label': 'Litter size', 'type': 'number', 'agg': 'avg', 'compare': True},
   {'id': 'exk-rt-l-f1', 'label': 'Born alive', 'type': 'number', 'agg': 'avg', 'compare': True},
   {'id': 'exk-rt-l-f2', 'label': 'Survival rate', 'type': 'calc', 'unit': '%', 'formula': '{Born alive} / {Litter size} * 100', 'agg': 'avg', 'compare': True},
   {'id': 'exk-rt-l-f3', 'label': 'Raised to weaning', 'type': 'number', 'agg': 'avg'}]},
]
TRAITS = [{'name': 'Mothering ability', 'tier': 1, 'must': True, 'def': '1 = restless or crushes piglets, 5 = calm, good milk, loses none.'},
          {'name': 'Temperament', 'tier': 1, 'must': False, 'def': '1 = nervous or pushy, 5 = placid and easy to handle.'},
          {'name': 'Grazing', 'tier': 2, 'must': False, 'def': '1 = needs a lot of extra feed, 5 = holds condition on grass alone.'},
          {'name': 'Conformation', 'tier': 2, 'must': False, 'def': 'Short upturned snout, tassels, sturdy legs. 1 = poor, 5 = excellent.'}]
GOAL = 'A placid, grass-fed Kunekune herd for the family table and a few weaners each year: good mothers, little extra feed, and colours kept apart so every pig can be traced. Example project: everything here is made up.'
add(id='exk-p', type='project', name='Kunekune herd', code='KK', kind='animal', species=SP, parentId='', goal=GOAL, strainIds=['exk-s-gin', 'exk-s-blk', 'exk-s-bw'], traits=TRAITS, recordTypes=RT,
    goals=[{'v': 1, 'date': '2025-05-01', 'statement': GOAL, 'why': 'Starting the herd.'}], goalReviewMonths=18, siteId='exk-site', tagStyle={'preset': 'animal'}, photoIds=[])
add(id='exk-p-g', type='project', name='Ginger line', code='G', kind='animal', species=SP, parentId='exk-p', goal='Keep the ginger colour and the gentle nature.', strainIds=['exk-s-gin'], traits=TRAITS, recordTypes=[], goals=[], photoIds=[])
add(id='exk-p-b', type='project', name='Black line', code='B', kind='animal', species=SP, parentId='exk-p', goal='The hardiest mothers, from the black sows.', strainIds=['exk-s-blk'], traits=TRAITS, recordTypes=[], goals=[], photoIds=[])

# ------------------------------------------------------------------ pigs
def pigrec(id, code, name, strain, sex, place, start, status='Kept for breeding', gen='P', proj='exk-p', mother='', father='', cross='', clutch='', scores=None, selection=None, desc=''):
    return add(id=id, type='individual', code=code, name=name, strainId=strain, projectId=proj, generation=gen, sex=sex, motherId=mother, fatherId=father, stockId='', startDate=start, status=status, placeId=place, crossId=cross, clutchId=clutch, description=desc, scores=scores or {}, selection=selection, photoIds=[])
pigrec('exk-h1', 'KK-24-01', 'Poppy', 'exk-s-gin', 'Female', 'exk-pl-r1', '2024-05-10', proj='exk-p-g', scores={'Mothering ability': 5, 'Temperament': 5, 'Grazing': 4, 'Conformation': 4}, desc='Ginger sow, the best mother in the herd. Two litters, no losses.')
pigrec('exk-h2', 'KK-24-02', 'Hazel', 'exk-s-blk', 'Female', 'exk-pl-r1', '2024-05-10', proj='exk-p-b', scores={'Mothering ability': 4, 'Temperament': 4, 'Grazing': 5, 'Conformation': 4}, desc='Black sow. Stays in condition on grass. Pregnant, due to farrow soon.')
pigrec('exk-h3', 'KK-24-03', 'Pearl', 'exk-s-bw', 'Female', 'exk-pl-r1', '2024-06-02', scores={'Mothering ability': 3, 'Temperament': 4, 'Grazing': 4, 'Conformation': 5}, desc='Black-and-white sow with the best tassels. Nervous with a first litter.')
pigrec('exk-r1', 'KK-24-04', 'Hamish', 'exk-s-gin', 'Male', 'exk-pl-boar', '2024-04-18', proj='exk-p-g', scores={'Temperament': 5, 'Conformation': 4})
pigrec('exk-r2', 'KK-24-05', 'Rufus', 'exk-s-blk', 'Male', 'exk-pl-boar', '2024-04-25', proj='exk-p-b', scores={'Temperament': 4, 'Conformation': 5})
pigrec('exk-r3', 'KK-25-01', 'Kahu', 'exk-s-bw', 'Male', 'exk-pl-boar', '2025-02-14', scores={'Temperament': 5, 'Conformation': 5}, desc='Bought from another breeder as an outcross boar, so the herd does not get too related.')
def cross(id, date, m, f, proj, code, status='Successful', outcome='', pred=None, notes=''):
    return add(id=id, type='cross', date=date, motherId=m, fatherId=f, method='Natural mating', status=status, projectId=proj, code=code, eggsSet='', outcome=outcome, notes=notes, goalV='1', prediction=pred)
cross('exk-c1', '2025-06-10', 'exk-h1', 'exk-r1', 'exk-p-g', '25C-1', outcome='7 piglets born alive')
cross('exk-c2', '2025-06-25', 'exk-h2', 'exk-r2', 'exk-p-b', '25C-2', outcome='8 piglets born alive')
cross('exk-c3', '2025-07-05', 'exk-h3', 'exk-r1', 'exk-p', '25C-3', outcome='6 piglets born alive')
cross('exk-c4', '2026-03-01', 'exk-h1', 'exk-r2', 'exk-p', '26C-1', outcome='7 piglets born alive')
cross('exk-c5', '2026-03-15', 'exk-h3', 'exk-r2', 'exk-p', '26C-2', outcome='6 piglets, 1 stillborn')
cross('exk-c6', '2026-06-20', 'exk-h2', 'exk-r1', 'exk-p', '26C-3', status='Done', notes='Mated in the third week of June. Gestation is about 114 days. Move to the farrowing hut five days before she is due.')
cross('exk-c7', '2026-11-20', 'exk-w1', 'exk-r3', 'exk-p', '26C-4', status='Planned', notes='Outcross: Marmalade to Kahu, to widen the gene pool.')
def litter(id, crossid, m, f, proj, date, alive, dead, weaned, wdate, wkg, notes):
    return add(id=id, type='clutch', crossId=crossid, motherId=m, fatherId=f, projectId=proj, kind='live', date=date, eggsSet='', fertile='', hatched='', bornAlive=alive, bornDead=dead, weaned=weaned, weanDate=wdate, weanWeight=wkg, notes=notes)
litter('exk-k1', 'exk-c1', 'exk-h1', 'exk-r1', 'exk-p-g', '2025-10-02', 7, 1, 7, '2025-11-27', 14, 'Farrowed overnight in the hut. One stillborn, the rest strong.')
litter('exk-k2', 'exk-c2', 'exk-h2', 'exk-r2', 'exk-p-b', '2025-10-17', 8, 0, 7, '2025-12-12', 13, 'Easy birth. One piglet lost at day 3 (crushed).')
litter('exk-k3', 'exk-c3', 'exk-h3', 'exk-r1', 'exk-p', '2025-10-27', 6, 1, 6, '2025-12-22', 12, 'First litter. Pearl was nervous, so we kept visitors away.')
litter('exk-k4', 'exk-c4', 'exk-h1', 'exk-r2', 'exk-p', '2026-06-23', 7, 0, 7, '2026-08-18', 15, 'Second litter, again no losses.')
litter('exk-k5', 'exk-c5', 'exk-h3', 'exk-r2', 'exk-p', '2026-07-07', 6, 1, 5, '2026-09-01', 14, 'Calmer this time. One piglet lost at day 5.')
keep = lambda d, *r, note='': {'decision': 'kept', 'reasons': list(r), 'note': note, 'date': d, 'goalV': '1'}
drop = lambda d, *r, note='': {'decision': 'rejected', 'reasons': list(r), 'note': note, 'date': d, 'goalV': '1'}
F1 = [  # id, code, name, sex, place, status, mother, father, cross, litter, project, scores, selection, colour
 ('exk-w1', 'KK-G-25-01', 'Marmalade', 'Female', 'exk-pl-r2', 'Selected', 'exk-h1', 'exk-r1', 'exk-c1', 'exk-k1', 'exk-p-g', {'Temperament': 5, 'Grazing': 5, 'Conformation': 4}, keep('2026-05-10', 'Meets target: Temperament', 'Holds condition on grass', note='Keeping her to take over from Poppy.'), 'ginger'),
 ('exk-w2', 'KK-G-25-02', 'Biscuit', 'Male', 'exk-pl-wean', 'Sold or rehomed', 'exk-h1', 'exk-r1', 'exk-c1', 'exk-k1', 'exk-p-g', {'Temperament': 4, 'Conformation': 3}, None, 'ginger'),
 ('exk-w3', 'KK-G-25-03', 'Honey', 'Female', 'exk-pl-r2', 'Active', 'exk-h1', 'exk-r1', 'exk-c1', 'exk-k1', 'exk-p-g', {'Temperament': 5, 'Grazing': 4}, None, 'ginger'),
 ('exk-b1', 'KK-B-25-01', 'Ebony', 'Female', 'exk-pl-r2', 'Selected', 'exk-h2', 'exk-r2', 'exk-c2', 'exk-k2', 'exk-p-b', {'Temperament': 4, 'Grazing': 5, 'Conformation': 5}, keep('2026-05-10', 'Meets target: Grazing', 'Good conformation'), 'black'),
 ('exk-b2', 'KK-B-25-02', 'Smudge', 'Female', 'exk-pl-r2', 'Active', 'exk-h2', 'exk-r2', 'exk-c2', 'exk-k2', 'exk-p-b', {'Temperament': 4, 'Grazing': 4}, None, 'black'),
 ('exk-b3', 'KK-B-25-03', 'Domino', 'Male', 'exk-pl-wean', 'Sold or rehomed', 'exk-h2', 'exk-r2', 'exk-c2', 'exk-k2', 'exk-p-b', {'Temperament': 3}, drop('2026-03-02', 'Related to the herd boar', note='Sold as a pet boar, wethered.'), 'black'),
 ('exk-x1', 'KK-25-02', 'Patch', 'Female', 'exk-pl-r2', 'Selected', 'exk-h3', 'exk-r1', 'exk-c3', 'exk-k3', 'exk-p', {'Temperament': 4, 'Grazing': 4, 'Conformation': 5}, keep('2026-05-10', 'Meets target: Conformation', 'Calm temperament'), 'bw'),
 ('exk-x2', 'KK-25-03', 'Clover', 'Female', 'exk-pl-r2', 'Active', 'exk-h3', 'exk-r1', 'exk-c3', 'exk-k3', 'exk-p', {'Temperament': 4, 'Conformation': 4}, None, 'ginger'),
 ('exk-x3', 'KK-25-04', 'Tank', 'Male', 'exk-pl-wean', 'Sold or rehomed', 'exk-h3', 'exk-r1', 'exk-c3', 'exk-k3', 'exk-p', {'Temperament': 3, 'Conformation': 2}, drop('2026-03-02', 'Poor conformation'), 'bw'),
]
FCOL = {}
for id, code, name, sex, place, status, m, f, c, k, proj, sc, sel, col in F1:
    start = {'exk-k1': '2025-10-02', 'exk-k2': '2025-10-17', 'exk-k3': '2025-10-27'}[k]
    pigrec(id, code, name, '', sex, place, start, status=status, gen='F1', proj=proj, mother=m, father=f, cross=c, clutch=k, scores=sc, selection=sel); FCOL[id] = col
def group(id, code, name, count, mother, father, cross_, lit, proj, gen, start, place, status='Active'):
    return add(id=id, type='individual', isGroup=True, code=code, name=name, mix=[], count=count, strainId='', projectId=proj, motherId=mother, fatherId=father, crossId=cross_, clutchId=lit, generation=gen, startDate=start, placeId=place, status=status, photoIds=[])
group('exk-g-k1', 'KK-G01', 'Rest of the 25C-1 litter, sold as weaners', 4, 'exk-h1', 'exk-r1', 'exk-c1', 'exk-k1', 'exk-p-g', 'F1', '2025-10-02', '', 'Sold or rehomed')
group('exk-g-k2', 'KK-G02', 'Rest of the 25C-2 litter, sold as weaners', 4, 'exk-h2', 'exk-r2', 'exk-c2', 'exk-k2', 'exk-p-b', 'F1', '2025-10-17', '', 'Sold or rehomed')
group('exk-g-k3', 'KK-G03', 'Rest of the 25C-3 litter, sold as weaners', 3, 'exk-h3', 'exk-r1', 'exk-c3', 'exk-k3', 'exk-p', 'F1', '2025-10-27', '', 'Sold or rehomed')
group('exk-g-k4', 'KK-G04', '7 weaners from 26C-1 (Poppy × Rufus)', 7, 'exk-h1', 'exk-r2', 'exk-c4', 'exk-k4', 'exk-p', 'F2', '2026-06-23', 'exk-pl-wean')
group('exk-g-k5', 'KK-G05', '5 weaners from 26C-2 (Pearl × Rufus)', 5, 'exk-h3', 'exk-r2', 'exk-c5', 'exk-k5', 'exk-p', 'F2', '2026-07-07', 'exk-pl-wean')

# ------------------------------------------------------------------ weigh-ins and litter records
e = 0
def entry(rt, ind, date, values, notes=''):
    global e; e += 1; add(id=f'exk-e{e}', type='entry', rtId=rt, indId=ind, parentEntryId='', date=date, values=values, photoIds=[], notes=notes, seq=e)
for ind, base, bc in [('exk-h1', 96, 4), ('exk-h2', 92, 4), ('exk-h3', 88, 3), ('exk-r1', 118, 4), ('exk-r2', 124, 4), ('exk-r3', 112, 4), ('exk-w1', 66, 4), ('exk-b1', 63, 4), ('exk-x1', 61, 3), ('exk-w3', 62, 4), ('exk-b2', 60, 3), ('exk-x2', 58, 3), ('exk-g-k4', 17, 4), ('exk-g-k5', 15, 4)]:
    for k, month in enumerate(['2026-07-30', '2026-08-30', '2026-09-28']):
        entry('exk-rt-w', ind, month, {'exk-rt-w-f0': base + [0, 3, 6][k], 'exk-rt-w-f1': bc if k < 2 or ind != 'exk-h3' else 4})
for ind, k, size, alive, wean in [('exk-h1', 'k1', 8, 7, 7), ('exk-h2', 'k2', 8, 8, 7), ('exk-h3', 'k3', 7, 6, 6), ('exk-h1', 'k4', 7, 7, 7), ('exk-h3', 'k5', 7, 6, 5)]:
    date = next(x['date'] for x in R if x['id'] == 'exk-' + k)
    entry('exk-rt-l', ind, date, {'exk-rt-l-f0': size, 'exk-rt-l-f1': alive, 'exk-rt-l-f3': wean})

# ------------------------------------------------------------------ treatments and sales
add(id='exk-in1', type='input', name='Pig wormer (example)', category='wormer', unit='mL', rate='1 mL per 10 kg of bodyweight', organic=False, qty=250, opened='2026-03-01', expiry='2027-12-31', notes='Example only. Always follow the label and your vet.', whp={'meat': 28}, photoIds=[])
add(id='exk-in2', type='input', name='Erysipelas vaccine (example)', category='vaccine', unit='mL', rate='2 mL under the skin behind the ear', organic=False, qty=100, opened='2026-02-10', expiry='2027-06-30', notes='Example only. Booster every six months.', whp={'meat': 21}, photoIds=[])
add(id='exk-in3', type='input', name='Pig grower pellets (example)', category='feed', unit='kg', rate='1 kg per pig per day on top of pasture', organic=False, qty=400, opened='2026-09-01', expiry='', notes='Example only. Kunekune do well on grass, so this is a top-up for nursing sows and weaners.', whp={}, photoIds=[])
herd = ['exk-h1', 'exk-h2', 'exk-h3', 'exk-r1', 'exk-r2', 'exk-r3', 'exk-w1', 'exk-w3', 'exk-b1', 'exk-b2', 'exk-x1', 'exk-x2']
add(id='exk-ap1', type='apply', date='2026-09-05', inputId='exk-in1', amount=40, unit='mL', method='Oral', reason='Routine worming', targets=herd, scope={'type': 'place', 'id': 'exk-pl-r1'}, repeatDays=90, notes='')
add(id='exk-ap2', type='apply', date='2026-08-20', inputId='exk-in2', amount=24, unit='mL', method='Injection', reason='Six-monthly booster', targets=herd, scope={'type': 'place', 'id': 'exk-pl-r1'}, repeatDays=180, notes='')
add(id='exk-ap3', type='apply', date='2026-09-28', inputId='exk-in3', amount=12, unit='kg', method='In feed', reason='Top-up for the weaners', targets=['exk-g-k4', 'exk-g-k5'], scope={'type': 'place', 'id': 'exk-pl-wean'}, repeatDays='', notes='')
add(id='exk-pr1', type='product', name='Weaners sold', kind='animal', unit='weaners', alsoWeight=False, weightUnit='kg', notes='')
for k, (d, q, who, tg) in enumerate([('2025-12-01', 4, 'Sold to a neighbour', 'exk-g-k1'), ('2025-12-14', 4, 'Sold at the farm gate', 'exk-g-k2'), ('2026-01-10', 3, 'Sold to a hobby farm', 'exk-g-k3')]):
    add(id=f'exk-y{k}', type='yield', date=d, productId='exk-pr1', qty=q, weight='', unit='weaners', quality='', targets=[tg], scope={'type': 'single'}, notes=who)

# ------------------------------------------------------------------ notes, reminders
NOTES = [('exk-n1', 'exk-p', '2025-05-01', 'Plan: three colours of Kunekune, two boars, grass-fed. Keep every litter recorded so the lines can be traced and the boars do not end up related to the gilts.'),
         ('exk-n2', 'exk-h1', '2025-10-02', 'Poppy farrowed overnight: seven live, one stillborn. All seven suckling by morning.'),
         ('exk-n3', 'exk-h3', '2025-10-27', 'Pearl was restless for two days and bit the hut rail. Kept it quiet and she settled. All six fed.'),
         ('exk-n4', 'exk-p', '2026-03-12', 'Rotated the sows to paddock 1 and rested paddock 2. Grass was knee high. Orchard run opened for the windfalls.'),
         ('exk-n5', 'exk-h2', '2026-09-18', 'Hazel is clearly in pig: udder filling and she is making a nest. Due in a couple of weeks. Hut cleaned and fresh straw ready.'),
         ('exk-n6', 'exk-w1', '2026-09-28', 'Marmalade weighed 72 kg at 12 months on grass alone. On track to breed from her in November.')]
for nid, ref, date, text in NOTES: add(id=nid, type='note', refId=ref, date=date, text=text, photoIds=[])
add(id='exk-rem1', type='reminder', date='2026-10-07', text='Move Hazel to the farrowing hut. Fresh straw and check the rail.', refId='exk-h2', done=False)
add(id='exk-rem2', type='reminder', date='2026-10-20', text='Plan the November mating: book Kahu in with Marmalade', refId='exk-p', done=False)

# ------------------------------------------------------------------ pictures
pal_of = {'exk-h1': 'ginger', 'exk-h2': 'black', 'exk-h3': 'bw', 'exk-r1': 'ginger', 'exk-r2': 'black', 'exk-r3': 'bw'}; pal_of.update(FCOL)
scenes = ['paddock', 'orchard', 'evening', 'mud']
for i, r in enumerate([x for x in R if x['type'] == 'individual' and not x.get('isGroup')]):
    young = r['startDate'] >= '2026-01-01'
    attach(r['id'], photo('exk-i-' + r['id'], G.img_pig(pal_of[r['id']], seed=10 + i, facing=1 if i % 2 == 0 else -1, scene=scenes[i % 4])), 'adult')
for sid, pal in [('exk-s-gin', 'ginger'), ('exk-s-blk', 'black'), ('exk-s-bw', 'bw')]:
    attach(sid, photo('exk-s-' + pal, G.img_pig(pal, seed=3, scene='orchard')), 'adult')
attach('exk-g-k4', photo('exk-g4', G.img_litter(('ginger', 'ginger', 'black', 'black', 'ginger', 'bw', 'black'), seed=4)), 'young')
attach('exk-g-k5', photo('exk-g5', G.img_litter(('black', 'bw', 'black', 'black', 'bw'), seed=5)), 'young')
for pid, img in [('exk-pl-farrow', G.img_hut()), ('exk-pl-r1', G.img_paddock(('ginger', 'black'))), ('exk-pl-r2', G.img_paddock(('bw', 'ginger'), 'evening')), ('exk-pl-boar', G.img_paddock(('black', 'bw'), 'mud')),
                 ('exk-pl-wean', G.img_litter(seed=6)), ('exk-pl-orch', G.img_paddock(('ginger', 'ginger'), 'orchard'))]:
    attach(pid, photo('exk-p-' + pid, img), 'place')
attach('exk-n2', photo('exk-n2', G.img_sow_litter('ginger', ('ginger', 'ginger', 'ginger', 'bw'), 21)), 'group')
attach('exk-n3', photo('exk-n3', G.img_sow_litter('bw', ('ginger', 'bw', 'bw', 'ginger'), 22)), 'group')
attach('exk-n4', photo('exk-n4', G.img_paddock(('ginger', 'black'), 'orchard')), 'place')
attach('exk-n5', photo('exk-n5', G.img_hut()), 'place')
attach('exk-n6', photo('exk-n6', G.img_scales()), 'adult')
add(id='exk-n7', type='note', refId='exk-in3', date='2026-09-28', text='Feed bags used for the weaners.', photoIds=[]); attach('exk-n7', photo('exk-n7', G.img_feed()), 'other')
add(id='exk-n8', type='note', refId='', date='2026-09-30', text='The two weaner litters side by side at three and four months. Shared for the local breeders page.', photoIds=[]); attach('exk-n8', photo('exk-n4b', G.img_litter(('ginger', 'ginger', 'black', 'black', 'bw', 'ginger'), seed=8, scene='orchard')), 'young')

# ------------------------------------------------------------------ breeding plan
def node(i, per, kind, label='', ref='', qty=0, via=''):
    n = {'id': i, 'periodId': per, 'kind': kind, 'label': label}
    if ref: n['refId'] = ref; n['lockedAt'] = LOCK
    if qty: n['qty'] = qty
    if via: n['via'] = via
    return n
def edge(i, kind, a, b, d='one', per='', via='', bend=0, note=''):
    x = {'id': i, 'kind': kind, 'from': a, 'to': b, 'note': note, 'bend': bend}
    if kind == 'cross': x['dir'] = d
    if per: x['periodId'] = per
    if via: x['via'] = via
    return x
per = [{'id': 'p0', 'name': 'Founders', 'span': '1 year'}, {'id': 'p1', 'name': 'First litters (F1)', 'span': '1 year'}, {'id': 'p2', 'name': 'Second litters', 'span': '1 year'}, {'id': 'p3', 'name': 'Next litter', 'span': '6 months'}]
N = [node('n1', 'p0', 'animal', 'Poppy (ginger)', 'exk-h1'), node('n2', 'p0', 'animal', 'Hamish (ginger boar)', 'exk-r1'), node('n3', 'p0', 'animal', 'Hazel (black)', 'exk-h2'), node('n4', 'p0', 'animal', 'Rufus (black boar)', 'exk-r2'), node('n5', 'p0', 'animal', 'Pearl (black and white)', 'exk-h3'),
     node('n6', 'p1', 'animal', 'Marmalade', 'exk-w1', via='e1'), node('n7', 'p1', 'animal', 'Ebony', 'exk-b1', via='e2'), node('n8', 'p1', 'animal', 'Patch', 'exk-x1', via='e3'),
     node('n9', 'p2', 'animal', '26C-1 weaners', 'exk-g-k4', via='e4'), node('n10', 'p2', 'animal', '26C-2 weaners', 'exk-g-k5', via='e5'), node('n12', 'p2', 'animal', 'Kahu (new boar)', 'exk-r3'),
     node('n11', 'p3', 'animal', 'Piglets from 26C-4', qty=7, via='e6'), node('n13', 'p3', 'group', 'Weaner paddock')]
E_ = [edge('e1', 'cross', 'n1', 'n2', 'one', 'p0'), edge('e2', 'cross', 'n3', 'n4', 'one', 'p0'), edge('e3', 'cross', 'n5', 'n2', 'one', 'p0'),
      edge('g1', 'grow', 'n1', 'n6', via='e1'), edge('g2', 'grow', 'n3', 'n7', via='e2'), edge('g3', 'grow', 'n5', 'n8', via='e3'),
      edge('e4', 'cross', 'n1', 'n4', 'one', 'p1', bend=1, note='Second litter, new boar'), edge('e5', 'cross', 'n5', 'n4', 'one', 'p1'),
      edge('g4', 'grow', 'n1', 'n9', via='e4'), edge('g5', 'grow', 'n5', 'n10', via='e5'),
      edge('e6', 'cross', 'n6', 'n12', 'one', 'p2', note='Outcross to widen the gene pool'), edge('g6', 'grow', 'n6', 'n11', via='e6'), edge('r1', 'release', 'n11', 'n13')]
next(x for x in R if x['id'] == 'exk-p')['plan'] = {'v': 1, 'periods': per, 'nodes': N, 'edges': E_}
for c, ed in [('exk-c1', 'e1'), ('exk-c2', 'e2'), ('exk-c3', 'e3'), ('exk-c4', 'e4'), ('exk-c5', 'e5'), ('exk-c7', 'e6')]: next(x for x in R if x['id'] == c)['planEdge'] = ed

json.dump({'app': 'lineage', 'version': 3, 'format': 'example', 'name': 'Pig example: Kunekune herd', 'anchorDate': ANCHOR, 'photos': PH, 'records': R}, open(os.path.join(EX, 'pigs-example.json'), 'w'), indent=1, ensure_ascii=False)
print('pig example:', len(R), 'records,', len(PH), 'pictures,', round(os.path.getsize(os.path.join(EX, 'pigs-example.json')) / 1024), 'KB')
