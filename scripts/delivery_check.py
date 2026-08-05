#!/usr/bin/env python3
"""The delivery backstop. Exit 0 or the run has not delivered.

The DELIVERY GATE in Phase 8 is enforced here in code, not just in prose:

  1. The draft of record was READ BACK (list_drafts, DRAFT_VIEW_FULL) and its
     JSON saved to a file. This script verifies that read-back mechanically:
     body present, paragraph breaks intact, no raw markup or base64 blobs,
     recipients and subject present.
  2. Every deliverable link is commit-pinned (a full 40-hex SHA, never a
     branch name), the path EXISTS at that SHA (git cat-file), and the SHA is
     reachable from a pushed remote ref, so the link cannot rot.
  3. Every expected link actually appears in the draft body (Gmail's
     google.com/url?q= rewrapping is unwrapped first, it is normal), in BOTH
     bodies, and inside an href in the HTML rather than as bare text.
  4. The HTML body, which the connector cannot give back, is verified from the
     payload the run passed to create_draft and tied to the draft by its
     plaintext. See resolve_html for why that is the only honest route.

Usage:
  python scripts/delivery_check.py \
    --readback out/<date>/draft_readback.json \
    --payload out/<date>/draft_payload.json \
    [--draft-id r123...] \
    --link https://github.com/<owner>/<repo>/tree/<sha>/runs/<date>/<slug> \
    --link https://github.com/<owner>/<repo>/blob/<sha>/runs/<date>/<slug>/field-study.html \
    ...

--readback accepts either the raw list_drafts response ({"drafts":[...]}) or a
single draft object. With --draft-id the matching draft is checked and its
absence is a failure. Prints PASS or every failure found, and exits non-zero on
any failure. The run may not record itself delivered unless this exits 0.
"""
import argparse
import json
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request

GH_LINK = re.compile(
    r"https://github\.com/([^/\s]+)/([^/\s]+)/(blob|tree)/([^/\s]+)(?:/([^\s?#]*))?"
)


def unwrap_gmail_links(text):
    return re.sub(
        r"https://www\.google\.com/url\?q=([^&\s]+)\S*",
        lambda m: urllib.parse.unquote(m.group(1)),
        text,
    )


def git(args, cwd):
    return subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True)


def check_github_link(url, repo_dir, failures):
    m = GH_LINK.match(url)
    if not m:
        return  # not a repo artifact link, presence-in-body is checked separately
    _, _, kind, ref, path = m.groups()
    path = (path or "").rstrip("/")
    if not re.fullmatch(r"[0-9a-f]{40}", ref):
        failures.append(f"link not commit-pinned (ref '{ref}' is not a 40-hex sha): {url}")
        return
    if path:
        if git(["cat-file", "-e", f"{ref}:{path}"], repo_dir).returncode != 0:
            failures.append(f"path does not exist at pinned sha: {ref}:{path}")
    elif git(["cat-file", "-e", f"{ref}^{{commit}}"], repo_dir).returncode != 0:
        failures.append(f"pinned sha does not exist locally: {ref}")
    contained = git(["branch", "-r", "--contains", ref], repo_dir)
    if contained.returncode != 0 or not contained.stdout.strip():
        failures.append(f"pinned sha not reachable from any pushed remote ref: {ref}")


def check_live_link(url, failures, tries=6, wait=20):
    """The hosted study must actually serve. Retries absorb Pages deploy lag."""
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "alaska-ai-delivery-check"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                body = resp.read(4096).decode("utf-8", "replace")
                if resp.status == 200 and len(body) > 500:
                    return
                last = f"status {resp.status}, {len(body)} bytes"
        except Exception as e:  # noqa: BLE001
            last = str(e)
        if attempt < tries - 1:
            time.sleep(wait)
    failures.append(f"live link not serving after {tries} tries ({last}): {url}")


def norm_text(s):
    """Comparable plaintext: links unwrapped, whitespace flattened."""
    return re.sub(r"\s+", " ", unwrap_gmail_links((s or "").replace("\r\n", "\n"))).strip()


def resolve_html(draft, payload, failures, notes):
    """Get the HTML body, from wherever it can honestly be obtained.

    THE CONNECTOR CANNOT GIVE IT BACK. list_drafts with DRAFT_VIEW_FULL returns
    plaintextBody and never htmlBody, and get_thread (which does document
    htmlBody) is denied by this connector's scopes. Verified against the real
    mailbox: the sibling carousel routine creates html-only drafts and they come
    back from list_drafts with no body field at all, which is only possible if
    htmlBody is never returned.

    So requiring htmlBody in the read-back is a check that no run can ever pass,
    and a gate nobody can satisfy gets deleted or bypassed. The HTML is instead
    verified from the PAYLOAD the run passed to create_draft, and the payload is
    tied to the draft by checking its plaintext really is the plaintext that
    came back. Without that tie, validating the payload proves nothing about the
    draft that actually exists, which would be theatre rather than a gate.
    """
    if (draft.get("htmlBody") or "").strip():
        notes.append("htmlBody came back in the read-back, verified directly")
        return draft["htmlBody"]

    if payload is None:
        failures.append(
            "no htmlBody anywhere. The Gmail read-back cannot return one, so "
            "pass --payload out/<date>/draft_payload.json, the exact object "
            "given to create_draft. The body the prospect reads is not "
            "verified without it.")
        return None

    html = payload.get("htmlBody") or payload.get("html_body") or ""
    if not html.strip():
        failures.append("the create_draft payload carries no htmlBody. CLAUDE.md "
                        "requires BOTH bodies on every draft, and Gmail will "
                        "render the plaintext alternative for everyone else.")
        return None

    # THE TIE. The payload must be the one that became this draft.
    pb, rb = norm_text(payload.get("body") or payload.get("plaintextBody")), \
        norm_text(draft.get("plaintextBody"))
    if not pb:
        failures.append("the payload has no plaintext body, so it cannot be tied "
                        "to the draft that came back")
        return None
    missing = [ln for ln in (l.strip() for l in re.split(r"(?<=[.!?])\s+", pb))
               if len(ln) > 25 and ln not in rb]
    if missing:
        failures.append(
            "the --payload is NOT the draft that came back, so its htmlBody says "
            "nothing about what was created. Sentence absent from the read-back: "
            f"{missing[0][:110]!r}")
        return None
    notes.append("payload tied to the read-back by its plaintext, htmlBody "
                 "verified from the payload")
    return html


def check_html_body(draft, links, failures, payload=None, notes=None):
    """The HTML body is what the prospect actually sees. Verify it, or say so.

    This gate read only plaintextBody for its whole life, so the body Gmail
    renders was never checked once while it printed DELIVERY CHECK PASSED.
    """
    notes = notes if notes is not None else []
    html = resolve_html(draft, payload, failures, notes)
    if html is None:
        return

    if not re.search(r"<(p|br|div)\b", html, re.I):
        failures.append("htmlBody has no paragraph markup, it will render as one run-on block")
    if re.search(r"[A-Za-z0-9+/=]{300,}", html):
        failures.append("htmlBody contains a raw base64-looking blob, an attachment leaked into it")
    if re.search(r"&lt;(p|a|br|div)\b", html, re.I):
        failures.append("htmlBody has escaped tags (&lt;p&gt;), the markup will show as literal text")

    unwrapped = unwrap_gmail_links(html)
    for link in links:
        if link not in unwrapped:
            failures.append(f"expected link missing from htmlBody: {link}")
        elif not re.search(r'href=["\']' + re.escape(link), unwrapped):
            failures.append(
                f"link appears in htmlBody as text but not inside an href, so it "
                f"is not clickable: {link}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--readback", required=True)
    ap.add_argument("--draft-id")
    ap.add_argument("--link", action="append", default=[])
    ap.add_argument("--live-link", action="append", default=[])
    ap.add_argument("--repo-dir", default=".")
    ap.add_argument("--min-paragraphs", type=int, default=2)
    ap.add_argument("--payload", help="the exact object passed to create_draft; the "
                    "Gmail read-back cannot return htmlBody, so the HTML is "
                    "verified from here and tied to the draft by its plaintext")
    args = ap.parse_args()

    failures = []
    notes = []

    payload = None
    if args.payload:
        with open(args.payload) as f:
            payload = json.load(f)

    with open(args.readback) as f:
        data = json.load(f)
    drafts = data.get("drafts", [data]) if isinstance(data, dict) else data
    draft = None
    if args.draft_id:
        draft = next((d for d in drafts if d.get("id") == args.draft_id), None)
        if draft is None:
            failures.append(f"draft of record {args.draft_id} not found in read-back")
    elif drafts:
        draft = drafts[0]
    else:
        failures.append("read-back contains no drafts")

    # EVERY deliverable link, whichever flag carried it. --live-link used to be
    # checked only for serving and never for presence in the body, which meant
    # the one thing the prospect is supposed to click was exempt from the check
    # that it is actually in the email. The study now ships as ONE live link, so
    # that exemption covered the entire deliverable.
    all_links = list(args.link) + list(args.live_link)

    if draft is not None:
        body = draft.get("plaintextBody") or ""
        if not body.strip():
            failures.append("plaintext body is empty or missing, the draft did not round-trip")
        else:
            normalized = body.replace("\r\n", "\n")
            if normalized.count("\n\n") < args.min_paragraphs:
                failures.append(
                    f"body has fewer than {args.min_paragraphs} paragraph breaks, spacing collapsed"
                )
            if re.search(r"[A-Za-z0-9+/=]{300,}", body):
                failures.append("body contains a raw base64-looking blob, an attachment leaked into text")
            if re.search(r"<(html|body|div|span|style|head)\b", body, re.I):
                failures.append("plaintext body contains raw HTML markup, it will read as code")
        # `or ""` rather than a get() default: the API returns an explicit null
        # for an unset subject, and a default only applies to a MISSING key, so
        # the old form raised AttributeError and took the whole gate down.
        if not (draft.get("subject") or "").strip():
            failures.append("subject is empty")
        if not draft.get("toRecipients"):
            failures.append("no recipients on the draft")
        unwrapped = unwrap_gmail_links(body)
        for link in all_links:
            if link not in unwrapped:
                failures.append(f"expected link missing from plaintext body: {link}")

        check_html_body(draft, all_links, failures, payload, notes)

    for link in args.link:
        check_github_link(link, args.repo_dir, failures)

    for link in args.live_link:
        check_live_link(link, failures)

    for n in notes:
        print(f"  ok  {n}")
    if failures:
        print("DELIVERY CHECK FAILED")
        for f_ in failures:
            print(f"  - {f_}")
        sys.exit(1)
    print("DELIVERY CHECK PASSED")


if __name__ == "__main__":
    main()
