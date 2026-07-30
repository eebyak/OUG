---
layout: page
title: "Conversion Notes — Partnership & Federation"
---   


[← Back to Partnership & Federation](index.md)

Observations that surface while migrating partnership documents from Drive to this repository. See [known-gaps.md](../known-gaps.md) for architecture-level gaps; this page is for smaller factual snags found while converting.

---

## Open

- [ ] **"Supervisory Board" and "Finance Committee" appear as governance bodies not named anywhere else in this repository.** [`federated-participation-incentive-framework.md`](federated-participation-incentive-framework.md) gives the "Supervisory Board" rate-setting authority over the Tariff Schedule and describes a "Finance Committee" that recommends compensation changes — both at what the document calls "G2" level. No other converted document (Governance & Decision Framework, Federated Legal Model, Grundordnung) uses either term; the closest equivalent by function would be the Hochschulrat (G1) or a Rectorate-level financial role. Not renamed here — flagged in case "Supervisory Board" is a deliberate distinct body (a real governance layer this repository hasn't captured yet) or simply an earlier-draft name for the Hochschulrat that never got reconciled.

- [ ] **Internal cross-reference error in the Partner Membership Framework.** Duty 1 (Section 3) says persistent module failure "triggers a module suspension process under Section 7" — but module suspension is actually specified in Section 8, not Section 7 (Section 7 is the Onboarding Process). Flagged inline in the converted document with `[sic]` rather than silently corrected, since it's a source-document error, not a conversion error.

## Resolved

- [x] **HP-7 status — third document now corroborates "resolved."** [`amendment-lehrpersonalmodell.md`](amendment-lehrpersonalmodell.md) Amendment B explicitly states that the Partner Membership Framework's Task Architecture (Section 5) is the formal closure of HP-7, consistent with [`governance-gap-closure-v2.md`](../governance/governance-gap-closure-v2.md). This is now three documents agreeing HP-7 is closed, against [`design-signature-founding.md`](../governance/design-signature-founding.md) alone still listing it as an open commitment — strong evidence the Design Signature entry is simply stale rather than reflecting a live disagreement. See [governance/conversion-notes.md](../governance/conversion-notes.md) for the original note.
