---
layout: page
title: "Conversion Notes — Design Pattern Catalogue"
---

[← Back to the pattern catalogue](index.md)

Tracking progress converting all 42 antipattern/design-pattern pairs from `OUG_Amazon_CH14-designpatterns.docx` (Chapter 14) into individual Markdown pages.

## Source Quality

Unlike several other source documents converted in this repository, Chapter 14 required **no cleanup** — no leaked AI-drafting commentary, no structural inconsistency. Verified programmatically against the raw document XML rather than by sampling: all 42 antipattern headers use consistent dark red shading (`#8B1A1A`), all 42 design pattern headers use consistent dark green (`#1A5C4A`), and all 84 entries use the identical 5-row anatomy (1 header row + 5 content rows). This appears to be the fully cleaned, unified version of the chapter — the inconsistencies (navy vs. red headers, a lean 3-part anatomy for 12 pairs) referenced in earlier work on this book are not present in this upload.

## Naming Discrepancies

**AP-18 / DP-18 — Resolved.** ✅ The full entry text (both AP-18's own header and DP-18's) consistently uses "The Accidental **Programme**" — British spelling. Only the master glance table at the front of the chapter uses the American "Program." Used "Programme" throughout the converted page, with a note on the page itself for anyone cross-checking against that master table.

**AP-23 / DP-23 — still open.** The block-specific glance table for 7org uses "The **Professionalised** Vocation" (British). Not yet checked against the full entry text — will confirm when Block 4 is converted.

## Batch Progress

| Block | Pairs | Status |
|---|---|---|
| 1 · HEI Observations | 1–6 | ✅ Complete (6 of 6) |
| 2 · Learn8 | 7–12 | ✅ Complete (6 of 6) |
| 3 · Curr4 | 13–18 | ✅ Complete (6 of 6) |
| 4 · 7org | 19–24 | ✅ Complete (6 of 6) |
| 5 · 6gov | 25–30 | ✅ Complete (6 of 6) |
| 6 · Person 1 | 31–36 | ✅ Complete (6 of 6) |
| 7 · Person 2 | 37–42 | ✅ Complete (6 of 6) |

## 🎉 All 42 Pairs Converted

## Block 7 (Person 2): The Richest Cluster of Direct Correspondence

Every one of the six pairs in the final block names or clearly maps onto a real, already-converted OUG document — several by exact terminology, not inference:

| Pattern | OUG document it corresponds to |
|---|---|
| AP-37/DP-37 The Coherent System | [Design Signature Founding](../governance/design-signature-founding.md) — **named directly in the source text**: "The OUG's Design Signature is the record that verifies system coherence across the founding architecture." |
| AP-38/DP-38 The Prepared Decision | [Governance & Decision Framework](../governance/governance-architecture.md) — its G1–G4 staged decision architecture |
| AP-39/DP-39 The Owned Strategy | [Strategy Formation Protocol](../strategy/strategy-formation-protocol.md) — matches almost point for point: seven-phase harvesting, iterative validation, ~18-month/two-year timeline, explicit rejection of survey-based "participation performance" |
| AP-40/DP-40 The Adaptive Cycle | [OKR Framework & Governance Dashboard's Bug Protocol](../strategy/okr-framework-dashboard.md) — same "contribution not failure" framing for missed targets |
| AP-41/DP-41 The Transformation Dashboard | [OKR Framework & Governance Dashboard](../strategy/okr-framework-dashboard.md) — same KPI-vs-OKR distinction, same terminology; also points directly at the [Developmental Audit Framework](../quality/developmental-audit-framework.md) |
| AP-42/DP-42 The Three-Channel System | [Committee Information Architecture](../governance/committee-information-architecture.md) — and named explicitly, by this exact pattern name, in Part 5's own structural incompatibilities table for AP-42 |

## Summary: What This Conversion Project Found

Across all 42 pairs, a pattern emerged that's worth stating plainly: **this is not a catalogue of abstract governance theory sitting alongside an unrelated set of OUG documents — it is, in large part, the OUG's own design specification, written at a different level of abstraction.** Roughly half the pairs (concentrated in Blocks 4–7, less so in Blocks 1–3) map onto real, already-converted institutional documents, sometimes by shared name, sometimes by shared numbering code (GP-3, GP-5, GP-6), sometimes by direct citation inside the book's own text. Blocks 1–3 read more like general organizational-dysfunction patterns (many would apply to any bureaucratic institution); Blocks 4–7 read increasingly like the working notes behind the OUG's actual governance architecture.

Two smaller findings worth carrying forward: two spelling discrepancies were found and resolved against full entry text (AP-18 "Programme," AP-23 "Professionalised" — both British spelling, both confirmed against the complete pattern text rather than just the glance tables). And the source document itself was clean — no leaked AI-drafting commentary anywhere in Chapter 14, unlike several of the governance documents converted earlier in this project.

## Cross-References Found While Converting

Blocks 1–5's connections to real OUG documents (logged above) were things I noticed while converting — inferred from shared names, shared terminology, shared gap codes. Block 6 is different: **the source text itself names OUG structures directly, inside the Implementation sections.**

- DP-31's Implementation section states outright: *"The OUG's Mission Hub architecture is a direct instantiation of this pattern."*
- DP-35's Implementation section states: *"in the OUG's case, the Hochschulrat for G1 and G2 roles"* — naming the actual governance body by its actual OUG designation.

This makes sense given how this block was produced — these twelve pairs (Blocks 6–7) were derived retrospectively, evidently with the OUG's own architecture already partly in view, rather than abstracted purely from an earlier dialogue the way Blocks 1–5 were. Worth keeping this distinction in mind for Block 7 as well: expect the same kind of direct, source-text-level naming rather than only inferred correspondence.

Also carried forward from the source: **AP-35 (The Unreviewed Leader) is explicitly connected to AP-23 (The Accidental Leader)** by a standalone note table in the original document — not paraphrased, quoted directly on AP-35's page. Linked bidirectionally.

## Major Finding: Block 5 (6gov) Cross-References Are Exact Code Matches, Not Just Thematic

Block 4's correspondence with real OUG documents (see above) turned out not to be the ceiling — Block 5 is even tighter. Three of six pairs share their **exact gap identifier code** with an already-converted OUG amendment document, not just a similar name:

| Pattern | Gap code | OUG document sharing that exact code |
|---|---|---|
| AP-27/DP-27 The Outcome Measure | GP-3 | [Amendment: Longitudinal Outcome Tracking (GP-3)](../quality/amendment-longitudinal-outcome-tracking.md) — the amendment's own title cites GP-3 |
| AP-28/DP-28 The Named Transformer | GP-5 | [Amendment: Rector's Transformation Mandate (GP-5, GP-6)](../leadership/amendment-transformation-mandate.md) |
| AP-29/DP-29 The Converted Incentive | GP-6 | Same amendment as above (GP-5, GP-6 combined) — and the [Incentive Conversion Statement](../governance/incentive-conversion-statement.md) is the literal document this pattern specifies, matching its three-question structure verbatim |

This confirms the "GP-" and "SP-" and "HP-" codes used throughout this book's derivation notes are the *same* gap-tracking codes used in the OUG's own amendment documents — not a coincidence of naming, but one shared numbering system across the book and the institution's working governance documents. Worth checking systematically whether every GP/SP/HP code in this catalogue has a corresponding amendment somewhere in the repository, since that would mean the pattern catalogue is effectively a annotated index of the OUG's own gap-closure history.

Also: **AP-30 (The Participation Decoy) explicitly names AP-22 (The Participation Façade)** as its structural complement — "where the Participation Façade describes the absence of genuine consultation influence on decisions, the Participation Decoy describes the absence of accountability for those who participate in making them." Linked bidirectionally.

## Major Finding: Block 4 (7org) Is the Direct Theoretical Source for Six Already-Converted OUG Documents

Every one of the six pairs in this block maps onto a real, already-converted institutional document — not thematically, but by shared name and often near-verbatim terminology:

| Pattern | OUG document it's the source of |
|---|---|
| AP-19/DP-19 The Designed Role | [Role Statement](../strategy/role-statement.md) |
| AP-20/DP-20 The Adaptive Institution | [Governance Review Calendar](../governance/governance-review-calendar.md) |
| AP-21/DP-21 The Home That Challenges | [Mission Hub Permeability Architecture](../governance/mission-hub-permeability-architecture.md) — takes its name directly from the pattern |
| AP-22/DP-22 The Quality Mechanism | [Committee Information Architecture](../governance/committee-information-architecture.md) + [Inter-Layer Feedback Protocol](../governance/interlayer-feedback-protocol.md) |
| AP-23/DP-23 The Professionalised Vocation | [Leadership & Stewardship Profiles](../leadership/leadership-stewardship-profiles.md) (the "PRECEPTA" framework) + the [SP-6/SP-7 amendments](../leadership/amendment-capability-measurement.md) — the "scientist's heart / manager's mind" language is shared almost word for word |
| AP-24/DP-24 The Developmental Audit | [Developmental Audit Framework](../quality/developmental-audit-framework.md) — same three-part structure (Self-Assessment, peer panel, Development Report) |

This strongly suggests Block 4 (7org) was the specific dialogue block the OUG's actual governance architecture was built directly against — worth checking whether the other blocks show the same density of correspondence, or whether this one is unusual.

## Cross-References Found While Converting (continued)

- Block 3 (Curr4) reads as a genuinely sequential design argument rather than six independent pairs: AP-13/DP-13 establishes purpose before access; AP-14/DP-14 protects federation quality once access exists; AP-15/DP-15 and AP-16/DP-16 both institute the same underlying move (separate expertise-based design from representation-based governance) at the curriculum level and the individual-role level respectively; AP-17/DP-17 and AP-18/DP-18 apply that same design-before-structure logic to pedagogy and to whole-programme sequencing. Worth considering whether the index or a future synthesis page should name this block-level narrative explicitly rather than leaving it implicit across six separate pages.

## Cross-References Found While Converting (continued)

- **AP-8 (The Loose Thread) and AP-10 (The Passive Consumer)** both invoke "the figure Person Learn8 explicitly warns against" — the same underlying learner archetype approached from two different structural angles (navigation vs. participation). Linked bidirectionally.
- **AP-12 (The Compliance Ceiling) explicitly names AP-1 (The Permission Illusion)** as its structural "twin" — same underlying law/convention confusion, opposite direction (one mistakes tradition for law, the other mistakes law for the limit of ambition). Linked.
- **DP-12 references "HP-1 of the HEI Observation Principles"** and the same "Governance Compliance Map" concept used in DP-1 — worth checking whether "HEI Observation Principles" is a separate document that should eventually be tracked in known-gaps.md if it isn't already converted somewhere in this repository.

## Site Navigation

`docs/_config.yml` in this working copy does not currently have the `minima: nav_pages:` curated list that earlier work on this repo's Jekyll setup established (per prior session notes) — it's running on default GitHub Pages theme settings with no explicit nav curation visible in this file. Worth checking whether `patterns/index.md` needs adding to that list once the live repo's actual `_config.yml` state is confirmed — the version in this working copy may not reflect the latest committed state.
