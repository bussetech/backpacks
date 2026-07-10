# backpacks

**Status:** ![status](https://img.shields.io/badge/status-active-00843D) ·
[![ci](https://github.com/bussetech/backpacks/actions/workflows/ci.yml/badge.svg)](https://github.com/bussetech/backpacks/actions/workflows/ci.yml)
· **Site:** <https://backpacks.bussetech.com> · **Visibility:** `public`

An aggregator and exploration tool for technical and boutique carry — makers, packs, and lines, with every spec traced to its source.

A [Bussetech Software Studio](https://bussetech.com) project: a static site
(Jekyll, shared studio theme) rendered from text-based data stores.

## Layout

| path | what |
| --- | --- |
| `data/` | the datasets — JSON/YAML/CSV/Markdown, versioned in git |
| `schema/` | JSON Schemas; CI validates `data/<name>.*` against `schema/<name>.schema.json` |
| `_posts/` | site posts — each one becomes a `/feed.json` item the studio portal aggregates |
| `gnomes/` | project gnome directories (stub — see `gnomes/README.md`) |
| `.github/workflows/` | thin callers into the studio's shared CI + the Pages deploy |

## Build locally

```sh
bundle install
bundle exec jekyll serve      # http://127.0.0.1:4000
```

No studio access needed — the theme and CI machinery are public. See
`CLAUDE.md` for how this repo fits the studio (and how it detaches from it).

## Licenses

Code: MIT (`LICENSE`). Published datasets: CC BY 4.0 — license and
provenance statements live in `data/index.md`.
