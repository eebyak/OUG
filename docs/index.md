<picture>
  <source media="(prefers-color-scheme: dark)" srcset="images/Logo1.png">
  <img src="images/Logo2.png" alt="OUG logo — an open book/gate whose three connected nodes represent distinct institutions and learners joined through a common academic structure, with the connecting lines standing for recognition across that federation" width="380">
</picture>

# Open University of Germany

## Designing a University from First Principles

The Open University of Germany (OUG) is a fictive public university federated model designed for a society in which learning no longer follows a single path, at a single pace, or within a single institution.


> **What would a university look like if it were designed around learning first, if we could design from first principles, assuming that there are no inherited structures and money and IT infrastructure wouldn't stop us?**

The OUG is not conceived as a replacement for existing universities. It is designed as a federated, open, and publicly anchored institution that connects them. Its purpose is to make high-quality higher education more accessible, more flexible, and more responsive to learners whose lives do not fit the assumptions of the traditional degree.

This repository contains the evolving institutional architecture of the OUG.

To understand **why** each element exists, please refer to the book.
**Designing a University from First Principles**

---

## The Core Proposition


> **When the same difficulties recur across institutions, roles, and reform efforts, the problem may not be the people. It may be the architecture.**


The OUG therefore treats the university as a deliberately designed public institution. Its governance, curriculum, quality assurance, financing, legal structure, and digital infrastructure are developed as parts of one coherent system.

---

## How the Architecture Was Developed

The OUG design emerged from long-term experience across higher education systems, roles, and institutional levels.

Alongside this experience, a series of blank-slate dialogues was conducted with people who hold different forms of insider knowledge: governance practitioners, strategists, curriculum designers, public-sector actors, institutional observers, administrators, and learners.

Each dialogue began with the same question:

> **If you had no financial, political, or IT constraints, and had the power to create a university on a blank slate, what would it look like?**

The dialogue partners were not shown the OUG design and were not asked to evaluate it. Their independently articulated ideas were interpreted into principles and returned to them for verification.

The resulting principles were then compared across perspectives and used to stress-test the emerging OUG architecture.

This work distinguishes between:

- **OUG Founding Commitments** — the personal and moral commitments from which the OUG was originally born;
  - every person is a student;
  - every person has the right to learn;
  - a democratic society has a responsibility to enable learning for all.

- **Bologna Founding Principles** — principles visible in the architecture of the earliest university:
  - learning is the goal;
  - the learner directs the learning relationship, while the institution holds the accountability;
  - what is available to learn is determined by learner need.

- **Dialogue-Derived Principles** — first principles independently articulated across the blank-slate dialogues and verified with the dialogue partners.
  - 42 principles were derived based on open dialogues;
  - the interlocutors agreed to the principles that were documented as emerging from the dialogue.

- **Institutional Design Principles** — portable structural rules synthesised from OUG commitments, the Bologna principles, the dialogue-derived principles, research, and legal realities.

- **Antipatterns and Design Patterns** — named recurring failures and reusable counter-designs;
  - in the spirit of software engineering, design patterns are a way to design systems around best practices. They can also be expressed as antipatterns — spaghetti code is one such antipattern. Patterns support communication at a meta-level about situations, because one word (the pattern name) is easier to use than a complex description.

- **Architectural Decisions** — the specific choices made for the OUG;
  - the OUG follows an architecture that is a specific implementation. It will adhere to some patterns but not all. It therefore has a signature that describes how well these patterns are implemented — like software architectures, not all patterns are used all the time. They are carefully chosen for a purpose and composed.
  - *Founding Commitments, Bologna Principles, Dialogue-Derived Principles, the Pattern Catalogue, and Architectural Decisions are all documented and reasoned through in the book. This repository documents their result — the Implementing Documents below, organised into the seven domains chapter 17 describes — not the derivation or decision process itself.*

- **Implementing Documents** — the statutes, frameworks, regulations, and operating models that make those choices concrete. This repository is designated for their collection, which can be very extensive. The main reasoning behind the architectural design can be found in the book.

---

## Start Here

The repository is organised into seven domains, exactly as described in Chapter 17 of the book. Each domain folder will fill in as documents are migrated from source; a link below that 404s simply hasn't been added yet.

### Curriculum & Pedagogy

- [Curriculum](curriculum)
- [Modules](curriculum/skill-based-modules)
- [Didactic Framework, B.Sc. Computer Science](curriculum/didactic-framework-bsc-cs.md)
- [Equity by Design Principles](curriculum/equity-by-design.md)
- [Platform: From Static Curriculum to Living Learning System](curriculum/platform-living-learning-system.md)
- [The OUG Presence Architecture](curriculum/presence-architecture.md)
- [Research & Doctoral Framework](curriculum/research-doctoral-framework.md)
- [New Study — B.Sc. Computer Science, Programme Document](curriculum/new-study-programme-document.md)

### Governance

- [Allgemeinwohl Verfassung (Public-Benefit Constitution)](governance/allgemeinwohl-verfassung.md)
- [Grundordnung](governance/grundordnung.md)
- [Rechtliche Implementierungsvoraussetzungen (Legal Implementation Requirements)](governance/legal-implementation-requirements.md)
- [Governance Artikel v2](governance/governance-article-v2.md)
- [Governance Gap Closure v2](governance/governance-gap-closure-v2.md)
- [Committee Information Architecture](governance/committee-information-architecture.md)
- [Code of Collegial Conduct](governance/code-of-collegial-conduct.md)
- [Inter-Layer Feedback Protocol](governance/interlayer-feedback-protocol.md)
- [Strategic Clarity Statement](governance/strategic-clarity-statement.md)

### Leadership & People

- [Leadership Development & Induction Framework](leadership/leadership-development-induction-framework.md)
- [Amendment: The Rector's Transformation Mandate and Incentive Conversion (GP-5, GP-6)](leadership/amendment-transformation-mandate.md)
- [Amendment: Capability Measurement and Governance Career Recognition (SP-6, SP-7)](leadership/amendment-capability-measurement.md)
- [Academic Community & Collegial Life Charter](leadership/academic-community-charter.md)
- [Founding Council Letters](leadership/founding-council-letters.md)
- [Founding Member Profile — Prof. Kay Berkling](leadership/founding-member-profile.md)

### Partnership & Federation

- [Partner Membership Framework](partnership/partner-membership-framework.md)
- [Federated Participation & Incentive Framework](partnership/federated-participation-incentive-framework.md)
- [Amendment: Lehrpersonalmodell and Kapazitätswirksamkeit](partnership/amendment-lehrpersonalmodell.md)

### Quality Assurance

- [Quality Assurance & Academic Governance](quality/quality-assurance-academic-governance.md)
- [Amendment: Longitudinal Outcome Tracking (GP-3)](quality/amendment-longitudinal-outcome-tracking.md)
- [Developmental Audit Framework](quality/developmental-audit-framework.md)
- [Reader's Guide for the Accreditation Committee](quality/readers-guide-accreditation.md)
- [Prüfungsordnung](quality/pruefungsordnung.md)

### Strategy & Finance

- [Strategic Constitution](strategy/strategic-constitution.md)
- [The OUG Role Statement](strategy/role-statement.md)
- [Strategy Formation Protocol](strategy/strategy-formation-protocol.md)
- [OKR Framework & Governance Dashboard](strategy/okr-framework-dashboard.md)
- [Five-Year Finance Plan 2026–2030](strategy/five-year-finance-plan.md) · [Finanzmodell v3](strategy/finanzmodell-v3.xlsx)
- [Ministeriumsmemorandum v2](strategy/ministeriumsmemorandum-v2.md)

### Presentation & Communication

- [The OUG Communication Architecture](communications/communication-architecture.md)
- [OUG Market Study](communications/market-study.md)
- [Ein gewöhnlicher Dienstag (A Perfectly Ordinary Tuesday)](communications/ein-gewoehnlicher-dienstag.md)
- [Menschlicher Fall (The Human Case)](communications/menschlicher-fall.pptx)
- [Partner and Ministry Decks](communications/partner-and-ministry-decks/) — DHBW, Die Fehlende Schicht, Ministerium, Erklärung
- [OUG Report 2025–26](communications/annual-report-2025-26.md)

## Document Status

The OUG is a prospective institutional design and evolving founding prototype.

Documents in this repository may have different levels of maturity:

| Status | Meaning |
|---|---|
| **Conceptual** | A proposed design that has not yet undergone formal review |
| **Drafted** | A complete working draft exists |
| **Internally validated** | Tested for coherence against the OUG principles and architecture |
| **Externally reviewed** | Reviewed by relevant external experts |
| **Legally reviewed** | Reviewed by specialist legal counsel |
| **Adopted** | Formally adopted by a competent body |
| **Operational** | Implemented and tested in practice |

Each document should identify its current status and version.

---

## Why Version Control Matters

A university that understands itself as a learning institution should be able to see how its own architecture changes.

Version control makes institutional reasoning visible. It allows assumptions to be challenged, decisions to be traced, unresolved questions to remain explicit, and improvements to accumulate without erasing their history.

The repository is therefore not simply a publication platform. It is part of the governance design itself.

---

## Contributing

The OUG is being developed as an open institutional architecture.

Constructive critique is welcome, particularly from:

- learners and student representatives;
- universities and academic staff;
- governance and quality-assurance practitioners;
- accreditation and legal experts;
- ministries and public-sector institutions;
- lifelong-learning and recognition specialists;
- digital-learning and interoperability communities.

Please use [Issues](../../issues) to raise questions, identify contradictions, propose improvements, or document risks.

Substantive changes should be linked to the relevant principle, pattern, architectural decision, or requirement wherever possible.

---

## The Standard Against Which the OUG Must Be Judged

The OUG should be judged by whether the institution remains accountable to learners when resources are scarce, leadership changes, political attention moves elsewhere, and the founding generation is gone.

That is the purpose of the architecture documented here.

---

**Open University of Germany**
*A prospective, presently fictive public university designed from first principles.*

*Last updated: 2026-07-27 · index.md v0.2*
