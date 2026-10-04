# Changelog

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
