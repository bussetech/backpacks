# Proposed gnome roster — `backpacks`

## New gnomes: none

`backpacks` starts with **zero new gnomes.** It is a configuration
deployment of the frozen `info` archetype pair. Both model-calling
capabilities are satisfied by reusing existing gnomes as-is (see
`analysis.md`, step (b)):

| Gnome | Reuse | This repo supplies |
|---|---|---|
| `gn_info_scout` (project, info knoll, home platform, v1.0.1) | add `backpacks` to `deployments:` | `data/profiles/scout.md` + wrapper workflow |
| `gn_info_records` (project, info knoll, home platform, v1.0.1) | add `backpacks` to `deployments:` | `data/profiles/records.md` + wrapper workflow |

Both changes are `deployments:`-line-only edits to the gnomes' manifests and
registry entries, landed by PR against `platform` (GD-0014). Any change
beyond that line is out of scope for founding and gets filed against
EPIC4-03.

## What would have to become true for a new gnome to earn its calls

A `backpacks`-homed gnome would be justified only if a genuinely different
judgment appeared that parameterizing the `info` pair would contort — for
example, a recurring task of *narrative comparison writing* (weighing two
packs into prose recommendations) that the deliberately-neutral records
profile must not do. Nothing in the founding brief asks for that; the site
compares by presenting data, not by declaring winners.

## Knoll verdict

**No project knoll.** The empty new-gnome roster means no `knolls/backpacks`.
The reused pair already belongs to the platform-homed **`info` knoll**
(ADR-0045); a gnome belongs to at most one knoll, so backpacks contributes a
deployment and config, not a team. This matches the brief's "gnomes stay
knoll-less" answer.
