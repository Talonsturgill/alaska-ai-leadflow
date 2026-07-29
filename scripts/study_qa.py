#!/usr/bin/env python3
"""Objective QA for the rendered Field Study page.

The study is a document, not a dashboard, and "does it read well" is mostly
measurable. This checks the rendered HTML against the typography and
information-design standards the page is built to (sources in the table below),
so a redesign can be verified instead of argued about.

  python scripts/study_qa.py --html out/<date>/field-study.html [--json]

Budgets and their sources:
  measure 45-80 char        WCAG 2.2 SC 1.4.8 (<=80), Butterick 45-90, Bringhurst 66
  para spacing >= 1.5x lh   WCAG 2.2 SC 1.4.8
  heading levels <= 3       Butterick "headings"; NN/g <=3 sizes
  total headings <= 18      one signpost per 250-350 words at this length
  bullets <= 25             NN/g, lengthy bullet content becomes a wall of text
  bold <= 30% of words      NN/g formatting-long-form-content
  pull quotes = 0           NN/g eyetracking, pull quotes break the commitment pattern
  body text >= 16px         Piepenbrock 2014, dark-mode penalty is worst at small sizes
  APCA Lc >= 75 body        APCA thresholds; WCAG 2 ratios overstate contrast on dark

Exits 0 if every hard budget passes, 1 otherwise. Advisory checks never fail
the run, they print as NOTE.
"""
import argparse
import json
import re
import sys
import html as htmllib

# ---------- colour math ----------

def _srgb(hexstr):
    h = hexstr.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


def wcag_luminance(hexstr):
    def lin(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(c) for c in _srgb(hexstr))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def wcag_ratio(fg, bg):
    a, b = wcag_luminance(fg), wcag_luminance(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def apca_lc(text_hex, bg_hex):
    """APCA 0.1.9 (W3 draft constants). Negative Lc = light text on dark."""
    def y(hexstr):
        r, g, b = _srgb(hexstr)
        return 0.2126729 * r ** 2.4 + 0.7151522 * g ** 2.4 + 0.0721750 * b ** 2.4
    ytxt, ybg = y(text_hex), y(bg_hex)
    blk_thrs, blk_clmp = 0.022, 1.414
    ytxt = ytxt if ytxt > blk_thrs else ytxt + (blk_thrs - ytxt) ** blk_clmp
    ybg = ybg if ybg > blk_thrs else ybg + (blk_thrs - ybg) ** blk_clmp
    if abs(ybg - ytxt) < 0.0005:
        return 0.0
    if ybg > ytxt:                                  # dark text on light
        sapc = (ybg ** 0.56 - ytxt ** 0.57) * 1.14
        out = 0.0 if sapc < 0.001 else sapc - 0.027
    else:                                           # light text on dark
        sapc = (ybg ** 0.65 - ytxt ** 0.62) * 1.14
        out = 0.0 if sapc > -0.001 else sapc + 0.027
    return out * 100.0


# ---------- html probing ----------

def visible_text(body):
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", body, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return htmllib.unescape(t)


def css_value(css, selector_frag, prop):
    """Best-effort: find `prop:` inside the first rule containing selector_frag."""
    for m in re.finditer(r"([^{}]+)\{([^}]*)\}", css):
        sel, decls = m.group(1), m.group(2)
        if selector_frag in sel:
            hit = re.search(prop + r"\s*:\s*([^;]+)", decls)
            if hit:
                return hit.group(1).strip()
    return None


def var_value(css, name):
    m = re.search(re.escape(name) + r"\s*:\s*([^;]+)", css)
    return m.group(1).strip() if m else None


def px(val, default=None, root=16.0):
    """px, rem and em all resolve to px. rem/em assume the root size."""
    if not val:
        return default
    m = re.search(r"(-?[\d.]+)\s*px", val)
    if m:
        return float(m.group(1))
    m = re.search(r"(-?[\d.]+)\s*r?em", val)
    if m:
        return float(m.group(1)) * root
    return default


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    doc = open(args.html, encoding="utf-8").read()
    css = " ".join(re.findall(r"<style[^>]*>(.*?)</style>", doc, flags=re.S))
    body = re.sub(r"<style[^>]*>.*?</style>", " ", doc, flags=re.S)

    text = visible_text(body)
    words = text.split()
    nwords = len(words)

    hard, soft = [], []

    def check(ok, label, got, want):
        (hard if ok is not None else soft).append(
            {"ok": bool(ok), "label": label, "got": got, "want": want})

    def note(label, got, want=""):
        soft.append({"ok": None, "label": label, "got": got, "want": want})

    # --- length ---
    note("word count", f"{nwords:,}", "~3,000 target")
    note("reading time", f"{nwords/220:.1f} min @220wpm", "under 8 min")

    # --- headings ---
    levels = {n: len(re.findall(rf"<h{n}[\s>]", body)) for n in range(1, 7)}
    used = [n for n, c in levels.items() if c]
    total_h = sum(levels.values())
    check(len(used) <= 3, "heading levels used",
          f"{len(used)} ({','.join('h'+str(n) for n in used)})", "<= 3")
    check(total_h <= 18, "total headings", total_h, "<= 18")

    # --- lists / prose balance ---
    nli = len(re.findall(r"<li[\s>]", body))
    npara = len(re.findall(r"<p[\s>]", body))
    check(nli <= 25, "bullet items", nli, "<= 25")
    check(nli <= npara, "bullets vs paragraphs", f"{nli} li / {npara} p",
          "bullets <= paragraphs")

    # --- emphasis ---
    bold_words = sum(len(visible_text(m).split())
                     for m in re.findall(r"<(?:strong|b)[\s>].*?</(?:strong|b)>",
                                         body, flags=re.S))
    pct = (bold_words / nwords * 100) if nwords else 0
    check(pct <= 30, "bolded text", f"{pct:.1f}%", "<= 30%")

    # --- pull quotes ---
    nquote = len(re.findall(r'class="[^"]*\bquote\b', body))
    check(nquote == 0, "pull quotes", nquote, "0 (use callouts)")

    # --- containers ---
    styles = set()
    for cls in re.findall(r'class="([^"]+)"', body):
        for c in cls.split():
            if re.search(rf"\.{re.escape(c)}\b[^{{}}]*\{{[^}}]*border\s*:", css):
                styles.add(c)
    check(len(styles) <= 3, "bordered container styles",
          f"{len(styles)} ({', '.join(sorted(styles)) or 'none'})", "<= 3")

    # --- measure & rhythm ---
    body_fs = px(css_value(css, "body", "font-size"))
    if body_fs is None:                      # `font: 17px/1.6 <stack>` shorthand
        short = css_value(css, "body", "font")
        m = re.search(r"(-?[\d.]+)px\s*/", short or "")
        body_fs = float(m.group(1)) if m else 16.0
    lh_raw = css_value(css, "body", "line-height") or "1.6"
    lh = px(lh_raw) or (float(re.search(r"[\d.]+", lh_raw).group()) * body_fs)
    maxw = (px(var_value(css, "--maxw"), root=body_fs)
            or px(css_value(css, ".wrap", "max-width"), root=body_fs)
            or px(css_value(css, ".page", "max-width"), root=body_fs))
    prose = px(var_value(css, "--prose"), root=body_fs)
    pad = px(css_value(css, ".wrap", "padding"), 0) or px(css_value(css, ".page", "padding"), 0) or 0
    col = prose if prose else ((maxw - 2 * pad) if maxw else None)
    if col:
        ch = col / (body_fs * 0.5)          # ~0.5em average advance for sans
        check(45 <= ch <= 80, "measure (line length)",
              f"{ch:.0f} char ({col:.0f}px @ {body_fs:.0f}px)", "45-80 char")
    else:
        note("measure", "could not determine", "45-80 char")

    p_mb = px(css_value(css, "p", "margin-bottom")) or px(css_value(css, "p", "margin"))
    if p_mb is not None:
        check(p_mb >= 1.5 * lh, "paragraph spacing",
              f"{p_mb:.0f}px (line-height {lh:.0f}px)", f">= {1.5*lh:.0f}px")

    check(body_fs >= 16, "body font-size", f"{body_fs:.0f}px", ">= 16px")

    # --- contrast ---
    bg = var_value(css, "--bg")
    if bg and bg.startswith("#"):
        for tok, floor, role in (("--ink", 75, "body"), ("--muted", 75, "secondary body"),
                                 ("--faint", 60, "captions"), ("--sub", 75, "secondary body"),
                                 ("--cap", 60, "captions")):
            v = var_value(css, tok)
            if v and v.startswith("#"):
                lc = abs(apca_lc(v, bg))
                check(lc >= floor, f"APCA {tok} on --bg",
                      f"Lc {lc:.0f} ({v})", f">= Lc {floor} ({role})")
        panel = var_value(css, "--panel") or var_value(css, "--surface")
        if panel and panel.startswith("#"):
            r = wcag_ratio(panel, bg)
            check(r >= 1.25, "surface vs background",
                  f"{r:.2f}:1 ({panel} on {bg})", ">= 1.25:1 to read without a border")

    # --- print ---
    has_print = bool(re.search(r"@media\s+print", css))
    light_print = False
    mp = re.search(r"@media\s+print[^{]*\{", css)
    if mp:                                   # walk braces to find the real block end
        i, depth = mp.end(), 1
        while i < len(css) and depth:
            depth += 1 if css[i] == "{" else (-1 if css[i] == "}" else 0)
            i += 1
        block = css[mp.end():i]
        m = re.search(r"--bg\s*:\s*(#[0-9a-f]{3,6})", block, flags=re.I)
        light_print = bool(m) and wcag_luminance(m.group(1)) > 0.5
    check(has_print and light_print, "print stylesheet",
          "light" if light_print else ("dark only" if has_print else "none"),
          "light theme for the PDF")

    failures = [c for c in hard if not c["ok"]]

    if args.json:
        print(json.dumps({"words": nwords, "hard": hard, "soft": soft,
                          "failures": len(failures)}, indent=2))
    else:
        print(f"\n  FIELD STUDY QA  —  {args.html}\n")
        for c in hard:
            print(f"  {'PASS' if c['ok'] else 'FAIL'}  {c['label']:32} "
                  f"{str(c['got']):34} want {c['want']}")
        for c in soft:
            print(f"  NOTE  {c['label']:32} {str(c['got']):34} {c['want']}")
        print(f"\n  {len(hard)-len(failures)}/{len(hard)} budgets met\n")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
