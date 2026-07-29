# Conversion Notes — Strategy & Finance

[← Back to Strategy & Finance](index.md)

Observations that surface while migrating strategy and finance documents from Drive to this repository. See [known-gaps.md](../known-gaps.md) for architecture-level gaps; this page is for smaller factual snags found while converting.

---

## Open

- [ ] **`OUG_Hagen_PatternSignature_Alignment.docx` referenced but not located.** [`role-statement.md`](role-statement.md) references this companion document twice as the source for "a full pattern signature alignment across twelve governance dimensions" comparing the OUG to FernUniversität Hagen. Not found in this repository or on Drive during conversion — worth a targeted search if it exists somewhere else, since it would be a substantial and directly relevant document if recovered.

- [ ] **The Five-Year Finance Plan's Part V arrived from the source with scrambled subsection ordering** — content for 5.4 appeared before 5.3, before 5.2, before 5.1, likely from how nested tables were extracted from the original docx. Reordered into logical sequence during conversion (5 → 5.1 → 5.2 → 5.3 → 5.4); no content was altered, only reordered. Flagged in case the original docx itself has a structural issue worth fixing at the source.

- [ ] **Finanzmodell v3.xlsx could not be reliably transferred.** Fetched from Drive as base64 and decoded, but the resulting file failed a zip/CRC integrity check (`Bad CRC-32 for file 'xl/styles.xml'`) — some corruption occurred in transit through the chat channel, despite the byte count matching the original exactly. Not delivered, to avoid handing over a file that looks fine but silently fails to open correctly. The original is untouched on Drive under `STRATEGY and FINANCE` — copy directly from there.

- [ ] **A second, unplanned finance spreadsheet exists on Drive:** `OpenUnivesity Planrechnung_Vordruck.xlsx`. Not in the original document plan, not converted. Appears to be an earlier or alternate financial planning template (different assumptions than Finanzmodell v3 — e.g. €20/ECTS pricing rather than €25, a 400-student Year 1 start rather than 50). Worth checking whether this is superseded by v3 or represents a genuinely different scenario worth preserving.

- [ ] **Two supporting technical files exist but aren't documents:** `write-excel.py` (the Python script that generates Finanzmodell v3.xlsx from `data.json`) and `data.json` (its input parameters). Not converted as markdown — noted here for completeness, since they explain how the finance model spreadsheet was actually produced and could be useful for regenerating or updating it.

## Resolved

- [x] **"Bug Protocol" gap closed.** Tracked in [known-gaps.md](../known-gaps.md) as a mechanism referenced elsewhere (including by name in the Five-Year Finance Plan's OKR discussion) but never located as its own document. It's fully specified in [`okr-framework-dashboard.md`](okr-framework-dashboard.md) § IV — a five-step process (Flag → Diagnose → Classify → Act → Learn) triggered when a Key Result scores below 0.4. known-gaps.md updated accordingly.

- [x] **`OUG_Communication_Architecture.docx` found misfiled in this domain's Drive folder.** Physically located in `STRATEGY and FINANCE` on Drive, but it's a communications document by content and by chapter 17's own domain plan. Used in the Presentation & Communication domain instead of here — not duplicated.
