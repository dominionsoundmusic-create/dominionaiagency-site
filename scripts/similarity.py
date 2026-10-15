#!/usr/bin/env python3
"""Duplicate-content check: Jaccard similarity on 5-word shingles between built pages.

Text compared: the page's own copy (hero H1 and lead, the content block and its FAQ). Shared template parts that are
the same on every page by design (header, footer, call band, breadcrumbs, the texting note, the call box, link pills,
cards, price tables, sources) are removed first.

CLAUDE.md rule 12: every pair of pages here must stay at or under 15%, and every page here against every page of the
sister brands AI Voice Agent Pros (dominionsoundmusic-create/aivoiceagentpros-site) and Dominion Web Design Pro
(dominionsoundmusic-create/dominionwebdesignpro-site, dist/) must stay at or under 15%. Shared runs of 8 or more words with
a sister site are also reported. Sister repos are read-only clones next to this repo; add more with --other.

Usage:
  python3 scripts/similarity.py [--dist dist] [--other DIR] [--only /ai-receptionist/] [--limit 0.15] [--report docs/qa-similarity.md]
Exit code 1 if any pair is above the limit.
"""
import argparse
import html
import itertools
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SISTERS = [ROOT.parent / "dominionsoundmusic-create" / "aivoiceagentpros-site",
           ROOT.parent / "dominionsoundmusic-create" / "dominionwebdesignpro-site" / "dist"]
DROP = [r'<div class="note note--texting">.*?</div>', r'<div class="note note--gold">.*?</div>',
        r'<aside class="sources".*?</aside>', r'<ul class="pill-list">.*?</ul>', r'<div class="price-grid">.*?</div>\s*</div>\s*</div>\s*</div>',
        r'<script.*?</script>', r'<style.*?</style>', r'<!--.*?-->', r'<figure.*?</figure>', r'<table.*?</table>', r'<select.*?</select>',
        r'<p class="demo-link">.*?</p>']


def page_text(raw):
    m = re.search(r'<div class="page-content"[^>]*>(.*)</main>', raw, re.S)
    if m:
        hero = re.search(r'<h1>(.*?)</h1>\s*<p class="hero__lead">(.*?)</p>', raw, re.S)
        body = (hero.group(1) + " " + hero.group(2) + " " if hero else "") + m.group(1)
    else:  # a sister site built another way: drop header, nav and footer
        body = re.sub(r"(?s)<header.*?</header>|<nav.*?</nav>|<footer.*?</footer>", " ", raw)
        b = re.search(r"(?s)<body[^>]*>(.*)</body>", body)
        body = b.group(1) if b else body
    body = re.sub(r'<section class="band band--black cta".*?</section>', " ", body, flags=re.S)
    body = re.sub(r'<h2[^>]*>[^<]*</h2>\s*(?=<ul class="pill-list">)', " ", body)
    body = re.sub(r'<h2 id="faq-title">[^<]*</h2>', " ", body)
    for pat in DROP:
        body = re.sub(pat, " ", body, flags=re.S)
    body = re.sub(r'<div class="cards">.*?(?=<section|</section>)', " ", body, flags=re.S)
    txt = html.unescape(re.sub(r"<[^>]+>", " ", body)).lower()
    txt = re.sub(r"(dominion ai agency|ai voice agent pros|dominion web design pro)", "the brand", txt)
    txt = re.sub(r"\(\d{3}\) \d{3}-\d{4}", "phone", txt)
    return re.findall(r"[a-z0-9']+", txt)


def shingles(words, n=5):
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def url_of(path, dist):
    rel = path.relative_to(dist).as_posix()
    if rel == "index.html":
        return "/"
    return "/" + rel[:-len("index.html")] if rel.endswith("/index.html") else "/" + rel


def kind(raw):
    m = re.search(r'<body class="type-([a-z]+)', raw)
    return m.group(1) if m else "page"


def load(dist):
    pages = {}
    for f in sorted(dist.rglob("*.html")):
        raw = f.read_text()
        if 'name="robots" content="noindex' in raw:
            continue
        words = page_text(raw)
        if len(words) < 40:  # redirect stubs and empty shells
            continue
        pages[url_of(f, dist)] = (kind(raw), words, shingles(words))
    return pages


# 8-word runs that are only proper names or carrier wording cannot be reworded.
NAMES = ("dominion digital group", "all rights reserved", "no mobile information will be shared", "a2p 10dlc",
         "telephone consumer protection act", "federal communications commission", "bureau of labor statistics",
         "health insurance portability and accountability act",
         # the legal d/b/a line and carrier-required SMS wording (CTIA / A2P registration) are the same on every Dominion site by design
         "d b a of dominion", "is a d b a of", "the brand is a d b a", "mobile information will be shared with third parties",
         "shared with third parties or affiliates for", "third parties or affiliates for marketing", "affiliates for marketing or promotional purposes",
         "originator opt in data and consent", "not liable for delayed or undelivered messages", "carriers are not liable for delayed",
         "message and data rates may apply", "message frequency varies", "information will be shared with third parties", "will be shared with third parties or")


def runs8(words):
    return {g for g in shingles(words, 8) if not any(n in g for n in NAMES)}


def jac(a, b):
    return len(a & b) / len(a | b) if a and b else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", default=str(ROOT / "dist"))
    ap.add_argument("--other", action="append", default=[])
    ap.add_argument("--only", default="")
    ap.add_argument("--limit", type=float, default=0.15)
    ap.add_argument("--report", default="")
    args = ap.parse_args()
    for other in SISTERS:
        if other.exists() and str(other) not in [str(Path(o).resolve()) for o in args.other]:
            args.other.insert(0, str(other))
    pages = load(Path(args.dist))
    fails, rows = [], []
    for (u1, (k1, w1, s1)), (u2, (k2, w2, s2)) in itertools.combinations(pages.items(), 2):
        if args.only and args.only not in (u1, u2):
            continue
        j = jac(s1, s2)
        rows.append((j, u1, u2, k1, k2))
        if j > args.limit:  # CLAUDE.md: every pair of pages here
            fails.append(f"pair above {args.limit:.0%}: {u1} vs {u2} = {j:.1%}")
    rows.sort(reverse=True)
    by_group = {}
    for j, u1, u2, k1, k2 in rows:
        g = k1 if k1 == k2 else "mixed"
        by_group.setdefault(g, []).append(j)
    print("Page pairs (Jaccard, 5-word shingles):")
    for g, js in sorted(by_group.items()):
        print(f"  {g:8s} pairs={len(js):4d} max={max(js):.1%} mean={sum(js)/len(js):.1%} min={min(js):.1%}")
    print("Top 10 pairs:")
    for j, u1, u2, k1, k2 in rows[:10]:
        print(f"  {j:.1%}  {u1}  {u2}")
    other_fail = []
    for other in args.other:
        dpages = load(Path(other))
        worst = []
        for u, (k, w, s) in pages.items():
            if args.only and u != args.only:
                continue
            s8 = runs8(w)
            for du, (dk, dw, ds) in dpages.items():
                j = jac(s, ds)
                shared8 = s8 & runs8(dw)
                worst.append((j, len(shared8), u, du, sorted(shared8)[:3]))
                if j > args.limit:
                    other_fail.append(f"above {args.limit:.0%} against {other} {du}: {u} = {j:.1%}")
                if shared8:
                    other_fail.append(f"shares {len(shared8)} 8-word run(s) with {other} {du}: {u}: {sorted(shared8)[:3]}")
        worst.sort(reverse=True)
        if not worst:
            print(f"Against {other}: no page matched --only {args.only}")
            continue
        print(f"Against {other} ({len(dpages)} pages): max Jaccard {worst[0][0]:.1%} ({worst[0][2]} vs {worst[0][3]}); "
              f"pages sharing an 8-word run: {len({d.split(': ')[1] for d in other_fail}) if other_fail else 0}")
    for f in fails + other_fail:
        print("FAIL", f)
    if args.report:
        out = ["| Group | Pairs | Max | Mean | Min |", "|---|---:|---:|---:|---:|"]
        for g, js in sorted(by_group.items()):
            out.append(f"| {g} | {len(js)} | {max(js):.1%} | {sum(js)/len(js):.1%} | {min(js):.1%} |")
        out += ["", "Top 15 pairs:", "", "| Jaccard | Page | Page |", "|---:|---|---|"]
        out += [f"| {j:.1%} | {u1} | {u2} |" for j, u1, u2, k1, k2 in rows[:15]]
        Path(args.report).write_text("\n".join(out) + "\n")
    return 1 if fails or other_fail else 0


if __name__ == "__main__":
    sys.exit(main())
