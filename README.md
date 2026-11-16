# Visibility bias in AI-based underwater fish monitoring — data, prompts, and scripts

This repository holds the supplementary material for the scoping review

> Lee, Y.-H.; Jang, K.-W. *Visibility Bias in AI-Based Underwater Fish Monitoring: A Scoping Review of Ecological Validity and a Reporting Checklist.* Biology (MDPI), submitted.

It lets readers check every count in the paper against the coded data, see the exact prompts given to the language model, and re-run the statistics and figures.

## What is here

| Folder | Contents |
|---|---|
| `data/coded_studies/` | Final coding of the 183 included studies, one JSON file per study (64 fields; overall ratings `V_ALL`, `D_ALL`, `R_ALL`, `C_ALL`, `E_ALL` with verbatim supporting quotations in `*_EV`). |
| `data/coding_runs/run1`, `run2` | The two separate coding runs of the language model for each study, before adjudication. |
| `data/logs/` | `corrections_log.json` (every change made after the coding runs: adjudication, human verification, systematic sweep, and the final recheck before submission, each with its reason and quotation); `human_model_agreement.json` (human vs model agreement on 12 items for the 55-study verification sample); `final_recheck_R.json`, `final_recheck_C.json`, `final_recheck_D.json` (decisions of the final recheck before submission); `data_source_classification.json`. |
| `prompts/` | Every prompt given to the language model (Supplementary Table S6), with coded values in English translation. `prompts/original/` holds the prompts exactly as run, in which some coded values are written in Korean; `glossary_korean_values.json` maps each Korean value to its English equivalent. |
| `tables/` | Supplementary Tables S1–S6 as Excel workbooks. |
| `scripts/` | `compute_stats.py` (all counts reported in Section 5), `mrcuai.py` (checklist items, Table 7 and Table S4), `figures_4_5.py` (Figures 4 and 5, SVG). |
| `figures/` | Figures 4, 5, and S1 (SVG and PNG). |

## Coded values

Some categorical values are stored in Korean, as in the codebook used during coding. `prompts/glossary_korean_values.json` gives the English value used in the paper for each one. Rating values: Y = reported/performed; P = partially; N = explicitly not done; NR = not reported; NA = not applicable.

## How the data were produced

Screening, full-text eligibility, and data charting were done by a large language model (Claude, Anthropic; `claude-opus-5-5`), each in two separate runs with adjudication against the full text. The first author coded a purposive 30% sample (55 studies) without access to the model's ratings and checked every key claim against the full text (176 study–claim checks). No second human coder rated a random sample, so the counts are model-extracted estimates (Sections 4.5–4.6 of the paper).

## Re-running

```bash
python3 scripts/compute_stats.py      # prints all counts as JSON
python3 scripts/mrcuai.py             # checklist item counts and distribution
python3 scripts/figures_4_5.py        # writes figures/Figure4.svg and Figure5.svg
```

Python 3.9 or later, standard library only.

## What is not here

The full texts of the included studies are not redistributed because of copyright. Each study is identified by its DOI in `data/coded_studies/`.

## Licence

Code (`scripts/`): MIT License (`LICENSE`). Data, prompts, tables, and figures: Creative Commons Attribution 4.0 International (`LICENSE-DATA`).

## Citation

Please cite the article above. Contact: Kyoung-Won Jang (jaang@wku.ac.kr).
