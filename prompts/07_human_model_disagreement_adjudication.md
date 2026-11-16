# Third-look adjudication of human vs LLM coding (scoping review, AI underwater fish monitoring)

You adjudicate, against the FULL TEXT, every disagreement between a human expert coder and an LLM coder.
Never guess. Every final value other than NR must rest on a verbatim quote (<=25 words) from the paper with a page/section.

Inputs
- Codebook: /home/claude/adj/codebook.txt (S3a item and overall-rating definitions, S3b rules). Follow it exactly.
- Your batch: /home/claude/adj/batchN.json. Per study: items{code:{human, llm}}, llm_evidence (LLM quotes per dimension), llm_note, sheet2 (human checks of LLM claims: 'Checked against the full text' Agree / disagree / cannot judge, 'Correct value', 'Note' with PDF pages), text (extracted full text path), pdf (path; use it with pymupdf if text is garbled or you need page numbers).
- Human labels are Korean dropdowns. Mapping: V1 Quantitative=quantitative(NTU/Secchi/attenuation/other quant), Qualitative=qualitative only. D1 Video=video, Survey day/year=survey day/year, Site/habitat=site/habitat, Random images=random image, Not reported=NR. E1 None=none. E5 Human reading of the same footage=human reading of same footage, Independent=independent reference. C5 Manual verification=manual FP verification, Duplicate prevention=duplicate/ID-switch handling.

IMPORTANT context: the human coder was NOT given the S3a overall-rating definitions, so he used NR where the codebook says N (R_ALL N = single-domain evaluation; E_ALL N = detection/classification metrics only, no ecological quantity), and his sheet had no V2-V4 (depth, illumination, camera distance) fields, so his V_ALL ignores them. Treat those as convention differences: decide by the codebook, but still verify the underlying facts (e.g., is the evaluation really single-domain? is depth really reported for the study's own imagery?).

Rule clarifications adopted now (apply them):
1. V6 = NR unless the authors explicitly state performance was not evaluated by visibility or data were restricted; N only with explicit statement. Altitude/distance bins are not a visibility measure.
2. C1 = a detection/classification SCORE threshold used for the reported results. Post-processing parameters (cluster size, track length, NMS IoU alone) are not C1. C4 = score-based reject/unknown/unsure output. Under the unified C rule a reject mechanism alone gives P (threshold reported and justified); Y requires C2/C3 calibration or uncertainty evaluated as an output, OR C5 (verified false positives / duplicate handling) together with C1. Check each case against this.
3. E3: new value 'Point correction' (point correction) when counts/densities are divided/multiplied by recall/precision or a detection rate without modelling detection probability; 'Observation model' only for an explicit model of detection probability/latent abundance with uncertainty. E_ALL Y requires E1 != none and (E5 = independent OR E3 = Observation model). Point correction alone does not give Y.
4. R: follow P2 strictly. Held-out sites/days/deployments within the same campaign or dataset are NOT external. Different season/year, campaign, camera, water condition, region or dataset IS external. Off-the-shelf models tested on the study's data count (R rule).
5. D: code the split that produced the headline results. Y only if the paper states (or the design makes unambiguous) that train/test were separated by video, survey day, site or region.

Task: for every study in your batch, adjudicate
 (a) every item where human != llm (after label mapping) and every overall dimension (V_ALL..E_ALL) where they differ,
 (b) every sheet2 row whose 'Checked against the full text' is disagree or cannot judge (incl. text/wording corrections the human requested about how the manuscript describes the study),
 (c) any additional error you notice in the LLM record for the five dimensions.
Read the relevant parts of the paper yourself for each one. The human's memos are evidence, not verdicts; the LLM's quotes are evidence, not verdicts.

Output: write /home/claude/adj/resN.json (N = batch number) as
{ "<ID>": { "fields": { "<FIELD e.g. D_ALL, D1, V6, C1, E3>": {"final": "<value in LLM vocabulary used in fall json: Y/P/N/NR/NA, D1 Korean labels like 'Video', 'Random images/frames', 'NR'; E3 'None'/'Point correction'/'Observation model'; C5 'None'/'Duplicate-count (ID-switch) handling'/'False-positive rate on verified sample'/'Both'>", "human": "...", "llm": "...", "winner": "human|llm|neither|both(convention)", "type": "convention|substantive", "quote": "...", "loc": "p.X / Sec", "reason": "<=40 words"} },
            "text_fixes": [ {"issue": "...", "correct_statement": "...", "quote": "...", "loc": "..."} ],
            "new_EV": {"<D>_EV": "updated verbatim evidence if the overall value changed"} } }
Include only fields you adjudicated. Use the LLM vocabulary values exactly as they appear in /home/claude/fall/<ID>.json (look at the file for the allowed values). Do not modify any files other than your res file. When done, reply with a 5-line summary: number adjudicated, human wins, llm wins, neither, and the substantive changes to overall ratings.
