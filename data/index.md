---
layout: page
title: Datasets
eyebrow: Data
description: The datasets behind backpacks — text-based, versioned, schema-validated, and collected one page at a time by an AI agent rather than a crawler.
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

**By an AI agent, one page at a time, on request. Not by a crawler, not on a
schedule, and not by a person.**

Say the exact thing, because the vague thing flatters us. The founding corpus
was assembled on 2026-07-09 by an agent session (Claude, driving the Bussetech
studio's tooling). For each maker, the agent searched, then **fetched each
cited page once**, read what came back, and recorded the facts with the URL.
Nothing was crawled recursively. Nothing was polled on a timer. No page was
fetched twice. And no human being sat and read these pages — an earlier
version of this page said one had, and that was not true.

**There is an unresolved tension here, and it is ours, not yours.** Evergoods
and GoRuck forbid using their sites "to spider, crawl, or scrape". A single
agent-initiated fetch of one product page is not spidering, and a browser
fetches pages too — but we are not going to pretend the question is obviously
settled in our favour, on a page whose whole argument is that a permissive
`robots.txt` does not license conduct an operator forbids in prose. We applied
that standard to the scheduled fetch layer and did not, at first, apply it to
ourselves. The question is filed as an open studio decision rather than
answered by whoever happened to be convenient. If either maker would rather we
did not, we will remove their specifications; every one of them is a fact they
published themselves, and none of them is worth this.

What follows is a statement about the **fetch layer** — the scheduled
machinery — and it remains exactly true. Every source in `data/sources.yml` is
`status: manual`; nothing is on a cron; each carries its reason in its own
`robots:` block:

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
absence of instruction, not a grant of permission.

That finding lands closer to home than we first wrote it. The agent that
collected this corpus **is** an AI agent, and it fetched these pages while
those files said nothing about agents like it. We did not read that silence as
permission to build a crawler, and none exists. Whether it was permission to
fetch ten pages once is the open question above.

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
