---
layout: page
title: Datasets
eyebrow: Data
description: The datasets behind backpacks — text-based, versioned, schema-validated, and entirely hand-carried.
permalink: /data/
---

Every dataset in this project is a text file in the repo (`data/`), validated
in CI against a JSON Schema (`schema/`), and served here verbatim.

## Datasets

| dataset | what it holds | schema |
| --- | --- | --- |
| `data/sites/` | resolved pack records, one file per pack | `schema/sites.schema.json` |
| `data/signals/` | one claim, one source, append-only | `schema/signals.schema.json` |
| `data/operators.yml` | the maker registry, and the parent companies that own them | `schema/operators.schema.json` |
| `data/sources.yml` | the source registry, and the fetch allowlist | `schema/sources.schema.json` |

`data/packs_index.yml` is generated from `data/sites/` for the index pages.
It is derived, not authoritative, and CI fails if it drifts.

The directory is called `sites` and the entity registry is called `operators`
because both names belong to a shared data contract this project did not
invent and does not get to rename. In this dataset a "site" is a pack and an
"operator" is a maker.

## The provenance chain

A published number can be walked back to a page someone read:

    a record in data/sites/  →  the signals it cites  →  the source each
    signal names  →  the exact URL that signal was read on

CI enforces every link in that chain. A record with no signals fails. A signal
naming a source that is not in the registry fails. It is the one property of
this dataset that is not allowed to degrade.

## How the data was collected

**By hand. All of it.** No page in this dataset was crawled, scraped, or
fetched on a schedule.

Every source in `data/sources.yml` is `status: manual`, and each carries the
reason in its own `robots:` block:

- **Evergoods** and **GoRuck** publish terms of service that prohibit using
  their sites "to spam, phish, pharm, pretext, spider, crawl, or scrape". A
  permissive `robots.txt` does not license conduct the operator forbids in
  prose. Where the two disagree, the stricter one governs.
- **Alpha One Niner** asks that its materials not be copied or transmitted
  without written consent. We record facts and cite pages; we reproduce no
  materials.
- **Mystery Ranch** publishes no feed. There is nothing to poll politely.
- **Filip Raboch** and **Sample** permit reading, and we still do not poll
  them. They are one-person shops. A scheduled fetcher aimed at a solo maker's
  store is rude in a way `robots.txt` has no vocabulary to express.
- **Carryology**, **The Perfect Pack** and **Suburban** publish clean,
  permissive feeds, and we do not touch those either. They are the people who
  have documented this subject for years. We read them, we credit them by
  name, and we link to them. We do not aggregate them on a cron.

Not one of the ten `robots.txt` files reviewed on 2026-07-09 named an AI or
LLM crawler — no `GPTBot`, `CCBot`, `ClaudeBot`, `anthropic-ai`, or
`Google-Extended` directive anywhere. We record that as a finding. It is an
absence of instruction, not a grant of permission, and we have not treated it
as one.

**Transformations applied:** unit conversion only (pounds and ounces to
grams), always with the maker's original figure preserved in a note. No
value was normalized, averaged, or reconciled across sources.

## Where sources disagree

They are left disagreeing. The dataset records both claims and says so on the
record. Sample's own page for the Article 404C reads `20L` in its title and
`18 L` in its spec block; both are stored as signals from that one URL, and
the record shows the conflict rather than choosing.

## What is missing

Gaps are data. Each record and each maker carries a `gaps` list naming what we
looked for and did not find — an unpublished weight, an unconfirmed founding
year, an acquisition whose effects no source describes. An empty field would
read as an answer. A named gap reads as the truth: we don't know.

## License

The datasets published by this project are licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (studio default,
ADR-0002). The project's code is MIT-licensed (see the repo's LICENSE).

The specifications are facts, and facts are not owned. The prose describing
them on the makers' own pages is theirs, and none of it is reproduced here.

## Commerce

There are no affiliate links on this site, and no monetization plumbing in
this repo. Whether there ever should be is an open question the studio has
recorded and deliberately not answered.
