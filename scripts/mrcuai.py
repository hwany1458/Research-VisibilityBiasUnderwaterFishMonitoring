import json,glob,statistics,re,sys
import os
R=[json.load(open(f)) for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), '..', 'data', 'coded_studies', '*.json')))]
QUANT={'NTU/FNU','Secchi','감쇠계수','기타 정량'}
ITEMS=[
 ('M1','Environmental conditions','At least two of: depth (V2), illumination (V3), quantitative turbidity or visibility (V1 quantitative), camera-to-subject range (V4)',lambda r: sum([r['V2']=='Y',r['V3']=='Y',r['V1'] in QUANT,r['V4']=='Y'])>=2),
 ('M2','Optical characterization','Instrument measurement of water clarity (V1 = NTU/FNU, Secchi depth, or attenuation coefficient); approximate visibility values, inclusion thresholds, and image-quality indices not credited',lambda r: r['V1'] in ('NTU/FNU','Secchi','감쇠계수')),
 ('M3','Biological context','Taxa identified (not fish as a single class) and species listed',lambda r: r['TAXA']!='어류 전체(종 구분 없음)' and bool(r.get('SPECIES'))),
 ('M4','Data provenance','Number of videos reported (NVID) and frame rate/extraction reported (FPS)',lambda r: r['NVID']=='보고됨' and r['FPS']=='Y'),
 ('M5','Data splitting','Split unit determinable (D overall rating ≠ NR)',lambda r: r['D_ALL']!='NR'),
 ('M6','Model specification','Pre-training reported (PRE ≠ NR) and operating threshold reported (C1 = Y)',lambda r: r['PRE']!='NR' and r['C1']=='Y'),
 ('M7','Evaluation metrics','Performance stratified by apparent (pixel) object size as a proxy for size class (E4) or by visibility or condition stratum (V6); recall alone not credited',lambda r: r['E4'] in ('크기별','둘 다') or r['V6'] in ('Y','P')),
 ('M8','False positives and uncertainty','Any of: calibration metric (C2), uncertainty (C3), reject/OOD (C4), false-positive/duplicate control (C5)',lambda r: r['C2']!='없음' or r['C3']!='없음' or r['C4']=='Y' or r['C5']!='없음'),
 ('M9','External validation','External test with the change in performance reported on a common metric (R1 = Y and R3 = Y)',lambda r: r['R1']=='Y' and r['R3']=='Y'),
 ('M10','Ecological endpoint','Ecological quantity linked (E1 ≠ none) and compared with a reference (E5 ≠ none)',lambda r: r['E1']!='없음' and r['E5']!='없음'),
 ('M11','Data and code sharing','Code released (CODE = Y) and data public (DSHR = public)',lambda r: r['CODE']=='Y' and r['DSHR']=='공개'),
]
if __name__=='__main__':
    tot={r['ID']:sum(1 for *_,f in ITEMS if f(r)) for r in R}
    for c,d,o,f in ITEMS: n=sum(1 for r in R if f(r)); print(c,d,n,round(100*n/len(R)))
    v=list(tot.values()); print('median',statistics.median(v),'IQR',statistics.quantiles(v,n=4),'max',max(v),'min',min(v))
    print('max ids',[ (k,t) for k,t in tot.items() if t>=8])
    json.dump(tot,open(os.path.join(os.path.dirname(__file__), '..', 'data', 'mrcuai_scores.json'), 'w'))
