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

{% for m in makers %}
<h2 id="{{ m.id }}">{{ m.name }}</h2>

{% if m.founded %}Founded {{ m.founded }}{% if m.hq %}, {{ m.hq }}{% endif %}.{% elsif m.hq %}{{ m.hq }}.{% endif %}
{%- if m.founders and m.founders.size > 0 %} Founded by {{ m.founders | join: " and " }}.{% endif %}
{%- if m.status == "acquired" %}
{%- assign parent = site.data.operators | where: "id", m.parent | first %}
**Acquired by {{ parent.name }}**, closed {{ m.acquired_date }}{% if m.acquisition_price %}, reported at {{ m.acquisition_price.amount }} {{ m.acquisition_price.currency }} (confidence: {{ m.acquisition_price.confidence }}){% endif %}.
{%- endif %}

{{ m.notes }}

{%- if m.predecessors and m.predecessors.size > 0 %}

**Lineage:** {{ m.predecessors | join: " → " }} → {{ m.name }}.
{%- endif %}

{%- assign mine = packs | where: "maker", m.id %}
{%- if mine.size > 0 %}

**Packs tracked ({{ mine.size }}):**
{% for rec in mine %}- [{{ rec.name }}](/packs/{{ rec.id }}/){% if rec.line %} — {{ rec.line }} line{% endif %}
{% endfor %}
{%- else %}

No packs tracked yet.
{%- endif %}

{%- if m.gaps and m.gaps.size > 0 %}

**What we don't know**
{% for gap in m.gaps %}- {{ gap }}
{% endfor %}
{%- endif %}

{%- if m.sources and m.sources.size > 0 %}

**Sources**
{% for s in m.sources %}- [{{ s.title | default: s.url }}]({{ s.url }}){% if s.publisher %} — {{ s.publisher }}{% endif %}{% if s.kind %} ({{ s.kind }}){% endif %}{% if s.note %}. {{ s.note }}{% endif %}
{% endfor %}
{%- endif %}
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

Both corrections are on the record in the studio's founding brief for this
project (`platform#223`). A dataset that hides its own errors is not a
source; it is a claim.
