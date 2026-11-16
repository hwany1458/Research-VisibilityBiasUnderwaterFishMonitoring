# Title/abstract screening — scoping review of AI-based underwater fish MONITORING (field data)

For each record (title, venue, keywords, FULL abstract) assign exactly one decision:

**I (include for full-text review)** — ALL of the following are indicated:
1. AI/ML (deep learning or classical machine learning) is used to detect, classify, count, track, segment or measure FISH (sharks/rays included; multi-taxon OK if fish are a target class).
2. Optical underwater imagery acquired in situ in natural or semi-natural waters (sea, estuary, river, lake, reservoir, canal, fishway/dam passage, fishing gear in the wild).
3. The abstract indicates the imagery comes from FIELD DEPLOYMENTS — the authors' own or partners' field footage (BRUV/RUV, diver video, fixed/cabled camera or observatory, ROV/AUV survey, in-trawl/towed camera, fishway counter, stereo-video survey) OR a monitoring-programme dataset with deployment information (OzFish, SEAMAPD21, GFISHERD24, DeepFish, Brackish/BrackishMOT, Deep Vision, Labeled Fishes in the Wild, Luderick-Seagrass, FishTrac/FishTrack23, or similar).
4. Primary empirical study (journal or peer-reviewed conference paper) with its own results.

**U (unclear data source)** — criteria 1, 2 and 4 appear met, but the abstract does not say where the imagery came from (e.g., "a self-constructed underwater fish dataset", "real underwater images", "a public dataset" without naming it), so criterion 3 cannot be judged.

**E (exclude)** — give ONE reason code:
- E-A aquaculture/farm cage, pond culture, tank, RAS, hatchery, laboratory or aquarium
- E-B only challenge/benchmark collections (Fish4Knowledge recognition sets, LifeCLEF/SeaCLEF/FishCLEF/ImageCLEF, URPC/UTDAC/RUOD/DUO/UODD/RUIE, Kaggle/Roboflow compilations, WildFish, QUT, Croatian fish, SUIM, IOCfish5K) and no field-monitoring dataset
- E-W web, internet, aquarium-photo, social-media or synthetic/simulated images
- E-N not fish (jellyfish, coral, sea cucumber, crabs, scallops, Nephrops, plankton, debris, nets, ships, mammals, turtles) OR not a detection/classification/counting/tracking/segmentation/measurement task (robotics control, navigation, sensors, lateral line, acoustics of vehicles, water quality, habitat mapping, etc.)
- E-S sonar/acoustic only (DIDSON, ARIS, echosounder, hydrophone, passive acoustics)
- E-H image enhancement/restoration only, without fish detection/classification evaluation
- E-R review, survey, perspective, editorial, dataset paper without model experiments, or software/tool description without evaluation
- E-X3 imagery not underwater in situ (on deck, market, conveyor, catch photos, aerial/drone, above-surface)
- E-O other (state briefly)

Rules: read the whole abstract; do not guess beyond it; if a record could be E for a clear reason, prefer E over U. Fishway/dam/hydropower passage and in-trawl cameras count as natural/semi-natural waters. If there is no abstract, decide from the title and use U when it looks potentially eligible.
