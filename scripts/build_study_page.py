#!/usr/bin/env python3
"""
build_study_page.py

Render a personalized Field Study (study.json) into a single self-contained HTML
page, on brand with alaskaaihq.com, with an inline SVG architecture diagram and
zero external calls. Optionally render a PDF via the pre-installed Chromium.

The room assembles study.json (see knowledge/FIELD_STUDY_SPEC.md). This script only
renders it. Sections whose data is missing are dropped rather than faked. All text
is HTML-escaped, so nothing in the data can break the page or inject markup.

Usage:
  python scripts/build_study_page.py --study out/<date>/study.json \\
      --out out/<date>/field-study.html [--pdf]

Stdlib only for the HTML. PDF is best effort and never blocks the HTML.
"""

import argparse
import html
import json
import os
import shutil
import subprocess
import sys


# ---------- helpers ----------

def esc(v):
    """HTML-escape any scalar; empty string for None."""
    if v is None:
        return ""
    return html.escape(str(v), quote=True)


def has(v):
    """True when a value carries real content."""
    if v is None:
        return False
    if isinstance(v, str):
        return v.strip() != ""
    if isinstance(v, (list, dict)):
        return len(v) > 0
    return True


def get(d, *path, default=None):
    cur = d
    for k in path:
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur


# ---------- brand css (inline, dark, restrained, aurora accent) ----------

CSS = """
:root{
  --bg:#070b12; --panel:#0d1420; --panel2:#111a28; --line:#1e2b3d;
  --ink:#eef3fb; --muted:#9fb0c6; --faint:#6f7f96;
  --aur1:#57e0c8; --aur2:#5aa9ff; --aur3:#9b8cff; --warm:#ffd18c;
  --good:#5fd0a6; --warn:#ffb35c;
  --maxw:820px;
}
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{
  margin:0;background:
    radial-gradient(1100px 500px at 78% -8%, rgba(90,169,255,.12), transparent 60%),
    radial-gradient(900px 460px at 8% 4%, rgba(87,224,200,.10), transparent 55%),
    var(--bg);
  color:var(--ink);
  font:16px/1.62 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,Helvetica,Arial,sans-serif;
  letter-spacing:.1px;
}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 22px 90px}
.eyebrow{font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--faint);margin:0 0 10px}
h1{font-size:clamp(30px,5.4vw,50px);line-height:1.04;margin:.1em 0 .28em;font-weight:680;letter-spacing:-.4px}
h2{font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:var(--aur1);margin:0 0 4px;font-weight:640}
.sec>h3,h3{font-size:clamp(20px,3vw,27px);line-height:1.15;margin:.1em 0 .5em;font-weight:640;letter-spacing:-.2px}
p{margin:0 0 14px}
a{color:var(--aur2);text-decoration:none;border-bottom:1px solid rgba(90,169,255,.35)}
strong{color:#fff;font-weight:640}
.small{font-size:13.5px;color:var(--muted)}
.faint{color:var(--faint)}
.mono{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}

/* cover */
.cover{padding:74px 0 30px;border-bottom:1px solid var(--line)}
.mark{display:flex;align-items:center;gap:11px;font-weight:660;letter-spacing:.02em}
.dot{width:11px;height:11px;border-radius:50%;
  background:radial-gradient(circle at 35% 30%,var(--aur1),var(--aur3));
  box-shadow:0 0 16px 2px rgba(87,224,200,.5)}
.thesis{font-size:clamp(19px,2.7vw,24px);line-height:1.4;color:var(--ink);max-width:46rem;margin:.2em 0 1.1em;font-weight:480}
.byline{font-size:13px;color:var(--faint);display:flex;flex-wrap:wrap;gap:8px 16px;align-items:center}
.byline .pill{border:1px solid var(--line);border-radius:999px;padding:3px 11px;color:var(--muted)}

/* sections */
.sec{padding:34px 0;border-bottom:1px solid var(--line)}
.sec:last-of-type{border-bottom:0}
.grid{display:grid;gap:14px}
@media(min-width:680px){.grid.c2{grid-template-columns:1fr 1fr}}
.card{background:linear-gradient(180deg,var(--panel),var(--panel2));border:1px solid var(--line);
  border-radius:14px;padding:18px 19px}
.card h4{margin:0 0 7px;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--aur1);font-weight:640}
.card p:last-child{margin-bottom:0}
.quote{border-left:2px solid var(--aur1);padding:6px 0 6px 18px;margin:4px 0 12px;color:#dbe6f5;font-size:18px;line-height:1.5}
.src{font-size:12px;color:var(--faint)}
.src a{color:var(--faint);border-bottom-color:rgba(111,127,150,.4)}
ul.clean{list-style:none;padding:0;margin:0 0 12px}
ul.clean li{padding:7px 0 7px 22px;position:relative;border-bottom:1px solid rgba(30,43,61,.6)}
ul.clean li:last-child{border-bottom:0}
ul.clean li:before{content:"";position:absolute;left:2px;top:15px;width:7px;height:7px;border-radius:50%;
  background:var(--aur2);box-shadow:0 0 9px rgba(90,169,255,.6)}
.tag{display:inline-block;font-size:11px;letter-spacing:.08em;text-transform:uppercase;
  border:1px solid var(--line);border-radius:6px;padding:1px 7px;color:var(--muted);margin-left:8px}
.tag.cash{color:var(--good);border-color:rgba(95,208,166,.4)}
.tag.capacity{color:var(--warm);border-color:rgba(255,209,140,.35)}

/* tables */
.tw{overflow-x:auto;margin:0 0 12px;border:1px solid var(--line);border-radius:12px}
table{border-collapse:collapse;width:100%;font-size:14px;min-width:460px}
th,td{text-align:left;padding:10px 13px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--faint);font-weight:560;font-size:12px;letter-spacing:.06em;text-transform:uppercase}
tr:last-child td{border-bottom:0}
td .k{color:#fff;font-weight:560}

/* two-column split for goals/non-goals etc */
.split{display:grid;gap:14px}
@media(min-width:680px){.split{grid-template-columns:1fr 1fr}}

/* roadmap */
.road{display:grid;gap:12px}
@media(min-width:720px){.road{grid-template-columns:repeat(3,1fr)}}
.lane{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:15px 16px}
.lane h4{margin:0 0 3px;font-size:15px;font-weight:640}
.lane .when{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--faint);margin-bottom:9px}
.lane.now{border-color:rgba(87,224,200,.4)}
.lane .item{font-size:14px;padding:8px 0;border-top:1px solid rgba(30,43,61,.7)}
.lane .item:first-of-type{border-top:0}
.lane .metric{display:block;color:var(--faint);font-size:12px;margin-top:2px}

/* scenario strip */
.scn{display:grid;gap:10px;margin:2px 0 12px}
@media(min-width:640px){.scn{grid-template-columns:repeat(3,1fr)}}
.scn .b{border:1px solid var(--line);border-radius:12px;padding:13px 14px;background:var(--panel)}
.scn .b .lab{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--faint);margin-bottom:5px}
.scn .b.cons{border-color:rgba(95,208,166,.45)}
.scn .b.cons .lab{color:var(--good)}
.clears{font-size:14px;color:var(--good);margin:0 0 8px}

/* diagram */
.diagram{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:10px;overflow-x:auto;margin:0 0 10px}
.diagram svg{display:block;min-width:520px;width:100%;height:auto}
.legend{display:flex;flex-wrap:wrap;gap:6px 15px;font-size:12px;color:var(--muted);margin:2px 2px 0}
.legend span{display:inline-flex;align-items:center;gap:6px}
.legend i{width:10px;height:10px;border-radius:3px;display:inline-block}

/* honest / callout */
.callout{background:linear-gradient(180deg,rgba(255,179,92,.07),rgba(255,179,92,.02));
  border:1px solid rgba(255,179,92,.28);border-radius:14px;padding:17px 19px}
.callout h3{color:var(--warm)}
.next{background:linear-gradient(180deg,var(--panel2),var(--panel));border:1px solid var(--line);
  border-radius:16px;padding:22px 22px;margin-top:8px}

/* sources */
ol.src-list{font-size:12.5px;color:var(--faint);padding-left:20px;margin:6px 0 0}
ol.src-list li{margin:0 0 6px;word-break:break-word}
ol.src-list a{color:var(--muted)}

footer{color:var(--faint);font-size:12px;padding:26px 0 0;text-align:center}

@media print{
  body{background:var(--bg)}
  .sec,.cover{page-break-inside:avoid}
}
"""


# ---------- svg architecture diagram ----------

KIND_ORDER = ["user", "external", "system", "ai", "data"]
KIND_FILL = {
    "user": "#1a2740", "external": "#1a2740", "system": "#14233a",
    "ai": "#123a34", "data": "#241a3a",
}
KIND_STROKE = {
    "user": "#5aa9ff", "external": "#5aa9ff", "system": "#5aa9ff",
    "ai": "#57e0c8", "data": "#9b8cff",
}
KIND_LABEL = {
    "user": "Person", "external": "External", "system": "Their system",
    "ai": "We build", "data": "Data",
}


def render_diagram(arch):
    """Layered left-to-right SVG from nodes/edges. Deterministic, self-contained."""
    nodes = [n for n in (arch.get("nodes") or []) if has(n.get("id")) and has(n.get("label"))]
    edges = arch.get("edges") or []
    if not nodes:
        return ""

    # column per kind, in KIND_ORDER; unknown kinds go to a trailing column
    cols = {}
    for n in nodes:
        k = n.get("kind") if n.get("kind") in KIND_ORDER else "system"
        cols.setdefault(k, []).append(n)
    used = [k for k in KIND_ORDER if k in cols]

    NW, NH = 150, 62          # node box
    CXG, RYG = 214, 26        # column gap (center to center), row gap
    padx, pady = 26, 30
    ncols = len(used)
    maxrows = max(len(cols[k]) for k in used)
    W = padx * 2 + NW + (ncols - 1) * CXG
    H = pady * 2 + maxrows * NH + (maxrows - 1) * RYG
    H = max(H, 160)

    pos = {}   # id -> (cx, cy)
    for ci, k in enumerate(used):
        group = cols[k]
        cx = padx + NW / 2 + ci * CXG
        block = len(group) * NH + (len(group) - 1) * RYG
        y0 = (H - block) / 2
        for ri, n in enumerate(group):
            cy = y0 + NH / 2 + ri * (NH + RYG)
            pos[n["id"]] = (cx, cy, k, n["label"])

    def esc_s(s):
        return html.escape(str(s), quote=True)

    parts = []
    parts.append(
        f'<svg viewBox="0 0 {int(W)} {int(H)}" role="img" '
        f'aria-label="Architecture diagram" xmlns="http://www.w3.org/2000/svg">'
    )
    parts.append(
        '<defs><marker id="arw" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
        'markerHeight="7" orient="auto-start-end">'
        '<path d="M0 0 L10 5 L0 10 z" fill="#5f7290"/></marker></defs>'
    )

    # edges first (under nodes)
    for e in edges:
        a, b = e.get("from"), e.get("to")
        if a not in pos or b not in pos:
            continue
        ax, ay, _, _ = pos[a]
        bx, by, _, _ = pos[b]
        # start/end at box edges horizontally
        x1 = ax + NW / 2 if bx >= ax else ax - NW / 2
        x2 = bx - NW / 2 if bx >= ax else bx + NW / 2
        mx = (x1 + x2) / 2
        parts.append(
            f'<path d="M{x1:.0f} {ay:.0f} C{mx:.0f} {ay:.0f} {mx:.0f} {by:.0f} {x2:.0f} {by:.0f}" '
            f'fill="none" stroke="#3a4a63" stroke-width="1.5" marker-end="url(#arw)"/>'
        )
        lab = e.get("label")
        if has(lab):
            parts.append(
                f'<text x="{mx:.0f}" y="{(ay + by) / 2 - 5:.0f}" fill="#8698b3" '
                f'font-size="10.5" text-anchor="middle" font-family="ui-monospace,monospace">{esc_s(lab)}</text>'
            )

    # nodes
    for nid, (cx, cy, k, label) in pos.items():
        x = cx - NW / 2
        y = cy - NH / 2
        fill = KIND_FILL.get(k, "#14233a")
        stroke = KIND_STROKE.get(k, "#5aa9ff")
        parts.append(
            f'<rect x="{x:.0f}" y="{y:.0f}" width="{NW}" height="{NH}" rx="11" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="1.4" opacity="0.96"/>'
        )
        parts.append(
            f'<text x="{cx:.0f}" y="{y + 16:.0f}" fill="{stroke}" font-size="9" '
            f'text-anchor="middle" font-family="ui-monospace,monospace" letter-spacing="0.6" '
            f'opacity="0.85">{esc_s(KIND_LABEL.get(k, "").upper())}</text>'
        )
        # wrap label to <= ~20 chars/line, max 2 lines
        words = str(label).split()
        lines, cur = [], ""
        for w in words:
            if len(cur) + len(w) + 1 <= 20:
                cur = (cur + " " + w).strip()
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        lines = lines[:2]
        ty = cy + 6 - (len(lines) - 1) * 7
        for ln in lines:
            parts.append(
                f'<text x="{cx:.0f}" y="{ty:.0f}" fill="#eef3fb" font-size="12.5" '
                f'text-anchor="middle" font-weight="600">{esc_s(ln)}</text>'
            )
            ty += 15
    parts.append("</svg>")

    # legend for kinds actually used
    leg = []
    for k in used:
        leg.append(
            f'<span><i style="background:{KIND_STROKE[k]}"></i>{esc_s(KIND_LABEL[k])}</span>'
        )
    legend = f'<div class="legend">{"".join(leg)}</div>'
    return f'<div class="diagram">{"".join(parts)}</div>{legend}'


# ---------- section renderers ----------

def sec_open(h2, h3=None):
    s = f'<section class="sec"><h2>{esc(h2)}</h2>'
    if h3:
        s += f"<h3>{esc(h3)}</h3>"
    return s


def render(study):
    m = study.get("meta", {})
    company = esc(m.get("company") or "your company")
    out = []

    # ---- cover ----
    out.append('<div class="wrap">')
    out.append('<header class="cover">')
    out.append('<div class="mark"><span class="dot"></span> Alaska AI</div>')
    out.append(f'<p class="eyebrow" style="margin-top:26px">Field Study prepared for {company}</p>')
    if has(study.get("thesis")):
        out.append(f'<h1>{esc(study["thesis"])}</h1>')
    if has(study.get("finding")):
        out.append(f'<p class="thesis">{esc(study["finding"])}</p>')
    by = []
    if has(m.get("segment")):
        by.append(f'<span class="pill">{esc(str(m.get("segment")).title())}</span>')
    if has(m.get("place")):
        by.append(f'<span class="pill">{esc(m.get("place"))}</span>')
    if has(m.get("date")):
        by.append(f'<span>{esc(m.get("date"))}</span>')
    by.append('<span class="faint">Researched and drafted by Alaska AI\'s agent team, reviewed by a human before it reached you</span>')
    out.append(f'<div class="byline">{"".join(by)}</div>')
    out.append("</header>")

    # ---- what we saw ----
    hw = study.get("homework", {})
    if has(hw):
        out.append(sec_open("What we saw", "The homework"))
        out.append('<div class="grid c2">')
        if has(hw.get("business")):
            out.append(f'<div class="card"><h4>The business</h4><p>{esc(hw["business"])}</p></div>')
        pain = hw.get("pain") or {}
        if has(pain.get("quote")) or has(pain.get("context")):
            block = '<div class="card"><h4>The real pain</h4>'
            if has(pain.get("quote")):
                block += f'<div class="quote">{esc(pain["quote"])}</div>'
            if has(pain.get("context")):
                block += f'<p>{esc(pain["context"])}</p>'
            if has(pain.get("source")):
                block += f'<p class="src">Source: <a href="{esc(pain["source"])}">{esc(pain["source"])}</a></p>'
            block += "</div>"
            out.append(block)
        out.append("</div>")
        comps = [c for c in (hw.get("competitors") or []) if has(c.get("name"))]
        inds = [i for i in (hw.get("industry_ai") or []) if has(i.get("point"))]
        if comps or inds:
            out.append('<div class="split" style="margin-top:14px">')
            if comps:
                b = '<div class="card"><h4>The field around them</h4><ul class="clean">'
                for c in comps:
                    line = f'<strong>{esc(c["name"])}</strong> {esc(c.get("what_ai"))}'
                    if has(c.get("source")):
                        line += f' <span class="src"><a href="{esc(c["source"])}">source</a></span>'
                    b += f"<li>{line}</li>"
                b += "</ul></div>"
                out.append(b)
            if inds:
                b = '<div class="card"><h4>AI in this industry now</h4><ul class="clean">'
                for i in inds:
                    line = esc(i["point"])
                    if has(i.get("source")):
                        line += f' <span class="src"><a href="{esc(i["source"])}">source</a></span>'
                    b += f"<li>{line}</li>"
                b += "</ul></div>"
                out.append(b)
            out.append("</div>")
        out.append("</section>")

    # ---- the opportunity ----
    op = study.get("opportunity", {})
    if has(op.get("job")):
        out.append(sec_open("The opportunity", op.get("job")))
        if has(op.get("why")):
            out.append(f'<p>{esc(op["why"])}</p>')
        bits = []
        if has(op.get("current_workaround")):
            bits.append(f'<div class="card"><h4>What they use today</h4><p>{esc(op["current_workaround"])}</p></div>')
        if has(op.get("forces")):
            bits.append(f'<div class="card"><h4>Why a change is realistic</h4><p>{esc(op["forces"])}</p></div>')
        if bits:
            out.append(f'<div class="grid c2">{"".join(bits)}</div>')
        out.append("</section>")

    # ---- the recommended build ----
    b = study.get("build", {})
    if has(b.get("name")):
        out.append(sec_open("The recommended build", b.get("name")))
        if has(b.get("what_it_does")):
            out.append(f'<p>{esc(b["what_it_does"])}</p>')
        arch = b.get("architecture") or {}
        dia = render_diagram(arch)
        if dia:
            out.append(dia)
            if has(arch.get("caption")):
                out.append(f'<p class="small faint">{esc(arch["caption"])}</p>')
        cards = []
        if has(b.get("feasibility")):
            cards.append(f'<div class="card"><h4>Where AI fits, and where it does not</h4><p>{esc(b["feasibility"])}</p></div>')
        if has(b.get("build_vs_buy")):
            cards.append(f'<div class="card"><h4>Build vs buy</h4><p>{esc(b["build_vs_buy"])}</p></div>')
        if cards:
            out.append(f'<div class="grid c2" style="margin-top:6px">{"".join(cards)}</div>')
        out.append("</section>")

    # ---- the plan ----
    pl = study.get("plan", {})
    if has(pl):
        out.append(sec_open("The plan", "What we would build, scoped"))
        if has(pl.get("problem")):
            out.append(f'<p>{esc(pl["problem"])}</p>')
        # goals / non-goals
        goals = [g for g in (pl.get("goals") or []) if has(g)]
        ngoals = [n for n in (pl.get("non_goals") or []) if has(n.get("item"))]
        if goals or ngoals:
            out.append('<div class="split">')
            if goals:
                gl = "".join(f"<li>{esc(g)}</li>" for g in goals)
                out.append(f'<div class="card"><h4>Goals</h4><ul class="clean">{gl}</ul></div>')
            if ngoals:
                nl = "".join(f'<li>{esc(n["item"])} <span class="faint">({esc(n.get("reason"))})</span></li>' for n in ngoals)
                out.append(f'<div class="card"><h4>Non-goals, on purpose</h4><ul class="clean">{nl}</ul></div>')
            out.append("</div>")
        # metrics table
        mets = [x for x in (pl.get("metrics") or []) if has(x.get("metric"))]
        if mets:
            rows = ""
            for x in mets:
                rows += (f'<tr><td class="k">{esc(x["metric"])}</td><td>{esc(x.get("baseline"))}</td>'
                         f'<td>{esc(x.get("target"))}</td><td>{esc(x.get("timeframe"))}</td></tr>')
            out.append('<h4 style="margin:18px 0 8px;color:var(--aur1);font-size:12px;letter-spacing:.16em;text-transform:uppercase">How we would measure success</h4>')
            out.append('<div class="tw"><table><thead><tr><th>Metric</th><th>Baseline</th>'
                       '<th>Target</th><th>By when</th></tr></thead><tbody>'
                       f'{rows}</tbody></table></div>')
        # phase 1 scope
        must = [x for x in (pl.get("phase1_must") or []) if has(x)]
        later = [x for x in (pl.get("phase1_later") or []) if has(x)]
        if must or later:
            out.append('<div class="split">')
            if must:
                out.append('<div class="card"><h4>Phase one, must have</h4><ul class="clean">'
                           + "".join(f"<li>{esc(x)}</li>" for x in must) + "</ul></div>")
            if later:
                out.append('<div class="card"><h4>Deliberately later</h4><ul class="clean">'
                           + "".join(f"<li>{esc(x)}</li>" for x in later) + "</ul></div>")
            out.append("</div>")
        # need from you
        need = [x for x in (pl.get("need_from_you") or []) if has(x)]
        if need:
            out.append('<div class="card" style="margin-top:14px"><h4>What we would need from you</h4><ul class="clean">'
                       + "".join(f"<li>{esc(x)}</li>" for x in need) + "</ul></div>")
        # risks
        risks = [x for x in (pl.get("risks") or []) if has(x.get("risk"))]
        if risks:
            rows = "".join(f'<tr><td class="k">{esc(x["risk"])}</td><td>{esc(x.get("mitigation"))}</td></tr>' for x in risks)
            out.append('<h4 style="margin:18px 0 8px;color:var(--aur1);font-size:12px;letter-spacing:.16em;text-transform:uppercase">Risks, and how we would handle them</h4>')
            out.append(f'<div class="tw"><table><thead><tr><th>Risk</th><th>Mitigation</th></tr></thead><tbody>{rows}</tbody></table></div>')
        # open questions
        oq = [x for x in (pl.get("open_questions") or []) if has(x.get("q"))]
        if oq:
            out.append('<div class="card" style="margin-top:8px"><h4>Open questions we would resolve together</h4><ul class="clean">'
                       + "".join(f'<li>{esc(x["q"])} <span class="faint">({esc(x.get("owner"))})</span></li>' for x in oq) + "</ul></div>")
        out.append("</section>")

    # ---- the numbers ----
    roi = study.get("roi", {})
    if has(roi):
        out.append(sec_open("The numbers", "Honest ROI, not a hero number"))
        if has(roi.get("cost_note")):
            out.append(f'<div class="card"><h4>What it costs to run, five year view</h4><p>{esc(roi["cost_note"])}</p></div>')
        bens = [x for x in (roi.get("benefits") or []) if has(x.get("benefit"))]
        if bens:
            lis = ""
            for x in bens:
                kind = str(x.get("kind") or "").lower()
                tag = ""
                if kind in ("cash", "capacity"):
                    tag = f'<span class="tag {kind}">{kind}</span>'
                note = f' <span class="faint">{esc(x.get("note"))}</span>' if has(x.get("note")) else ""
                lis += f'<li><strong>{esc(x["benefit"])}</strong>{tag}{note}</li>'
            out.append(f'<div class="card" style="margin-top:14px"><h4>Where the value comes from</h4><ul class="clean">{lis}</ul></div>')
        scn = roi.get("scenarios") or {}
        if has(scn.get("conservative")) or has(scn.get("most_likely")) or has(scn.get("aggressive")):
            out.append('<div class="scn" style="margin-top:14px">')
            out.append(f'<div class="b cons"><div class="lab">Conservative</div>{esc(scn.get("conservative"))}</div>')
            out.append(f'<div class="b"><div class="lab">Most likely</div>{esc(scn.get("most_likely"))}</div>')
            out.append(f'<div class="b"><div class="lab">Aggressive</div>{esc(scn.get("aggressive"))}</div>')
            out.append("</div>")
        if roi.get("conservative_clears") is True:
            out.append('<p class="clears">The conservative case still clears the bar. That is the case we would stand behind.</p>')
        if has(roi.get("payback_range")):
            out.append(f'<p><strong>Payback</strong> {esc(roi["payback_range"])}</p>')
        if has(roi.get("base_rate_note")):
            out.append(f'<div class="callout" style="margin-top:8px"><h3>The honest base rate</h3><p>{esc(roi["base_rate_note"])}</p></div>')
        if has(roi.get("value_owner")):
            out.append(f'<p class="small" style="margin-top:12px"><strong>Who owns the number</strong> {esc(roi["value_owner"])}</p>')
        out.append("</section>")

    # ---- roadmap ----
    rm = study.get("roadmap", {})
    if has(rm.get("now")) or has(rm.get("next")) or has(rm.get("later")):
        out.append(sec_open("The roadmap", "By confidence, not by calendar"))
        out.append('<div class="road">')
        for key, label, cls in (("now", "Now", "now"), ("next", "Next", ""), ("later", "Later", "")):
            items = [x for x in (rm.get(key) or []) if has(x.get("item"))]
            lane = f'<div class="lane {cls}"><div class="when">{esc(label)}</div>'
            if not items:
                lane += '<div class="item faint">to be shaped</div>'
            for x in items:
                met = f'<span class="metric">{esc(x.get("metric"))}</span>' if has(x.get("metric")) else ""
                lane += f'<div class="item">{esc(x["item"])}{met}</div>'
            lane += "</div>"
            out.append(lane)
        out.append("</div>")
        if has(rm.get("gates")):
            out.append(f'<p class="small faint" style="margin-top:10px">{esc(rm["gates"])}</p>')
        out.append("</section>")

    # ---- the honest part ----
    honest = [x for x in (study.get("honest_part") or []) if has(x)]
    if honest:
        out.append('<section class="sec"><div class="callout"><h3>The honest part, what could make this not work</h3><ul class="clean">'
                   + "".join(f"<li>{esc(x)}</li>" for x in honest) + "</ul></div></section>")

    # ---- next step ----
    if has(study.get("next_step")):
        out.append('<section class="sec"><div class="next"><h2>What this is</h2>'
                   '<h3>This is the free version of how we work</h3>'
                   f'<p>{esc(study["next_step"])}</p>'
                   '<p class="small faint">The full picture lives at '
                   '<a href="https://alaskaaihq.com/services/">alaskaaihq.com/services</a>.</p></div></section>')

    # ---- sources ----
    srcs = [s for s in (study.get("sources") or []) if has(s.get("url"))]
    if srcs:
        out.append('<section class="sec"><h2>Sources</h2><ol class="src-list">')
        for s in srcs:
            claim = f'{esc(s.get("claim"))} ' if has(s.get("claim")) else ""
            out.append(f'<li>{claim}<a href="{esc(s["url"])}">{esc(s["url"])}</a></li>')
        out.append("</ol></section>")

    out.append('<footer>Alaska AI, in-state and building. This study was prepared for '
               f'{company} and is not for redistribution.</footer>')
    out.append("</div>")  # wrap
    return "\n".join(out)


def build_html(study):
    title = esc((study.get("meta") or {}).get("company") or "Alaska AI")
    body = render(study)
    return (
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
        f"<title>Field Study, {title}</title>"
        f"<style>{CSS}</style></head><body>{body}</body></html>"
    )


def try_pdf(html_path, pdf_path):
    """Best effort: render the HTML to PDF via the pre-installed Chromium."""
    chrome = None
    for c in (os.environ.get("CHROME_BIN"),
              "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"):
        if c and os.path.exists(c):
            chrome = c
            break
    if not chrome:
        # try any chromium on PATH
        for name in ("chromium", "chromium-browser", "google-chrome", "chrome"):
            p = shutil.which(name)
            if p:
                chrome = p
                break
    if not chrome:
        print("  pdf skipped, no chromium found (html is the deliverable)", file=sys.stderr)
        return False
    try:
        subprocess.run(
            [chrome, "--headless", "--no-sandbox", "--disable-gpu",
             "--no-pdf-header-footer", f"--print-to-pdf={pdf_path}",
             "file://" + os.path.abspath(html_path)],
            check=True, capture_output=True, timeout=120,
        )
        if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 800:
            return True
    except Exception as e:  # noqa: BLE001
        print(f"  pdf skipped, {e.__class__.__name__} (html is the deliverable)", file=sys.stderr)
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--study", required=True, help="path to study.json")
    ap.add_argument("--out", required=True, help="output .html path")
    ap.add_argument("--pdf", action="store_true", help="also render a PDF (best effort)")
    args = ap.parse_args()

    with open(args.study, encoding="utf-8") as fh:
        study = json.load(fh)

    html_str = build_html(study)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)) or ".", exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(html_str)
    print(f"wrote {args.out}  ({len(html_str)} bytes)")

    if args.pdf:
        pdf_path = os.path.splitext(args.out)[0] + ".pdf"
        if try_pdf(args.out, pdf_path):
            print(f"wrote {pdf_path}  ({os.path.getsize(pdf_path)} bytes)")


if __name__ == "__main__":
    main()
