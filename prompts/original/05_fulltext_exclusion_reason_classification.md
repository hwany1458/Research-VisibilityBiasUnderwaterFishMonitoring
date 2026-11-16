# Assign ONE primary full-text exclusion reason to each of the 157 records in /home/claude/v3/excl/records.json
Use the record's EXCL code, NOTE and DATA (these come from two independent full-text coders and an adjudicator). Process ALL 157 records.
Categories (apply in this priority order; pick the FIRST that applies):
1. NOFISH  - no fish detection/classification/counting/tracking/segmentation/length task (non-fish targets, habitat classification).
2. NOML    - no machine-learning/AI component.
3. NOTINSITU - imagery is not underwater in situ field imagery: web/internet/stock/social-media images, aquarium photos, synthetic, on-deck/market/out-of-water, fishing-port images, compilations from public and private sources.
4. AQUA    - aquaculture cages/ponds/tanks/RAS, rearing facilities, laboratory tanks.
5. BENCH   - quantitative results only on challenge/benchmark collections (Fish4Knowledge recognition/FCS/MOS sets, LifeCLEF/SeaCLEF, URPC/RUOD/DUO, Kaggle/Roboflow compilations, WildFish, QUT, UOT32 etc.) with no field-monitoring dataset.
6. PROV    - the source/acquisition of the imagery is never stated or described, so field deployment cannot be established (and none of 1-5 is established).
7. NOQUANT - no quantitative results for the field imagery, or own results cannot be identified.
If a record fits both BENCH and PROV (e.g., benchmark data plus an own dataset of unstated origin), choose BENCH only if the NOTE says the quantitative results are benchmark-only; otherwise PROV.
Output: write ONLY your own file (path in your prompt): JSON object {ID: CATEGORY}. Do not open the other judge's file.
