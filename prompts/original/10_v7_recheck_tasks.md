# V7 re-check tasks (issued 16 November 2026; each run as a separate model instance)

## 10a. Re-check of external-robustness coding (24 studies with R3 = Y)
Re-check external-robustness coding under a tightened rule. Rules: 09_v7_rule_changes.md item 2 (R3 = Y only if the SAME trained model is evaluated in-domain and on external data with the SAME metric, both values or the change reported). Codebook background: 03b_charting_instructions_v2.md (P2 policy).
Studies: every study currently coded R3 = Y. A mock reviewer specifically questioned Pedersen 2019 (off-the-shelf vs fine-tuned on same data), the Zhang 2020 study, Gallitto 2025 (compares with an F1 taken from another paper) and Jenrette 2022 (three data-generation methods, possibly no in-domain vs external comparison) — check them carefully, plus every other study in the list. Read the relevant results in the full text for each.
Output per study: R1, R3, R_ALL, changed, verbatim quote (<=30 words), location, reason (<=40 words). Process every study.

## 10b. Re-check of data-independence coding (66 studies)
Rules: 09_v7_rule_changes.md (the D rules under "Already in force" and new item 3 on provider splits). Background codebook: 03b_charting_instructions_v2.md.
Studies: users of DeepFish or Brackish, and studies whose D1 says image/k-fold while D_ALL = NR.
For each study decide D1, D3, D4, D_ALL that produced the headline results: (a) did it use the dataset provider's predefined split (then inherit the unit), (b) its own stated random image/frame split or k-fold over images (N, or P with leakage/near-duplicate handling), (c) only counts/ratios with no assignment stated (D1 = NR, D_ALL = NR), (d) a grouped split (Y). Make D1 and D_ALL consistent. Read the methods for every study.
Output per study: D1, D3, D4, D_ALL, changed, verbatim quote, location, reason.

## 10c. Re-check of calibration/false-positive coding (60 studies)
Rules: 09_v7_rule_changes.md item 1 (and the C1 definition under "Already in force").
Studies: all studies currently C_ALL = Y or NA, or with any C5 value.
For each study verify against the full text: C1 (score threshold for reported results), C2, C3, C4, C5 — in particular whether C5 is duplicate handling only, or humans actually checked the system's outputs on field footage and reported false positives (count or rate), or both. Test-set precision/confusion matrices are not C5. A mock reviewer named Kitchingman 2023 (Seq-NMS), Gallitto 2025 (DeepSORT without ID-switch rate), and three NA studies said to report false-positive rates (Jahanbakht 2023, McIntosh 2022, Soom 2022) — check those carefully. Then apply the V7 C_ALL rule.
Output per study: C1–C5, C_ALL, changed, verbatim quote, location, reason.

## 10d. Data charting of one study added after publication check (two independent runs)
You are an independent data-extraction coder. Code ONE study (Varini et al. 2026, SharkTrack, Ecological Informatics 95, 103713). Follow 03b_charting_instructions_v2.md exactly, with the rule changes in 09_v7_rule_changes.md (these override). Use exactly the keys and value vocabulary of the existing final records; also fill DATASRC (OWN/PUBLIC) and INCL/EXCL against the eligibility criteria. Do not look at any other coder's output.
