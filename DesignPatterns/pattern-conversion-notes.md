# Conversion Notes — Design Pattern Catalogue

[← Back to the pattern catalogue](index.md)

Tracking progress converting all 42 antipattern/design-pattern pairs from `OUG_Amazon_CH14-designpatterns.docx` (Chapter 14) into individual Markdown pages.

## Source Quality

Unlike several other source documents converted in this repository, Chapter 14 required **no cleanup** — no leaked AI-drafting commentary, no structural inconsistency. Verified programmatically against the raw document XML rather than by sampling: all 42 antipattern headers use consistent dark red shading (`#8B1A1A`), all 42 design pattern headers use consistent dark green (`#1A5C4A`), and all 84 entries use the identical 5-row anatomy (1 header row + 5 content rows). This appears to be the fully cleaned, unified version of the chapter — the inconsistencies (navy vs. red headers, a lean 3-part anatomy for 12 pairs) referenced in earlier work on this book are not present in this upload.

## One Naming Discrepancy Found

**AP-18 / DP-18** and **AP-23 / DP-23** have two different names depending on which glance table in the source is consulted:

| Pair | Master glance table (front matter) | Block-specific glance table (immediately preceding the entry) |
|---|---|---|
| AP-18 | "The Accidental **Program**" | "The Accidental **Programme**" |
| AP-23 (DP-23) | *(need to re-verify exact spelling in full entry text when converting)* | "The **Professionalised** Vocation" |

The book uses British spelling conventions dominantly elsewhere (e.g. "Programme," "Professionalised," "Organisational"). The catalogue index above uses the block-specific (British) spelling as more likely authoritative, since it sits immediately next to the full entry. **Not yet resolved against the actual AP-18/DP-18 and AP-23/DP-23 entry text** — flag for correction once those two pairs are converted, in case the full entry itself uses a third variant.

## Batch Progress

| Block | Pairs | Status |
|---|---|---|
| 1 · HEI Observations | 1–6 | 🔄 1 of 6 converted (AP-1/DP-1) |
| 2 · Learn8 | 7–12 | ⬜ Not started |
| 3 · Curr4 | 13–18 | ⬜ Not started |
| 4 · 7org | 19–24 | ⬜ Not started |
| 5 · 6gov | 25–30 | ⬜ Not started |
| 6 · Person 1 | 31–36 | ⬜ Not started — retrospectively derived, see index note |
| 7 · Person 2 | 37–42 | ⬜ Not started — retrospectively derived, see index note |

## Site Navigation

`docs/_config.yml` in this working copy does not currently have the `minima: nav_pages:` curated list that earlier work on this repo's Jekyll setup established (per prior session notes) — it's running on default GitHub Pages theme settings with no explicit nav curation visible in this file. Worth checking whether `patterns/index.md` needs adding to that list once the live repo's actual `_config.yml` state is confirmed — the version in this working copy may not reflect the latest committed state.
