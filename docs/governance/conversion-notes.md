# Conversion Notes — Governance

[← Back to Governance](index.md)

Observations that surface while migrating governance documents from Drive to this repository — inconsistencies between documents, numbers that don't quite line up, claims worth double-checking against the source of truth. These aren't gaps in the architecture (see [known-gaps.md](../known-gaps.md) for that) — they're small factual snags found *while converting*, kept here so they don't get lost and can be resolved in a dedicated pass later rather than silently ignored or silently "fixed" by guessing.

**How to use this:** add an entry whenever a conversion turns up something that looks off. Resolve by checking against source data and marking closed rather than deleting, so there's a record of what was checked and when.

---

## Open

- [ ] **Governance folder is still larger than what's currently in scope.** The `governance/` folder on Drive contains 18 files; the 9 from an earlier screenshot plus now `federated-legal-model.md` are reflected in `governance/index.md` and the main index's document list. The remaining 8 — Strategic Positioning ("The Missing Layer"), Incentive Conversion Statement, Design Authority Constitution, Mission Hub Permeability Architecture, Governance Review Calendar, Design Signature Founding (the 42-principle scorecard), Governance Principles Assessment, Portfolio Governance — exist on Drive but are deliberately deferred for now. Portfolio Governance is a native Google Doc rather than `.docx`, as is Grundordnung despite that one being in scope. Revisit when ready to expand governance scope.

- [ ] **Anlage 1 and Anlage 2 (referenced by Grundordnung § 16) not yet migrated.** Grundordnung § 16 formally adopts "Strategisches Rahmenwerk – First Principles and Derived Institutional Capabilities" (Anlage 1) and "Strategic Decision Protocol" (Anlage 2) by reference, but neither exists as a file in this repository yet. The statute now points at documents that don't exist here.

## Resolved

- [x] **"Federated Legal Model" — real document found and converted.** Chapter 17's inventory named a document called *Federated Legal Model* for the Governance domain; it wasn't found under that name in the original 18-file Drive listing. A file called `Federated_Legal_Model_2.docx`, uploaded separately, turned out to be it — or close enough to be treated as it: Part I is titled "Foundational Legal Identity of the Open University of Germany" and its opening sections define the exact four-way constitutional separation (employment authority / academic authority / degree-awarding authority / operational administration) that chapter 17 attributes to this document. Converted in full as [`federated-legal-model.md`](federated-legal-model.md) — 9 Parts, §1–§21, plus five appendices (Legal Responsibility Matrix, Joint & Dual Degree Calculation Formula, Academic Affiliation Contract Template, Conflict Escalation Structure, Central Examination Regulation Annex, Responsibility & Signature Matrix).

  **This supersedes the original "treat Grundordnung as the match" decision** from earlier in this log — that substitution was made when no candidate document could be found. `Grundordnung`'s entry in the main index has *not* been reverted, since it's independently valuable as the founding statute; `federated-legal-model.md` has been added as its own new entry instead. Both now exist in the repository as separate documents.

  **Source-quality issue found and fixed during conversion:** the source `.docx` contained several passages of leaked AI-drafting commentary between Parts — meta-remarks like *"Excellent. We now draft Part III – Degree Awarding Protocol in full constitutional form... This draft assumes..."* and *"It operationalizes your Governance Framework (G1–G4) and prevents the political drift Manning describes"* — addressed to whoever was drafting the document, not written as constitutional text. Four such passages were identified and removed (before Parts III, V, VI, and one shorter aside before the Conflict Escalation Structure appendix). None of the surrounding substantive legal text was altered. Worth knowing this document was AI-assisted in its drafting and worth a pass to confirm no other artifacts remain, since these four were caught by pattern-matching on phrases like "Excellent," "We now draft," and "Below is" — a different leaked phrasing could have been missed.

  **Also fixed:** several sections used Word's ASCII-art grid-table format (long dash borders) rather than proper structure — the Legal Responsibility Matrix (8 sub-tables) and the Responsibility & Signature Matrix (6 RACI-style tables) were rebuilt as clean Markdown tables. Content unchanged, only the formatting.
