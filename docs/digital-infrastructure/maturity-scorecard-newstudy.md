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

**Second, what evidence went into this version.** Three sources so far: the platform's Datenschutzerklärung and Barrierefreiheitserklärung (privacy and accessibility statements) — unusually candid, self-critical documents, not marketing copy; seven screenshots of the platform's actual learner-facing interface; and direct inspection of the [`curriculum/skill-based-modules/`](../curriculum/skill-based-modules/index.md) JSON pipeline itself. Where a row cites JSON evidence, that means a file was opened and checked programmatically, not read from a screenshot.

**A fourth source, weighted differently: a team technical update.** A round of rows below cite a written technical update from the platform's own engineering side — infrastructure changes (VPN-gated admin surfaces, self-hosted third-party assets, call-recording retention), a documentation overhaul, and a new self-hosted AI initiative. This is **self-reported by the team, not independently verified** — I have not re-fetched the live privacy/accessibility pages to confirm these changes are reflected there, partly because the update itself states those legal pages "are still placeholders" pending a rewrite. Rows built on this source are marked *(per team update, unverified)* throughout, and should be treated as good-faith reporting to be checked against the actual pages once they're updated — not as equivalent to the directly-verified rows above.

**How to complete this:** for every row marked *Not assessed — requires internal evidence*, someone with actual access (the platform's operators, or DHBW/OUG governance once the institutional relationship is clarified) fills in the Level and Evidence columns. Rows already pre-filled can be corrected if the public evidence turns out to be stale or wrong — the citation is there so you can check.

---

## Section 1: Architecture Foundations

### 1.1 Compliance Gates

| ID | Check | Status | Evidence | Notes |
|---|---|---|---|---|
| **AF-G1** | Named Enterprise Architect with documented responsibilities | ☐ Pass ☐ Fail ☐ Not assessed | *(no public evidence — likely Fail given beta/pilot status; confirm internally)* | |
| **AF-G2** | Architecture Review Board meets ≥quarterly, decision log maintained | ☐ Pass ☐ Fail ☐ Not assessed | *(no public evidence)* | |
| **AF-G3** | ADR repository, ≥5 decisions in last 12 months | ☐ Pass ☐ Fail ☑ **Not assessed** *(real movement — see note)* | *(per team update, unverified)* The team reports retiring WikiJS in favour of a proper Markdown-based documentation site covering the whole project — newstudy, the OOAPI implementation, architecture diagrams, and data-flow diagrams. | This is real evidence of documentation *practice*, but a documentation site is not the same instrument as an ADR repository — D4 specifically asks for discrete, dated decision records with alternatives-considered and rationale, not narrative architecture documentation. Genuinely closer than before; still not confirmed to be the specific artifact this gate names. |
| **AF-G4** | Legacy system decommission register with target dates | ☐ Pass ☐ Fail ☑ **Not assessed** *(real movement — see note)* | *(per team update, unverified)* GitLab and WikiJS are reported as fully removed, not merely deprecated. | The original assessment ("likely N/A, no legacy migration in scope") undersold this — a real decommissioning did happen. Still not a Pass: no evidence of a formal *register* with target dates as a maintained artifact, just the outcome of a review that presumably happened informally. |
| **AF-G5** | DPIA completed for all personal-data systems, DPO-reviewed | ☐ Pass ☑ **Fail** ☐ Not assessed | Datenschutzerklärung §7: *"eine ... Datenschutz-Folgenabschätzung (Art. 35 DSGVO) für risikoreiche Verarbeitungen (Chat, Video) befinden sich in Arbeit"* — DPIA explicitly **in progress, not complete** | Direct evidence of Fail, not absence of evidence. Corroborated, not contradicted, by the team's own later update, which states the legal pages "are still placeholders" pending rewrite — this Fail should be assumed to still stand until those pages are actually revised. |

### 1.2 Maturity Assessment

| Criterion | Level (0–5) | Evidence | Notes |
|---|---|---|---|
| Architecture principles documented and applied | ☐ Not assessed | *(no public evidence)* | |
| API gateway operational | ☐ Not assessed | *(no public evidence — architecture is described as a set of self-hosted services, not through a documented gateway pattern)* | |
| Service catalogue completeness | ☐ Not assessed *(real movement — see note)* | *(no public evidence)* | *(per team update, unverified)* A stack review is reported — Element's room-sorting adopted, GitLab and WikiJS both dropped entirely as "not earning their place." Deliberately retiring tools that aren't pulling weight is exactly the kind of active inventory discipline a maintained service catalogue would produce — suggestive, not confirmation the catalogue itself exists as an artifact. |
| Exit capability | ☐ Not assessed | Data portability (Art. 20) is partly supported via the built-in PDF export — see Section 5 (Credentialing) note. Not the same as a tested bulk export/migration path. | Partial positive signal only |
| Security baseline (DPIA + ISMS) | ☑ **Level 1 (Initial)** | Datenschutzerklärung §7: DPIA "in Arbeit" (in progress); RoPA "in Arbeit"; no ISO/IEC 27001 mentioned anywhere | Team update reports security headers and a CSP added across vhosts — a real improvement to technical security posture, but distinct from the DPIA/RoPA/ISO findings this row is actually about; not moved for that reason. |

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
| **LS-G2** | LMS authenticates via OIDC; zero local student/staff accounts | ☐ Pass ☐ Fail ☐ Not assessed | Keycloak/OIDC is used (§4.1), and screenshots of the live interface show a "ZUM EINSCHREIBEN EINLOGGEN" (log in to enrol) gate on module detail pages, consistent with OIDC-gated enrolment actions — but "newstudy" isn't a conventional LMS in the D3a sense — module catalogue/progress tracker. Whether *zero* local accounts exist (the second half of this gate) is still not confirmable from outside | Applicability of the gate itself still needs internal confirmation; the OIDC-in-use half is now better evidenced than before |
| **LS-G3** | LTI Advantage (LTI 1.3 + AGS) in production | ☐ Pass ☐ Fail ☐ Not assessed | *(no public evidence — no third-party tool integration described anywhere)* | |
| **LS-G4** | WCAG 2.1 AA compliance documented, current VPAT available | ☐ Pass ☑ **Fail** ☐ Not assessed | Barrierefreiheitserklärung §2: *"partially conformant"*, based on **internal self-assessment only** — explicitly *"no full external BITV audit (e.g. BITV-Test, VPAT) has taken place yet"* | |
| **LS-G5** | Vendor analytics data sharing blocked without DPIA approval | ☐ Pass ☐ Fail ☐ Not assessed | *(no evidence of vendor analytics sharing found; also no DPIA yet per AF-G5, so this gate may not be meaningfully assessable until DPIA exists)* | |

### 3.2 Maturity Assessment

| Criterion | Level (0–5) | Evidence | Notes |
|---|---|---|---|
| LMS sovereignty | ☑ **Level 2** | European hosting confirmed (Hetzner, Germany); but DPAs not yet signed and 3 non-European sub-processors in active use for front-end assets (Google reCAPTCHA/gstatic, Cloudflare CDN, OpenFreeMap — Datenschutzerklärung §5–6) | Partial credit only — hosting location good, contractual/sub-processor picture incomplete |
| LTI ecosystem breadth | ☐ Not assessed | *(no public evidence)* | |
| xAPI emission coverage | ☑ **Level 0** | The "recommendations" feature is explicitly described as simple rule-based sorting on count data (likes, enrolments, completions) — Datenschutzerklärung §3 — not xAPI/Caliper event emission | This is specifically about behavioural/analytics event streams (Domain 3c) — do not conflate with the module *content* portability finding directly below, which is a different, much stronger, criterion |
| Content portability | ☑ **Level 3** *(updated — direct JSON evidence, not inferred)* | All 31 modules in [`curriculum/skill-based-modules/`](../curriculum/skill-based-modules/index.md) are stored as OOAPI v6-formatted JSON — an open, documented, non-proprietary interoperability standard, exactly what D2 §10 and D3 LMS-05/07/08 specify. Verified directly: 375 learning outcomes total, each with a coded competency ID and Bloom complexity level, bilingual (de-DE/en-GB) text. This is real, structured, exportable content — not merely a claim. | Capped at Level 3, not higher: no evidence of QTI assessment-item export or a tested migration-to-alternative-LMS path specifically, which D3 LMS-07/08 also ask for; the underlying data is genuinely portable, but portability of *assessment content* specifically hasn't been separately confirmed |
| Adoption rate | ☐ Not assessed | *(no usage data published; this is inherently internal data)* | |
| AI governance in LMS | ☑ **Level 0–N/A** *(update pending — see note)* | No AI tooling described in the original two legal pages. The one automated feature (translation bot) was disabled 15 July 2026 (§4.5) because it sent message text to Google. | *(per team update, unverified)* The team reports the translation bot is back, rebuilt on a local, self-hosted model, specifically because it removes the original reason for disabling it — no text leaves their server. If confirmed, this is a clean resolution of the exact problem the original finding described, not just a new feature. Also reported: locally-generated multilingual video documentation and subtitle/transcript generation for recorded sessions, both self-hosted. Not upgraded from Level 0 until the live pages (or another independently checkable source) confirm this — see the header note on team-reported evidence. |

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
| Micro-credential infrastructure | ☑ **Level 0** *(unchanged, but see note)* | No mention of micro-credential issuance | **Worth distinguishing clearly:** Level 0 here is about the *credentialing/issuance layer* specifically — no ELM, no signing, no Europass integration. It is not a statement about the underlying data. Direct inspection of [`curriculum/skill-based-modules/`](../curriculum/skill-based-modules/index.md) shows 375 fully specified, coded, Bloom-leveled learning outcomes across 31 modules, all resolving against a 172-entry competency codebook — genuinely rich, ready-to-map input data. What's absent is the layer that would turn that data into a signed, portable, learner-owned credential (D3 CRED-01 through CRED-10), not the underlying substance a credential would certify. This makes the gap smaller and more precisely scoped than "Level 0" alone suggests: the hard part (structured, validated competency data) exists; the remaining part (issuance infrastructure) is a defined build, not a research problem. **One specific sub-finding directly relevant to D3 CRED-07/CRED-10 (ESCO mapping):** the codebook has a dedicated `x-dhbw-esco-skills` field on all 172 entries, and it is an empty array on every single one — the ESCO cross-reference this section of D3 requires is schema-ready but entirely unpopulated, not partially done.

---

## Section 5: Learning Analytics (Domain 3c)

### 5.1 Compliance Gates

| ID | Check | Status | Evidence | Notes |
|---|---|---|---|---|
| **AN-G1** | Pseudonymisation at ingestion; no real identities in analytics store | ☐ Pass ☐ Fail ☐ Not assessed | Datenschutzerklärung §3 explicitly states **no** automated decision-making/profiling under Art. 22 — the "recommendations" are simple count-based sorts, not a pseudonymised analytics pipeline at all | This gate may not apply — there doesn't appear to be a "learning analytics" system in the D3c sense to assess |
| **AN-G2** | Stage 2 cohort size minimum (n≥10) enforced | ☐ Pass ☐ Fail ☐ Not assessed | N/A if no cohort analytics exist | |
| **AN-G3** | Student data dashboard: plain-language events, correction mechanism | ☐ Pass ☐ Fail ☐ Not assessed | A progress dashboard exists and is now directly evidenced, not just inferred: screenshots show a "Coverage of Enrolled Modules" view with enrolled-module count, learning-outcome count, ECTS progress, and a Bloom-weighted domain radar chart. Whether it meets the *specific* gate requirements — plain-language event listing and a correction-request mechanism — is not confirmed by what's visible | Upgraded from "no evidence found" to "feature confirmed to exist, specific gate requirements not confirmed" — a real but partial improvement in what's known |
| **AN-G4** | Stage 3 opt-out operational, doesn't affect other services | ☐ Pass ☐ Fail ☐ Not assessed | Account-level withdrawal of consent is described (§8, Art. 7(3)) but this ends *all* platform access — not a scoped opt-out from analytics alone while keeping other services | Likely Fail on the "doesn't affect other services" clause specifically — confirm |
| **AN-G5** | Early-warning model bias-tested in last 12 months | ☐ Pass ☑ **Fail / N/A** ☐ Not assessed | No early-warning model appears to exist at all — see AN-G1 note | |

### 5.2 Maturity Assessment

| Criterion | Level (0–5) | Evidence | Notes |
|---|---|---|---|
| Pipeline privacy architecture | ☑ **Level 0 / N/A** | No three-stage pipeline described; explicit statement that no Art. 22 profiling occurs | |
| Student data rights implementation | ☐ Not assessed *(partial signal — see note)* | Screenshots of the live platform show a personal "Coverage of Enrolled Modules" view: enrolled module count, learning outcome count, ECTS progress, and a Bloom-weighted domain radar chart with per-domain achievement percentages. This is a real, working self-view of personal progress. | **Why still "Not assessed" rather than scored:** this is evidence of *a* student-facing dashboard, but not evidence it meets D3 ANA-04's specific requirements — plain-language *event* listing (not just aggregate percentages), an explicit data-use purpose statement, and a correction-request mechanism. The coverage view is a genuine positive signal, not a confirmed Pass. |
| Early-warning system quality | ☑ **Level 0 / N/A** | No early-warning system found | |
| Analytics serving learner | ☐ Not assessed *(partial signal — see note)* | The same coverage dashboard is, by design, learner-facing rather than institutional — it shows the learner their own achievement, not an administrator's view of the learner. That directionality is consistent with this criterion's intent. | Falls short of a scored Level for the same reason as above: one screenshot of one feature is evidence of intent, not a verified claim that analytics *systematically* serve the learner across the platform |
| xAPI semantic consistency | ☑ **Level 0** | No xAPI or equivalent event standard mentioned | This remains distinct from the Bloom-level/competency-domain tagging confirmed in the [module JSON data](../curriculum/skill-based-modules/index.md) (see Section 3) — that tagging is rich *curriculum metadata*, not a *behavioural event stream*, which is what this criterion actually asks about |

---

## Section 6: Backend and Stakeholder Data (Domain 3d)

### 6.1 Compliance Gates

| ID | Check | Status | Evidence | Notes |
|---|---|---|---|---|
| **BD-G1** | ISO/IEC 27001 certified for Zone A, audit <12 months | ☐ Pass ☑ **Fail** ☐ Not assessed | Not mentioned anywhere; §7 lists concrete technical measures in place (TLS, disabled federation, DKIM/DMARC) but ISO 27001 certification is not among them | |
| **BD-G2** | RoPA covers all sub-domains, DPO-reviewed <12 months | ☐ Pass ☑ **Fail** ☐ Not assessed | Datenschutzerklärung §7: *"ein formelles Verzeichnis von Verarbeitungstätigkeiten (Art. 30 DSGVO) ... befinden sich in Arbeit"* — explicitly in progress, not complete | *(Corroborated, not contradicted, by the team's own later update)*: their technical update explicitly states the legal pages "are still placeholders" pending a rewrite — meaning this Fail should be assumed to still stand until those pages are actually revised, not treated as stale just because other infrastructure work has happened since. |
| **BD-G3** | HR/finance systems on European sovereign infrastructure | ☐ Pass ☐ Fail ☐ Not assessed | N/A — this platform does not appear to be an HR or finance system; Domain 3d in the institutional sense (HR, ERP, research data) is out of scope for what "newstudy" actually is | Confirm whether this gate even applies to this specific deployment |
| **BD-G4** | PAM deployed for Zone A, session recording, time-limited elevation | ☐ Pass ☐ Fail ☑ **Not assessed** *(real movement — see note)* | *(per team update, unverified)* Sensitive admin surfaces — Matrix admin panel, bot manager, Keycloak admin console, and the documentation site — are reported to now sit behind a self-hosted, key-based WireGuard tunnel and return 403 from the public internet. | This is a genuine, specific security improvement if accurate — but it's network-perimeter isolation, not PAM as D4 defines it. Still missing even if the VPN claim is confirmed: separate admin identities from daily-use accounts, session recording, and time-limited privilege elevation. Upgrade from "no signal at all" to "a real control exists, but not the specific one this gate asks about" — not a Pass. |
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
| **AS-G2** | AI outputs labelled, human-approval workflow operational | ☐ Pass ☐ Fail ☑ **Not assessed** *(real movement — see note)* | *(per team update, unverified)* The team reports building a self-hosted AI capability and describes one relevant workflow directly: a curation queue where a local model would propose competency and Bloom-level tags from imported module text, with a human approving or correcting each suggestion before publication — explicitly framed as "the model suggests, the person decides." | This is a precise match to D3's own Tier 1 ("Assistive") AI category — draft/suggest, human approves before anything is used. Not scored as a Pass: the update's own language is ambiguous about whether this workflow is live in production or validated in the team's self-hosted lab only ("a small self-hosted lab... to find out whether there is anything genuinely useful" — feasibility language, not "in production since" language). Worth a direct follow-up question rather than assuming either way. |
| **AS-G3** | Governance AI on European sovereign infrastructure | ☐ Pass ☐ Fail ☑ **Not assessed** *(real movement — see note)* | *(per team update, unverified)* The stated approach is explicitly self-hosted-only (their own hardware, not a cloud provider), with a named reason: "we cannot really send student or course data to Claude, OpenAI or anyone similar," and a licensing discipline restricted to Apache-2.0/MIT models. If accurate, this is close to an ideal-case answer to this gate. | Not scored because deployment status is unconfirmed (see AS-G2 note) and because "governance AI" here is closer to curriculum-curation assistance than committee/decision-workflow AI, which is what this gate more narrowly describes in D3. Directionally very strong regardless of exact scope. |
| **AS-G4** | Retention schedule documented, DPO-approved | ☐ Pass ☑ **Fail** ☐ Not assessed | Datenschutzerklärung §4.2 explicitly: chat messages/media retained **indefinitely**, no purge job configured — *"das ist derzeit ehrlich der Ist-Zustand"* (honestly the current state); §7 confirms no uniform retention schedule exists yet | *(per team update, unverified)* A real, narrower retention policy is separately reported for video-call recordings specifically (Jitsi/OpenTalk, 30-day automatic deletion, never leaving their infrastructure) — but this doesn't resolve the original finding, which was about chat/media broadly. Two different data types, two different retention postures; the call-recording policy is good news that doesn't generalise to the rest of AS-G4's scope without confirmation. |
| **AS-G5** | Admin tool adoption ≥80% of target users | ☐ Pass ☐ Fail ☐ Not assessed | N/A — no administration tooling in scope for this platform | |

### 7.2 Maturity Assessment

*Original assessment: likely not meaningfully applicable* — "newstudy"/CampusCircle is a student-facing module catalogue and collaboration tool, not an institutional administration/committee-governance system in the sense D3e primarily describes.

**Revised note.** One narrower but real administrative process now has direct relevance: the module curation pipeline (a parser produces module drafts from the actual DHBW Modulhandbuch PDF, which then sit in a queue for competency and Bloom-level tagging before publication). This is genuinely a Domain 3e administrative workflow, just a curriculum-data one rather than a governance-decision one, and the team's own description of how AI fits into it — suggest, don't decide; human approves every item — is exactly the Tier 1 pattern D3 §3e.4 specifies. Still not scored, for the same reason as AS-G2/AS-G3: it's unclear from the team's update whether this AI-assisted version of the curation workflow is running in production or was validated in their lab and not yet wired into the live pipeline. Worth a direct question rather than an assumption. The broader committee-governance sense of Domain 3e (AS-G1, AS-G5) remains genuinely out of scope for this platform, per the original assessment.

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
| Sovereign infrastructure coverage | ☑ **Level 2** *(update pending — see note)* | Core hosting confirmed European (Hetzner/Inline, Germany); original finding: 3 non-European sub-processors in active use for front-end assets (Google reCAPTCHA/gstatic, Cloudflare CDN, OpenFreeMap), with removal only "planned" (§5–6) | *(per team update, unverified)* The team reports third-party libraries are now self-hosted rather than pulled from CDNs, and security headers plus a CSP have been added across the main application pages — which is precisely what would resolve this finding if confirmed. Not upgraded from Level 2 until independently checked, but this is the single most directly on-point piece of the whole update relative to a specific, previously-cited gap. |
| European standard adoption | ☑ **Level 0–1** | No eduGAIN, EWP, ELM, or EMREX participation found | Unaffected by the team update — none of eduGAIN/EWP/ELM/EMREX participation is mentioned in it either |
| Open-source and European procurement | ☑ **Level 2–3 (tooling), Level 0 (documented policy)** | Strong tool choices (Matrix/Element, OpenTalk, Jitsi, Keycloak, Etherpad — all match D2 Annex A); no evidence of a formal procurement policy driving them | *(per team update, unverified)* The reported self-hosted AI approach follows the identical pattern and, notably, articulates its own reasoning explicitly: self-hosted over cloud AI specifically to avoid sending student/course data to non-European providers, and a stated commitment to Apache-2.0/MIT-licensed models only, avoiding non-commercial-only licences. This is a genuinely well-reasoned application of D1's sovereignty principles, in the team's own words, independent of whether every use case described is in production yet — the *reasoning* is sound evidence of principled practice even before every deployment is confirmed. |
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
| Student experience quality | ☐ Not assessed *(partial signal — see note)* | Screenshots show real, working features beyond a bare catalogue: search by name/code, filtering by competency type/domain code/ESCO skill/Bloom level/EQF level/module type/language/coordinator/ECTS and workload ranges, module favouriting, a personal roadmap with locked/available/in-progress/completed/optional/planned states and prerequisite arrows, and the coverage dashboard described in Section 5. This is evidence of considered UX design intent. | **Still not scored:** feature richness is not the same as confirmed quality — no satisfaction data, no usage data, no evidence anyone other than a test account has used these features. The gap between "the features exist and look well-designed" and "the features work well for real learners" is exactly what this criterion is asking about, and only the first half is evidenced. |
| Staff experience quality | ☐ Not assessed | *(N/A — this is a student-facing tool; "staff" experience may not be the relevant framing)* | |
| Accessibility compliance | ☑ **Level 1** | Barrierefreiheitserklärung §2: internal self-assessment only, "partially conformant," explicit 14-item list of what a full audit would still need to check (§5) | Well-documented gap, not absence of documentation |
| Mobile and offline capability | ☑ **Level 2** *(updated — direct evidence, not inferred)* | Seven screenshots confirm the platform genuinely renders and functions in a phone browser — module catalogue, roadmap, coverage dashboard, and module detail views all load and are interactive on an iPhone. This is real, first-hand confirmation, stronger than the "viewport tag present" signal used previously. | **Not scored higher than Level 2** because the same screenshots also show real layout strain: long module titles are truncated, and multi-column roadmap/stream cards extend past the viewport requiring horizontal scroll (visible directly in the roadmap views). Functions on mobile — is not yet *well-designed* for mobile. Offline capability specifically remains unevidenced either way. |

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

## Revision History

**Revision 3 — team technical update.** A round of updates driven by a technical status update from the platform's own team — infrastructure changes, a documentation overhaul, and a new self-hosted AI initiative. Handled differently from the previous two revisions: nothing here was independently re-verified against the live pages (the pages themselves are reported to still be placeholders pending rewrite), so every affected row is marked *(per team update, unverified)* and, in every case, moved from "no evidence" toward "reported, not confirmed" — never straight to a scored Pass. Rows touched: AF-G3/AF-G4 (documentation site, tool decommissioning), BD-G4 (WireGuard-gated admin surfaces — real, but not the same thing as PAM), AS-G2/AS-G3/Section 7.2 (the self-hosted AI curation workflow, a strong match to D3's Tier 1 AI pattern), AS-G4 (call-recording retention resolves a narrower slice of the original chat/media finding, not the whole thing), Section 3.2 AI governance (the translation bot's self-hosted revival directly answers the original Google-data-sharing finding, if confirmed), and Section 8 sovereignty (self-hosted third-party assets is the single most directly on-point item in the whole update, addressing the exact CDN/reCAPTCHA sub-processor finding cited before).

One thing worth being direct about: this update also surfaced its own internal tension. The team's message is candid that curriculum-data AI assistance (Bloom/competency suggestion, ESCO mapping) is still "currently manual" in one place while describing a working local-model solution for it in another — most likely meaning the capability has been validated in their self-hosted lab but not yet wired into the live production pipeline. That's a reasonable, normal state for R&D work, but it means several of the more exciting-sounding items in the update are closer to "demonstrated feasible" than "shipped." Worth asking directly rather than assuming either way before the next revision.

**Revision 2 — screenshots and the JSON pipeline.** Strengthened with two new evidence sources beyond the original two legal pages: seven screenshots of the live interface, and — the more substantial addition — direct inspection of the [`curriculum/skill-based-modules/`](../curriculum/skill-based-modules/index.md) JSON pipeline itself. Rows updated: Content portability (Section 3, upgraded to Level 3 on real evidence — 375 coded outcomes across 31 modules in an open OOAPI v6 format), Micro-credential infrastructure (Section 4, score unchanged but re-scoped with a precise finding: the ESCO field exists and is universally empty, not partially populated), Student data rights and Analytics serving learner (Section 5, moved from "no evidence" to "partial signal, not yet a confirmed Pass"), and Student experience quality and Mobile capability (Section 9, moved from "no evidence" to real but bounded evidence — features and mobile function are confirmed; quality and adoption are not). The pattern worth naming: in every case, the new evidence moved a row from "unknown" toward "partially known," not straight to "resolved."

**Revision 1 — initial template.** Built directly against Document 4's structure, pre-filled from the platform's Datenschutzerklärung and Barrierefreiheitserklärung — two unusually candid, self-critical legal pages, not marketing copy.

---

*Open University of Germany · Digital Infrastructure · Maturity Scorecard Working Template · Assessed against D4 v1.0*
