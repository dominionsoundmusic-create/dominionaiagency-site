#!/usr/bin/env python3
"""Rule and SEO checks over the built site in dist/ (Dominion AI Agency). Copied from the Water Damage Pro Dallas
build system and adapted to this site's rules (CLAUDE.md, INTAKE.md).

Checks every built page for: invented trust claims and the INTAKE.md words to avoid, setup-time promises, em and en
dashes, competitor names outside the guides, prices that are not INTAKE.md's (guides may cite market prices), the texting
note on every page that mentions texting, forms (only "agency-contact" on /contact/ with its exact fields), referral links
only on /tools/, eyebrow labels, the exact top-bar quote, the footer copyright and credit, the handwritten marker, the
privacy and terms carrier lines; SEO basics (one H1, unique title and description, canonical, JSON-LD validity, 3 to 6
FAQs visible and in FAQPage JSON-LD); link and image integrity; no photo twice on one page; the phone number never typed
into a page source (it lives only in src/data/site.json).

Usage: python3 scripts/check.py [--dist DIR] [--only /ai-receptionist/]
Exit code 1 if any error is found.
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORIGIN = "https://dominionaiagency.com"
SITE = json.loads((ROOT / "src" / "data" / "site.json").read_text())
PHONE = SITE["business"]["phone"]
_d = re.sub(r"\D", "", PHONE)[-10:]
PHONE_TEL = "tel:+1" + _d
MARK = "dwdp:handwritten 2026-10-15"
PHOTOS = json.loads((ROOT / "docs" / "photos.json").read_text())
REUSE = {k: v for k, v in json.loads((ROOT / "docs" / "image-reuse.json").read_text()).items() if not k.startswith("_")}
QUOTE = "I believe the unbelievable, I receive the impossible, because it's doable."
NO_EXTRAS = ("/404.html", "/privacy-policy/", "/terms/")  # no hero, body images or FAQs needed
ALLOWED_PRICES = {"597", "1,097", "1,997", "297", "197", "497", "97"}  # INTAKE.md only
FORM_FIELDS = ["form-name", "bot-field", "name", "business", "email", "phone", "message"]

BANNED = [
    # invented team, staff, clients, results, trust
    r"\bour team\b", r"\bteam of\b", r"\bour (?:engineers?|developers?|staff|employees|experts?|specialists|technicians|reps|agents team)\b",
    r"\bengineers\b", r"\bour clients (?:include|say|love|have seen)", r"\bclients? served\b", r"\bhundreds of (?:clients|businesses)",
    r"\bthousands of (?:clients|businesses)", r"\bcase stud(?:y|ies)\b(?! )", r"\btestimonials?\b", r"\b5[- ]star", r"\bfive[- ]star",
    r"\baward", r"\bcertified (?:partner|agency|experts?)", r"\b(?:official|certified|premier) (?:highlevel |gohighlevel )?partner",
    r"\bHIPAA[- ]compliant\b", r"\blawyer[- ]approved\b",
    # INTAKE.md words to avoid and CLAUDE.md banned phrases
    r"guarantee", r"#1\b", r"\bnumber one\b", r"\bbest in the industry\b", r"\btop[- ]rated\b", r"\bindustry[- ]leading\b",
    r"\bcutting[- ]edge\b", r"\brevolutionary\b", r"\bgame[- ]?changer", r"\bunlock", r"\bsupercharge", r"\bseamless",
    r"\bleverag(?:e|es|ing)\b", r"in today's fast-paced world", r"\bnever miss", r"\b48 hours\b", r"\b7 days\b(?! a week)",
    r"\blive in (?:\d+|one|two|three|a few|days)", r"\bwithin (?:\d+|one|two|24|48) (?:hours?|days?|minutes?)\b", r"\bdouble your",
    r"30-40%", r"\bbattle[- ]tested\b", r"\breplaces? your staff\b", r"\bworks perfectly\b", r"\bnever (?:misses|fails)\b",
    r"\byour trusted partner\b", r"\bone-stop solution\b", r"\blook no further\b", r"\bunmatched excellence\b",
    r"\bwe've got you covered\b", r"\bwe have got you covered\b", r"\bour team of experts\b", r"\bour engineers\b",
    # other builds and numbers
    r"Johnson Plumbing", r"\(469\)", r"\(832\)", r"\(689\)", r"Water Damage Pro", r"DFW Expert Roofers", r"HVAC Pro\b",
]
# Vendor and competitor names: never on service, industry or core pages (CLAUDE.md rule 4). Guides may name products
# only as cited general market information (warning there, so each one gets looked at).
VENDORS = ["RingCentral", "Smith.ai", "Smith AI", "Ruby Receptionists", "Ruby", "Dialpad", "Nextiva", "Rosie", "Goodcall", "Synthflow",
           "Retell", "Vapi", "Bland AI", "Lindy", "Jobber", "Housecall Pro", "Weave", "Upfirst", "Beside", "Zoom Phone", "GoTo",
           "OpenPhone", "Quo", "Aircall", "JustCall", "Allo", "Ooma", "Grasshopper", "AnswerConnect", "PATLive", "Abby Connect",
           "Davinci", "Moneypenny", "Posh", "Dialzara", "My AI Front Desk", "Slang", "Numa", "Clara", "Sona", "Air AI", "Podium",
           "Birdeye", "Tidio", "Intercom", "Drift", "ManyChat", "Zapier", "Make.com", "n8n", "HubSpot", "Salesforce", "Zoho",
           "Keap", "ActiveCampaign", "Calendly", "Acuity", "Square", "Vagaro", "Booksy", "GlossGenius", "OpenTable", "Resy", "Toast",
           "Clio", "MyCase", "Dentrix", "Eaglesoft", "Open Dental", "Housecall", "FieldEdge", "Follow Up Boss", "kvCORE"]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.text = []
        self.skip = 0
        self.h1 = 0
        self.title = ""
        self._in_title = False
        self.meta = {}
        self.links = []
        self.imgs = []
        self.ids = []
        self.canonical = None
        self.jsonld = []
        self._in_ld = False
        self._ld = ""
        self.headings = []
        self._h = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if tag in ("script", "style"):
            self.skip += 1
            if tag == "script" and a.get("type") == "application/ld+json":
                self._in_ld = True
                self._ld = ""
        if tag == "title":
            self._in_title = True
        if tag == "h1":
            self.h1 += 1
        if tag in ("h1", "h2", "h3", "h4"):
            self._h = [tag, ""]
        if tag == "meta":
            k = a.get("name") or a.get("property")
            if k:
                self.meta[k] = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        if tag == "a":
            self.links.append(a.get("href"))
        if tag == "img":
            self.imgs.append(a)

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1
            if self._in_ld:
                self.jsonld.append(self._ld)
                self._in_ld = False
        if tag == "title":
            self._in_title = False
        if self._h and tag == self._h[0]:
            self.headings.append((self._h[0], self._h[1].strip()))
            self._h = None

    def handle_data(self, data):
        if self._in_ld:
            self._ld += data
        if self._in_title:
            self.title += data
        if self._h:
            self._h[1] += data
        if not self.skip:
            self.text.append(data)


def url_of(path, dist):
    rel = path.relative_to(dist).as_posix()
    if rel == "index.html":
        return "/"
    if not rel.endswith("/index.html"):
        return "/" + rel
    return "/" + rel[: -len("index.html")]


def resolve(href, dist):
    href = href.split("#")[0].split("?")[0]
    if not href:
        return True
    if href.startswith(ORIGIN):
        href = href[len(ORIGIN):] or "/"
    p = dist / href.lstrip("/")
    if href.endswith("/"):
        return (p / "index.html").exists()
    # a flat URL (/page) would be served from page.html
    return p.exists() or (dist / (href.lstrip("/") + ".html")).exists()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", default=str(ROOT / "dist"))
    ap.add_argument("--only", default="")
    ap.add_argument("--skip-links", action="store_true", help="ignore links to pages not built yet")
    args = ap.parse_args()
    dist = Path(args.dist).resolve()
    errors, warnings = [], []
    titles, descs = defaultdict(list), defaultdict(list)
    files = sorted(dist.rglob("*.html"))
    sitemap = (dist / "sitemap.xml").read_text() if (dist / "sitemap.xml").exists() else ""
    for f in files:
        url = url_of(f, dist)
        if args.only and not url.startswith(args.only):
            continue
        raw = f.read_text()
        p = PageParser()
        p.feed(raw)
        text = re.sub(r"\s+", " ", " ".join(p.text))
        noindex = 'name="robots" content="noindex' in raw

        def err(msg):
            errors.append(f"{url}: {msg}")

        def warn(msg):
            warnings.append(f"{url}: {msg}")

        # hard copy rules (visible text + title + meta + alt)
        alts = " ".join(im.get("alt", "") for im in p.imgs)
        visible = text + " " + p.title + " " + p.meta.get("description", "") + " " + alts
        for pat in BANNED:
            for mt in re.finditer(pat, visible, re.I):
                ctx = visible[max(0, mt.start() - 50): mt.end() + 50]
                err(f"banned phrase /{pat}/ in: ...{ctx}...")
        if "—" in visible or "–" in visible:
            for mt in re.finditer("[—–]", visible):
                err(f"em/en dash in: ...{visible[max(0, mt.start()-40): mt.end()+40]}...")
        is_guide = 'class="type-guide"' in raw
        for v in VENDORS:
            if re.search(r"(?<![\w.])" + re.escape(v) + r"(?![\w])", visible):
                (warn if is_guide else err)(f"vendor/competitor name '{v}' (only in guides, cited)")
        body_m = re.search(r'<div class="page-content"[^>]*>(.*)</main>', raw, re.S)
        body_raw = body_m.group(1) if body_m else raw
        body_txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", " ", body_raw)))
        for mt in re.finditer(r"\$\s?([\d,]+(?:\.\d+)?)", body_txt + " " + p.title + " " + p.meta.get("description", "")):
            amt = mt.group(1).rstrip(",")
            if amt not in ALLOWED_PRICES and not is_guide:
                err(f"price ${amt} is not an INTAKE.md price: ...{body_txt[max(0, mt.start()-60): mt.end()+40]}...")
        if not is_guide and re.search(r"\d+(?:\.\d+)?\s?(?:%|percent)", body_txt):
            for mt in re.finditer(r"[^.]*\d+(?:\.\d+)?\s?(?:%|percent)[^.]*", body_txt):
                warn(f"statistic on a non-guide page (must be cited in Sources): {mt.group(0).strip()[:140]}")
        # texting: every page that talks about texting carries the note in its own body
        if re.search(r"\b(?:SMS|text messag|texting|text back|texts?\b|texted|text reminders?)", body_txt, re.I) and url not in NO_EXTRAS:
            if "Texting is not live yet" not in body_txt and "texting is not live yet" not in body_txt.lower():
                err("mentions texting but the body has no 'Texting is not live yet' note")
        # forms: only the agency-contact form, only on /contact/
        forms = re.findall(r"<form\b[^>]*>", raw)
        if forms and url != "/contact/":
            err(f"form found outside /contact/: {forms}")
        if url == "/contact/":
            if len(forms) != 1 or 'name="agency-contact"' not in forms[0] or 'data-netlify="true"' not in forms[0]:
                err(f"/contact/ must have exactly one Netlify form named agency-contact: {forms}")
            names = re.findall(r'<(?:input|textarea|select)\b[^>]*\bname="([^"]+)"', raw)
            if names != FORM_FIELDS:
                err(f"agency-contact fields {names} != {FORM_FIELDS}")
            if re.search(r'type="checkbox"', raw):
                err("no checkbox (no SMS consent box) on the contact form")
        # referral links only on /tools/
        if url != "/tools/" and re.search(r"gohighlevel\.com/\?fp_ref|servicetitan\.com/", raw):
            err("referral link outside /tools/")
        if url == "/tools/" and "referral link" not in visible.lower():
            err("/tools/ is missing its referral disclosure")
        if re.search(r'class="[^"]*(?:eyebrow|kicker|overline|badge)', raw):
            err("eyebrow/badge label found")
        if QUOTE not in raw.replace("&#39;", "'").replace("&rsquo;", "'"):
            err("top-bar quote missing or not exact")
        if "Jesse Duplantis" not in raw or "John 3:16" not in raw:
            err("quote credit or John 3:16 missing")
        if "© 2026 Dominion Digital Group. All rights reserved." not in raw or 'href="https://dominionwebdesignpro.com"' not in raw:
            err("footer copyright or credit missing")
        if re.search(r'href="https://dominionwebdesignpro.com"[^>]*rel="[^"]*nofollow', raw):
            err("the Dominion Web Design Pro credit must be a followed link")
        if url != "/404.html" and "Texting is not live yet" not in raw:
            err("texting note missing from the footer")
        if MARK not in raw[:4096]:
            err("dwdp:handwritten marker missing from the first 4KB")
        if "lorem" in visible.lower() or "TODO" in visible or "PHONE_" in raw or "XXX" in visible or "[PASTE" in visible:
            err("placeholder text")
        if "PHONE-PENDING" in raw:
            err("PHONE-PENDING placeholder left in a page")
        if url == "/privacy-policy/" and "No mobile information will be shared with third parties/affiliates for marketing or promotional purposes." not in visible:
            err("privacy policy is missing the carrier sentence word for word")
        if url == "/terms/" and not re.search(r"reply\s+STOP", visible, re.I):
            err("terms are missing the reply STOP opt-out")
        if 'googletagmanager.com/gtag/js?id=G-ZBZQPMRDEW' not in raw:
            err("GA4 tag missing")

        # SEO basics
        if p.h1 != 1:
            err(f"expected exactly one h1, found {p.h1}")
        if not p.title.strip():
            err("missing title")
        if len(p.title) > 70:
            warn(f"title is {len(p.title)} chars: {p.title}")
        d = p.meta.get("description", "")
        if not d:
            err("missing meta description")
        elif not (110 <= len(d) <= 170):
            warn(f"meta description is {len(d)} chars")
        titles[p.title].append(url)
        descs[d].append(url)
        if url != "/404.html" and not noindex:
            if p.canonical != ORIGIN + url:
                err(f"canonical {p.canonical} != {ORIGIN + url}")
            if f"<loc>{ORIGIN}{url}</loc>" not in sitemap:
                err("indexable page missing from sitemap.xml")
        if noindex and f"<loc>{ORIGIN}{url}</loc>" in sitemap:
            err("noindex page listed in sitemap")
        # images: hero plus at least two in-body figures on every content page
        figs = raw.count('<figure class="fig')
        has_hero = '<section class="hero ' in raw
        if url not in NO_EXTRAS and (not has_hero or figs < 2):
            err(f"needs a hero and at least two in-body images (hero={has_hero}, body images={figs})")
        for k in ("og:title", "og:description", "og:url", "og:image"):
            if not p.meta.get(k):
                err(f"missing {k}")
        if p.meta.get("og:image") and not p.meta["og:image"].startswith("https://"):
            err("og:image not absolute")
        # JSON-LD
        if len(p.jsonld) > 1:
            err("more than one JSON-LD block")
        faq_count = 0
        for block in p.jsonld:
            try:
                data = json.loads(block)
            except json.JSONDecodeError as e:
                err(f"invalid JSON-LD: {e}")
                continue
            types = [g.get("@type") for g in data.get("@graph", [])]
            if len(types) != len(set(types)):
                err(f"duplicate JSON-LD types: {types}")
            for g in data.get("@graph", []):
                if g.get("@type") == "FAQPage":
                    faq_count = len(g["mainEntity"])
        visible_faq = raw.count('class="faq__item"')
        if visible_faq != faq_count:
            err(f"visible FAQ items ({visible_faq}) != FAQPage entries ({faq_count})")
        max_faq = 6
        if url not in NO_EXTRAS:
            if not (3 <= visible_faq <= max_faq):
                err(f"page needs 3 to 6 common questions, has {visible_faq}")
            if 'id="faq-title">' not in raw:
                err("visible FAQ block missing")
            if faq_count == 0:
                err("FAQPage JSON-LD missing")
        # headings order
        last = 1
        for tag, label in p.headings:
            lvl = int(tag[1])
            if lvl > last + 1:
                warn(f"heading jumps from h{last} to {tag}: {label[:50]}")
            last = lvl
        # links and images
        for href in p.links:
            if href is None or href.strip() in ("", "#"):
                err("empty href")
                continue
            if href.startswith(("tel:", "mailto:", "http://", "https://")) and not href.startswith(ORIGIN):
                if href.startswith("tel:") and href != PHONE_TEL:
                    err(f"unexpected phone link {href}")
                continue
            if not resolve(href, dist):
                if not args.skip_links:
                    err(f"broken internal link {href}")
            elif href.startswith("/") and not href.split("#")[0].endswith(("/", ".html", ".xml", ".txt", ".svg", ".jpg", ".png", ".pdf")) \
                    and not (dist / (href.split("#")[0].lstrip("/") + ".html")).exists():
                warn(f"internal link without trailing slash {href}")
        if url not in ("/404.html",):
            for m_img in re.finditer(r'<figure class="fig[^"]*">(?:<picture>.*?</source>?)?.*?<img ([^>]*)>', raw, re.S):
                if 'loading="lazy"' not in m_img.group(1):
                    err("in-body figure image without loading=lazy")
        for im in p.imgs:
            src = im.get("src", "")
            if not im.get("alt") and im.get("alt") != "":
                err(f"img missing alt: {src}")
            if not im.get("width") or not im.get("height"):
                err(f"img missing width/height: {src}")
            if src.startswith("/") and not (dist / src.lstrip("/")).exists():
                err(f"missing image file {src}")
        # one photo, one appearance per page (CLAUDE.md photos rule 3)
        seen_groups = {}
        for im in p.imgs:
            f = im.get("src", "").rsplit("/", 1)[-1]
            if not f.endswith(".jpg"):
                continue
            src = f
            if f in REUSE and not (ROOT / "src" / "static" / "images" / f).exists():
                src = REUSE[f]["from"]
            g = PHOTOS.get(src, {}).get("group")
            if g is None:
                err(f"image {f} is not in docs/photos.json or docs/image-reuse.json")
                continue
            if g in seen_groups:
                err(f"same photo shown twice on the page: {seen_groups[g]} and {f}")
            seen_groups[g] = f
        dup_ids = {i for i in p.ids if p.ids.count(i) > 1}
        if dup_ids:
            err(f"duplicate ids: {sorted(dup_ids)}")
        words = len(text.split())
        body_type = re.search(r'<body class="type-([a-z]+)', raw)
        if body_type and body_type.group(1) in ("service", "guide", "industry") and words < 1700:
            warn(f"only {words} words on page (including template)")

    for t, urls in titles.items():
        if len(urls) > 1:
            errors.append(f"duplicate title '{t}' on {urls}")
    for d, urls in descs.items():
        if len(urls) > 1 and d:
            errors.append(f"duplicate description on {urls}")

    # _redirects: every target must exist, and no rule may shadow a real page
    red = dist / "_redirects"
    if args.skip_links:
        pass
    elif red.exists():
        for line in red.read_text().splitlines():
            parts = line.split()
            if not parts or parts[0].startswith("#"):
                continue
            src, dst = parts[0], parts[1]
            if not resolve(dst, dist):
                errors.append(f"_redirects: target {dst} does not exist (from {src})")
            if "*" not in src and src != "/" and resolve(src, dist) and not src.endswith(".html"):
                errors.append(f"_redirects: rule {src} shadows a real page")
            # Netlify serves an existing file before applying a rule that has no "!" (force), so a
            # wildcard never hides a real page; a forced rule would.
            if len(parts) > 2 and parts[2].endswith("!"):
                errors.append(f"_redirects: forced rule {src} would hide real pages")
    else:
        errors.append("dist/_redirects missing")
    # the phone number lives only in src/data/site.json
    for src in sorted((ROOT / "src" / "pages").rglob("*.html")) + sorted((ROOT / "src" / "templates").rglob("*.html")):
        t = src.read_text()
        if re.search(r"636[-. ]?7511|6367511", t):
            errors.append(f"{src.relative_to(ROOT)}: phone number typed into a page (use site.business.phone_display / phone_tel)")
    errors = list(dict.fromkeys(errors))
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"\n{len(files)} pages checked, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
