# Conversion Notes — Curriculum

[← Back to Curriculum & Pedagogy](index.md)

Observations that surface while migrating curriculum documents from Drive to this repository — inconsistencies between documents, numbers that don't quite line up, claims worth double-checking against the source of truth. These aren't gaps in the architecture (see [known-gaps.md](../known-gaps.md) for that) — they're small factual snags found *while converting*, kept here so they don't get lost and can be resolved in a dedicated pass later rather than silently ignored or silently "fixed" by guessing.

**How to use this:** add an entry whenever a conversion turns up something that looks off. Resolve by checking against source data (e.g. the actual Modulhandbuch once it exists) and marking closed rather than deleting, so there's a record of what was checked and when.

---

## Open

- [ ] **Module learning-outcome completion count.** Two independently-written documents both cite the same figure for how many of the 37 B.Sc. CS modules have complete learning-outcome specifications — the [Didactic Framework](didactic-framework-bsc-cs.md) and [Equity by Design](equity-by-design.md) working paper. The [Platform](platform-living-learning-system.md) document's consolidated table also states "4 of 37 modules fully specified." All three agree numerically (4 complete / 33 incomplete), which is either good corroboration across independently-written documents, or the same stale figure copied forward by whoever drafted each one. Worth checking against the actual Modulhandbuch once it's migrated, to confirm the number still holds rather than assuming three citations makes it three independent confirmations.

- [ ] **Module numbering scheme doesn't match between two documents describing the same programme.** The [Didactic Framework](didactic-framework-bsc-cs.md)'s Module Architecture Table (Section V) and the [New Study Programme Document](new-study-programme-document.md)'s module list (Section V) both describe the B.Sc. Computer Science curriculum, using the same stream names (MAF, SPS, PSC, DAI, HSC, RPS) — but assign different `T4INF####` codes to what appear to be the same modules. Example: "Programming Foundations" is `T4INF1004` in the Didactic Framework's table but `T4INF3001` in the New Study Programme Document.
  **Update:** the machine-generated module data in [`skill-based-modules/`](skill-based-modules/index.md) uses the *Didactic Framework's* numbering (`T4INF1004`, `T4INF1602`, `T4INF2001`–`2006`, `T4INF3102`, `T4INF3915`, `T4INF4900`, `T4INF4902`, `T4INF4348`, `T4INF4324`, `T4INF9006`, etc.) — not the New Study Programme Document's. Since this is pipeline output generated from source course data rather than hand-written prose, this is real evidence that the New Study Programme Document's numbering is the one that drifted, not the Didactic Framework's. Not yet fully closed — still worth confirming directly against the Modulhandbuch once migrated — but this is no longer just "two documents disagree," it's "two documents disagree and a third, machine-generated source sides with one of them."

- [ ] **Internal module-count inconsistency within the New Study Programme Document itself.** Section V's prose says the document "provides the module-level description for each of the 37 taught modules in the programme, plus the Capstone and Thesis" (implying 39 total), but the Section IV summary table sums stream module counts (6+6+5+7+4+4) plus the 2-item Capstone/Thesis row to a stated **total of 34**. The two figures — 37 taught modules mentioned in prose vs. a table that totals 34 — don't reconcile within the same document. Worth resolving which number is correct (and whether "37" is a copy-paste artifact from the other curriculum documents that consistently use that figure) before citing either number elsewhere.

---

## Resolved

*(none yet)*
