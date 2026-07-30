---
layout: page
title: "Known Gaps"
---

[← Back to Digital Infrastructure](index.md)

This page records documents, inconsistencies, or unresolved decisions that affect the Digital Infrastructure domain.

---

## Framework Completeness

- [x] ~~**"Documents 1–6" versus four documents actually found.**~~ **Resolved.** All four documents (D1 Manifesto, D2 Architecture Reference Model, D3 Functional Domain Specifications, D4 HEI IT Architecture Evaluation Framework) are converted and cross-reference each other consistently as a complete set. No Document 5 or 6 is named anywhere across all four. Working conclusion: the framework was only ever fully specified as four documents; the "1–6" citation elsewhere in the repository (the Five-Year Finance Plan, the OUG Report 2025–26) overstates what exists. Not corrected retroactively in those documents' own text — flagged there with a note instead, per this project's practice of not silently editing source conversions.

## ⭐ Next Actionable Item: Score the Live Platform

- [ ] **The live [New Study Module Catalogue](https://newstudy.campuscircle.de/) has not been formally scored against Document 4's compliance gates and maturity ladder.** This is now fully unblocked — all four documents exist. The platform demonstrably implements real pieces of this architecture: OOAPI-based module data, course sign-in, skill-profile development, and Matrix/Element-based video and whiteboard rooms (named explicitly three times across Documents 2 and 3 as the framework's own recommended tooling — this is corroborating evidence, not a coincidental match). What's missing is the actual scored assessment: working through Document 4's 37 compliance gates (Pass/Fail) and 47 maturity criteria (0–5 scale, 235 points across 9 sections) against the real platform, the way the [Design Signature Founding](../governance/design-signature-founding.md) scores OUG governance against the 42-pattern catalogue cell by cell. **This is the natural next piece of work for this domain.**

## Cross-Domain Reconciliation

- [ ] **Relationship to the Platform: Living Learning System document.** [Curriculum's Platform document](../curriculum/platform-living-learning-system.md) describes an eight-milestone platform development path. This domain's Document 2 (Architecture Reference Model) and Document 3 (Functional Domain Specifications) describe the same underlying platform at the level of technical architecture rather than pedagogical milestones. The two have not yet been explicitly cross-referenced or checked for consistency.
- [ ] **Relationship to the Five-Year Finance Plan's IT cost breakdown.** The Finance Plan's Part IV prices out a 23-tool technology stack. Whether that specific tool list is consistent with the architecture this domain's documents specify — and would pass D1's own three-condition sovereignty test (hosting independence, update independence, fork rights) — has not been checked systematically, though several individual tools (Nextcloud, Matrix/Element, Gravitee) appear in both.
- [ ] **D3's 25-criterion evaluation table and D4's 47-criterion evaluation table are related but not identical** — D3's table (in its own closing section) appears to be an earlier or more condensed version of the same scoring logic that D4 develops fully into compliance gates plus a 0–5 maturity ladder. Worth confirming whether D3's table is meant to be superseded by D4's fuller version, or used alongside it at a different level of granularity.

---

*Update this page only when a gap is confirmed, resolved, consolidated into another document, or deliberately left open.*
