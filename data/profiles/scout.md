# backpacks scout profile — dataset configuration for gn_info_scout

(Consumed as the `dataset_profile` input; platform `docs/gnome-evolution.md`.
This file defines WHAT the dataset catalogs; the gnome's prompt defines HOW.
backpacks is info-archetype build 3. The archetype data contract is frozen
(ADR-0045): `data/signals/`, `data/sites/`, `data/operators.yml`, and the
schema pair. Only the domain below is ours.)

## The dataset

Technical and boutique carry: backpacks and adjacent carry (slings, pouches,
organizers). Deliberately not mainstream — makers whose designs are discussed
on their merits by people who use them hard.

The **subject-of-record ("site" in archetype vocabulary) is one pack model**.
A model offered in several capacities is one subject per capacity when the
maker sells them as distinct products with distinct specs (GR1 21L and GR1
26L are two subjects); a model offered in several colorways or fabrics is
**one** subject, with the fabric variants recorded as attributes.

`site_hint` format for unknown subjects: `"<maker as reported> <model name>
— <capacity as reported>"`.

## Attribute vocabulary

`maker`, `line`, `name`, `capacity_l`, `weight_g`, `dimensions`,
`materials`, `price`, `made_in`, `status`, `released`, `discontinued`,
`carry_style`, `use_case`.

Maker-level attributes (subject_type `maker`, resolved into
`data/operators.yml`): `founded`, `country`, `homepage`, `parent`,
`acquired_date`, `acquisition_price`, `predecessor`, `status`.

## What is signal-worthy

Specifications a reader would compare: capacity, weight, dimensions,
materials, price (with its currency and the date observed), where it is
made. Lifecycle facts: release, discontinuation, a maker's acquisition or
closure. Corporate lineage and era distinctions.

**Stock status is not signal-worthy.** "Sold out", "currently unavailable",
and "back in stock" churn weekly and say nothing about the pack. Do not emit
them. `status` records the product's *lifecycle*, never its inventory.

Marketing prose is not signal-worthy. "Bombproof", "the last pack you'll
ever buy", and "obsessively engineered" are the maker talking. A reviewer's
subjective verdict is not a spec; do not launder an opinion into an
attribute. Record what is measurable and attributable.

**Cap: the most informative ~8 signals per subject.**

## Conflicting values are the point

When two sources disagree — or when *one page disagrees with itself* — emit
**two signals**, each tied to what its source actually said. Never average,
never pick, never silently prefer the newer. The records gnome resolves;
the scout reports.

Worked example, live in this dataset: Sample's product page for Article 404C
carries `20L` in its page title and `18 L` in its spec block. That is two
signals from one URL, both true statements about what the page says.

## Confidence refinement

Primary sources for this domain are **the maker's own product and about
pages** and, for corporate events, the acquiring company's investor
relations releases and regulatory filings.

Reputable carry publications and review sites (Carryology, The Perfect
Pack, Pack Hacker) are `medium` — excellent on context, history, and
judgment; secondhand on numbers.

Retailer listings are `medium` at best and often stale; a retailer's spec
never outranks the maker's.

Search-result snippets are **not a source**. If the page was not read, the
claim is not a signal.

## Attribution is the product

This dataset serves people who know their corners of it better than we do.

- A specification without a source does not get published. It is recorded as
  a gap, in the record's `gaps:` list, naming what is unknown.
- Never reproduce a maker's or reviewer's prose. Record the **fact** and
  cite the page. Facts are not owned; paragraphs are. Several makers'
  terms of service forbid copying their materials, and one forbids crawling
  outright — see `data/sources.yml`, where every source is `manual` and the
  reason is written down.
- Credit community sources by name. They are why this dataset can exist.
- Where sources are silent, be silent. Do not infer that an acquisition
  changed a product, or that a discontinued pack was bad. Silence in the
  sources is a finding: say "sources are silent" and move on.

## History, not embarrassment

Discontinued packs and acquired makers are records, exactly as cancelled
sites are records in kdc (GD-0004). A pack that is gone stays in the
dataset with `status: discontinued`. A maker that was acquired keeps its
pre-acquisition history in `notes`, with the acquisition dated and cited,
and **no claim about what changed unless a source says so**.
