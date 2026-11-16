# Adjudication rules (final, 2026-11-07)

Two independent coders disagreed on some overall ratings. You are the adjudicator. For each assigned study you get both coders' values and evidence in /home/claude/coding/disc_by_id.json (keys p1/p2, p1_ev/p2_ev, sub_diff, notes). Read the relevant parts of the full text /home/claude/coding/txt/<ID>.txt yourself and decide the correct value under CODING_INSTRUCTIONS.md (including its Policy decisions) PLUS the clarifications below, which take precedence. You may choose p1, p2, or a third value.

## Clarifications
1. C_ALL (unified):
   - Y = calibration metrics or uncertainty estimates reported/evaluated as outputs (C2 or C3), OR false-positive/duplicate verification (C5) together with a reported threshold value (C1 = Y).
   - P = a threshold value is reported AND its choice is justified (sensitivity analysis, PR operating points, F1-maximising, per-class tuning, reject/unsure rule), OR C5 without a reported threshold value.
   - N = a threshold value is reported but used as a default/unexplained choice, with no false-positive or duplicate handling.
   - NR = no threshold value reported and no C5.
   - NA = classification-only study with no per-instance score threshold, reject or unsure mechanism.
   - C5 requires that false positives / duplicate counts are actually measured or explicitly handled by a stated mechanism (e.g., Seq-NMS, track merging, expert review of detections with FP count). Merely choosing a tracker "to reduce ID switches" without measuring or a stated duplicate-handling rule is not C5.
2. D (split):
   - If a study has several evaluation designs, code the design that produced the headline/final test results.
   - If the paper gives only split ratios or counts and never states the unit or that it was random → D1 = NR (lower information), D_ALL = NR.
   - Predefined public split: D_ALL = P only if the paper (or its cited dataset paper, as described in the text) states the split unit; otherwise NR.
   - D4 = Y requires explicit discussion of leakage/near-duplicates between train and test.
3. R (external):
   - Policy P2 applies: different site/estuary/day within the same campaign or dataset is NOT external.
   - Different season or year at the same site IS external (counts as "Season/period").
   - Two datasets from the same camera network/campaign (e.g., LifeCLEF 2014 and 2015, both Fish4Knowledge Taiwan) are NOT external to each other.
   - R1 = Y if ANY model evaluated in the paper (including off-the-shelf models trained elsewhere) is tested outside its training domain with numeric results. R3 = Y if the in-domain vs external performance difference is reported numerically (or both numbers are given).
   - Qualitative-only external demonstration → R1 = Y, R3 = N → R_ALL = P.
4. E:
   - Lengths/counts measured by humans from the SAME footage (including stereo measurements by annotators) = "Human reading of the same footage (e.g., MaxN)". Independent = a reference not derived from the same imagery (diver UVC, catch counts, physical length measurement, tagging/PIT, eDNA, sonar).
   - A challenge "counting score" computed against expert per-species counts of the same videos = E1 "Comparison with human counts", E5 "Human reading of the same footage" → E_ALL = P. If the paper reports no counts/ecological quantity at all → E1 = None.
   - A quantity computed but never reported/evaluated (e.g., "lengths can be computed") → E1 = None.
5. V: qualitative statements count only if they describe the study's OWN data conditions (e.g., "our footage was murky"); generic statements in the Introduction about underwater challenges → V1 = NR.
6. INCL (P4): include only if performance on in-situ underwater imagery is reported. If most imagery is web/aquarium/social-media and in-situ underwater results are not reported separately → INCL = N.

## Output
For each study write /home/claude/coding/adjudicated/<ID>.json:
{"ID": "...", "final": {"<FIELD>": "<value>", ...}, "sub": {"<subitem>": "<value>", ...}, "evidence": {"<FIELD>": "verbatim quote (≤25 words) with section cue"}, "reason": {"<FIELD>": "one sentence"}}
"final" must contain every disputed field for that study. "sub" contains any sub-items (D1, R1, R3, C1, C5, E1, E5, V1, V6, D3, D4, C4, INCL/EXCL…) whose final value should be set so that they are consistent with the final overall rating. If INCL becomes N, also set EXCL.
