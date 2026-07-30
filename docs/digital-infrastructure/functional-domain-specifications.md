---
layout: page
title: "Functional Domain Specifications"
---


*Five Domain Specifications for the European HEI Digital Alliance Platform: Learning Systems · Credentialing & Student Records · Learning Analytics · Backend & Stakeholder Data · Administration Systems & AI*

*Document 3 of the European HEI Digital Alliance Framework · Version 1.0 · May 2026*
*Companion to [Document 2: Architecture Reference Model](architecture-reference-model.md)*

> **Source:** migrated from `D3_Functional_Domain_Specifications.docx`
> **Status:** *(to be set — see [Document Status](../index.md#document-status))*

## Introduction: How to Use This Document

This document provides the five Functional Domain Specifications that translate the Architecture Reference Model (Document 2) into detailed operational requirements for each major domain of the European HEI Digital Alliance platform. Where Document 2 defines the architectural framework — zones, layers, principles and integration contracts — this document defines what each domain must do, what data it owns, what it must expose, and what it must never do.

Each domain specification follows the same structure: a domain card summarising the key architectural facts; a scope definition establishing precisely what is in and out of the domain; detailed functional requirements with rationale and standards references; data governance requirements; API and integration requirements; user experience and adoption requirements; AI and automation requirements where applicable; vendor lock-in risk assessment; and evaluation criteria for use with the Evaluation Framework ([Document 4](hei-evaluation-framework.md)).

The five domains are not fully independent — they have defined dependencies and boundary rules between them. These cross-domain boundaries are the most architecturally important section of each specification. They determine where data authority lies, which system makes which decisions, and how events flow from one domain to another. Disputes about cross-domain ownership are resolved by reference to the master data domain table in Document 2, Section 7.3.

| Domain | Name | Primary Responsibility |
|---|---|---|
| **3a** | Learning Systems | Delivering the learning experience: LMS, assessment tools, learning content management, and LTI-based third-party tool integration. Does not own grades or credentials. |
| **3b** | Credentialing & Student Records | Certifying, sealing and archiving academic achievement. The only domain authorised to issue signed credentials. Owns the immutable student record. |
| **3c** | Learning Analytics | Collecting, pseudonymising, analysing and reporting on learning behaviour data. Serves the learner first, the institution second. |
| **3d** | Backend & Stakeholder Data | Governing the authoritative institutional data: identity, HR, finance, research. The high-protection layer. Feeds all other domains; never receives data back as master authority. |
| **3e** | Administration Systems & AI | Managing institutional processes: committees, decisions, workflows, reporting, archive. The primary domain for AI augmentation of administrative work. |

---

## Domain 3a: Learning Systems

**Architecture Layer:** Layer 5 (Experience) for delivery; Layer 3 (Process) for academic process events
**Sovereign Zone:** Zone B (European sovereign cloud) for LMS and delivery infrastructure
**Data Master Authority:** Assessment activity scores (pre-certification only). Does NOT own grades, credentials or identity.
**Exposes via API:** Learning events (xAPI/Caliper to Layer 4), LTI context and grade passback, content metadata (LOM), course roster (Names and Roles Provisioning)
**Mandatory Standards:** LTI Advantage (1EdTech), SCORM 2004 / xAPI for content, IMS QTI for assessment, WCAG 2.1 AA
**Recommended Components:** ILIAS, OpenOlat, or Moodle (self-hosted on European sovereign infrastructure)

### 3a.1 Scope

The Learning Systems domain covers all technology directly involved in the delivery of learning experiences: the Learning Management System (LMS), assessment tools, learning content repositories, virtual classroom environments, and third-party specialist tools integrated through LTI. It covers the student-facing experience of organised academic learning.

This domain does NOT cover: the formal certification of academic achievement (Domain 3b); the analysis of learning behaviour data (Domain 3c); the management of student enrolment or degree audit (Layer 3 Process of Document 2); or the identity and authentication infrastructure (Domain 3d). These boundaries are not arbitrary — they reflect the principle that no single domain controls both the learning process and its certified outcome.

### 3a.2 The LMS as a Delivery Platform, Not a System of Record

The most important scoping decision in this domain is that the LMS is a delivery platform, not a system of record. This distinction has direct architectural consequences:

- The LMS does not own the student's identity. It receives identity assertions from Layer 1 (Domain 3d) via OIDC/SAML. If a student's enrolment status changes, the LMS reflects this because Layer 1 pushes the update — not because the LMS has its own enrolment logic.
- The LMS does not issue grades. It records assessment activity scores as operational data during the learning process. When a score is formally awarded as a grade by academic authority, that event passes to Domain 3b (Credentialing) via the API gateway for certification. The LMS score is an input to that process, not the certified outcome.
- The LMS does not own learning analytics. It generates learning event streams (xAPI) that flow to Domain 3c (Learning Analytics) via the API gateway. The LMS never analyses its own event data in ways that affect student outcomes — that analysis happens in Domain 3c under appropriate privacy controls.
- The LMS does not manage study programmes. Programme structure, module sequences, ECTS values and learning outcomes are maintained in the campus management system (Layer 3 Process). The LMS receives this structure as configuration; it does not define it.

### 3a.3 Functional Requirements

| ID | Requirement | Rationale | Standard / Reference |
|---|---|---|---|
| **LMS-01** | The LMS must authenticate all users via the institution's OIDC provider (Layer 1). No local user accounts for students or staff. | Ensures JML model works: when a student's enrolment ends, access ends automatically without manual LMS administration. | OpenID Connect Core 1.0; SCIM 2.0 for group provisioning |
| **LMS-02** | The LMS must support LTI Advantage (1EdTech LTI 1.3) including Assignment and Grades Service, Names and Roles Provisioning Service, and Deep Linking. | Enables plug-and-play tool integration without point-to-point connections. Any LTI Advantage-certified tool can connect to any compliant LMS. | 1EdTech LTI Advantage specification |
| **LMS-03** | All assessment activity scores must be transmitted to Domain 3b via the API gateway when formally awarded by academic authority. The LMS must not be the final authority on what constitutes a grade. | Enforces the boundary between learning process (3a) and certified achievement (3b). Prevents grades existing only in the LMS. | Internal API contract: LMS → API Gateway → Credentialing service |
| **LMS-04** | The LMS must emit xAPI statements for all significant learning events (content access, assessment attempt, assessment completion, forum post, video view) to the analytics landing service via the API gateway. | Enables Domain 3c to build a complete picture of learning activity without the LMS performing analytics itself. | IEEE xAPI (Experience API) 9274.1 |
| **LMS-05** | The LMS must provide a content repository that stores learning materials in open formats (SCORM 2004, xAPI/Tin Can packages, HTML5, PDF) with no proprietary lock-in for content storage. | Ensures learning content is portable when the LMS is replaced. Content must be exportable without vendor assistance. | SCORM 2004; xAPI content packages; IMS Common Cartridge |
| **LMS-06** | All user-facing interfaces must meet WCAG 2.1 Level AA accessibility requirements. Accessibility compliance must be documented in the product's VPAT (Voluntary Product Accessibility Template). | Legal requirement under EU Web Accessibility Directive (2016/2102/EU). Ethical requirement for inclusive education. | WCAG 2.1 AA; EU Web Accessibility Directive |
| **LMS-07** | The LMS must support IMS QTI 2.1 for assessment item import and export. Assessment items must be exportable in QTI format without vendor assistance. | Prevents assessment content lock-in. Ensures institutional investment in assessment design is portable. | IMS QTI 2.1; IMS QTI 3.0 where available |
| **LMS-08** | The LMS must provide a bulk data export in open format (JSON or CSV with documented schema) covering all courses, enrolments, submissions and scores. This export must be executable within 5 business days without vendor assistance. | Exit capability requirement from Architecture Principle 5. | OpenAPI export endpoint; documented data schema |
| **LMS-09** | The LMS must not share student behaviour data with the LMS vendor's analytics products, recommendation engines or AI services without explicit DPIA approval and student consent. | GDPR data minimisation and purpose limitation. Prevents extraction of student data to non-European analytics infrastructure. | GDPR Art. 5(1)(b)(c); DPIA required per Art. 35 |
| **LMS-10** | The LMS must operate on European sovereign cloud infrastructure or on institutional on-premises infrastructure. Hosting by a non-European cloud provider under non-European legal jurisdiction is not permitted. | Digital sovereignty requirement. Moodle hosted on AWS US-East does not satisfy this requirement even though Moodle itself is open-source. | Architecture Principle 5; Manifesto Principle II.5 |

### 3a.4 Third-Party Tool Integration via LTI

The LTI Advantage standard is the mechanism through which the Learning Systems domain achieves genuine plug-and-play modularity. The following requirements govern all third-party tool integrations:

**Tool approval process.** Every third-party tool must be approved through a defined process that includes: DPIA assessment; verification of WCAG 2.1 AA compliance; confirmation of LTI Advantage certification; data processing agreement with the tool provider; and confirmation that data generated by students in the tool does not leave European jurisdiction without explicit consent.

**Tool catalogue.** All approved tools are listed in an institutional tool catalogue accessible to all academic staff. The catalogue records: the tool's purpose, its LTI certification status, its data processing agreement status, its DPIA reference, and the date of last review.

**Tool retirement.** When a tool is removed from the catalogue, all LTI connections are deactivated and affected course content owners are notified with a minimum 90-day notice period. Student data held by the tool is exported and archived before deactivation.

**Shadow tool policy.** Academic staff may not connect tools that are not in the approved catalogue to their courses. The LMS must technically enforce this by requiring administrator approval for LTI tool registration. Shadow tools discovered in use trigger the approval process, not immediate removal — but they must complete the approval process within 60 days or be disconnected.

### 3a.5 User Experience and Adoption

User experience is a first-class requirement for this domain. An LMS that is technically compliant but practically abandoned by students and staff has failed its purpose. The following metrics are required:

- Monthly active user rate: at least 85% of enrolled students must access the LMS at least once per month during teaching periods
- Staff course creation rate: at least 90% of taught courses must have an active LMS presence with materials and activities
- Mobile usability: the LMS must be fully functional on mobile browsers without a native app requirement
- Time-to-first-use: a new student must be able to access their first course within 24 hours of enrolment confirmation
- Support ticket rate: LMS-related support tickets must not exceed 5% of the enrolled student population per teaching period

Where metrics fall below these thresholds persistently (two consecutive terms), the institution conducts a user research exercise to identify barriers and implements service improvements. Persistent failure (four consecutive terms) triggers an architecture review to assess whether the selected LMS is fit for purpose.

### 3a.6 AI in Learning Systems

AI tools that operate within the Learning Systems domain — AI tutoring assistants, automated feedback generators, intelligent content recommendation, AI-assisted assessment design — must satisfy the following requirements in addition to the general AI governance requirements from the Manifesto:

**Disclosure to students.** Students must be informed, at the point of each AI interaction, that they are interacting with an AI system. The nature of the AI (tutoring assistant, feedback generator, etc.) must be clear. There must be a pathway to human support for any AI-mediated learning interaction.

**No AI-generated grades.** AI systems must not generate final grades or summative assessment outcomes. They may generate formative feedback, suggested scores for instructor review, and practice assessment results. All summative grading remains a human academic decision.

**European AI preference.** Where AI tutoring or feedback tools exist in the European open-source ecosystem with equivalent capability, they are preferred. Proprietary non-European AI systems that process student interaction data require DPIA approval and must demonstrate GDPR compliance in their data processing.

**AI literacy integration.** Courses using AI tools must include explicit instruction on how those tools work, their limitations, and how to use them critically. AI literacy is not an add-on — it is part of the pedagogical design.

---

## Domain 3b: Credentialing and Student Records

**Architecture Layer:** Layer 2 (Credentialing and Student Records)
**Sovereign Zone:** Zone A (Sovereign Core) — all data in this domain is Zone A by definition
**Data Master Authority:** Certified academic credentials (grades, qualifications, micro-credentials). The institutional archive. No other domain holds authoritative certified achievement data.
**Exposes via API:** Credential verification endpoints (cryptographic, no live DB required), ELM-format credentials (to student / Europass / wallet), EMREX/ELMO transcripts (to partner institutions)
**Mandatory Standards:** ELM v3 / EDCI, EMREX/ELMO, Open Badges 3.0, eIDAS qualified electronic signatures, W3C Verifiable Credentials
**Recommended Components:** Europass EDCI infrastructure, EMREX Node, Open Badges 3.0-compliant issuer, institutional PKI (from Layer 1)

### 3b.1 The Central Principle: Learner Ownership

The defining architectural principle of this domain is that certified academic achievements belong to the learner. The institution is the witness and certifier of the achievement — it applies its seal to make the credential trustworthy — but the student holds the credential, controls where it is presented, and cannot have it altered or withheld once issued, except through a formally governed revocation and reissuance process.

This principle is not merely philosophical. It has direct technical consequences: credentials must be cryptographically sealed at issuance; the verification mechanism must not require a live connection to the issuing institution; the student must be able to export their credentials at any time without cost or institutional permission; and the institutional archive must be immutable — additions only, no modifications.

### 3b.2 Scope

This domain covers: the formal certification of all levels of academic achievement (qualifications, modules, micro-credentials, significant assessment events); the long-term immutable archive of student academic records; the issuance of machine-readable, cryptographically signed credentials in European standard formats; the electronic exchange of transcripts with partner institutions; and the management of the credential lifecycle (issuance, revocation, reissuance).

This domain does NOT cover: the learning process that produces the achievement (Domain 3a); the decision about what grade to award (an academic governance function in the Process layer); the identity management of the student (Domain 3d); or the analytics of learning patterns (Domain 3c). The domain is deliberately narrow: it does one thing — certify and preserve achievement — and it does it at the highest standard of integrity.

### 3b.3 Functional Requirements

| ID | Requirement | Rationale | Standard / Reference |
|---|---|---|---|
| **CRED-01** | All credentials issued by this domain must be formatted in ELM v3 (European Learning Model) and signed with a qualified electronic signature from the institution's PKI. | European interoperability standard. Enables verification by any European institution or employer without contacting the issuing institution. | ELM v3; European Digital Credentials Infrastructure (EDCI); eIDAS qualified electronic signature |
| **CRED-02** | Every issued credential must have a unique, persistent, dereferenceable identifier. The identifier must remain valid and verifiable for a minimum of 75 years from date of issuance. | Student credentials must outlast the institution's current technology landscape. A credential issued in 2026 must be verifiable in 2100. | W3C Verifiable Credentials Data Model; ELM persistent identifier requirements |
| **CRED-03** | Credential verification must be possible without a live connection to the issuing institution's systems. Cryptographic verification using the institution's published public key is the required mechanism. | An institution that goes offline, merges or changes its systems must not invalidate credentials already issued. Independence from live systems is essential for long-term trust. | PKI; qualified electronic signatures; offline verification |
| **CRED-04** | The institutional archive must be append-only and immutable. No credential record, once written, may be modified. Corrections are handled exclusively through formal revocation of the incorrect credential and issuance of a corrected one. | Data integrity of academic records is a legal and ethical requirement. Immutability prevents institutional abuse and protects students from having records altered without their knowledge. | ISO 30300 Records Management; applicable national archive legislation |
| **CRED-05** | Students must be able to export all their credentials at any time in ELM format, as a Europass Digital CV addition, and as a European Digital Identity Wallet-compatible package. Export must be available within 24 hours of request at no cost to the student. | Learner ownership principle. The student's credentials belong to the student. | ELM v3; Europass API; eIDAS 2 Wallet specification |
| **CRED-06** | The domain must implement an EMREX Node and participate in the EMREX network, enabling electronic transcript exchange with partner institutions in all EMREX-participating countries. | Enables credit recognition for incoming exchange students and reduces administrative burden of manual transcript processing. | EMREX/ELMO specification; EMREX Network participation |
| **CRED-07** | Micro-credentials must be issued conforming to the EU Council Recommendation on micro-credentials (2022), including: learning outcomes, volume indicator (notional hours), quality assurance reference, and ESCO-mapped competences. | Enables micro-credentials to be recognised across European institutions and by employers without requiring contact with the issuing institution. | EU Council Recommendation on micro-credentials (2022); ESCO; ELM v3 |
| **CRED-08** | All credential issuance events must be logged in the SIEM (Zone A) with: the credential identifier, the student pseudonym, the issuing academic authority, the timestamp, and the signature verification result. | Audit trail for compliance and for detecting fraudulent credential issuance attempts. | ISO/IEC 27001; GDPR Art. 30 (records of processing activities) |
| **CRED-09** | The revocation process must: notify the student immediately on revocation; record the reason for revocation in the archive; publish the revocation in the credential's revocation list; and be documented in an institutional revocation policy approved by academic governance. | Students have the right to know if their credential has been revoked and why. Revocation policy prevents arbitrary use of revocation as a disciplinary tool. | ELM revocation specification; GDPR Art. 13/14 (information rights) |
| **CRED-10** | ESCO competence mappings must be included in all module-level and micro-credential issuances. Mappings must be maintained by academic staff, validated through the quality assurance process, and updated when ESCO taxonomy is revised. | Enables employer-facing and cross-institution interpretability. ESCO mappings make the credential meaningful beyond the issuing institution's internal vocabulary. | ESCO v1.1+; ELM learning outcome specification |

### 3b.4 The Credential Lifecycle

| Stage | Trigger | Actions | Student Notification |
|---|---|---|---|
| **Trigger** | Academic authority formally awards grade or qualification via campus management system | Assessment outcome transmitted to credentialing service via API gateway | Not applicable (internal process) |
| **Issuance** | Credentialing service receives trigger with student identity, assessment metadata and outcome | Format ELM credential; apply PKI signature; write to immutable archive; assign persistent identifier | Credential available in student portal and for export within 24 hours |
| **Delivery** | Student requests export to Europass, Wallet or direct download | Credential transmitted via Europass API or wallet-compatible package; delivery logged | Confirmation of delivery; instructions for sharing with third parties |
| **Verification** | Third party requests verification of credential | Cryptographic verification using institution's published public key; no live DB lookup required | Not required unless revocation is discovered |
| **Revocation** | Error discovered in issued credential; student successfully appeals; fraud detected | Revocation record written to archive; revocation list updated; corrected credential issued if applicable | Immediate notification with reason; information on reissuance timeline |
| **Reissuance** | Follows revocation where error was institutional | New credential issued with corrected data; linked to revocation record of original | Notification of reissuance; both original revocation and new credential accessible in student portal |

### 3b.5 Long-Term Archive Requirements

The student academic record is among the most long-lived institutional data assets. Requirements specific to long-term preservation:

**Retention period.** Academic records (grades, qualifications, transcripts) must be retained for a minimum of 75 years from the date of the most recent award. This period covers the working lifetime of the student plus a reasonable period for posthumous verification.

**Format migration.** The archive must have a documented format migration policy: when the ELM standard is revised, existing credentials must be migrated to the new format and re-signed, with the original signed credential also preserved. The migration must be logged and auditable.

**Disaster recovery.** The archive must be replicated to a geographically separate location with a recovery point objective (RPO) of no more than 4 hours and a recovery time objective (RTO) of no more than 24 hours.

**Independence from operational systems.** The archive must be accessible independently of the campus management system, the LMS and any other operational system. Archive access must be possible even if all other institutional systems are offline.

---

## Domain 3c: Learning Analytics

**Architecture Layer:** Layer 4 (Integration and Data) — analytics pipeline sits in the data layer, not the experience layer
**Sovereign Zone:** Stage 1 (landing): Zone A or Zone B with strict controls. Stage 2 (curated): Zone B. Stage 3 (individual support): Zone A-governed, Zone B-operated.
**Data Master Authority:** Pseudonymised learning event data (Stage 1 and 3). Anonymised cohort analytics (Stage 2). Does NOT own identity or certified credentials.
**Exposes via API:** Cohort analytics reports (to institutional BI), individual learning support flags (to personal tutors via API, scoped per student), student's own data (to student portal via API)
**Mandatory Standards:** IEEE xAPI 9274.1, IMS Caliper Analytics, WCAG 2.1 AA for student-facing dashboards, GDPR pseudonymisation requirements
**Recommended Components:** xAPI-compliant landing service, Exasol or DuckDB (analytics engine), Grafana (dashboards), custom early-warning service

### 3c.1 The Five Privacy Principles

Before any functional requirements, this domain is governed by five privacy principles that are architectural constraints, not policy aspirations. These principles determine the structure of the three-stage pipeline and the access controls on each stage.

> **Privacy Principles for Learning Analytics**
>
> **Principle 1 — Data minimisation at collection.** Collect only learning events that are necessary for the defined analytical purposes. Every event type collected must have a documented analytical use case. Event types without documented use cases are not collected, regardless of technical availability.
>
> **Principle 2 — Pseudonymisation at ingestion.** Real student identities are replaced with persistent pseudonyms at the point of data ingestion into the analytics pipeline. The pseudonym-to-identity mapping is held only in Zone A under strict access controls. Analytics processing never sees real identities.
>
> **Principle 3 — Student data rights are operationally real.** Students have the right to access their own learning data, understand what inferences have been drawn, and challenge those inferences. These rights are implemented as working system features, not aspirational policy statements.
>
> **Principle 4 — Analytics serves the learner first.** The primary purpose of this domain is improving student outcomes. Institutional reporting is a legitimate secondary purpose. Surveillance, commercial exploitation and staff performance management are prohibited purposes.
>
> **Principle 5 — Inference transparency.** When the analytics system generates a flag, recommendation or alert that affects a student's experience (early-warning flag to their tutor, recommended learning pathway, at-risk notification), the basis for that inference must be documentable and explainable to the student on request.

### 3c.2 The Three-Stage Pipeline

The three-stage pipeline is the core architectural pattern of this domain. The stages enforce privacy controls structurally — the architecture makes privacy violations technically difficult, not just policy-prohibited.

**Stage 1: Landing.** Raw xAPI and IMS Caliper event streams arrive from Domain 3a (LMS and learning tools) via the API gateway. At ingestion, each event is pseudonymised: the student's real identifier is replaced with a persistent pseudonym, and the mapping is stored separately in Zone A. The pseudonymised event is written to the landing store. The real identifier is not retained in the analytics pipeline at any subsequent stage. The landing store retains events for a configurable window (default 90 days). After this window, events are either promoted to Stage 2 (in aggregated form) or deleted. Individual-level raw events are never retained beyond the landing window. The landing store is accessible only to the automated ETL pipeline — no human access to this stage.

**Stage 2: Curated Cohort Analytics.** The ETL pipeline aggregates Stage 1 data into cohort-level analytical datasets in the curated data warehouse. Aggregation enforces a minimum cohort size (default n≥10) — data about groups smaller than this threshold is suppressed to prevent re-identification of individuals. Stage 2 data is linked to programme, module and cohort metadata (not to individual identities). It enables institutional questions: which programmes have high disengagement at which points? Which assessment designs correlate with poor outcomes? Which support interventions are most effective at cohort level? Stage 2 data is accessible to the analytics team, institutional research office and quality assurance staff, under data access agreements.

**Stage 3: Individual Learning Support.** Stage 3 operates on pseudonymised individual-level data for early-warning and learning support applications. Access to Stage 3 data requires explicit governance authorisation and is limited to personal tutors (scoped to their own students, with student consent), student support services (scoped to referred students), and the students themselves (full access to their own data via the self-service dashboard). Re-linking a pseudonym to a real identity — necessary when a tutor needs to act on an early-warning flag — requires a Zone A authorisation call that is audit-logged. The analytics system never makes this link automatically; it always requires a human action with a logged justification.

### 3c.3 Functional Requirements

| ID | Requirement | Rationale | Standard / Reference |
|---|---|---|---|
| **ANA-01** | All learning events must be collected in xAPI (IEEE 9274.1) or IMS Caliper format. Non-standard event formats from individual tools are acceptable only if the LTI connector transforms them to xAPI/Caliper before they enter the pipeline. | Semantic interoperability: events from different tools mean the same thing and can be combined in analysis. | IEEE xAPI 9274.1; IMS Caliper Analytics 1.2 |
| **ANA-02** | Pseudonymisation must be applied at ingestion, before any event is written to the landing store. The pseudonymisation function must be: deterministic (same student always gets the same pseudonym); irreversible without the mapping table; and the mapping table must be stored in Zone A with access restricted to the re-identification authorisation service. | Privacy by design. Ensures that even if the landing store is compromised, student identities cannot be determined from the data alone. | GDPR Art. 4(5) pseudonymisation; GDPR Recital 26 |
| **ANA-03** | Stage 2 aggregation must enforce a minimum cohort size of n≥10. Groups smaller than this threshold must be suppressed or aggregated with adjacent groups before any output is produced. | Re-identification risk: in a group of 3 students, even anonymised data is likely identifiable. The n≥10 threshold is a conservative but defensible standard. | GDPR data minimisation; k-anonymity principles |
| **ANA-04** | Every student must have access to a self-service data dashboard showing: all learning events collected about them (in plain language, not raw xAPI); the inferences and flags generated from their data; the purposes for which their data is used; and a mechanism to request corrections or contest automated recommendations. | GDPR Art. 15 (right of access); Art. 22 (rights related to automated decision-making); Manifesto Principle IV.12. | — |
| **ANA-05** | Early-warning flags visible to tutors must be accompanied by: the specific data patterns that triggered the flag; the confidence level of the model; the recommended action; and a clear statement that the flag is a support prompt, not a performance assessment. | Transparency of inference (Privacy Principle 5). Prevents early-warning flags from being used as disciplinary tools. | GDPR Art. 22; EU AI Act Article 13 (transparency) |
| **ANA-06** | No individual-level analytics output may be shared with Domain 3a vendors, LTI tool providers, or any external party without explicit DPIA approval and student consent. Cohort-level aggregated data may be shared for benchmarking under data sharing agreements that prohibit re-identification. | Data purpose limitation. The analytics infrastructure exists to serve the institution's educational mission, not to supply data to commercial analytics providers. | GDPR Art. 5(1)(b) purpose limitation |
| **ANA-07** | The early-warning model must be reviewed and validated annually by a panel that includes academic staff, student representatives and the Data Protection Officer. The model must be tested for demographic bias (differential performance across gender, ethnicity, disability and socioeconomic indicators). Biased models must be corrected before deployment. | Algorithmic fairness. Early-warning models trained on historical data can encode historical inequalities and systematically disadvantage already-marginalised groups. | EU AI Act (high-risk AI in education); GDPR Art. 22 |
| **ANA-08** | Students must have the right to opt out of Stage 3 individual learning support analytics. Opt-out must be simple, reversible, and must not affect the student's access to any other service. Opt-out does not prevent Stage 1 collection (operational) or Stage 2 cohort analytics (anonymised). | GDPR Art. 21 (right to object). Individual analytics is a more intrusive processing purpose than cohort analytics; opt-out must be available. | GDPR Art. 21; Manifesto Principle IV.12 |

### 3c.4 The Student Data Dashboard

The student data dashboard is the operational implementation of the right to understand and challenge (Manifesto Principle IV.12). Requirements:

- Available to all enrolled students via the student self-service portal (Domain 3a experience layer), authenticated via OIDC
- Shows all xAPI events collected in plain language (not raw technical format): "You accessed the Week 3 lecture video on 14 March at 14:32" not "Actor: [pseudonym], Verb: watched, Object: video/week3-lecture, Result: {duration: 847}"
- Shows any early-warning flags currently active, with plain-language explanation of what triggered them
- Shows the data retention schedule: when this data will be deleted from each stage
- Provides a one-click mechanism to request a correction (e.g. "This event was recorded in error — I did not access this resource") which generates a formal review request
- Provides a one-click opt-out mechanism for Stage 3 individual analytics
- Is available in all languages in which the institution delivers teaching

---

## Domain 3d: Backend and Stakeholder Data

**Architecture Layer:** Layer 1 (Identity and Trust) and Layer 4 (Integration and Data) — the authoritative data foundation
**Sovereign Zone:** Zone A exclusively. No authoritative data from this domain may reside in Zone B or Zone C.
**Data Master Authority:** Identity, HR, finance, research project data. All eight master data domains flow from or through this layer. This domain feeds all others; it never receives data back as a master authority.
**Exposes via API:** Identity assertions (SAML/OIDC), provisioning events (SCIM), financial data (to ERP), HR data (to IGA), research metadata (to research systems). All outputs via API gateway.
**Mandatory Standards:** SCIM 2.0, SAML 2.0, OIDC, ISO/IEC 27001, ISO/IEC 27701, GDPR Art. 30 processing records
**Recommended Components:** Evolveum midPoint (IGA), OpenXPKI (PKI), SAP S/4HANA or Unit4 (ERP), P&I LogaHR or Unit4 HCM (HR), OpenNebula or equivalent private cloud (Zone A infrastructure)

### 3d.1 The High-Protection Layer

This domain is the institutional data bedrock. It holds the most sensitive and most consequential data in the platform: the identity, employment, financial and research records of every person and organisational unit associated with the institution. Everything else in the platform depends on the integrity and availability of this layer.

The defining characteristic of this domain is that data flows outward to other domains — never inward as master authority. The IGA system provisions users to the LMS, the credentialing service and the collaboration platform. The finance system provides cost centre data to the analytics platform. The HR system provides employment records to the identity layer. No other domain tells this layer what the authoritative values of these data elements are.

This one-directional authority is what makes the architecture coherent. If the LMS could update identity records, or if the collaboration platform could change HR data, the master data principle would collapse into the fragmented, inconsistent data landscape that the architecture is designed to eliminate.

### 3d.2 Data Sub-Domains and Their Governance

Domain 3d contains five sub-domains, each with its own governance requirements, retention schedules and access controls:

| Sub-domain | System of Record | Sensitivity | Key Governance Requirements |
|---|---|---|---|
| Identity & Access | IGA system (midPoint) | High — affects access to all institutional systems | JML model enforced; MFA for all accounts; quarterly access recertification; privileged access management; SCIM provisioning to all downstream systems |
| HR & Employment | HR/Payroll system | Very High — employment contracts, salary, performance | Access restricted to HR staff and line managers (scoped); GDPR Art. 88 employment data requirements; retention per applicable labour law; no export to analytics domain in identified form |
| Finance & Procurement | ERP (SAP/Unit4) | High — budgets, invoices, procurement | Access controls by financial role and cost centre; audit trail on all transactions; financial data exposed to analytics only as anonymised aggregates at cost centre level |
| Student Administrative Records | Campus management system | High — enrolment status, programme data, examination status | Separate from certified credentials (Domain 3b); these are operational records. Retention per applicable education law; access by academic and admin staff; student has right of access |
| Research Project Data | Research management system | Variable — public outputs vs. restricted/classified research | Access controlled by project PI; special handling for dual-use research; data sharing agreements for collaborative projects; integration with European research infrastructures (ORCID, OpenAIRE) |

### 3d.3 Functional Requirements

| ID | Requirement | Rationale | Standard / Reference |
|---|---|---|---|
| **BACK-01** | All Zone A infrastructure must hold current ISO/IEC 27001 certification. The certification scope must include all systems in this domain. Certificates must be available for audit on request. | Legal and contractual requirement for operating infrastructure at this sensitivity level. Also a requirement for cyber insurance and many research funding bodies. | ISO/IEC 27001:2022 |
| **BACK-02** | Personal data processing in this domain must be documented in a Record of Processing Activities (RoPA) per GDPR Art. 30. The RoPA must be reviewed and updated at least annually. | GDPR legal requirement. The RoPA is the primary accountability document for data protection compliance. | GDPR Art. 30 |
| **BACK-03** | The IGA system must provision and deprovision user accounts to all downstream systems within defined SLAs: new joiner accounts within 4 business hours of HR/admissions trigger; leavers deprovisioned within 2 business hours of termination event. | Orphaned accounts are a primary security vulnerability in HEI environments. The JML SLA prevents orphaned accounts from persisting. | NIST SP 800-53 (Access Management); ISO/IEC 27001 A.9 |
| **BACK-04** | All HR, finance and identity data must be encrypted at rest using AES-256 or equivalent. Encryption keys must be managed in the institution's HSM (Hardware Security Module) or equivalent key management service in Zone A. | Encryption at rest protects data in the event of physical media theft or unauthorised system access. | ISO/IEC 27001 A.10; GDPR Art. 32 |
| **BACK-05** | No HR or finance system may be hosted outside Zone A (European sovereign infrastructure). Processing of HR and financial data in non-European cloud environments is prohibited without explicit DPA governance approval and a documented legal basis. | HR data (employment contracts, salary, performance) and financial data are among the most sensitive institutional data. Hosting outside European jurisdiction creates unacceptable legal exposure. | GDPR Art. 44–49 (international transfers); Architecture Principle 5 |
| **BACK-06** | The IGA system must maintain a complete audit log of all provisioning and deprovisioning events, all access reviews, all privilege elevations, and all policy changes. Audit logs must be retained for 7 years and must be tamper-evident. | Audit trail for security incident investigation, compliance demonstration, and access dispute resolution. | ISO/IEC 27001 A.12.4; GDPR accountability principle |
| **BACK-07** | Access to privileged system functions (IGA administration, database administration, key management, network configuration) must use a Privileged Access Management (PAM) system with: separate credentials from daily-use accounts; session recording; time-limited privilege elevation; and alerts on anomalous patterns. | Privileged account compromise is the primary attack vector in institutional data breaches. PAM significantly reduces the blast radius of credential compromise. | CIS Controls v8; ISO/IEC 27001 A.9.4 |
| **BACK-08** | All APIs exposed by this domain must enforce field-level access control: the requesting system receives only the specific fields it is authorised to see, not the full record. This is enforced at the API gateway, not by application-level filtering. | Principle of least privilege at the data level. An LMS that needs to know a student's name and email does not need to see their disability status or financial aid record. | GDPR data minimisation; OWASP API Security |

### 3d.4 The Vendor Lock-in Risk Assessment

Domain 3d presents the highest vendor lock-in risk in the entire platform, for three reasons: the data volumes are the largest; the migration complexity is the highest (HR and finance systems embed institutional process logic over years of customisation); and the cost of data loss is catastrophic. The following mitigations are required:

**Annual data export test.** The institution conducts an annual test of the bulk data export for all Domain 3d systems. The test must demonstrate that a complete, correct export of all data can be completed within 5 business days without vendor assistance. Test results are reported to the Architecture Review Board.

**Open format requirement.** All Domain 3d systems must store data in formats that can be read without the originating software: SQL databases with documented schemas, JSON/XML in published formats, or standards-compliant formats (HR-XML, UBL for finance). Proprietary binary formats are not permitted for primary data storage.

**Customisation register.** All customisations to Domain 3d systems (configuration changes, workflow modifications, data model extensions, integrations) must be documented in a customisation register. The register supports migration planning and reduces the institutional knowledge dependency on the originating vendor.

**Contract requirements.** Domain 3d vendor contracts must include: source code escrow for custom components; data portability clause with defined export formats and timelines; a right to migrate without punitive fees; and a transition assistance obligation of at least 12 months at current pricing after termination notice.

---

## Domain 3e: Administration Systems and AI-Augmented Processes

**Architecture Layer:** Layer 3 (Process and Academic Systems) — administrative process layer
**Sovereign Zone:** Zone B (European sovereign cloud) for workflow and collaboration; Zone A for archive and access-controlled decision records
**Data Master Authority:** Committee decision records, workflow state, process documentation, administrative archive. Does NOT own identity, credentials or HR data.
**Exposes via API:** Decision records (to archive and to governance reporting), process status (to institutional dashboard), anonymised process analytics (to BI layer), AI-generated summaries (for human review and approval)
**Mandatory Standards:** BPMN 2.0 for process modelling, CMIS for document management, OAIS/PREMIS for archiving, ISO 15489 records management
**Recommended Components:** Nextcloud (collaboration base), Camunda or Flowable (BPM), AI assistant (European sovereign model), MailStore or RODA (archive)

### 3e.1 The Opportunity This Domain Addresses

Administrative processes — committee governance, decision routing, reporting, archiving — represent one of the most significant and most consistently neglected opportunities in higher education digital transformation. While institutions have invested heavily in student-facing systems and research infrastructure, the internal processes of institutional governance have typically been left to run on email chains, shared drives, paper minutes, and tools with low adoption rates.

The consequences are practical and serious: decisions taken in committees cannot be efficiently traced to their implementation; discussion context is lost between meetings; access to historical decisions is slow and unreliable; compliance with internal regulations cannot be easily audited; and the institutional memory embedded in administrative processes is fragile, dependent on the continuity of individual staff members rather than on robust systems.

This domain addresses these consequences directly. It is also the primary domain for AI augmentation in the platform — and it is precisely the right place for AI, because the risks are lower (administrative process data vs. student personal data), the gains are immediate and visible, and the governance framework is well-defined.

### 3e.2 Core Functions

**Committee and Meeting Management.** The meeting management system handles the full lifecycle of committee governance: agenda preparation, background document distribution, discussion facilitation (synchronous or asynchronous), decision recording, vote capture, minutes generation, and approval workflow. This function replaces the combination of email, shared drives and word-processed minutes that currently manages most institutional committee governance.

The AI contribution to meeting management is in summarisation and structuring. AI tools can: generate a structured agenda from submitted items with appropriate categorisation; produce a draft summary of discussion points from a meeting record or transcript; suggest action points and responsible parties from the discussion; and generate a structured minutes draft for human review and approval. All AI outputs in this function are drafts — human approval is mandatory before any output is distributed or archived.

**Decision Workflow and Routing.** The decision workflow system manages the movement of decisions through the institution's governance structure: from initial proposal, through committee consideration, to approval by the appropriate authority, to implementation assignment, to completion tracking, to archive.

This function is currently one of the most fragmented in higher education institutions. Decisions are taken in one committee but their implementation is tracked (if at all) through separate systems or informal follow-up. The decision workflow system creates a single, transparent record of every governance decision from proposal to completion, with: the decision text; the supporting documents; the committee that took it; the votes (where applicable); the implementation authority; the implementation deadline; and the completion status.

AI contribution: routing suggestions (based on the content of a proposal, suggest which committee should consider it and what supporting information is required), deadline management (automated reminders and escalation when implementation deadlines approach), and pattern analysis (identifying decisions that consistently miss implementation deadlines or that are repeatedly revisited — signals of process problems that require governance attention).

**Reporting and Institutional Analytics.** The reporting function aggregates data from across the administration domain (and from anonymised outputs of other domains) to support institutional governance and quality assurance. This includes: statutory reporting to national and European bodies; accreditation evidence packages; board and senate reporting; and internal management information.

The AI contribution to reporting is in drafting: given a structured dataset and a reporting template, AI can produce a draft narrative that human staff review and edit. This is particularly valuable for accreditation reports, which require consistent structure across multiple sections and extensive cross-referencing of evidence. The draft-and-review model ensures AI accelerates human work without replacing human judgement about what the data means for the institution.

**Archive and Records Management.** The records management function governs the lifecycle of institutional documents from creation to final disposition: classification, retention schedule assignment, access rights management, transfer to long-term archive, and eventual disposal. This function is governed by applicable national archive law and, for institutions with EU funding, by EU grant management requirements.

Automatic classification is the primary AI contribution: AI can suggest the classification and retention schedule for a document based on its content, the process that generated it, and the governing policy. Human staff confirm or override the suggestion. Over time, confirmed classifications train an improving model. This significantly reduces the administrative burden of records management while maintaining human accountability for final classification decisions.

### 3e.3 Functional Requirements

| ID | Requirement | Rationale | Standard / Reference |
|---|---|---|---|
| **ADM-01** | All committee decisions must be recorded in a structured, searchable format in the decision workflow system. Free-text email decisions and decisions recorded only in word-processed minutes that are stored in shared drives are not acceptable as the primary record. | Enables audit, compliance checking, and institutional learning from governance history. Free-text email decisions are not auditable or searchable at scale. | ISO 15489 Records Management; applicable national governance regulations |
| **ADM-02** | Every decision record must include: the decision text; the supporting documents (linked by reference, not embedded); the committee and date; the vote outcome (where applicable); the implementation authority; the implementation deadline; and the archive classification. | Complete decision records enable compliance auditing, governance review, and institutional memory preservation. | ISO 15489; BPMN 2.0 for process documentation |
| **ADM-03** | The workflow system must enforce routing rules: proposals submitted to the wrong committee are flagged and redirected; decisions requiring approval at a higher governance level are automatically escalated; implementation deadlines trigger automated reminders at configurable intervals. | Reduces governance errors caused by informal routing. Ensures the right committee makes the right decisions. | BPMN 2.0 workflow specification |
| **ADM-04** | All AI-generated outputs in this domain (meeting summaries, draft minutes, routing suggestions, classification suggestions, report drafts) must be clearly labelled as AI-generated and must require explicit human approval before distribution or archiving. The identity of the approving human must be recorded in the audit log. | Human decision authority principle (Manifesto Principle III.7). AI augments administrative processes; it does not replace human governance authority. | EU AI Act; Manifesto Principle III.7 |
| **ADM-05** | AI tools used in this domain must operate on European sovereign infrastructure. Meeting content, decision records and institutional governance data must not be processed by AI services hosted outside European jurisdiction or by AI models that transmit institutional data to non-European training infrastructure. | Governance data is among the most sensitive institutional data — not because of personal data content (though some governance decisions do involve personal data) but because it reflects the institution's strategic decision-making. | Architecture Principle 5; GDPR Art. 44–49 |
| **ADM-06** | The records management system must implement a documented retention schedule for each document and decision type, aligned with applicable national archive law and EU grant management requirements. Retention schedules must be reviewed annually and updated when applicable law changes. | Legal compliance. Retaining documents beyond their retention period creates liability. Disposing of documents before their retention period creates compliance risk. | ISO 15489; applicable national archive law; EU grant regulations |
| **ADM-07** | Access to administrative records must be governed by the classification of the record and the role of the requesting person. Sensitive governance records (personnel decisions, disciplinary proceedings, strategic financial planning) must be accessible only to staff with documented need. Access to historical records must default to restricted; declassification must be a deliberate governance decision. | Institutional governance data includes personnel decisions, disciplinary proceedings and strategic information. Unrestricted access to such records creates serious legal and reputational risk. | GDPR Art. 5(1)(f) integrity and confidentiality; applicable national public records law |
| **ADM-08** | The administration domain must provide a governance health dashboard to institutional leadership: showing the number of open decisions awaiting implementation, overdue implementation deadlines, committee workload metrics, and decision cycle time trends. This dashboard must be automatically populated from the decision workflow system — not manually assembled from email and shared drive records. | Real-time governance intelligence. Leadership cannot improve what they cannot see. A governance dashboard makes institutional process health visible without requiring manual report assembly. | ISO 15489; good governance principles |
| **ADM-09** | All tools in this domain must have demonstrated adoption rates of at least 80% of target users within 12 months of deployment. Tools with adoption rates below 60% after 12 months are subject to mandatory user research and service redesign. Tools with adoption rates below 40% after 18 months are replaced. | UX and adoption are architectural requirements (Architecture Reference Model Section 8.1). A workflow tool unused by 60% of target users has not solved the governance problem — it has added a new system alongside the informal processes that continue. | Architecture Reference Model Section 8.1; Manifesto Principle I |
| **ADM-10** | The domain must support plug-and-play tool integration: any tool that satisfies the domain's API contracts and data governance requirements can be connected without architectural changes. Tool replacement must be possible with data export and import in documented open formats. | Prevents vendor lock-in at the administrative tools layer. Ensures the institution can respond to better tools becoming available without architectural rework. | Architecture Principle 5; Manifesto Principle I.3 |

### 3e.4 The AI Governance Framework for This Domain

AI augmentation in the administration domain is governed by a framework that is more permissive than AI in student-facing domains (because the data involved is primarily process data rather than personal student data) but still requires structured governance. The framework has three tiers:

| Tier | AI Function | Human Oversight Required | Examples |
|---|---|---|---|
| **Tier 1 — Assistive** | AI drafts, suggests, or summarises. Human approves or rejects before any action. | Full review and explicit approval before distribution or archiving. AI output labelled clearly. | Meeting summary drafts, agenda suggestions, report narrative drafts, document classification suggestions |
| **Tier 2 — Automated with Alert** | AI acts automatically but generates an alert for human review. Human can override within a defined window. | Human receives alert; can override within 48 hours. All automated actions logged. | Deadline reminder emails, routine routing of standard proposal types, retention schedule application to standard document types |
| **Tier 3 — Fully Automated** | AI acts automatically with no human review required. | Annual audit of automated action log; anomaly detection alerts. | Archiving of completed decision records per defined retention schedule, generation of routine compliance reports from structured data |

Tier 3 automation is limited to processes where: the inputs are fully structured (no free text); the rules are unambiguous (no judgement required); the outputs affect only administrative records (not people directly); and the action is reversible. Any process that involves personnel decisions, disciplinary proceedings, student-affecting decisions, or financial commitments above defined thresholds must remain at Tier 1 or Tier 2.

### 3e.5 The User Experience Imperative

This domain has historically been the site of the highest rates of tool failure in higher education digital transformation — not technical failure, but adoption failure. OpenProject, various SharePoint implementations, bespoke committee management systems — all have been deployed and subsequently abandoned in favour of email and shared drives, because the tools were more complex, less convenient or less responsive than the informal processes they were meant to replace.

The adoption requirements in ADM-09 are not aspirational targets. They are exit criteria: tools that fail to meet adoption thresholds within the defined timeframes are replaced. This is a governance commitment, not a service improvement suggestion. The reason is architectural: a workflow system that is bypassed does not improve institutional governance — it adds complexity without adding capability.

Practical implications for tool selection in this domain:

- **Mobile-first design is a requirement, not a preference.** Governance participants (academics, senior administrators) access tools from mobile devices as frequently as from desktops. A tool that requires desktop access will be abandoned by anyone who primarily works on a phone or tablet.
- **Notification integration is required.** The workflow system must send notifications through channels that users already monitor: email, messaging platform (Matrix/Element), and calendar. A system that requires users to log in to check status will not achieve adequate adoption.
- **Minimal friction for the most common actions.** The most common action in committee governance is reading and approving a recommendation. This action must be completable in under 30 seconds from the notification. Systems that require multiple navigation steps to complete simple approvals will be abandoned.
- **Offline capability for reading.** Governance documents must be readable offline (downloaded to device). Systems that require constant connectivity to display documents will be abandoned by users in variable connectivity environments.

---

## Cross-Domain Boundary Rules and Evaluation Criteria

### Cross-Domain Boundary Rules

The boundaries between domains are the most architecturally significant design decisions in this specification. The following rules govern data and authority flows between domains. Any proposed integration that would violate these rules requires an Architecture Review Board decision.

| From | To | Permitted? | Rule |
|---|---|---|---|
| 3a Learning | 3b Credentialing | **Permitted (one-way)** | 3a sends assessment outcome events to 3b via API gateway. 3b returns credential issuance confirmation. 3a never writes directly to the student record archive. |
| 3a Learning | 3c Analytics | **Permitted (one-way)** | 3a sends xAPI events to 3c landing stage. 3c never sends individual-level data back to 3a. Cohort insights may inform instructional design (as human-mediated decisions, not automated feedback loops). |
| 3a Learning | 3d Backend | **Permitted (read-only)** | 3a reads identity and enrolment data from 3d via API gateway. 3a never writes to 3d. |
| 3b Credentialing | 3a Learning | **Not Permitted** | 3b does not send data to 3a. Credential issuance is a terminal event — it does not feedback into the learning system. |
| 3b Credentialing | 3d Backend | **Permitted (read-only)** | 3b reads student identity from 3d at the moment of credential issuance. 3b writes only to its own archive. |
| 3c Analytics | 3a Learning | **Not Permitted (automated)** | Analytics outputs do not automatically modify learning content or course structure. Insights are delivered to human staff who make pedagogical decisions. No direct automated feedback loop. |
| 3c Analytics | 3d Backend | **Not Permitted** | 3c operates on pseudonymised data. It never reads from or writes to the authoritative identity records in 3d. |
| 3d Backend | All domains | **Permitted (one-way, authoritative)** | 3d is the source of identity, HR and finance data for all other domains. Data flows from 3d outward via the API gateway. No other domain writes to 3d as a master authority. |
| 3e Admin | 3b Credentialing | **Not Permitted** | Administrative decisions (e.g. committee decisions about degree awards) are passed to 3b via the campus management system (Layer 3 Process). 3e does not write directly to the credentialing service. |
| 3e Admin | 3d Backend | **Permitted (read, limited write)** | 3e reads organisational and role data from 3d. 3e may write process records (committee decisions, workflow states) to its own archive. HR data updates (e.g. a committee decision to appoint a person) flow via the HR system, not directly from 3e to 3d. |
| 3e Admin | 3c Analytics | **Permitted (anonymised output only)** | 3e may receive anonymised process analytics from 3c (e.g. how long decisions take). 3e does not receive individual-level student analytics. |

### Domain Evaluation Criteria

The following criteria are used in the Evaluation Framework ([Document 4](hei-evaluation-framework.md)) to assess each domain's implementation maturity. Each criterion is assessed at three levels: **Non-Compliant (0)**, **Partially Compliant (1)**, and **Fully Compliant (2)**. The sum across criteria gives the domain maturity score.

| Domain | Criterion | Fully Compliant Means | Max |
|---|---|---|---|
| **3a** | LMS Sovereignty | LMS operates on European sovereign infrastructure; no US cloud hosting; verified data residency. | 2 |
| **3a** | LTI Adoption | ≥80% of third-party tools integrated via LTI Advantage; LTI catalogue maintained; shadow tools < 10% of total tools in use. | 2 |
| **3a** | xAPI Emission | All learning events emitted to analytics landing service in xAPI format; event types documented; coverage > 90% of learning activity. | 2 |
| **3a** | AI Disclosure | All AI tools in learning environment disclose their AI nature to students; AI output labelled; human escalation pathway documented. | 2 |
| **3a** | Accessibility | WCAG 2.1 AA verified for LMS and all integrated tools; VPAT documents available; accessibility audit conducted in last 12 months. | 2 |
| **3a** | Adoption | Monthly active user rate ≥ 85%; support ticket rate < 5%; course LMS presence ≥ 90%. | 2 |
| **3b** | ELM Issuance | At least one credential type issued in ELM v3 format with qualified electronic signature; EDCI-verified. | 2 |
| **3b** | Learner Export | Students can export all credentials within 24 hours at no cost in ELM, Europass and wallet-compatible formats. | 2 |
| **3b** | EMREX Node | EMREX node operational; electronic transcript exchange tested with ≥ 2 partner institutions. | 2 |
| **3b** | Immutable Archive | Archive is append-only; retention period documented at 75 years; DR tested; independent of operational systems. | 2 |
| **3b** | Micro-credentials | Micro-credential issuance infrastructure in place; conforming to EU Council Recommendation; ESCO mappings present. | 2 |
| **3c** | Pseudonymisation | Pseudonymisation at ingestion verified; mapping table in Zone A; no real identities in analytics pipeline. | 2 |
| **3c** | Three-Stage Pipeline | All three stages operational; cohort size minimum enforced; access controls audited. | 2 |
| **3c** | Student Dashboard | Student data dashboard deployed; shows events in plain language; opt-out mechanism functional; correction request process tested. | 2 |
| **3c** | Bias Testing | Early-warning model tested for demographic bias in last 12 months; results documented; biases corrected. | 2 |
| **3d** | ISO 27001 | Current ISO/IEC 27001 certification covering all Zone A systems; last audit < 12 months. | 2 |
| **3d** | JML SLA | JML provisioning SLAs met: joiners < 4 hours; leavers < 2 hours; verified by quarterly audit. | 2 |
| **3d** | RoPA Current | Record of Processing Activities current; reviewed in last 12 months; covers all sub-domains. | 2 |
| **3d** | PAM Deployed | Privileged Access Management system operational; session recording active; quarterly recertification conducted. | 2 |
| **3d** | Export Test | Annual bulk data export test passed for all 3d sub-domains; results reported to Architecture Review Board. | 2 |
| **3e** | Decision System | ≥ 90% of committee decisions recorded in structured workflow system; < 10% in email/shared drive only. | 2 |
| **3e** | AI Tier Labels | All AI outputs labelled; Tier 1 approval workflow operational; human approval logged for all Tier 1 outputs. | 2 |
| **3e** | Adoption | Administration tool adoption ≥ 80% of target users at 12 months. | 2 |
| **3e** | Archive Compliance | Retention schedules documented and implemented; classification applied to ≥ 90% of records. | 2 |
| **3e** | Governance Dashboard | Governance health dashboard operational; auto-populated from workflow system; reviewed by leadership monthly. | 2 |

*(This table — 25 criteria across the five domains, 50 points maximum — is the fine-grained companion to the Annex B checklist in Document 2. Together with Document 4's fuller maturity ladder, this is the actual instrument for scoring the live New Study platform's maturity once all four documents are converted — see [known-gaps.md](known-gaps.md).)*

---

*Open University of Germany · Functional Domain Specifications · Document 3 of the Digital Alliance Framework · Version 1.0 · May 2026*
