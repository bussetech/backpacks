---
layout: page
title: Makers
eyebrow: Explore
description: "The makers catalogued by backpacks — histories, lineages and acquisitions, each fact cited, each unknown named."
permalink: /makers/
---

{%- assign makers = site.data.operators | where: "type", "maker" -%}
{%- assign parents = site.data.operators | where: "type", "parent-company" -%}
{%- assign packs = site.data.packs_index -%}

{{ makers.size }} makers. Some are companies with product lines; two are one
person building to order.

Corporate history is recorded the way the rest of this dataset is recorded:
what a source says, attributed, with the date. Where sources are silent — and
on the questions people most want answered, they often are — the silence is
written down as a gap rather than filled with a plausible sentence.

{% for m in makers -%}
{%- assign mine = packs | where: "maker", m.id %}
- **[{{ m.name }}](/makers/{{ m.id }}/)**{% if m.founded %} — founded {{ m.founded }}{% endif %}{% if m.hq %}, {{ m.hq }}{% endif %}{% if m.status == "acquired" %}{% assign parent = site.data.operators | where: "id", m.parent | first %}. **Acquired by {{ parent.name }}**, {{ m.acquired_date }}{% endif %}. {{ mine.size }} pack{% if mine.size != 1 %}s{% endif %} tracked{% if m.gaps and m.gaps.size > 0 %}, {{ m.gaps.size }} known gap{% if m.gaps.size != 1 %}s{% endif %}{% endif %}.
{% endfor %}

## Parent companies

Registered so an acquisition resolves to an entity rather than a bare string.

{% for p in parents %}- **{{ p.name }}** — {{ p.notes }}
{% endfor %}

## A note on eras

Two entries here carry corrections we made to our own founding brief, and we
have left the corrections visible rather than quietly fixing them:

- The brief called the maker **Filip Robach**. No such designer exists. His
  name is **Filip Raboch**, as his own store spells it.
- The brief described **SAMPLE** and **ARTICLE** as two product lines. Sample
  is the brand; Article is how Sample numbers its models. Encoding them as
  siblings would have misrepresented a maker to readers who know better.

Neither correction is hidden. Each maker's entry states what the error was and
links the sources that settle it — Raboch's own store for his name, and
Carryology's interview with Dan Matsuda for the Article numbering. A dataset
that quietly fixes its own errors is not a source; it is a claim.
