---
layout: page
title: OOAPI v6 — Machine-Readable Module Data
---

# OOAPI v6 — Machine-Readable Module Data

[← Back to Curriculum & Pedagogy](../index.md)

This folder holds the machine-readable side of the curriculum: one [OOAPI](https://ooapi.org/) v6-formatted JSON file per module, plus the competency codebook they're built against. Where documents like the [Didactic Framework](../didactic-framework-bsc-cs.md) and [New Study Programme Document](../new-study-programme-document.md) describe the curriculum in prose, these files are the structured data the [Platform](../platform-living-learning-system.md) and the curriculum designer tool actually read.

## How These Files Are Produced

This is generated output, not hand-authored — regenerating it means re-running the pipeline, not editing JSON by hand. Per the original processing notes:

1. **Source course JSONs** (e.g. `T4INF1602_suggestion.json`) contain the raw competences, study load, and module content.
2. **`batch_converter.py`** reads the source JSONs and produces standardised `OOAPI_V5/` and `OOAPI_V6/` folders — this folder is that v6 output.
3. **`generate_codebook.py`** reads the raw competence codebook and produces the OOAPI-formatted codebook (`competence_codebook_v11_ooapi.json` below).
4. **`build_curriculum_index.py`** reads the v6 module JSONs and the codebook, and produces `curriculum_index.json` and `edges.json` (not currently in this folder).
5. **`curriculum_designer.html`** — an interactive tool — loads that index and renders the curriculum graph.

If the source data changes, the fix goes in upstream (the source JSONs or the scripts), then the pipeline re-runs — not a direct edit to the files listed below.

## What's Here

### Module specifications (31 files)

One `{code}_ooapi_v6.json` per module: `T4_1000`, `T4_2000`, `T4_3000`, `T4INF1001`–`T4INF1007`, `T4INF1101`, `T4INF1601`, `T4INF1602`, `T4INF2001`–`T4INF2006`, `T4INF2601`, `T4INF3102`, `T4INF3103`, `T4INF3906`, `T4INF3915`, `T4INF4324`, `T4INF4348`, `T4INF4900`, `T4INF4900.1`, `T4INF4902`, `T4INF4902.1`, `T4INF9006`.

### Codebooks

- `competence_codebook_v10_ooapi.json`
- `competence_codebook_v11_ooapi.json`

Two versions are present — worth confirming which is the one actually feeding the current pipeline output before treating both as live.

### Pipeline artifacts

- `conversion_summary.json` — batch run metadata (31 files found, 31 converted, 0 failed, generated 2026-04-21)
- `information.txt` — the pipeline notes this index is based on

### Not migrated / ignore

- `.bmp` — 0 bytes, appears to be an empty artifact rather than a real file. Flagging rather than silently dropping it; delete if confirmed unneeded.

---

## Important: This Data Confirms a Conversion-Notes Discrepancy

The module codes in these files (`T4INF1004`, `T4INF1602`, `T4INF2001`–`2006`, `T4INF3102`, `T4INF3915`, `T4INF4900`, `T4INF4902`, `T4INF4348`, `T4INF4324`, `T4INF9006`, `T4_1000`/`T4_2000`/`T4_3000` …) **match the numbering used in the [Didactic Framework](../didactic-framework-bsc-cs.md)'s Module Architecture Table** — not the numbering used in the [New Study Programme Document](../new-study-programme-document.md) (which uses `T4INF1001`–`1006` for MAF, `T4INF3001`–`3102` for PSC, etc.).

Since this folder is machine-generated pipeline output rather than hand-written prose, it's reasonable to treat it as closer to a source of truth than either narrative document. See the updated entry in [conversion-notes.md](../../conversion-notes.md) — this doesn't fully close that question, but it's real evidence pointing at which document has the numbering drift.
