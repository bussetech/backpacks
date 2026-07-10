---
layout: page
title: Packs
eyebrow: Explore
description: "Every pack in the backpacks dataset, explorable by maker, capacity, carry style and use case — with sources cited and gaps named."
permalink: /packs/
---

{%- assign packs = site.data.packs_index -%}
{%- assign makers = site.data.operators | where: "type", "maker" -%}

{{ packs.size }} packs from {{ makers.size }} makers. Every row links to a
record with its sources and its gaps. Specifications are what the maker
published, converted to common units where the maker did not.

Nothing on this page ranks anything. Two packs sit side by side so you can
read the numbers yourself. The dataset has no opinion about which one you
should carry, and would not be worth much if it did.

## All packs

Sorted by capacity, smallest first; packs whose capacity the maker never
published sort last. *Not published* means we looked and the maker does not
say — each record names the gap.

<div style="overflow-x:auto" markdown="0">
<table>
  <thead>
    <tr>
      <th>Pack</th><th>Maker</th><th>Capacity</th><th>Weight</th><th>Price</th><th>Status</th>
    </tr>
  </thead>
  <tbody>
  {%- for rec in packs %}
    <tr>
      <td><a href="/packs/{{ rec.id }}/">{{ rec.name }}</a></td>
      <td><a href="/makers/#{{ rec.maker }}">{{ rec.maker_name }}</a></td>
      <td>{% if rec.capacity_l %}{{ rec.capacity_l }} L{% else %}<em>not published</em>{% endif %}</td>
      <td>{% if rec.weight_g %}{{ rec.weight_g }} g{% else %}<em>not published</em>{% endif %}</td>
      <td>{% if rec.price_amount %}{{ rec.price_amount }} {{ rec.price_currency }}{% else %}<em>—</em>{% endif %}</td>
      <td>{{ rec.status }}</td>
    </tr>
  {%- endfor %}
  </tbody>
</table>
</div>

Prices are dated observations, read from the maker's page on the day recorded
on each entry (2026-07-09 for the founding corpus). They drift. Weights are in
grams; where a maker published pounds and ounces, the record says so and keeps
the maker's original figure alongside.

## By maker

{% for m in makers -%}
{%- assign mine = packs | where: "maker", m.id -%}
{%- if mine.size > 0 %}
### {{ m.name }}

{% for rec in mine %}- [{{ rec.name }}](/packs/{{ rec.id }}/){% if rec.line %} — {{ rec.line }} line{% endif %}{% if rec.capacity_l %}, {{ rec.capacity_l }} L{% endif %}
{% endfor %}
{% endif -%}
{%- endfor %}

## By carry style

How the pack opens and how it rides. A pack can carry more than one style, and
several here have none recorded — the maker did not say, so neither do we.

{% assign styles = "panel-loader,clamshell,half-zip,rolltop,top-loader,three-zip" | split: "," -%}
{%- for style in styles -%}
{%- capture rows -%}
{%- for rec in packs -%}{%- if rec.carry_style contains style %}- [{{ rec.name }}](/packs/{{ rec.id }}/) — {{ rec.maker_name }}
{% endif -%}{%- endfor -%}
{%- endcapture -%}
{%- if rows != "" %}
### {{ style }}

{{ rows }}
{% endif -%}
{%- endfor %}

## By use case

What the maker built it for. This is not a verdict on what it is good at —
people carry hunting packs to work and training rucks around the world.

{% assign cases = "edc,travel,hiking,hunting,military,training" | split: "," -%}
{%- for uc in cases -%}
{%- capture rows -%}
{%- for rec in packs -%}{%- if rec.use_case contains uc %}- [{{ rec.name }}](/packs/{{ rec.id }}/) — {{ rec.maker_name }}
{% endif -%}{%- endfor -%}
{%- endcapture -%}
{%- if rows != "" %}
### {{ uc }}

{{ rows }}
{% endif -%}
{%- endfor %}
