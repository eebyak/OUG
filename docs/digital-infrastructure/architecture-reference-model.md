---
layout: page
title: "Architecture Reference Model"
---
 


*The Modular Platform Architecture for European Higher Education: Principles, Zones, Layers, Data Ownership and Integration Contracts*

*Document 2 of the European HEI Digital Alliance Framework · Version 1.0 · May 2026*
*Companion to [Document 1: European HEI Digital Alliance Manifesto](manifesto.md)*

> **Source:** migrated from `D2_Architecture_Reference_Model.docx`
> **Status:** *(to be set — see [Document Status](../index.md#document-status))*

## Introduction: What This Document Does

This Architecture Reference Model is the technical framework that translates the principles of the European HEI Digital Alliance Manifesto into architectural decisions. Where the Manifesto establishes *why* European higher education institutions must act collectively on digital sovereignty — and commits them to API-first architecture, European infrastructure preference, student data protection and cooperative development — this document establishes *how* those commitments are realised in a concrete, implementable architecture.

This document is authoritative on four things: the deployment zone model that defines where different categories of data and service reside; the five-layer architecture model that organises the functional capabilities of the platform; the data ownership and boundary decisions that determine which layer holds master authority for which data; and the integration contract requirements that govern how layers communicate. These four architectural decisions are the foundation on which [Document 3](functional-domain-specifications.md) (the Functional Domain Specifications) and [Document 4](hei-evaluation-framework.md) (the Evaluation Framework) are built.

This document is not a product specification and does not mandate specific vendor choices. It mandates architectural patterns, open standards and interface contracts. Within those constraints, institutions retain freedom to select components that best match their context, maturity and cooperative memberships.

> **How to Read This Document**
>
> The document is structured in four parts. Part I establishes the six architecture principles that govern all decisions in this framework. Part II describes the three-zone sovereign deployment model. Part III presents the five-layer functional architecture with data ownership assignments for each layer. Part IV defines the integration contracts — the data flows, API patterns and boundary rules — between layers and between the platform and the European interoperability ecosystem.
>
> Institutions implementing this framework should read Part I first and treat it as a governance commitment. Parts II and III define the target architecture. Part IV is the operational reference for integration teams.

---

## Part I: Architecture Principles

### 1. The Six Architecture Principles

These six principles are binding on all architecture decisions made under this framework. They are not guidelines — they are constraints. A decision that violates a principle requires explicit governance approval and a documented exception with a time-limited remediation plan. The principles are listed in order of precedence: where two principles appear to conflict, the higher-numbered principle gives way to the lower-numbered one.

#### Principle 1: Identity Before Everything Else

No component of the platform enters production use until the identity layer is established, tested and authoritative. Identity is the prerequisite for every other architectural decision because every other service — learning management, campus administration, analytics, collaboration, credentialing — depends on knowing, with confidence, who a person is, what their current affiliations are, what roles they hold, and what they are authorised to access.

This principle has operational consequences that frequently conflict with institutional impatience to deploy visible services. A new LMS, a new collaboration platform, a new student portal — all of these are attractive early wins. None of them should be deployed for production use before the identity layer is stable, because deploying them without a stable identity layer creates precisely the kind of fragmented, user-store-per-application architecture that this framework is designed to eliminate.

The identity layer is considered stable when: an authoritative IGA system is provisioning users from HR and student records; a federation gateway is connected to the national higher education federation and eduGAIN; a Joiner-Mover-Leaver lifecycle model is operating automatically; and MFA is enforced for all administrative and high-risk accounts.

#### Principle 2: API-First, No Point-to-Point

All communication between platform components — whether between internal layers, between legacy systems and new components, or between the institution's platform and external partners — passes through the API gateway layer. No direct database connections, no file-based integrations, no point-to-point API calls that bypass the gateway. Without exception.

This principle is the single most operationally difficult commitment in this framework. It will be violated under pressure — when a quick integration is needed, when a legacy system has no API surface, when a vendor insists their product must connect directly to another product. Each violation creates a dependency that accumulates into the brittle, opaque, unmaintainable integration landscape that this architecture is designed to replace. The governance response to every proposed exception is: define an API contract, expose it through the gateway, and treat the point-to-point connection as a transitional arrangement with a documented decommission date.

#### Principle 3: Standards Define Boundaries, Not Products

The boundaries between components — what Layer 3 must provide to Layer 4, what the campus management service must expose to the credential layer, what the learning system must send to the analytics module — are defined in terms of open, publicly documented standards, not in terms of the specific product currently occupying that position.

This means: before any component is procured, the institution documents the API contracts that component must satisfy, expressed in terms of open standards. The procurement specification asks whether a product satisfies the contract, not whether it integrates with specific other products. Products that require non-standard integration patterns, proprietary APIs or direct database connections do not satisfy the contract and cannot be selected under this framework.

The practical benefit is that components become genuinely replaceable. When the campus management service is replaced in Year 6, it is replaced by any product that satisfies the same API contracts. The rest of the platform is unaffected.

#### Principle 4: Data Has One Master, Many Consumers

Every piece of institutional data has exactly one authoritative source — one system that is the master of record for that data. All other systems that need that data consume it through the API layer; they do not hold independent copies that they update autonomously.

This principle eliminates data duplication, synchronisation failures and the integrity problems that arise when multiple systems each believe they own the same data. A student's name exists in one place — the Backend/Stakeholder Data layer, fed from the HR and admissions systems. The learning system displays it by consuming the identity service. The credential system includes it in a signed credential by reading it from the identity layer at the moment of issuance. Neither system stores its own copy that it updates independently.

Data ownership assignments for each domain are specified in Part III of this document and elaborated in [Document 3](functional-domain-specifications.md).

#### Principle 5: Exit Capability Is Architecturally Enforced

The platform's architecture must make it possible to replace any component without replacing all components. This requires that every component: exposes its data in open, documented formats; supports data export through a defined migration API; does not require proprietary data formats for its primary operations; and satisfies its API contracts through standard protocols that an alternative product can also satisfy.

Exit capability is not just a contractual requirement (which vendors can subvert through pricing and friction). It must be architecturally enforced: the institution should be able to demonstrate, for each component, a documented migration path to at least one alternative that satisfies the same API contracts. If this cannot be demonstrated, the architecture has a lock-in risk that must be addressed.

#### Principle 6: Security and Privacy Are Structural, Not Supplemental

Security controls and privacy protections are built into the architecture at the layer boundaries, not added as a supplemental layer on top. This means: authentication and authorisation are enforced at the API gateway before any request reaches a component; data minimisation is enforced at the analytics boundary before any student data leaves the learning layer; pseudonymisation is applied before data crosses from the Learning Systems layer to the Analytics layer; and encryption is applied to all data in transit and at rest as a default, not as an option.

A Data Protection Impact Assessment (DPIA) is required before any new component is connected to the platform. The DPIA must document: what personal data the component processes; the legal basis for that processing; what data minimisation and pseudonymisation measures are applied; who has access and under what authorisation model; and what the retention and deletion schedule is. Components that cannot satisfy the DPIA requirements do not connect to the platform.

---

## Part II: The Three-Zone Deployment Model

### 2. Sovereign Deployment Zones

The platform is deployed across three functional zones. These zones are not organisational units or network segments in the traditional sense — they are governance zones that determine the legal jurisdiction, physical location, access controls and operational model applicable to each component. A component's zone assignment is a governance decision, not a purely technical one, and must be reviewed annually.

The zone model is the architectural expression of the digital sovereignty value framework from the Manifesto. It ensures that the data and functions that require maximum institutional control are in Zone A; that elastic, scalable and collaborative functions are in Zone B on European sovereign infrastructure; and that cross-institutional trust and mobility functions are in Zone C under federated governance.

**Zone A: Sovereign Core** — IAM / Identity Governance and Administration (IGA); Root CA and PKI (certificate authority and key management); Campus management / Student Information System core; ERP / Finance / HR / Payroll core; Research data management (sensitive and restricted datasets); Data warehouse curated zone (quality-assured, governed data); Archive and records management (long-term preservation); SIEM / Security Operations Centre; all personal data of students and staff in its authoritative form.

Zone A operates either on self-managed on-premises infrastructure or in a contractually isolated sovereign cloud environment. "Contractually isolated" means: data processing agreement in place, data stored exclusively on European soil, sub-processors listed and approved, no access by non-European authorities permitted, auditable at any time by the institution without vendor cooperation. Zone A components must meet ISO/IEC 27001 requirements and, where personal data is processed, ISO/IEC 27701.

**Zone B: European Platform Cloud** — API gateway and integration platform (Gravitee / Frends); container platform and Kubernetes management; Learning Management System (LMS); collaboration (file storage, document editing, messaging, video conferencing); DevOps (Git, CI/CD, artefact registry); object storage (landing zone for analytics pipelines); disaster recovery capacity and backup targets; AI sandboxes, notebook environments, GPU workloads; monitoring, logging and observability infrastructure.

Zone B operates on European sovereign cloud infrastructure — OVHcloud, Exoscale, T-Systems T Cloud Public, or equivalent — with verifiable European data residency, published sub-processor lists, and ISO/IEC 27017/27018 certification. Zone B is designed for elastic scaling, cross-institution collaboration and rapid service deployment. It is not appropriate for personal data in its authoritative form, but is appropriate for application processing of that data when adequate controls are in place.

**Zone C: Federation and Partner Zone** — eduGAIN national federation participation; EWP (Erasmus Without Paper) API registry and connectors; library consortium access (EZB, Primo, OCLC WorldShare); research network access (GÉANT, national research networks); European Student Card / ESI identity assertions; eIDAS trust paths and European Digital Identity Wallet integration; guest identity management (time-limited, scoped access); alumni identity and engagement services; partner organisation portals (employers, research partners).

Zone C is not infrastructure that the institution owns — it is a trust fabric that the institution participates in through standardised federation protocols (SAML 2.0, OIDC, EWP APIs). The institution's interface to Zone C is the federation gateway in Zone A/B, which enforces trust decisions, attribute release policies and access scope limits. No Zone C entity has direct access to Zone A systems. All cross-zone communication goes through the federation gateway.

### 2.1 Zone Boundary Rules

The following rules govern what may and may not cross zone boundaries. These rules are architectural — they must be enforced by the API gateway and federation gateway, not merely stated as policy.

| Data / Function | Zone A → Zone B | Zone B → Zone A | Zone C ↔ A/B |
|---|---|---|---|
| Personal data (raw, identified) | Not permitted in persistent storage. Permitted for transient processing under DPIA | Not permitted without explicit authorisation and audit log | Not permitted. Attribute assertions only, via federation gateway |
| Pseudonymised analytics data | Permitted for analytics processing after pseudonymisation at Zone A boundary | Not permitted | Not applicable |
| Anonymised aggregate data | Freely permitted | Freely permitted | Freely permitted for reporting |
| Application session tokens | Permitted (short-lived, scoped) | Not applicable — tokens originate in Zone B | Not permitted in raw form. Federated assertions only |
| Credentials (certified, sealed) | Permitted (student holds; Zone A archive is read-only reference) | Not applicable | Permitted for verification (cryptographic, no live database call required) |
| Audit logs | Zone B logs replicated to Zone A SIEM | Not applicable | Not applicable |
| Configuration and secrets | Zone A is master of all secrets. Zone B receives time-limited, scoped credentials | Not permitted — Zone B never stores Zone A master credentials | Not applicable |

---

## Part III: The Five-Layer Functional Architecture

### 3. Layer Architecture Overview

The platform is organised into five functional layers. Each layer has a defined set of responsibilities, owns specific categories of data, exposes specific API surfaces, and consumes services from other layers only through defined interfaces. The layer model is a logical organisation — it does not necessarily correspond to separate physical systems. A single product may participate in multiple layers. What matters is that the responsibilities, data ownership and interface contracts defined for each layer are respected, regardless of which product implements them.

The five layers, in order from foundational to user-facing, are:

- **Layer 1: Identity and Trust** — who is this person and what are they authorised to do?
- **Layer 2: Credentialing and Student Records** — what has this person achieved and how is it certified?
- **Layer 3: Process and Academic Systems** — how are academic and administrative processes conducted?
- **Layer 4: Integration and Data** — how do components communicate and how is institutional data governed?
- **Layer 5: Experience and Engagement** — what do users actually interact with?

The fundamental rule of the layer model is: a higher-numbered layer depends on lower-numbered layers, never the reverse. Layer 5 (experience) consumes services from Layers 1–4. Layer 4 (integration) connects to Layers 1–3. Layer 3 (process) depends on Layer 1 (identity) and exposes data to Layer 2 (credentialing). No lower-numbered layer ever calls a higher-numbered layer. This prevents the circular dependencies that create architectural fragility.

### 4. Layer 1: Identity and Trust

**Data Owner:** IAM/IGA system (Zone A). No other layer holds authoritative identity data.
**Exposes via API:** User provisioning events (SCIM), attribute assertions (SAML/OIDC), group memberships, role assignments, lifecycle events (join/move/leave).
**Mandatory Standards:** SAML 2.0, OpenID Connect (OIDC), SCIM 2.0, eduGAIN federation metadata, WebAuthn/FIDO2.
**Recommended Components:** Evolveum midPoint (IGA), SATOSA + SimpleSAMLphp (federation gateway), OpenXPKI (PKI), Keycloak or equivalent (OIDC broker).

#### 4.1 What Layer 1 Owns

Layer 1 is the authoritative source for: the existence of a person in the institution's digital estate; their current affiliations (student, staff, guest, alumni, research associate); their roles within those affiliations; their authentication credentials and MFA configuration; their attribute profile for release to service providers; and the complete lifecycle history of their identity (when they joined, how their roles changed, when they left).

Layer 1 receives its authoritative data from two upstream sources: the HR system (for staff) and the student admissions and enrolment system (for students). These are the systems of record. Layer 1 does not invent identity data — it reflects and governs what those systems assert.

#### 4.2 The Joiner-Mover-Leaver Model

The Joiner-Mover-Leaver (JML) model defines how identity lifecycle events are handled. Every event in a person's affiliation — admission, enrolment, programme transfer, placement period, graduation, employment start, role change, leave of absence, employment end — must trigger a defined set of identity actions automatically. The IGA system is the enforcement point for this model.

| Event | Identity Action | Platform Consequence |
|---|---|---|
| Student admitted | Account created, birthright access provisioned (LMS, email, collaboration, library) | Student can authenticate immediately; all standard services available within 24 hours of admission event |
| Student enrols in programme | Programme-specific roles assigned; LMS course groups provisioned; study programme metadata associated with identity | LMS shows correct courses; student data correct in reporting; EWP mobility assertions correct |
| Staff member joins | Account created, role-based access provisioned, MFA enrolled, department group assigned | Email, collaboration, departmental systems and administrative tools available on Day 1 |
| Role change (promotion, transfer) | Old role permissions removed, new role permissions applied; access reconciliation run | Access reflects current role within one working day; old access does not persist |
| Student on placement / exchange | Affiliation status updated; EWP assertions updated; access scope adjusted | Partner institution can verify student status via eduGAIN; access to home institution systems maintained at appropriate scope |
| Student graduates | Academic record locked; credential issuance triggered; account transitioned to alumni status | Degree credential issued and signed; alumni access profile activated; student account permissions removed |
| Staff member leaves | Account deprovision triggered; access removed within defined SLA; account archived for audit retention period | All access removed; no orphaned accounts; audit log retained per retention policy |
| Guest access granted | Time-limited, scoped account created with explicit expiry date and minimum necessary access | Guest can access specified services; account auto-expires; no manual deprovisioning required |

#### 4.3 Federation and External Identity

The federation gateway is the institution's interface to Zone C. It translates between the institution's internal identity model and the external federation standards (SAML 2.0 for eduGAIN, OIDC for modern service providers). The federation gateway enforces the institution's attribute release policy — determining which attributes are shared with which service providers and under what conditions.

All external identity assertions — from partner institutions via eduGAIN, from the European Student Card infrastructure, from eIDAS-based services — are validated by the federation gateway before they are accepted as authoritative. The gateway applies trust rules defined by the national federation and eduGAIN metadata. No external identity assertion bypasses the gateway and reaches Zone A systems directly.

#### 4.4 Privileged Access Management

Administrative accounts — those with access to Zone A systems, to the API gateway configuration, to the IGA system itself, to cryptographic key material — require privileged access management separate from standard user accounts. Requirements: separate account identity from daily-use account; MFA enforced without exception; session recording for audit; time-limited privilege elevation for specific tasks; regular recertification of privileged roles (minimum annually); and automated alert on anomalous privileged access patterns.

### 5. Layer 2: Credentialing and Student Records

**Data Owner:** Credentialing service (Zone A). Grades are certified events owned by the learner; the institution's archive is the authoritative witness but not the controlling party.
**Exposes via API:** Credential issuance events (ELM format, signed), transcript data (EMREX/ELMO format), verification endpoints (cryptographic, no live DB lookup required), export to Europass/wallet.
**Mandatory Standards:** ELM v3 (European Learning Model), EDCI (European Digital Credentials Infrastructure), EMREX/ELMO, Open Badges 3.0, eIDAS qualified electronic signatures, W3C Verifiable Credentials.
**Recommended Components:** Europass Digital Credentials Infrastructure (EDCI), Open Badges compliant issuer, EMREX Node, institutional PKI (from Layer 1) for signing.

#### 5.1 The Learner Ownership Architecture

This layer implements the Manifesto's commitment to learner ownership of credentials. The architectural model is: a grade is not a database record that an institution controls — it is a certified event that the institution witnessed and sealed. Once sealed, it cannot be altered by any party, including the issuing institution. The student holds the portable representation; the institution archives the sealed copy as an immutable record.

> **The Certified Event Model**
>
> When an assessment outcome is formally awarded (a grade, a credit, a qualification, a micro-credential), the following sequence occurs:
>
> 1. The Process layer (Layer 3) records the assessment outcome in the campus management system with the relevant academic authority's approval.
> 2. Layer 2 receives a credential issuance trigger via the API gateway, including: the student's identity (from Layer 1), the assessment metadata (learning outcomes, ECTS volume, date, awarding body), and the outcome.
> 3. Layer 2 formats the credential in ELM v3 format, applies the institution's qualified electronic signature via the PKI service (Layer 1), and assigns a unique, persistent credential identifier.
> 4. The signed credential is archived in the institution's immutable record store (Zone A). This archive copy cannot be modified — only a revocation record can be added.
> 5. The signed credential is delivered to the student via their chosen channel: Europass Digital Credentials, European Digital Identity Wallet, direct download, or institutional credential wallet.
> 6. The verification endpoint is published: any third party can verify the credential cryptographically without contacting the issuing institution's live systems.
>
> The institution retains no ability to alter the credential after issuance. If an error is discovered, the original credential is formally revoked (with a documented reason), and a corrected credential is issued and linked to the revocation record. Both the revoked and corrected credentials are permanently archived.

#### 5.2 Credential Granularity

The credentialing layer applies the learner ownership model at three levels of granularity. The appropriate level for each type of achievement is determined by the academic governance process; the architecture supports all three:

**Qualification credentials.** Full degrees, diplomas and certificates — the traditional award. Issued at graduation or programme completion. Already supported by the Europass EDCI infrastructure.

**Module and credit credentials.** Individual module completions with credit volume (ECTS), learning outcomes and grade. Issued at the end of each assessment period. Enables cross-institution credit recognition and supports the stackable qualification model.

**Micro-credentials.** Short, focused learning achievements conforming to the EU Council Recommendation on micro-credentials (2022). Include learning outcomes, volume indicator, quality assurance reference, and ESCO-mapped competences. The architecture supports issuance and verification of micro-credentials to the same standard as full qualifications.

#### 5.3 ESCO Integration

All credentials issued at module and micro-credential level should include ESCO (European Skills, Competences, Qualifications and Occupations) mappings of the learning outcomes, in addition to the institution's own learning outcome descriptions. ESCO mappings are maintained by a semantic mapping service that connects the institution's programme and module data (from Layer 3) to the ESCO taxonomy. This mapping is maintained by academic staff responsible for curriculum design and validated through the quality assurance process.

ESCO mapping enables employer-facing and cross-institution interpretability of credentials — a hiring manager or a partner institution can understand what a graduate knows and can do in a vocabulary that is independent of the issuing institution's internal terminology.

### 6. Layer 3: Process and Academic Systems

**Data Owner:** Campus management system owns student process data (admissions, enrolment, examination status, degree audit). Administrative workflow system owns committee decisions and process records. Neither system owns identity (Layer 1) or certified credentials (Layer 2).
**Exposes via API:** Student status (enrolment, programme, standing), assessment outcomes (pre-certification), study programme data, mobility records (EWP format), administrative decisions and workflow states.
**Mandatory Standards:** EWP v3+ (Erasmus Without Paper), LTI Advantage (for LMS integration), IMS QTI (assessment), REST/JSON over HTTPS for all API surfaces.
**Recommended Components:** HISinOne or equivalent campus management system, AI-augmented administrative workflow system (see Domain Specification 3e), EWP connector service.

#### 6.1 Campus Management as a Service, Not a Centre

This layer contains what is conventionally called the Campus Management System (CMS). The critical architectural distinction from conventional CMS deployment is that the campus management function operates as a service within the platform — it is one provider of process data among several — not as the centre of gravity around which everything else is organised.

The campus management service receives identity data from Layer 1 (it does not manage its own user store), sends certified assessment outcomes to Layer 2 (it does not issue credentials itself), exposes its process data to the API gateway (Layer 4) rather than to other applications directly, and participates in the EWP mobility network through a connector service rather than through native EWP implementation.

This service model means that if the campus management product is replaced — which, given the typical 7–10 year product lifecycle of CMS systems, will happen at least once per generation — the impact is bounded to Layer 3. The identity layer, the credentialing layer, the integration layer and the experience layer are unaffected, because they depend on API contracts, not on the specific product.

#### 6.2 Administrative Process Digitalisation and AI Augmentation

Administrative processes — committee governance, decision workflows, reporting, archiving — represent one of the most significant opportunities for both digital standardisation and AI augmentation in higher education. They are also one of the most consistently neglected areas: institutions have typically invested in student-facing and academic systems while leaving administrative processes to run on email chains, shared drives and tools with poor adoption rates.

This layer includes the administrative workflow infrastructure that manages: committee meetings (agenda management, discussion documentation, decision recording, vote capture, minutes generation); decision workflows (routing decisions to the appropriate next governance stage, attaching required supporting documents, tracking status, enforcing deadlines); discussion summaries (AI-assisted generation of structured summaries from meeting records, with human review and approval before distribution); archive and access rights (automatic archiving of finalised decisions with appropriate retention periods and access controls based on the sensitivity classification of the decision type); and reporting (aggregated, anonymised reporting on institutional governance processes for quality assurance and accreditation purposes).

The AI augmentation of these processes is discussed in depth in Document 3e (Administration Systems Domain Specification). The architectural principle here is that AI tools in this layer operate on process data, not on personal data from Layers 1 or 2. They assist with summarisation, routing and classification; they do not make decisions that substitute for human governance authority.

#### 6.3 EWP Integration Architecture

Erasmus Without Paper (EWP) integration is a mandatory component of Layer 3 for any institution participating in Erasmus+ mobility. The EWP connector is a discrete service that: reads outgoing and incoming mobility records from the campus management system via the API gateway; translates them into EWP API v3+ format and registers them with the EWP Registry; receives EWP API calls from partner institutions and routes them to the campus management system via the API gateway; and manages the Learning Agreement workflow (nomination, approval, changes, final transcript) in EWP-compliant format.

The EWP connector is a separate service, not embedded in the campus management product. This separation means that when EWP releases a new API version, only the connector needs to be updated. The campus management system is unaffected. This separation is the architectural lesson from institutions that have embedded EWP logic directly in their CMS: each CMS upgrade becomes an EWP migration, multiplying the cost and risk of both.

### 7. Layer 4: Integration and Data

**Data Owner:** No data master authority in this layer — it is a conduit and a governance enforcement point. The data warehouse holds curated, quality-assured analytical data but is not the master of any operational data domain.
**Exposes via API:** API traffic governance (rate limiting, authentication, routing, versioning), event streams (xAPI/Caliper for learning events), ETL pipelines (raw → curated → domain marts), BI and analytics outputs.
**Mandatory Standards:** REST/JSON, xAPI (IEEE 9274.1), IMS Caliper, ODATA, OpenAPI 3.0 for all gateway API documentation.
**Recommended Components:** Gravitee (API gateway), Frends (integration platform), Kestra (workflow orchestration), Exasol or DuckDB (analytical database), object storage (Cubbit/Scality) for landing zone.

#### 7.1 The API Gateway as the Enforcement Point

The API gateway is the platform's central nervous system. Every communication between components — Layer 1 to Layer 3, Layer 3 to Layer 2, Layer 5 to any other layer — passes through the gateway. The gateway enforces: authentication (every request must carry a valid token issued by Layer 1); authorisation (the token's scopes must include the requested resource); rate limiting (protecting services from accidental or malicious overload); versioning (requests to deprecated API versions are routed to migration endpoints); and audit logging (every API call is logged with the caller identity, the resource accessed, and the timestamp).

The gateway is also the observability point for the entire platform. API traffic patterns reveal integration failures, performance bottlenecks, unusual access patterns that may indicate security events, and adoption rates for new services. The gateway log feeds the SIEM (Zone A) and the operational monitoring infrastructure (Zone B).

#### 7.2 The Learning Analytics Data Architecture

Learning analytics data flows through a three-stage pipeline that enforces the privacy principles from the Manifesto at each stage. The three stages are not optional — they are architectural requirements.

| Stage | Content | Privacy Treatment | Who Can Access |
|---|---|---|---|
| **Stage 1 — Landing** | Raw xAPI/Caliper event streams from LMS and learning tools. Timestamped, attributed to a pseudonymous identifier. | Pseudonymisation applied at ingestion — real identity replaced with a persistent pseudonym. Pseudonym-to-identity mapping stored separately in Zone A with strict access controls. | Integration platform only. No human access. Retained for configurable window (default 90 days) then deleted. |
| **Stage 2 — Curated** | Quality-assured, harmonised learning activity data. Linked to programme, module and cohort metadata (not to individual identity). | Cohort-level aggregation applied. Minimum cohort size enforced (default: n≥10) to prevent re-identification. No individual-level data in this stage. | Analytics team, institutional research office, quality assurance staff. Read-only. No export to external systems without DPIA. |
| **Stage 3 — Individual Support** | Individual-level pseudonymised data for early-warning and learning support applications. Re-linkable to identity only within Layer 1 under controlled conditions. | Pseudonymous. Access to identity linkage requires explicit governance approval and is audit-logged. Individual cannot be identified by analytics system users without Zone A authorisation. | Personal tutors (scoped to their own students, with student consent), student support services, students themselves (full access to their own data via self-service dashboard). |

#### 7.3 Master Data Domains and Ownership

The following table defines the eight master data domains and their authoritative sources. This table is the reference for all integration work: when a component needs a piece of data, the first question is "which master domain does this belong to?" and the second is "which service is the authoritative source for this domain?" The answer to the second question determines which API endpoint to call.

| Domain | Master Authority | Zone | Key Data Elements |
|---|---|---|---|
| Person / Identity | IGA system fed by HR and admissions | A | Name, date of birth, contact data, authentication credentials, MFA status |
| Organisation | HR and administrative registry | A | Departments, faculties, cost centres, external organisations |
| Role / Affiliation | IGA system (computed from HR + admissions events) | A | Student status, staff role, guest scope, alumni status, group memberships |
| Study Offering | Campus management system | A | Programmes, modules, course catalogue, ECTS values, learning outcomes, ESCO mappings |
| Teaching Event / Examination | Campus management system | A | Scheduled instances, assessment results (pre-certification), grade records |
| Research Project | Research management system | A | Project metadata, funding body, PI, team members, output records |
| Financial Object | ERP / Finance system | A | Cost centres, budget lines, purchase orders, invoices, project codes |
| Certified Credential | Credentialing service (Layer 2) | A | Signed ELM credentials, revocation records, issuance audit log |

### 8. Layer 5: Experience and Engagement

**Data Owner:** No data master authority. Experience layer components consume data from Layers 1–4; they do not own or store authoritative data.
**Exposes via API:** User session state (transient, not persisted beyond session), UI preferences (stored locally or in a lightweight preferences service), analytics events (forwarded to Layer 4).
**Mandatory Standards:** LTI Advantage (for external tool integration), OIDC (for authentication), Web Content Accessibility Guidelines (WCAG 2.1 AA minimum for all user interfaces).
**Recommended Components:** ILIAS or OpenOlat (LMS), Nextcloud + ONLYOFFICE/Collabora (collaboration), OpenTalk (video), Element/Matrix (messaging), student self-service portal (custom or procured, API-connected).

#### 8.1 The User Experience Criterion

User experience and adoption rate are first-class architectural criteria in this framework. A tool that satisfies all sovereignty and API requirements but that users abandon in favour of shadow alternatives has failed architecturally, not just commercially. The adoption rate of institutional tools is a proxy for the platform's fitness: low adoption means the platform is not serving its users, which means its data is incomplete, its security controls are bypassed, and its governance claims are hollow.

The evaluation framework ([Document 4](hei-evaluation-framework.md)) includes user experience and adoption rate as explicit assessment criteria for each tool category. Institutions are expected to measure adoption rates, conduct user satisfaction surveys, and treat persistently low adoption as a signal requiring architectural or service design response — not just a communication or training problem.

#### 8.2 Plug-and-Play Tool Integration via LTI

The Learning Tools Interoperability (LTI) Advantage standard is the mechanism through which third-party tools — specialist assessment platforms, simulation environments, laboratory tools, AI tutoring systems — integrate with the LMS without creating point-to-point dependencies. LTI enables: single sign-on (the student authenticates once to the LMS and is silently authenticated to the external tool); grade passback (assessment scores in external tools are reported back to the LMS gradebook through the Assignment and Grades service); Names and Roles Provisioning (the external tool receives course membership information without requiring its own user management); and deep linking (instructors can embed specific external tool resources directly within course content).

LTI Advantage is the architectural expression of the plug-and-play modularity principle at the experience layer. A tool that supports LTI Advantage can be connected to the LMS in hours and replaced with a different tool without any data migration, user account management or architectural change. A tool that does not support LTI Advantage requires point-to-point integration that violates Principle 2 and must be justified as an exception with a migration plan.

#### 8.3 The Student Self-Service Portal

The student self-service portal is the primary experience layer interface for students. Its architectural requirements are: it connects to Layer 1 (identity) via OIDC for authentication; it displays academic records from Layer 3 via the API gateway; it provides access to the student's own credentials from Layer 2; it shows the student's own learning analytics data from Stage 3 of the analytics pipeline; it enables the student to manage their own data rights (access requests, portability exports, consent management). The portal does not hold any authoritative data of its own.

---

## Part IV: Integration Contracts and Data Flows

### 9. Inter-Layer Data Flows

This section defines the canonical data flows between layers. These flows are the integration contracts that all components must satisfy. A component that cannot participate in these flows through standard protocols cannot be adopted under this framework.

| From | Flow Type | To | Standard / Protocol |
|---|---|---|---|
| HR System | Provisioning | Layer 1 IGA | SCIM 2.0 push on create/update/delete events |
| Admissions System | Provisioning | Layer 1 IGA | SCIM 2.0 or REST webhook on enrolment events |
| Layer 1 IGA | Attribute assertion | Layer 3 Campus Mgmt | LDAP read (internal) or SCIM pull for user lookup |
| Layer 1 Federation GW | SSO assertion | All Zone B services | SAML 2.0 (for legacy SP), OIDC (for modern SP) |
| Layer 1 Federation GW | Federated assertion | Zone C eduGAIN | SAML 2.0, eduGAIN metadata exchange |
| Layer 3 Campus Mgmt | Assessment outcome | Layer 2 Credentialing | REST/JSON event via API gateway — trigger credential issuance |
| Layer 2 Credentialing | Signed credential | Student (held by learner) | ELM v3 / EDCI format, delivered via Europass API or wallet |
| Layer 2 Credentialing | Transcript data | Partner institutions | EMREX/ELMO protocol, via EWP connector or direct EMREX node |
| Layer 3 Campus Mgmt | Mobility records | Zone C EWP | EWP API v3+, via EWP connector service |
| Layer 5 LMS | Learning events | Layer 4 Analytics Landing | xAPI statements (IEEE 9274.1) or IMS Caliper events |
| Layer 4 Analytics | Pseudonymised cohort data | Curated DWH | ETL pipeline, pseudonymisation applied before transfer |
| Layer 4 DWH | Anonymised aggregates | Layer 5 BI / Dashboards | ODATA or REST/JSON, no individual-level data |
| Layer 4 Analytics Stage 3 | Pseudonymised individual data | Layer 5 Student Portal | REST/JSON via API gateway, scoped to authenticated student's own data |
| All layers | Security events | Zone A SIEM | Syslog, CEF or API push to SIEM ingest endpoint |

### 10. European Standard Integration Points

The following table maps each major European interoperability standard to the layer at which it operates, the component responsible for implementing it, and the consequence of non-implementation. This table is the reference for European interoperability compliance assessment.

| Standard | Layer | Responsible Component | Non-implementation Consequence |
|---|---|---|---|
| eduGAIN | Layer 1 | Federation gateway | Institution cannot participate in cross-European SSO. Students and staff cannot access partner institution services. Research network access is compromised. |
| SAML 2.0 | Layer 1 | Federation gateway | All legacy service providers (including most research tools and many HE-specific applications) cannot participate in SSO. |
| OIDC | Layer 1 | OIDC broker (e.g. Keycloak) | Modern applications and API clients cannot authenticate. Mobile apps and REST API clients are excluded. |
| EWP v3+ | Layer 3 | EWP connector service | Erasmus+ mobility processes must be conducted on paper or through manual data entry. Learning agreements and transcripts cannot be exchanged electronically with partner institutions. |
| EMREX/ELMO | Layer 2 | EMREX node | Electronic transcript exchange with partner institutions in 20+ European countries is unavailable. Incoming credit recognition is manual. |
| ELM v3 / EDCI | Layer 2 | Credentialing service | Credentials cannot be issued in the European standard format. Students cannot add qualifications to the Europass Digital CV. Credentials are not verifiable by European employers without contacting the institution directly. |
| Open Badges 3.0 | Layer 2 | Credentialing service | Micro-credentials and achievement badges cannot be issued in a portable, internationally recognised format. |
| LTI Advantage | Layer 5 | LMS | Third-party learning tools cannot be integrated without point-to-point connections. Tool diversity is limited to what the LMS vendor provides natively. |
| xAPI / IEEE 9274.1 | Layer 4 | Analytics landing service | Learning events from multiple tools cannot be collected in a standard format. Cross-tool learning analytics is unavailable. |
| SCIM 2.0 | Layer 1 | IGA system | Automated user provisioning to Zone B services requires custom integration per application. JML model cannot be enforced automatically. |
| OAI-PMH | Layer 2 | Repository / CRIS | Research outputs and institutional publications cannot be harvested by European research aggregators (OpenAIRE, BASE, EuroPMC). |
| eIDAS / Wallet | Layer 2 | Credentialing service | Credentials cannot be accepted into the European Digital Identity Wallet. Institution cannot participate in eIDAS-based qualified signature workflows. |

### 11. API Contract Requirements

Every API endpoint exposed through the API gateway must satisfy the following minimum requirements. These requirements apply to all layers and all components — institutional, commercial and open-source equally.

#### 11.1 Documentation Requirements

- OpenAPI 3.0 specification published and maintained in the API gateway's developer portal
- Human-readable description of each endpoint's purpose, inputs, outputs and error conditions
- Version history: changes between versions documented, breaking changes flagged with migration guidance
- Authentication requirements: which token scopes are required for each endpoint
- Data catalogue entry: which master data domain(s) are accessed or modified by each endpoint

#### 11.2 Security Requirements

- All API traffic over HTTPS with TLS 1.3 minimum
- Authentication via OAuth 2.0 / OIDC tokens issued by Layer 1. No API keys accepted for personal data endpoints
- Token scopes must be as narrow as possible — principle of least privilege enforced at the gateway
- Rate limiting applied to all endpoints. Limits documented. Clients receive HTTP 429 with Retry-After header, not silent failure
- Input validation: all inputs validated against documented schema. Malformed requests return HTTP 400 with structured error

#### 11.3 Data Requirements

- Personal data minimisation: endpoints return only the fields the requesting client is authorised to see. Field-level access control enforced at the gateway
- Pseudonymisation: any endpoint that returns personal data for analytics purposes returns pseudonymised identifiers, not real identities
- Pagination: all list endpoints support cursor-based pagination. No unbounded queries that return entire datasets
- Audit logging: all read and write operations on personal data are logged to the SIEM with caller identity and timestamp

#### 11.4 Exit and Portability Requirements

- Data export endpoint: every component that holds institutional data must expose a bulk export endpoint in an open format (JSON-LD, CSV with documented schema, or domain-specific open standard)
- Migration API documentation: the export endpoint documentation must include sufficient information for a competent developer to import the data into a replacement system
- Export must be executable by the institution without vendor assistance within 5 business days of request
- No proprietary binary formats for primary data storage. Standards-based formats only.

---

## Part V: Transition and Governance

### 12. Transitioning from Legacy Architecture

Most institutions adopting this framework will be transitioning from a landscape that includes monolithic systems, point-to-point integrations and shadow IT. The transition strategy must be realistic about this starting point and must avoid the two most common failure modes: the "big bang" cutover that attempts to replace everything at once, and the "parallel universe" approach that builds a new architecture alongside the old one without ever decommissioning the old.

#### 12.1 The Strangulation Pattern

The recommended migration approach is the strangulation pattern: legacy systems are progressively encircled by the new architecture rather than immediately replaced. The sequence is:

1. **Connect legacy systems to the API gateway.** Every legacy system that cannot expose a native API gets an adapter layer — a thin service that wraps the legacy system's existing interface and exposes it as a standard REST API through the gateway. This is not a permanent solution, but it brings legacy systems under API governance immediately, stopping the accumulation of new point-to-point connections.
2. **Connect legacy systems to the identity layer.** Every legacy system that manages its own user store is connected to the IGA system for user provisioning. The legacy system continues to operate but stops managing identity autonomously.
3. **Stabilise and test the identity layer.** Before any service migration, verify that the JML model is working correctly, that the federation gateway is participating in eduGAIN, and that MFA is enforced for all administrative accounts.
4. **Migrate collaboration and productivity services.** These are typically the easiest first migrations because they have clear European sovereign alternatives (Nextcloud, Open-Xchange, OpenTalk) and because their data is the least sensitive and most portable.
5. **Implement the credentialing layer.** This can proceed independently of the campus management migration and delivers immediate value (student-held credentials, EMREX integration, Europass connection) without requiring any change to existing student records systems.
6. **Define campus management API contracts.** Before the campus management product is replaced, define the full API contracts for Layer 3. These contracts become the specification for either a new procurement or a consortium contribution.
7. **Migrate or replace the campus management service against the defined contracts.** The rest of the platform is unaffected because it depends on the contracts, not on the specific product.
8. **Decommission legacy systems.** Once a legacy system's functions have been fully migrated and the new system has been validated in production, the legacy system is decommissioned and its infrastructure freed.

#### 12.2 The Five Migration Patterns

For each legacy system, one of five migration patterns is appropriate depending on the system's criticality, the availability of replacement components, and the data migration complexity:

**Rehost with API wrapper.** The legacy system continues to run on existing infrastructure but receives an API adapter that exposes its data through the gateway. Appropriate for systems with acceptable functional capability but no native API. Temporary measure with a defined exit date.

**Replatform to sovereign infrastructure.** The legacy system's data and configuration are migrated to sovereign infrastructure without changing the application. Appropriate for systems that are architecturally sound but hosted on non-sovereign infrastructure.

**Parallel operation with synchronisation.** Old and new systems run in parallel with automated data synchronisation during a defined transition period. Appropriate for high-risk migrations where rollback capability is essential. The synchronisation window must have a defined end date.

**Domain-wave replacement.** The legacy system is replaced function by function, domain by domain. Appropriate for monolithic systems where different functional domains can be replaced at different speeds. The API contracts define the boundaries between completed and in-progress domains.

**Archive and decommission.** The legacy system has no active users but data must be retained for legal or audit reasons. Data is migrated to the archiving layer in an open format, the operational system is shut down, and the archived data is accessible through the records management service.

#### 12.3 Governance of the Transition

The transition programme requires three governance mechanisms that do not exist in typical IT project governance:

**Architecture Decision Records (ADRs).** Every significant architectural decision — which product satisfies which API contract, which migration pattern is applied to which legacy system, which European standard version is implemented — is documented in a structured ADR. An ADR records: the decision, the alternatives considered, the rationale for the choice, and the conditions under which the decision should be revisited. ADRs are maintained in a version-controlled repository and reviewed annually.

**Integration freeze for new point-to-point connections.** From the moment this framework is adopted, no new point-to-point integrations between any two platform components are permitted without an architecture review. Every new integration must be routed through the API gateway. Violations are reported to the governance committee. This freeze is the single most important transition governance commitment because it stops the accumulation of the technical debt that made the transition necessary.

**Legacy system decommission register.** Every legacy system that is being retained during the transition is listed in a decommission register with: the current function it serves, the new component that will replace it, the migration pattern to be applied, the target decommission date, and the data migration plan. This register is reviewed quarterly by the governance committee. Systems without a decommission plan are not permitted on the register indefinitely.

### 13. Governance of the Architecture

This Architecture Reference Model is a living document. It will be revised as European standards evolve, as new components enter the recommended list, and as the experience of implementing institutions generates lessons that require architectural responses. The governance of this model is the responsibility of the European Higher Education Digital Alliance.

#### 13.1 Institutional Architecture Governance

Each signatory institution maintains the following governance functions for its own platform implementation:

**Enterprise Architect.** Responsible for maintaining the institution's implementation of this reference model, for reviewing all new procurement decisions against the architecture principles, for maintaining the Architecture Decision Record repository, and for representing the institution's architecture experience in European alliance governance.

**Architecture Review Board.** Convened quarterly (or more frequently when significant decisions are pending). Membership includes the Enterprise Architect, CISO, Data Protection Officer, and representatives from the major functional domains (academic, administrative, research). Responsible for approving new component adoptions, architecture exceptions, and updates to the transition programme.

**Annual Architecture Assessment.** Using the Evaluation Framework ([Document 4](hei-evaluation-framework.md)), each institution conducts an annual self-assessment of its implementation against this reference model. The assessment is shared with the European alliance coordination body and used to identify areas where alliance support is needed.

#### 13.2 Alliance-Level Architecture Governance

The Alliance maintains this reference model through a transparent governance process:

**Versioning.** This model uses semantic versioning. Minor versions (1.1, 1.2) reflect updates to recommended components, corrections and clarifications. Major versions (2.0) reflect changes to the fundamental architecture principles or zone model and require a full governance review with a defined transition period for institutions already implementing the previous version.

**Contribution.** Any signatory institution may propose amendments to this model by submitting an Architecture Change Proposal (ACP) to the Alliance technical committee. ACPs are reviewed against the Manifesto principles, against the implementation experience of member institutions, and against the current state of European standards. Accepted changes are incorporated in the next minor version.

**Conflict resolution.** Where implementation experience reveals that a principle or requirement in this model is unworkable in specific institutional contexts, the institution documents the conflict in an Architecture Decision Record and requests a formal exception from the Alliance governance committee. Exceptions are time-limited. Systemic exceptions — where multiple institutions face the same conflict — trigger an Architecture Change Proposal.

---

## Annex A: Recommended European Components by Layer

The following table lists the recommended European-origin or open-source components for each architectural layer. "European-origin" means the project or company is headquartered in a European country or Switzerland. "Open-source with sovereign deployment" means the software is open-source and can be self-hosted on European sovereign infrastructure independently of the originating company. All listed components have production deployments at European higher education institutions.

| Layer | Function | Component | Sovereignty Basis |
|---|---|---|---|
| L1 | IGA / Identity Governance | Evolveum midPoint | Open-source (AGPL), Czech-origin, self-hosted, production at multiple European universities |
| L1 | Federation Gateway | SATOSA + SimpleSAMLphp | Open-source (Apache/LGPL), Nordic-origin, used by SURF, SWITCH and 50+ national federations |
| L1 | OIDC Broker | Keycloak | Open-source (Apache), Red Hat-origin but fully self-hostable; or Zitadel (Swiss-origin) |
| L1 | PKI / Certificate Authority | OpenXPKI | Open-source (Apache), German-origin, self-hosted |
| L1 | Cross-institutional Federation | eduGAIN | GÉANT-operated European federation infrastructure |
| L2 | Credential Issuance | Europass EDCI + ELM toolkit | EU Commission-operated; open specification; institution-operated signing via own PKI |
| L2 | Transcript Exchange | EMREX Node | Open-source, Nordic/European consortium, self-hosted |
| L2 | Open Badges | Open Badges 3.0 compliant issuer | Multiple open-source options; standard is vendor-neutral |
| L3 | Campus Management | HISinOne | German-origin, widely deployed in DACH; consortium development model via HIS-HE |
| L3 | EWP Connector | EWP reference implementation | Open-source, operated by EWP consortium; self-hosted connector |
| L3 | Admin Workflow + AI | Nextcloud + AI assistant module, or open-source BPM (Camunda) | Nextcloud: German-origin open-source. Camunda: German-origin, open-source core |
| L4 | API Gateway | Gravitee | French-origin, open-source core (Apache), European headquarters |
| L4 | Integration Platform | Frends | Finnish-origin, commercial with European data residency |
| L4 | Workflow Orchestration | Kestra | French-origin, open-source (Apache) |
| L4 | Analytical Database | Exasol | German-origin; or DuckDB (open-source, MIT licence, Dutch-origin) |
| L4 | Object Storage | Cubbit (Italian) or Scality (French) | European-origin, European data residency, S3-compatible |
| L4 | Backup | Bareos (German-origin open-source) or SEP sesam (German-origin commercial) | Self-hosted, no foreign cloud dependency |
| L5 | LMS | ILIAS | German-origin, open-source (GPL), LTI Advantage certified |
| L5 | LMS (alternative) | OpenOlat | Swiss-origin, open-source (Apache), LTI Advantage certified |
| L5 | LMS (open-source, non-European but sovereign-deployable) | Moodle | Australian-origin, GPL, fully self-hostable on European sovereign infrastructure. Satisfies sovereignty requirements when self-hosted; does not satisfy them when hosted by a US commercial cloud provider. |
| L5 | Collaboration / Files | Nextcloud + ONLYOFFICE | German-origin (Nextcloud), Russian-origin but EU-incorporated and self-hostable (ONLYOFFICE). Nextcloud is the preferred file layer. |
| L5 | Video Conferencing | OpenTalk | German-origin, open-source core, on-premises deployable |
| L5 | Messaging / Chat | Element (Matrix protocol) | UK-origin, open-source (Apache), federated protocol; or Wire (Swiss-origin) |
| L5 | Email / Calendar | Open-Xchange | German-origin, open-source core, widely deployed in European education |
| L5 | Endpoint Management | opsi (open-source) or baramundi (commercial) | Both German-origin; baramundi is the stronger commercial DACH option |

## Annex B: Architecture Principle Compliance Checklist

This checklist is intended for use in quarterly architecture reviews and in the annual assessment. For each principle, the institution rates itself: Compliant, Partially Compliant (with documented exception), or Non-Compliant (with remediation plan).

| Principle / Check | Evidence Required |
|---|---|
| **P1:** Identity layer operational before any other service in production | IGA system provisioning from HR and admissions; federation gateway connected to national federation and eduGAIN; JML model automated; MFA enforced for admin accounts |
| **P2:** No point-to-point integrations | Integration register showing all connections pass through API gateway; zero open exceptions without documented decommission date |
| **P3:** All API contracts in open standards | API gateway developer portal contains OpenAPI 3.0 specs for all endpoints; no proprietary integration protocols in use |
| **P4:** Data master ownership documented | Master data domain register complete; every data element has a documented authoritative source; no orphaned data copies |
| **P5:** Exit capability demonstrated | Migration path documented for each component; bulk export endpoint tested for each data-holding component; export executable without vendor within 5 business days |
| **P6:** DPIA complete for all components | DPIA register complete; no component processing personal data without a current DPIA; DPO sign-off on all DPIAs |
| **Zone A:** Sovereign infrastructure verified | Contractual documentation of European data residency, sub-processor list, audit rights; ISO 27001 certification of hosting |
| **Zone B:** European sovereign cloud | Cloud provider has European data residency, ISO 27017/27018 certification; sub-processor list published |
| **Zone C:** eduGAIN participation | Institution listed in national federation metadata; eduGAIN participation confirmed; attribute release policy published |
| **EWP:** Full API participation | EWP registry confirms institution supports outgoing and incoming mobility APIs at current version |
| **ELM/EDCI:** Credential issuance live | At least one credential type (e.g. diploma supplement) issued in ELM v3 format and verifiable via EDCI |
| **EMREX:** Node operational | EMREX node registered and operational; electronic transcript exchange tested with at least one partner institution |
| **Analytics:** Three-stage pipeline enforced | Pseudonymisation at ingestion confirmed; cohort size minimum enforced; individual stage access controls audited |
| **Student data rights:** Self-service dashboard | Student data dashboard accessible; plain-language data use explanation published; correction/contest process documented and tested |

*(This checklist has empty "Status" and "Target" columns in the source, intended to be filled in per-institution during an actual self-assessment — reproduced here as evidence requirements only, since the OUG has not yet conducted this assessment. See [known-gaps.md](known-gaps.md) for the note on scoring the live New Study platform against this checklist and against Document 4's fuller maturity ladder.)*

---

*Open University of Germany · Architecture Reference Model · Document 2 of the Digital Alliance Framework · Version 1.0 · May 2026*
