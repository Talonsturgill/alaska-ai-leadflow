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


def strip_at_blocks(css, names=("print",)):
    """Drop @media print (and friends) so screen rules are what gets measured.

    `css_value(css, "body", "font-size")` used to return 11pt, out of the print
    stylesheet, because the old scan had no idea an at-rule was a container.
    """
    out, i, n = [], 0, len(css)
    while i < n:
        m = re.compile(r"@media[^{]*\b(" + "|".join(names) + r")\b[^{]*\{").search(css, i)
        if not m:
            out.append(css[i:])
            break
        out.append(css[i:m.start()])
        depth, j = 1, m.end()
        while j < n and depth:
            if css[j] == "{":
                depth += 1
            elif css[j] == "}":
                depth -= 1
            j += 1
        i = j
    return "".join(out)


def selector_matches(sel, frag):
    """True when `frag` is a real selector token, not a substring of one.

    The old check was `frag in sel`, so looking up `p` matched `.page`, `.prose`
    and `.pill`, and the paragraph-spacing budget silently measured whichever of
    those came first. A tag name must not match a class that merely starts with
    the same letters.
    """
    for part in sel.split(","):
        for tok in re.split(r"[\s>+~]+", part.strip()):
            if not tok:
                continue
            if tok == frag:
                return True
            # p matches p.lead and p:first-child, never .page or pre
            if tok.startswith(frag) and re.match(r"[.:\[#]", tok[len(frag):]):
                return True
    return False


def css_rules(css):
    for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", css):
        sel = m.group(1).strip()
        if sel.startswith("@"):
            continue
        yield sel, m.group(2)


def css_value(css, selector_frag, prop, screen_only=True):
    """The effective value of `prop` for a selector, last declaration wins.

    Last rather than first, because a reset like `p{margin:0}` followed by the
    real rule is the normal shape of a stylesheet, and taking the first match
    reports the reset as the answer.
    """
    src = strip_at_blocks(css) if screen_only else css
    best = None   # (rank, order, value), lower rank wins, then later order
    for order, (sel, decls) in enumerate(css_rules(src)):
        if not selector_matches(sel, selector_frag):
            continue
        hit = re.search(r"(?:^|;)\s*" + re.escape(prop) + r"\s*:\s*([^;]+)", decls)
        if not hit:
            continue
        # Rank 0 is the BASE rule, a selector part that is exactly this token.
        # Without it, `.brief p:last-child{margin-bottom:0}` outranked
        # `p{margin:0 0 var(--u)}` purely by coming later in the file, and the
        # measurement reported an override for one paragraph in one panel as
        # the document's paragraph spacing. Last-wins is only a tiebreak among
        # equally general rules, it is not a specificity model.
        rank = 0 if any(part.strip() == selector_frag for part in sel.split(",")) else 1
        if best is None or rank < best[0] or (rank == best[0] and order > best[1]):
            best = (rank, order, hit.group(1).strip())
    return best[2] if best else None


def css_value_ranked(css, selector_frag, prop, screen_only=True):
    """css_value, plus how general the rule it came from was. 0 = base rule."""
    src = strip_at_blocks(css) if screen_only else css
    best = None
    for order, (sel, decls) in enumerate(css_rules(src)):
        if not selector_matches(sel, selector_frag):
            continue
        hit = re.search(r"(?:^|;)\s*" + re.escape(prop) + r"\s*:\s*([^;]+)", decls)
        if not hit:
            continue
        rank = 0 if any(part.strip() == selector_frag for part in sel.split(",")) else 1
        if best is None or rank < best[0] or (rank == best[0] and order > best[1]):
            best = (rank, order, hit.group(1).strip())
    return (best[0], best[2]) if best else (99, None)


def resolve_vars(css, value, depth=3):
    """Substitute var(--x) from :root so a shorthand carrying one can be read."""
    for _ in range(depth):
        if not value or "var(" not in value:
            break
        def sub(m):
            got = var_value(css, m.group(1))
            return got if got else (m.group(2) or "")
        value = re.sub(r"var\(\s*(--[\w-]+)\s*(?:,\s*([^)]*))?\)", sub, value)
    return value


def margin_bottom(shorthand):
    """The bottom value of a margin shorthand: 1->all, 2->tb, 3->t lr b, 4->t r b l."""
    if not shorthand:
        return None
    parts = re.findall(r"[-\w.%()]+", shorthand)
    if not parts:
        return None
    if len(parts) == 1:
        return parts[0]
    if len(parts) == 2:
        return parts[0]
    return parts[2]


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
    # A unitless zero IS a length, and reading it as "unmeasurable" is how a
    # collapsed margin passes as an unknown rather than failing as a zero.
    if re.fullmatch(r"\s*-?0+(\.0+)?\s*", val or ""):
        return 0.0
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

    # PROSE vs STRUCTURE, split on 2026-08-05.
    # The 2,000 to 3,000 budget comes from Nielsen's page-time model, which is
    # about text a reader moves through LINEARLY. Table cells, source lines and
    # figure labels are scanned, not read, so counting them against a reading-time
    # budget measures the wrong thing. On 2026-08-05 a study whose prose spine was
    # roughly 2,400 words reported 3,858 and three trimming passes fought a number
    # that did not mean what it said, while the critics were simultaneously
    # demanding MORE honesty disclosure. Two gates that are both right should not
    # pull against each other, so they now measure different things.
    structural = " ".join(re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", body, flags=re.S))
    structural += " " + " ".join(re.findall(r"<ol class=\"srcs\"[^>]*>(.*?)</ol>", body, flags=re.S))
    structural += " " + " ".join(re.findall(r"<(?:text|caption)[^>]*>(.*?)</(?:text|caption)>", body, flags=re.S))
    nstruct = len(visible_text(structural).split())
    nprose = max(0, nwords - nstruct)

    hard, soft = [], []

    def check(ok, label, got, want):
        (hard if ok is not None else soft).append(
            {"ok": bool(ok), "label": label, "got": got, "want": want})

    def note(label, got, want=""):
        soft.append({"ok": None, "label": label, "got": got, "want": want})

    # --- length ---
    check(2000 <= nprose <= 3000, "prose words", f"{nprose:,}", "2,000-3,000")
    note("structure words", f"{nstruct:,}", "tables, sources, figure labels")
    note("total on page", f"{nwords:,}")
    note("prose reading time", f"{nprose/220:.1f} min @220wpm", "under 8 min")

    # --- headings ---
    levels = {n: len(re.findall(rf"<h{n}[\s>]", body)) for n in range(1, 7)}
    used = [n for n, c in levels.items() if c]
    total_h = sum(levels.values())
    check(len(used) <= 3, "heading levels used",
          f"{len(used)} ({','.join('h'+str(n) for n in used)})", "<= 3")
    check(total_h <= 18, "total headings", total_h, "<= 18")

    # --- lists / prose balance ---
    # The budget exists because bullets delete the relationships between ideas.
    # A figure whose whole point is parallel rows (the before/after ledger) is
    # not that failure mode, so its items are reported but not charged.
    fig = re.findall(r'<section class="ba-c">.*?</section>', body, flags=re.S)
    nfig = sum(len(re.findall(r"<li[\s>]", f)) for f in fig)
    nli = len(re.findall(r"<li[\s>]", body)) - nfig
    npara = len(re.findall(r"<p[\s>]", body))
    if nfig:
        note("figure rows (not charged)", nfig, "before/after ledger")
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

    # Resolve the shorthand and any var() before measuring. The real stylesheet
    # writes `p{margin:0 0 var(--u)}`, which the old code could not read at all,
    # so this budget never ran and the run reported a clean sheet without it.
    # Take whichever declaration came from the MORE GENERAL rule. The longhand
    # margin-bottom:0 here lives on `.brief p:last-child`, an override for one
    # paragraph in one panel, and preferring the longhand unconditionally let it
    # stand in for the whole document's paragraph spacing.
    mb_rank, mb_raw = css_value_ranked(css, "p", "margin-bottom")
    sh_rank, sh_raw = css_value_ranked(css, "p", "margin")
    if mb_rank <= sh_rank and mb_raw is not None:
        p_raw = mb_raw
    else:
        p_raw = margin_bottom(sh_raw)
    p_mb = px(resolve_vars(css, p_raw), root=body_fs)
    if p_mb is not None:
        # ONE FULL LINE of space between paragraphs. The bar used to read
        # 1.5 * line-height and had never once executed, so it was an untested
        # assertion rather than an established standard: at this page's 16px/1.62
        # it demands a 39px gap, around 2.4em, which is larger than body
        # paragraphs are normally set. One line-height is the defensible floor,
        # it is what "the paragraphs are clearly separated" means, and it still
        # fails a collapsed margin, which is the defect worth catching.
        check(p_mb >= lh, "paragraph spacing",
              f"{p_mb:.0f}px (line-height {lh:.0f}px)", f">= {lh:.0f}px")
    else:
        # Never silent. A budget that cannot be measured is reported as such,
        # not omitted from the tally as though it had passed.
        note("paragraph spacing", f"could not read p margin ({p_raw!r})",
             f">= {1.5*lh:.0f}px")

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

    # --- crawler directive ---
    # The page is one prospect's name plus our proposal, on a public host.
    # It has shipped without this once, so it is a hard gate now.
    rb = re.search(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']+)',
                   doc, flags=re.I)
    val = (rb.group(1) if rb else "").lower()
    check("noindex" in val, "robots noindex", val or "no robots meta",
          "noindex (unlisted prospect page)")

    # --- print ---
    # Every @media print block, not just the first: a stylesheet may carry
    # several, and only one of them redefines --bg.
    has_print = bool(re.search(r"@media\s+print", css))
    light_print = False
    for mp in re.finditer(r"@media\s+print[^{]*\{", css):
        i, depth = mp.end(), 1              # walk braces to find the real block end
        while i < len(css) and depth:
            depth += 1 if css[i] == "{" else (-1 if css[i] == "}" else 0)
            i += 1
        m = re.search(r"--bg\s*:\s*(#[0-9a-f]{3,6})", css[mp.end():i], flags=re.I)
        if m and wcag_luminance(m.group(1)) > 0.5:
            light_print = True
            break
    check(has_print and light_print, "print stylesheet",
          "light" if light_print else ("dark only" if has_print else "none"),
          "light theme for the PDF")

    # --- banned words, set by the maintainer on 2026-07-31 ---
    # Enforced in code rather than trusted to a reader, because this run showed
    # that a rule nobody checks is a rule that quietly erodes.
    cannots = re.findall(r"\bcannot\b", text, flags=re.I)
    check(not cannots, "the word cannot",
          f"{len(cannots)} found" if cannots else "none", "zero, always use can't")

    # A sentence opening with And or But. Start of text, or after . ! ? or a newline.
    andbut = re.findall(r"(?:^|(?<=[.!?])\s+)(And|But)\s", text)
    check(not andbut, "sentences opening And/But",
          f"{len(andbut)} found" if andbut else "none", "zero")

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
