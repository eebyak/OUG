---
layout: page
title: Curriculum & Pedagogy
---

# Curriculum & Pedagogy

[← Back to main index](../index.md)

The curriculum layer answers the question a prospective student, a partner university, and an accreditation reviewer all ask first: what, exactly, does a person study, and how do we know they learned it? The OUG's answer is built around three commitments that run through every document in this domain — the curriculum is modular down to the individual credential, it is organised around tasks and demonstrated competence rather than seat time, and it treats the absence of a physical campus as a design problem to be solved deliberately, not an inconvenience to be apologised for.

---


<div class="diagram-block">
  <a class="diagram-preview" href="#curriculum">
    <img
      src="{{ '/curriculum/images/Curriculum.png' | relative_url }}"
      alt="OUG Curriculum Map">
  </a>
  <p class="diagram-caption">Click the diagram to enlarge.</p>
</div>

<div id="curriculum" class="lightbox">
  <a class="lightbox-backdrop" href="#close" aria-label="Close"></a>

  <div class="lightbox-panel">
    <a class="lightbox-close" href="#close" aria-label="Close">×</a>

    <img
      src="{{ '/curriculum/images/Curriculum.png' | relative_url }}"
      alt="Enlarged OUG Curriculum Map">
  </div>
</div>


---

## What's Here

Documents are currently sitting as their original `.docx` source files while the migration to Markdown is worked through one at a time.

| Document | Status | Target filename |
|---|---|---|
| OUG_Didactic_Framework_BSc_CS.docx | ✅ Converted → [`didactic-framework-bsc-cs.md`](didactic-framework-bsc-cs.md) | — |
| OUG Equity by Design Principles.docx | ✅ Converted → [`equity-by-design.md`](equity-by-design.md) | — |
| OUG Platform Living Learning System.docx | ✅ Converted → [`platform-living-learning-system.md`](platform-living-learning-system.md) | — |
| OUG_Presence_Architecture.docx | ✅ Converted → [`presence-architecture.md`](presence-architecture.md) | — |
| OUG Research Doctoral Framework.docx | ✅ Converted → [`research-doctoral-framework.md`](research-doctoral-framework.md) | — |
| OUG_BSc_CS_New_Study_Programme_Document.docx | ✅ Converted → [`new-study-programme-document.md`](new-study-programme-document.md) | — |
| `skill-based-modules/` (per-module JSON) | ✅ Added | see note below |

### A note on `skill-based-modules/`

This folder isn't one of the nine documents chapter 17 described for this domain — it's new: structured, per-module JSON rather than narrative prose. Worth deciding at some point whether it belongs here as machine-readable module data feeding the eventual [Platform](platform-living-learning-system.md), or whether it should be documented separately as its own thing. Not resolving that now — just flagging it so it doesn't quietly get treated as if it was always part of the plan.

### `OOAPI_V6/`

Machine-readable module data — one OOAPI v6 JSON file per module, plus the competency codebook. See [`OOAPI_V6/index.md`](OOAPI_V6/index.md) for the full inventory and how it's generated. This data is also the source of real evidence on the module-numbering discrepancy tracked in [conversion-notes.md](../conversion-notes.md).

---

*This page is a snapshot, not a source of truth — the [main index](../index.md) is the canonical list of what this domain is meant to eventually contain. Update the table above as each document is added and converted.*
