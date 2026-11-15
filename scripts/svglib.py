"""Tiny SVG helper for scientific schematic figures."""
import re, html

FONT = "Arial, 'Liberation Sans', Helvetica, sans-serif"
INK = '#1d1d1f'

class SVG:
    def __init__(self, w, h):
        self.w, self.h, self.items, self.defs = w, h, [], []
        self.defs.append(
            '<marker id="arr" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            '<path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker>')
        for c, n in [('#1d1d1f', 'k'), ('#2f6f9f', 'b'), ('#c0392b', 'r'), ('#3a8f5c', 'g'), ('#d9822b', 'o'), ('#6b7280', 'gr')]:
            self.defs.append(f'<marker id="a{n}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>')

    def add(self, s): self.items.append(s)
    def grad(self, gid, stops, vertical=True):
        x2, y2 = ('0', '1') if vertical else ('1', '0')
        st = ''.join(f'<stop offset="{o}" stop-color="{c}" stop-opacity="{a}"/>' for o, c, a in stops)
        self.defs.append(f'<linearGradient id="{gid}" x1="0" y1="0" x2="{x2}" y2="{y2}">{st}</linearGradient>')

    def rect(self, x, y, w, h, fill='none', stroke=INK, sw=1.5, rx=0, dash=None, opacity=1):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"{d}/>')
    def line(self, x1, y1, x2, y2, stroke=INK, sw=2, arrow=None, dash=None, opacity=1):
        m = f' marker-end="url(#a{arrow})"' if arrow else ''
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"{m}{d}/>')
    def path(self, d, stroke=INK, sw=2, fill='none', arrow=None, dash=None, opacity=1):
        m = f' marker-end="url(#a{arrow})"' if arrow else ''
        da = f' stroke-dasharray="{dash}"' if dash else ''
        self.add(f'<path d="{d}" stroke="{stroke}" stroke-width="{sw}" fill="{fill}" opacity="{opacity}"{m}{da}/>')
    def circle(self, cx, cy, r, fill='none', stroke=INK, sw=1.5, opacity=1):
        self.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"/>')

    def text(self, x, y, s, size=20, anchor='start', weight='normal', fill=INK, italic=False):
        size = max(size, 17)
        """Mini markup: _{sub}  ^{sup}  *italic*"""
        out, i, base_it = [], 0, italic
        it = italic
        pend = [0.0]
        def dyp():
            if pend[0]:
                v = pend[0]; pend[0] = 0.0; return f' dy="{v:.1f}"'
            return ''
        def esc(t): return html.escape(t, quote=False)
        while i < len(s):
            if s.startswith('_{', i) or s.startswith('^{', i):
                sub = s[i] == '_'; j = s.index('}', i)
                inner = s[i+2:j]
                inner_it = it
                parts = re.split(r'(\*)', inner)
                dy = 0.28 * size if sub else -0.38 * size
                first = True
                for p in parts:
                    if p == '*': inner_it = not inner_it; continue
                    if not p: continue
                    st = ' font-style="italic"' if inner_it else ''
                    dyattr = f' dy="{dy + pend[0]:.1f}"' if first else ''
                    if first: pend[0] = 0.0
                    out.append(f'<tspan font-size="{size*0.68:.1f}"{dyattr}{st}>{esc(p)}</tspan>')
                    first = False
                pend[0] = -dy
                i = j + 1
            elif s[i] == '*':
                it = not it; i += 1
            else:
                j = i
                while j < len(s) and s[j] != '*' and not s.startswith('_{', j) and not s.startswith('^{', j): j += 1
                st = ' font-style="italic"' if it else ' font-style="normal"'
                out.append(f'<tspan{st}{dyp()}>{esc(s[i:j])}</tspan>')
                i = j
        self.add(f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}" fill="{fill}" xml:space="preserve">{"".join(out)}</text>')

    def lines(self, x, y, rows, size=20, lh=None, **kw):
        lh = lh or size * 1.25
        for k, r in enumerate(rows): self.text(x, y + k * lh, r, size=size, **kw)

    def fish(self, cx, cy, L, fill='#7a8b99', opacity=1, flip=False, stroke='#3d4a55'):
        """Simple side-view fish of total length L centred at (cx, cy)."""
        h = L * 0.34; s = -1 if flip else 1
        nose = cx + s * L * 0.5; tailb = cx - s * L * 0.30; tailx = cx - s * L * 0.5
        d = (f'M{nose:.1f},{cy:.1f} Q{cx + s*L*0.1:.1f},{cy - h:.1f} {tailb:.1f},{cy:.1f} '
             f'Q{cx + s*L*0.1:.1f},{cy + h:.1f} {nose:.1f},{cy:.1f} Z '
             f'M{tailb + s*2:.1f},{cy:.1f} L{tailx:.1f},{cy - h*0.55:.1f} L{tailx + s*L*0.04:.1f},{cy:.1f} L{tailx:.1f},{cy + h*0.55:.1f} Z')
        self.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="1.2" opacity="{opacity}"/>')
        self.circle(cx + s * L * 0.33, cy - h * 0.12, max(1.2, L * 0.03), fill='#111', stroke='none', opacity=opacity)

    def svg(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}">'
                f'<defs>{"".join(self.defs)}</defs><rect width="{self.w}" height="{self.h}" fill="#ffffff"/>' + ''.join(self.items) + '</svg>')
