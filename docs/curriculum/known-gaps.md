---
layout: page
title: "Known Gaps"
---

[← Back to Curriculum & Pedagogy](index.md)

This page records documents, inconsistencies, or unresolved decisions that affect the Curriculum and Pedagogy domain.

Some items require existing documents and data sources to be reconciled. Others require a missing implementing document to be added before the relevant part of the academic architecture can be treated as complete.

**How to use this list:** for each item, determine whether it can be resolved by correcting an existing document, reconciling available source material, or creating a separate implementing instrument.

---

## Programme and Module Architecture

* [ ] **Authoritative Modulhandbuch** — two source documents are available: `Modulhandbuch.docx`, which contains the programme rationale, qualification goals, curriculum architecture, pathways, and module-description framework; and `OUG_Modulhandbook.docx`, which contains detailed individual module specifications. These sources must be reconciled with the [New Study Programme Document](new-study-programme-document.md), the [Didactic Framework](didactic-framework-bsc-cs.md), and the [machine-readable module data](skill-based-modules/index.md) before a definitive Modulhandbuch is published.

* [ ] **Module inventory, codes, and ECTS totals** — the curriculum documents do not yet use one fully consistent module inventory. Module codes differ between the New Study Programme Document and the Didactic Framework, while the machine-readable data generally follows the Didactic Framework. The Programme Document also states that the degree contains 160 ECTS of stream modules but sets the thesis threshold at 150 ECTS of completed stream modules. Module counts, codes, stream assignments, and degree thresholds must be reconciled against the authoritative Modulhandbuch.

## Machine-Readable Curriculum

* [ ] **OOAPI version and data inventory** — the [New Study Programme Document](new-study-programme-document.md) refers to OOAPI v5, while the repository publishes [OOAPI v6 module data](skill-based-modules/index.md). The current version, authoritative source, regeneration process, and relationship between the JSON records, Modulhandbuch, live platform, and narrative curriculum documents should be stated consistently.

* [ ] **Curriculum pipeline artifacts** — the machine-readable curriculum index refers to generated artifacts such as `curriculum_index.json`, `edges.json`, source JSON files, and conversion scripts that are not currently included in the published directory. Confirm which artifacts are required for transparency and reproducibility and which belong only to the operational platform repository.

## Research and Doctoral Education

* [ ] **Doctoral Regulations / Promotionsordnung** — the [Research & Doctoral Framework](research-doctoral-framework.md) defines doctoral admission, supervision, progression, examination, governance, and degree-awarding principles. No separate formal doctoral regulation has yet been identified that gives these provisions a binding procedural basis.

* [ ] **Research Ethics and Integrity Policy** — the Research & Doctoral Framework establishes the Research Ethics Committee, Research Integrity Officer, review requirements, misconduct responsibilities, and principles for AI use. It also refers to further OUG research ethics policies and guidance that have not yet been identified as separate implementing documents.

---

*Update this page only when a gap is confirmed, resolved, consolidated into another document, or deliberately left open.*
