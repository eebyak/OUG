---
layout: page
title: "Maturity Scorecard: CampusCircle / newstudy — Working Template"
---

*A hand-completable instrument, structured directly against [Document 4: HEI IT Architecture Evaluation Framework](hei-evaluation-framework.md)*

> **Status:** Working template — partially pre-filled from public evidence, not a completed assessment.
> **Subject:** `campuscircle.de` / `newstudy.campuscircle.de` ("TIA Beta") — the live module catalogue and collaboration platform referenced throughout this domain.
> **Assessed by:** *(name)* · **Date started:** *(date)* · **Date completed:** *(date)*

## ⚠ Read This Before Filling In the Rest

Two things worth knowing before treating this scorecard as reflecting the OUG's own maturity.

**First, what this platform actually is.** Its own Datenschutzerklärung and Barrierefreiheitserklärung both state, explicitly and repeatedly: this is a *"semi-official pilot project ('TIA Beta')"* in the environment of DHBW Mosbach — **"not an official DHBW system"** — with formal institutional governance *"still pending"* between the operator and DHBW. The controller entity name field in the privacy policy is a literal unfilled placeholder (`[[ENTITY_NAME]]`). No Data Protection Officer is finally named. This means Section 1 (Architecture Foundations) of D4 is very likely to score near zero not because the platform is poorly built, but because the institutional governance apparatus D4 assumes exists (a named Enterprise Architect, a quarterly Architecture Review Board, an ADR repository) is a category of thing a beta pilot by its nature doesn't yet have. **Score what's there; don't read a low Section 1 score as a verdict on the engineering.**

**Second, what "pre-filled" means here.** Two rows of evidence went into the pre-fills below: the platform's Datenschutzerklärung (privacy policy) and Barrierefreiheitserklärung (accessibility statement) — both unusually candid, self-critical documents, not marketing copy. Everything pre-filled is cited to a specific section of one of those two pages. Everything else is genuinely unknown from outside — the module catalogue itself never rendered for me (JS-heavy SPA, static fetch only returns "loading..."), and nothing about internal governance, audit logs, SLA performance, or ARB minutes is ever going to be on a public page regardless of actual maturity. Where I have no evidence, the row says exactly that — it is not scored as a 0, because absence of public evidence is not the same claim as absence of the capability.

**How to complete this:** for every row marked *Not assessed — requires internal evidence*, someone with actual access (the platform's operators, or DHBW/OUG governance once the institutional relationship is clarified) fills in the Level and Evidence columns. Rows already pre-filled can be corrected if the public evidence turns out to be stale or wrong — the citation is there so you can check.

---

## Section 1: Architecture Foundations

### 1.1 Compliance Gates

| ID | Check | Status | Evidence | Notes |
|---|---|---|---|---|
| **AF-G1** | Named Enterprise Architect with documented responsibilities | ☐ Pass ☐ Fail ☐ Not assessed | *(no public evidence — likely Fail given beta/pilot status; confirm internally)* | |
| **AF-G2** | Architecture Review Board meets ≥quarterly, decision log maintained | ☐ Pass ☐ Fail ☐ Not assessed | *(no public evidence)* | |
| **AF-G3** | ADR repository, ≥5 decisions in last 12 months | ☐ Pass ☐ Fail ☐ Not assessed | *(no public evidence)* | |
| **AF-G4** | Legacy system decommission register with target dates | ☐ Pass ☐ Fail ☐ Not assessed | *(no public evidence — likely N/A, no legacy migration in scope for a new pilot)* | |
| **AF-G5** | DPIA completed for all personal-data systems, DPO-reviewed | ☐ Pass ☑ **Fail** ☐ Not assessed | Datenschutzerklärung §7: *"eine ... Datenschutz-Folgenabschätzung (Art. 35 DSGVO) für risikoreiche Verarbeitungen (Chat, Video) befinden sich in Arbeit"* — DPIA explicitly **in progress, not complete** | Direct evidence of Fail, not absence of evidence |

### 1.2 Maturity Assessment

| Criterion | Level (0–5) | Evidence | Notes |
|---|---|---|---|
| Architecture principles documented and applied | ☐ Not assessed | *(no public evidence)* | |
| API gateway operational | ☐ Not assessed | *(no public evidence — architecture is described as a set of self-hosted services, not through a documented gateway pattern)* | |
| Service catalogue completeness | ☐ Not assessed | *(no public evidence)* | |
| Exit capability | ☐ Not assessed | Data portability (Art. 20) is partly supported via the built-in PDF export — see Section 5 (Credentialing) note. Not the same as a tested bulk export/migration path. | Partial positive signal only |
| Security baseline (DPIA + ISMS) | ☑ **Level 1 (Initial)** | Datenschutzerklärung §7: DPIA "in Arbeit" (in progress); RoPA "in Arbeit"; no ISO/IEC 27001 mentioned anywhere | |

---

## Section 2: Identity and Federation

### 2.1 Compliance Gates

| ID | Check | Status | Evidence | Notes |
|---|---|---|---|---|
| **ID-G1** | IGA system provisioning from HR and admissions as authoritative sources | ☐ Pass ☑ **Fail** ☐ Not assessed | Datenschutzerklärung §4.1: Keycloak self-registration with email-domain allowlist (DHBW domains + `campuscircle.de` + common providers) — **not** fed from an institutional HR/admissions system | |
| **ID-G2** | National federation + eduGAIN participation | ☐ Pass ☑ **Fail** ☐ Not assessed | No mention anywhere in either legal page. Note: Matrix-level federation is explicitly *disabled* (§4.2) — a different, narrower thing than eduGAIN, but worth not conflating | |
| **ID-G3** | MFA enforced for all administrative accounts | ☐ Pass ☑ **Fail** ☐ Not assessed | Datenschutzerklärung §4.1: WebAuthn/passkey or TOTP is listed as *optional* ("ggf.") — not enforced | Applies to what's visible (student/user accounts); admin-account posture specifically not described |
| **ID-G4** | JML SLA documented and met: joiners 4h, leavers 2h | ☐ Pass ☑ **Fail** ☐ Not assessed | No JML process described at all; account lifecycle is self-service registration and self-service deletion (§4.1), not an institutionally-triggered lifecycle | |
| **ID-G5** | Attribute release policy documented, DPO-approved, enforced | ☐ Pass ☐ Fail ☐ Not assessed | *(no public evidence)* | |

### 2.2 Maturity Assessment

| Criterion | Level (0–5) | Evidence | Notes |
|---|---|---|---|
| IGA completeness | ☑ **Level 0–1** | Self-registration model, not IGA-provisioned (§4.1) | |
| Federation breadth | ☑ **Level 0–1** | Matrix federation explicitly disabled (§4.2); no eduGAIN/EWP/ESI/EMREX mentioned | |
| JML lifecycle automation | ☑ **Level 0** | No JML model described; self-service only | |
| Privileged access management | ☐ Not assessed | *(no public evidence on admin/privileged accounts specifically)* | |
| MFA coverage | ☑ **Level 1** | Optional WebAuthn/TOTP for user accounts (§4.1); no data on admin account MFA | |

---

## Section 3: Learning Systems (Domain 3a)

### 3.1 Compliance Gates

| ID | Check | Status | Evidence | Notes |
|---|---|---|---|---|
| **LS-G1** | LMS hosted on European sovereign or on-prem infrastructure | ☑ **Pass** ☐ Fail ☐ Not assessed | Datenschutzerklärung §5: hosting via Hetzner Online GmbH, Germany (EU); Inline GmbH, Germany | DPAs with both **not yet fully executed** — see note below |
| **LS-G2** | LMS authenticates via OIDC; zero local student/staff accounts | ☐ Pass ☐ Fail ☐ Not assessed | Keycloak/OIDC is used (§4.1) but "newstudy" isn't a conventional LMS in the D3a sense — module catalogue/progress tracker. Applicability itself needs internal confirmation | |
| **LS-G3** | LTI Advantage (LTI 1.3 + AGS) in production | ☐ Pass ☐ Fail ☐ Not assessed | *(no public evidence — no third-party tool integration described anywhere)* | |
| **LS-G4** | WCAG 2.1 AA compliance documented, current VPAT available | ☐ Pass ☑ **Fail** ☐ Not assessed | Barrierefreiheitserklärung §2: *"partially conformant"*, based on **internal self-assessment only** — explicitly *"no full external BITV audit (e.g. BITV-Test, VPAT) has taken place yet"* | |
| **LS-G5** | Vendor analytics data sharing blocked without DPIA approval | ☐ Pass ☐ Fail ☐ Not assessed | *(no evidence of vendor analytics sharing found; also no DPIA yet per AF-G5, so this gate may not be meaningfully assessable until DPIA exists)* | |

### 3.2 Maturity Assessment

| Criterion | Level (0–5) | Evidence | Notes |
|---|---|---|---|
| LMS sovereignty | ☑ **Level 2** | European hosting confirmed (Hetzner, Germany); but DPAs not yet signed and 3 non-European sub-processors in active use for front-end assets (Google reCAPTCHA/gstatic, Cloudflare CDN, OpenFreeMap — Datenschutzerklärung §5–6) | Partial credit only — hosting location good, contractual/sub-processor picture incomplete |
| LTI ecosystem breadth | ☐ Not assessed | *(no public evidence)* | |
| xAPI emission coverage | ☑ **Level 0** | The "recommendations" feature is explicitly described as simple rule-based sorting on count data (likes, enrolments, completions) — Datenschutzerklärung §3 — not xAPI/Caliper event emission | |
| Content portability | ☐ Not assessed | *(no public evidence — module catalogue content itself never rendered for me)* | |
| Adoption rate | ☐ Not assessed | *(no usage data published; this is inherently internal data)* | |
| AI governance in LMS | ☑ **Level 0–N/A** | No AI tooling described. The one automated feature (translation bot) was disabled 15 July 2026 (§4.5) — no AI disclosure framework needed if no AI is in use | Confirm whether any AI exists elsewhere in the platform not covered by these two pages |

---

## Section 4: Credentialing and Student Records (Domain 3b)

### 4.1 Compliance Gates

| ID | Check | Status | Evidence | Notes |
|---|---|---|---|---|
| **CR-G1** | ELM v3 credential issued, EDCI-verified | ☐ Pass ☑ **Fail** ☐ Not assessed | No mention anywhere of ELM, EDCI, or any credential-issuance mechanism | |
| **CR-G2** | Archive append-only and immutable | ☐ Pass ☐ Fail ☐ Not assessed | *(no public evidence; the platform's "audit-log" for admin edits (§4.4) is a different thing from an immutable credential archive)* | |
| **CR-G3** | Student credential export ≤24h, zero cost | ☐ Pass ☐ Fail ☐ Not assessed | PDF export exists for progress data (§4.4, §8) but this is not a *credential* export in the D3b sense | Likely N/A rather than Fail — the platform doesn't appear to issue credentials at all |
| **CR-G4** | EMREX Node operational | ☐ Pass ☑ **Fail** ☐ Not assessed | No mention anywhere | |
| **CR-G5** | Credential revocation policy documented and implemented | ☐ Pass ☐ Fail ☐ Not assessed | N/A if no credentials are issued | |

### 4.2 Maturity Assessment

| Criterion | Level (0–5) | Evidence | Notes |
|---|---|---|---|
| ELM credential coverage | ☑ **Level 0** | No evidence of any credential issuance | This whole domain may simply not be in scope for this specific platform — confirm whether credentialing happens elsewhere (e.g. DHBW's own systems) rather than scoring this as a platform failure |
| Offline verifiability | ☑ **Level 0 / N/A** | No credentials to verify | |
| Archive permanence | ☐ Not assessed | *(no public evidence on the "newstudy" progress/enrolment data's retention beyond account deletion — §4.4)* | |
| EMREX / transcript exchange | ☑ **Level 0** | No mention | |
| Micro-credential infrastructure | ☑ **Level 0** | No mention | |

---

## Section 5: Learning Analytics (Domain 3c)

### 5.1 Compliance Gates

| ID | Check | Status | Evidence | Notes |
|---|---|---|---|---|
| **AN-G1** | Pseudonymisation at ingestion; no real identities in analytics store | ☐ Pass ☐ Fail ☐ Not assessed | Datenschutzerklärung §3 explicitly states **no** automated decision-making/profiling under Art. 22 — the "recommendations" are simple count-based sorts, not a pseudonymised analytics pipeline at all | This gate may not apply — there doesn't appear to be a "learning analytics" system in the D3c sense to assess |
| **AN-G2** | Stage 2 cohort size minimum (n≥10) enforced | ☐ Pass ☐ Fail ☐ Not assessed | N/A if no cohort analytics exist | |
| **AN-G3** | Student data dashboard: plain-language events, correction mechanism | ☐ Pass ☐ Fail ☐ Not assessed | A progress dashboard exists (§4.4: goals, competency-radar) but its relationship to GDPR Art. 15 access-rights functionality specifically isn't described | Worth checking directly against the live product rather than the privacy policy alone |
| **AN-G4** | Stage 3 opt-out operational, doesn't affect other services | ☐ Pass ☐ Fail ☐ Not assessed | Account-level withdrawal of consent is described (§8, Art. 7(3)) but this ends *all* platform access — not a scoped opt-out from analytics alone while keeping other services | Likely Fail on the "doesn't affect other services" clause specifically — confirm |
| **AN-G5** | Early-warning model bias-tested in last 12 months | ☐ Pass ☑ **Fail / N/A** ☐ Not assessed | No early-warning model appears to exist at all — see AN-G1 note | |

### 5.2 Maturity Assessment

| Criterion | Level (0–5) | Evidence | Notes |
|---|---|---|---|
| Pipeline privacy architecture | ☑ **Level 0 / N/A** | No three-stage pipeline described; explicit statement that no Art. 22 profiling occurs | |
| Student data rights implementation | ☐ Not assessed | Progress dashboard exists but not evaluated against the specific dashboard requirements in D3 ANA-04 | Worth a direct product check |
| Early-warning system quality | ☑ **Level 0 / N/A** | No early-warning system found | |
| Analytics serving learner | ☐ Not assessed | | |
| xAPI semantic consistency | ☑ **Level 0** | No xAPI or equivalent event standard mentioned | |

---

## Section 6: Backend and Stakeholder Data (Domain 3d)

### 6.1 Compliance Gates

| ID | Check | Status | Evidence | Notes |
|---|---|---|---|---|
| **BD-G1** | ISO/IEC 27001 certified for Zone A, audit <12 months | ☐ Pass ☑ **Fail** ☐ Not assessed | Not mentioned anywhere; §7 lists concrete technical measures in place (TLS, disabled federation, DKIM/DMARC) but ISO 27001 certification is not among them | |
| **BD-G2** | RoPA covers all sub-domains, DPO-reviewed <12 months | ☐ Pass ☑ **Fail** ☐ Not assessed | Datenschutzerklärung §7: *"ein formelles Verzeichnis von Verarbeitungstätigkeiten (Art. 30 DSGVO) ... befinden sich in Arbeit"* — explicitly in progress, not complete | |
| **BD-G3** | HR/finance systems on European sovereign infrastructure | ☐ Pass ☐ Fail ☐ Not assessed | N/A — this platform does not appear to be an HR or finance system; Domain 3d in the institutional sense (HR, ERP, research data) is out of scope for what "newstudy" actually is | Confirm whether this gate even applies to this specific deployment |
| **BD-G4** | PAM deployed for Zone A, session recording, time-limited elevation | ☐ Pass ☐ Fail ☐ Not assessed | *(no public evidence)* | |
| **BD-G5** | Annual bulk data export test conducted, ARB-reviewed | ☐ Pass ☐ Fail ☐ Not assessed | *(no public evidence)* | |

### 6.2 Maturity Assessment

| Criterion | Level (0–5) | Evidence | Notes |
|---|---|---|---|
| One-directional data authority | ☐ Not assessed | *(no public evidence — and likely not applicable in the institutional sense to this platform)* | |
| ISO 27001 scope and currency | ☑ **Level 0–1** | No ISMS or certification mentioned; concrete measures listed (§7) fall short of a certified ISMS | |
| JML SLA performance | ☑ **Level 0** | Self-service only, no institutional JML (see Section 2) | |
| Data encryption posture | ☑ **Level 1** | Datenschutzerklärung §7: TLS in transit confirmed; **"serverseitige Verschlüsselung der gespeicherten Daten 'at rest' ist aktuell nicht durchgängig implementiert"** — encryption at rest explicitly not consistently implemented | Direct, cited evidence |
| Vendor lock-in risk | ☐ Not assessed | *(no public evidence on export/migration testing)* | |

---

## Section 7: Administration Systems and AI (Domain 3e)

### 7.1 Compliance Gates

| ID | Check | Status | Evidence | Notes |
|---|---|---|---|---|
| **AS-G1** | ≥90% of committee decisions in structured workflow system | ☐ Pass ☐ Fail ☐ Not assessed | N/A — no committee/governance workflow tooling is described; this is a student-facing platform, not an administrative one | Confirm applicability before scoring |
| **AS-G2** | AI outputs labelled, human-approval workflow operational | ☐ Pass ☐ Fail ☐ Not assessed | The one automated content-processing feature (translation bot) was disabled 15 July 2026; no other AI-generated output described | Likely N/A |
| **AS-G3** | Governance AI on European sovereign infrastructure | ☐ Pass ☐ Fail ☐ Not assessed | N/A — no governance AI in scope | |
| **AS-G4** | Retention schedule documented, DPO-approved | ☐ Pass ☑ **Fail** ☐ Not assessed | Datenschutzerklärung §4.2 explicitly: chat messages/media retained **indefinitely**, no purge job configured — *"das ist derzeit ehrlich der Ist-Zustand"* (honestly the current state); §7 confirms no uniform retention schedule exists yet | Strong, explicit evidence |
| **AS-G5** | Admin tool adoption ≥80% of target users | ☐ Pass ☐ Fail ☐ Not assessed | N/A — no administration tooling in scope for this platform | |

### 7.2 Maturity Assessment

*Likely not meaningfully applicable to this specific platform* — "newstudy"/CampusCircle is a student-facing module catalogue and collaboration tool, not an institutional administration/committee-governance system. Recommend marking this section **N/A for this assessment target** rather than scoring it, and noting that Domain 3e maturity would need to be assessed against whatever system (if any) DHBW or the OUG actually uses for committee governance.

---

## Section 8: Digital Sovereignty and European Interoperability

### 8.1 Compliance Gates

| ID | Check | Status | Evidence | Notes |
|---|---|---|---|---|
| **SOV-G1** | Digital sovereignty status report completed <12 months | ☐ Pass ☑ **Fail** ☐ Not assessed | No such report exists; this scorecard is arguably the first attempt at one | |
| **SOV-G2** | EWP participation: current API version for mobility | ☐ Pass ☑ **Fail** ☐ Not assessed | No mention anywhere | |
| **SOV-G3** | Domain 3d contracts include portability, exit, residency clauses | ☐ Pass ☑ **Fail** ☐ Not assessed | Datenschutzerklärung §5: DPAs (AVV) with **both** Inline GmbH and Hetzner Online GmbH are explicitly *"noch nicht final unterzeichnet"* (not yet finally signed) | Direct evidence — contracts aren't even executed, let alone containing the required clauses |
| **SOV-G4** | Open-source/European procurement policy approved and applied | ☐ Pass ☐ Fail ☐ Not assessed | The actual tool choices (Keycloak, Matrix/Synapse/Element, OpenTalk, Jitsi, Etherpad, MinIO) are heavily open-source and match D2's Annex A recommendations closely — but no *documented policy* driving those choices is evidenced | The outcome looks compliant; the governance process behind it is unconfirmed |

### 8.2 Maturity Assessment

| Criterion | Level (0–5) | Evidence | Notes |
|---|---|---|---|
| Sovereign infrastructure coverage | ☑ **Level 2** | Core hosting confirmed European (Hetzner/Inline, Germany); but 3 non-European sub-processors in active use for front-end assets, with removal only "planned" (§5–6) | |
| European standard adoption | ☑ **Level 0–1** | No eduGAIN, EWP, ELM, or EMREX participation found | |
| Open-source and European procurement | ☑ **Level 2–3 (tooling), Level 0 (documented policy)** | Strong tool choices (Matrix/Element, OpenTalk, Jitsi, Keycloak, Etherpad — all match D2 Annex A); no evidence of a formal procurement policy driving them | Split score — genuinely worth discussing which matters more for this criterion |
| Alliance and cooperative membership | ☐ Not assessed | *(no public evidence)* | |
| Vendor lock-in risk (aggregate) | ☐ Not assessed | *(no public evidence on export testing, though self-hosted open-source stack is inherently lower-risk than proprietary SaaS)* | |

---

## Section 9: User Experience and Adoption

### 9.1 Compliance Gate

| ID | Check | Status | Evidence | Notes |
|---|---|---|---|---|
| **UX-G1** | Adoption metrics measured and reported for major tool categories | ☐ Pass ☐ Fail ☐ Not assessed | *(no public evidence — inherently internal data)* | |
| **UX-G2** | Tools <60% adoption at 12 months have ARB-reviewed improvement plans | ☐ Pass ☐ Fail ☐ Not assessed | *(no public evidence; also contingent on UX-G1 and AF-G2 both existing)* | |

### 9.2 Maturity Assessment

| Criterion | Level (0–5) | Evidence | Notes |
|---|---|---|---|
| Adoption measurement | ☐ Not assessed | *(no public evidence)* | |
| Student experience quality | ☐ Not assessed | *(no public evidence — would require actual user research, not a public legal page)* | |
| Staff experience quality | ☐ Not assessed | *(N/A — this is a student-facing tool; "staff" experience may not be the relevant framing)* | |
| Accessibility compliance | ☑ **Level 1** | Barrierefreiheitserklärung §2: internal self-assessment only, "partially conformant," explicit 14-item list of what a full audit would still need to check (§5) | Well-documented gap, not absence of documentation |
| Mobile and offline capability | ☐ Not assessed | *(no public evidence, though `meta-viewport` responsive tags are present on all pages — a weak positive signal, not proof)* | |

---

## Score Summary (to complete once all sections are filled)

| Section | Max | Your Score | Gap |
|---|---|---|---|
| 1. Architecture Foundations | 25 | | |
| 2. Identity & Federation | 25 | | |
| 3. Learning Systems | 30 | | |
| 4. Credentialing & Student Records | 25 | | |
| 5. Learning Analytics | 25 | | |
| 6. Backend & Stakeholder Data | 25 | | |
| 7. Administration & AI | 30 | *(likely N/A for this platform — see Section 7 note)* | |
| 8. Digital Sovereignty | 25 | | |
| 9. User Experience & Adoption | 25 | | |
| **TOTAL** | **235** *(or 205 excluding Section 7 if marked N/A)* | | |

See [Document 4, Section 10.1](hei-evaluation-framework.md#101-score-interpretation) for band interpretation once a total is reached.

## Before You Finalise This

A few honest recommendations, not just for form's sake:

1. **Resolve the institutional-status question first.** Several of the lowest scores here (Section 1, most of Section 2) are downstream of this platform not yet having a clarified institutional relationship with DHBW or the OUG. If that relationship is clarified — the pilot is formally adopted, or superseded by an institutional system — this scorecard should be redone against whatever the actual institutional platform turns out to be, not patched in place.
2. **Domains 3b, 3c, and 3e may simply not be what this platform is for.** Rather than scoring them low, consider explicitly marking them out of scope for this specific target and noting where (if anywhere) those functions actually live in the broader OUG/DHBW landscape.
3. **The self-reported gaps are the most valuable part of this exercise.** Both source pages are unusually candid about what's missing (encryption at rest, DPIA, RoPA, signed DPAs, retention schedules, an accessibility audit). That candour is itself worth preserving and crediting — it's exactly the kind of honesty the [Design Signature Founding](../governance/design-signature-founding.md) methodology was built to reward, not penalise.

---

*Open University of Germany · Digital Infrastructure · Maturity Scorecard Working Template · Assessed against D4 v1.0*
