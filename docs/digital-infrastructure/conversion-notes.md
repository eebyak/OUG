---
layout: page
title: "Conversion Notes"
---

[← Back to Digital Infrastructure](index.md)

Observations that surface while migrating the European HEI Digital Alliance Framework documents from uploaded `.docx` files into this repository.

---

## Source Quality

D1 (Manifesto) converted cleanly — well-structured, no leaked drafting commentary, consistent formatting throughout. Its "Adoption and Signature" section contains a blank institution/alliance signature form (name, title, date fields) not relevant to a reference document; omitted from the converted page with a note rather than reproduced as dead form fields.

## The "Documents 1–6" Discrepancy

Both the [Five-Year Finance Plan](../strategy/five-year-finance-plan.md) and [OUG Report 2025–26](../communications/annual-report-2025-26.md) cite "Documents 1–6" of this framework. The Manifesto's own "Companion Documents" section (its closing pages) names only Document 2 (Architecture Reference Model), Document 3 (Functional Domain Specifications), and Document 4 (HEI IT Architecture Evaluation Framework) as existing alongside itself — four documents total. No Document 5 or 6 is named anywhere in D1's own text. Given D2, D3, and D4 all uploaded together with D1 and all cross-reference each other consistently as a complete set, the working assumption is that **the framework was only ever fully specified as four documents**, and the "1–6" figure elsewhere in the repository is either a planning aspiration that was never realized or an imprecision in those other documents. Logged as an open item in [known-gaps.md](known-gaps.md) rather than silently resolved either way.

## Batch Progress

| Document | Status |
|---|---|
| D1 — Manifesto | ✅ Converted → [`manifesto.md`](manifesto.md) |
| D2 — Architecture Reference Model | ✅ Converted → [`architecture-reference-model.md`](architecture-reference-model.md) |
| D3 — Functional Domain Specifications | ⬜ Not yet converted (~1,760 lines in source) |
| D4 — HEI IT Architecture Evaluation Framework | ⬜ Not yet converted (~1,540 lines in source) |

## D2 Findings

- **The live New Study platform's tooling is directly named as recommended architecture, not merely compatible with it.** D2's Layer 5 (Experience and Engagement) recommends "Element/Matrix (messaging)" by name — exactly the Matrix/Element rooms with video calls and whiteboarding you described as already running. Annex A confirms this in more detail: Element (Matrix protocol), UK-origin, open-source (Apache), federated protocol. This is corroborating evidence, not just a plausible connection — worth citing directly when the platform is eventually scored against Document 4's maturity ladder.
- **D2's Annex B compliance checklist has empty "Status" and "Target" columns in the source** — it's a template for institutional self-assessment, not a completed assessment. Reproduced as evidence requirements only; filling it in for the OUG's actual live implementation is exactly the maturity-scoring work flagged for after D1–D4 are all converted.
- D2 references "Domain Specification 3e" (Administration Systems) by name when discussing AI-augmented administrative workflows — confirms Document 3 has at least five lettered sub-specifications (3a–3e likely), matching the "five domains" named in D1's companion documents list and this domain's own index.

## Cross-References Found While Converting

- D1's Principle II (§5, "Open source as the sovereignty instrument") gives a precise three-condition test — hosting independence, update independence, fork rights — for when open-source software counts as sovereignty-compliant. Worth checking against the [Five-Year Finance Plan's](../strategy/five-year-finance-plan.md) 23-tool IT stack (Part IV) once Documents 2 and 3 are converted, to see whether each tool in that stack would actually pass this test.
- D1 explicitly names the live reference points its principles are drawn from — SURF/SURFdrive, SWITCH, DH.NRW, DFN/eduGAIN, Finland's Digivisio 2030 — real European cooperative infrastructure bodies, not hypothetical examples. Worth knowing these are real, checkable precedents if this Manifesto is ever used externally (e.g. toward the partnerships suggested in the [Market Study](../communications/market-study.md)).

## Site Navigation

Added `digital-infrastructure/index.md` to `docs/_config.yml`'s `header_pages` list, and added a "Digital Infrastructure" section to the main `docs/index.md`, updating "seven connected domains" to "eight."
