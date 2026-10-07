# Lineage Tracker data format

**Format version 19** (Lineage Tracker 0.19). This document describes how Lineage Tracker stores
records, so that people and AI tools can convert existing breeding records
into a file Lineage Tracker can import.

**Converting records from elsewhere? Use the friendly import format in
section 6.** It links records by tag codes and names, the way you already
write them, so it is far easier for people and AI to get right. The full
format below is what Lineage Tracker uses internally and in backups. It is updated with every release that changes
the format; see [CHANGELOG.md](CHANGELOG.md).

Machine-readable version: [lineage-schema.json](lineage-schema.json) (JSON Schema).
Worked examples: [`examples/plants-example.json`](../examples/plants-example.json)
and [`examples/animals-example.json`](../examples/animals-example.json).

---

## 1. Files Lineage Tracker reads

| File | What it is |
|---|---|
| `lineage-backup-YYYY-MM-DD.zip` | Full backup: `lineage.json`, photos and readable CSV copies. |
| `lineage-records-YYYY-MM-DD.json` | Records-only backup (no photos). |
| Any `.json` file in the format below | Import file, e.g. one produced by AI from your old records. |

Import with **Settings > Restore or import a file**. Importing adds new records
and only replaces an existing record (same `id`) when the incoming copy has a
newer `updatedAt`. **Undo last restore** reverses an import.

### Top-level object

```json
{
  "app": "lineage",
  "version": 19,
  "exportedAt": "2026-10-02T09:00:00.000Z",
  "records": [ ... ],
  "photos": [ ... ]
}
```

- `app` must be `"lineage"`.
- `records` is one flat list of every record. Each has a `type`.
- `photos` lists photo files. In a zip they point at image files; in a JSON
  file they may hold `data:` URLs. Leave it as `[]` when converting records.

---

## 2. Conventions

- **IDs:** any unique string, e.g. `"oldbook-plant-17"`. Records link to each
  other by these IDs. Choose a prefix so imports never clash with IDs Lineage Tracker
  creates itself.
- **Dates:** `YYYY-MM-DD`. Best-before dates may be `YYYY-MM`.
- **Text:** plain UTF-8. Leave a field out, or use `""`, when unknown. Never
  invent values.
- **Timestamps:** `createdAt` and `updatedAt` are milliseconds since 1970
  (optional when importing; Lineage Tracker fills them in).
- **Deleted records** carry `deletedAt`, `delBatch` and `delRoot` and sit in the
  recycle bin for 30 days. After that they shrink to a marker
  `{ "id", "type", "deletedAt", "purged": true, "updatedAt" }`, kept so a
  device that hasn't synced yet can't bring the record back. Don't produce
  these when converting.
- **Example records** carry `"example": true`.

## 3. How records connect

```
strain (variety or breed) ──< stock (lot: packet, saved seed, eggs)
   │                              │
   └──< individual (tagged plant or animal) >── place (bed, pot, coop, pen)
            │   motherId / fatherId point at individuals or strains
            │   stockId  = lot it was grown or hatched from
            │   crossId  = cross that produced it
            ├──< entry (record of a project's record type, e.g. a fruit harvest)
            │       └──< entry (child record, e.g. a storage check on that fruit)
            └──< note (dated text and photos; notes can attach to any record)
cross (pairing or pollination): motherId, fatherId ──> stock or individuals
project (breeding program) ──< project (lines, via parentId)
germ (germination test) ──> stock
reminder ──> any record
```

Parentage is read in this order: the record's own `motherId`/`fatherId`, then
its `crossId`, then its `stockId`. So a plant grown from a saved-seed lot whose
lot has parents gets those parents automatically.

---

## 4. Record types

Every record has `id` and `type`. Fields not listed are ignored.

### `strain`: variety or breed

| Field | Type | Notes |
|---|---|---|
| `name` | string | Required. As printed on the packet or breed name. |
| `kind` | `"plant"` or `"animal"` | |
| `group` | string | e.g. `Pumpkin`, `Herb`, `Chicken`. Groups the library. |
| `species` | string | Scientific name, e.g. `Cucurbita moschata`. Used for cross warnings. |
| `speciesVerified` | boolean | True only when confirmed from a packet, breeder or registry. |
| `hybrid` | boolean | F1 hybrid: seed saved from it won't grow true to type. |
| `origin` | string | Breeder, seller or source. |
| `description` | string | |
| `photoIds` | string[] | |
| `mainPhotoId`, `frame` | string, object | Chosen main photo and its framing (see 4.12). |

### `stock`: lot (seed packet, saved seed, cuttings, young plants, hatching eggs)

| Field | Type | Notes |
|---|---|---|
| `strainId` | id | Variety or breed. Empty for seed saved from your own cross. |
| `form` | string | `seed`, `cuttings`, `seedlings`, `tubers`, `divisions`, `scions`, `tissue`, `eggs`, `young`, `adults` or `other`. Missing means seed (plants) or eggs (animals). |
| `cloneOf`, `propMethod` | id, string | For clonal forms: the plant the batch was taken from, and how (Cutting, Division, Runner or sucker, Graft or bud, Tissue culture, Layering, Bulb or tuber offset). |
| `label` | string | e.g. `BF × SA — F2 — Plant 04 — 2028`. |
| `source`, `batch`, `year` | string | `year` is free text: `2026`, `Autumn 2027`. |
| `bestBefore` | `YYYY-MM` or `YYYY-MM-DD` | |
| `qty` | number | Amount held. |
| `unit` | string | `seeds`, `eggs`, `straws`... |
| `minQty` | number | Flag as low below this. |
| `location` | string | Where it is stored. |
| `status` | `"active"`, `"archive"`, `"used"` | `archive` = backup seed not for routine sowing. |
| `projectId` | id | |
| `motherId`, `fatherId`, `crossId` | id | Parents for saved seed or offspring. |
| `notes` | string | |
| `photoIds` | string[] | Label or packet photos. |

Older files may have a text `quantity` instead of `qty`/`unit`; Lineage Tracker
converts it.

### `individual`: a tagged plant or animal

| Field | Type | Notes |
|---|---|---|
| `code` | string | Required, unique. The tag, e.g. `BFxSA-F2-P04`, `BA-H01`. |
| `name` | string | Nickname. |
| `strainId` | id | For founders and pure-variety plants. Often empty for crosses. |
| `projectId` | id | Project or line it belongs to. |
| `generation` | string | `F1`, `F2`, `BC1`, `Outcross`... |
| `sex` | `""`, `"Female"`, `"Male"`, `"Unknown"` | |
| `motherId`, `fatherId` | id | An individual or a strain. Same id twice = selfed. |
| `stockId` | id | Lot it was grown or hatched from. |
| `crossId` | id | Cross that produced it. |
| `startDate` | date | Sown, born or hatched. |
| `status` | string | One of `Active`, `Selected`, `Kept for breeding`, `Harvested`, `Culled`, `Sold or rehomed`, `Died`. |
| `placeId` | id | Current place. |
| `description` | string | |
| `scores` | object | Trait name to score 1–5, e.g. `{"Small seed cavity": 4}`. Names match the project's traits. |
| `goalV` | string | Goal version it was selected under (set when its status becomes Selected or Kept for breeding). |
| `ringId`, `microchip`, `regNo` | string | Optional animal identification. |
| `cloneOf`, `propMethod` | id, string | A clone: genetically the same as the plant it was taken from. Its family line, founder percentages and inbreeding come from that plant. |
| `trayId`, `trayCell` | id, string | The seed tray and cell (such as A1) it was potted up from. |
| `mainPhotoId`, `frame` | | See 4.12. |

### `project`: breeding program or line

| Field | Type | Notes |
|---|---|---|
| `name` | string | Required. |
| `code` | string | Starts suggested tag IDs, e.g. `BFxSA`. |
| `kind` | `"plant"` or `"animal"` | |
| `species` | string | |
| `parentId` | id | Set for a line inside a larger project. |
| `goal` | string | |
| `strainIds` | id[] | Founding varieties or breeds. |
| `traits` | array | `{ "name": "Small seed cavity", "tier": 2, "must": false }`. Tier 1 matters most. `must` = a candidate is out without it. Lines with no traits use their parent's. |
| `recordTypes` | array | Data the project tracks. See 4.11. Lines also get their parent's types. |
| `goals` | array | Goal versions, oldest first: `{ "v": "1.1", "date", "statement", "inScope", "outScope", "success", "timeframe", "reason", "traits": [...] }`. `v` is major.minor; `traits` is a copy of the target traits when that version was made. `goal` always holds the current statement. |
| `goalReviewMonths`, `goalReviewedAt` | number, date | How often to review the goal (default 12) and when it was last reviewed. |
| `siteId` | id | Site whose weather the project is compared with. Lines use their parent's. |

### `cross`: pollination or pairing

| Field | Type | Notes |
|---|---|---|
| `date` | date | |
| `motherId`, `fatherId` | id | Individuals or strains. Same id twice = self. Leave one empty when unknown. |
| `method` | string | `Hand-pollinated`, `Self-pollinated`, `Open-pollinated`, `Natural mating`, `Artificial insemination`, `Other`. |
| `status` | string | `Planned`, `Done`, `Successful`, `Failed`. |
| `projectId` | id | |
| `outcome`, `notes` | string | |
| `goalV` | string | Goal version the cross was made under. |
| `code` | string | The cross code, such as `26C-1`. |
| `attempts`, `fruitSet`, `seedsSaved` | number | Flowers pollinated or matings tried, how many took, and seeds saved or young born. Used for success rates in the cross planner. |
| `eggsSet`, `dueDate` | date | For animals: when eggs went into the incubator or under a hen, and an optional manual due date. Without one, the due date is worked out from the species' gestation or incubation time. |

### `note`

`refId` (any record, or empty for a general note), `date`, `text`, `photoIds`.

### `entry`: one logged record of a project's record type

| Field | Type | Notes |
|---|---|---|
| `rtId` | id | The record type definition (inside a project's `recordTypes`). |
| `indId` | id | The plant or animal. |
| `parentEntryId` | id | For child types, e.g. a storage check points at its fruit entry. |
| `seq` | number | Item number for item types: Fruit 1, Fruit 2... |
| `date` | date | |
| `values` | object | Field id to value. Numbers as numbers, scores 1–5, choices as the option text, dates as `YYYY-MM-DD`, yes/no as `"Yes"`/`"No"`. Calculated fields are not stored. |
| `notes`, `photoIds` | | |

### `place`: growing spot or animal housing

`name`, `kind` (`plant`/`animal`), `method`, `details`, `photoIds`,
`mainPhotoId`, `frame`.

Plant methods: `In ground`, `Garden bed`, `Raised bed`, `Container or pot`,
`Grow bag`, `Mound or hill`, `Greenhouse or polytunnel`, `Hydroponic`, `Other`.
Animal methods: `Free range`, `Coop and run`, `Pen`, `Hutch or cage`,
`Paddock`, `Barn or shed`, `Aviary`, `Pond or tank`, `Other`.

### `germ`: germination test

`lotId`, `date` (started), `method` (`Paper towel`, `Seed tray`, `Soil`,
`Other`), `sown` (number tested), `counts` (array of `{ "day": 7, "n": 8 }`,
running totals of sprouted seeds), `done` (boolean), `notes`.

### `reminder`

`date`, `text`, `refId` (optional), `done` (boolean).

### `site`: a location for weather

`name`, `lat`, `lon` (rounded to 2 decimals, about 1 km), `locLabel`,
`seasonStart` (month 1–12; empty = July in the southern hemisphere, January in
the northern), `heat` (heat-day threshold °C, default 35), `frost` (frost-night
threshold °C, default 2), `gddBase` (growing degree day base °C, default 10),
`manual` (boolean: the person keeps their own instruments), `manualMode`
(`mixed` = gauge readings with regional data for gaps, or `regional`).

Regional weather itself is not stored in records or backups. It is downloaded
from Open-Meteo and cached on each device, and the backup's `readable/` folder
holds monthly weather summaries for each site.

### `reading`: a manual rain gauge and thermometer reading

`siteId`, `date`, `rain` (mm since the previous reading), `tmax` and `tmin`
(highest and lowest since the thermometer was last reset), `notes`. Each
reading covers the days after the previous reading up to its own date.

### Workspaces, units and encryption

Each workspace (your records, an example, a shared library, a split-off list) is a separate set of records on the device; a backup contains the workspace that was open when it was made. Units are a display setting: all measurements are stored metric. Gauge readings imported from a weather station carry `source: "station"`. When sync is protected with a passphrase, the Drive copy is `{ "format": "sync-encrypted", "salt", "data" }` (AES-GCM, key derived from the passphrase); backups made on the device are not encrypted.

### Lists, catalogues and lending (0.17)

`list`: `name`, `notes`, `trade` (used for sharing), `ltype` (`free`, `swap`, `sale`, `mixed`, `library`), `status`, `contact`, `area`, `postsTo`, `postage`, and `items`: `{ ref, bag, reserve, price: { mode, amount }, manual, sent, note }` where `ref` is a variety or lot id.
`received`: a list someone sent you: `sender { userId, name, contact, area }`, `name`, `items` (names, species, bag, price, availability, small photo), `starred`, `imported`.
`loan`: `listId`, `ref`, `who`, `bags`, `date`, `due`, `returned`.
`kit` (breeder) and `trial` (tester): a tester kit and its results.
`profile`: `userId` (random), `displayName`, `devices`. Every record carries `dev`, the id of the device that last changed it.

### Groups and other 0.17 fields

An `individual` with `isGroup: true` is a bed, patch or flock: `mix: [{ strainId, count }]`, `count`. `groupOf` on an individual points to the group it was picked from. `selection: { decision, reasons, note, date, goalV }` records why a plant or animal was kept or rejected. Entries carry `est: { fieldId: true }` for estimated numbers, and harvests `est: true`. Sites carry `region: { lat, lon }`, rounded to half a degree.

### 0.19 additions

`clutch`: a hatch or birth from a cross: `crossId`, `motherId`, `fatherId`, `projectId`, `kind` (`eggs` or `live`), `date`, `eggsSet`, `fertile`, `hatched`, `bornAlive`, `bornDead`, `weaned`, `weanDate`, `weanWeight`, `notes`. Offspring created from it carry `clutchId`.
Individuals: `flowers: { male, female, first, end }` (dates), `aka` (earlier tags), `name` (nickname).
Crosses: `prediction: { genes, mother, father, results: [{ sex, ph, p }], date }` from the genetics calculator.
Projects: `tagStyle: { preset, pattern }` where preset is `projgen`, `selection`, `cross`, `year`, `simple`, `animal` or `custom`.
`profile.breederCode`: the short code added to tags on shared items.

### `product` and `yield`: what your garden or farm produces

`product`: `name`, `kind` (`plant` or `animal`), `unit` (such as `kg`, `eggs`, `L`, `fruit`), `alsoWeight` (record a weight as well as a count), `weightUnit`, `notes`.

`yield`: one harvest or collection: `date`, `productId`, `qty`, `weight`, `unit`, `quality`, `targets` and `scope` (the same as for inputs: the plants, animals, place, tray or project it came from), `notes`.

### `input`: something given to plants or animals

`name`, `brand`, `category` (`fert`, `soil`, `pest`, `disease`, `weed`, `med`, `vaccine`, `wormer`, `feed`, `other`), `active` (active ingredient), `unit`, `rate` (as printed on the label), `whp` (withholding periods in days: `{ "harvest", "eggs", "milk", "meat" }`), `organic`, `qty` (amount on hand), `opened`, `expiry`, `notes`, `photoIds`.

### `apply`: one use of an input

`date`, `inputId`, `amount`, `unit`, `method`, `reason`, `targets` (ids of the plants, animals, places, trays or projects it covered), `scope` (`{ "type": "single" | "pick" | "place" | "project" | "tray", "id" }`), `repeatDays`, `notes`. Withholding dates are worked out from the input's `whp` and the date.

Projects can also carry `noInputs: true`, meaning members are grown without inputs.

### `tray`: a seed tray

`code` (such as `T01`), `date` (sown), `lotId`, `strainId`, `projectId`, `placeId`, `rows`, `cols`, `seedsPerCell`, `notes`, `closed`, and `cells`: an object keyed by cell name (`A1`, `A2`, `B1`...), each `{ "s": "sown" | "up" | "failed" | "potted" | "culled", "up": date, "indId": id }`. Cells not listed are still waiting.

### `offer`: something listed for sale or swap (only when selling is turned on)

`itemId` (a lot or a plant or animal), `packSize`, `price` (`{ "mode": "price" | "free" | "swap", "amount" }`), `postage` (`{ "mode": "per" | "free" | "pickup", "amount", "extra" }`, extra being per additional pack), `available`, `sent`, `postsTo` (`all`, `notWaTas`, `local`, `none`), `area`, `contact`, `notes`, `status` (`open`, `soldout`, `closed`). Offers hold only what the person types: never payment details, addresses or phone numbers unless they write them in.

### `plan`: a season plan

`season` (label such as `2026–27`), `items`: list of `{ "strainId", "plants", "sowBy", "placeId", "saveSeed", "sown" }`.

Records created by the import wizard also carry `importBatch`, so an import
can be undone as one group.

### 4.11 Record type definitions (inside `project.recordTypes`)

```json
{
  "id": "rt-harvest",
  "name": "Fruit harvest",
  "itemName": "Fruit",
  "parentRt": "",
  "repeatDays": null,
  "fields": [
    { "id": "f-weight", "label": "Weight", "type": "number", "unit": "kg", "agg": "avg", "compare": true },
    { "id": "f-cavity", "label": "Cavity width", "type": "number", "unit": "cm" },
    { "id": "f-flesh",  "label": "Flesh thickness", "type": "number", "unit": "cm", "compare": true },
    { "id": "f-ratio",  "label": "Flesh to cavity ratio", "type": "calc", "formula": "{Flesh thickness} / {Cavity width}", "compare": true },
    { "id": "f-flavour","label": "Flavour", "type": "score" }
  ]
}
```

- `itemName` set means each entry is a separate item (Fruit, Litter, Clutch).
- `parentRt` set means entries attach to an item of that type (e.g. Storage
  check logged against each Fruit).
- `repeatDays` adds members to the due list when not logged for that long.
- Field `type`: `number`, `score` (1–5), `choice` (`options`; optional
  `endOptions` end a trial, e.g. `["Unusable"]`), `text`, `date`, `yesno`,
  `calc` (`formula` using other field labels in braces, `+ - * / ( )` only).
- `agg` sets how entries combine in comparisons: `avg`, `max`, `min`, `sum`,
  `latest`. `compare: true` shows the field in the project's comparison table.
- `archived: true` marks a retired field or type whose old values are kept.

### 4.12 Main photo framing

`frame` is `{ "x": 0.5, "y": 0.5, "z": 1 }`: the centre of the square as a
fraction of the photo's width and height, and the zoom (1 = the largest square
that fits). The photo itself is never altered.

---

## 5. Sync files in Google Drive

When sync is on, each person's Drive holds a folder named **Lineage Tracker sync**:

| File | Contents |
|---|---|
| `lineage-records.json` | `{ "app": "lineage", "version": 19, "format": "sync", "updatedAt", "by", "records": [...] }`, every record including deletion markers. |
| `photos/<photoId>.jpg`, `photos/<photoId>-thumb.jpg` | Photos, identified by the `photoId` app property. |
| `weekly snapshots/lineage-records-YYYY-MM-DD.json` | The last eight weekly copies, in the records-only backup format. Any of them can be restored from Settings. |

Devices merge by keeping, for each record id, the copy with the newest
`updatedAt`.

## 6. Friendly import format (use this for conversions)

Open **Settings > Import from a spreadsheet or another app** (the import
wizard) and choose the file, or paste it straight from Claude or ChatGPT. The
wizard shows what will be created and anything it couldn't match before
saving, and the whole import can be undone.

Records link by the names you already use: tag codes for plants and animals,
names for varieties, projects, places and sites, and labels for lots. Anything
already in Lineage Tracker with the same name or tag is reused, not duplicated or
overwritten. Every section is optional; include only what you have.

```json
{
  "app": "lineage",
  "format": "friendly",
  "varieties": [
    { "name": "Black Futsu", "kind": "plant", "group": "Pumpkin",
      "species": "Cucurbita moschata", "speciesConfirmed": true, "hybrid": false,
      "source": "Example Seeds", "description": "" }
  ],
  "places": [
    { "name": "Raised bed 1", "for": "plant", "type": "Raised bed", "details": "" }
  ],
  "projects": [
    { "name": "Arrakis Black", "code": "AB", "kind": "plant",
      "species": "Cucurbita moschata", "partOf": "",
      "goal": "Black skin, orange flesh, small cavity, long storage.",
      "inScope": "", "outScope": "", "success": "", "timeframe": "",
      "founders": ["Black Futsu", "South Anna Butternut"],
      "traits": [ { "name": "Black skin", "tier": 1, "mustHave": true } ],
      "recordTypes": [
        { "name": "Fruit harvest", "itemName": "Fruit",
          "fields": [ { "label": "Weight", "type": "number", "unit": "kg" },
                      { "label": "Flavour", "type": "score" } ] },
        { "name": "Storage check", "parent": "Fruit harvest",
          "fields": [ { "label": "Condition", "type": "choice",
                        "options": ["Sound", "Softening", "Unusable"],
                        "endOptions": ["Unusable"] } ] }
      ] }
  ],
  "lots": [
    { "variety": "Black Futsu", "form": "seed", "label": "", "source": "Example Seeds",
      "batch": "B-123", "year": "2026", "bestBefore": "2028-06",
      "quantity": 20, "unit": "seeds", "status": "active",
      "project": "", "mother": "", "father": "" }
  ],
  "tagged": [
    { "tag": "BF-P01", "nickname": "", "variety": "Black Futsu",
      "project": "Arrakis Black", "generation": "", "sex": "",
      "mother": "", "father": "", "fromLot": "B-123",
      "sown": "2026-10-20", "status": "Active", "place": "Raised bed 1",
      "scores": { "Black skin": 4 }, "description": "" },
    { "tag": "BFxSA-F1-P01", "project": "Arrakis Black", "generation": "F1",
      "mother": "BF-P01", "father": "South Anna Butternut", "sown": "2027-10-15" }
  ],
  "crosses": [
    { "date": "2027-01-10", "mother": "BF-P01", "father": "SA-P01",
      "method": "Hand-pollinated", "status": "Successful",
      "project": "Arrakis Black", "result": "Fruit set", "notes": "" }
  ],
  "records": [
    { "tag": "BF-P01", "type": "Fruit harvest", "item": 1, "date": "2027-03-01",
      "values": { "Weight": 2.4, "Flavour": 4 }, "notes": "" },
    { "tag": "BF-P01", "type": "Storage check", "ofItem": 1, "date": "2027-06-01",
      "values": { "Condition": "Sound" } }
  ],
  "notes": [ { "date": "2026-11-02", "about": "BF-P01", "text": "First female flower." } ],
  "germinationTests": [
    { "lot": "B-123", "date": "2026-09-01", "seeds": 10, "method": "Paper towel",
      "counts": [ { "day": 5, "sprouted": 4 }, { "day": 9, "sprouted": 8 } ],
      "finished": true }
  ],
  "readings": [ { "site": "Home garden", "date": "2026-10-01", "rainMm": 12, "maxC": 31, "minC": 14 } ]
}
```

How names are matched:

- **mother / father:** a tag code, or a variety name for founders. Leave one
  empty when unknown. Use the same tag twice for a selfed plant.
- **fromLot / lot:** the lot's label or batch, or the variety name when that
  variety has only one lot.
- **cloneOf:** on a tagged plant or a lot, the tag of the plant it was
  propagated from. `form` on a lot says what it is (seed, cuttings, seedlings,
  tubers, divisions, scions, tissue, eggs, young, adults).
- **Gift files** that Lineage Tracker makes when sharing with a friend use this
  same format, so they open in the import wizard or from **Restore a backup
  or open a gift file**.
- **about** (notes): a tag, variety, project, place or lot label. Anything
  unmatched becomes a general note.
- **records:** `type` is a record type name in the plant or animal's project.
  If the type doesn't exist, the wizard creates it from the values it finds.
  `item` numbers items such as Fruit 1, Fruit 2; `ofItem` attaches a child
  record (like a storage check) to that item.
- Values may be loose: `"status": "keep"`, `"sex": "hen"`,
  `"method": "hand"` and dates such as `20/10/2026` or spreadsheet date
  numbers are understood. The preview lists anything it couldn't read.

## 7. Spreadsheet (CSV) import

Save each sheet as CSV and choose them all at once in the import wizard. The
wizard recognises a file by its name or its column headings, and you can
change what it thinks a file holds. Column names follow the spreadsheet copies
in a backup's `readable/` folder, and common alternatives work too (Breed for
Variety, Dam and Sire for Mother and Father, Sown or Born, and so on).

| File holds | Main columns |
|---|---|
| Varieties and breeds | Name, Plant or animal, Group, Species, Species confirmed, Source, Description |
| Lots | Lot, Variety or breed, Source, Batch, Packed harvested or bought, Best before, Quantity, Unit, Stored, Status, Mother, Father, Notes |
| Places | Place, For, Type, Details |
| Tagged | Tag, Nickname, Variety or breed, Project, Generation, Sex, Sown or born, Status, Place, Mother, Father, From lot, Trait scores (`Name: 4; Name: 3`) |
| Crosses | Date, Mother, Father, Method, Status, Result, Project, Details |
| Notes | Date, About, Note |
| Germination tests | Lot, Started, Seeds tested, Method, Counts (`5: 4; 9: 8`), Finished |
| Records of a record type | Tag, an item number column (optional), Date, then one column per field, Notes. Choose the project and record type name in the wizard. |

## 8. Converting your records with AI

1. Gather your records: spreadsheets, exports from other apps, or photos of
   notebook pages.
2. Give the AI this document (or its link) and paste the prompt below with
   your records.
3. Paste the reply into the import wizard, check the preview, and import.
   **Undo that import** reverses it if anything looks wrong.

Sending records to an AI service shares them with that service. Importing into
Lineage Tracker itself keeps everything on your device.

### Conversion prompt

```
Convert my breeding records into Lineage Tracker's friendly import format, described
in section 6 of the Lineage Tracker data format document (format version 19).

Rules:
- Output one JSON object with "app": "lineage" and "format": "friendly".
- Link records by tag codes and names exactly as written in my records.
  Never invent ids.
- One entry in "varieties" per variety or breed, "lots" per seed packet or
  saved seed lot, "tagged" per individually tracked plant or animal,
  "crosses" per pollination or pairing, and "notes" for dated observations.
- Put repeated measurements (weights, counts, storage checks) in "records",
  and define their record type with fields in the project's "recordTypes".
- Use the status, method and kind words listed in the document where they fit.
- Dates as YYYY-MM-DD. If only a month or year is known, keep it in a note
  instead of guessing a day.
- Never invent data. Leave unknown fields out, and after the JSON list
  anything you could not place.

My records:
[paste here]
```

## 9. Planned

See the README and CHANGELOG for what's coming next.
