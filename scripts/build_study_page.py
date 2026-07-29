#!/usr/bin/env python3
"""Render study.json into the self-contained Field Study page (and a PDF).

DESIGN CONTRACT, and why each rule exists. Every number here traces to research,
not taste. The page is a document a busy non-expert reads once, cold, so it is
built for the way people actually read rather than for how much we know.

  Measure 62-70 char          WCAG 2.2 SC 1.4.8 (<=80), Butterick 45-90, Bringhurst 66
  Paragraph gap >= 1.5x lh    WCAG 2.2 SC 1.4.8. Tighter than the leading fuses blocks
  3 heading levels, <=18      Butterick "headings"; NN/g <=3 sizes
  Action-title headings       Minto; Alley/Garner measured better recall for sentence
                              headlines over topic labels + bullets
  Answer first                Minto pyramid, NN/g inverted pyramid. 81% of viewing
                              time is in the first three screens
  Summary that stands alone   USC/Sant: <=10% of body, forwardable on its own
  Callouts, never pull quotes NN/g eyetracking: pull quotes break the commitment
                              pattern and drop readers into light scanning
  Caveats interwoven          O'Keefe meta-analysis: interwoven r=.141,
                              caveat-first r=.014 n.s. Never raise one unanswered
  Numbers right, tabular      Few; proportional digits break column alignment
  Tables not charts <=20 nums Tufte, Visual Display, pp. 20 & 178
  Body >=16px, one accent     Piepenbrock 2014 (dark-mode penalty is worst at small
                              sizes); NN/g minimalism
  Light print theme           A dark PDF is unreadable on paper and gives up the
                              positive-polarity reading advantage

Usage:
  python scripts/build_study_page.py --study out/<date>/study.json \\
      --out out/<date>/field-study.html [--pdf] [--demo-embed demo/index.html]
"""
import argparse
import html
import json
import os
import subprocess
import sys

# ---------- helpers ----------


def esc(v):
    if v is None:
        return ""
    return html.escape(str(v), quote=True)


def has(v):
    if v is None:
        return False
    if isinstance(v, str):
        return bool(v.strip())
    if isinstance(v, (list, dict, tuple)):
        return len(v) > 0
    return True


def get(d, *path, default=None):
    cur = d
    for p in path:
        if not isinstance(cur, dict) or p not in cur:
            return default
        cur = cur[p]
    return cur if cur is not None else default


def para(text, cls=""):
    """One or more paragraphs from a string with blank-line breaks."""
    if not has(text):
        return ""
    c = f' class="{cls}"' if cls else ""
    blocks = [b.strip() for b in str(text).split("\n\n") if b.strip()]
    return "".join(f"<p{c}>{esc(b)}</p>" for b in blocks)


# ---------- embedded brand type ----------
# The site runs Fraunces (display), Manrope (body) and JetBrains Mono (data).
# The study has to look like alaskaaihq.com made it, and it must stay a single
# offline file, so the subsetted woff2 rides inline as base64. Subset to the
# glyphs a study can emit: ~99 KB raw, ~133 KB encoded.
FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "fonts")


def font_face(family, filename, weights, style="normal"):
    path = os.path.join(FONT_DIR, filename)
    if not os.path.exists(path):
        return ""
    import base64
    b64 = base64.b64encode(open(path, "rb").read()).decode("ascii")
    return (f"@font-face{{font-family:'{family}';"
            f"src:url(data:font/woff2;base64,{b64}) format('woff2');"
            f"font-weight:{weights};font-style:{style};font-display:block}}")


def embedded_fonts():
    # Static instances, not variable. Chromium cannot embed a variable instance
    # into a PDF: it falls back to Type 3 glyph procedures with no outlines,
    # which measured 19 Type 3 objects and a 2.6x larger file. Instanced cuts
    # give real /FontFile2 outlines and a smaller PDF.
    return "".join([
        font_face("Fraunces", "fraunces.woff2", "400"),
        font_face("Manrope", "manrope.woff2", "400"),
        font_face("Manrope", "manrope-sb.woff2", "650"),
        font_face("JBMono", "jbmono.woff2", "400"),
    ])


# ---------- brand css ----------
# Colour ladder is APCA-verified against --bg. Lc 90+ body, 75+ secondary,
# 60+ captions. WCAG 2.x ratios overstate contrast on dark backgrounds, which is
# why the previous --faint (#6f7f96) passed AA and was still unreadable at Lc -33.

CSS = """
*{box-sizing:border-box}
:root{
  --u:28px;                     /* vertical rhythm unit, every gap is a multiple */
  --prose:37rem;                /* ~65 characters at 17px */
  --wide:56rem;                 /* tables, diagram, demo only */

  /* alaskaaihq.com's own tokens. The study should look like the site made it. */
  --bg:#02060f;                 /* --night, the site's true ground */
  --surface:#122a46;            /* --panel2 lifted to 1.40:1, reads without a border */
  --rule:#1c3350;               /* --line */

  --ink:#e2eaf6;                /* APCA Lc -86. Capped near 85, above that dark
                                   mode halates (APCA author's own guidance) */
  --sub:#c3d2e6;                /* --body */
  --cap:#a6b9d1;                /* --mute lifted to APCA Lc 63. The site's own
                                   #8da2be measures Lc 51 here, below the 60 floor
                                   for caption-size text on this ground */

  --ui:Manrope,ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --display:Fraunces,Georgia,"Times New Roman",serif;
  --mono:JBMono,ui-monospace,SFMono-Regular,Menlo,monospace;

  --accent:#3ce6b4;             /* --green, the structural accent */
  --gold:#ffc72c;               /* Alaska flag gold, the signature. Budgeted:
                                   it appears on the mark, the one hero number,
                                   and the row that carries the argument. */
  --link:#5ac8f0;               /* --blue */
  --warn:#f2a43a;               /* --amber */
}
html{-webkit-text-size-adjust:100%;
  /* never let the browser fake a weight or an italic we did not embed. A
     synthesised face survives into the PDF and looks smeared. */
  font-synthesis:none}
body{
  margin:0;background:var(--bg);color:var(--ink);
  font:17px/1.62 var(--ui);
  letter-spacing:.005em;        /* light-on-dark counters close up slightly */
  font-variant-numeric:oldstyle-nums proportional-nums;
  -webkit-font-smoothing:antialiased;
}
.page{max-width:var(--wide);margin:0 auto;padding:0 24px calc(var(--u)*3)}
.prose{max-width:var(--prose)}

p{margin:0 0 var(--u)}
strong{color:var(--ink);font-weight:650}
em{font-style:normal;color:var(--sub)}
a{color:var(--link);text-decoration:none;border-bottom:1px solid rgba(138,184,240,.35)}
a:hover{border-bottom-color:var(--link)}

h1,h2,h3{margin:0;text-wrap:balance}
h1{font-family:var(--display);font-size:clamp(38px,6.6vw,64px);font-weight:400;
  line-height:.98;letter-spacing:-.022em;font-variation-settings:"opsz" 96;
  margin-left:-.045em}
h2{font-family:var(--display);font-size:clamp(24px,3.2vw,30px);font-weight:400;
  line-height:1.18;letter-spacing:-.012em;margin:0 0 calc(var(--u)*.5)}
h3{font-size:20px;font-weight:650;line-height:1.3;
  margin:calc(var(--u)*1.5) 0 calc(var(--u)*.5)}
p,li{text-wrap:pretty}

/* ---------- cover ---------- */
.cover{padding:calc(var(--u)*2) 0 calc(var(--u)*.5)}
.mark{display:flex;align-items:center;gap:10px;font:400 13px/1 var(--mono);
  letter-spacing:.18em;margin-bottom:calc(var(--u)*2.5);color:var(--ink)}
/* Polaris, the constellation mark the brand system already uses. Arms have to
   be thin and the glyph big enough or a 4-point star reads as a plus sign. */
.mark i{width:14px;height:14px;display:block;background:var(--gold);
  clip-path:polygon(50% 0,55.5% 44.5%,100% 50%,55.5% 55.5%,50% 100%,
                    44.5% 55.5%,0 50%,44.5% 44.5%)}
.eyebrow{font:400 12px/1 var(--mono);letter-spacing:.16em;text-transform:uppercase;
  color:var(--cap);margin:0 0 18px}
.cover h1{max-width:27ch}
.covermeta{margin-top:calc(var(--u)*1.6);padding-top:14px;
  border-top:1px solid var(--rule);font:400 12px/1.5 var(--mono);
  letter-spacing:.1em;text-transform:uppercase;color:var(--cap);
  display:flex;flex-wrap:wrap;gap:10px 28px;max-width:var(--prose)}
.covermeta span{font-variant-numeric:tabular-nums}

/* ---------- the standalone summary ---------- */
.brief{border-left:2px solid var(--gold);padding:0 0 0 calc(var(--u)*.85);
  margin:calc(var(--u)*1.5) 0 calc(var(--u)*2);max-width:var(--prose)}
.brief h2{font:400 12px/1 var(--mono);letter-spacing:.18em;text-transform:uppercase;
  color:var(--gold);margin-bottom:calc(var(--u)*.7)}
.brief p{color:var(--sub)}
.brief p strong{color:var(--ink)}
.brief p:last-child{margin-bottom:0}

/* ---------- sections ---------- */
.sec{padding:0;margin:calc(var(--u)*3) 0 0}
.sec-n{font:400 12px/1 var(--mono);color:var(--gold);letter-spacing:.18em;
  display:block;margin-bottom:14px;font-variant-numeric:tabular-nums}
.sec-lede{font-size:19px;line-height:1.55;color:var(--sub);
  max-width:34rem;margin:0 0 calc(var(--u)*1.2)}

/* ---------- callout: carries NEW information, never a repeated quote ---------- */
.callout{border-left:2px solid var(--gold);padding:2px 0 2px calc(var(--u)*.85);
  margin:calc(var(--u)*1.2) 0;max-width:var(--prose)}
.callout .big{display:block;font-family:var(--display);font-weight:400;
  font-size:clamp(30px,4.6vw,46px);line-height:1.02;letter-spacing:-.02em;
  margin-bottom:12px;color:var(--ink);font-variant-numeric:lining-nums tabular-nums}
.callout p{color:var(--sub);margin:0}

/* ---------- lists: rare, short, never nested ---------- */
ul.clean{list-style:none;padding:0;margin:0 0 var(--u);max-width:var(--prose)}
ul.clean li{position:relative;padding:0 0 calc(var(--u)*.42) 20px;color:var(--sub)}
ul.clean li::before{content:"";position:absolute;left:2px;top:11px;width:5px;height:5px;
  border-radius:50%;background:var(--accent)}
ul.clean li:last-child{padding-bottom:0}
ul.clean li strong{color:var(--ink)}

/* ---------- tables ---------- */
.tw{overflow-x:auto;margin:0 0 var(--u);max-width:var(--wide)}
table{border-collapse:collapse;width:100%;font-size:16px}
caption{text-align:left;font-size:16px;color:var(--sub);margin-bottom:14px;max-width:var(--prose)}
th,td{padding:11px 18px 11px 0;text-align:left;vertical-align:baseline}
th{color:var(--sub);font-weight:650;font-size:15px;border-bottom:1px solid var(--rule)}

td{color:var(--sub)}
td:first-child{color:var(--ink)}
.num{text-align:right;font-variant-numeric:lining-nums tabular-nums;font-family:var(--mono);font-size:15px}
th.num{font-family:var(--ui);font-size:15px}
tr.total td{border-top:2px solid var(--gold);color:var(--ink);font-weight:650;padding-top:14px}
tfoot td{color:var(--cap);font-size:15px;border-top:1px solid var(--rule);padding-top:12px}

/* ---------- diagram ----------
   All SVG paint comes from CSS, never hardcoded hex, so the print theme
   re-colours the figure instead of leaving dark boxes on a light page.
   Edge stroke is full-opacity --cap = 4.6:1 on the surface; the previous
   #54627a at .7 alpha composited to 1.76:1 and failed WCAG 1.4.11 (3:1). */
.dg-e{stroke:var(--cap)}
.dg-n{fill:var(--ink);font:640 15px/1.25 var(--ui);letter-spacing:-.005em}
.dg-k{fill:var(--cap);font:400 11px/1 var(--mono);letter-spacing:.1em}
.dg-n-bar{fill:var(--cap);opacity:.55}
.dg-build{fill:var(--accent)}
.dg-build-bar{fill:var(--accent)}
@media (max-width:640px){
  /* never let the viewBox scale type below legibility, stack instead */
  .figure svg{min-width:600px}
  .figure{overflow-x:auto;-webkit-overflow-scrolling:touch}
}
.figure{margin:calc(var(--u)*1.2) 0;max-width:var(--wide)}
.figure svg{display:block;width:100%;height:auto;background:var(--surface);border-radius:10px}
.figcap{font-size:15px;color:var(--cap);margin-top:12px;max-width:var(--prose)}
.legend{display:flex;flex-wrap:wrap;gap:16px;margin-top:12px;font-size:14px;color:var(--cap)}
.legend i{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:6px}

/* ---------- demo ---------- */
.demoembed{margin:calc(var(--u)*1.2) 0;border-radius:10px;overflow:hidden;background:var(--surface)}
.demoembed iframe{display:block;width:100%;height:640px;border:0;background:var(--bg)}

/* ---------- sources ---------- */
.srcs{max-width:var(--prose);margin:0;padding:0;list-style:none;
  counter-reset:s;font-size:15px}
.srcs li{counter-increment:s;position:relative;padding:0 0 14px 30px;color:var(--cap)}
.srcs li::before{content:counter(s);position:absolute;left:0;top:1px;
  font:600 13px/1.5 ui-monospace,Menlo,monospace;color:var(--accent)}
.srcs a{word-break:break-word;font-size:14px}

.foot{margin-top:calc(var(--u)*2.5);padding-top:var(--u);
  border-top:1px solid var(--rule);font-size:14px;color:var(--cap);max-width:var(--prose)}

hr.div{border:0;border-top:1px solid var(--rule);margin:calc(var(--u)*2.5) 0 0}

@media (max-width:640px){
  body{font-size:16px}
  .page{padding:0 18px calc(var(--u)*2)}
}

/* Light theme for print. A dark PDF is unreadable on paper, and paper is where
   positive polarity actually helps (Piepenbrock 2013). */
@media print{
  html{print-color-adjust:auto;-webkit-print-color-adjust:economy}
  :root{--bg:#fff;--surface:#f4f6f9;--rule:#ccd4de;
        --ink:#12181f;--sub:#39434f;--cap:#59636f;--link:#12508f;--accent:#0f6f60}
  body{font-size:11pt}
  .page{max-width:none;padding:0}
  .sec{break-inside:auto}
  h1,h2,h3{break-after:avoid}
  .figure,.tw,.callout{break-inside:avoid}
  .demoembed{display:none}
  a{border-bottom:0}
}
"""

# ---------- architecture diagram ----------
# Columns come from FLOW DEPTH, not from node kind. Kind-ordering was producing
# crossing edges and colliding labels. Edge labels are dropped entirely: at this
# size they were unreadable and they are what made the figure look like spaghetti.

# One accent plus ink weight, not five hues. The old palette had two identical
# swatches, fills at 1.05-1.13:1 (invisible), and violet/blue only 9.8 dE apart,
# below the threshold where full-colour-vision readers separate them reliably.
# Encoding now rides on weight and a sublabel, which survive greyscale print and
# colour-vision deficiency.
KIND_LABEL = {"user": "Person", "external": "Theirs today", "system": "Theirs today",
              "ai": "We build", "data": "Their data"}
NODE_INK = "#aab7c8"        # 4.6:1 on the surface, clears WCAG 1.4.11
NODE_ACCENT = "#57e0c8"     # 8.5:1, spent only on what we build


def _depth(nodes, edges):
    """Longest-path depth per node, so flow reads left to right without crossings."""
    ids = [n["id"] for n in nodes]
    incoming = {i: [] for i in ids}
    for e in edges:
        if e.get("from") in incoming and e.get("to") in incoming:
            incoming[e["to"]].append(e["from"])
    depth, seen = {}, set()

    def d(i):
        if i in depth:
            return depth[i]
        if i in seen:
            return 0
        seen.add(i)
        depth[i] = 0 if not incoming[i] else max(d(p) for p in incoming[i]) + 1
        return depth[i]

    for i in ids:
        d(i)
    return depth


def render_diagram(arch):
    nodes = [n for n in (arch.get("nodes") or [])
             if has(n.get("id")) and has(n.get("label"))]
    edges = [e for e in (arch.get("edges") or []) if has(e.get("from")) and has(e.get("to"))]
    if not nodes:
        return ""

    depth = _depth(nodes, edges)
    # Cap the flow at MAXCOL bands. Column count, not node count, is what drives
    # the viewBox wider than the render box and shrinks the type. Merging
    # adjacent depths also cuts the routing paths a reader must follow (7PMG G2).
    MAXCOL = 5
    raw = sorted({depth.get(n["id"], 0) for n in nodes})
    if len(raw) > MAXCOL:
        per = (len(raw) + MAXCOL - 1) // MAXCOL
        band = {d: i // per for i, d in enumerate(raw)}
    else:
        band = {d: i for i, d in enumerate(raw)}
    cols = {}
    for n in nodes:
        cols.setdefault(band[depth.get(n["id"], 0)], []).append(n)
    order = sorted(cols)

    # Pin the viewBox to the actual render width so one unit is one CSS pixel and
    # labels can never shrink below legibility. Previously a 7-column flow scaled
    # to 0.62 on desktop and 0.29 on a phone, rendering 15px type at 9.4 and 3.9px.
    CANVAS = 848
    BH, GY, PAD = 62, 18, 14
    rows = max(len(v) for v in cols.values())
    ncol = len(order)
    GX = 34 if ncol > 4 else 44
    BW = int((CANVAS - PAD * 2 - (ncol - 1) * GX) / ncol)
    W = CANVAS
    H = PAD * 2 + rows * (BH + 16) + (rows - 1) * GY

    pos = {}
    for ci, c in enumerate(order):
        group = cols[c]
        span = len(group) * (BH + 16) + (len(group) - 1) * GY
        y0 = (H - span) / 2
        for ri, n in enumerate(group):
            pos[n["id"]] = (PAD + ci * (BW + GX), y0 + ri * (BH + 16 + GY))

    out = [f'<svg class="dg" viewBox="0 0 {W:.0f} {H:.0f}" role="img" '
           f'aria-label="How the pieces fit together" '
           f'xmlns="http://www.w3.org/2000/svg">']
    # marker inherits the path stroke, so one def serves every edge and it
    # re-colours for print along with everything else
    out.append('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" '
               'markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" '
               'orient="auto-start-reverse">'
               '<path d="M0,1.5 L9,5 L0,8.5 z" fill="context-stroke"/></marker></defs>')

    R = 12          # corner radius, the single biggest lift in perceived quality
    for e in edges:
        a, b = pos.get(e["from"]), pos.get(e["to"])
        if not a or not b:
            continue
        x1, y1 = a[0] + BW, a[1] + BH / 2
        x2, y2 = b[0], b[1] + BH / 2
        if x2 < x1:
            continue                     # backward edges add crossings, not meaning
        if abs(y2 - y1) < 2:
            d = f"M{x1:.0f},{y1:.0f} H{x2:.0f}"
        else:
            mid = x1 + (x2 - x1) / 2
            down = 1 if y2 > y1 else -1
            d = (f"M{x1:.0f},{y1:.0f} H{mid-R:.0f} "
                 f"Q{mid:.0f},{y1:.0f} {mid:.0f},{y1+R*down:.0f} "
                 f"V{y2-R*down:.0f} Q{mid:.0f},{y2:.0f} {mid+R:.0f},{y2:.0f} "
                 f"H{x2:.0f}")
        out.append(f'<path class="dg-e" d="{d}" fill="none" stroke-width="1.75" '
                   f'stroke-linecap="round" stroke-linejoin="round" '
                   f'marker-end="url(#ah)"/>')

    # Nodes: no box. The label IS the node, sitting on a rule. The old rects
    # measured 1.05-1.13:1 against the surface, so they were ink encoding nothing.
    for n in nodes:
        x, y = pos[n["id"]]
        k = n.get("kind") if n.get("kind") in KIND_LABEL else "system"
        build = k == "ai"
        cls = "dg-n dg-build" if build else "dg-n"
        out.append(f'<rect class="{cls}-bar" x="{x:.0f}" y="{y:.0f}" '
                   f'width="{BW}" height="2.5" rx="1.25"/>')
        # the kind rides ON the node, not in a legend (spatial contiguity, d=1.10)
        out.append(f'<text class="dg-k" x="{x:.0f}" y="{y+20:.0f}">'
                   f'{esc(KIND_LABEL[k].upper())}</text>')
        label = str(n["label"])
        words, lines, cur = label.split(), [], ""
        limit = max(12, int(BW / 7.4))
        for w in words:
            if len(cur + " " + w) > limit and cur:
                lines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            lines.append(cur)
        for i, ln in enumerate(lines[:3]):
            out.append(f'<text class="{cls}" x="{x:.0f}" y="{y+41+i*17:.0f}">'
                       f'{esc(ln)}</text>')
    out.append("</svg>")
    return "".join(out)


# ---------- document ----------

def section(num, title, lede=None, body=""):
    n = f'<span class="sec-n">{esc(num)}</span>' if num else ""
    l = f'<p class="sec-lede">{esc(lede)}</p>' if has(lede) else ""
    return (f'<hr class="div"><section class="sec">{n}'
            f'<h2 class="prose">{esc(title)}</h2>{l}{body}</section>')


def callout(big, note=None):
    n = f"<p>{esc(note)}</p>" if has(note) else ""
    return f'<div class="callout"><span class="big">{esc(big)}</span>{n}</div>'


def render(study, demo_embed=None):
    m = study.get("meta", {})
    company = esc(m.get("company") or "your company")
    out = []

    # ---- cover ----
    out.append('<header class="cover">')
    out.append('<div class="mark"><i></i>Alaska AI</div>')
    out.append(f'<p class="eyebrow">Field study prepared for {company}</p>')
    out.append(f'<h1>{esc(study.get("thesis") or "")}</h1>')
    bits = []
    if has(m.get("place")):
        bits.append(f"<span>{esc(m['place'])}</span>")
    if has(m.get("date")):
        bits.append(f"<span>{esc(m['date'])}</span>")
    if bits:
        out.append(f'<p class="covermeta">{"".join(bits)}</p>')
    out.append("</header>")

    # ---- the standalone brief (layer one) ----
    brief = study.get("brief") or study.get("finding")
    if has(brief):
        out.append('<div class="brief"><h2>In short</h2>' + para(brief) + "</div>")

    n = 0

    def nxt():
        nonlocal n
        n += 1
        return f"{n:02d}"

    # ---- 01 what we found ----
    hw = study.get("homework") or {}
    found = study.get("found") or {}
    body = para(found.get("body") or get(hw, "pain", "context"), "prose")
    src = found.get("source") or get(hw, "pain", "source")
    if has(body):
        if has(found.get("callout_big")):
            body += callout(found["callout_big"], found.get("callout_note"))
        if has(found.get("body_2")):
            body += para(found["body_2"], "prose")
        out.append(section(nxt(), found.get("title") or "What we found",
                           found.get("lede"), body))

    # ---- 02 what it is costing ----
    cost = study.get("costing") or {}
    if has(cost.get("body")):
        b = para(cost["body"], "prose")
        if has(cost.get("callout_big")):
            b += callout(cost["callout_big"], cost.get("callout_note"))
        if has(cost.get("body_2")):
            b += para(cost["body_2"], "prose")
        out.append(section(nxt(), cost.get("title") or "What it is costing",
                           cost.get("lede"), b))

    # ---- 03 what would change (outcome, before the build) ----
    opp = study.get("opportunity") or {}
    if has(opp.get("outcome_body")) or has(opp.get("why")):
        b = para(opp.get("outcome_body") or opp.get("why"), "prose")
        if has(opp.get("current_workaround")):
            b += para(opp["current_workaround"], "prose")
        out.append(section(nxt(), opp.get("title") or "What would change",
                           opp.get("lede"), b))

    # ---- 04 what we would build ----
    build = study.get("build") or {}
    if has(build.get("what_it_does")):
        b = ""
        if has(build.get("plain_parts")):        # pre-training, plain nouns first
            b += para(build["plain_parts"], "prose")
        b += para(build["what_it_does"], "prose")
        arch = build.get("architecture") or {}
        svg = render_diagram(arch)
        if svg:
            b += f'<div class="figure">{svg}'
            if has(arch.get("caption")):
                b += f'<p class="figcap">{esc(arch["caption"])}</p>'
            b += "</div>"
        if demo_embed:
            b += (f'<div class="demoembed"><iframe src="{esc(demo_embed)}" '
                  f'title="Interactive demonstration of the recommended build" '
                  f'loading="lazy"></iframe></div>'
                  f'<p class="figcap">A working demonstration, built on your own facts. '
                  f'It is a demonstration and it is honest about that, and it does '
                  f'nothing this study did not scope. '
                  f'<a href="{esc(demo_embed)}" target="_blank" rel="noopener">'
                  f'Open it full screen</a>.</p>')
        if has(build.get("feasibility")):
            b += para(build["feasibility"], "prose")
        if has(build.get("build_vs_buy")):
            b += para(build["build_vs_buy"], "prose")
        out.append(section(nxt(), build.get("title") or f'What we would build',
                           build.get("lede"), b))

    # ---- 05 what it costs and returns ----
    roi = study.get("roi") or {}
    if any(has(roi.get(k)) for k in ("table", "lede_body", "scenarios", "cost_note")):
        b = ""
        if has(roi.get("lede_body")):
            b += para(roi["lede_body"], "prose")
        rows = roi.get("table") or []
        if rows:
            heads = roi.get("table_head") or ["", "Conservative", "Most likely", "Aggressive"]
            t = ['<div class="tw"><table>']
            if has(roi.get("table_caption")):
                t.append(f'<caption>{esc(roi["table_caption"])}</caption>')
            numcls = ' class="num"'
            t.append("<thead><tr>" + "".join(
                "<th%s>%s</th>" % (numcls if i else "", esc(h))
                for i, h in enumerate(heads)) + "</tr></thead><tbody>")
            for r in rows:
                cls = ' class="total"' if r.get("emphasis") else ""
                cells = "".join(f'<td class="num">{esc(c)}</td>' for c in r.get("cells", []))
                t.append(f'<tr{cls}><td>{esc(r.get("label",""))}</td>{cells}</tr>')
            t.append("</tbody>")
            if has(roi.get("table_note")):
                t.append(f'<tfoot><tr><td colspan="{len(heads)}">'
                         f'{esc(roi["table_note"])}</td></tr></tfoot>')
            t.append("</table></div>")
            b += "".join(t)
        if has(roi.get("payback_range")):
            b += callout(roi.get("payback_big") or "Payback", roi["payback_range"])
        if has(roi.get("base_rate_note")):
            b += para(roi["base_rate_note"], "prose")
        if has(roi.get("value_owner")):
            b += para(roi["value_owner"], "prose")
        out.append(section(nxt(), roi.get("title") or "What it costs, and what it returns",
                           roi.get("lede"), b))

    # ---- 06 how we would start ----
    rm = study.get("roadmap") or {}
    if has(rm.get("body")) or has(rm.get("now")):
        b = para(rm.get("body"), "prose")
        lanes = [("Now", rm.get("now")), ("Next", rm.get("next")), ("Later", rm.get("later"))]
        rows = [(k, v) for k, v in lanes if has(v)]
        if rows:
            t = ['<div class="tw"><table><thead><tr><th>Phase</th><th>What runs</th>'
                 '<th>How we would know it worked</th></tr></thead><tbody>']
            for label, items in rows:
                for i, it in enumerate(items):
                    lab = esc(label) if i == 0 else ""
                    t.append(f'<tr><td>{lab}</td><td>{esc(it.get("item",""))}</td>'
                             f'<td>{esc(it.get("metric",""))}</td></tr>')
            t.append("</tbody>")
            if has(rm.get("gates")):
                t.append(f'<tfoot><tr><td colspan="3">{esc(rm["gates"])}</td></tr></tfoot>')
            t.append("</table></div>")
            b += "".join(t)
        if has(rm.get("need_from_you")):
            b += para(rm["need_from_you"], "prose")
        out.append(section(nxt(), rm.get("title") or "How we would start",
                           rm.get("lede"), b))

    # ---- 07 what would make us wrong ----
    hp = study.get("honest") or {}
    legacy = study.get("honest_part")
    if has(hp.get("body")):
        b = para(hp["body"], "prose")
        out.append(section(nxt(), hp.get("title") or "What would make us wrong",
                           hp.get("lede"), b))
    elif has(legacy):
        items = "".join(f"<li>{esc(x)}</li>" for x in legacy if has(x))
        out.append(section(nxt(), "What would make us wrong", None,
                           f'<ul class="clean">{items}</ul>'))

    # ---- 08 the next step ----
    if has(study.get("next_step")):
        out.append(section(nxt(), study.get("next_step_title") or "The next step",
                           None, para(study["next_step"], "prose")))

    # ---- sources ----
    srcs = [s for s in (study.get("sources") or []) if has(s.get("url"))]
    if srcs:
        li = "".join(
            f'<li>{esc(s.get("claim",""))}<br><a href="{esc(s["url"])}">{esc(s["url"])}</a></li>'
            for s in srcs)
        out.append(section(None, "What we checked",
                           "Every number in this study traces to a page we read. "
                           "If we have any of it wrong, that is worth knowing too.",
                           f'<ol class="srcs">{li}</ol>'))

    out.append(f'<p class="foot">Alaska AI. Prepared for {company}. '
               f'Not for redistribution.</p>')
    return "".join(out)


def audit(study, rendered):
    """Warn when study.json carries content the page never showed.

    A gate condition that misses a renamed key drops an entire section with no
    error, which is exactly how a study ships without its numbers. Anything with
    real text in it should appear somewhere in the output.
    """
    missing = []

    def walk(node, path):
        if isinstance(node, dict):
            for k, v in node.items():
                walk(v, path + [k])
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, path + [str(i)])
        elif isinstance(node, str) and len(node.split()) >= 6:
            probe = esc(" ".join(node.split()[:6]))
            if probe not in rendered:
                missing.append(".".join(path))

    for key, val in study.items():
        if key in ("meta", "sources"):
            continue
        walk(val, [key])
    return missing


def build_html(study, demo_embed=None):
    title = esc((study.get("meta") or {}).get("company") or "Alaska AI")
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>Field Study, {title}</title>'
            f'<style>{embedded_fonts()}{CSS}</style></head><body><div class="page">'
            f'{render(study, demo_embed)}</div></body></html>')


def try_pdf(html_path, pdf_path):
    for exe in ("/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
                "chromium", "chromium-browser", "google-chrome"):
        try:
            r = subprocess.run(
                [exe, "--headless", "--no-sandbox", "--disable-gpu",
                 f"--print-to-pdf={pdf_path}", "--no-pdf-header-footer",
                 f"file://{os.path.abspath(html_path)}"],
                capture_output=True, timeout=120)
            if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 1000:
                return True
        except Exception:
            continue
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--study", required=True, help="path to study.json")
    ap.add_argument("--out", required=True, help="output .html path")
    ap.add_argument("--pdf", action="store_true", help="also render a PDF (best effort)")
    ap.add_argument("--demo-embed", default=None,
                    help="relative src of the demo to embed, e.g. demo/index.html")
    args = ap.parse_args()

    with open(args.study, encoding="utf-8") as fh:
        study = json.load(fh)

    html_str = build_html(study, args.demo_embed)

    dropped = audit(study, html_str)
    if dropped:
        print("WARNING: content in study.json never reached the page:", file=sys.stderr)
        for d in dropped:
            print(f"  - {d}", file=sys.stderr)

    os.makedirs(os.path.dirname(os.path.abspath(args.out)) or ".", exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(html_str)
    print(f"wrote {args.out}  ({len(html_str)} bytes)")

    if args.pdf:
        pdf = os.path.splitext(args.out)[0] + ".pdf"
        print(f"wrote {pdf}" if try_pdf(args.out, pdf) else "pdf skipped (no chromium)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
