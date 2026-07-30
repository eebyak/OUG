---
layout: page
title: "Digital Infrastructure"
---

[← Back to main index](../index.md)

# Digital Infrastructure

This is the OUG's eighth domain — added because the documents that justify it now exist. The repository's own [known-gaps register](../known-gaps.md) had flagged "Institutional Digital and Data Architecture" as a cross-cutting concern that "may eventually justify a separate Operations and Implementation domain, but such a domain should only be created once the relevant documents exist." Four documents, found together, are exactly that occasion.

## What This Domain Answers

Every other domain in this repository assumes a working digital platform sits underneath it: the [Modulhandbuch](../curriculum/modulhandbuch.md) assumes machine-readable module data exists somewhere; the [Quality Assurance Framework](../quality/quality-assurance-academic-governance.md) assumes learning analytics exist to audit; the [Five-Year Finance Plan](../strategy/five-year-finance-plan.md) budgets for a 23-tool technology stack and repeatedly cites "the European HEI Digital Alliance Framework (Documents 1–6)" as its technical foundation — without that framework being present in the repository. This domain is that framework.

It answers four questions in sequence: *why* should European higher education build sovereign digital infrastructure at all (the Manifesto); *what* architecture translates that commitment into decisions (the Architecture Reference Model); *what*, specifically, must each functional part of the platform do (the Functional Domain Specifications); and *how does an institution know* whether it has actually achieved what it committed to (the Evaluation Framework).

## What's Here

- **[European HEI Digital Alliance Manifesto](manifesto.md)** *(Document 1)* — the declaration: digital infrastructure and AI as public goods, European sovereignty as a constitutional rather than commercial matter, and seventeen binding platform principles covering procurement, sovereignty, AI governance, student data rights, and cooperation over competition.
- **[Architecture Reference Model](architecture-reference-model.md)** *(Document 2)* — six binding architecture principles (identity first, API-first, standards over products, one data master per domain, exit capability by design, security and privacy as structural), the three-zone sovereign deployment model (Sovereign Core, European Platform Cloud, Federation & Partner Zone), and the five-layer platform architecture with explicit data ownership at every layer — including the exact Matrix/Element messaging component you mentioned, listed as the recommended Layer 5 tool.
- **[Functional Domain Specifications](functional-domain-specifications.md)** *(Document 3)* — five detailed operational specifications: Learning Systems, Credentialing & Student Records, Learning Analytics, Backend & Stakeholder Data, and Administration Systems & AI — each with numbered functional requirements (LMS-01 through ADM-10), explicit cross-domain boundary rules, and a 25-criterion, 50-point evaluation scorecard.
- **[HEI IT Architecture Evaluation Framework](hei-evaluation-framework.md)** *(Document 4)* — the complete self-assessment instrument: 37 binary compliance gates and 47 graduated maturity criteria (0–5 scale) across 9 sections, a 235-point scoring system with six interpretation bands (Not Compliant through Leading), section weighting with alliance-level compliance gates, and an improvement plan template.

**All four documents of the framework are now converted.** ✅ See the note below on what that unblocks.
**A working [maturity scorecard](maturity-scorecard-newstudy.md)** — structured directly against Document 4, partially pre-filled from real evidence found on the live platform's own privacy and accessibility pages — is also available for hand completion. See [known-gaps.md](known-gaps.md) for what it found and what's still open.

See [conversion-notes.md](conversion-notes.md) for progress and [known-gaps.md](known-gaps.md) for what remains open in this domain.

## The Live Implementation

This isn't a purely theoretical framework. The **[New Study Module Catalogue](https://newstudy.campuscircle.de/)** — already linked from the [Curriculum domain](../curriculum/index.md) — is a working, deployed instance of parts of this architecture, not a mockup: it exposes module data through OOAPI, supports course sign-in and personal skill-profile development, and connects to Matrix/Element-based rooms for video calls and collaborative whiteboarding — open-source, self-hostable tools consistent with the sovereignty principles set out in the Manifesto and named explicitly, three separate times across Documents 2 and 3, as the framework's own recommended tooling.

That means the OUG's digital-infrastructure maturity is genuinely partial rather than purely aspirational: real components exist at a real maturity level. **The instrument to score that maturity precisely now exists in full** — Document 4's 37 compliance gates and 47 graduated criteria (0–5 scale, 235 points total across 9 sections). The honest next step is applying it directly to the live platform, the same way the [Design Signature Founding](../governance/design-signature-founding.md) scores the OUG's governance against the [42-pattern catalogue](../design-patterns.md) — cell by cell, with evidence, rather than a general maturity assertion. This is flagged as the next piece of work in [known-gaps.md](known-gaps.md).

## Cross-References Worth Knowing

- **The "Documents 1–6" citation may overstate what exists.** The Manifesto's own closing section names only three companion documents (2, 3, 4) — not six. See [conversion-notes.md](conversion-notes.md) for the full note; the [Strategy & Finance known-gaps register](../strategy/known-gaps.md) has been updated accordingly rather than left claiming two further documents are still missing.
- **This domain's documents are the technical foundation cited by, but never previously present for:** the [Five-Year Finance Plan's](../strategy/five-year-finance-plan.md) BMBF grant strategy (§6.1, "Digitale Transformation der Hochschulen"), its IT infrastructure cost breakdown (Part IV), and the [OUG Report 2025–26's](../communications/annual-report-2025-26.md) DIGITAL STUDY initiative.

---

*This page is a snapshot, not a source of truth — the [main index](../index.md) is the canonical list of what this domain is meant to eventually contain.*
