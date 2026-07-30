---
layout: page
title: "Conversion Notes — Quality Assurance"
---   

[← Back to Quality Assurance](index.md)

Observations that surface while migrating quality documents from Drive to this repository. See [known-gaps.md](../known-gaps.md) for architecture-level gaps; this page is for smaller factual snags found while converting.

---

## Open

- [ ] **Section-numbering mismatch between the QA framework and its own amendment.** [Amendment GP-3](amendment-longitudinal-outcome-tracking.md) inserts a new Section 3.6 ("Longitudinal Outcome Indicators") "following Section 3.5 (Stichprobe)." But [`quality-assurance-academic-governance.md`](quality-assurance-academic-governance.md) v2 numbers Stichprobe as **Section 3.7**, with **3.6** already occupied by "Assessment Validity, Reliability, and Transparency." The amendment appears to have been written against an earlier draft's section numbering that shifted before v2 was finalised. Flagged inline in both documents rather than silently renumbered — needs a real decision on which numbering is authoritative before both are cited together formally.

- [ ] **The Reader's Guide cites a "Leadership & Stewardship Profiles" document (G-06) that can't be located.** Referenced repeatedly — by the Reader's Guide, by [`quality-assurance-academic-governance.md`](quality-assurance-academic-governance.md), and by [`governance/design-authority-constitution.md`](../governance/design-authority-constitution.md) — as the authoritative source for governance role competency requirements and mandate boundaries. No standalone document under this name exists in this repository. It may be content embedded in the [Leadership Development & Induction Framework](../leadership/leadership-development-induction-framework.md) rather than a separate file, or it may be a genuine unfiled gap. Added to [known-gaps.md](../known-gaps.md) — worth checking Drive specifically for this title if it hasn't already surfaced.

- [ ] **The Reader's Guide's document table cites several not-yet-converted or dropped-scope documents as if live.** Strategic Constitution, Strategy Formation Protocol, OKR Framework & Governance Dashboard, Financial Model v3, Gebührenordnung, and the Hochschulfinanzierungsvertrag Plan (all `strategy/` domain, not yet converted) — plus Curriculum Framework and Modulhandbuch, which were deliberately dropped from the curriculum domain's scope earlier (content folded into the New Study Programme Document instead). Not fixed silently — each reference is annotated inline in [`readers-guide-accreditation.md`](readers-guide-accreditation.md) rather than removed, so the Guide's own claims stay checkable against what's actually in the repository.

## Resolved

*(none yet for this domain)*
