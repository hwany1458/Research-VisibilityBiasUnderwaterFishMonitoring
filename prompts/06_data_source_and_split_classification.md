# Two classifications for each of the 182 included studies in /home/claude/v4/cls/records.json
Process ALL 182 records (no sampling). Use DATA, D_EV, NOTE; open the full text (path in TXT) whenever these fields do not settle the question.

A. SRC — where the imagery used for the study's own reported evaluation came from:
 - OWN: at least one reported quantitative evaluation uses footage collected by the authors or their partners/programme (own deployments, own monitoring programme, own observatory archive), whether or not public datasets are also used.
 - PUBLIC: all reported evaluations use only public monitoring datasets collected by others (e.g., DeepFish, Brackish, OzFish, SEAMAPD21, Deep Vision, Luderick, FishTrack23, OBSEA public archive, Fish4Knowledge archive) — including Kaggle/Roboflow redistributions of these.

B. SPLIT — only for records whose D1 is "이미지/프레임 무작위" or "k-fold(이미지)"; otherwise write "NA":
 - EXPLICIT: the paper states that images/frames (or image-level folds) were split at random or without grouping, or states a split at image level in words.
 - COUNTS_ONLY: the paper gives only numbers or ratios of images per set (e.g., "8000 training and 2000 test images", "80/20") and never states how images were assigned; the image-level unit was inferred.

Output: write ONLY your own file (path in your prompt) as JSON {ID: {"SRC": "...", "SPLIT": "...", "why": "<short quote or reason>"}}. Do not read the other judge's file.
