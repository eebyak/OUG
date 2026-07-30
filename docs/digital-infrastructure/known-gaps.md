---
layout: page
title: "Known Gaps"
---

[← Back to Digital Infrastructure](index.md)

This page records documents, inconsistencies, or unresolved decisions that affect the Digital Infrastructure domain.

---

## Framework Completeness

- [x] ~~**"Documents 1–6" versus four documents actually found.**~~ **Resolved.** All four documents (D1 Manifesto, D2 Architecture Reference Model, D3 Functional Domain Specifications, D4 HEI IT Architecture Evaluation Framework) are converted and cross-reference each other consistently as a complete set. No Document 5 or 6 is named anywhere across all four. Working conclusion: the framework was only ever fully specified as four documents; the "1–6" citation elsewhere in the repository (the Five-Year Finance Plan, the OUG Report 2025–26) overstates what exists. Not corrected retroactively in those documents' own text — flagged there with a note instead, per this project's practice of not silently editing source conversions.

## ⭐ Next Actionable Item: Complete the Maturity Scorecard

- [ ] **A [working scorecard template](maturity-scorecard-newstudy.md) now exists, partially pre-filled from public evidence — it still needs internal completion.** Two of the platform's own legal pages (its privacy policy and accessibility statement) turned out to be unusually candid, giving real, citable evidence for roughly 15–20 of Document 4's 47 maturity criteria and several of its 37 compliance gates — mostly revealing genuine, self-acknowledged gaps (encryption at rest not implemented, DPIA and RoPA both explicitly "in progress," hosting DPAs not yet signed, several non-European sub-processors still in use for front-end assets, accessibility only internally self-assessed). Everything else in the template is left honestly blank rather than guessed, since it requires internal evidence (audit logs, actual SLA performance, adoption metrics, ARB records) that no public page will ever show. **Someone with real access to the platform's operations needs to complete the remaining rows.**
- [ ] **A prior, more fundamental question the scorecard surfaces:** the platform's own pages state, repeatedly, that it is *"not an official DHBW system"* and that its institutional governance relationship is *"still pending."* Completing the scorecard is worthwhile regardless, but the scorecard itself recommends resolving this institutional-status question before treating the result as a statement about the OUG's or DHBW's actual maturity — see the template's closing "Before You Finalise This" section.

## Cross-Domain Reconciliation

- [ ] **Relationship to the Platform: Living Learning System document.** [Curriculum's Platform document](../curriculum/platform-living-learning-system.md) describes an eight-milestone platform development path. This domain's Document 2 (Architecture Reference Model) and Document 3 (Functional Domain Specifications) describe the same underlying platform at the level of technical architecture rather than pedagogical milestones. The two have not yet been explicitly cross-referenced or checked for consistency.
- [ ] **Relationship to the Five-Year Finance Plan's IT cost breakdown.** The Finance Plan's Part IV prices out a 23-tool technology stack. Whether that specific tool list is consistent with the architecture this domain's documents specify — and would pass D1's own three-condition sovereignty test (hosting independence, update independence, fork rights) — has not been checked systematically, though several individual tools (Nextcloud, Matrix/Element, Gravitee) appear in both.
- [ ] **D3's 25-criterion evaluation table and D4's 47-criterion evaluation table are related but not identical** — D3's table (in its own closing section) appears to be an earlier or more condensed version of the same scoring logic that D4 develops fully into compliance gates plus a 0–5 maturity ladder. Worth confirming whether D3's table is meant to be superseded by D4's fuller version, or used alongside it at a different level of granularity.

---

*Update this page only when a gap is confirmed, resolved, consolidated into another document, or deliberately left open.*
