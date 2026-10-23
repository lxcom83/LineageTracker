# Changelog

## 0.30.2 (no data format change)
- Kind view: `kindsKept()`, `viewKind()`, `setViewKind()`, `inKindView()` and `kindDefault()` in `js11.js`. When more than one of plants, animals and other things is kept, a header button (`#kindBtn`, `updateKindBtn()` and `kindMenu()` in `js33.js`) shows one kind at a time or everything. The choice is stored on the device only (`localStorage` key `lt.kindview`), never in the records or backups. `keepsNow()` and `keepsKind('product')` follow the view, so wording and features match; the tagged, library, crosses and projects lists filter by it; in the all view tagged rows say Plant or Animal. The "what do you keep" setting is unchanged.
- AI key from the website account: Settings has a box (`accountKeyHTML()`, `useAccountKey()` in `js14.js`) that opens the locked code copied from the website account page (`LT-AIKEY1:` plus base64 JSON `{p, m, b}`, blob `{v:1, iter, salt, iv, ct}`, PBKDF2-SHA-256 and AES-GCM) with the account password, on the device, and sets the Claude or Gemini key as if typed. No network call.
- Get the key from the member's own storage: "Get it from my Google Drive / Dropbox" buttons (`fetchStoredKey()` in `js14.js`, wired in `js3.js`) read `ai-key.ltkey` (the same locked code), which the website's account page puts there with the same Google client ID and Dropbox app key (Drive: appProperties lineageRole=aikey, in the app's sync folder; Dropbox: /ai-key.ltkey in the app folder). Read only; never switches sync on (Dropbox needs Dropbox already connected in Sync, since signing in from here would turn sync on). The code still needs the website password to open.
- Settings always shows everything you keep: the kind view does not apply on the Settings page, and the switch is hidden there (`kindViewOff()`).
- Spanish: es 2188/2188.

## 0.30.1 (no data format change)
- Welcome page wording by what the person keeps (`welcomeLine()` in `js2.js`): animals only, plants only, both, or only products; the "Just looking around" paragraph lists only the examples offered; "Everything stays on this device." is translated.
- Hatch calendar: the candling and stop-turning tip shows only when an egg batch is on the go (it showed for pig births).
- Spanish: share-style settings (branding options, caption hint) and every `emptyBox` message; `tools/i18n_extract.py` now collects `emptyBox` text and button labels. es 2176/2176.

## 0.30.0 (no data format change)
- Spanish batch 4 (es 2144/2144): label size names and gap options (`SIZE_NOTES`, `sizeLabel` in `js32.js`), list names and blurbs (`js23.js`), group chips (`js22.js`), seed-saving headings (`js11.js`), `emptyBox` now translates its text and label (`js2.js`), read-only / give-code strings (`js15.js`), the how-to guide (`js17.js`), flowering message (`js24.js`), bin text (`js4.js`), coiChip prefix (`js12.js`). Example data stays English by design. Native-speaker review still needed.

## 0.29.0 (no data format change: new optional settings and optional fields only)
- Hatch and birth calendar: `#/hatch` (`pHatch`, `hatchBatches` in `js29.js`), shown when the `animalDue` feature is on, linked from the Pairings page. Batches come from pairings whose parents are animals and whose species has a gestation or incubation time (`REPRO`, `js12.js`); eggs use `eggsSet`, others the pairing date; a pairing with a hatch or birth record, or status Successful, counts as finished. Eggs show candling (day 7) and stop-turning (3 days before hatch) marks; overdue batches are flagged; eggs with no set date are listed under Needs a date.
- Share styles: `S.settings.shareStyles` (up to 6: `{id, name, hashtags, brand: 'full'|'discreet', template}`) and `shareStyleLast`; the credit line is never off. Built from the old `shareBrand` and `shareTemplate`, which are kept in step for older copies.
- Shared smart keys: `S.sync.shareKeys` (off by default; only with a sync passphrase; `keysOnAt` stamps the choice). Keys travel only inside the encrypted sync copy; a device with the switch off passes them through untouched.
- Dry inputs: input records gain optional `prodForm` (`'dry'`), coverage and `petWarn` fields; units pellets and handful.
- First-run card: `S.settings.controlSeen`.
- Partner versions: signed links checked on the device (`PARTNER_KEYS`, `verifyPartnerLink` in `js19.js`); unsigned and expired links go back to plain Lineage Tracker. The "Powered by" credit always shows.
- Spanish: batch 3 (Settings feature list, log tags, colour genetics names and phenotypes, label settings, search boxes, theme names) and the new calendar. 2108/2108.
- Fix: "Add a animal" is now "Add an animal"; the add-variety and add-breed buttons are translated.

## 0.28.2 (no data format change: new optional list flag `siteManaged`)
- Lists: optional `siteManaged` (checkbox "I manage this list's stock and prices on the website"). When set, the list page shows "Import changes from LT-Catalogue", which reads a `.lt-update.json` file (`app:'lt-update'`, `catalogueId` = list id, `items:[{key, price, available}]`, key = the list item's `ref`), lists each change old to new, and on Apply sets the list item's `price` and `manual` availability (`js21.js importListUpdate`). Unknown keys are ignored; an update for another list is refused.

## 0.28.1 (no data format change: new optional setting `updatesOff`)
- Cloud panel: master switch "All online features" at the top (same `S.settings.offline`, now shown positively), and a switch on every connection even when not set up: sync, AI help, weather, club check, and app updates (`S.settings.updatesOff`; `sw.js` serves the app from cache while the `lineage-flags` cache holds `no-update-check`).
- Log an input: "Applied to" is now tick boxes for any number of places (beds, pots), projects and trays, plus single plants or animals; one log covers them all (`js16.js`, `scope` is `pick` when mixed, a single bed or project keeps its old shape). Log text lists the names.
- Inputs list shows the label photo as the thumbnail (`js16.js`).
- Fix: the cloud icon in the Settings note had no size and filled the page (`head.html`).

## 0.28.0 (no data format change: new `product` kind and `S.settings.other`, both optional)
- "Other things": a third thing to keep besides plants and animals. `S.settings.other` (boolean) beside `S.settings.keeps`; with neither plants nor animals `keepsNow()` is `'none'` and only labels, share, lists, offers and import show (`PRODUCT_ONLY` in `js11.js`). New `product` strain kind, `product` stock form and `product` offer type; starts empty (no starter groups).
- Setup asks with three tick boxes and Continue; Settings has a combined "What you keep" choice (`KEEP_COMBOS`).
- Library filter chips show Plants, Animals and Other when more than one is kept; the add-item form hides species and hybrid fields for goods.
- Share sheet: Picture size (Small, Medium, Large) resizes the photos in a catalogue file at share time (`SHARE_Q`, `js21.js`); records are unchanged.
- Fix: Settings crashed when the due list feature was off (`js3.js`).

## 0.27.5 (no data format change)
- Sharing a list now ends with a one-line pointer to LT-Catalogue for sellers.
- Pig example: `examples/pigs-example.json` (Kunekune herd: 3 breeds, 20 tagged pigs, litters with farrowing dates, a pregnant sow with a birth-due reminder, paddock rotation, worming and vaccine records with withholding, weigh-ins, a breeding plan, 33 cartoon pictures). Built by `tools/make_pig_example.py` with the art in `tools/example_art3.py`. Opens from `#/try/pigs`, the home-page example buttons and Settings.
- The withholding notice on the due list now shows as Today while it is active, instead of overdue from the day it was given (`js16.js`).
- Spanish: withholding words and scope wording, example toasts and buttons.
- Spanish batch 2: due-list sentences (`js5.js`, `js7.js`, `js11.js`, `js12.js`, `js14.js`, `js16.js`, `js21.js`), Log filters (`js28.js`), sticker presets and field labels (`js32.js`) and the Lists tabs now go through `tl()`. Spanish is 1860/1860. Plural forms added for lot and seedling.

## 0.27.4 (no data format change)
- Input sheet (`inputSheet` in `js16.js`, `labelBoxHTML`/`mountLabelReader` in `js31.js`): Take photo / Choose photo buttons and the photo thumbnails now sit at the top, in the same layout as the packet scan; up to two photos (front and back); the label is read automatically as soon as a photo is added when smart features are on, with a Read the label again button; the copy-and-paste box shows only in manual mode (paused or offline) after a photo, and a one-line hint shows when smart features are off. Scan label in Library, Inputs opens the same sheet. The bottom Label photo field is gone.

## 0.27.3 (no data format change)
- First real language: Spanish (`lang-src/es.json`, beta, neutral Spanish with tú). All 1,675 migrated phrases and the 10 plural forms are translated; `tools/i18n_check.py` reports 100% and no placeholder problems. Settings, Language now offers English and Español.
- First-run setup, Getting started checklist and the home quick buttons are now translated (they were plain English before).
- Still English in Spanish: dashboard counters and the More page tiles, built-in categories and record types, filters, and the example data. These need to be migrated screen by screen, as before.

## 0.27.2 (no data format change)
- Seed tray page: the hint above the cells now explains the tap cycle (once = up, twice = didn't come up, three times = back to waiting).
- Germination test sheet (`germSheet` in `js5.js`): while a test is in progress, a button "Finish test: the rest didn't come up" ticks Test finished and saves, so any counts typed are kept and uncounted seeds simply count as not coming up.

## 0.27.1 (examples only, no code change)
- Every bird and plant in the three built-in examples now has its own sample picture (cartoon drawings tagged SAMPLE IMAGE, with photo labels): hens, roosters, pullets and cockerels in each breed's colours with leg bands for the generation, chicks, flocks, and squash plants at different stages (seedling, growing, flower, fruit, weak and culled, selected) with a plant tag showing the code. Drawn by `tools/example_art2.py`, added by `tools/make_individual_pictures.py` (run after `make_examples.py` and `make_example_media.py`; re-runnable, ids start `exi-`). No real photos, so nothing to license.

## Unreleased (examples only, no code change)
- The three built-in examples now include sample pictures (drawings tagged SAMPLE IMAGE) with photo labels, front and back photos on the squash packets, a Log note that is not linked to anything, and a Breeding plan on each example project (periods, locked-in and planned boxes, planned and recorded crosses, quantity boxes, a block or pen). Built by `tools/make_example_media.py` after `tools/make_examples.py`.

## 0.27.0 (no data format change; new sync settings `keepRule`, `lastSnapshotDay`)
- Automatic backups (`js35.js`): while sync is on, `maybeSnapshot()` makes one records backup a day (was weekly) in the sync folder's snapshots folder, named `lineage-records-YYYY-MM-DD.json` (sealed when sync is passphrase-protected). Photos are not duplicated: they are already synced one by one.
- Tidying: `backupsToKeep(names, rule)` keeps the newest backup of each of the last d days, w ISO weeks and m months (rules: 7/4/12 default, 14/8/24, last 10, keep all), plus every "keep forever" file (name ends `-keep.json`) and anything without a date. Replaces the old keep-8 rule. Only files in Lineage Tracker's own folder are touched.
- Settings, Sync across devices: a list of backups with date and size, Restore (merges like restoring a file, undoable), Keep forever / Stop keeping (renames the file so every device respects it), Delete, and the keep rule. Providers gained `getSnapshot`, `renameSnapshot` and `size` in `listSnapshots` (Drive and Dropbox).
- Settings, Backups explains that each Back up now is a new file (keep the newest two or three), or that automatic backups are on.

## 0.26.1 (no data format change)
- Settings, Backups shows whether the browser keeps the records permanently (`navigator.storage.persisted()`), the space used (`estimate()`), and an Ask again button (`persist()`). On iPhone and iPad, when not opened from the Home Screen, it explains how to add it first. `mountPersist()` in `js34.js`, called from `render()` on the settings page. The request on every start (in `init`) is unchanged.

## 0.26.0 (data format: new record type `ltdesign`; new settings only)
- LT-Print designs in the app (`js34.js`). Labels page, Design: add a `.ltprint` file made in LT-Print (tools.lineagetracker.org). It is checked and cleaned with `ltpClean()` (same rules as LT-Print's `cleanTemplate`), kept as a record `{ type: 'ltdesign', name, design, from }` (so backups and sync carry it), filled in from the ticked plants, animals, lots, places or trays (`ltpRowOf`), and printed offline.
- No account and no internet are needed to use a design. The design's fonts are embedded in the printed page as data URLs, so "Save as a file" gives a self-contained sheet.
- Supports everything LT-Print saves: text with `{fields}`, dates with a sum (`{today+3y}`), numbering (`{number}`), QR codes, Code 128 barcodes, shapes, lines, pictures (data URLs only), fold-over, and the design's own typed rows.
- The sheet is laid out on A4 or Letter (the app's sticker sheets when the size matches, otherwise as many as fit), or one per page for label printers. It keeps the start-at position and cutting outline. Settings: `settings.lab.design`, `ltpPaper`, `ltpOwn`.
- Designs above about 1.5 MB are refused, to keep sync small. Removing a design moves it to the recycle bin.
- "Print sticker" on plant, animal and lot pages (when Labels is on, and the record is still on the sticker list) opens `#/labels?what=...&pick=<id>` with that record first and ticked.

## 0.25.0 (translation framework; no data format change; new setting `lang`)
- English wording is the key: `tl('text', {vars})`, `tlp(n, 'one', 'many')` (also behind `plural()`), `tlx('text')` to mark wording in a table. Language files are `lang-src/<code>.json`, built by `build.py` into `lang/<code>.js` (loaded by script tag so file:// works) and listed in `LT_LANGS`. Missing wording falls back to English. See `docs/TRANSLATING.md`.
- `?lang=pseudo` shows every translated string as accented text in brackets so unmigrated English is easy to spot.
- `S.settings.lang`, Settings, Language section (beta label, suggest-a-wording link, device suggestion that is never applied by itself). `<html lang>` and `dir` follow the language. Dates and numbers use `LOC()`.
- Migrated: page frame (tab bar, labels), + menu, Library page, common buttons, form save buttons, vocabulary words (`word()`), counts (`plural()`).
- Long words wrap or shorten (CSS), tab labels cut with an ellipsis.
- `tools/i18n_extract.py` writes `lang-src/en.json`; `tools/i18n_check.py` reports missing wording and placeholder mismatches.

## 0.24.0 (data format: `input.dose`; new settings only)
- Share several photos (`js30.js`): picker (2 to 12, oldest first), collage JPEG, slideshow MP4 (WebCodecs plus the vendored mp4-muxer, MIT, Vanilagy; falls back to MediaRecorder MP4 or WebM, then a picture set), picture set for carousels. Shapes: tall 1080x1350, square 1080x1080, story 1080x1920. Buttons on the Log, variety, plant and project pages.
- Share branding option `shareBrand` ('full' default, 'discreet' slim web-address strip) on all share pictures and captions.
- Library Products tab (record type `product` unchanged); `#/products` still works.
- Input label scan (Library, Inputs, Scan label) and `input.dose` `{ amt, max, unit, per, perUnit }` (`perUnit`: `L`, `m2`, `plant`, `kg`) with a "how much to add" calculator on the input page and in Log an input. Saved containers in `settings.containers` (`[{ name, l }]`).
- Sticker label designer (`js32.js`), settings in `settings.lab`; replaces the old three-size label page.
- Library tab bar scrolls sideways on narrow screens. + menu grouped (Add, Record, View and share) with Share photos. Calculator accepts litres, mL, UK and US gallons, US fl oz, m², ft², yd², kg, g, lb; stand-alone Calculator on the Inputs tab; last size per input kept in `settings.doseLast`.
- Animal lists say Pairing (planner, new pairing, codes, toasts) instead of Cross.
- Stickers page: preview sits under the size choices; start-at number moved next to Print.

## 0.23.0 (new record type `vgroup`)
- Manage groups (`#/groups`): `vgroup` records {name, kind} keep empty groups and sync; rename, merge and delete re-tag every variety or breed of that kind; starter lists (24 plant, 14 animal groups) are suggestions in the Group field, which now follows the plant/animal choice.
- Crosses and pairings list (`#/crosses`) with hatches and births; reachable from My garden.
- Library Inputs chips filter by category kind; Place page: Move something here (adds a Moved note) and Log input.
- Wording: Pairing for animals on plant/animal pages; My garden Backups and Export tiles act on tap.

## 0.22.0 (data format: notes may carry `tags`; new record type `logtag`)
- Log tags: `note.tags` (array of keys: built-in, automatic `sys-*`, or a `logtag` id). Tag picker and "Add your own tag" in the note form. Automatic tags on Sown, Took cuttings, Moved, Potted up and Sent packs entries.
- Log filters in the URL (`#/log?about=&tag=&from=&to=&photos=&roll=`): About picker (including general only), tag chips, dates, photos. Roll-up on by default for varieties, projects and places (`roll=0` turns it off).
- "See all in Log" links on variety, plant and project pages; Manage tags page (`#/tags`) with add, rename, merge, delete; `readable/notes.csv` has a Tags column.

## 0.21.0 (no data format change)
- Each list has its own wording: examples and your own animal lists say Stock, breeds and animals; plant lists say seed packets and varieties. A new list asks what it keeps (`keeps` on the workspace record).
- Library header buttons follow the tab: Scan (packets) on Varieties and Lots only and not for animal-only lists, Labels on Lots and Places, Add matches the tab.
- + menu: View the log, and Set a reminder for everyone.
- Log: Share and Delete beside Edit; text on the share picture is editable; Settings, Sharing: default caption template (`shareTemplate`, placeholders {text} {tags} {website} {youtube}); standard caption includes the how-to videos link; Settings, Watch how-to videos.
- Lighter logo in dark mode (light and dark SVGs, chosen by theme).
- Sync pulls on return to the front and every 4 minutes while open.
- Library: tapping a group chip on a variety or breed shows only that group. Crosses and what comes from them take their Group from their parents.

## 0.20.1 (format version 19)
- Breeding plan, new Cross sheet: choose the time period first, then both parents (from that period, with a switch to include earlier ones), then one way, two ways or selfed, then whether to grow out the offspring in the next period and how many. A cross line stores its period (`periodId`). The separate "Add the next plant?" pop-up is folded into this sheet; the remembered answer is still under More.
- Breeding plan: boxes can have a quantity (`qty`), shown as x12, set when adding a cross or by editing a box. Locked-in boxes can be changed to a different real plant or animal after a confirmation that lists what is attached; recorded crosses keep their original parents.
- Fix: on touch screens a pop-up opened by tapping a graph box or finishing a line closed at once. Pop-ups now ignore the tap that opened them. The zoom buttons moved below the graph.
- Pop-ups fit the visible screen above the on-screen keyboard, scroll with a visible scroll bar, and do not pop the keyboard up on phones.
- New plant: optional How many? makes several plants at once, each with its own tag (counting on from the suggested or typed tag), then lists the IDs in one pop-up with a Close button.
- Potting up seedlings: the default label is now the same tag style as New plant (for example BF-P01), not the variety name. Variety name, project tags and tray and cell are still choices.
- Log: a note or photo that is not linked to anything can be shared like a plant, with the Lineage Tracker credit and website.

## 0.20 (format version 19)
- Breeding plan: lay out a project before you know which plants you will use. Each project has a Breeding plan button. Plan in time periods of any length, from a few days to years, for fast indoor cycles as well as yearly crosses (several can be added at once, numbered on: Generation 1, 2, 3), add plants, animals and blocks or pens, and draw crosses (one way, two ways or selfed), grown-on lines and lines into a block. Boxes can be left to be chosen later; choosing the real plant locks the box in, picked in two steps (first a kind you have tagged plants or animals of, then the exact one). Dotted lines are planned; a cross turns solid when you record it from the line. See it as a table (the default on a phone) or a graph, both kept in step. The bottom bar becomes the plan editor (Exit, Line, +, Undo, More). Drawing a cross asks whether to add next period's plant, and can remember your answer. Deleting part of a plan never deletes your real plants or crosses. Format: new `plan` on projects and `planEdge` on crosses, additive.
- Growth phase: the "Made with Lineage Tracker" credit on shared pictures, captions, PDFs and web pages is always on, and the switch that removed it is gone from Settings. Anyone who had already turned it off is back on. (Code: `CREDIT_LOCKED_ON` in js1.js.)
- Scanning a packet: take up to two photos, the front and the back. When a second photo is added, the details on it are read and added to the form without overwriting anything you already have. Choose both from the gallery at once if you like. Each photo is labelled packet front or back, and both are saved with the packet.
- Photo labels: say what a photo shows, such as Seedling, Flower, Harvest, Cut open, Chick, Eggs or Problem, with separate lists for plants and animals. Label photos when you add or edit a note, a variety, a packet or a record; open any photo to change its label; or tap a label right after a quick photo (switch that off in Settings, Photos). Labels show under a note's photos, sync and back up with your records, and are in the data format (4.13) with fixed keys so a database can pick the right photo. Unlabelled photos stay unlabelled.
- Clearer wording: the first-run notice and the twice-a-year donation reminder say the app is free forever, with no ads and no paid tiers, in line with the website.

## 0.19 (format version 19)
- Flowering: one-tap First male flower, First female flower and Flowering finished buttons; a flowering timeline on each project; the cross form and cross page warn when parents' flowering doesn't overlap.
- Colour genetics calculator: ready-made genes for chickens (blue, barring, dominant white, blue eggshell), pumpkins and squash, and tomatoes, plus your own genes; handles dominant, blended and sex-linked traits; results can be saved to a planned cross.
- Clutches, litters and hatches: eggs set, fertile and hatched (or born, stillborn and weaned) with percentages worked out, and offspring created in one tap, individually with tags or as a group.
- Cross cards: share both parents side by side with the cross's stage, from Waiting on flowers or Planned pairing to seeds saved or chicks hatched.
- Naming: tag styles chosen per project (project and generation, selection history, cross, year, simple, breeder prefix, or your own pattern) with a live preview; generations worked out from the parents, including backcrosses and selfing; Add existing plants or animals to a project, optionally re-tagging them with their old tags kept as "also known as"; the Purdy pedigree on every plant; breeder codes (from your user ID unless you choose one) on everything shared; tap any plant on the bloodline chart for its full founder breakdown.
- Sync: Dropbox recommended and shown first, plain connect screen, a reminder to connect your other devices, and a "Sync paused: tap to resume" bar when Google signs out. Move to a new phone in Settings.
- Shared pictures and captions now say "Free at lineagetracker.org".
- Examples: the plant example shows groups, lists, harvests, flowering, selection reasons and a planned cross; a new breeding example follows an Olive Egger chicken line with four founders, two lines, clutches, a backcross and a saved genetics prediction.

## 0.18
- Dropbox sync, alongside Google Drive: the same records, photos, weekly snapshots, passphrase protection and conflict list, kept in the app's own Dropbox folder. Choose either in Settings, Sync. Sign-ins renew themselves.
- Built-in lists: "All my seeds and stock" and "Not on a list yet", with Move ticked to a list for sorting several at once.
- What you're offering on trading lists: seeds, cuttings or clones, slips or tubers, seedlings or plants, divisions, scions, hatching eggs, young, adults, pairs or trios. Wording, bag names and availability follow it, and stock can be entered right in the item.
- Lists collapse any variety or type with three or more entries, plant rows show age then place, and the Group switch appears from four plants.
- Adding a plant: that variety's packets come first and a single match is picked for you; choosing a packet fills in the variety.
- New plant codes for one-word varieties use three letters (CHO-P01). "today" instead of "0 days". The reserve hint follows the bag size as you type.

## 0.17 (format version 17)
- Lists: a new button at the top of the screen. Make your own lists (veggies, flowers, chickens, a seed bank catalogue); one variety can be on several. Lists from others arrive as catalogue files you can browse, star into a wishlist, request from, and import into your library with where they came from kept. Remove a list any time; anything you imported stays.
- Sharing inside lists, when Selling and swapping is on: seeds per bag, a reserve to keep, prices, bags available worked out from your stock, sent and received in swaps, and seed-library lending with return reminders. Share a list as a catalogue file, a PDF, a web page or a text list. Old offers become a list automatically.
- Groups: a bed, patch or flock as one entry, mixed varieties with rough counts. Inputs, harvests, photos and moves apply to the whole group, and a standout can be tracked separately.
- Tester kits (Breeder): send seed with a kit file; testers in any mode record a few things and send results back, which appear in the project with their general area and season weather.
- Collapsible groups in the Library and Plants lists (by type by default, changeable in Settings), plant rows showing place and age, Expand and Collapse all.
- Home: a getting-started checklist for new users (gone after 30 days) and compact quick buttons.
- Selection reasons, measured or estimated numbers, record completeness, a starter trait dictionary, species chosen from your library, and examples drawn from your own library.
- Your name for shared lists and a random user ID (synced), a device name, a sync conflicts list where an overwritten version can be brought back, and a coarse region per site, worked out on the device and not shared.
- Log moved into My garden.

## 0.16
- Reading labels with AI: a spinner and expected time while waiting, a Cancel button, Save waits until the details arrive, busy replies retried automatically, then Try again and (with both keys) the other AI as a backup. Plain wording for busy, free-allowance and offline errors. Ask about your records gets the same.
- Sources inside each variety: each purchase or swap gets a code like Choko-C1 and a received date, and the variety page compares sources (plants grown, germination, harvest). Adding a variety you already have offers to add it as a new source instead; genuinely different plants get a distinct name. Group names are suggested as you type, with a check for near misses. Merge into... combines duplicates.
- How a plant started: from seed (which packet), a cutting or division (which plant), bought as a seedling, or other, shown on the plant's page. Move or repot records the new place with a dated note, and a new bed, pot or pen can be added straight from the list. Propagate is now "Take cuttings or divide".
- Whole fruit or crowns as a form a lot can take.
- Share pictures: the photo takes the space the words don't need, a square option, and lineagetracker.org on every shared picture, caption, catalogue and report. Plant photos get their own caption.
- A gentle donation reminder, twice a year, never in the first six months, and never on top of anything else.

## 0.15.1
- Gemini: the default model is now gemini-3.8-flash, replacing gemini-2.5-flash, which Google has retired for new users. When Google retires a model and names its replacement, the app now switches automatically, remembers it, and tries again.

## 0.15
- Partner versions: clubs, seed libraries, societies and businesses can offer their own version with their name, logo, colours, welcome message, variety list and a chosen set of features, using the "Make it yours" page on lineagetracker.org. Partner versions always show "Powered by Lineage Tracker", keep Lineage Tracker's support links, and keep records on each person's device. Anyone can switch back to plain Lineage Tracker in Settings.
- Licence: all rights reserved, with the code published for transparency, plus free relabelling terms and a trademark notice (LICENSE.md, RELABELLING.md, TRADEMARKS.md).
- Fixes: a stray line of text at the bottom of the screen, and "1 varieties".

## 0.14 (format version 14)
- My garden (or My farm, if you keep animals): a new button in the top bar opens one page with everything you set up: beds and pens, weather, inputs, harvests and products, varieties and packets, season plan, seed trays, labels, reminders, projects, offers, workspaces and backups. Each tile shows a count and has a quick add button.
- Harvests and products: set up what you produce once (eggs, milk, honey, tomatoes, pumpkins with count and weight), then record it against a plant, animal, bed, pen, tray or project. Season totals show on each, alongside inputs, and in the comparison table and history reports.
- The + menu now holds only quick jobs: a note or photo, scanning a packet, adding a plant or animal, sowing a tray, logging an input, recording a harvest, and for animals a pairing and reminders. Setup items moved to My garden.
- Weather moved from Settings to My garden. Places and weather are now available in every mode.

## 0.13
- Help and feedback in Settings: send feedback through the website's form (the app fills in its version, device and mode for you to see and change), how-to guides, how your data is handled, and a link to support the project.
- What's new: a short summary after each update.
- If something goes wrong, a bar appears with details to copy and a pre-filled report.
- "Try an example" links (app address followed by #/try/plants or #/try/animals) open an example straight away, separate from your records.
- First open now explains that records stay on the device and nothing is shared unless you choose.

## 0.12 (format version 12)
- Workspaces: keep separate sets of records on one device. Examples now open in their own workspace, so they never mix with your records and can be reset any time. Open a library another breeder shares with you (read-only unless you allow editing), split your own records into lists such as "Chickens" or "Seed bank", and copy or move a project, variety or plant between them with its family line, notes and photos. Only "My records" syncs.
- Share a workspace as a library file for other breeders to open.
- Printable pedigree certificates for animals and plants (three generations, with registration, ring and microchip numbers, inbreeding figure and a QR code), and provenance sheets for seed and other stock, with parents, cross, germination tests and hand-pollination noted.
- Automatic cross codes such as 26C-1, with your own pattern, shown on crosses and offered for older crosses.
- Units: show and enter weather and new record types in °F, inches and pounds. Records are still stored in metric, so switching back and forth loses nothing.
- Breeder or garden name for pedigrees and provenance sheets.
- Import a home weather station's CSV export as daily gauge readings, with automatic column and unit detection.
- Optional passphrase protection for sync: records and photos are encrypted on the device before they reach Google Drive. Other devices ask for the passphrase once.

## 0.11 (format version 11)
- Inputs: fertilisers, composts, sprays, medicines, vaccines, wormers and feeds set up once in the Library, with the label rate, withholding periods, organic status, stock on hand, use-by date and a label photo. With smart features on, the label can be read from a photo.
- Log an input against one plant or animal, a hand-picked group, everything in a place, a whole project or a seed tray, with the amount, method and reason. Stock comes off automatically.
- Withholding periods (before harvest, eggs, milk or meat) show on each plant or animal and in the due list. Repeating inputs, like a fortnightly feed or worming every three months, come back as due reminders.
- Season totals per plant, animal, place and project, plus an "Inputs this season" column in the comparison table.
- Projects can be set to "no inputs"; logging an input against a member warns you.
- Share one plant's or animal's history: a printable report (save as PDF for a vet or adviser), a short text summary, or a spreadsheet of its records, choosing the date range and what's included.
- Egg log record type for layers, per hen or per pen.
- Tag codes for plants and animals without a project code now use the variety's initials (Ronde de Nice gives RDN-P01) instead of TAG.

## 0.10.3
- The official logo: the leafy tree with a woven double-helix trunk, used for the app, icons and share cards.

## 0.10 (format version 10)
- Seed trays: each tray gets an ID (T01, T02...) and its cells a position (A1, A2, B1...). Tap cells as they come up, see the germination rate and first day up, then pot up the survivors as plants labelled by variety name, project tag or tray and cell. Trays can be saved as a germination test for their packet, printed as QR labels, and show in the due list for checking and potting up. The season plan's Sown button can start a tray.
- Google Gemini as an option for reading packet photos and answering questions, alongside Claude. Google offers a free tier with an AI Studio key; on that tier Google may use what's sent to improve its products.

## 0.9 (format version 9)
- More than seeds: the library holds cuttings, seedlings and young plants, tubers and bulbs, divisions, scions, tissue culture, hatching eggs, and young or adult animals (`form`).
- Cuttings and clones: a Propagate action records cuttings, divisions, runners, grafts or tissue culture, as one batch or individually, linked to the source plant (`cloneOf`, `propMethod`). Clones share their source's family line, founder percentages and inbreeding figure, and appear in the bloodline chart joined by a "clone" line.
- Share with a friend, in every mode: a friendly image and message with no prices, plus an optional gift file the friend can open in their own Lineage Tracker, so the variety's history travels with it.
- Selling and swapping, off unless turned on: offers with price, free or swap, postage per order and per extra pack, availability, posting area and how to arrange. Share each offer as an image and caption, share everything as one catalogue image or a text list for groups, print a catalogue, and record packs sent.
- Lineage Tracker never handles payment or adds personal details: listings contain only what the person types.

## 0.8 (format version 8)
- Modes: on first open, choose what you keep (plants, animals or both) and how you'll use it: Garden, Seed saver or Breeder. Each mode shows only the features it needs, forms tuck advanced fields behind "More details", and Settings can switch any feature on or off. Nothing is deleted when switching.
- Check before buying: look up a name in the shop, even offline, with near-miss matching, F1 hybrid warnings and crossing advice.
- Season plan: list what you'll grow, with checks for enough seed, old or poorly germinating seed, F1 seed you mean to save, and varieties that could cross. Marking an entry sown takes the seed off the packet and can add the plants.
- Seed-saving guidance for common crops: how each pollinates, isolation distances and how many plants to save from.
- F1 hybrid flag on varieties (`hybrid`), set automatically when the name says F1.
- Printable labels with QR codes for plants, animals, seed packets and places, in three sizes. QR codes are generated on the device.
- Cross planner: planned crosses with one-tap "done today", success rates by pairing (`attempts`, `fruitSet`, `seedsSaved`) and, for animals, the lowest-inbreeding pairings.
- Inbreeding coefficient (Wright's method) for each plant or animal and for planned pairings.
- Birth and hatch due dates for common livestock and poultry, with candling and lockdown reminders for eggs (`eggsSet`, `dueDate`).
- Progress by generation on project pages, and scoring sessions that step through a family one plant or animal at a time.
- Ring, microchip and registration numbers for animals, and a show-result record type.

## 0.7
- New name: Lineage Tracker. Breeding records for plants and animals.
- New logo (a tree whose trunk is a woven double helix, navy and copper) and matching colours throughout the app, icons and share cards.
- Proper app icons, including the round-cropped Android version, and a sharp browser-tab icon.
- Repeating checks for plants now stop once the plant's season is over (animals continue for life).
- The data format is unchanged (files still say `"app": "lineage"`), so all earlier backups and imports still work.

## 0.6 (format version 6)
- Import wizard: spreadsheets (CSV) and a new friendly JSON format that links by tag codes and names, so AI conversions are easy to get right. Preview with warnings before saving, duplicates reused rather than copied, whole import undoable. Understands loose values such as Dam and Sire columns, "keep" or "hen", Australian dates and spreadsheet date numbers.
- Share to social media: a ready-to-post image card and editable caption for any plant, animal, project or bloodline chart. Optional "Tracked with Lineage" credit and link.
- Optional donation link and site address in `config.json`.
- Records created by an import carry `importBatch`.

## 0.5 (format version 5)
- Versioned project goals: goal, in scope, out of scope, what success looks like and timeframe. Minor (1.1) and major (2.0) revisions, each with the reason and a copy of the target traits. Changing target traits saves a new minor version automatically. Yearly goal review in the due list.
- Crosses and selections record the goal version they were made under (`goalV`).
- Sites and weather: daily regional weather from Open-Meteo, 20-year usual-year averages, season summaries, month-by-month tables, season calendar chart with crosses, sowings and harvests, seasons compared alongside project results, and the weather on the day of each cross.
- Optional manual rain gauge and thermometer readings per site (`reading` records), compared with the regional data.
- Backups add monthly weather summaries and gauge readings to `readable/`.

## 0.4.1
- With sync on, delete warnings say the change reaches every synced device, and permanent bulk actions (delete from the recycle bin, replace everything with a backup) need a typed confirmation.

## 0.4 (format version 4)
- Optional sync across devices through each person's own Google Drive, using the `drive.file` permission only. Off by default. Set up once per site with `config.json` (see SYNC-SETUP.md).
- Records sync as one file; photos upload once and download on other devices as needed; eight weekly snapshots kept in Drive.
- Deleted records emptied from the recycle bin keep a small marker (`purged: true`) so they stay deleted on every device. Removing example data works the same way.
- "Replace everything with a backup" now moves records missing from the backup to the recycle bin instead of erasing them, and the backup's records win on every device. Undo last restore works the same way.
- Erasing a device turns sync off on it first, so the Drive copy is never touched.
- Cloud button in the header shows sync status; tap to sync or sign in again.

## 0.3 (format version 3)
- Bloodline chart for each project: founder colours, trace mode, folded large families, zoom, save as image.
- Main photo for plants, animals, varieties, projects and places, with framing (`mainPhotoId`, `frame`).
- Places: growing spots and animal housing (`place` records, `individual.placeId`). Moving a plant or animal logs a note.
- Germination tests on lots (`germ` records). Lots now hold numeric `qty`, `unit` and `minQty`; old text `quantity` converts automatically.
- Due list: fruit set checks, storage checks, germination tests, low stock, repeating record types (`recordType.repeatDays`) and reminders (`reminder` records).
- Optional "Add to calendar" (.ics file or Google Calendar link), off by default.
- Plant and chicken example files with explore buttons; example records carry `example: true` and can be removed in one step.
- Backup zip adds `readable/places.csv` and `readable/germination-tests.csv`.

## 0.2 (format version 2)
- Record types per project (`project.recordTypes`) and logged `entry` records, including child entries for trials such as storage checks.
- Comparison table on project pages.
- Zip backups with photos as image files and readable CSV copies; records-only quick backup.
- Restore keeps newer records; undo last restore; 30-day recycle bin (`deletedAt`, `delBatch`, `delRoot`).

## 0.1 (format version 1)
- Library of varieties and lots, tagged plants and animals, crosses, projects with target traits and 1–5 scores, notes with photos, JSON backup.
