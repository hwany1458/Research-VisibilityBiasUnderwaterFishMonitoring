# Full-text eligibility check (15 studies) — monitoring-application criterion

Full texts: /home/claude/coding/txt/{ID}.txt for ID in:
S008 S010 S011 S013 S014 S015 S016 S017 S019 S021 S041 S055 S098 S108 S109

Read EACH full text completely enough to find the data/methods/experiments sections (do not judge from the abstract alone; process all 15, no sampling).

INCLUDE (Y) only if ALL hold:
1. AI/ML detects, classifies, counts, tracks, segments or measures fish.
2. The model is EVALUATED on optical underwater imagery of wild fish acquired in situ in natural or semi-natural waters (sea, estuary, river, lake, fishway/dam passage, in-trawl camera in the wild).
3. That evaluation imagery comes from field deployments: the authors' own/partners' field footage (BRUV/RUV, diver, fixed/cabled observatory, ROV/AUV, towed/in-trawl, fishway counter, stereo-video survey) OR a monitoring dataset with deployment information (OzFish, SEAMAPD21, GFISHERD24, DeepFish, Brackish/BrackishMOT, Deep Vision, Labeled Fishes in the Wild, Luderick-Seagrass, FishTrac/FishTrack23, or similar).
4. Primary empirical study with its own results.

EXCLUDE (N) with one code: E-A aquaculture/tank/lab/aquarium; E-B only benchmark/challenge collections (Fish4Knowledge recognition sets, LifeCLEF/SeaCLEF/FishCLEF, URPC/RUOD/DUO, Kaggle/Roboflow compilations, WildFish, QUT, Croatian fish) and no field-monitoring dataset; E-W web/synthetic images; E-N not fish/not such a task; E-S sonar only; E-R no own experiments; E-O other.
A study that uses a field-monitoring dataset for ANY of its reported evaluations meets criterion 3.

Output: write ONLY your own file (path given in your prompt), TSV with header
ID	decision	code	evidence
where evidence = the dataset(s) used for evaluation and where the imagery came from, with a short quote or section reference. Work independently; do not read other output files in this folder. Use your own scratch dir if needed (/tmp/ex15_<yourname>/).
