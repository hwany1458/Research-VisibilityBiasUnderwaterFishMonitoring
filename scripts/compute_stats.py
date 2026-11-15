import json, glob, sys, statistics
from collections import Counter
import os
D = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'coded_studies')
R = [json.load(open(f)) for f in sorted(glob.glob(D + '/*.json'))]
R = [r for r in R if r.get('INCL') == 'Y']
N = len(R)
out = {'N': N}
per = lambda y: 'a' if y <= 2019 else ('b' if y <= 2022 else 'c')
out['period_n'] = dict(Counter(per(int(r['YEAR'])) for r in R))
out['peer'] = dict(Counter(r['PEER'] for r in R))
for k in ['PLAT', 'ENV', 'TYPE', 'TAXA', 'PRE', 'CODE', 'DSHR', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'D1', 'D3', 'D4', 'R1', 'R3', 'C1', 'C2', 'C3', 'C4', 'C5', 'E1', 'E2', 'E3', 'E4', 'E5']:
    out[k] = dict(Counter(r.get(k) for r in R))
for d in 'VDRCE':
    out[d + '_ALL'] = dict(Counter(r[d + '_ALL'] for r in R))
    out[d + '_Y_by_period'] = {p: sum(1 for r in R if per(int(r['YEAR'])) == p and r[d + '_ALL'] == 'Y') for p in 'abc'}
yc = Counter(sum(r[d + '_ALL'] == 'Y' for d in 'VDRCE') for r in R)
out['Ycount'] = dict(sorted(yc.items()))
out['pairs'] = dict(Counter(''.join(d for d in 'VDRCE' if r[d + '_ALL'] == 'Y') for r in R if sum(r[d + '_ALL'] == 'Y' for d in 'VDRCE') >= 2))
import re
fam = Counter()
for r in R:
    a = (r.get('ARCH') or '').lower()
    for k, p in [('YOLO', 'yolo'), ('RCNN', 'r-cnn|rcnn'), ('SSD', r'\bssd'), ('Retina', 'retina'), ('Transformer', 'detr|transformer|vit'), ('Classical', 'svm|hog|gmm|haar|cascade|genetic')]:
        if re.search(p, a): fam[k] += 1
out['arch'] = dict(fam)
out['F4K'] = sum(1 for r in R if any(k in (r.get('DATA') or '').lower() for k in ('fish4knowledge', 'lifeclef', 'seaclef', 'fishclef', 'f4k')))
for k in ['OzFish', 'SEAMAPD21', 'DeepFish', 'OBSEA', 'Brackish']:
    out['ds_' + k] = sum(1 for r in R if k.lower() in (r.get('DATA') or '').lower())
out['E_linked_same'] = sum(1 for r in R if r['E1'] != '없음' and r['E5'] == '같은 영상의 사람 판독(MaxN 등)')
out['E_linked_indep'] = sum(1 for r in R if r['E1'] != '없음' and r['E5'].startswith('독립'))
out['C_denom'] = sum(1 for r in R if r['C_ALL'] != 'NA')
out['C5_any'] = sum(1 for r in R if r['C5'] != '없음')
out['C5_dup'] = sum(1 for r in R if r['C5'] in ('중복계수(ID switch) 처리', '둘 다'))
out['C5_fp'] = sum(1 for r in R if r['C5'] in ('검증 표본 오탐률', '둘 다'))
out['R_external'] = sum(1 for r in R if r['R1'] == 'Y'); out['R_numeric'] = sum(1 for r in R if r['R1'] == 'Y' and r['R3'] == 'Y')
out['V_quant'] = sum(1 for r in R if r['V1'] in ('NTU/FNU', 'Secchi', '감쇠계수', '기타 정량'))
out['V_qual'] = sum(1 for r in R if r['V1'] == '정성 서술만'); out['V_nr'] = sum(1 for r in R if r['V1'] == 'NR')
out['ids_V_quant'] = [r['ID'] for r in R if r['V1'] in ('NTU/FNU', 'Secchi', '감쇠계수', '기타 정량')]
out['ids_V_N'] = [r['ID'] for r in R if r['V_ALL'] == 'N']; out['ids_E_Y'] = [r['ID'] for r in R if r['E_ALL'] == 'Y']
out['ids_C_Y'] = [r['ID'] for r in R if r['C_ALL'] == 'Y']; out['ids_C4'] = [r['ID'] for r in R if r['C4'] == 'Y']
print(json.dumps(out, ensure_ascii=False, indent=0))
