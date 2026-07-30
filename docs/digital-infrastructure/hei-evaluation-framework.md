---
layout: page
title: "HEI IT Architecture Evaluation Framework"
---


*A Self-Assessment Instrument for European Higher Education Institutions: Compliance Gates · Maturity Ladders · Scoring · Improvement Roadmap*

*Document 4 of the European HEI Digital Alliance Framework · Version 1.0 · May 2026*
*Companion to Documents 1–3 of the European HEI Digital Alliance Framework*

> **Source:** migrated from `D4_HEI_Evaluation_Framework.docx`
> **Status:** *(to be set — see [Document Status](../index.md#document-status))*
> **This is the instrument for the maturity-scoring work flagged throughout this domain's conversion notes.** With all four documents now converted, the honest next step is applying this framework directly to the live [New Study Module Catalogue](https://newstudy.campuscircle.de/) — see [known-gaps.md](known-gaps.md).

## Introduction: Purpose and Structure

This Evaluation Framework provides a structured self-assessment instrument for European higher education institutions implementing the European HEI Digital Alliance Framework. It has three purposes: to allow individual institutions to assess their current state against the framework's requirements; to provide a common language for reporting to alliance bodies and accreditation organisations; and to generate a prioritised improvement roadmap that guides the institution's next phase of development.

The framework operates at two levels. The **compliance gate** level is binary: each check either passes or fails. Institutions that fail a compliance gate are not in compliance with the Alliance framework and must provide a documented remediation plan with a binding timeline. The **maturity ladder** level is graduated: each criterion is assessed on a 0–5 scale that describes the institution's current capability and defines what higher maturity looks like. The maturity ladder generates a score that can be tracked over time and compared across institutions.

The assessment is intended to be conducted annually, facilitated by the institution's Enterprise Architect and reviewed by the Architecture Review Board. First-time assessors should expect the assessment to take 2–3 days of focused work across a small team. Subsequent annual assessments should take 1 day. The outputs — compliance status, maturity scores, priority findings and improvement plan — are reported to the European Higher Education Digital Alliance coordination body as part of annual membership reporting.

> **How to Use This Framework**
>
> **Step 1 — Compliance Gates.** Work through each section's compliance gate table. For each check, record Pass or Fail. A single Fail requires a documented remediation plan before the maturity assessment for that section is meaningful.
>
> **Step 2 — Maturity Assessment.** For each criterion in the maturity tables, assess the institution at Level 0–5. Record the evidence that supports the assessment. Where evidence is absent, default to Level 0.
>
> **Step 3 — Scoring.** Complete the score summary table (Section 10). Calculate domain scores and the total architecture maturity score.
>
> **Step 4 — Priority Findings.** Identify the three to five criteria with the greatest gap between current score and target score. These become the priority improvement areas.
>
> **Step 5 — Improvement Plan.** Complete the improvement plan template (Section 11) for each priority finding, with owner, target level, actions and timeline.
>
> **Step 6 — Reporting.** Submit the completed assessment to the Alliance coordination body. Share the improvement plan with the Architecture Review Board for governance approval.

### Maturity Level Definitions

The following five-level maturity scale applies to all criteria in this framework. The level descriptions are generic; each criterion section provides criterion-specific descriptions for each level.

| Level | Label | Generic Description |
|---|---|---|
| **0** | **Absent** | No capability exists. The criterion is not addressed. No plan is in place. |
| **1** | **Initial** | Ad hoc activity exists but is undocumented, inconsistent, and dependent on individual knowledge rather than institutional process. |
| **2** | **Defined** | A documented approach exists and is applied consistently, but is not yet measured for effectiveness and may not cover all relevant scope. |
| **3** | **Managed** | The approach is measured, monitored, and produces predictable results. Coverage is comprehensive. Deviations are identified and corrected. |
| **4** | **Measured** | The approach is continuously measured against defined targets. Performance data drives improvement decisions. Benchmarking against peers occurs. |
| **5** | **Leading** | The institution is at or beyond European best practice. It actively contributes to advancing the field — through open-source contributions, standards work, published case studies, or cooperative service provision. |

---

## Section 1: Architecture Foundations

This section assesses whether the institution has established the governance structures, documentation practices and foundational decisions required before any domain-level implementation can be meaningful. An institution that has not established these foundations cannot reliably assess itself at domain level — the foundations are the precondition for everything else.

### 1.1 Compliance Gates — Architecture Foundations

| ID | Compliance Check | Pass Condition | Fail Consequence |
|---|---|---|---|
| **AF-G1** | An Enterprise Architect role exists with documented responsibilities for maintaining the Architecture Reference Model implementation. | Named individual; documented role; included in Architecture Review Board. | No named architect: all domain assessments are provisional. |
| **AF-G2** | An Architecture Review Board (or equivalent governance body) meets at least quarterly to review architecture decisions. | Meeting minutes for last 4 quarters available; defined membership; decision log maintained. | No governance body: architecture principle compliance cannot be verified. |
| **AF-G3** | An Architecture Decision Record (ADR) repository exists with at least 5 documented decisions from the last 12 months. | ADR repository accessible; decisions include rationale and alternatives considered. | No ADR repository: architecture decisions are undocumented and unreviewable. |
| **AF-G4** | A legacy system decommission register exists listing all retained legacy systems with target decommission dates. | Register accessible; all known legacy systems listed; each has a decommission plan or explicit keep decision. | No register: legacy system scope is unknown. |
| **AF-G5** | A DPIA (Data Protection Impact Assessment) has been completed for every system processing personal data of students or staff, reviewed in the last 24 months. | DPIA register complete; each DPIA has DPO sign-off; review dates within scope. | Missing DPIAs: GDPR non-compliance. Remediation required before maturity assessment. |

### 1.2 Maturity Assessment — Architecture Foundations

| Criterion | 0 Absent | 1 Initial | 2 Defined | 3 Managed | 4 Measured | 5 Leading | Doc |
|---|---|---|---|---|---|---|---|
| **Architecture principles documented and applied** | No principles documented | Principles exist informally; inconsistently applied | Six architecture principles documented (per Doc 2); applied to new decisions | Principles applied to all decisions; deviations formally documented as exceptions | Principles measured for compliance quarterly; exception rate tracked and declining | Principles published openly; contributed to European alliance standards work | D2 P1-6 |
| **API gateway operational** | No API gateway | API gateway deployed but only a minority of integrations use it | API gateway governing ≥50% of integrations; others have documented migration plan | ≥90% of integrations via gateway; zero new point-to-point without ARB approval | 100% of integrations via gateway; API traffic metrics reviewed monthly | API gateway configuration and patterns shared as open reference for alliance | D2 P2 |
| **Service catalogue completeness** | No service catalogue | Partial inventory exists for some domains | Complete inventory of all production systems with owner and zone assignment | Service catalogue actively maintained; updated within 30 days of any change | Service catalogue linked to CMDB; change events auto-update catalogue | Service catalogue model contributed to European alliance as reference standard | D2 |
| **Exit capability** | No exit plans for any system | Exit plan exists for 1–2 low-risk systems | Exit plans documented for all Tier 1 systems; bulk export tested for at least one | Annual export test conducted for all Tier 1 systems; migration paths documented | All exit tests passing; exit capability verified by external audit | Exit capability framework published; contributes to European procurement standards | D2 P5 |
| **Security baseline (DPIA + ISMS)** | No DPIA process; no ISMS | DPIAs exist for some systems; ISMS in planning | DPIA process documented and applied; ISMS implemented for Zone A | ISO/IEC 27001 certified for Zone A; DPIAs current for all personal data systems | ISO/IEC 27701 implemented; ISMS audit findings actioned within SLA | ISMS approach published; contributes to European HEI security community | D2 P6 |

---

## Section 2: Identity and Federation

Identity is the architectural foundation on which every other domain depends. This section assesses the completeness and maturity of the institution's identity governance, lifecycle management, federation participation and privileged access controls. No other section's maturity score is reliable without at least Level 2 in the core JML criterion.

### 2.1 Compliance Gates — Identity and Federation

| ID | Compliance Check | Pass Condition | Fail Consequence |
|---|---|---|---|
| **ID-G1** | An IGA (Identity Governance and Administration) system is in production, provisioning users from HR and admissions as authoritative sources. | IGA system named; HR and admissions feeds verified; provisioning tested. | No IGA: all downstream domain assessments are provisional. |
| **ID-G2** | The institution participates in its national higher education identity federation and in eduGAIN. | Listed in national federation metadata; eduGAIN participation confirmed at federation level. | Not in national federation or eduGAIN: European interoperability is blocked. |
| **ID-G3** | MFA is enforced for all administrative accounts (those with access to Zone A systems, API gateway configuration, IGA, PKI, or financial systems). | MFA enforcement policy documented; compliance verified by quarterly audit; exceptions register maintained. | MFA not enforced for admin accounts: critical security non-compliance. |
| **ID-G4** | A Joiner-Mover-Leaver process is documented and automated: new accounts provisioned within 4 business hours; leavers deprovisioned within 2 business hours. | SLA documented; last-quarter performance data available; breaches investigated and resolved. | No documented JML process: orphaned accounts risk is unmanaged. |
| **ID-G5** | An attribute release policy is documented, approved by the DPO, and enforced by the federation gateway. | Policy document available; DPO approval on record; technical enforcement verified. | No attribute release policy: GDPR data minimisation non-compliance in federation. |

### 2.2 Maturity Assessment — Identity and Federation

| Criterion | 0 Absent | 1 Initial | 2 Defined | 3 Managed | 4 Measured | 5 Leading | Doc |
|---|---|---|---|---|---|---|---|
| **IGA completeness** | No IGA system | IGA deployed but provisioning is manual or partial | IGA provisions all staff and students from authoritative sources; JML automated | IGA covers all user types (guests, alumni, research associates); recertification automated | IGA performance metrics tracked; provisioning SLAs met >99% of time; anomaly alerting active | IGA configuration published as open reference; midPoint community contributor | D2 §4, D3 3d |
| **Federation breadth** | Not in national federation | In national federation; eduGAIN participation in progress | Full eduGAIN participation; SP and IdP registered; basic attribute release policy active | Attribute release policy reviewed annually; SP catalogue maintained; guest federation operational | EWP, ESI, EMREX federation points all operational; eIDAS trust path in place | Federation configuration shared with alliance; contributes to GÉANT federation working group | D2 §4.3 |
| **JML lifecycle automation** | No automated JML | Joiners automated; leavers manual | Joiners and leavers automated; movers partially automated (some role changes manual) | Full JML automation including movers, guests, alumni; SLAs met and measured | JML SLA compliance >99.9%; anomaly detection on lifecycle events; quarterly access review | JML model published; contributes to European IGA best practice documentation | D2 §4.2 |
| **Privileged access management** | No PAM; shared admin credentials | PAM policy documented; partial implementation | PAM system deployed for Zone A; separate accounts; session recording active | PAM covers all privileged roles; time-limited elevation enforced; quarterly recertification | PAM anomaly alerting tuned; all privileged sessions reviewed quarterly; zero standing privilege for critical systems | PAM approach published; contributes to European HEI security standards | D2 §4.4, D3 3d |
| **MFA coverage** | MFA absent | MFA for some admin accounts only | MFA enforced for all Zone A admin accounts; phishing-resistant MFA (WebAuthn) in pilot | WebAuthn enforced for all admin accounts; risk-based MFA for high-risk user actions | MFA coverage metrics tracked; adaptive MFA operational; annual phishing simulation | MFA approach and tooling contributed to European alliance security community | D3 3d |

---

## Section 3: Learning Systems (Domain 3a)

This section assesses the sovereignty, interoperability, accessibility and adoption of the institution's learning technology stack. User experience and adoption are first-class criteria here — technical compliance without meaningful adoption is assessed at Level 1 regardless of the sophistication of the technical implementation.

### 3.1 Compliance Gates — Learning Systems

| ID | Compliance Check | Pass Condition | Fail Consequence |
|---|---|---|---|
| **LS-G1** | The LMS is hosted on European sovereign infrastructure or on institutional on-premises infrastructure. US commercial cloud hosting under US legal jurisdiction is not compliant. | Hosting contract confirms European data residency; sub-processor list reviewed by DPO. | Non-European hosting: sovereignty non-compliance. Migration plan required. |
| **LS-G2** | The LMS authenticates all users via the institution's OIDC provider (Layer 1). No local user accounts for students or staff exist in the LMS. | OIDC integration verified; local account audit confirms zero student/staff local accounts. | Local accounts exist: JML model is broken for LMS. |
| **LS-G3** | The LMS supports LTI Advantage (1EdTech LTI 1.3) including Assignment and Grades Service. | LTI Advantage certification confirmed from vendor; at least one tool integrated via LTI Advantage in production. | No LTI Advantage: plug-and-play tool integration is unavailable. |
| **LS-G4** | All user-facing LMS interfaces meet WCAG 2.1 Level AA. A current VPAT (Voluntary Product Accessibility Template) is available. | VPAT dated within 24 months; accessibility audit conducted or in progress. | No accessibility documentation: EU Web Accessibility Directive non-compliance. |
| **LS-G5** | The LMS does not share student behaviour data with the vendor's analytics products without explicit DPIA approval. | Vendor data processing agreement reviewed; DPO confirms no analytics sharing without DPIA. | Vendor analytics data sharing without DPIA: GDPR non-compliance. |

### 3.2 Maturity Assessment — Learning Systems

| Criterion | 0 Absent | 1 Initial | 2 Defined | 3 Managed | 4 Measured | 5 Leading | Doc |
|---|---|---|---|---|---|---|---|
| **LMS sovereignty** | Non-European cloud hosting | European cloud; sub-processors not fully verified | European sovereign cloud or on-prem; verified data residency; DPA in place | ISO 27017/18 verified for hosting; sub-processor list current; annual review | LMS sovereignty audited externally; hosting provider contributes to European sovereign cloud ecosystem | LMS deployment model published as European reference; contributes to SURF/DH.NRW-equivalent cooperative | D3 LMS-10 |
| **LTI ecosystem breadth** | No LTI tools | 1–3 tools via LTI; LTI Advantage not yet operational | LTI Advantage operational; 5+ tools integrated; tool catalogue exists | ≥80% of third-party tools via LTI Advantage; shadow tool rate <10%; catalogue maintained | Tool adoption metrics tracked per LTI tool; underperforming tools reviewed quarterly | LTI catalogue and approval process published as open model for alliance | D3 LMS-02, 3a.4 |
| **xAPI emission coverage** | No xAPI | xAPI from LMS only; external tools not covered | xAPI from LMS and ≥3 major tool types; event types documented | ≥90% of learning activity covered by xAPI; all tool integrations emit standardised events | xAPI coverage metrics tracked; semantic consistency audited annually | xAPI vocabulary contributed to alliance; semantic mapping published | D3 LMS-04, ANA-01 |
| **Content portability** | Proprietary content formats only | Some SCORM content; no QTI export | SCORM 2004 and QTI export operational; content exportable without vendor assistance | All assessment items in QTI; all courses exportable as IMS Common Cartridge; tested annually | Content migration tested to at least one alternative LMS; time-to-migrate documented | Content portability approach published; contributes to European open content standards | D3 LMS-05, 07, 08 |
| **Adoption rate** | <50% monthly active students | 50–70% monthly active | 70–85% monthly active; 80%+ courses have active LMS presence | ≥85% monthly active; ≥90% course LMS presence; mobile access >50% | Adoption metrics benchmarked against European peers; UX improvement cycle active | Adoption and UX research published; contributes to European learning technology community | D3 3a.5 |
| **AI governance in LMS** | AI tools deployed without disclosure or policy | AI disclosure policy exists but inconsistently applied | All AI tools disclose their nature; AI policy documented and approved | AI policy covers all tool types; no AI summative grading; European AI preference applied | AI tool performance and compliance audited annually; student feedback on AI used in redesign | AI governance model published; contributes to European HEI AI policy community | D3 3a.6 |

---

## Section 4: Credentialing and Student Records (Domain 3b)

This section assesses the institution's implementation of learner-owned, cryptographically sealed credentials and its participation in European credential exchange infrastructure. The 75-year persistence requirement and the offline verification requirement are the most architecturally demanding criteria in this section.

### 4.1 Compliance Gates — Credentialing

| ID | Compliance Check | Pass Condition | Fail Consequence |
|---|---|---|---|
| **CR-G1** | At least one credential type is issued in ELM v3 format with a qualified electronic signature from the institution's PKI. | ELM v3 credential sample available; signature verifiable via institution's published public key; EDCI-verified. | No ELM issuance: European credential standard not implemented. |
| **CR-G2** | The credentialing archive is append-only and immutable. Modifications to issued credentials are not technically possible. | Technical immutability verified; audit log confirms no modifications; DR tested. | Mutable archive: learner ownership and data integrity principles violated. |
| **CR-G3** | Students can export all their credentials in ELM format within 24 hours of request at no cost. | Export mechanism demonstrated; 24-hour SLA documented; cost: zero. | Export not available or delayed: learner ownership principle violated. |
| **CR-G4** | An EMREX Node is operational and registered with the EMREX network. | EMREX registry listing confirmed; electronic transcript exchange tested with at least one partner institution. | No EMREX node: electronic transcript exchange unavailable. |
| **CR-G5** | The credential revocation policy is documented, DPO-approved, and technically implemented. | Policy available; revocation mechanism tested; student notification tested. | No revocation policy or mechanism: credential lifecycle management incomplete. |

### 4.2 Maturity Assessment — Credentialing and Student Records

| Criterion | 0 Absent | 1 Initial | 2 Defined | 3 Managed | 4 Measured | 5 Leading | Doc |
|---|---|---|---|---|---|---|---|
| **ELM credential coverage** | No ELM credentials issued | Pilot: one credential type in ELM | Qualifications (degree/diploma) issued in ELM v3; EDCI-verified; student export operational | All major award types in ELM; module-level credentials issued; ESCO mappings present | Micro-credentials in ELM; all credentials wallet-compatible; Europass integration live | ELM implementation published as reference; contributes to EDCI standards community | D3 CRED-01,07,10 |
| **Offline verifiability** | Verification requires live DB lookup | Cryptographic verification possible but not documented | Offline verification documented and demonstrated; public key published | Verification tested independently by partner institutions; zero live-system dependency | Verification infrastructure audited annually; 99.99% uptime of public key endpoint | Verification model published; contributes to European credential trust framework | D3 CRED-02,03 |
| **Archive permanence** | Mutable records; no long-term retention plan | Retention policy exists but not enforced technically | Append-only archive; 75-year retention documented; DR tested annually | Archive independent of operational systems; format migration policy documented | Archive tested to survive full operational system replacement; external audit passed | Archive model published; contributes to European long-term credential preservation standards | D3 CRED-04, 3b.5 |
| **EMREX / transcript exchange** | No electronic transcript exchange | EMREX node in development | EMREX node operational; exchange tested with 1–2 partners | EMREX exchange active with ≥5 partner institutions; incoming credits processed electronically | EMREX exchange covers majority of mobility partners; manual transcript rate <10% | EMREX best practice published; contributes to European transcript exchange community | D3 CRED-06 |
| **Micro-credential infrastructure** | No micro-credential issuance | Micro-credential policy developed; infrastructure in planning | Micro-credential issuance operational; EU Council Recommendation conformance verified | ESCO mappings for all micro-credentials; stackability metadata present; employer recognition tested | Micro-credential ecosystem metrics tracked; stackable qualification pathways operational | Micro-credential model published; contributes to European micro-credential standards | D3 CRED-07 |

---

## Section 5: Learning Analytics (Domain 3c)

This section assesses the institution's implementation of privacy-preserving learning analytics. The pseudonymisation gate is binary and foundational: an analytics system that processes identified student data without pseudonymisation at ingestion is non-compliant regardless of all other capabilities. The student dashboard and opt-out mechanism are equally non-negotiable.

### 5.1 Compliance Gates — Learning Analytics

| ID | Compliance Check | Pass Condition | Fail Consequence |
|---|---|---|---|
| **AN-G1** | Pseudonymisation is applied at ingestion into the analytics pipeline. Real student identities are not present in the analytics data store. | Pseudonymisation mechanism documented; technical verification that real identities are absent from analytics store; pseudonym mapping stored separately in Zone A. | Identified student data in analytics: GDPR non-compliance. Analytics must be suspended. |
| **AN-G2** | Stage 2 cohort analytics enforces a minimum cohort size of n≥10. Groups smaller than this are suppressed. | Suppression mechanism technically verified; sample output audit confirms no sub-10 group data. | No cohort size minimum: re-identification risk unmanaged. |
| **AN-G3** | A student-facing data dashboard is operational, showing learning events in plain language and providing a correction request mechanism. | Dashboard URL accessible to enrolled students; plain-language event display verified; correction form functional. | No student dashboard: GDPR Art. 15 right of access not implemented. |
| **AN-G4** | An opt-out mechanism for Stage 3 individual analytics is operational and does not affect other services. | Opt-out function demonstrated; verified that opting out does not affect LMS access or other services. | No opt-out: GDPR Art. 21 right to object not implemented. |
| **AN-G5** | Early-warning models have been tested for demographic bias in the last 12 months. Biased models are corrected before deployment. | Bias testing report available; methodology documented; corrections applied where bias found. | No bias testing: EU AI Act high-risk AI requirements not met. |

### 5.2 Maturity Assessment — Learning Analytics

| Criterion | 0 Absent | 1 Initial | 2 Defined | 3 Managed | 4 Measured | 5 Leading | Doc |
|---|---|---|---|---|---|---|---|
| **Pipeline privacy architecture** | Identified student data in analytics | Pseudonymisation planned; landing stage without pseudonymisation | Three-stage pipeline operational; pseudonymisation at ingestion; mapping in Zone A | Pseudonymisation verified by annual technical audit; re-identification risk assessment conducted | Privacy architecture independently audited; re-identification attempts tested and documented | Privacy architecture published as European reference; contributes to EU learning analytics standards | D3 ANA-02, 3c.2 |
| **Student data rights implementation** | No student data access | Students can request data but process is manual | Student dashboard operational; events shown in plain language; opt-out functional | Dashboard updated in real-time; correction process 5-day SLA; student satisfaction measured | Data rights fulfilment rate tracked; NPS for dashboard measured; continuous improvement cycle | Student data rights implementation published as European model; contributes to policy development | D3 ANA-03,04,08, 3c.4 |
| **Early-warning system quality** | No early-warning system | Early-warning exists but no bias testing or validation | Early-warning operational; annual bias test conducted; demographic parity measured | Bias corrected; model performance tracked by cohort; unexplained differential flagged automatically | Predictive accuracy and fairness metrics benchmarked against European peers; student feedback used in redesign | EWS model and fairness methodology published; contributes to European responsible AI in education | D3 ANA-05,07 |
| **Analytics serving learner** | Analytics outputs used only for institutional reporting | Some outputs shared with tutors but without student consent or transparency | Tutor access scoped to own students; student consent in place; purpose limitation documented | Personalised learning support active; student-reported helpfulness of analytics >60% | Correlation between analytics intervention and student outcome improvement measured | Analytics-to-outcome evidence published; contributes to European learning analytics research | D3 ANA-05,06, 3c.3 |
| **xAPI semantic consistency** | No standardised event collection | xAPI from LMS only; external tools not covered | Controlled vocabulary documented; ≥3 tool types emitting semantically consistent events | Semantic consistency audited annually; ontology maintained and versioned | Cross-tool analytics validated; semantic drift detection automated | xAPI ontology published; contributes to IEEE xAPI standards community | D3 ANA-01, 3c.2 |

---

## Section 6: Backend and Stakeholder Data (Domain 3d)

This section assesses the highest-protection data domain in the platform. ISO/IEC 27001 certification and a current Record of Processing Activities are non-negotiable compliance requirements. The one-directional data authority rule — that 3d feeds all other domains but never receives data back as master authority — is the most important architectural criterion in this section.

### 6.1 Compliance Gates — Backend Data

| ID | Compliance Check | Pass Condition | Fail Consequence |
|---|---|---|---|
| **BD-G1** | Zone A infrastructure holds current ISO/IEC 27001 certification. Certificate scope includes all systems in Domain 3d. Last audit was within 12 months. | Certificate available; scope document confirms Domain 3d coverage; audit date within 12 months. | No ISO 27001: security assurance for most sensitive data is unverified. |
| **BD-G2** | A Record of Processing Activities (RoPA) per GDPR Art. 30 covers all Domain 3d sub-domains (identity, HR, finance, student records, research). Last reviewed within 12 months. | RoPA document available; five sub-domains covered; DPO review date within 12 months. | Incomplete or outdated RoPA: GDPR Art. 30 non-compliance. |
| **BD-G3** | HR and finance systems are hosted in Zone A (European sovereign infrastructure). No HR or financial personal data is hosted outside European jurisdiction. | Hosting contracts confirm European data residency for HR and ERP systems; DPO approval on record. | Non-European hosting of HR/finance: highest-risk data sovereignty non-compliance. |
| **BD-G4** | Privileged Access Management (PAM) is deployed for all Zone A systems. Separate admin credentials, session recording, and time-limited elevation are operational. | PAM system named; separate credential model verified; session recording active; elevation audit log available. | No PAM: privileged account security is the institution's highest-priority unmitigated risk. |
| **BD-G5** | Annual bulk data export test has been conducted for all Domain 3d systems in the last 12 months. Results reported to Architecture Review Board. | Test report available; ARB meeting minutes confirm review; gaps have remediation plans. | No export test: exit capability for most critical data is unverified. |

### 6.2 Maturity Assessment — Backend Data

| Criterion | 0 Absent | 1 Initial | 2 Defined | 3 Managed | 4 Measured | 5 Leading | Doc |
|---|---|---|---|---|---|---|---|
| **One-directional data authority** | Other domains write to 3d as masters | Some reverse flows exist; mapping incomplete | All eight master data domains have documented authoritative source in 3d; reverse writes prohibited | Reverse write prohibition enforced at API gateway; violations create alerts | Zero confirmed reverse write violations in last 12 months; governance enforced automatically | Data authority model published; contributes to European HEI data governance standards | D2 §7.3, D3 3d.2 |
| **ISO 27001 scope and currency** | No ISMS | ISMS in planning or partial implementation | ISO 27001 certified for Zone A systems; last audit <12 months | ISO 27701 implemented; annual surveillance audit findings actioned within 30 days | ISO 27001 + 27701 + 27017 + 27018 all certified; ISMS maturity improving year-on-year | ISMS approach published; contributes to European HEI information security community | D3 BACK-01 |
| **JML SLA performance** | No SLA; manual provisioning | SLA defined; performance not measured | JML SLA documented (joiners 4h, leavers 2h); last-quarter performance data available | SLA compliance >99%; breaches investigated with root-cause analysis within 5 days | SLA compliance >99.9%; proactive anomaly detection prevents breaches before they occur | JML SLA model published; contributes to European IGA best practice | D3 BACK-03, D2 §4.2 |
| **Data encryption posture** | Encryption absent or ad hoc | Encryption at rest for some Zone A systems | AES-256 at rest for all systems; TLS 1.3 in transit; key management documented | Keys in HSM or equivalent; rotation schedule enforced; encryption audited annually | Key management independently audited; zero encryption gaps confirmed; automated compliance checking | Encryption approach published; contributes to European HEI security standards | D3 BACK-04 |
| **Vendor lock-in risk** | No exit plans; proprietary formats | Exit plans for some systems; format inventory incomplete | Customisation register maintained for all 3d systems; exit plans documented | Annual export test passing for all systems; migration paths documented to at least one alternative | Exit capability independently verified; contract exit clauses reviewed by legal annually | Lock-in risk model published; contributes to European open procurement standards | D3 3d.4 |

---

## Section 7: Administration Systems and AI-Augmented Processes (Domain 3e)

This section assesses the institution's digitalisation of administrative processes and its governance of AI augmentation in those processes. The adoption criterion is assessed with particular rigour here — historical failure rates in administrative tool adoption are high enough that adoption below threshold is treated as a compliance issue, not merely a maturity issue.

### 7.1 Compliance Gates — Administration Systems

| ID | Compliance Check | Pass Condition | Fail Consequence |
|---|---|---|---|
| **AS-G1** | ≥90% of committee decisions are recorded in a structured, searchable workflow system. Decisions recorded only in email or shared drive word documents are not compliant. | Decision system audit: sample of last quarter's decisions; ≥90% in workflow system. | <90% structured decisions: governance auditability requirement not met. |
| **AS-G2** | All AI-generated outputs (meeting summaries, draft minutes, routing suggestions, report drafts) are labelled as AI-generated and require explicit human approval before distribution. | Sample AI outputs reviewed; labelling verified; approval workflow audit log reviewed. | AI outputs distributed without labelling or human approval: EU AI Act non-compliance. |
| **AS-G3** | AI tools used in this domain operate on European sovereign infrastructure. Governance data is not processed by non-European AI services. | AI tool hosting verified; DPO confirms no governance data sent to non-European AI infrastructure. | Non-European AI processing governance data: sovereignty and GDPR non-compliance. |
| **AS-G4** | A documented retention schedule exists for all document and decision types, aligned with applicable national archive law. | Retention schedule document available; DPO and records manager approval on record; schedule reviewed in last 12 months. | No retention schedule: records management and legal compliance requirements unmet. |
| **AS-G5** | Administration tool adoption rate is ≥80% of target users. Tools below 60% adoption after 12 months have a documented improvement plan. | Adoption metrics for last 12 months available; tools below threshold have ARB-reviewed improvement plans. | Adoption not measured: UX and adoption requirements cannot be assessed. |

### 7.2 Maturity Assessment — Administration Systems

| Criterion | 0 Absent | 1 Initial | 2 Defined | 3 Managed | 4 Measured | 5 Leading | Doc |
|---|---|---|---|---|---|---|---|
| **Decision digitalisation** | Decisions in email/shared drives only | Workflow system deployed but <50% adoption | ≥90% decisions in structured system; decision records include all required fields | Decision search and audit functional; implementation tracking operational; compliance auditable | Governance health dashboard live; cycle time metrics tracked; leadership reviews monthly | Decision management model published; contributes to European higher education governance standards | D3 ADM-01,02,08 |
| **AI augmentation quality** | No AI augmentation | AI tools deployed without governance framework | Tier 1/2/3 AI framework documented; all AI outputs labelled; human approval workflow operational | AI performance measured; Tier 3 automation audited annually; escalation alerts functional | AI augmentation ROI measured (time saved vs. quality of output); student/staff satisfaction measured | AI augmentation governance model published; contributes to European responsible AI in HEI policy | D3 ADM-04, 3e.4 |
| **European sovereign AI tooling** | Non-European AI for governance data | European AI in pilot; some non-European tools remain | All governance AI on European sovereign infrastructure; DPA in place with all AI providers | AI provider sovereignty verified annually; sub-processor list current; no non-European processing | AI sovereignty independently audited; contributing to European sovereign AI ecosystem development | Contributing to open European AI models for governance use cases | D3 ADM-05 |
| **Records management compliance** | No retention schedules; ad hoc deletion | Retention policy documented for major document types | Retention schedules implemented for all document types; automated disposition operational | Compliance audited annually; retention breach rate <1%; archive access controls verified | Zero retention breaches; automated compliance monitoring; national archive authority satisfied | Records management model published; contributes to European digital records standards | D3 ADM-06,07 |
| **Adoption and UX** | <50% target users | 50–70% adoption; UX issues unaddressed | ≥80% adoption at 12 months; UX research conducted once; improvement actions taken | Adoption >85%; monthly UX feedback cycle; mobile access >60% | Adoption metrics benchmarked against peers; continuous improvement cycle; NPS >40 | UX research and adoption methodology published as European reference | D3 ADM-09, 3e.5 |
| **Governance analytics** | No governance process analytics | Manual reporting on governance metrics | Basic governance dashboard: open decisions, overdue items, committee workload | Dashboard auto-populated; trend analysis; decision cycle time improving year-on-year | Governance health metrics benchmarked; predictive modelling of workload and risk | Governance analytics model published; contributes to European institutional effectiveness research | D3 ADM-08 |

---

## Section 8: Digital Sovereignty and European Interoperability

This section assesses the institution's overall sovereignty posture and its participation in European interoperability standards. It is a cross-cutting section — it draws on evidence from all domain sections but assesses the institution's aggregate strategic position rather than individual domain capabilities.

### 8.1 Compliance Gates — Sovereignty

| ID | Compliance Check | Pass Condition | Fail Consequence |
|---|---|---|---|
| **SOV-G1** | A digital sovereignty status report has been completed in the last 12 months, listing which systems are sovereign, which are not, and the transition plan for non-sovereign systems. | Sovereignty status report available; ARB reviewed; non-sovereign systems have documented transition plans. | No sovereignty status report: the institution's strategic sovereignty position is unknown. |
| **SOV-G2** | EWP participation: the institution supports the current EWP API version for outgoing and incoming mobility processes. | EWP registry listing confirms current API version support; mobility processes operational via EWP. | EWP non-participation: Erasmus+ mobility cannot be administered digitally. |
| **SOV-G3** | All production vendor contracts for Domain 3d systems include: data portability clause, migration API documentation requirement, exit/transition clause, and European data residency requirement. | Sample contract review confirms required clauses; legal team sign-off on record. | Missing contract clauses: exit capability and sovereignty commitments are not contractually enforceable. |
| **SOV-G4** | The institution has a documented open-source and European-preference procurement policy, reviewed and approved by governance in the last 24 months. | Policy document available; governance approval on record; applied to last three major procurements. | No procurement policy: sovereignty preference has no operational effect. |

### 8.2 Maturity Assessment — Digital Sovereignty

| Criterion | 0 Absent | 1 Initial | 2 Defined | 3 Managed | 4 Measured | 5 Leading | Doc |
|---|---|---|---|---|---|---|---|
| **Sovereign infrastructure coverage** | All systems on non-European cloud | Zone A defined; some systems migrating | Zone A operational with ≥3 critical systems; Zone B on European cloud; transition plan for remaining | ≥90% of high-sensitivity data in Zone A; Zone B verified European; sovereignty status tracked | All data in compliant zones; annual sovereignty audit passed; zero unplanned non-European processing | Sovereignty architecture published as European reference; contributes to Gaia-X / European cloud standards | D2 §2 |
| **European standard adoption** | Not participating in major European standards | 1–2 standards in partial implementation | eduGAIN, EWP, ELM all operational at basic level; EMREX node registered | Full participation in eduGAIN, EWP v3+, ELM v3, EMREX; eIDAS trust path in place | All European mobility, credential and identity standards operational; eIDAS Wallet integration live | Contributing to European standards bodies (GÉANT, 1EdTech, EWP consortium, EDCI) | D2 §10 |
| **Open-source and European procurement** | No procurement preference | Policy drafted but not yet applied | Procurement policy applied to last 3 procurements; European/OSS preference documented | Policy compliance rate >80%; each non-European choice formally justified; ARB reviewed annually | 100% procurement policy compliance; European alternatives evaluated for every new procurement | Procurement policy published as model; contributes to European public sector procurement standards | D1 P.II |
| **Alliance and cooperative membership** | No cooperative membership | Awareness of cooperatives; membership in planning | Member of at least one national cooperative (SURF equivalent); cooperative services in use | Contributing member: sharing implementation experience; joining standards working groups | Active contributor: open-source code, configuration, case studies published; standards community roles held | Founding or steering member of European alliance cooperative; shapes European HEI digital strategy | D1 P.V, D2 §2 |
| **Vendor lock-in risk (aggregate)** | High lock-in in most domains; no exit plans | Exit plans for some domains; contract clauses incomplete | Exit plans for all Tier 1 systems; contract clauses in ≥50% of major contracts | Exit clause coverage >80% of major contracts; annual export tests passing across domains | Zero systems without workable exit plan; lock-in risk formally risk-managed at board level | Lock-in risk methodology published; contributes to European open procurement standards | D2 P5 |

---

## Section 9: User Experience and Adoption

This cross-cutting section assesses whether the platform's tools are actually used. It is a distinct section because adoption failure is the most common form of digital transformation failure in higher education — and it is the form most consistently absent from technical evaluation frameworks. Technical compliance without meaningful adoption is assessed no higher than Level 2 in any maturity criterion. An institution cannot claim Level 3 or above for any tool category if it has not measured actual adoption.

### 9.1 Compliance Gate — UX and Adoption

| ID | Compliance Check | Pass Condition | Fail Consequence |
|---|---|---|---|
| **UX-G1** | Adoption metrics (monthly active user rates, task completion rates, or equivalent) are measured and reported for all major tool categories: LMS, collaboration, administrative workflow, student portal. | Adoption measurement methodology documented; data from last two terms available for each major tool category. | Adoption not measured: the institution's actual digital effectiveness is unknown. |
| **UX-G2** | Tools with adoption rates below 60% of target users after 12 months have a documented ARB-reviewed improvement plan or a decision to replace. | Low-adoption tool register available; improvement plans or replacement decisions reviewed by ARB. | Low adoption unaddressed: investment is being wasted; users are using shadow alternatives. |

### 9.2 Maturity Assessment — User Experience and Adoption

| Criterion | 0 Absent | 1 Initial | 2 Defined | 3 Managed | 4 Measured | 5 Leading | Doc |
|---|---|---|---|---|---|---|---|
| **Adoption measurement** | No adoption metrics collected | Ad hoc usage data from some tools | Systematic adoption metrics for all major tools; data collected each term | Metrics benchmarked against peers; trend data over ≥4 terms available | Predictive modelling of adoption risk; early intervention before tools fall below threshold | Adoption measurement methodology published; contributes to European HEI digital effectiveness research | D3 3a.5, 3e.5 |
| **Student experience quality** | Students report significant friction; shadow tools widespread | Mixed experience; some key pain points identified | UX research conducted once; major pain points addressed; shadow tool rate declining | Annual UX research cycle; satisfaction score improving; mobile access >50% for all major tools | NPS >40 for institutional tools; shadow tool rate <5%; continuous user feedback loop | Student experience model published as European reference | D3 3a.5 |
| **Staff experience quality** | Staff report significant friction with institutional tools; workarounds common | Mixed experience; administrative tools particularly poor | UX improvements for top 3 staff pain points implemented; adoption improving | Staff satisfaction measured; tool performance SLAs tracked; UX investment justified by adoption data | Staff NPS >40 for institutional tools; administrative tool adoption >85% | Staff digital experience model published; contributes to European HEI HR and digital strategy | D3 3e.5 |
| **Accessibility compliance** | No accessibility assessment | WCAG 2.1 AA assessed for one or two tools | VPAT available for all major tools; WCAG 2.1 AA verified or in progress for all | WCAG 2.1 AA confirmed for all tools; annual accessibility audit conducted | WCAG 2.2 readiness assessed; user testing with disabled users conducted annually | Accessibility evaluation methodology published; contributes to European inclusive education standards | D3 LMS-06 |
| **Mobile and offline capability** | Desktop-only tools; no mobile support | Mobile access available but degraded experience | All major tools functional on mobile browsers without native app requirement; offline reading for key content | Native mobile apps or PWAs for high-frequency functions; offline mode for learning content | Mobile-first design validated by usage data; >60% of sessions on mobile; offline coverage >80% | Mobile-first evaluation methodology published; contributes to European digital education access research | D3 3a.5, 3e.5 |

---

## Section 10: Score Summary and Interpretation

Complete the score summary table below by entering the institution's assessed level (0–5) for each criterion and calculating the section totals. The maximum possible score for each section and the overall total are shown. Use the interpretation guide to understand what the overall score means and to set realistic improvement targets.

| Section / Domain | Max Score | Criteria |
|---|---|---|
| **Section 1: Architecture Foundations** | 25 | 5 criteria × 5 |
| **Section 2: Identity and Federation** | 25 | 5 criteria × 5 |
| **Section 3: Learning Systems (3a)** | 30 | 6 criteria × 5 |
| **Section 4: Credentialing & Student Records (3b)** | 25 | 5 criteria × 5 |
| **Section 5: Learning Analytics (3c)** | 25 | 5 criteria × 5 |
| **Section 6: Backend & Stakeholder Data (3d)** | 25 | 5 criteria × 5 |
| **Section 7: Administration Systems & AI (3e)** | 30 | 6 criteria × 5 |
| **Section 8: Digital Sovereignty** | 25 | 5 criteria × 5 |
| **Section 9: User Experience & Adoption** | 25 | 5 criteria × 5 |
| **TOTAL ARCHITECTURE MATURITY SCORE** | **235** | **47 criteria** |

*(The source table also includes "Your Score" and "Gap" columns, left blank for institutional self-completion — reproduced here as the scoring structure only, since the OUG has not yet conducted this assessment.)*

### 10.1 Score Interpretation

| Score Range | Band | Interpretation |
|---|---|---|
| **0** | **Not Compliant** | The institution has not yet begun systematic implementation of the European HEI Digital Alliance Framework. Compliance gates are failing in multiple sections. The priority is to address failing compliance gates before focusing on maturity improvement. Alliance membership is conditional on a remediation plan with binding timelines. |
| **1–47** | **Early Stage** | Foundation work is beginning but implementation is inconsistent and largely undocumented. Most criteria are at Level 0 or 1. The institution should focus on Sections 1 (Architecture Foundations) and 2 (Identity) before progressing other sections. |
| **48–94** | **Developing** | The institution has documented approaches in most areas and is beginning systematic implementation. Some compliance gates may still be failing. The priority is closing remaining compliance gate failures and reaching Level 2 in all criteria. |
| **95–141** | **Defined** | The institution has documented and consistently applied approaches across most domains. Compliance gates are passing. The priority is moving from defined to managed — adding measurement, monitoring and continuous improvement. |
| **142–188** | **Managed** | The institution measures performance across all domains and uses data to drive improvement. Compliance gates are all passing. The institution is beginning to benchmark against peers and contribute to the European ecosystem. |
| **189–235** | **Leading** | The institution is at European best practice across all domains and is actively contributing to advancing the field. It is a reference point for other institutions and a contributor to European standards and cooperative services. |

### 10.2 Section Weighting and Priority

Not all sections carry equal strategic weight. The following weighting reflects the architectural dependencies between sections: foundational sections that enable all others score higher weight in the alliance's assessment of institutional readiness for collaborative services.

| Section | Weight | Alliance Gate | Rationale |
|---|---|---|---|
| Architecture Foundations | **Critical** | Level 2 required | Prerequisite for all other sections. Without governance and documentation, no other assessment is reliable. |
| Identity and Federation | **Critical** | Level 3 required | Without reliable identity, no federated service — EWP, ELM, LMS, analytics — is trustworthy. |
| Learning Systems (3a) | **High** | Level 2 required | Primary student-facing service; sovereignty and adoption failures directly affect educational mission. |
| Credentialing (3b) | **High** | Level 2 required | European credential standards are a policy obligation for Erasmus+ participants. |
| Learning Analytics (3c) | **High** | Level 2 required | GDPR compliance in analytics is a legal requirement; pseudonymisation gate is non-negotiable. |
| Backend Data (3d) | **Critical** | Level 3 required | Highest-sensitivity data; ISO 27001 is a baseline legal and contractual expectation. |
| Administration Systems (3e) | **Medium** | Level 1 required | High value but lower risk; institutional maturity varies widely; compliance gates are achievable. |
| Digital Sovereignty | **High** | Level 2 required | Without sovereignty posture, other sections cannot be sustained in the long term. |
| User Experience | **Medium** | Level 1 required | Enables the institution to demonstrate that technical compliance translates to real-world benefit. |

---

## Section 11: Improvement Plan Template

Complete one improvement plan entry for each priority finding. Priority findings are the criteria with the greatest gap between current level and target level, weighted by the section priority from Section 10.2. A minimum of three and a maximum of eight improvement entries should be active at any time. More than eight active improvement items typically indicates insufficient prioritisation.

*(The source provides three blank copies of the following template for institutional completion — reproduced once here as the structure, not populated, since the OUG has not yet conducted this assessment.)*

| Field | Content |
|---|---|
| **Section / Criterion** | |
| **Current Level (0–5)** | |
| **Target Level (0–5)** | |
| **Target Date** | |
| **Owner** | |
| **Why This Priority** | |
| **Required Actions (numbered steps)** | 1. 2. 3. |
| **Success Measures** | |
| **Dependencies / Blockers** | |
| **Alliance Support Required** | |

---

## Annex A: Compliance Gate Summary Checklist

This checklist consolidates all compliance gates across all sections for use as a rapid initial screen. Record Pass, Fail, or Not Assessed for each gate. Any Fail requires a remediation plan before the full maturity assessment is meaningful.

*(37 gates total across nine sections — reproduced below by ID and check; "Status" and "Remediation Plan Ref" columns are blank in the source, for institutional completion.)*

| Gate | Check |
|---|---|
| **AF-G1** | Enterprise Architect role exists with documented responsibilities |
| **AF-G2** | Architecture Review Board meets quarterly; decision log maintained |
| **AF-G3** | ADR repository with ≥5 decisions from last 12 months |
| **AF-G4** | Legacy system decommission register with target dates |
| **AF-G5** | DPIA completed for all personal data systems; DPO reviewed |
| **ID-G1** | IGA system in production; provisioning from HR and admissions |
| **ID-G2** | National federation + eduGAIN participation confirmed |
| **ID-G3** | MFA enforced for all Zone A administrative accounts |
| **ID-G4** | JML SLA documented and measured: joiners 4h, leavers 2h |
| **ID-G5** | Attribute release policy documented, DPO-approved, enforced |
| **LS-G1** | LMS on European sovereign or on-premises infrastructure |
| **LS-G2** | LMS authenticates via OIDC; zero local student/staff accounts |
| **LS-G3** | LTI Advantage (LTI 1.3 + AGS) in production |
| **LS-G4** | WCAG 2.1 AA compliance documented; current VPAT available |
| **LS-G5** | Vendor analytics data sharing blocked without DPIA approval |
| **CR-G1** | ELM v3 credential issued and EDCI-verified |
| **CR-G2** | Credentialing archive append-only and immutable |
| **CR-G3** | Student credential export in ≤24 hours at zero cost |
| **CR-G4** | EMREX Node operational and registered |
| **CR-G5** | Credential revocation policy documented and technically implemented |
| **AN-G1** | Pseudonymisation at analytics ingestion; no real identities in analytics store |
| **AN-G2** | Cohort size minimum n≥10 technically enforced in Stage 2 |
| **AN-G3** | Student data dashboard operational; plain-language events; correction mechanism |
| **AN-G4** | Stage 3 opt-out operational; does not affect other services |
| **AN-G5** | Early-warning model bias test completed in last 12 months |
| **BD-G1** | ISO/IEC 27001 certified for Zone A; last audit <12 months |
| **BD-G2** | RoPA covers all Domain 3d sub-domains; DPO review <12 months |
| **BD-G3** | HR and finance on European sovereign infrastructure |
| **BD-G4** | PAM deployed for Zone A; session recording active; time-limited elevation |
| **BD-G5** | Annual bulk data export test conducted; ARB reviewed |
| **AS-G1** | ≥90% of committee decisions in structured workflow system |
| **AS-G2** | AI outputs labelled; human approval workflow operational |
| **AS-G3** | Governance AI on European sovereign infrastructure |
| **AS-G4** | Retention schedule documented and DPO-approved |
| **AS-G5** | Administration tool adoption ≥80%; low-adoption tools have improvement plans |
| **SOV-G1** | Digital sovereignty status report completed in last 12 months |
| **SOV-G2** | EWP participation: current API version for outgoing and incoming mobility |
| **SOV-G3** | Domain 3d vendor contracts include portability, exit and residency clauses |
| **SOV-G4** | Open-source / European procurement policy approved and applied |
| **UX-G1** | Adoption metrics measured and reported for all major tool categories |
| **UX-G2** | Tools below 60% adoption at 12 months have ARB-reviewed improvement plans |

## Annex B: Visual Reporting — Radar Chart Template

The following radar chart template is used for reporting to institutional leadership, alliance bodies and accreditation organisations. It provides a visual representation of the institution's maturity profile across the nine assessment sections. The chart shows current score (solid line) and target score (dashed line) for each section, making gaps visible at a glance.

> **Radar Chart Data Template**
>
> Complete the following values from your Section 10 score summary to generate the radar chart. Use a spreadsheet tool (LibreOffice Calc, Excel) with the radar chart type and apply the values below. The maximum axis value for each dimension is the section maximum score (25 or 30 as applicable).

| Section | Max | Current | Target (12 months) |
|---|---|---|---|
| Architecture Foundations | 25 | | |
| Identity & Federation | 25 | | |
| Learning Systems | 30 | | |
| Credentialing | 25 | | |
| Learning Analytics | 25 | | |
| Backend Data | 25 | | |
| Administration & AI | 30 | | |
| Digital Sovereignty | 25 | | |
| User Experience | 25 | | |

The radar chart should be included in the Annual Architecture Assessment report, the Alliance membership report, and the Architecture Review Board quarterly briefing. Over time, the chart shows the institution's improving maturity profile and identifies sections where progress is slower than planned.

## Annex C: Alliance Reporting Template

Institutions submit the following summary to the European Higher Education Digital Alliance coordination body annually, by 31 March for the preceding academic year.

| Field | Content |
|---|---|
| **Institution name and country** | |
| **Reporting period** | Academic year |
| **Total maturity score (current)** | |
| **Total maturity score (previous year)** | |
| **Compliance gates: number passing** | |
| **Compliance gates: number failing** | |
| **Critical-section compliance (AF, ID, 3d)** | All passing / Partially passing / Non-compliant |
| **Top 3 improvement items this year** | 1. 2. 3. |
| **European standards newly implemented** | |
| **Cooperative memberships** | |
| **Open-source contributions made** | |
| **Alliance support requested** | |
| **Key challenges for next year** | |
| **Date and signatory** | |

---

*Open University of Germany · HEI IT Architecture Evaluation Framework · Document 4 of the Digital Alliance Framework · Version 1.0 · May 2026*
