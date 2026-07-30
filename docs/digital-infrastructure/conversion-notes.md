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
| D3 — Functional Domain Specifications | ✅ Converted → [`functional-domain-specifications.md`](functional-domain-specifications.md) |
| D4 — HEI IT Architecture Evaluation Framework | ✅ Converted → [`hei-evaluation-framework.md`](hei-evaluation-framework.md) |

## 🎉 All Four Documents Converted

The Digital Infrastructure domain is complete: Manifesto (why), Architecture Reference Model (how, at the structural level), Functional Domain Specifications (how, at the operational level, domain by domain), and now the Evaluation Framework (how to know whether it's actually true).

## D4 Findings

- **This is genuinely the instrument, not just a description of one.** 37 binary compliance gates and 47 graduated maturity criteria across 9 sections, summing to a 235-point score with six named interpretation bands (Not Compliant → Early Stage → Developing → Defined → Managed → Leading). Three sections (Architecture Foundations, Identity and Federation, Backend Data) are marked "Critical" with a required alliance-level minimum maturity level — meaning a real institution couldn't claim overall compliance while failing these, even with a high score elsewhere.
- **D4's scoring table structure and D3's evaluation criteria table are related but not identical** — D4 develops the fuller compliance-gate-plus-maturity-ladder version; D3's closing table is a leaner 25-criterion precursor. Logged as an open reconciliation question in [known-gaps.md](known-gaps.md) rather than assumed to be redundant.
- **Several source tables in D4 are blank templates for institutional self-completion** (the Section 10 score summary's "Your Score"/"Gap" columns, the full Section 11 improvement plan template, Annex A's "Status" column, Annex B's radar chart values, Annex C's reporting fields). Reproduced as structure only, not populated with invented data — consistent with how D2's Annex B checklist was handled.

## Cross-Domain Note: The Maturity-Scoring Work Is Now Unblocked

With all four documents converted, the task flagged at the start of this domain's work — scoring the live [New Study Module Catalogue](https://newstudy.campuscircle.de/) against the framework's own maturity ladder — is fully actionable for the first time. See [known-gaps.md](known-gaps.md) for how this is now framed as the domain's next concrete piece of work, structured the same way [Design Signature Founding](../governance/design-signature-founding.md) scores OUG governance against the 42-pattern catalogue: cell by cell, with evidence, not as a general assertion.

## Cross-References Found While Converting

- **Two more direct mentions of Matrix/Element**, beyond D2's Annex A component recommendation: Domain 3e's notification requirements explicitly name "messaging platform (Matrix/Element)" as one of the required notification channels for the administration workflow system. Combined with D2's Layer 5 recommendation and Annex A entry (Element/Matrix, UK-origin, open-source Apache licence, federated protocol), that's four independent mentions across three documents — clearly the framework's actual intended tooling, not a coincidental match to what's live on New Study.
- **D2's Annex B and D3's closing table are both precursors to D4's fuller scoring system** — D2's Annex B is a compliance checklist with blank Status/Target columns; D3's closing table is a 25-criterion, 50-point scorecard; D4 develops both into the full 37-gate, 47-criterion, 235-point system. All three are templates for institutional self-completion in the source, not populated assessments — reproduced as structure only throughout this domain's conversion, consistent with the project's practice of not inventing scores that don't exist.
- **The cross-domain boundary rules table in D3 is the most load-bearing content in that document** — an explicit, enumerated list of what's permitted and forbidden between all five domains (e.g. Analytics → Learning Systems is "Not Permitted (automated)" specifically to block automated feedback loops from learner data into course content). Any future OUG platform architecture decision should be checked against this table before implementation.
- D2 references "Domain Specification 3e" (Administration Systems) by name when discussing AI-augmented administrative workflows — confirmed by D3's actual five lettered sub-specifications (3a–3e), matching the "five domains" named in D1's companion documents list and this domain's own index.
- D1's Principle II (§5, "Open source as the sovereignty instrument") gives a precise three-condition test — hosting independence, update independence, fork rights — for when open-source software counts as sovereignty-compliant. Worth checking against the [Five-Year Finance Plan's](../strategy/five-year-finance-plan.md) 23-tool IT stack (Part IV), to see whether each tool in that stack would actually pass this test.
- D1 explicitly names the live reference points its principles are drawn from — SURF/SURFdrive, SWITCH, DH.NRW, DFN/eduGAIN, Finland's Digivisio 2030 — real European cooperative infrastructure bodies, not hypothetical examples. Worth knowing these are real, checkable precedents if this Manifesto is ever used externally (e.g. toward the partnerships suggested in the [Market Study](../communications/market-study.md)).

## Site Navigation

Added `digital-infrastructure/index.md` to `docs/_config.yml`'s `header_pages` list, and added a "Digital Infrastructure" section to the main `docs/index.md`, updating "seven connected domains" to "eight."
