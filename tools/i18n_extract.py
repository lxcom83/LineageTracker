#!/usr/bin/env python3
"""Collect every translatable English wording from the source into lang-src/en.json.
Finds tl('..'), tlp(n,'one','many'), tlx('..'). Run from the project folder."""
import re, glob, json, sys
SRC = [f for f in sorted(glob.glob('js*.js')) + ['i18n.js', 'i18n-ui.js'] if f != 'app.js']
STR = r"""(?:'((?:[^'\\\n]|\\.)*)'|"((?:[^"\\\n]|\\.)*)"|`((?:[^`\\$]|\\.|\$(?!\{))*)`)"""
def unq(m, i0=1):
    s = next(g for g in m.groups()[i0-1:i0+2] if g is not None)
    return re.sub(r"\\(.)", lambda x: {'n': '\n', 't': '\t'}.get(x.group(1), x.group(1)), s)
RE_TL = re.compile(r"\b(?:tl|tlx)\(\s*" + STR)
RE_LBL = re.compile(r"\bsaveLabel:\s*" + STR)
# Wording passed to helpers that translate it themselves (toast, F.* labels and placeholders, fact, factLink, sec, sheet titles,
# photoField, and error messages that end up in a toast).
RE_HELP = re.compile(r"\b(?:toast|fact|factLink|sec|sheet|formSheet|photoField|searchBox|new Error)\(\s*" + STR)
RE_F = re.compile(r"\bF\.(?:text|area|date|month|select|check|ref)\(\s*'[^']*',\s*" + STR)
RE_PH = re.compile(r"\bF\.(?:text|area)\(\s*'[^']*',\s*" + STR + r"\s*,\s*[^,()`]+?\s*,\s*" + STR)
RE_TLP = re.compile(r"\b(?:tlp|plural)\(\s*[^,()]+(?:\([^()]*\))?[^,()]*,\s*" + STR + r"\s*(?:,\s*" + STR + r")?")
def main(write=True):
    strings, plurals, where = {}, {}, {}
    for f in SRC:
        txt = open(f, encoding='utf-8').read()
        for m in RE_TL.finditer(txt):
            k = unq(m); strings[k] = k; where.setdefault(k, f)
        for rx in (RE_HELP, RE_F):
            for m in rx.finditer(txt):
                k = unq(m)
                if k.strip(): strings[k] = k; where.setdefault(k, f)
        for m in RE_PH.finditer(txt):
            g = m.groups(); k = next((x for x in g[3:] if x is not None), None)
            if k and k.strip(): k = re.sub(r"\\(.)", lambda x: x.group(1), k); strings[k] = k; where.setdefault(k, f)
        for m in RE_LBL.finditer(txt):
            k = unq(m); strings[k] = k; where.setdefault(k, f)
        for m in RE_TLP.finditer(txt):
            g = m.groups(); one = next(x for x in g[:3] if x is not None)
            many = next((x for x in g[3:] if x is not None), one + 's')
            plurals[one] = {'one': '{n} ' + one, 'other': '{n} ' + many}
    out = {'strings': dict(sorted(strings.items())), 'plurals': dict(sorted(plurals.items()))}
    if write:
        json.dump(out, open('lang-src/en.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f'{len(strings)} strings, {len(plurals)} plurals -> lang-src/en.json')
    return out
if __name__ == '__main__': main()
