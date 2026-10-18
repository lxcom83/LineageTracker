"""Builds the example data that ships with Lineage Tracker.
- examples/olive-example.json: a multi-founder chicken breeding project (new in 0.19)
- examples/plants-example.json: adds 0.19-era records to the existing squash example
Re-runnable: earlier additions are replaced. Photos can be added later through PHOTOS."""
import json, os, base64, glob
HERE = os.path.dirname(os.path.abspath(__file__)); EX = os.path.join(HERE, '..', 'examples')
ANCHOR = '2026-10-01'
PHOTOS = {}   # record id -> list of image files (added when licensed photos are available)

def photo_records(prefix):
    out, ids = [], {}
    for rid, files in PHOTOS.items():
        if not rid.startswith(prefix): continue
        for k, f in enumerate(files):
            pid = f'{rid}-ph{k}'; data = base64.b64encode(open(f, 'rb').read()).decode()
            out.append({'id': pid, 'full': 'data:image/jpeg;base64,' + data}); ids.setdefault(rid, []).append(pid)
    return out, ids

# ---------------------------------------------------------------- Olive Egger
SP = 'Gallus gallus domesticus'
R = []
def add(**r): R.append(r); return r
add(id='exo-s-ara', type='strain', name='Araucana', kind='animal', group='Chicken', species=SP, speciesVerified=True, origin='Example Poultry', description='Lays sky-blue eggs. Carries the blue-eggshell gene (O), which is dominant.', photoIds=[])
add(id='exo-s-wel', type='strain', name='Welsummer', kind='animal', group='Chicken', species=SP, speciesVerified=True, origin='Example Poultry', description='Dark brown, speckled eggs. Friendly, good forager.', photoIds=[])
add(id='exo-s-mar', type='strain', name='Black Copper Maran', kind='animal', group='Chicken', species=SP, speciesVerified=True, origin='Example Poultry', description='The darkest brown eggs. Hardy, calm.', photoIds=[])
add(id='exo-s-aus', type='strain', name='Black Australorp', kind='animal', group='Chicken', species=SP, speciesVerified=True, origin='Example Poultry', description='Australian utility breed and a prolific layer of brown eggs.', photoIds=[])
for pid, name, method, details in [('exo-pl-a', 'Breeding pen A', 'Pen', 'Araucana hen with the Welsummer rooster.'), ('exo-pl-b', 'Breeding pen B', 'Pen', 'Araucana hens with the Maran rooster.'),
                                   ('exo-pl-brood', 'Brooder', 'Brooder', 'Heat plate, first four weeks.'), ('exo-pl-grow', 'Grow-out run', 'Run', 'Young birds, five weeks to point of lay.'), ('exo-pl-coop', 'Laying coop', 'Coop and run', 'Main laying flock, deep litter.')]:
    add(id=pid, type='place', name=name, kind='animal', method=method, details=details, photoIds=[])
add(id='exo-site', type='site', name='Example farm', lat=-32.73, lon=151.55, locLabel='Hunter Valley, NSW (example)', seasonStart=7, heat=32, frost=0, gddBase=10, manual=False, manualMode='regional')
RT = [
 {'id': 'exo-rt-e', 'tplKey': 'eggs', 'name': 'Egg count', 'itemName': '', 'parentRt': '', 'fields': [
   {'id': 'exo-rt-e-f0', 'label': 'Days counted', 'type': 'number', 'agg': 'sum'}, {'id': 'exo-rt-e-f1', 'label': 'Eggs laid', 'type': 'number', 'agg': 'sum'},
   {'id': 'exo-rt-e-f2', 'label': 'Laying rate', 'type': 'calc', 'unit': '%', 'formula': '{Eggs laid} / {Days counted} * 100', 'agg': 'avg', 'compare': True},
   {'id': 'exo-rt-e-f3', 'label': 'Average egg weight', 'type': 'number', 'unit': 'g', 'agg': 'avg', 'compare': True},
   {'id': 'exo-rt-e-f4', 'label': 'Egg colour (olive depth)', 'type': 'score', 'agg': 'latest', 'compare': True}], 'repeatDays': 30},
 {'id': 'exo-rt-w', 'tplKey': 'weigh', 'name': 'Weigh-in', 'itemName': '', 'parentRt': '', 'fields': [
   {'id': 'exo-rt-w-f0', 'label': 'Weight', 'type': 'number', 'unit': 'kg', 'agg': 'latest', 'compare': True}, {'id': 'exo-rt-w-f1', 'label': 'Body condition', 'type': 'score', 'agg': 'latest', 'compare': True}], 'repeatDays': 30},
]
TRAITS = [{'name': 'Egg colour (olive depth)', 'tier': 1, 'must': True, 'def': '1 = sky blue, 3 = sage green, 5 = deep olive.'},
          {'name': 'Laying rate', 'tier': 1, 'must': False, 'def': 'Eggs per week at peak lay.'},
          {'name': 'Temperament', 'tier': 2, 'must': False, 'def': '1 = flighty or aggressive, 5 = calm and easy to handle.'},
          {'name': 'Heat tolerance', 'tier': 2, 'must': False, 'def': '1 = panting and off lay above 30°C, 5 = active and laying in heat.'}]
GOAL = 'A calm, productive line laying deep olive eggs, built from Araucana blue eggs and dark brown Welsummer and Maran eggs, with Australorp laying ability to come. Example project: everything here is made up.'
add(id='exo-p', type='project', name='Olive Egger line', code='OE', kind='animal', species=SP, parentId='', goal=GOAL, strainIds=['exo-s-ara', 'exo-s-wel', 'exo-s-mar', 'exo-s-aus'], traits=TRAITS, recordTypes=RT,
    goals=[{'v': 1, 'date': '2025-07-01', 'statement': GOAL, 'why': 'Starting the line.'}], goalReviewMonths=12, siteId='exo-site', tagStyle={'preset': 'animal'})
add(id='exo-p-w', type='project', name='Line W (Araucana × Welsummer)', code='W', kind='animal', species=SP, parentId='exo-p', goal='Olive eggs with Welsummer speckling and friendliness.', strainIds=['exo-s-ara', 'exo-s-wel'], traits=[], recordTypes=[])
add(id='exo-p-m', type='project', name='Line M (Araucana × Maran)', code='M', kind='animal', species=SP, parentId='exo-p', goal='The darkest olive, from the darkest brown.', strainIds=['exo-s-ara', 'exo-s-mar'], traits=[], recordTypes=[])
def bird(id, code, name, strain, sex, place, start, status='Kept for breeding', gen='P', proj='exo-p', mother='', father='', cross='', clutch='', scores=None, selection=None, desc=''):
    return add(id=id, type='individual', code=code, name=name, strainId=strain, projectId=proj, generation=gen, sex=sex, motherId=mother, fatherId=father, stockId='', startDate=start, status=status, placeId=place, crossId=cross, clutchId=clutch, description=desc, scores=scores or {}, selection=selection, photoIds=[])
bird('exo-h1', 'OE-24-01', 'Juniper', 'exo-s-ara', 'Female', 'exo-pl-a', '2024-03-02', scores={'Egg colour (olive depth)': 1, 'Laying rate': 3, 'Temperament': 4})
bird('exo-h2', 'OE-24-02', 'Sage', 'exo-s-ara', 'Female', 'exo-pl-b', '2024-03-02', scores={'Egg colour (olive depth)': 1, 'Laying rate': 3, 'Temperament': 5})
bird('exo-h3', 'OE-24-03', 'Willow', 'exo-s-ara', 'Female', 'exo-pl-b', '2024-03-09', scores={'Egg colour (olive depth)': 1, 'Laying rate': 4, 'Temperament': 3})
bird('exo-r1', 'OE-24-04', 'Basil', 'exo-s-wel', 'Male', 'exo-pl-a', '2024-02-20', scores={'Temperament': 5})
bird('exo-r2', 'OE-24-05', 'Copper', 'exo-s-mar', 'Male', 'exo-pl-b', '2024-02-14', scores={'Temperament': 4, 'Heat tolerance': 4})
bird('exo-h4', 'OE-24-06', 'Dot', 'exo-s-aus', 'Female', 'exo-pl-coop', '2024-04-01', scores={'Laying rate': 5, 'Temperament': 5})
def cross(id, date, m, f, proj, code, status='Successful', eggs='', outcome='', pred=None):
    return add(id=id, type='cross', date=date, motherId=m, fatherId=f, method='Natural mating', status=status, projectId=proj, code=code, eggsSet=eggs, outcome=outcome, notes='', goalV='1', prediction=pred)
cross('exo-c1', '2025-08-20', 'exo-h1', 'exo-r1', 'exo-p-w', '25C-1', eggs='2025-08-25', outcome='8 chicks from 12 eggs')
cross('exo-c2', '2025-08-22', 'exo-h2', 'exo-r2', 'exo-p-m', '25C-2', eggs='2025-08-27', outcome='11 chicks from 14 eggs')
cross('exo-c3', '2025-09-05', 'exo-h3', 'exo-r2', 'exo-p-m', '25C-3', eggs='2025-09-08', outcome='6 chicks from 10 eggs')
def clutch(id, crossid, m, f, proj, date, set_, fert, hatched, notes):
    return add(id=id, type='clutch', crossId=crossid, motherId=m, fatherId=f, projectId=proj, kind='eggs', date=date, eggsSet=set_, fertile=fert, hatched=hatched, bornAlive='', bornDead='', weaned='', weanDate='', weanWeight='', notes=notes)
clutch('exo-k1', 'exo-c1', 'exo-h1', 'exo-r1', 'exo-p-w', '2025-08-25', 12, 10, 8, 'Incubator. Candled day 7 and day 14.')
clutch('exo-k2', 'exo-c2', 'exo-h2', 'exo-r2', 'exo-p-m', '2025-08-27', 14, 13, 11, 'Broody Australorp sat them.')
clutch('exo-k3', 'exo-c3', 'exo-h3', 'exo-r2', 'exo-p-m', '2025-09-08', 10, 7, 6, 'Incubator. Two late quitters.')
keep = lambda *r: {'decision': 'kept', 'reasons': list(r), 'note': '', 'date': '2026-03-15', 'goalV': '1'}
drop = lambda *r: {'decision': 'rejected', 'reasons': list(r), 'note': '', 'date': '2026-01-20', 'goalV': '1'}
F1 = [
 ('exo-w1', 'OE-W-25-01', 'Olive', 'Female', 'exo-pl-coop', 'Selected', 'exo-h1', 'exo-r1', 'exo-c1', 'exo-k1', 'exo-p-w', {'Egg colour (olive depth)': 4, 'Laying rate': 4, 'Temperament': 5}, keep('Meets target: Egg colour (olive depth)', 'Calm temperament')),
 ('exo-w2', 'OE-W-25-02', 'Fern', 'Female', 'exo-pl-coop', 'Selected', 'exo-h1', 'exo-r1', 'exo-c1', 'exo-k1', 'exo-p-w', {'Egg colour (olive depth)': 3, 'Laying rate': 5, 'Temperament': 4}, keep('Meets target: Laying rate', 'Healthy')),
 ('exo-w3', 'OE-W-25-03', '', 'Male', 'exo-pl-grow', 'Sold or rehomed', 'exo-h1', 'exo-r1', 'exo-c1', 'exo-k1', 'exo-p-w', {'Temperament': 2}, drop('Poor temperament')),
 ('exo-w4', 'OE-W-25-04', '', 'Female', 'exo-pl-coop', 'Active', 'exo-h1', 'exo-r1', 'exo-c1', 'exo-k1', 'exo-p-w', {'Egg colour (olive depth)': 2, 'Laying rate': 4}, None),
 ('exo-m1', 'OE-M-25-01', 'Moss', 'Female', 'exo-pl-coop', 'Selected', 'exo-h2', 'exo-r2', 'exo-c2', 'exo-k2', 'exo-p-m', {'Egg colour (olive depth)': 5, 'Laying rate': 3, 'Temperament': 4}, keep('Meets target: Egg colour (olive depth)', 'Hardy')),
 ('exo-m2', 'OE-M-25-02', 'Ivy', 'Female', 'exo-pl-coop', 'Active', 'exo-h2', 'exo-r2', 'exo-c2', 'exo-k2', 'exo-p-m', {'Egg colour (olive depth)': 4, 'Laying rate': 4, 'Temperament': 4}, None),
 ('exo-m3', 'OE-M-25-03', 'Bramble', 'Male', 'exo-pl-b', 'Kept for breeding', 'exo-h2', 'exo-r2', 'exo-c2', 'exo-k2', 'exo-p-m', {'Temperament': 5, 'Heat tolerance': 4}, keep('Calm temperament', 'Healthy')),
 ('exo-m4', 'OE-M-25-04', '', 'Male', 'exo-pl-grow', 'Sold or rehomed', 'exo-h2', 'exo-r2', 'exo-c2', 'exo-k2', 'exo-p-m', {'Temperament': 3}, None),
 ('exo-m5', 'OE-M-25-05', 'Thistle', 'Female', 'exo-pl-coop', 'Active', 'exo-h3', 'exo-r2', 'exo-c3', 'exo-k3', 'exo-p-m', {'Egg colour (olive depth)': 4, 'Laying rate': 3}, None),
]
for id, code, name, sex, place, status, m, f, c, k, proj, sc, sel in F1:
    hatch = {'exo-k1': '2025-09-15', 'exo-k2': '2025-09-17', 'exo-k3': '2025-09-29'}[k]
    bird(id, code, name, '', sex, place, hatch, status=status, gen='F1', proj=proj, mother=m, father=f, cross=c, clutch=k, scores=sc, selection=sel)
add(id='exo-g-k1', type='individual', isGroup=True, code='OE-G01', name='Rest of the 25C-1 hatch, sold as pullets', mix=[], count=4, strainId='', projectId='exo-p-w', motherId='exo-h1', fatherId='exo-r1', crossId='exo-c1', clutchId='exo-k1', generation='F1', startDate='2025-09-15', placeId='', status='Sold or rehomed', photoIds=[])
add(id='exo-g-k2', type='individual', isGroup=True, code='OE-G02', name='Rest of the 25C-2 hatch, sold as pullets', mix=[], count=7, strainId='', projectId='exo-p-m', motherId='exo-h2', fatherId='exo-r2', crossId='exo-c2', clutchId='exo-k2', generation='F1', startDate='2025-09-17', placeId='', status='Sold or rehomed', photoIds=[])
# This season: an intercross between the lines, a backcross to the Maran, and a planned outcross with a saved genetics prediction
cross('exo-c4', '2026-08-15', 'exo-w1', 'exo-m3', 'exo-p', '26C-1', eggs='2026-08-20', outcome='9 chicks from 12 eggs')
cross('exo-c5', '2026-08-25', 'exo-m1', 'exo-r2', 'exo-p-m', '26C-2', eggs='2026-08-28', outcome='7 chicks from 10 eggs')
PRED = {'genes': ['Blue eggshell (O)'], 'mother': ['O/o'], 'father': ['o/o'], 'results': [{'sex': None, 'ph': 'Blue-shelled eggs (carries non-blue)', 'p': 0.5}, {'sex': None, 'ph': 'Not blue-shelled', 'p': 0.5}], 'date': '2026-09-20'}
cross('exo-c6', '2026-11-01', 'exo-w2', 'exo-r3', 'exo-p', '26C-3', status='Planned', pred=PRED)
bird('exo-r3', 'OE-24-07', 'Oscar', 'exo-s-aus', 'Male', 'exo-pl-coop', '2024-04-01', scores={'Temperament': 5, 'Laying rate': 5}, desc='Australorp rooster from a high-laying line. Planned outcross for laying ability.')
clutch('exo-k4', 'exo-c4', 'exo-w1', 'exo-m3', 'exo-p', '2026-08-20', 12, 11, 9, 'First hatch combining Line W and Line M.')
clutch('exo-k5', 'exo-c5', 'exo-m1', 'exo-r2', 'exo-p-m', '2026-08-28', 10, 9, 7, 'Backcross to Copper for darker eggs.')
add(id='exo-g-k4', type='individual', isGroup=True, code='OE-G03', name='9 chicks from 26C-1 (Line W × Line M)', mix=[], count=9, strainId='', projectId='exo-p', motherId='exo-w1', fatherId='exo-m3', crossId='exo-c4', clutchId='exo-k4', generation='F2', startDate='2026-09-10', placeId='exo-pl-brood', status='Active', photoIds=[])
for n in range(1, 8):
    bird(f'exo-b{n}', f'OE-26-{n:02d}', '', '', ['Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Female'][n - 1], 'exo-pl-brood', '2026-09-18', status='Active', gen='BC1F1', proj='exo-p-m', mother='exo-m1', father='exo-r2', cross='exo-c5', clutch='exo-k5')
# Egg counts and weigh-ins
e = 0
def entry(rt, ind, date, values, notes=''):
    global e; e += 1; add(id=f'exo-e{e}', type='entry', rtId=rt, indId=ind, parentEntryId='', date=date, values=values, photoIds=[], notes=notes, seq=e)
for ind, base, colour, wt in [('exo-h1', 19, 1, 58), ('exo-h2', 18, 1, 57), ('exo-h3', 21, 1, 59), ('exo-h4', 25, '', 61), ('exo-w1', 22, 4, 56), ('exo-w2', 25, 3, 57), ('exo-m1', 19, 5, 60), ('exo-m2', 21, 4, 58), ('exo-m5', 18, 4, 57)]:
    for k, month in enumerate(['2026-06-30', '2026-07-31', '2026-08-31', '2026-09-30']):
        laid = base + [-3, -1, 1, 2][k]
        entry('exo-rt-e', ind, month, {'exo-rt-e-f0': 30, 'exo-rt-e-f1': laid, 'exo-rt-e-f3': wt + [0, 0, 1, 1][k], **({'exo-rt-e-f4': colour} if colour != '' else {})})
for ind, w in [('exo-w1', 1.9), ('exo-w2', 2.0), ('exo-w3', 2.6), ('exo-w4', 1.8), ('exo-m1', 2.1), ('exo-m2', 2.0), ('exo-m3', 2.9), ('exo-m4', 2.7), ('exo-m5', 1.9)]:
    entry('exo-rt-w', ind, '2026-01-10', {'exo-rt-w-f0': w, 'exo-rt-w-f1': 4}, 'Weighed at 16 weeks.')
# A wormer with withholding, eggs as a product, a laying flock group, notes and a reminder
add(id='exo-in1', type='input', name='Poultry wormer (example)', category='wormer', unit='mL', rate='1 mL per litre of drinking water', organic=False, qty=180, opened='2026-03-01', expiry='2027-12-31', notes='Example only.', whp={'eggs': 7, 'meat': 28}, photoIds=[])
add(id='exo-g-flock', type='individual', isGroup=True, code='OE-G04', name='Laying flock', mix=[{'strainId': 'exo-s-aus', 'count': 4}, {'strainId': 'exo-s-ara', 'count': 2}], count=6, strainId='', projectId='', generation='', startDate='2024-05-01', placeId='exo-pl-coop', status='Active', photoIds=[])
add(id='exo-ap1', type='apply', date='2026-09-02', inputId='exo-in1', amount=20, unit='mL', method='In water', reason='Routine worming', targets=['exo-g-flock', 'exo-w1', 'exo-w2', 'exo-m1', 'exo-m2', 'exo-m5', 'exo-h4'], scope={'type': 'place', 'id': 'exo-pl-coop'}, repeatDays=90, notes='')
add(id='exo-pr1', type='product', name='Eggs', kind='animal', unit='eggs', alsoWeight=False, weightUnit='kg', notes='')
for k, (d, q) in enumerate([('2026-09-07', 31), ('2026-09-14', 34), ('2026-09-21', 33), ('2026-09-28', 36)]):
    add(id=f'exo-y{k}', type='yield', date=d, productId='exo-pr1', qty=q, weight='', unit='eggs', quality='', targets=['exo-g-flock'], scope={'type': 'single'}, notes='Weekly collection, laying flock.')
for nid, ref, date, text in [('exo-n1', 'exo-p', '2025-07-01', 'Plan: Araucana hens over a Welsummer rooster (Line W) and a Maran rooster (Line M). Blue shell plus brown coating should give olive F1s.'),
                              ('exo-n2', 'exo-w1', '2026-03-15', 'First olive egg from Olive at 26 weeks. Sage green with fine speckles.'),
                              ('exo-n3', 'exo-m1', '2026-03-20', 'Moss lays the darkest olive so far: deep khaki.'),
                              ('exo-n4', 'exo-p', '2026-09-20', 'Backcross chicks (26C-2) hatched well. Expect about half to lay blue-based eggs, and darker olive than the F1s.')]:
    add(id=nid, type='note', refId=ref, date=date, text=text, photoIds=[])
add(id='exo-rem1', type='reminder', date='2026-10-16', text='Move the backcross chicks from the brooder to the grow-out run', refId='exo-p', done=False)
ph, pids = photo_records('exo-')
for r in R:
    if r['id'] in pids: r['photoIds'] = pids[r['id']]
json.dump({'app': 'lineage', 'version': 3, 'format': 'example', 'name': 'Breeding example: Olive Egger line', 'anchorDate': ANCHOR, 'photos': ph, 'records': R}, open(os.path.join(EX, 'olive-example.json'), 'w'), indent=1, ensure_ascii=False)
print('olive example:', len(R), 'records')

# ---------------------------------------------------------------- Plant example additions
P = os.path.join(EX, 'plants-example.json'); d = json.load(open(P))
recs = [r for r in d['records'] if not r['id'].startswith('exp-v19-')]
by = {r['id']: r for r in recs}
def setf(i, **kw):
    if i in by: by[i].update(kw)
setf('exp-p', tagStyle={'preset': 'projgen'})
for lid, src in [('exp-l-wb', 'Example Seeds'), ('exp-l-li', 'Heirloom swap group'), ('exp-l-tr', 'Example Seeds'), ('exp-l-bc', 'Local nursery')]:
    if lid in by and not by[lid].get('source'): by[lid]['source'] = src
for i, fl in [('exp-i-lf2-p03', ('2025-12-18', '2025-12-27', '2026-02-24')), ('exp-i-lf2-p07', ('2025-12-20', '2026-01-03', '2026-02-28')), ('exp-i-tf2-p02', ('2025-12-10', '2025-12-21', '2026-02-15')),
              ('exp-i-lf2-p02', ('2025-12-22', '2026-01-06', '2026-02-20')), ('exp-i-tf2-p03', ('2025-12-12', '2025-12-24', '2026-02-10'))]:
    setf(i, flowers={'male': fl[0], 'female': fl[1], 'first': '', 'end': fl[2]})
setf('exp-i-lf2-p03', name='Shed Queen', selection={'decision': 'kept', 'reasons': ['Meets target: Storage life', 'Meets target: Sweet, dense flesh', 'Healthy and vigorous'], 'note': 'Still firm after seven months in the shed.', 'date': '2026-05-02', 'goalV': '1'})
setf('exp-i-lf2-p07', name='Gem', selection={'decision': 'kept', 'reasons': ['Meets target: Small seed cavity', 'Productive'], 'note': 'Smallest cavity of the 10.', 'date': '2026-05-02', 'goalV': '1'})
setf('exp-i-tf2-p02', selection={'decision': 'kept', 'reasons': ['Healthy and vigorous', 'Meets target: Fruit 1 to 2 kg'], 'note': '', 'date': '2026-05-02', 'goalV': '1'})
setf('exp-i-lf2-p01', selection={'decision': 'rejected', 'reasons': ['Diseased', 'Poor storage'], 'note': 'Powdery mildew early.', 'date': '2026-02-01', 'goalV': '1'})
setf('exp-i-lf2-p04', selection={'decision': 'rejected', 'reasons': ['Poor flavour'], 'note': 'Watery.', 'date': '2026-04-10', 'goalV': '1'})
new = [
 {'id': 'exp-v19-cx', 'type': 'cross', 'date': '2026-12-20', 'motherId': 'exp-i-lf3-1', 'fatherId': 'exp-i-cb-1', 'method': 'Hand pollinated', 'status': 'Planned', 'projectId': 'exp-p', 'code': '26C-4', 'outcome': '', 'notes': 'Bring the combined line back to the best F3.', 'goalV': '1'},
 {'id': 'exp-v19-grp', 'type': 'individual', 'isGroup': True, 'code': 'MIX-G01', 'name': 'Front border mix', 'mix': [{'strainId': 'exp-s-tr', 'count': 3}, {'strainId': 'exp-s-bc', 'count': 4}], 'count': 7, 'strainId': '', 'projectId': '', 'generation': '', 'startDate': '2026-09-25', 'placeId': 'exp-pl-mound', 'status': 'Active', 'photoIds': []},
 {'id': 'exp-v19-in1', 'type': 'input', 'name': 'Seaweed tonic (example)', 'category': 'fert', 'unit': 'mL', 'rate': '30 mL per 9 L watering can', 'organic': True, 'qty': 800, 'opened': '2026-09-01', 'expiry': '', 'notes': 'Example only.', 'whp': {}, 'photoIds': []},
 {'id': 'exp-v19-ap1', 'type': 'apply', 'date': '2026-09-28', 'inputId': 'exp-v19-in1', 'amount': 60, 'unit': 'mL', 'method': 'Watered in', 'reason': 'Transplant shock', 'targets': ['exp-pl-rb1', 'exp-i-lf3-1', 'exp-i-lf3-2', 'exp-i-lf3-3'], 'scope': {'type': 'place', 'id': 'exp-pl-rb1'}, 'repeatDays': 14, 'notes': ''},
 {'id': 'exp-v19-pr1', 'type': 'product', 'name': 'Squash', 'kind': 'plant', 'unit': 'fruit', 'alsoWeight': True, 'weightUnit': 'kg', 'notes': ''},
 {'id': 'exp-v19-l1', 'type': 'list', 'name': 'Squash I grow every year', 'notes': 'The reliable ones.', 'trade': False, 'ltype': 'free', 'status': 'open', 'items': [{'ref': 'exp-s-wb'}, {'ref': 'exp-s-bc'}, {'ref': 'exp-s-tr'}]},
 {'id': 'exp-v19-l2', 'type': 'list', 'name': 'Seed swap table', 'notes': 'Spare seed for the autumn swap.', 'trade': True, 'ltype': 'swap', 'status': 'open', 'contact': 'Find me at the swap table', 'area': 'Example town', 'postsTo': 'local', 'postage': {'mode': 'pickup', 'amount': '', 'extra': ''},
  'items': [{'ref': 'exp-l-li', 'offer': 'seed', 'bag': 10, 'reserve': '', 'price': {}, 'manual': ''}, {'ref': 'exp-l-tr', 'offer': 'seed', 'bag': 8, 'reserve': '', 'price': {}, 'manual': ''}]},
]
for k, (ind, q, w) in enumerate([('exp-i-lf2-p03', 3, 5.2), ('exp-i-lf2-p07', 4, 4.1), ('exp-i-tf2-p02', 6, 9.8), ('exp-i-lf2-p02', 3, 4.4), ('exp-i-tf2-p03', 5, 8.1)]):
    new.append({'id': f'exp-v19-y{k}', 'type': 'yield', 'date': '2026-04-12', 'productId': 'exp-v19-pr1', 'qty': q, 'weight': w, 'unit': 'fruit', 'quality': 'Good', 'targets': [ind], 'scope': {'type': 'single'}, 'notes': ''})
d['records'] = list(by.values()) + new
d['name'] = 'Plant example: Pantry Keeper squash'
pph, ppids = photo_records('exp-')
if pph: d['photos'] = pph
for r in d['records']:
    if r['id'] in ppids: r['photoIds'] = ppids[r['id']]
json.dump(d, open(P, 'w'), indent=1, ensure_ascii=False)
print('plant example:', len(d['records']), 'records')
