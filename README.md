# Lineage Tracker

**Breeding records for plants and animals.**

A breeding journal for plants and animals that runs entirely on your own device.
Keep a seed and stock library with germination tests, tag individual plants and
animals, record crosses and pairings, choose what each project measures
(harvests, storage trials, weigh-ins, litters, your own fields), compare
candidates side by side, trace bloodlines in a family-tree chart, record where
each plant grows or animal lives, and keep a dated log of notes and photos. A
due list keeps track of what needs doing next.

No account and no server. Records and photos stay on the device.

## Put it online with GitHub Pages (free)

The address only serves the app. Your records never leave your device.

1. Sign in at github.com and create a new repository named `lineage`.
   Make it **Public** (free Pages sites need a public repository).
2. On the empty repository page, choose **uploading an existing file** and drag
   in everything from this folder: `index.html`, `sw.js`,
   `manifest.webmanifest`, `icon-192.png`, `icon-512.png`, `README.md`, and
   the `examples` and `docs` folders (drag the folders themselves so their
   names are kept), and `config.example.json`. Commit the files.
3. Go to **Settings > Pages**. Under Branch choose `main` and `/ (root)`, then
   Save.
4. After a minute or two the site is live at
   `https://YOUR-USERNAME.github.io/lineage/`.
5. Open that address in Chrome on your phone, tap the menu, then
   **Install app** (or **Add to Home screen**).

Never upload backup files or your starter file to the repository. Everything in
a public repository can be seen by anyone.

**Updating later:** upload the new files over the old ones, including
`docs` and `examples`. The installed app picks up the new version the next
time it opens with internet. Your records are not affected.

Keep using the same address. Each address has its own separate storage, so if
you ever move Lineage Tracker, back up first and restore at the new address.

## Examples

New users can load a plant example (a squash project with two lines, an F2
family, storage trials and germination tests) or a chicken example (a Blue
Australorp laying line over three generations) from the welcome screen or
Settings. Example records are marked and can be removed in one step without
touching your own records. The files live in `examples/`.

## Bringing in existing records

`docs/DATA-FORMAT.md` explains the data structure in plain English, with a
schema (`docs/lineage-schema.json`) and a ready-made prompt for converting old
spreadsheets, app exports or notebook photos with Claude or ChatGPT.
`docs/CHANGELOG.md` lists changes between versions.

## On a computer, without the internet

Double-click `index.html`. Chrome, Edge and Firefox all work. Records saved this
way are separate from the phone's; use a backup to move them across.

## Backups

Everything lives in the browser's storage on one device, so keep copies
elsewhere.

- **Full backup** (Home or Settings, **Back up now**): one zip file with every
  record and photo. Inside are your photos as normal image files and spreadsheet
  (CSV) copies of every record, so your data is readable even without Lineage Tracker.
  Lineage Tracker restores straight from the zip; there's no need to unzip it.
- **Quick backup** (on phones): records only, small enough to send to Google
  Drive or email after every session.
- Copy full backups to a USB stick, SD card, computer or cloud drive. Lineage Tracker
  reminds you when changes pile up.
- **Restoring** (Settings, **Restore or import a file**) adds what's missing
  and only overwrites a record when the backup's copy is newer. **Undo last
  restore** puts things back if you restore the wrong file.
- **Recycle bin:** deleted records stay for 30 days before they're removed for
  good.

## What each project tracks

Each breeding project can add record types:

- Suggested for plants: Fruit harvest, Storage check (logged against each
  fruit, and shows how many days it keeps), Plant check.
- Suggested for animals: Weigh-in, Litter or clutch, Egg count, Health event.
- Or build your own with number, score, choice, text, date, yes/no and
  calculated fields.

Lines share their parent project's record types. The project page compares every
tagged member on scores and measurements, and can log one storage check for
every stored fruit at once.

## Modes: simple or detailed

On first open, Lineage Tracker asks two things: what you keep (plants, animals or
both) and how you'll use it.

- **Garden:** seed library, check before buying, season plan, notes and photos,
  a simple list of your plants, reminders and backups.
- **Seed saver:** adds saving seed and offspring with parents, crosses,
  germination tests, places, harvests and storage checks, seed-saving guidance,
  weather, labels and sharing.
- **Breeder:** everything, including projects, goals, scoring, the bloodline
  chart, cross planner, inbreeding checks, progress charts and the import wizard.

Change mode any time in Settings, or switch single features on or off. Nothing
is deleted when you switch.

## Help, feedback and testing

Settings, Help and feedback opens the feedback form on lineagetracker.org with
the app's version and device filled in. Links of the form
`https://app.lineagetracker.org/#/try/plants` (or `/animals`) open an example
straight away, which is handy for testers.

## Workspaces, pedigrees and more

- **Workspaces:** examples, libraries other breeders share with you, and your own
  split-off lists each live in their own workspace, so nothing mixes with your
  records. Only "My records" syncs.
- **Pedigree certificates and provenance sheets** print from any plant, animal
  or seed lot.
- **Cross codes** like 26C-1, **imperial units**, **weather-station import**
  and optional **passphrase protection** for synced data.

## Inputs and history

- **Inputs:** set up the fertilisers, sprays, medicines and feeds you use once,
  then log them against plants, animals, beds, pens, trays or projects with
  amounts. Withholding periods and repeat reminders show in the due list, and
  each plant or animal shows its season totals.
- **Share a history:** a printable report, short summary or spreadsheet of one
  plant's or animal's records, for a vet, adviser or friend.

## Sharing, swapping and selling

- **Share with a friend** from any variety, packet or plant: an image and a
  friendly message, with an optional gift file they can open in their own
  Lineage Tracker.
- **Selling and swapping** is off until you turn it on in Settings. Then list
  seeds, cuttings, young plants or animals with a price (or free or swap),
  postage and how many are available, and share single offers, a catalogue
  image, a text list for groups or a printed catalogue.
- Lineage Tracker never handles payment and never adds your name, address or
  phone number. Only what you type into a listing is shared.

## Goals, weather and sharing

- **Versioned goals:** each project has a goal charter (goal, scope, success,
  timeframe). Revisions get version numbers, a reason, and a snapshot of the
  target traits. A yearly review reminder keeps long projects on course.
- **Weather:** add a site with your location under **Weather**. Lineage Tracker
  downloads regional weather from Open-Meteo, compares each season with a usual
  year, and lays your crosses and harvests over the season's rain and
  temperature. If you keep your own rain gauge and thermometer, turn on manual
  readings for the site.
- **Share:** the **Share** button on plants, animals, projects and the
  bloodline chart makes a ready-to-post image and caption.

## Importing records from elsewhere

**Settings > Import from a spreadsheet or another app** reads CSV files and
the friendly import format described in `docs/DATA-FORMAT.md`, with a preview
before anything is saved and one-tap undo. The guide includes a prompt for
converting old records or notebook photos with Claude or ChatGPT.

## Sync across devices (optional)

Use the same records on your phone, tablet and computer through your own
Google Drive. It's off by default, and Lineage Tracker can only see the files it
creates. Whoever hosts the site sets it up once by following
`docs/SYNC-SETUP.md` and adding a `config.json` file; after that, anyone can
turn it on in **Settings > Sync across devices**. Sync only works from the web
address, not from a file.

## Bloodline chart, places, germination and the due list

- **Bloodline chart** (project page): founders across the top and a row per
  generation. Each box shows how much of each founder it carries. Tap a box to
  trace its ancestors and descendants; large families fold up until tapped.
  Save the chart as an image.
- **Main photos:** choose and frame the photo that represents each plant,
  animal, variety, project or place. It appears in the chart and lists.
- **Places:** garden beds, raised beds, pots, coops, pens. Compare results by
  place, and moving a plant or animal is logged automatically.
- **Germination tests** on lots, with a regrow alert below your threshold.
- **Due list:** fruit set checks, storage checks, germination tests, low seed,
  repeating checks and your own reminders. Adding items to your phone's
  calendar is optional and off by default.

## Smart features (optional, off by default)

Settings has three ways to have Claude read packets and labels or answer questions
about your records: copy and paste with your existing Claude or ChatGPT app
(free), a Google Gemini API key (automatic, with a free tier; Google may use free-tier content to improve its products), or a Claude API key (automatic, billed per use by Anthropic).

## Files

- `index.html`: the whole app
- `sw.js`, `manifest.webmanifest`, `icon-*.png`: let it install and work offline
- `examples/`: plant and chicken example data
- `docs/`: data format, schema, changelog and sync setup guide
- `brand/`: the logo (`lineage-tracker-logo.png`, transparent background) and the versions built into the app
- `config.example.json`: copy to `config.json` and fill in your Google client
  ID (for sync), your site address (used in share links) and an optional
  donation link

## Licence

Lineage Tracker is free to use, and its code is published so anyone can check how it works. It is not open source: copying, modifying or hosting the code needs permission. Clubs, seed libraries and businesses can offer their own relabelled version for free with the "Make it yours" kit at https://lineagetracker.org/partners.html. See LICENSE.md, RELABELLING.md and TRADEMARKS.md.
