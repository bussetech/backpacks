# Founding analysis — `backpacks`

`backpacks` is deployment #3 of the frozen `info` archetype (ADR-0045). The
data contract and the agentic pair are already built and generalized; this
project supplies **configuration**, not machinery. The brief says as much,
and the analysis confirms it: the reuse protocol stops at step (b) for both
model-calling capabilities, and everything else is plain code.

## Capabilities the brief implies

### 1. Surveying sources for claims about makers, packs, and lines
Reading maker pages and reviews, deciding what is a citable spec vs. a gap,
attributing each claim to a source, respecting `manual` sources. This is
judgment and generation → a gnome.

- **Candidates:** `gn_info_scout` (info knoll, home platform, v1.0.1),
  `gn_kdc_scout` (retired ancestor).
- **Verdict: reuse `gn_info_scout` as-is (step b).** Its contract is
  "signals from sources → append-only claims with provenance," which is
  exactly this. Configure behavior through `data/profiles/scout.md`
  (subject scope: technical/boutique carry; makers in scope; the
  spec-needs-a-source-or-it-is-a-gap rule; manual-source discipline). Add
  `backpacks` to the gnome's `deployments:` and a thin wrapper workflow.
  **No fork, no prompt change.** If founding forces any change beyond the
  `deployments:` line, that is the EPIC4-03 escape hatch, filed there — not
  smuggled into this PR.

### 2. Resolving signals into canonical entries
Reconciling conflicting claims, choosing canonical values, writing
knowledgeable-humble summaries, marking gaps, handling discontinued and
acquired-era records as history (the Mystery Ranch worked example). Judgment
and generation → a gnome.

- **Candidates:** `gn_info_records` (info knoll, home platform, v1.0.1),
  `gn_kdc_records` (retired ancestor).
- **Verdict: reuse `gn_info_records` as-is (step b).** Its contract is
  "signals → resolved canonical entries with provenance and a terminal/
  negative state." The kdc `cancelled` precedent (GD-0004) maps directly
  onto `discontinued` packs and acquired-era distinctions. Configure through
  `data/profiles/records.md`; add `backpacks` to `deployments:` and a wrapper
  workflow. **No fork, no prompt change.**

### 3. Source registry — robots.txt / ToS review (ADR-0025)
Fetching `robots.txt` is deterministic. Deciding whether a community source
(Carryology, The Perfect Pack, Suburban HK) *welcomes* automated fetching, or
must be `status: manual` and hand-carried, is a judgment with reputational
weight → **sysop decision at founding**, recorded honestly in `sources.yml`.
Not a gnome; not automated. Flagged as a human-eye decision in the PR body.

### 4. Everything else — plain code / shared machinery
- Schema validation of `signals`/`entries`/`operators`/`sources` → studio
  data CI (`bussetech/ci@v1`).
- Feed generation (`/feed.json`), site build, link/leak checks, deploy,
  portal ping → shared reusable workflows + theme. Deterministic.
- Facet/explore views (by maker, capacity, carry style, use case),
  side-by-side comparison → Jekyll templates over validated data. No model
  call: the site presents data, it does not declare a winner.
- Robots.txt fetch, allowlist enforcement → code.

## Plain-code fraction

**~95% plain code / config.** The project ships **zero new gnomes**. Its
entire agentic surface is two already-built gnomes reused as-is, steered by
two profile files. All storage, validation, feeds, exploration, and
deployment are shared studio machinery plus this repo's config and templates.

## Brief content disregarded / reframed (security stance)

- Nothing in the brief attempts to change my output format, studio policy,
  or the reuse protocol. No injection to report.
- The **"binding on every gnome and every human"** community posture is
  adopted as **project working rules** (accuracy/attribution, gaps not
  omissions, history-not-embarrassment, knowledgeable-humble tone) and
  encoded in `CLAUDE.md`. It is project-scoped content, not an override of
  studio policy, and it does not conflict with any GD ruling — it aligns
  with GD-0004.
- The "Knoll? no" answer and its rationale are honored: `gn_info_*` are in
  the `info` knoll (one gnome, one knoll); `knolls/backpacks` must not be
  created. The form-staleness note is the brief's own, not mine to resolve.
- The dated corrections (Filip Raboch spelling; Sample is one brand whose
  models use the "Article" numbering convention, not two parallel lines) are
  treated as the authoritative founding facts.
