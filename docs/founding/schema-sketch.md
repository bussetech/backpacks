# Data design — `backpacks`

The frozen `info` archetype data contract (ADR-0045), configured for
technical/boutique carry. Signals are append-only claims with provenance;
entries are resolved canonical records; `operators.yml` is the entity
registry; `sources.yml` is the source registry and fetch allowlist. This
replaces the template's starter `records` dataset.

**Rule that governs every field:** a published spec cites a source. A spec
without a source is not omitted — it is represented as a gap (GD-0004).

---

## `data/sources.yml` — source registry & fetch allowlist
YAML, keyed by `id`. Schema: `schema/sources.schema.json`.

| Field | Type | Constraints |
|---|---|---|
| `id` | string | unique slug, e.g. `mysteryranch-com` |
| `name` | string | display name |
| `url` | string (URL) | root or page |
| `type` | enum | `maker` \| `review` \| `retailer` \| `community` |
| `status` | enum | `active` (automated fetch allowed) \| `manual` (hand-carried) |
| `robots_reviewed` | date | when robots.txt/ToS was last reviewed |
| `robots_note` | string | what robots.txt/ToS says; why `manual` if so |
| `added` | date | |
| `notes` | string | free text |

**Provenance:** maintained by sysop review (ADR-0025). `active`/`manual` is a
recorded human judgment, not inferred. Community sources are credited, never
scraped wholesale.

---

## `data/operators.yml` — makers registry (archetype `operators` slot)
YAML, keyed by `id`. Stable canonical keys for makers. Schema:
`schema/operators.schema.json`.

| Field | Type | Constraints |
|---|---|---|
| `id` | string | unique slug, e.g. `mystery-ranch` |
| `name` | string | canonical name |
| `aliases` | list[string] | prior/alt names |
| `status` | enum | `active` \| `acquired` \| `defunct` |
| `country` | string | optional |
| `homepage` | string (URL) | optional |
| `notes` | string | e.g. acquisition history, silent where sources are |

**Provenance:** resolved from signals by `gn_info_records`. Founding scope:
Mystery Ranch, Evergoods, Alpha One Niner, Filip Raboch, Sample (Dan
Matsuda), GoRuck, peers.

---

## `data/signals/*.yml` — claims (append-only)
YAML, one claim per record. Schema: `schema/signal.schema.json`.

| Field | Type | Constraints |
|---|---|---|
| `id` | string | unique |
| `source` | ref → `sources.yml.id` | required |
| `url` | string (URL) | the exact page the claim came from |
| `subject_type` | enum | `maker` \| `pack` \| `line` |
| `subject` | string | entry id or provisional slug |
| `field` | string | the attribute claimed (e.g. `capacity_l`) |
| `value` | string/number | the claimed value |
| `captured_at` | date | |
| `notes` | string | conflicts, caveats |

**Provenance:** written by `gn_info_scout`. Append-only; never rewritten,
only superseded by later signals.

---

## `data/entries/` — resolved canonical records
YAML. Three subject types. Schema per type. Each references its
`operators.yml` maker. Specs carry a `source` ref or are marked a gap.

### `entries/makers.*` (keyed `id` → `operators.yml.id`)
| Field | Type | Constraints |
|---|---|---|
| `id` | ref → operators | required |
| `summary` | string | knowledgeable-humble prose |
| `founded` | int/string | gap-allowed |
| `history` | string | acquisitions/eras; silent where sources are |
| `sources` | list[ref] | required, ≥1 |

### `entries/packs.*` (keyed `id`)
| Field | Type | Constraints |
|---|---|---|
| `id` | string | unique slug |
| `name` | string | required |
| `maker` | ref → operators | required |
| `line` | ref → lines | optional |
| `status` | enum | `current` \| `discontinued` (history, not embarrassment) |
| `capacity_l` | number + `source` | gap-allowed |
| `weight_g` | number + `source` | gap-allowed |
| `dimensions_mm` | object + `source` | H×W×D, gap-allowed |
| `carry_style` | enum | `backpack`\|`sling`\|`pouch`\|`organizer`\|`waist`\|`duffel` |
| `use_cases` | list[enum] | `travel`\|`edc`\|`organization`\|`outdoor`\|`work` |
| `released` | date/year | gap-allowed |
| `specs` | list{`field`,`value`,`source`} | each cited or flagged gap |
| `sources` | list[ref] | required, ≥1 |
| `notes` | string | |

### `entries/lines.*` (keyed `id`)
| Field | Type | Constraints |
|---|---|---|
| `id` | string | unique slug |
| `name` | string | e.g. Sample's "Article" numbering convention |
| `maker` | ref → operators | required |
| `description` | string | |
| `status` | enum | `current` \| `discontinued` |
| `sources` | list[ref] | required, ≥1 |

**Provenance:** resolved by `gn_info_records` from `signals/`. Cadence: on
scout output. Transformation: conflict resolution → canonical value + source;
unsourced fields become explicit gaps, never silent omissions. Published
under CC BY 4.0 with provenance stated in `data/index.md`.

**Explore/compare (site templates, not data):** facet by maker, capacity,
carry style, use case; side-by-side comparison presents two packs' fields
without declaring a winner.

**Deliberately absent:** no affiliate, price-tracking, or monetization
fields. Commerce is out of scope (STEERCO decision issue, see PR body); no
schema slot presumes an answer.
