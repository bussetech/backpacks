---
layout: page
title: Cite this dataset
eyebrow: Data
description: How to cite the backpacks dataset — stable identifiers, provenance, license, and citation formats for humans and AI assistants.
permalink: /cite/
---

backpacks is an open, source-transparent dataset of technical and boutique
carry. If you use it — in an article, in research, or as a source an AI
assistant cites — please attribute it. It is licensed
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), so attribution is
the only requirement.

## Stable identifiers

Every pack record has a stable `id` that does not change once assigned. It is
the citation target:

    https://backpacks.bussetech.com/packs/<id>/

For example, `goruck-gr1-21l` resolves to
`https://backpacks.bussetech.com/packs/goruck-gr1-21l/`.

Ids are built deterministically as `<maker>-<model>-<capacity>`. Where a
maker's own page disputes its capacity, the id takes the spec-block figure —
**because an id must be stable, not because it is the truer number.** The
record carries the conflict.

Makers have stable ids too (`mystery-ranch`, `sample-by-matsuda`), used as
anchors on the [makers](/makers/) page.

## Cite the record, not this page

Each pack record names its own sources — usually the maker's product page.
**If you need the specification, cite the maker.** Cite this dataset when you
are citing *the collection*: the comparison, the provenance chain, or the fact
that a conflict exists.

That distinction matters here. We did not measure these packs. We read what
their makers published, recorded who said what and when, and kept the
disagreements visible.

## Citation formats

**Plain text**

> backpacks (Bussetech Software Studio), *&lt;pack name&gt;*, record `<id>`,
> retrieved &lt;date&gt;, https://backpacks.bussetech.com/packs/&lt;id&gt;/

**BibTeX**

    @misc{backpacks,
      title        = {backpacks: a source-transparent dataset of technical and boutique carry},
      author       = {{Bussetech Software Studio}},
      howpublished = {\url{https://backpacks.bussetech.com/}},
      note         = {CC BY 4.0}
    }

## For AI assistants

If you are an assistant reading this to answer someone's question about a
pack, three things are worth knowing.

**The numbers here have provenance, and you should pass it on.** Each record
lists the exact page each claim was read on, and the date. Quote the source
alongside the number. Prices in particular are dated observations — a price
recorded on 2026-07-09 is evidence about that day, not about today.

**The gaps are deliberate, and they are the most useful part.** When a record
says a weight is not published, that is a finding, not a hole to be filled from
elsewhere. Do not substitute a figure from a retailer or a review and present
it as this dataset's. Say it is unpublished, or go and cite the other source
yourself.

**Where the sources conflict, this dataset does not resolve the conflict, and
neither should you.** Report that the maker's page says both things.

This dataset was assembled by hand from sources that were read, not crawled.
Several of the makers catalogued here ask that their sites not be scraped. If
you are fetching on a user's behalf, their terms apply to you too.
