# backpacks records profile — dataset configuration for gn_info_records

(Consumed as the `dataset_profile` input; platform `docs/gnome-evolution.md`.
This file defines the record schema surface and the id rule; the gnome's
prompt defines the resolution method. Record schema of record:
`schema/sites.schema.json`. Entity registry: `data/operators.yml`.)

## The subject

One record per **pack model at one capacity**. A model sold in several
capacities with distinct specs is several records (`goruck-gr1-21l`,
`goruck-gr1-26l`); a model sold in several fabrics or colorways is one
record, with the variants in `materials` and, where they differ, per-variant
weights in `notes`.

Cluster signals on maker + model name + capacity.

## Record schema fields (only these)

id, name, maker, line, status,
specs{capacity_l, capacity_note, weight_g, weight_note, dimensions,
materials, made_in},
price{amount, currency, observed},
carry_style, use_case, released, discontinued,
first_seen, last_updated, confidence,
sources[{url, title, publisher, date, note}], signals, gaps, notes.

- `maker` — an id from `data/operators.yml` only. Never invent one; propose
  additions in run notes.
- `line` — the maker's own product-family name, **only where the maker
  actually operates named lines** (Evergoods CIVIC, Mystery Ranch Hunting).
  Omit it otherwise. A model-numbering convention is not a line: Sample's
  "Article 404C" is a model name under the brand Sample, not a line called
  ARTICLE. Getting this wrong misrepresents a maker to an audience that
  knows better.
- `specs.capacity_note` / `specs.weight_note` — carry the disagreement when
  sources conflict (`"maker page title says 20L; spec block on the same page
  says 18L"`). Do not resolve a conflict the sources have not resolved.
- `price` is a **dated observation**, not a fact about the pack. Always
  stamp `observed`. Prices churn; a stale price with a date is honest, a
  stale price without one is a lie.
- `gaps` — a list of attributes that are genuinely unknown, each naming what
  is missing. An empty spec field with no gap entry reads as "we didn't
  bother"; a gap entry reads as "we looked". Prefer the latter.

## Status vocabulary

`current | discontinued | made-to-order | unknown`.

- `made-to-order` — built per order, often by raffle or in batches, with a
  stated lead time (Filip Raboch, Sample). It is a real, distinct lifecycle,
  not a euphemism for out of stock.
- **Inventory is never a status.** "Sold out" is not `discontinued`. If a
  catalog-current pack shows no stock, it stays `current`; note it only if a
  source says the model is ending.
- `unknown` is permitted and preferred over a guess.

Discontinued packs stay in the dataset. Their story goes in `notes`.

## The maker registry (`data/operators.yml`)

Makers are entities, not records. `status` there is `active | acquired |
defunct | unknown`. Acquisition facts (`parent`, `acquired_date`,
`acquisition_price`) are recorded **only from primary or reputable business
sources**, each cited.

Where a maker has corporate lineage worth telling — a predecessor brand, a
sale, a revival — it goes in `notes`, dated and cited, and it stops there.
Do not narrate consequences the sources do not state. "Mystery Ranch was
acquired by YETI Holdings on 2024-02-02" is a fact. "Quality declined after
the acquisition" is not, unless a source says it and you attribute it.

## The id rule (deterministic; collision clause at the end)

Build `<maker>-<model>-<capacity>`, lowercase, ASCII, hyphenated:

- `<maker>` = the maker's `operators.yml` id.
- `<model>` = a slug of the model name, dropping generic words ("backpack",
  "pack", "bag", "rucksack") and the maker's own name when it repeats.
- `<capacity>` = the integer litre capacity plus `l` (`21l`, `26l`). Omit
  this segment entirely when the model has exactly one capacity **and** the
  maker does not label it by size.
- **Collision clause:** if that id would name a *different* existing pack,
  append `-<generation>` (`-gen3`), then `-2`, `-3` — the sole allowed
  disambiguation.

Where capacity itself is disputed, the id takes the **maker's spec-block
figure**, and `capacity_note` carries the conflict. An id is a filename, not
a truth claim; it must be stable, so it never tracks a contested number.
