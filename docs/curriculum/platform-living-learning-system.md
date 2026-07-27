# Platform: From Static Curriculum to Living Learning System

*Open University of Germany · Digital Platform Architecture · 2026*

> **Source:** migrated from `OUG Platform Living Learning System.docx`
> **Status:** *(to be set — see [Document Status](../index.md#document-status))*

*Eight milestones in the transformation of the module handbook into a data-driven, student-centred, adaptive learning environment — and how each milestone closes a gap in the OUG platform architecture*

> **What this document is.** The OUG's Governance Principles Assessment identified the absence of a specified digital platform as a gap in the institutional design. This document closes that gap. It describes the platform that exists — a stepwise transformation of the traditional module handbook into a living, data-driven learning system — in terms of its design principles, its equity implications, and its alignment with the OUG's institutional commitments. Each of the eight milestones in the platform's development corresponds to a principle derivable from the OUG's mission, its quality assurance framework, and its pedagogical philosophy. The platform is not a commercial LMS repurposed for an unusual context. It is purpose-built for the OUG's specific institutional form: federated, modular, competency-based, and oriented toward learners who cannot be assumed to have access to a campus.

---

## I. The Starting Point: The Limits of the Static Module Handbook

Every programme-based university begins with a module handbook — the document that defines the structure of a study programme in static, text-heavy form. Modules are described in terms of their ECTS credits, workload hours, teaching formats, and intended learning outcomes. The handbook serves accreditation, documentation, and compliance purposes effectively. It is the authoritative record of what a programme contains.

But the module handbook has three structural limitations that matter specifically for the OUG's target population. First, it is not interactive — it describes the curriculum as something to be read, not explored. Second, it is not personalised — it presents a single linear sequence to every learner regardless of their prior knowledge, available time, or learning goals. Third, it is not navigable from a learner's perspective — it was designed for accreditation reviewers, not for working adults approaching a degree in non-linear fragments over several years.

> The module handbook answers the question: what does this programme contain? The platform answers the question: what should I do next, what have I become capable of, and where does this take me? These are different questions, requiring a different kind of document — and, ultimately, a different kind of system.

The eight milestones described in this document trace the transformation from the first kind of system to the second. Each milestone is a design decision, not merely a technical development step. Each one encodes a principle about what learning infrastructure should do for a learner — particularly a learner who is not a traditional full-time student with a campus, a cohort, and a fixed timetable.

---

## II. Eight Milestones: From Documentation to Adaptation

### Milestone 1 — The Curriculum as a Searchable Index

*Linear reading of a PDF → Non-linear exploration of a structured catalogue*

The first transformation is the conversion of the module handbook into a searchable, filterable catalogue. Students can search modules by name or code, filter by stream or competency domain, and access module information instantly on any device. This step alone changes the fundamental interaction with the curriculum: from prescribed sequence to self-directed navigation. The student is no longer constrained by the order in which a document was written but can approach the curriculum from their own entry point — their interests, their employer's needs, their prior knowledge gaps.

**Design principles**
- Curriculum structure must be machine-readable before it can be learner-navigable.
- Non-linear access is an equity principle: it removes the advantage of those who already know how to decode a linear academic document.
- Mobile-first design is not a convenience feature — it is a requirement for learners who study between professional and caregiving commitments.

**OUG alignment.** The OUG's OOAPI v5 compliance and Europass integration both presuppose a machine-readable curriculum. The searchable catalogue is the learner-facing expression of the same data layer that enables interoperability with employers and other institutions. At OUG, this milestone is not a UI improvement — it is the platform expression of the institutional commitment to open standards.

### Milestone 2 — Rewriting the Curriculum in Terms of Skills

*Describing what a module contains → Describing what a student becomes capable of*

The second milestone is more fundamental than the first. Content is no longer presented only as modules, but reinterpreted as a system of skills and competencies. Each module is decomposed into domains, competencies, Bloom taxonomy levels (from remembering to creating), and links to external frameworks including ESCO. What was implicit in the module handbook — learning objectives like "students can design algorithms" or "apply mathematical reasoning" — becomes explicit, structured, and machine-readable. This creates a semantic layer on top of the curriculum, enabling comparison between modules, aggregation of skills across modules, and alignment with labour market frameworks that employers actually use.

**Design principles**
- Competency transparency enables learners to understand what they are developing, not merely what they are completing.
- ESCO mapping is the bridge between academic learning outcomes and labour market language — it makes the credential interpretable outside the institution that issued it.
- Bloom-level tagging makes cognitive progression visible: not just what a student knows, but how deeply they know it.

**OUG alignment.** The OUG's Quality Assurance Framework establishes learning outcomes as the primary unit of quality, requiring ESCO alignment for every module. The eleven competency domains of the B.Sc. CS programme (PROG, SOFT, NETW, DATA, AI, METH, ETHI, UXHI, COMM, RESE, PERS) are the semantic structure that Milestone 2 makes navigable. For OUG's target learners — professionals seeking to upskill or credential existing expertise — the competency layer is not supplementary. It is the primary reason the platform is useful to them.

### Milestone 3 — Making Learning Progress Visible

*"You passed this course" → "This is how your capability profile is evolving"*

Once the curriculum is structured in terms of competencies, it becomes possible to track progress not only in ECTS but in skills. The platform introduces multiple simultaneous views of progress: ECTS-based progress (e.g., 40 of 150 credits completed), module completion status, domain coverage, a competency radar showing multi-dimensional profile development, and Bloom-level distribution across completed modules. Students can see not only how far they have progressed in their degree, but which competencies they have developed strongly, which areas are underrepresented, and how their learning is distributed across cognitive levels. The abstract structure of a degree becomes visible and interpretable.

**Design principles**
- Multi-dimensional progress display is an advantage-frame intervention: it shows learners what they have built, not what they still lack.
- Radar charts and skill trees make the implicit logic of a curriculum explicit — they are not decorative visualisations but navigational instruments.
- Competency gap visibility supports self-directed learning decisions without requiring a personal advisor for every decision.

**OUG alignment.** The Lowery and Wout (2010) research on inequality framing demonstrated that how progress is displayed affects engagement — showing achievement (advantage frame) rather than deficit (disadvantage frame) is directly associated with sustained engagement among non-traditional learners. The OUG's platform operationalises this insight at the UX level: the primary progress view is competency gained, not credits remaining. This is a design choice with measurable equity implications.

### Milestone 4 — Enabling Self-Regulated Learning

*Following a predefined path → Managing one's own learning trajectory*

Building on visible progress, the platform introduces elements of student agency: students can define their own goals (complete a specific module by a given date, reach a target competency level in a domain), track progress toward those goals, and interact directly with competencies through feedback mechanisms. This layer supports self-regulated learning — students are not only following a curriculum requirement but actively managing their trajectory through it. The curriculum becomes not just a requirement structure but a space for planning, reflection, and decision-making. The system begins to resemble a learning environment rather than a catalogue.

**Design principles**
- Goal-setting by learners, not only by institutions, is the operational expression of learner agency.
- Self-regulation is a learnable meta-skill — the platform that supports it is also developing it.
- Feedback on perceived learning, distinct from formal assessment, creates a signal that is invisible in traditional grading systems.

**OUG alignment.** The OUG's Quality Assurance Framework explicitly identifies metacognitive skills — self-regulation, planning, reflection — as core academic standards, not supplementary extras. The platform's goal-setting and self-tracking functions are the pedagogical infrastructure through which these standards are developed. For working adults, who must manage their study time against professional and caregiving demands, self-regulation support is not a nice-to-have — it is a prerequisite for completion.

### Milestone 5 — Structuring Learning Pathways

*Navigating a flat list of modules → Navigating a structured learning network*

With modules and competencies structured and progress visible, the platform introduces a skill tree representation. Modules are visualised as nodes in a dependency graph: connected by prerequisite relationships, marked as locked, available, in progress, or completed. This representation makes explicit what is often hidden in traditional curricula — the implicit pathways and dependencies between learning elements. Students can now answer the questions that a PDF module handbook cannot: What can I take next? What builds on what? Where am I in the system? What does my current position in the curriculum look like as a structure rather than a list?

**Design principles**
- Prerequisite transparency removes hidden knowledge barriers — learners can see why certain modules are locked and what unlocks them.
- Graph-based navigation supports non-linear entry into the curriculum, a requirement for learners with prior experiential knowledge.
- The skill tree is a planning instrument: it makes multi-semester learning trajectories visualisable from any current position.

**OUG alignment.** The OUG's B.Sc. CS programme specifies a threshold-based pathway (120 ECTS across 4+ streams unlocks Capstone; all stream modules plus Capstone unlocks Thesis). The skill tree is the visual implementation of this threshold logic — it makes the stacking model navigable rather than merely described. For OUG's federated learners, who may be taking modules across partner institutions in different semesters, the dependency graph is the primary orientation instrument.

### Milestone 6 — Toward Adaptive Guidance

*Self-navigation alone → Guided pathways based on individual competency profiles*

With all previous layers in place — structured content, competency mapping, progress tracking, goal-setting, and pathway visualisation — the platform is positioned to introduce recommendation mechanisms. These operate on multiple logics: fill gaps (identify underdeveloped competencies and suggest modules that address them), strengthen (deepen existing strengths through advanced modules in well-developed domains), and path next (suggest logical next steps based on current position in the dependency graph and stated goals). The foundation for recommendation is already present in the data model — competencies, Bloom levels, domain distributions, module relationships, and the learner's own interaction history.

**Design principles**
- Recommendation based on competency profile is personalisation in the educationally meaningful sense — it responds to what a learner has actually developed, not to demographic assumptions.
- Multiple recommendation logics (gap-filling, strengthening, pathway progression) respect that different learners at different stages need different kinds of guidance.
- Transparent recommendation reasoning — showing why a module is suggested — preserves learner agency rather than replacing it.

**OUG alignment.** The OUG's Academic Community Charter specifies that the institution provides meaningful learning support alongside the structural flexibility of modular study. Adaptive guidance is the platform implementation of this commitment. It is particularly significant for OUG's target learners — professionals who need efficient pathways and cannot afford to take modules that do not serve their development — and for learners without strong prior academic advising relationships, who may not know how to navigate a complex curriculum without structural support.

### Milestone 7 — Fine-Grained Feedback and Learning Analytics

*Module-level pass/fail signals → Competency-level feedback creating a continuous improvement loop*

A further development step integrates feedback at the granularity of competencies, not just modules. Students can evaluate their perceived competency development through lightweight interactions (confirming, questioning, or flagging specific competencies), providing signals about their actual learning experience that are invisible in formal assessment records. This creates a data layer reflecting the gap between intended and perceived learning outcomes — one of the most important and most ignored quality signals in higher education. Aggregated across learners and over time, this data enables curriculum refinement at the competency level: identifying systematic misalignments between what a module claims to develop and what learners report actually developing.

**Design principles**
- Feedback at the competency level, not just the module level, is the operational expression of "learning outcomes as the primary unit of quality."
- Student-generated quality signals are a source of information that external examiner reviews and employer surveys cannot provide — they capture the subjective learning experience in real time.
- The feedback loop (curriculum → student interaction → data → curriculum refinement) makes quality assurance continuous rather than periodic.

**OUG alignment.** The OUG's Quality Assurance Framework specifies the Stichprobe as an annual independent assessment sample — a structural mechanism for verifying that formal assessment reflects actual learning. The platform's competency-level feedback layer complements this: it provides continuous learner-generated signals between formal review cycles. Together, they constitute a dual quality system — periodic expert verification and continuous learner signal — that no traditional QA framework provides. The Berkling (in review) finding that engagement depth predicts learning gain (r = 0.958) is only exploitable if the platform captures engagement at sufficient granularity. This milestone provides that granularity.

### Milestone 8 — Social and Collaborative Layer

*An individual learning record in a shared institutional space → A structured learning environment where learning actually happens*

The integration of Matrix rooms — open-source, federated communication infrastructure — adds a social dimension to the platform without creating a proprietary communication dependency. Each module is connected to a communication space in which peer interaction, discussion, and collaborative knowledge-building can occur. This connects the structured learning model with community formation, peer support, and the kind of incidental learning that traditional campus students take for granted and online learners are systematically denied. The platform evolves from a representation of learning into a space where learning happens.

**Design principles**
- Community formation in a distributed institution requires deliberate infrastructure — it does not emerge automatically from shared enrolment.
- Open-source, federated communication (Matrix) prevents platform lock-in and preserves the OUG's open standards commitment at the community layer.
- Peer learning is both a pedagogical resource and a retention mechanism — learners who are connected to a community are more likely to persist through productive struggle periods.

**OUG alignment.** The OUG's Academic Community Charter specifies in detail how intellectual community is built deliberately in a distributed institution: through Mission Hubs, digital infrastructure, Annual Colloquia, and participation in governance. The Matrix integration is the always-on substrate of this community — the space between formal events. For OUG's target learners, who study across time zones, work schedules, and caregiving windows, asynchronous community infrastructure is not a supplement to campus life. It is campus life.

---

## III. Consolidated Design Principles and OUG Alignment

The eight milestones yield twenty-four design principles. The following table maps each to its equity implication and its status within the OUG's institutional design.

| Milestone | Principle | Equity Implication | OUG Status |
|---|---|---|---|
| M1 | Non-linear curriculum access | Removes advantage of those who know how to decode academic documents | Implemented — OOAPI v5 |
| M1 | Mobile-first interface design | Reaches learners without dedicated study spaces or desktop access | Specified as requirement |
| M1 | Machine-readable curriculum structure | Prerequisite for interoperability, personalisation, and analytics | OOAPI v5 compliant |
| M2 | Competency-level learning outcomes | Makes development visible, not just completion | Partially — 4 of 37 modules fully specified |
| M2 | ESCO skills alignment | Bridges academic credentials and labour market legibility | Specified, implementation in progress |
| M2 | Bloom-level cognitive tagging | Makes depth of learning visible alongside breadth | Specified in platform model |
| M3 | Multi-dimensional progress display | Advantage-frame intervention — shows achievement, not deficit | Platform design principle confirmed |
| M3 | Competency radar visualisation | Supports orientation in a complex, non-linear curriculum | Implemented in platform |
| M3 | Domain coverage tracking | Enables learners to identify strategic gaps without advisor dependency | Implemented in platform |
| M4 | Learner-defined goal setting | Operationalises agency and self-regulation support | Implemented in platform |
| M4 | Progress tracking toward self-set goals | Supports metacognitive development as institutional standard | Aligns with QA Framework |
| M4 | Competency-level learner feedback | Generates quality signal invisible to formal assessment | Milestone 7 — implemented |
| M5 | Prerequisite dependency graph | Removes hidden knowledge barriers — makes curriculum logic transparent | Implemented in skill tree |
| M5 | Lock/available/complete status display | Enables non-linear planning without advisor guidance | Implemented in platform |
| M5 | Multi-semester pathway visualisation | Supports long-term planning for part-time learners | Implemented in platform |
| M6 | Gap-filling recommendations | Personalisation based on actual competency profile, not demographics | In development |
| M6 | Strengthening recommendations | Respects learner preference for depth over breadth | In development |
| M6 | Transparent recommendation reasoning | Preserves agency — shows why, not just what | Design principle specified |
| M7 | Competency-level feedback loop | Continuous quality signal between formal review cycles | Implemented — complements Stichprobe |
| M7 | Aggregated learning analytics | Enables curriculum refinement at competency level | Implemented in platform |
| M7 | Intended vs. perceived LO alignment | Identifies systematic curriculum misalignments in real time | Implemented in platform |
| M8 | Open-source communication (Matrix) | Prevents lock-in — preserves open standards at community layer | Implemented — federated |
| M8 | Module-linked community spaces | Enables community formation without campus | Implemented in platform |
| M8 | Asynchronous-first community design | Reaches learners across work schedules and time zones | Core design principle |

---

## IV. What This Platform Closes in the OUG's Design

### The Platform Gap in the Governance Assessment

The OUG Governance Principles Assessment (2026) identified a specific gap under the Platform domain: "No platform accessibility specification document currently exists in the OUG document stack." The assessment noted that "accessibility compliance" — while necessary — is not sufficient, and that the equity question is whether the platform works on a mid-range smartphone with variable bandwidth, for a learner without specialist digital literacy. This document, and the platform it describes, closes that gap.

The eight-milestone architecture is not a procurement specification for a generic LMS. It is a purpose-built system designed for the OUG's specific institutional form and target population. Its design principles are derivable from the OUG's founding commitments: open standards, competency-based learning, Europass integration, asynchronous-first access, and the framing of learners as capable adults in the right system at last.

### The Equity Communication Gap

The Governance Principles Assessment also identified a communication framing gap: no specification existed for how individual learner-facing communications should be framed. The platform closes this structurally: by making the primary progress view competency-gained rather than credits-remaining, by making the skill tree the entry point rather than the distance to completion, and by making recommendation the expression of a learner's individual competency profile rather than a generic programme map. The framing is built into the architecture — it does not depend on individual advisors making individual framing choices.

### The Berkling Connection: Auditable Learning

Berkling (in review) argues that the standard micro-credential model has a fundamental epistemological weakness: it certifies a state — you can do X — with no information about how that state was reached. The engagement-gain correlation (r = 0.958) suggests that the path is constitutive of the skill, not incidental to it. The student who completed core and extension tasks over eight weeks did not just learn more — they learned differently, more durably, more transferably. The platform's engagement tracking at competency level (Milestone 7) is the technical foundation for a pathway-certified credential: a Europass digital credential that carries not only the outcome but the verified engagement record that produced it. This is the next development step in the platform's trajectory.

> What this platform builds is not just a better way to navigate a degree. It builds the data infrastructure that makes a trustworthy, auditable, learner-owned credential possible — one that tells employers not only what a graduate can do, but how they came to be able to do it.

---

*Open University of Germany · Digital Platform Architecture · Living Learning System · 2026*
