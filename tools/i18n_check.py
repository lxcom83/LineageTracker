#!/usr/bin/env python3
"""Check each language file in lang-src/ against the English master (lang-src/en.json).
Reports missing wording, leftovers that no longer exist, and {placeholder} mismatches.
Exit code 1 when a placeholder is wrong (a broken sentence); missing wording is only reported."""
import json, glob, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import i18n_extract
cur = i18n_extract.main(write=False)
ph = lambda s: sorted(re.findall(r'\{(\w+)\}', s))
bad = 0
for f in sorted(glob.glob('lang-src/*.json')):
    code = os.path.basename(f)[:-5]
    if code == 'en': continue
    d = json.load(open(f, encoding='utf-8')); st = d.get('strings', {}); pl = d.get('plurals', {})
    missing = [k for k in cur['strings'] if k not in st]
    extra = [k for k in st if k not in cur['strings']]
    wrong = [k for k, v in st.items() if k in cur['strings'] and ph(k) != ph(v)]
    for k, forms in pl.items():
        if k in cur['plurals'] and any('{n}' not in v for v in forms.values()): wrong.append(k)
    done = len(cur['strings']) - len(missing)
    print(f'{code}: {done}/{len(cur["strings"])} translated ({100*done//max(1,len(cur["strings"]))}%), {len(missing)} missing, {len(extra)} unused, {len(wrong)} placeholder problems')
    for k in wrong: print('  PLACEHOLDER', repr(k)); bad += 1
    if '-v' in sys.argv:
        for k in missing: print('  MISSING', repr(k))
        for k in extra: print('  UNUSED', repr(k))
sys.exit(1 if bad else 0)
