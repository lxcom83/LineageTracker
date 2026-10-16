# Translating Lineage Tracker

English wording lives in the code and is also the key. A language file maps that English wording to the translation. Anything not translated shows in English, so a half-finished language still works.

## For developers
- `tl('Add note')` for wording; `tl('Tagged {code}', { code })` for inserted values (a translator can move `{code}`).
- `tlp(n, 'plant', 'plants')` for counts ("1 plant", "2 plants"). Languages with more plural forms (`one`, `few`, `many`, `other`) add them in the file.
- `tlx('Seed packets')` marks wording stored in a table; the code that uses the value calls `tl(value)`.
- Nothing is escaped by `tl`. Keep wrapping in `h()` where the text lands in HTML.
- These helpers translate their wording themselves, so pass plain English: `toast()`, the form fields `F.text/area/date/month/select/check/ref` (label, placeholder, option text, "none" text, group labels), `fact()`, `factLink()`, `sec()`, `sheet()` and `formSheet()` titles, `photoField()`. Error messages thrown with `new Error('...')` reach the person through `toast()`, so they are translated too. The extractor picks all of these up.
- Fixed wording inside HTML templates is written as `${h(tl('Wording'))}`. The scripts used for the first migration (tlwrap.mjs, tlwrap2.mjs, which need the acorn parser) are kept in the handover qa-tools folder; new wording should simply be written that way from the start.
- Keys must be literal strings so the extractor can find them. Do not build a sentence by joining pieces; use one `tl` with `{values}`.
- After changing wording: `python3 tools/i18n_extract.py` (updates `lang-src/en.json`), then `python3 tools/i18n_check.py` (add `-v` to list missing wording).
- `?lang=pseudo` in the address shows every translated string as accented text in brackets. Plain English that appears while pseudo is on has not been migrated yet.

## For translators
Copy `lang-src/en.json` to `lang-src/<code>.json` (for example `es.json`), add a `meta` block and translate the values:

```json
{ "meta": { "name": "Español", "beta": true },
  "strings": { "Add note": "Añadir nota", "Tagged {code}": "Etiquetado {code}" },
  "plurals": { "plant": { "one": "{n} planta", "other": "{n} plantas" } } }
```
Keep every `{placeholder}` exactly as written. Run `python3 build.py` to build `lang/<code>.js`. Keep `"beta": true` until a native speaker has checked it.

## Rules the app follows
- The language is never changed for you. A device in another language gets a suggestion in Settings only.
- Right-to-left languages (ar, he, fa, ur) switch the page direction.
- Dates and numbers follow the language; English keeps the device's own format.
- Fonts and share pictures for other writing systems are added per language when that language is.
