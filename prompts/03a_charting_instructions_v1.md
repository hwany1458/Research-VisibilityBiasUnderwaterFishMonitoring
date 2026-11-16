# Coding instructions — V-D-R-C-E scoping review of AI-based underwater fish monitoring

You are a data-extraction coder for a scoping review (PRISMA-ScR). For each assigned study you will read the FULL TEXT file `/home/claude/coding/txt/<ID>.txt` (pdftotext output of the paper; layout may be noisy, tables may be scrambled) and write one JSON file `/home/claude/coding/coded/<ID>.json`.

Bibliographic metadata for each ID is in `/home/claude/coding/lit/merged.json` (fields: id, year, author, title, venue, vol, doi …). Use it for AUTHOR/YEAR/TITLE/VENUE/DOI; do not re-derive them.

## Absolute rules
1. Code from the full text (Methods, Results, Supplementary if included). Never from the abstract alone.
2. Use ONLY the allowed values listed below, spelled exactly (they are Korean strings — copy them). Free-text fields: short English.
3. Distinguish **N** (the paper states or clearly shows it was NOT done, e.g. "images were randomly split 80/20") from **NR** (not mentioned anywhere). When you cannot find it, it is NR, never N.
4. Every overall rating (V_ALL, D_ALL, R_ALL, C_ALL, E_ALL) MUST have an evidence string in the matching *_EV field: section/table/figure reference or page cue + a verbatim quotation (≤ 25 words, English) from the text. If you cannot quote evidence, the overall rating is "NR" and *_EV says "no statement found".
5. No charitable interpretation, no inference from what "would normally be done". If genuinely ambiguous, choose the lower-information value and set CONF to "Low" with the reason in NOTE.
6. Mechanically apply the overall-rating rules below; do not override them with holistic judgment.
7. If the text file is unreadable or clearly the wrong paper, write {"ID": "...", "ERROR": "reason"} and move on.
8. Write each paper's JSON file immediately after finishing that paper (so progress is never lost), then continue to the next.

## Key definitions
- **Visibility (V)**: physical optical conditions — turbidity (NTU/FNU), Secchi depth, attenuation/beam coefficient, depth, illumination, camera-to-subject range, image-quality metrics (UIQM/UCIQE). "Turbid water" said in words only = "Qualitative description only".
- **Split unit (D1)**: the unit at which train/val/test were separated. Frame-level random split of frames from the same videos = "Random images/frames". Split by whole videos = "Video". By survey day = "Survey day"; by site/habitat = "Site/habitat"; by region/country = "Region". Using a public dataset's predefined split = "Predefined public split" (then note the original split unit in NOTE: DeepFish = random per-habitat image split 50/20/30; Fish4Knowledge/LifeCLEF = predefined; OzFish = predefined by image; SEAMAPD21 = predefined by image; Brackish = predefined, frame-based).
- **External test (R1)**: evaluation on data from outside the training distribution — different site, season, camera, water condition, species composition, or another dataset. Testing on a held-out split of the same dataset is NOT external.
- **Calibration (C2)**: ECE, reliability diagrams, Brier, temperature scaling evaluation. A confidence threshold alone is C1, not C2.
- **C5**: human verification of a sample of detections reporting a false-positive rate, and/or explicit handling of duplicate counts / ID switches in tracking.
- **E1**: the ecological variable the AI output is connected to, beyond detection metrics. "Comparison with human counts" = compared with human counts of the SAME footage; "MaxN/MeanCount" = produces MaxN or MeanCount; "Abundance/density"; "Occupancy"; "Biomass/length" (length/biomass); "Population trend" (time series/trend); "Behaviour"; "Multiple" (several). If only mAP/F1/accuracy, E1 = "None".
- **E5 reference independence**: "Independent reference (UVC, stereo length, tagging, PIT, eDNA, sonar)" = compared with a reference not derived from the same optical footage (diver census, stereo-video length measurement, tagging/PIT, eDNA, sonar, trawl catch, known number of fish in an enclosure). "Human reading of the same footage (e.g., MaxN)" = compared with human annotation/MaxN of the same videos. "None" = no comparison.

## Policy decisions fixed by the lead author (2026-11-07) — these override any other reading
- P1 (V): if the study restricted data to clear/low-turbidity conditions (or excluded poor-visibility footage) WITHOUT measuring visibility, V_ALL = N.
- P2 (R): held-out sites, days, or deployments WITHIN THE SAME survey campaign/dataset are NOT external (R1 = N). That design is credited under D only. R1 = Y requires a different campaign, season/year, camera system, water condition, region, or another dataset.
- P3 (C): uncertainty that is computed but used only internally (e.g., active-learning sample selection, pseudo-label filtering) and never reported or evaluated as an output does NOT count as C3.
- P4 (INCL): imagery not acquired underwater in situ (web/aquarium photos, museum specimens, on-deck) → INCL = N.
- C_ALL for classification-only studies: NA only if the study produces no per-instance score/threshold at all. If it reports a score threshold, reject option, or unsure class → apply the normal C rules (C1 = Y alone → P).
- C4 = Y only if the paper implements an open-set / OOD / reject / unsure mechanism (not merely discusses false positives).
- V2 = depth reported; V3 = illumination conditions reported; V4 = camera-to-subject range reported.
- R3 = Y if the performance change between in-domain and external test is reported numerically.

## Overall-rating rules (apply mechanically)
- **V_ALL**: Y if V1 ∈ {NTU/FNU, Secchi, Attenuation coefficient, Other quantitative} AND V6 = Y. P if at least one of V1–V4 is reported (V1 ≠ NR or V2/V3/V4 = Y) but V6 ∈ {P, N}. N if the paper states visibility was not measured/controlled or deliberately excluded poor-visibility footage without characterising it. NR if visibility is never mentioned. NA: never.
- **D_ALL**: Y if D1 ∈ {Video, Survey day, Site/habitat, Region}. P if D1 = Random images/frames or k-fold (images) but (D3 = Y or D4 = Y), OR D1 = Predefined public split and the paper states what that split is. N if D1 ∈ {Random images/frames, k-fold (images)} and D3 ≠ Y and D4 ≠ Y. NR if D1 = NR. NA: never. (Pure classification on cropped single-fish images still has a split unit — code it.)
- **R_ALL**: Y if R1 = Y and R3 = Y. P if R1 = Y and R3 = N. N if the paper evaluates on a single dataset/domain only (R1 = N). NR only if the provenance of the test data cannot be determined. NA: never.
- **C_ALL**: Y if C2 ≠ None or C3 ≠ None, OR (C5 ≠ None and C1 = Y). P if C1 = Y with a threshold sensitivity analysis (performance at several thresholds, PR curves discussed as operating points) but no C2/C3/C5, OR C5 ≠ None but C1 = NR. N if a default threshold is used as-is and no false-positive/uncertainty discussion exists AND the paper has detection/counting output. NR if even the threshold is not reported and nothing else applies. NA if the study has no detection/counting output (pure classification of pre-cropped images, segmentation-only benchmarks with no counting).
- **E_ALL**: Y if E1 ≠ None AND (E5 = Independent reference… OR E3 ≠ None). P if E1 ≠ None AND E5 = Human reading of the same footage… (agreement with human reading of the same footage only), OR E1 ≠ None with no comparison at all. N if only detection metrics (mAP, F1, accuracy, IoU) are reported (E1 = None). NR: rare, only if unreadable. NA: never.

## Schema and allowed values (write every key; use null only for free-text fields with nothing to say)
```
ID, CODER = "claude", DATE = "2026-11-07"
KEY   : "<Author><Year>"               AUTHOR, YEAR, TITLE, VENUE, DOI : from merged.json
PEER  : ["Journal (peer-reviewed)","Preprint","Conference (peer-reviewed)"]
INCL  : ["Y","N"]      -- N only if the paper fails inclusion (review, no experiment, not underwater, sonar-only, non-fish)
EXCL  : ["Review/survey","Sonar only","Not underwater imagery","Experiment None","Not fish","Duplicate publication","Full text not obtainable","Other"] or null
TYPE  : ["Detection","Classification","Counting","Tracking","Segmentation","Multi-stage pipeline","Dataset with experiments","Other"]
PLAT  : ["BRUV","DOV (diver)","ROV/AUV","Fixed camera/observatory","In-trawl camera","Aquaculture cage","Tank/laboratory","Mixed","NR"]
ENV   : ["Coral reef","Temperate rocky reef/kelp","Estuarine/brackish","Freshwater","Deep sea","Aquaculture","Mixed","NR"]
REGION: free text          TAXA : ["Single species","Few species (2–10)","Many species (>10)","Fish as one class","Family/genus level"]
NCLASS: integer or null    SPECIES: free text     DATA : free text (dataset names / own footage)
NIMG  : integer or null    NVID : ["Reported","NR"]  FPS  : ["Y","NR"]
V1 : ["NTU/FNU","Secchi","Attenuation coefficient","Other quantitative","Qualitative description only","NR"]
V2, V3, V4 : ["Y","NR"]    V5 : ["UIQM","UCIQE","Other","NR"]
V6 : ["Y","P","N"]   (performance reported stratified by visibility/turbidity/water condition: Y = quantitative strata; P = qualitative e.g. "clear vs murky subsets"; N = none)
V7 : ["Y","N"]       (a model/regression relating visibility to detection performance)
V_ALL : ["Y","P","N","NR","NA"]     V_EV : evidence string
D1 : ["Random images/frames","Video","Survey day","Site/habitat","Region","k-fold (images)","Predefined public split","NR"]
D2 : free text e.g. "70/15/15"      D3 : ["Y","N","NR"]  (near-duplicate removal / clustering)   D4 : ["Y","N"] (leakage discussed)
D_ALL, D_EV
R1 : ["Y","N"]   R2 : ["Site","Season/period","Water quality/turbidity","Camera/equipment","Species composition","Multiple","Not applicable"]   R3 : ["Y","N"]
R_ALL, R_EV
C1 : ["Y","NR"]  C2 : ["ECE","Reliability diagram","Brier","Other","None"]  C3 : ["None","MC dropout","Ensemble","Bayesian","conformal","Other"]
C4 : ["Y","N"]   C5 : ["False-positive rate on verified sample","Duplicate-count (ID-switch) handling","Both","None"]
C_ALL, C_EV
E1 : ["None","Comparison with human counts","MaxN/MeanCount","Abundance/density","Occupancy","Biomass/length","Population trend","Behaviour","Multiple"]
E2 : ["Y","N"]  (quantitative comparison with manual/human census of any kind)
E3 : ["None","N-mixture","Occupancy model","Distance sampling","Other hierarchical model"]
E4 : ["FNR","Size-stratified","Both","None"]  (false-negative rate reported / performance by size class)
E5 : ["Independent reference (UVC, stereo length, tagging, PIT, eDNA, sonar)","Human reading of the same footage (e.g., MaxN)","None"]
E_ALL, E_EV
ARCH : free text   PRE : ["ImageNet","COCO","Underwater dataset","None","NR"]   METR : free text
CODE : ["Y","N"]   DSHR : ["Public","On request","N"]
CONF : ["High","Medium","Low"]   NOTE : free text (ambiguities, dataset split provenance, anything a human verifier should check)
```

## Worked example (illustrative)
A BRUV snapper-counting paper that splits by video, tests only in one region, reports results at several confidence thresholds, and compares automated counts with human MaxN of the same videos → V1 = NR, V6 = N, V_ALL = NR ("no mention of turbidity or visibility"); D1 = Video, D_ALL = Y, D_EV = "Methods 2.3: 'videos were allocated to training and test sets so that no video appeared in both'"; R1 = N, R_ALL = N; C1 = Y, C5 = None, C_ALL = P, C_EV = "Fig. 3 reports precision/recall at thresholds 0.3–0.9"; E1 = MaxN/MeanCount, E2 = Y, E5 = Human reading of the same footage (e.g., MaxN), E3 = None, E_ALL = P.
