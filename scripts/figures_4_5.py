import json, glob, sys
import os; sys.path.insert(0, os.path.dirname(__file__))
from svglib import SVG
R = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), '..', 'data', 'coded_studies', '*.json')))]
R = [r for r in R if r.get('INCL') == 'Y']
COL = {'Y': '#1f4e79', 'P': '#7fb3d5', 'N': '#d9622b', 'NR': '#c9ccd1', 'NA': '#ffffff'}
LAB = {'Y': 'Yes (fully reported/performed)', 'P': 'Partial', 'N': 'No (explicitly not done)', 'NR': 'Not reported', 'NA': 'Not applicable'}
DIMS = [('V', 'Visibility characterization'), ('D', 'Data independence'), ('R', 'External-domain robustness'),
        ('C', 'Calibration & false-positive control'), ('E', 'Ecological endpoint validation')]

# ---------------- Figure 5: stacked bars
W, H = 1400, 600
s = SVG(W, H)
x0, x1 = 430, 1360; bw = x1 - x0; y = 70; bh = 62; gap = 26
for t in (0, 25, 50, 75, 100):
    xx = x0 + bw * t / 100
    s.line(xx, 55, xx, 70 + 5 * (bh + gap) - gap + 8, stroke='#e2e5e9', sw=1.5)
    s.text(xx, 48, f'{t}%', size=17, anchor='middle', fill='#555')
for d, name in DIMS:
    vals = [r[d + '_ALL'] for r in R]
    n = len(vals); cx = x0
    s.text(30, y + bh / 2 + 7, f'{d}  {name}', size=21, weight='bold')
    nna = vals.count('NA')
    s.text(30, y + bh / 2 + 30, f'n = {n - nna}' + (f' ({nna} not applicable)' if nna else ''), size=15, fill='#666')
    denom = n - nna
    for k in ('Y', 'P', 'N', 'NR'):
        c = vals.count(k)
        if not c: continue
        w = bw * c / denom
        s.rect(cx, y, w, bh, fill=COL[k], stroke='#ffffff', sw=1.5)
        if w > 22:
            s.text(cx + w / 2, y + bh / 2 + 7, str(c), size=19 if w > 38 else 15, anchor='middle', weight='bold', fill='#ffffff' if k in ('Y', 'N') else '#1d2733')
        cx += w
    y += bh + gap
ly = y + 14; lx = 430
for k in ('Y', 'P', 'N', 'NR'):
    s.rect(lx, ly, 24, 24, fill=COL[k], stroke='#888', sw=1)
    s.text(lx + 32, ly + 19, LAB[k], size=17)
    lx += {'Y': 330, 'P': 140, 'N': 300, 'NR': 0}[k]
open(os.path.join(os.path.dirname(__file__), '..', 'figures', 'Figure4.svg'), 'w').write(s.svg())

# ---------------- Figure 6: study x dimension matrix, two panels
R2 = sorted(R, key=lambda r: (int(r['YEAR']), r['AUTHOR']))
n = len(R2); half = (n + 1) // 2; panels = [R2[:half], R2[half:]]
cw = 17; ch = 34; gx = 230
W2 = gx + half * cw + 40; ph = 30 + 5 * ch + 40
H2 = 70 + 2 * ph + 120
s = SVG(W2, H2)
for pi, P in enumerate(panels):
    gy = 62 + pi * (ph + 12)
    for j, r in enumerate(P):
        for i, (d, name) in enumerate(DIMS):
            v = r[d + '_ALL']
            s.rect(gx + j * cw, gy + i * ch, cw, ch, fill=COL[v], stroke='#ffffff', sw=1)
            if v == 'NA':
                s.line(gx + j * cw + 3, gy + i * ch + ch - 3, gx + j * cw + cw - 3, gy + i * ch + 3, stroke='#9aa0a6', sw=1.2)
    for i, (d, name) in enumerate(DIMS):
        s.text(gx - 12, gy + i * ch + ch / 2 + 7, f'{d}', size=21, anchor='end', weight='bold')
        s.text(gx - 40, gy + i * ch + ch / 2 + 6, name.split(' ')[0], size=15, anchor='end', fill='#555')
    prev = None; lastx = -999; lift = 0
    for j, r in enumerate(P):
        yr = int(r['YEAR'])
        if yr != prev:
            x = gx + j * cw
            lift = 17 if (x - lastx < 44 and lift == 0) else 0
            s.line(x, gy - 3, x, gy + 5 * ch + 6, stroke='#1d2733', sw=1.6)
            s.text(x + 3, gy - 7 - lift, str(yr), size=13, fill='#333')
            prev = yr; lastx = x
    for j, r in enumerate(P):
        ny = sum(r[d + '_ALL'] == 'Y' for d, _ in DIMS)
        s.text(gx + j * cw + cw / 2, gy + 5 * ch + 22, str(ny), size=13, anchor='middle', fill='#1f4e79' if ny else '#aaa', weight='bold' if ny else 'normal')
    s.text(gx - 12, gy + 5 * ch + 22, 'No. of Y', size=14, anchor='end', fill='#555')
ly = 70 + 2 * ph + 16; lx = gx
for k in ('Y', 'P', 'N', 'NR', 'NA'):
    s.rect(lx, ly, 22, 22, fill=COL[k], stroke='#888', sw=1)
    if k == 'NA': s.line(lx + 3, ly + 19, lx + 19, ly + 3, stroke='#9aa0a6', sw=1.2)
    s.text(lx + 30, ly + 17, LAB[k], size=16)
    lx += {'Y': 280, 'P': 110, 'N': 250, 'NR': 160, 'NA': 0}[k]
s.text(gx, ly + 54, f'Each column is one included study (n = {n}), ordered by publication year and first author; the matrix continues in the lower panel.', size=15, fill='#555')
open(os.path.join(os.path.dirname(__file__), '..', 'figures', 'Figure5.svg'), 'w').write(s.svg())
print('ok', n)
