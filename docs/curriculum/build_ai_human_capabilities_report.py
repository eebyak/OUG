#!/usr/bin/env python3
r"""Create a Markdown analysis of AI readiness and human capabilities.

The script scans a directory for OOAPI-style module JSON files (default:
``T*INF*v6.json``), enriches their learning outcomes from the DHBW/OUG
competence codebook, and creates one reader-friendly Markdown report.

The report deliberately distinguishes three kinds of evidence:

1. **Explicit AI evidence** from ``x-dhbw-ai_related``,
   ``x-dhbw-ai_domain`` and ``ai-upskilling`` markers.
2. **Explicit human-capability evidence** from ``x-dhbw-human_skill_tag``,
   meta-skill categories and human-oriented capability clusters.
3. **Inherent / contextual human-capability evidence** inferred transparently
   from competence domains, module formats, titles, descriptions and learning-
   outcome wording. This is reported as an inference, never as a formal tag.

This makes visible the "hidden human curriculum": design thinking, stakeholder
interaction, interdisciplinary work, societal responsibility, project work,
reflection, judgement and similar capabilities that are often present in a
programme without being labelled as generic soft skills.

No external AI service is used. The analysis is deterministic and auditable;
the inference dictionaries near the top of this file can be reviewed and
changed by curriculum staff.

Example (PowerShell)
--------------------
python .\build_ai_human_capabilities_report.py `
  --dir ".\dir" `
  --pattern "T*INF*v6.json" `
  --codebook ".\competence_codebook_v11_ooapi.json" `
  --output ".\New_Study_AI_Human_Capabilities.md" `
  --language "en-GB"

Dependencies
------------
Python 3.10+ only. No third-party packages are required.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from statistics import mean
from typing import Any, Iterable, Mapping, Sequence


# ---------------------------------------------------------------------------
# Cognitive level and AI taxonomy
# ---------------------------------------------------------------------------
BLOOM_LEVEL = {
    "remember": 1,
    "understand": 2,
    "apply": 2,
    "analyze": 3,
    "analyse": 3,
    "evaluate": 4,
    "create": 4,
    "unknown": 0,
}

LEVEL_LABEL = {
    1: "Foundation and recognition",
    2: "Use and application",
    3: "Analysis and integration",
    4: "Evaluation, design and stewardship",
    0: "Unspecified",
}

AI_DOMAIN_LABELS = {
    "technical": "Technical foundations",
    "application": "Applied use",
    "evaluation": "Evaluation and verification",
    "product": "Product judgement and success metrics",
    "mlops": "Operationalisation and MLOps",
    "agentic": "Agentic systems",
    "ethics": "Ethics, fairness and responsibility",
    "governance": "Governance and accountability",
    "societal": "Societal consequences",
    "sociocultural": "Cultural and linguistic context",
    "cognitive": "Cognitive independence",
    "agency": "Human agency",
}

AI_FAMILIES = {
    "Build and operate AI": {"technical", "application", "mlops", "agentic"},
    "Evaluate and improve AI": {"evaluation", "product"},
    "Govern AI responsibly": {"ethics", "governance", "societal", "sociocultural"},
    "Preserve human agency with AI": {"cognitive", "agency"},
}


# ---------------------------------------------------------------------------
# Transparent human-capability inference model
# ---------------------------------------------------------------------------
# Domain evidence is intentionally weaker than an explicit human-skill tag.
# It says that a competence domain normally requires a human capability in
# practice, not that the programme has formally tagged that capability.
DOMAIN_TO_HUMAN_DIMENSIONS: dict[str, tuple[str, ...]] = {
    "COMM": (
        "Communication and stakeholder translation",
        "Collaboration, facilitation and conflict competence",
    ),
    "TEAM": ("Collaboration, facilitation and conflict competence",),
    "PERS": (
        "Self-direction, reflection and resilience",
        "Project leadership and professional responsibility",
    ),
    "ETHI": ("Ethical and societal judgement",),
    "CREA": (
        "Creativity and innovation",
        "Human-centred design and empathy",
    ),
    "PROJ": (
        "Project leadership and professional responsibility",
        "Collaboration, facilitation and conflict competence",
        "Interdisciplinary integration and systems thinking",
    ),
    "RSCH": ("Research, evidence and epistemic responsibility",),
    "ANLY": ("Critical judgement and analytical independence",),
    "QUAL": ("Critical judgement and analytical independence",),
    "METH": (
        "Critical judgement and analytical independence",
        "Research, evidence and epistemic responsibility",
    ),
    "ARCH": (
        "Interdisciplinary integration and systems thinking",
        "Creativity and innovation",
    ),
    "APPL": ("Interdisciplinary integration and systems thinking",),
    "SECU": (
        "Ethical and societal judgement",
        "Project leadership and professional responsibility",
    ),
    "KNOW": ("Research, evidence and epistemic responsibility",),
    "MATH": (
        "Critical judgement and analytical independence",
        "Research, evidence and epistemic responsibility",
    ),
    "THEO": ("Critical judgement and analytical independence",),
}

HUMAN_DIMENSIONS: dict[str, dict[str, Any]] = {
    "Critical judgement and analytical independence": {
        "description": (
            "Students analyse alternatives, test claims, recognise uncertainty and "
            "retain independent judgement rather than accepting technical or AI outputs at face value."
        ),
        "keywords": (
            "critical", "critically", "judge", "judgement", "evaluate", "assess",
            "analyse", "analyze", "compare", "validate", "verify", "uncertainty",
            "independence", "quality criteria", "limitations", "trade-off", "tradeoff",
        ),
    },
    "Communication and stakeholder translation": {
        "description": (
            "Students explain technical matters to different audiences, document decisions, "
            "present evidence and translate between specialist and non-specialist perspectives."
        ),
        "keywords": (
            "communicat", "present", "presentation", "explain", "document", "audience",
            "stakeholder", "non-technical", "nontechnical", "report", "discussion",
            "dialogue", "visualisation", "visualization",
        ),
    },
    "Collaboration, facilitation and conflict competence": {
        "description": (
            "Students coordinate work with others, give and receive feedback, facilitate "
            "collective decisions and handle disagreement constructively."
        ),
        "keywords": (
            "team", "group work", "groupwork", "collaborat", "cooperat", "feedback",
            "facilitat", "workshop", "conflict", "negotiate", "peer", "co-design",
            "codesign", "collective", "joint",
        ),
    },
    "Self-direction, reflection and resilience": {
        "description": (
            "Students regulate their own learning and work, reflect on strengths and limits, "
            "adapt to unfamiliar situations and remain capable under uncertainty."
        ),
        "keywords": (
            "independent", "autonomous", "self-directed", "self directed", "reflect",
            "resilien", "adapt", "initiative", "strengths and weaknesses", "own work",
            "self-assess", "uncertain", "learning diary", "portfolio",
        ),
    },
    "Ethical and societal judgement": {
        "description": (
            "Students consider rights, fairness, public consequences, power, sustainability "
            "and professional responsibility when designing or deploying technology."
        ),
        "keywords": (
            "ethic", "societ", "social", "fairness", "bias", "responsib", "law",
            "legal", "governance", "public", "sustainab", "justice", "rights",
            "discrimination", "impact assessment", "dignity", "accountability",
        ),
    },
    "Human-centred design and empathy": {
        "description": (
            "Students investigate human needs and contexts, design usable interactions and "
            "consider how systems affect the people who must live and work with them."
        ),
        "keywords": (
            "human-centred", "human centered", "user-centred", "user centered", "user",
            "usability", "ux", "interaction", "interface", "design thinking", "empathy",
            "needs", "persona", "participant", "co-design", "codesign", "accessibility",
        ),
    },
    "Creativity and innovation": {
        "description": (
            "Students generate alternatives, prototype, combine ideas and create novel or "
            "context-sensitive solutions rather than merely reproduce known procedures."
        ),
        "keywords": (
            "creativ", "innovat", "ideat", "prototype", "novel", "design", "invent",
            "alternative solution", "explor", "conceptualise", "conceptualize",
        ),
    },
    "Interdisciplinary integration and systems thinking": {
        "description": (
            "Students connect technical, organisational, professional and societal perspectives "
            "and understand how components and stakeholders interact in larger systems."
        ),
        "keywords": (
            "interdisciplin", "cross-disciplinary", "cross disciplinary", "integrat",
            "system thinking", "systems thinking", "socio-technical", "sociotechnical",
            "transfer", "across domains", "boundary", "relationships", "architecture",
            "holistic", "context",
        ),
    },
    "Research, evidence and epistemic responsibility": {
        "description": (
            "Students investigate systematically, use literature and data responsibly, distinguish "
            "evidence from assertion and recognise the limits of what is currently known."
        ),
        "keywords": (
            "research", "scientific", "academic", "literature", "evidence", "hypothesis",
            "experiment", "methodolog", "data collection", "citation", "source",
            "reproduc", "validity", "reliability", "limits of knowledge",
        ),
    },
    "Project leadership and professional responsibility": {
        "description": (
            "Students plan and deliver work, make accountable decisions, coordinate resources "
            "and accept responsibility for outcomes in professional contexts."
        ),
        "keywords": (
            "project", "capstone", "lead", "manage", "planning", "coordinate", "deadline",
            "professional", "accountab", "responsibility", "decision", "risk", "client",
            "practice", "delivery",
        ),
    },
}

HUMAN_TAG_TO_DIMENSIONS = {
    "social": (
        "Communication and stakeholder translation",
        "Collaboration, facilitation and conflict competence",
    ),
    "self": (
        "Self-direction, reflection and resilience",
        "Critical judgement and analytical independence",
    ),
}

CLUSTER_TO_DIMENSIONS = {
    "human-social": (
        "Communication and stakeholder translation",
        "Collaboration, facilitation and conflict competence",
        "Ethical and societal judgement",
    ),
    "personal-reflective": (
        "Self-direction, reflection and resilience",
        "Critical judgement and analytical independence",
    ),
    "creative-aesthetic": ("Creativity and innovation",),
    "cognitive": (
        "Critical judgement and analytical independence",
        "Interdisciplinary integration and systems thinking",
    ),
}

META_CATEGORY_TO_DIMENSIONS = {
    "analytical": ("Critical judgement and analytical independence",),
    "collaboration": ("Collaboration, facilitation and conflict competence",),
    "cognitive": (
        "Critical judgement and analytical independence",
        "Research, evidence and epistemic responsibility",
    ),
    "adaptability": ("Self-direction, reflection and resilience",),
}

# Assessment formats and learning designs frequently teach human capabilities
# even when learning outcomes do not carry an explicit human tag.
FORMAT_KEYWORDS = {
    "seminar": (
        "Communication and stakeholder translation",
        "Research, evidence and epistemic responsibility",
    ),
    "presentation": ("Communication and stakeholder translation",),
    "referat": ("Communication and stakeholder translation",),
    "project": (
        "Project leadership and professional responsibility",
        "Collaboration, facilitation and conflict competence",
    ),
    "projekt": (
        "Project leadership and professional responsibility",
        "Collaboration, facilitation and conflict competence",
    ),
    "portfolio": ("Self-direction, reflection and resilience",),
    "design": (
        "Creativity and innovation",
        "Human-centred design and empathy",
    ),
    "entwurf": (
        "Creativity and innovation",
        "Interdisciplinary integration and systems thinking",
    ),
    "thesis": (
        "Research, evidence and epistemic responsibility",
        "Self-direction, reflection and resilience",
    ),
    "hausarbeit": (
        "Research, evidence and epistemic responsibility",
        "Communication and stakeholder translation",
    ),
}


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class DomainInfo:
    code: str
    name: str
    description: str = ""
    outcome_id: str = ""


@dataclass(frozen=True)
class SkillInfo:
    code: str
    name: str
    description: str
    domain_code: str
    bloom: str
    ai_related: bool
    ai_domains: tuple[str, ...]
    human_tag: str
    clusters: tuple[str, ...]
    meta_skills: tuple[str, ...]
    meta_category: str
    outcome_id: str = ""


@dataclass
class OutcomeOccurrence:
    code: str
    name: str
    description: str
    domain_code: str
    domain_name: str
    bloom: str
    level: int
    ai_related: bool
    ai_domains: tuple[str, ...]
    human_tag: str
    clusters: tuple[str, ...]
    meta_skills: tuple[str, ...]
    meta_category: str


@dataclass
class Module:
    path: Path
    code: str
    title: str
    description: str
    stream: str
    year: str
    semester: str
    ects: float
    assessment: str
    outcomes: list[OutcomeOccurrence] = field(default_factory=list)


@dataclass
class DimensionEvidence:
    direct_points: float = 0.0
    metadata_points: float = 0.0
    inferred_points: float = 0.0
    direct_skills: set[str] = field(default_factory=set)
    metadata_skills: set[str] = field(default_factory=set)
    inferred_skills: set[str] = field(default_factory=set)
    reasons: set[str] = field(default_factory=set)
    snippets: list[str] = field(default_factory=list)

    @property
    def score(self) -> float:
        return self.direct_points + self.metadata_points + self.inferred_points

    @property
    def label(self) -> str:
        if self.direct_points >= 3.0:
            return "Directly human-tagged"
        if self.metadata_points >= 3.0:
            return "Explicit in capability metadata"
        if self.score >= 5.0 and len(self.reasons) >= 2:
            return "Strongly evidenced"
        if self.score >= 3.0:
            return "Moderately evidenced"
        if self.score > 0:
            return "Contextual opportunity"
        return "Not evidenced"


@dataclass
class ModuleAnalysis:
    module: Module
    ai_outcomes: list[OutcomeOccurrence]
    dimensions: dict[str, DimensionEvidence]

    @property
    def direct_human_skills(self) -> list[OutcomeOccurrence]:
        return [o for o in self.module.outcomes if o.human_tag]

    @property
    def metadata_human_skills(self) -> list[OutcomeOccurrence]:
        return [
            o
            for o in self.module.outcomes
            if o.meta_category
            or any(c in {"human-social", "personal-reflective", "creative-aesthetic"} for c in o.clusters)
        ]

    @property
    def integrated(self) -> bool:
        return bool(self.ai_outcomes) and any(ev.score >= 3 for ev in self.dimensions.values())


# ---------------------------------------------------------------------------
# Generic helpers
# ---------------------------------------------------------------------------
def clean_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).replace("\u00a0", " ").replace("\u200b", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\s*\n\s*", "\n", text)
    return text.strip()


def natural_sort_key(text: str) -> list[Any]:
    return [int(p) if p.isdigit() else p.lower() for p in re.split(r"(\d+)", text)]


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return data


def localized_value(value: Any, language: str) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return clean_text(value)
    if isinstance(value, Mapping):
        return clean_text(value.get("value", ""))
    if not isinstance(value, Sequence):
        return clean_text(value)
    candidates = [item for item in value if isinstance(item, Mapping)]
    requested = language.lower()
    base = requested.split("-")[0]
    for item in candidates:
        if str(item.get("language", "")).lower() == requested:
            return clean_text(item.get("value", ""))
    for item in candidates:
        if str(item.get("language", "")).lower().split("-")[0] == base:
            return clean_text(item.get("value", ""))
    for preferred in ("en-GB", "de-DE", "en", "de"):
        for item in candidates:
            item_lang = str(item.get("language", "")).lower()
            if item_lang == preferred.lower() or item_lang.split("-")[0] == preferred.split("-")[0].lower():
                return clean_text(item.get("value", ""))
    return clean_text(candidates[0].get("value", "")) if candidates else ""


def unique_sorted(values: Iterable[str]) -> list[str]:
    return sorted({clean_text(v) for v in values if clean_text(v)}, key=natural_sort_key)


def first_present(*values: Any) -> Any:
    for value in values:
        if value is not None and value != "":
            return value
    return None


def as_number(value: Any) -> float | None:
    try:
        if value in (None, ""):
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


def study_load(module: Mapping[str, Any], unit: str) -> float | None:
    for item in module.get("studyLoad", []) or []:
        if isinstance(item, Mapping) and str(item.get("studyLoadUnit", "")).lower() == unit.lower():
            return as_number(item.get("value"))
    return None


def normalise_bloom(value: Any) -> str:
    raw = clean_text(value).lower()
    if raw in {"remember", "understand", "apply", "analyze", "analyse", "evaluate", "create"}:
        return "analyze" if raw == "analyse" else raw
    if "create" in raw or "gestalt" in raw:
        return "create"
    if "evaluat" in raw or "bewert" in raw:
        return "evaluate"
    if "analy" in raw:
        return "analyze"
    if "apply" in raw or "anwend" in raw:
        return "apply"
    if "understand" in raw or "versteh" in raw:
        return "understand"
    if "remember" in raw or "foundation" in raw or "grundlage" in raw:
        return "remember"
    if raw in {"l1", "1"}:
        return "remember"
    if raw in {"l2", "2"}:
        return "understand"
    if raw in {"l3", "3"}:
        return "analyze"
    if raw in {"l4", "4"}:
        return "evaluate"
    return "unknown"


def level_from_code_or_bloom(code: str, bloom: str) -> int:
    match = re.match(r"^[A-Z]+-(\d)-", code or "")
    if match:
        return int(match.group(1))
    return BLOOM_LEVEL.get(bloom, 0)


def module_stream(data: Mapping[str, Any]) -> str:
    ext = data.get("ext") or {}
    new_study = ext.get("newStudy") or {}
    return clean_text(first_present(ext.get("x-dhbw-stream"), new_study.get("stream"), data.get("stream")))


def module_year(data: Mapping[str, Any]) -> str:
    ext = data.get("ext") or {}
    new_study = ext.get("newStudy") or {}
    return clean_text(first_present(ext.get("x-dhbw-academic-year"), new_study.get("year"), data.get("academicYear"), data.get("year")))


def module_semester(data: Mapping[str, Any]) -> str:
    ext = data.get("ext") or {}
    new_study = ext.get("newStudy") or {}
    value = first_present(
        data.get("semester"), data.get("term"), ext.get("x-dhbw-semester"),
        ext.get("x-dhbw-recommended-semester"), ext.get("x-dhbw-term"), new_study.get("semester")
    )
    if isinstance(value, Sequence) and not isinstance(value, str):
        return ", ".join(clean_text(v) for v in value if clean_text(v))
    return clean_text(value)


def markdown_escape(value: Any) -> str:
    return clean_text(value).replace("|", "\\|").replace("\n", "<br>")


def stable_anchor(code: str) -> str:
    slug = re.sub(r"[^a-z0-9_-]+", "-", clean_text(code).lower()).strip("-")
    return f"module-{slug or 'unknown'}"


def bar(value: float, maximum: float, width: int = 10) -> str:
    if maximum <= 0:
        return "░" * width
    filled = max(0, min(width, round((value / maximum) * width)))
    return "█" * filled + "░" * (width - filled)


def md_table(headers: Sequence[str], rows: Sequence[Sequence[Any]]) -> list[str]:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(markdown_escape(v) for v in row) + " |")
    return lines


def first_sentence(text: str, max_chars: int = 180) -> str:
    text = clean_text(text)
    if not text:
        return ""
    parts = re.split(r"(?<=[.!?])\s+", text)
    sentence = parts[0]
    if len(sentence) <= max_chars:
        return sentence
    return sentence[: max_chars - 1].rstrip() + "…"


# ---------------------------------------------------------------------------
# Codebook and module loading
# ---------------------------------------------------------------------------
class CodebookIndex:
    def __init__(self, data: Mapping[str, Any], language: str):
        self.domains_by_code: dict[str, DomainInfo] = {}
        self.domains_by_id: dict[str, DomainInfo] = {}
        self.skills_by_code: dict[str, SkillInfo] = {}
        self.skills_by_id: dict[str, SkillInfo] = {}

        for row in data.get("learningOutcomes", []) or []:
            if not isinstance(row, Mapping):
                continue
            primary = row.get("primaryCode") or {}
            if clean_text(primary.get("codeType")) != "x-dhbw-domain":
                continue
            code = clean_text(primary.get("code"))
            if not code:
                continue
            domain = DomainInfo(
                code=code,
                name=localized_value(row.get("name"), language) or code,
                description=localized_value(row.get("description"), language),
                outcome_id=clean_text(row.get("learningOutcomeId")),
            )
            self.domains_by_code[code] = domain
            if domain.outcome_id:
                self.domains_by_id[domain.outcome_id] = domain

        for row in data.get("learningOutcomes", []) or []:
            if not isinstance(row, Mapping):
                continue
            primary = row.get("primaryCode") or {}
            if clean_text(primary.get("codeType")) != "x-dhbw-competence-id":
                continue
            code = clean_text(primary.get("code"))
            if not code:
                continue
            ext = row.get("ext") or {}
            domain_code = ""
            for parent_id in row.get("parentIds", []) or []:
                parent = self.domains_by_id.get(clean_text(parent_id))
                if parent:
                    domain_code = parent.code
                    break
            if not domain_code:
                domain_code = code.split("-")[0]
            ai_domains = tuple(unique_sorted(ext.get("x-dhbw-ai_domain") or []))
            meta_skills = tuple(unique_sorted(ext.get("x-dhbw-meta-skills") or []))
            ai_related = bool(ext.get("x-dhbw-ai_related")) or bool(ai_domains) or any(
                value.lower() == "ai-upskilling" for value in meta_skills
            )
            skill = SkillInfo(
                code=code,
                name=localized_value(row.get("name"), language) or code,
                description=localized_value(row.get("description"), language),
                domain_code=domain_code,
                bloom=normalise_bloom(first_present(row.get("complexityLevel"), ext.get("x-dhbw-bloom_category"))),
                ai_related=ai_related,
                ai_domains=ai_domains,
                human_tag=clean_text(ext.get("x-dhbw-human_skill_tag")),
                clusters=tuple(unique_sorted(ext.get("x-dhbw-clusters") or [])),
                meta_skills=meta_skills,
                meta_category=clean_text(ext.get("x-dhbw-meta_skill_category")),
                outcome_id=clean_text(row.get("learningOutcomeId")),
            )
            self.skills_by_code[code] = skill
            if skill.outcome_id:
                self.skills_by_id[skill.outcome_id] = skill

    def skill_for(self, outcome: Mapping[str, Any]) -> SkillInfo | None:
        primary = outcome.get("primaryCode") or {}
        code = clean_text(primary.get("code"))
        outcome_id = clean_text(outcome.get("learningOutcomeId"))
        return self.skills_by_code.get(code) or self.skills_by_id.get(outcome_id)

    def domain_name(self, code: str) -> str:
        return self.domains_by_code.get(code, DomainInfo(code, code or "Unclassified")).name


def load_modules(directory: Path, pattern: str, codebook: CodebookIndex, language: str) -> list[Module]:
    paths = sorted(directory.glob(pattern), key=lambda p: natural_sort_key(p.name))
    if not paths:
        raise FileNotFoundError(f"No module files matched {pattern!r} in {directory.resolve()}")

    modules: list[Module] = []
    errors: list[str] = []
    seen: dict[str, Path] = {}

    for path in paths:
        try:
            data = load_json(path)
            code = clean_text(data.get("code")) or path.stem
            if code in seen:
                raise ValueError(f"Duplicate module code {code!r}: {seen[code].name} and {path.name}")
            seen[code] = path
            assessment = localized_value(data.get("assessment"), language)
            module = Module(
                path=path,
                code=code,
                title=localized_value(data.get("name"), language) or code,
                description=localized_value(data.get("description"), language),
                stream=module_stream(data) or "Unassigned",
                year=module_year(data) or "Unspecified",
                semester=module_semester(data),
                ects=study_load(data, "ects") or 0.0,
                assessment=assessment,
            )
            for outcome in data.get("learningOutcomes", []) or []:
                if not isinstance(outcome, Mapping):
                    continue
                primary = outcome.get("primaryCode") or {}
                code_from_module = clean_text(primary.get("code"))
                skill = codebook.skill_for(outcome)
                outcome_ext = outcome.get("ext") or {}
                if skill:
                    skill_code = code_from_module or skill.code
                    bloom = normalise_bloom(first_present(outcome.get("complexityLevel"), skill.bloom))
                    occurrence = OutcomeOccurrence(
                        code=skill_code,
                        name=localized_value(outcome.get("name"), language) or skill.name,
                        description=localized_value(outcome.get("description"), language) or skill.description,
                        domain_code=skill.domain_code,
                        domain_name=codebook.domain_name(skill.domain_code),
                        bloom=bloom,
                        level=level_from_code_or_bloom(skill_code, bloom),
                        ai_related=skill.ai_related,
                        ai_domains=skill.ai_domains,
                        human_tag=skill.human_tag,
                        clusters=skill.clusters,
                        meta_skills=skill.meta_skills,
                        meta_category=skill.meta_category,
                    )
                else:
                    skill_code = code_from_module or clean_text(outcome.get("learningOutcomeId"))
                    domain_code = skill_code.split("-")[0] if "-" in skill_code else "UNCL"
                    ai_domains = tuple(unique_sorted(outcome_ext.get("x-dhbw-ai_domain") or []))
                    meta_skills = tuple(unique_sorted(outcome_ext.get("x-dhbw-meta-skills") or []))
                    bloom = normalise_bloom(outcome.get("complexityLevel"))
                    occurrence = OutcomeOccurrence(
                        code=skill_code,
                        name=localized_value(outcome.get("name"), language) or skill_code,
                        description=localized_value(outcome.get("description"), language),
                        domain_code=domain_code,
                        domain_name=codebook.domain_name(domain_code),
                        bloom=bloom,
                        level=level_from_code_or_bloom(skill_code, bloom),
                        ai_related=bool(outcome_ext.get("x-dhbw-ai_related")) or bool(ai_domains),
                        ai_domains=ai_domains,
                        human_tag=clean_text(outcome_ext.get("x-dhbw-human_skill_tag")),
                        clusters=tuple(unique_sorted(outcome_ext.get("x-dhbw-clusters") or [])),
                        meta_skills=meta_skills,
                        meta_category=clean_text(outcome_ext.get("x-dhbw-meta_skill_category")),
                    )
                module.outcomes.append(occurrence)
            modules.append(module)
        except Exception as exc:
            errors.append(f"{path.name}: {exc}")

    if errors:
        raise ValueError("Problems while reading module files:\n- " + "\n- ".join(errors))

    def sort_key(module: Module) -> tuple[Any, ...]:
        return (
            natural_sort_key(module.year),
            natural_sort_key(module.semester),
            natural_sort_key(module.stream),
            natural_sort_key(module.code),
        )

    return sorted(modules, key=sort_key)


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------
def add_evidence(
    evidence: dict[str, DimensionEvidence],
    dimension: str,
    *,
    direct: float = 0.0,
    metadata: float = 0.0,
    inferred: float = 0.0,
    skill_code: str = "",
    reason: str = "",
    snippet: str = "",
) -> None:
    item = evidence.setdefault(dimension, DimensionEvidence())
    item.direct_points += direct
    item.metadata_points += metadata
    item.inferred_points += inferred
    if skill_code:
        if direct:
            item.direct_skills.add(skill_code)
        if metadata:
            item.metadata_skills.add(skill_code)
        if inferred:
            item.inferred_skills.add(skill_code)
    if reason:
        item.reasons.add(reason)
    if snippet and snippet not in item.snippets and len(item.snippets) < 4:
        item.snippets.append(snippet)


def keyword_matches(text: str, keywords: Sequence[str]) -> list[str]:
    lower = text.lower()
    return [keyword for keyword in keywords if keyword.lower() in lower]


def analyse_module(module: Module) -> ModuleAnalysis:
    evidence: dict[str, DimensionEvidence] = {
        name: DimensionEvidence() for name in HUMAN_DIMENSIONS
    }

    # Module-level context: title, description and assessment format.
    context_text = " ".join([module.title, module.description, module.assessment]).lower()
    for marker, dimensions in FORMAT_KEYWORDS.items():
        if marker in context_text:
            for dimension in dimensions:
                add_evidence(
                    evidence,
                    dimension,
                    inferred=1.0,
                    reason=f"Module format or title contains ‘{marker}’",
                    snippet=first_sentence(module.description or module.assessment),
                )

    ai_outcomes: list[OutcomeOccurrence] = []
    for outcome in module.outcomes:
        if outcome.ai_related:
            ai_outcomes.append(outcome)

        text = " ".join([module.title, module.description, module.assessment, outcome.name, outcome.description])

        # Explicit human tags are the strongest evidence.
        if outcome.human_tag:
            for dimension in HUMAN_TAG_TO_DIMENSIONS.get(outcome.human_tag.lower(), ()): 
                add_evidence(
                    evidence,
                    dimension,
                    direct=3.0,
                    skill_code=outcome.code,
                    reason=f"Explicit human-skill tag: {outcome.human_tag}",
                    snippet=first_sentence(outcome.description),
                )

        # Capability clusters are explicit codebook metadata, but broader than a
        # direct human tag, so they receive a lower evidence weight.
        for cluster in outcome.clusters:
            for dimension in CLUSTER_TO_DIMENSIONS.get(cluster.lower(), ()): 
                add_evidence(
                    evidence,
                    dimension,
                    metadata=1.5,
                    skill_code=outcome.code,
                    reason=f"Capability cluster: {cluster}",
                    snippet=first_sentence(outcome.description),
                )

        if outcome.meta_category:
            for dimension in META_CATEGORY_TO_DIMENSIONS.get(outcome.meta_category.lower(), ()): 
                add_evidence(
                    evidence,
                    dimension,
                    metadata=2.0,
                    skill_code=outcome.code,
                    reason=f"Meta-skill category: {outcome.meta_category}",
                    snippet=first_sentence(outcome.description),
                )

        # Domain inference makes inherent human capabilities visible. It is
        # intentionally separated from formal tags in the report.
        for dimension in DOMAIN_TO_HUMAN_DIMENSIONS.get(outcome.domain_code, ()): 
            add_evidence(
                evidence,
                dimension,
                inferred=0.8,
                skill_code=outcome.code,
                reason=f"Inherent in competence domain {outcome.domain_code} ({outcome.domain_name})",
                snippet=first_sentence(outcome.description),
            )

        # Wording evidence catches design thinking, stakeholder interaction,
        # societal problems, project work and interdisciplinary practice even
        # where the codebook has not tagged them directly.
        for dimension, config in HUMAN_DIMENSIONS.items():
            matches = keyword_matches(text, config["keywords"])
            if matches:
                # Cap keyword evidence to avoid long descriptions overwhelming
                # the more authoritative codebook metadata.
                points = min(1.5, 0.45 * len(set(matches)))
                add_evidence(
                    evidence,
                    dimension,
                    inferred=points,
                    skill_code=outcome.code,
                    reason="Wording evidence: " + ", ".join(sorted(set(matches))[:4]),
                    snippet=first_sentence(outcome.description),
                )

        # AI outcomes with societal, governance, cognitive or agency tags are
        # themselves evidence that AI is taught together with human judgement.
        for ai_domain in outcome.ai_domains:
            if ai_domain in {"ethics", "governance", "societal", "sociocultural"}:
                add_evidence(
                    evidence,
                    "Ethical and societal judgement",
                    metadata=1.5,
                    skill_code=outcome.code,
                    reason=f"AI domain explicitly includes {ai_domain}",
                    snippet=first_sentence(outcome.description),
                )
            if ai_domain in {"cognitive", "agency"}:
                add_evidence(
                    evidence,
                    "Critical judgement and analytical independence",
                    metadata=1.5,
                    skill_code=outcome.code,
                    reason=f"AI domain explicitly includes {ai_domain}",
                    snippet=first_sentence(outcome.description),
                )
                add_evidence(
                    evidence,
                    "Self-direction, reflection and resilience",
                    metadata=1.0,
                    skill_code=outcome.code,
                    reason=f"AI domain explicitly includes {ai_domain}",
                    snippet=first_sentence(outcome.description),
                )

    return ModuleAnalysis(module=module, ai_outcomes=ai_outcomes, dimensions=evidence)


def analyse_modules(modules: list[Module]) -> list[ModuleAnalysis]:
    return [analyse_module(module) for module in modules]


def ai_family_for_domain(domain: str) -> str:
    for family, domains in AI_FAMILIES.items():
        if domain in domains:
            return family
    return "Other / unclassified AI capability"


def aggregate_dimension_evidence(analyses: Sequence[ModuleAnalysis]) -> dict[str, DimensionEvidence]:
    aggregate = {name: DimensionEvidence() for name in HUMAN_DIMENSIONS}
    for analysis in analyses:
        for name, item in analysis.dimensions.items():
            target = aggregate[name]
            target.direct_points += item.direct_points
            target.metadata_points += item.metadata_points
            target.inferred_points += item.inferred_points
            target.direct_skills.update(item.direct_skills)
            target.metadata_skills.update(item.metadata_skills)
            target.inferred_skills.update(item.inferred_skills)
            target.reasons.update(item.reasons)
            for snippet in item.snippets:
                if snippet not in target.snippets and len(target.snippets) < 6:
                    target.snippets.append(snippet)
    return aggregate


def group_analyses(analyses: Sequence[ModuleAnalysis], attribute: str) -> dict[str, list[ModuleAnalysis]]:
    grouped: dict[str, list[ModuleAnalysis]] = defaultdict(list)
    for analysis in analyses:
        value = clean_text(getattr(analysis.module, attribute)) or "Unspecified"
        grouped[value].append(analysis)
    return dict(sorted(grouped.items(), key=lambda item: natural_sort_key(item[0])))


def narrative_summary(analyses: Sequence[ModuleAnalysis]) -> list[str]:
    modules = [a.module for a in analyses]
    ai_modules = [a for a in analyses if a.ai_outcomes]
    integrated = [a for a in analyses if a.integrated]
    all_ai = [o for a in analyses for o in a.ai_outcomes]
    ai_domains = Counter(domain for o in all_ai for domain in o.ai_domains)
    ai_levels = Counter(o.level for o in all_ai)
    human = aggregate_dimension_evidence(analyses)
    strongest = sorted(human.items(), key=lambda kv: (-kv[1].score, kv[0]))[:3]
    weakest = sorted(human.items(), key=lambda kv: (kv[1].score, kv[0]))[:3]

    paragraphs: list[str] = []
    if all_ai:
        high = sum(count for level, count in ai_levels.items() if level >= 3)
        high_share = high / len(all_ai) if all_ai else 0
        families = Counter(ai_family_for_domain(domain) for domain in ai_domains.elements())
        top_families = ", ".join(name for name, _ in families.most_common(3))
        module_word = "module" if len(modules) == 1 else "modules"
        skill_word = "skill" if len({o.code for o in all_ai}) == 1 else "skills"
        occurrence_word = "occurrence" if len(all_ai) == 1 else "occurrences"
        paragraphs.append(
            f"Across **{len(modules)} selected {module_word}**, New Study contains **{len({o.code for o in all_ai})} unique AI-related {skill_word}** "
            f"appearing in {len(all_ai)} {occurrence_word}. {high_share:.0%} of these occurrences are encoded at analytical, evaluative or design level "
            f"(levels 3–4), rather than only at introductory tool-use level. The strongest AI capability families are **{top_families or 'not yet classifiable'}**."
        )
    else:
        module_word = "module" if len(modules) == 1 else "modules"
        paragraphs.append(
            f"Across **{len(modules)} selected {module_word}**, no learning outcomes were marked as AI-related in the supplied codebook. "
            "This may reflect the selected files rather than the full curriculum."
        )

    if strongest:
        strongest_text = ", ".join(f"**{name}**" for name, _ in strongest)
        paragraphs.append(
            "The human side of the curriculum is broader than the explicit `human_skill_tag` field. "
            f"When direct tags, capability clusters, competence domains and module designs are considered together, the strongest dimensions are {strongest_text}. "
            "This is the programme’s hidden human curriculum: capabilities carried by projects, design work, research, communication, ethics and interdisciplinary problem-solving rather than isolated as generic ‘soft-skill’ modules."
        )

    if ai_modules:
        ai_module_word = "module" if len(ai_modules) == 1 else "modules"
        show_word = "shows" if len(ai_modules) == 1 else "show"
        paragraphs.append(
            f"**{len(integrated)} of {len(ai_modules)} AI-bearing {ai_module_word}** {show_word} moderate or strong evidence of human capabilities. "
            "Those modules are especially important because they teach students not merely to operate AI, but to question, explain, govern and situate it in human contexts."
        )

    if weakest:
        weak_names = ", ".join(f"**{name}**" for name, item in weakest if item.score < 3)
        if weak_names:
            paragraphs.append(
                f"The least visible dimensions in the selected data are {weak_names}. This is a curriculum-design signal, not proof of absence: "
                "the module JSON may omit teaching formats or assessment practices that develop these capabilities."
            )

    return paragraphs


# ---------------------------------------------------------------------------
# Markdown generation
# ---------------------------------------------------------------------------
def build_markdown(
    analyses: list[ModuleAnalysis],
    output: Path,
    title: str,
    programme: str,
    institution: str,
    include_front_matter: bool = True,
) -> None:
    modules = [a.module for a in analyses]
    all_outcomes = [o for module in modules for o in module.outcomes]
    all_ai = [o for a in analyses for o in a.ai_outcomes]
    direct_human = [o for a in analyses for o in a.direct_human_skills]
    metadata_human = [o for a in analyses for o in a.metadata_human_skills]
    unique_ai = {o.code: o for o in all_ai}
    unique_direct_human = {o.code: o for o in direct_human}
    unique_metadata_human = {o.code: o for o in metadata_human}
    ai_domains = Counter(domain for o in all_ai for domain in o.ai_domains)
    human_aggregate = aggregate_dimension_evidence(analyses)
    streams = unique_sorted(module.stream for module in modules)
    years = unique_sorted(module.year for module in modules)
    integrated_modules = [a for a in analyses if a.integrated]

    lines: list[str] = []
    if include_front_matter:
        lines.extend(["---", "layout: page", f'title: "{title}"', "---", ""])

    lines.extend([
        f"# {title}",
        "",
        f"**{programme}**  ",
        f"{institution}  ",
        f"Assembled {date.today().isoformat()}",
        "",
        "> This report is generated from the selected machine-readable module files and the competence codebook. "
        "It distinguishes **formal tags** from **transparent curriculum inference**. Inferred human capabilities are evidence-based interpretations of domains, wording and learning formats; they are not new formal learning outcomes.",
        "",
        "<a id=\"executive-reading\"></a>",
        "## Executive reading",
        "",
    ])
    for paragraph in narrative_summary(analyses):
        lines.extend([paragraph, ""])

    lines.extend([
        "## Portfolio snapshot",
        "",
    ])
    snapshot_rows = [
        ["Modules analysed", len(modules)],
        ["ECTS represented", f"{sum(m.ects for m in modules):g}"],
        ["Streams represented", len(streams)],
        ["Academic years represented", len(years)],
        ["Unique learning outcomes", len({o.code for o in all_outcomes if o.code})],
        ["Unique AI-related skills", len(unique_ai)],
        ["Direct human-tagged skills", len(unique_direct_human)],
        ["Human-oriented metadata skills", len(unique_metadata_human)],
        ["Modules integrating AI and human capability", len(integrated_modules)],
    ]
    lines.extend(md_table(["Measure", "Value"], snapshot_rows))
    lines.extend(["", "## How the analysis works", ""])
    lines.extend([
        "- **Explicit AI evidence** comes from `x-dhbw-ai_related`, `x-dhbw-ai_domain`, or an `ai-upskilling` marker in the competence codebook.",
        "- **Explicit human evidence** comes from `x-dhbw-human_skill_tag`, human-oriented capability clusters and meta-skill categories.",
        "- **Inherent human evidence** is inferred from competence domains such as Communication, Ethics, Personal Development, Project Management, Research, Analysis and Architecture.",
        "- **Contextual evidence** comes from module titles, descriptions, assessments and learning-outcome wording: for example project work, design thinking, stakeholder interaction, group work, societal problems or interdisciplinary integration.",
        "- The analysis measures **curricular intent and opportunity**, not actual student attainment. Delivery quality and assessment validity still require human review.",
        "",
        '<a id="module-navigation"></a>',
        "## Module navigation",
        "",
    ])
    nav_rows = []
    for a in analyses:
        m = a.module
        nav_rows.append([
            m.code,
            f"[{m.title}](#{stable_anchor(m.code)})",
            m.stream,
            m.year,
            m.semester or "—",
            len(a.ai_outcomes),
            len([d for d in a.dimensions.values() if d.score >= 3]),
        ])
    lines.extend(md_table(["Code", "Module", "Stream", "Year", "Semester", "AI LOs", "Human dimensions ≥ moderate"], nav_rows))

    # AI section
    lines.extend(["", "<a id=\"ai-readiness\"></a>", "## AI readiness", ""])
    if not all_ai:
        lines.extend(["No AI-related learning outcomes were identified in the selected module files.", ""])
    else:
        level_rows = []
        max_level_count = max(Counter(o.level for o in all_ai).values(), default=1)
        for level in (1, 2, 3, 4):
            occurrences = [o for o in all_ai if o.level == level]
            modules_at_level = {a.module.code for a in analyses if any(o.level == level for o in a.ai_outcomes)}
            examples = "; ".join(unique_sorted(o.name for o in occurrences)[:4]) or "—"
            level_rows.append([
                f"L{level}", LEVEL_LABEL[level], len({o.code for o in occurrences}), len(occurrences),
                len(modules_at_level), bar(len(occurrences), max_level_count), examples,
            ])
        lines.extend(md_table(
            ["Level", "Interpretation", "Unique skills", "Occurrences", "Modules", "Relative emphasis", "Examples"],
            level_rows,
        ))
        lines.extend(["", "### AI capability domains", ""])
        domain_rows = []
        max_ai_domain = max(ai_domains.values(), default=1)
        for domain, count in ai_domains.most_common():
            domain_rows.append([
                AI_DOMAIN_LABELS.get(domain, domain.replace("-", " ").title()),
                ai_family_for_domain(domain),
                count,
                bar(count, max_ai_domain),
                len({a.module.code for a in analyses if any(domain in o.ai_domains for o in a.ai_outcomes)}),
            ])
        lines.extend(md_table(["AI domain", "Capability family", "Occurrences", "Relative emphasis", "Modules"], domain_rows))

        lines.extend(["", "### AI progression by academic year", ""])
        year_rows = []
        for year, group in group_analyses(analyses, "year").items():
            outcomes = [o for a in group for o in a.ai_outcomes]
            year_rows.append([
                year,
                len(group),
                len({o.code for o in outcomes}),
                len(outcomes),
                f"{mean([o.level for o in outcomes]):.2f}" if outcomes else "—",
                ", ".join(unique_sorted(d for o in outcomes for d in o.ai_domains)) or "—",
            ])
        lines.extend(md_table(["Year", "Modules", "Unique AI skills", "AI occurrences", "Average AI level", "AI domains"], year_rows))

        lines.extend(["", "### AI coverage by stream", ""])
        stream_rows = []
        for stream, group in group_analyses(analyses, "stream").items():
            outcomes = [o for a in group for o in a.ai_outcomes]
            stream_rows.append([
                stream,
                len(group),
                len({o.code for o in outcomes}),
                len(outcomes),
                f"{mean([o.level for o in outcomes]):.2f}" if outcomes else "—",
                ", ".join(unique_sorted(ai_family_for_domain(d) for o in outcomes for d in o.ai_domains)) or "—",
            ])
        lines.extend(md_table(["Stream", "Modules", "Unique AI skills", "Occurrences", "Average level", "Capability families"], stream_rows))

        lines.extend(["", "### AI skill inventory", ""])
        ai_inventory_rows = []
        for code, outcome in sorted(unique_ai.items(), key=lambda item: (item[1].level, natural_sort_key(item[0]))):
            modules_with = [a.module.code for a in analyses if any(o.code == code for o in a.ai_outcomes)]
            ai_inventory_rows.append([
                code,
                outcome.name,
                f"L{outcome.level}",
                LEVEL_LABEL.get(outcome.level, "Unspecified"),
                ", ".join(AI_DOMAIN_LABELS.get(d, d) for d in outcome.ai_domains) or "AI-related, domain not specified",
                ", ".join(modules_with),
            ])
        lines.extend(md_table(["Code", "AI skill", "Level", "Cognitive role", "AI domains", "Modules"], ai_inventory_rows))

    # Human capabilities section
    lines.extend(["", "<a id=\"human-capabilities\"></a>", "## Human capabilities: the visible and hidden curriculum", ""])
    lines.extend([
        "The table below combines explicit codebook metadata with inherent and contextual evidence. The distinction matters: a programme can teach collaboration, human-centred design or societal judgement through authentic work even when the corresponding learning outcome is filed under a technical domain.",
        "",
    ])
    dimension_rows = []
    max_human_score = max((item.score for item in human_aggregate.values()), default=1)
    for name, item in sorted(human_aggregate.items(), key=lambda kv: (-kv[1].score, kv[0])):
        modules_with = []
        streams_with = []
        for a in analyses:
            ev = a.dimensions[name]
            if ev.score > 0:
                modules_with.append(a.module.code)
                streams_with.append(a.module.stream)
        example = item.snippets[0] if item.snippets else "—"
        dimension_rows.append([
            name,
            item.label,
            f"{item.score:.1f}",
            bar(item.score, max_human_score),
            len(set(modules_with)),
            len(set(streams_with)),
            len(item.direct_skills),
            len(item.metadata_skills),
            len(item.inferred_skills),
            example,
        ])
    lines.extend(md_table(
        ["Human capability", "Evidence level", "Evidence score*", "Relative emphasis", "Modules", "Streams", "Direct tags", "Metadata skills", "Inferred skills", "Example evidence"],
        dimension_rows,
    ))
    lines.extend([
        "",
        "*The evidence score is a descriptive weighting used to rank visibility within this report. It is **not** a grade, accreditation score or measure of student performance.",
        "",
        "### Direct human-skill tags",
        "",
    ])
    if unique_direct_human:
        human_rows = []
        for code, outcome in sorted(unique_direct_human.items(), key=lambda item: natural_sort_key(item[0])):
            modules_with = [a.module.code for a in analyses if any(o.code == code for o in a.direct_human_skills)]
            human_rows.append([
                code,
                outcome.name,
                outcome.human_tag or "—",
                ", ".join(outcome.clusters) or "—",
                outcome.meta_category or "—",
                ", ".join(modules_with),
            ])
        lines.extend(md_table(["Code", "Skill", "Human tag", "Capability clusters", "Meta category", "Modules"], human_rows))
    else:
        lines.append("No direct `x-dhbw-human_skill_tag` values were found in the selected modules.")

    lines.extend(["", "### Broader human-oriented capability metadata", ""])
    if unique_metadata_human:
        metadata_rows = []
        for code, outcome in sorted(unique_metadata_human.items(), key=lambda item: natural_sort_key(item[0])):
            modules_with = [a.module.code for a in analyses if any(o.code == code for o in a.metadata_human_skills)]
            metadata_rows.append([
                code,
                outcome.name,
                ", ".join(outcome.clusters) or "—",
                outcome.meta_category or "—",
                ", ".join(modules_with),
            ])
        lines.extend(md_table(["Code", "Skill", "Capability clusters", "Meta category", "Modules"], metadata_rows))
    else:
        lines.append("No broader human-oriented capability clusters or meta-skill categories were found in the selected modules.")

    lines.extend(["", "### Human capability progression by academic year", ""])
    human_year_rows = []
    for year, group in group_analyses(analyses, "year").items():
        agg = aggregate_dimension_evidence(group)
        visible = [(name, item) for name, item in agg.items() if item.score > 0]
        top = ", ".join(name for name, _ in sorted(visible, key=lambda kv: (-kv[1].score, kv[0]))[:4]) or "—"
        human_year_rows.append([
            year,
            len(group),
            len([1 for _, item in visible if item.score >= 3]),
            sum(len(a.direct_human_skills) for a in group),
            sum(len(a.metadata_human_skills) for a in group),
            top,
        ])
    lines.extend(md_table(["Year", "Modules", "Dimensions ≥ moderate", "Direct-tag occurrences", "Metadata occurrences", "Strongest dimensions"], human_year_rows))

    lines.extend(["", "### Human capability by stream", ""])
    human_stream_rows = []
    for stream, group in group_analyses(analyses, "stream").items():
        agg = aggregate_dimension_evidence(group)
        top_names = [
            name
            for name, item in sorted(agg.items(), key=lambda kv: (-kv[1].score, kv[0]))
            if item.score > 0
        ][:4]
        top = ", ".join(top_names) or "—"
        human_stream_rows.append([
            stream,
            len(group),
            len({o.code for a in group for o in a.direct_human_skills}),
            len({o.code for a in group for o in a.metadata_human_skills}),
            len([1 for item in agg.values() if item.score >= 3]),
            top,
        ])
    lines.extend(md_table(["Stream", "Modules", "Direct-tag skills", "Metadata skills", "Dimensions ≥ moderate", "Strongest dimensions"], human_stream_rows))

    # AI-human integration
    lines.extend(["", "<a id=\"integration\"></a>", "## Where AI and human capability meet", ""])
    integration_rows = []
    for a in analyses:
        ai_names = unique_sorted(o.name for o in a.ai_outcomes)
        top_human = [
            name for name, item in sorted(a.dimensions.items(), key=lambda kv: (-kv[1].score, kv[0]))
            if item.score >= 3
        ][:4]
        if a.ai_outcomes and top_human:
            category = "Integrated AI + human capability"
        elif a.ai_outcomes:
            category = "AI present; human evidence limited"
        elif top_human:
            category = "Human capability present; AI not explicit"
        else:
            category = "Neither strongly visible in metadata"
        integration_rows.append([
            f"[{a.module.code}](#{stable_anchor(a.module.code)})",
            a.module.title,
            category,
            "; ".join(ai_names[:3]) or "—",
            "; ".join(top_human) or "—",
        ])
    lines.extend(md_table(["Module", "Title", "Profile", "AI examples", "Human dimensions"], integration_rows))

    # Module evidence profiles
    lines.extend(["", "<a id=\"module-profiles\"></a>", "## Module evidence profiles", ""])
    for a in analyses:
        m = a.module
        lines.extend([
            f'<a id="{stable_anchor(m.code)}"></a>',
            f"### {m.code} · {m.title}",
            "",
            f"**Stream:** {m.stream}  ",
            f"**Year / semester:** {m.year} / {m.semester or 'not specified'}  ",
            f"**ECTS:** {m.ects:g}  ",
            f"**Assessment:** {m.assessment or 'not specified'}",
            "",
        ])
        if m.description:
            lines.extend([m.description, ""])

        lines.extend(["#### AI capability", ""])
        if a.ai_outcomes:
            ai_rows = []
            for outcome in sorted(a.ai_outcomes, key=lambda o: (o.level, natural_sort_key(o.code))):
                ai_rows.append([
                    outcome.code,
                    outcome.name,
                    f"L{outcome.level}",
                    ", ".join(AI_DOMAIN_LABELS.get(d, d) for d in outcome.ai_domains) or "Unspecified",
                    outcome.description,
                ])
            lines.extend(md_table(["Code", "Skill", "Level", "AI domains", "Learning outcome"], ai_rows))
        else:
            lines.append("No AI-related learning outcomes are explicitly registered for this module.")

        lines.extend(["", "#### Human capability evidence", ""])
        human_rows = []
        for name, item in sorted(a.dimensions.items(), key=lambda kv: (-kv[1].score, kv[0])):
            if item.score <= 0:
                continue
            human_rows.append([
                name,
                item.label,
                f"{item.direct_points:.1f} direct + {item.metadata_points:.1f} metadata + {item.inferred_points:.1f} inferred",
                "; ".join(sorted(item.reasons)[:4]),
                item.snippets[0] if item.snippets else "—",
            ])
        if human_rows:
            lines.extend(md_table(["Dimension", "Evidence", "Basis", "Why it was detected", "Example"], human_rows))
        else:
            lines.append("No human-capability evidence was detected from the available metadata.")

        # Compact module interpretation.
        top_dims = [name for name, item in sorted(a.dimensions.items(), key=lambda kv: (-kv[1].score, kv[0])) if item.score >= 3][:3]
        if a.ai_outcomes and top_dims:
            interpretation = (
                f"This module integrates AI capability with **{', '.join(top_dims)}**. "
                "It therefore contributes to a graduate profile in which technical capability is coupled to human judgement and responsibility."
            )
        elif a.ai_outcomes:
            interpretation = (
                "This module contributes explicit AI capability, but the supplied metadata carries limited evidence of associated human capabilities. "
                "Reviewing teaching and assessment design may reveal additional human learning that is not yet encoded."
            )
        elif top_dims:
            interpretation = (
                f"This module primarily strengthens **{', '.join(top_dims)}**. "
                "These capabilities form part of the human foundation on which responsible AI practice later depends."
            )
        else:
            interpretation = "The available metadata does not support a strong AI or human-capability interpretation for this module."
        lines.extend(["", f"**Interpretation:** {interpretation}", "", "[↑ Back to module navigation](#module-navigation)", "", "---", ""])

    # Design questions and limitations
    lines.extend(["## Curriculum design questions generated by the evidence", ""])
    missing_ai_families = [family for family, domains in AI_FAMILIES.items() if not any(domain in ai_domains for domain in domains)]
    low_human = [name for name, item in sorted(human_aggregate.items(), key=lambda kv: kv[1].score) if item.score < 3]
    if missing_ai_families:
        lines.append("- **AI breadth:** the selected modules do not yet visibly cover " + ", ".join(missing_ai_families) + ".")
    if low_human:
        lines.append("- **Human-capability visibility:** the least visible dimensions are " + ", ".join(low_human[:4]) + ". They may need stronger learning outcomes, richer assessment evidence or simply better metadata.")
    ai_only = [a.module.code for a in analyses if a.ai_outcomes and not a.integrated]
    if ai_only:
        lines.append("- **AI–human coupling:** review " + ", ".join(ai_only) + " to determine whether judgement, communication, ethics or agency are taught but not yet encoded.")
    if not missing_ai_families and not low_human and not ai_only:
        lines.append("- The selected data shows broad and integrated coverage. The next step is validation against actual assessment tasks and student work.")

    lines.extend([
        "",
        "## Limitations",
        "",
        "- The report analyses the files selected by the filename pattern; it does not claim to represent modules that are absent from the directory.",
        "- Codebook tags are treated as authoritative metadata, but module-specific learning-outcome wording is retained where it differs from the codebook.",
        "- Domain and keyword inference identifies plausible human-capability learning. It cannot prove that the capability is taught well, assessed validly or achieved by students.",
        "- Repeated occurrence shows curricular emphasis, not independent breadth. The report therefore distinguishes unique skills from occurrences.",
        "- Semester progression can only be analysed where semester metadata exists in the JSON files.",
        "",
        "---",
        "",
        f"*Generated from {len(modules)} module files and one competence codebook.*",
        "",
    ])

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a Markdown analysis of AI readiness and human capabilities from module JSON files."
    )
    parser.add_argument("--dir", required=True, type=Path, help="Directory containing module JSON files")
    parser.add_argument("--pattern", default="T*INF*v6.json", help="Module filename glob pattern")
    parser.add_argument("--codebook", required=True, type=Path, help="Competence codebook JSON file")
    parser.add_argument("--output", type=Path, default=Path("New_Study_AI_Human_Capabilities.md"), help="Markdown output path")
    parser.add_argument("--language", default="en-GB", help="Preferred language for module and skill text")
    parser.add_argument("--title", default="AI and Human Capabilities in New Study")
    parser.add_argument("--programme", default="Bachelor of Computer Science (B.Sc.)")
    parser.add_argument("--institution", default="Open University of Germany (OUG)")
    parser.add_argument("--no-front-matter", action="store_true", help="Do not add Jekyll front matter")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if not args.dir.exists() or not args.dir.is_dir():
            raise FileNotFoundError(f"Module directory does not exist: {args.dir}")
        if not args.codebook.exists():
            raise FileNotFoundError(f"Codebook does not exist: {args.codebook}")
        codebook = CodebookIndex(load_json(args.codebook), args.language)
        modules = load_modules(args.dir, args.pattern, codebook, args.language)
        analyses = analyse_modules(modules)
        build_markdown(
            analyses=analyses,
            output=args.output,
            title=args.title,
            programme=args.programme,
            institution=args.institution,
            include_front_matter=not args.no_front_matter,
        )
        print(f"Created {args.output.resolve()}")
        print(f"Analysed {len(modules)} module files.")
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
