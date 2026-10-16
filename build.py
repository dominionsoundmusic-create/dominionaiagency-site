#!/usr/bin/env python3
"""Build the static Dominion AI Agency site (dominionaiagency.com).

Build system copied from Water Damage Pro Dallas (59b7e0a); every value adapted to this site.
Pages live in src/pages as Jinja templates with a YAML front matter block.
Shared business data (including the ONE copy of the phone number) lives in src/data/site.json.
Output goes to dist/. Folder pages get a trailing-slash URL (/ai-receptionist/); a page may set its own
`url` in front matter (the kept industry URLs such as /ai-for/law-firms.html). The 404 page is /404.html.

Photos (Maurice's reuse rule): docs/photos.json lists every photo the site has (generic photos reused
from Dominion Web Design Pro and Maurice's lead sites, renamed, with new alt text). A page may also name a NEW image that has not
been made yet; docs/image-reuse.json maps that file name to an existing photo, and until the new image
is saved in src/static/images/ the build serves a crop of that existing photo under the new name, with
the existing photo's alt text, so the markup is final and nothing ever shows as broken or empty. Every
such slot is listed in docs/image-list.md with its Artistly prompt.

Usage:
  python3 build.py                 # full build to dist/, also writes docs/image-list.md
  python3 build.py --out DIR       # build somewhere else (no docs written)
"""
import argparse
import html
import json
import re
import shutil
import struct
import sys
from pathlib import Path

import yaml
from jinja2 import ChainableUndefined, Environment, FileSystemLoader, pass_context
from markupsafe import Markup

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
PAGES = SRC / "pages"
STATIC = SRC / "static"
IMAGES = STATIC / "images"
CACHE = ROOT / ".imgcache"  # WebP copies made by the build (git-ignored; rebuilt if missing)
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
BUILD_DATE = "2026-10-15"
OG_DEFAULT = "shop-owner-phone-call-notes-hero.jpg"
PENDING = CACHE / "pending"  # stand-in crops of existing photos for planned images not made yet
PHOTOS = json.loads((ROOT / "docs" / "photos.json").read_text())
REUSE = {k: v for k, v in json.loads((ROOT / "docs" / "image-reuse.json").read_text()).items() if not k.startswith("_")}


def image_size(path):
    """Return (width, height) for a JPEG/PNG/WebP file, or None."""
    data = path.read_bytes()
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", data[16:24])
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        if data[12:16] == b"VP8X":
            w = int.from_bytes(data[24:27], "little") + 1
            h = int.from_bytes(data[27:30], "little") + 1
            return w, h
        return None
    if data[:2] == b"\xff\xd8":
        i = 2
        while i < len(data):
            marker = data[i + 1]
            length = struct.unpack(">H", data[i + 2:i + 4])[0]
            if marker in (0xC0, 0xC1, 0xC2):
                h, w = struct.unpack(">HH", data[i + 5:i + 9])
                return w, h
            i += 2 + length
    return None


def make_placeholder(file, width, height):
    """Stand-in for a planned image that is not made yet: a crop of the existing photo docs/image-reuse.json
    names for it, at the planned size (cached in .imgcache/pending/). Never a blank or brand-color block."""
    if file not in REUSE:
        raise SystemExit(f"{file}: planned image has no stand-in photo in docs/image-reuse.json")
    src = IMAGES / REUSE[file]["from"]
    out = PENDING / file
    if out.exists() and image_size(out) == (width, height) and out.stat().st_mtime >= src.stat().st_mtime:
        return out
    from PIL import Image
    out.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(src).convert("RGB")
    sc = max(width / im.width, height / im.height)
    im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    left, top = (im.width - width) // 2, (im.height - height) // 2
    im.crop((left, top, left + width, top + height)).save(out, "JPEG", quality=84, optimize=True)
    return out


def stand_in_alt(file):
    """Alt text for a planned image while its stand-in photo is shown: describe what is really shown."""
    return PHOTOS[REUSE[file]["from"]]["alt"]


def url_for_source(rel):
    """src/pages relative path -> public URL path."""
    parts = list(rel.with_suffix("").parts)
    if parts == ["index"]:
        return "/"
    if parts == ["404"]:
        return "/404.html"
    if parts[-1] == "index":
        parts = parts[:-1]
    return "/" + "/".join(parts) + "/"


def out_path_for(url, out):
    if url.endswith(".html"):
        return out / url.lstrip("/")
    if not url.endswith("/"):  # a flat URL such as /page -> dist/page.html
        return out / (url.lstrip("/") + ".html")
    return out / url.strip("/") / "index.html" if url != "/" else out / "index.html"


TABLE_RE = re.compile(r"<table>(.*?)</table>", re.S)
SECTION_RE = re.compile(r'<section class="band band--tint([^"]*)"')


def color_breaks(html_text):
    """Marked bands (band--tint in a page source) become bold color breaks between white sections: black
    bands, and the FAQ band is always the gold one (INTAKE.md: white, black band, white, gold band)."""
    def one(m):
        if "faq" in m.group(1).split():
            return '<section class="band band--tint band--gold%s"' % m.group(1)
        return '<section class="band band--tint band--black%s"' % m.group(1)
    return SECTION_RE.sub(one, html_text)


CELL_RE = re.compile(r"<(th|td)\b([^>]*)>", re.S)


def label_table_cells(html_text):
    """Give each body cell a data-label with its column heading, so CSS can stack
    table rows as cards on narrow screens without horizontal scrolling."""
    def one(m):
        body = m.group(1)
        head = re.search(r"<thead>(.*?)</thead>", body, re.S)
        if not head:
            return m.group(0)
        labels = [strip_tags(h) for h in re.findall(r"<th\b[^>]*>(.*?)</th>", head.group(1), re.S)]

        def row(rm):
            i = [0]

            def cell(cm):
                n = i[0]
                i[0] += 1
                if n < len(labels) and labels[n] and "data-label" not in cm.group(2):
                    lab = html.escape(labels[n], quote=True)
                    return f'<{cm.group(1)}{cm.group(2)} data-label="{lab}">'
                return cm.group(0)
            return CELL_RE.sub(cell, rm.group(0))
        tbody = re.sub(r"<tr\b.*?</tr>", row, body[head.end():], flags=re.S)
        return "<table class=\"stack\">" + body[:head.end()] + tbody + "</table>"
    return TABLE_RE.sub(one, html_text)


def strip_tags(text):
    return html.unescape(re.sub(r"<[^>]+>", "", str(text))).strip()


def minify_css(css):
    """Small, safe CSS minifier for inlining: drop comments and collapse whitespace."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};,>])\s*", r"\1", css)
    return css.replace(";}", "}").strip()


class Builder:
    def __init__(self, out, write_docs):
        self.out = out
        self.write_docs = write_docs
        self.site = json.loads((SRC / "data" / "site.json").read_text())
        # The phone number lives once, in business.phone; display and tel forms are derived here.
        # While it is the placeholder PHONE-PENDING, both forms show the placeholder (check.py warns).
        b = self.site["business"]
        digits = re.sub(r"\D", "", b["phone"])
        if b["phone"] == "PHONE-PENDING" or len(digits) not in (10, 11):
            b["phone_display"], b["phone_tel"] = "PHONE-PENDING", "PHONE-PENDING"
        else:
            digits = digits[-10:]
            b["phone_display"] = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
            b["phone_tel"] = "+1" + digits
        self.site["cta"]["primary_label"] = self.site["cta"]["primary_label"].replace(
            "{phone}", self.site["business"]["phone_display"])
        self.missing_images = {}  # filename -> dict
        self._srcset_cache = {}
        self.pending = set()
        self.env = Environment(
            loader=FileSystemLoader([str(SRC / "templates"), str(PAGES)]),
            undefined=ChainableUndefined,
            autoescape=False,
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.env.globals.update(
            site=self.site,
            img=self.img,
            webp_srcset=self.webp_srcset,
            picture=self.picture,
            image_exists=lambda f: bool(f) and (IMAGES / f).exists(),
            img_size=lambda f: image_size(IMAGES / f) or (1200, 750),
            svc=self.find("services"),
            guide=self.find("guides"),
            ind=self.find("industries"),
            inline_css=minify_css((SRC / "static" / "css" / "site.css").read_text()),
        )
        self.env.filters["striptags_plain"] = strip_tags
        self.env.filters["tojson_ld"] = lambda v: Markup(
            json.dumps(v, ensure_ascii=False, indent=1).replace("</", "<\\/")
        )

    def find(self, key):
        items = {i["slug"]: i for i in self.site[key]}

        def get(slug):
            if slug not in items:
                raise KeyError(f"unknown {key} slug: {slug}")
            return items[slug]
        return get

    # ---- images -------------------------------------------------------
    # Phones should not download a 1920px JPEG. For every photo a page uses, the build makes
    # WebP copies at several widths (cached in .imgcache/ so rebuilds are fast) and the page
    # offers them through <picture> + srcset, so each browser fetches only the size it needs.
    # The original JPEG (or its placeholder) stays as the fallback <img src>.
    WEBP_WIDTHS = (480, 800, 1200, 1600, 1920)
    WEBP_QUALITY = 72

    def webp_srcset(self, file):
        """Return a srcset string of WebP copies for `file`, creating them if needed ('' if none)."""
        if not file or not file.lower().endswith((".jpg", ".jpeg", ".png")):
            return ""
        src = self.src_path(file)
        if not src:
            return ""
        if file in self._srcset_cache:
            return self._srcset_cache[file]
        from PIL import Image  # only needed when photos are present
        size = image_size(src)
        if not size:
            return ""
        full_w = size[0]
        widths = sorted({w for w in self.WEBP_WIDTHS if w < full_w} | {full_w})
        stem = Path(file).stem + ("-pending" if src.parent == PENDING else "")
        CACHE.mkdir(exist_ok=True)
        parts, im = [], None
        for w in widths:
            name = f"{stem}-{w}.webp"
            cached = CACHE / name
            if not cached.exists() or cached.stat().st_mtime < src.stat().st_mtime:
                if im is None:
                    im = Image.open(src).convert("RGB")
                h = round(im.height * w / im.width)
                out = im if w == im.width else im.resize((w, h), Image.LANCZOS)
                out.save(cached, "WEBP", quality=self.WEBP_QUALITY, method=6)
            shutil.copy2(cached, self.out / "images" / name)
            parts.append(f"/images/{name} {w}w")
        self._srcset_cache[file] = ", ".join(parts)
        return self._srcset_cache[file]

    def picture(self, file, alt, width, height, sizes, extra=""):
        """<picture> with WebP sources and the JPEG as fallback. `extra` goes on the <img>."""
        img = (f'<img src="/images/{file}" alt="{html.escape(alt, quote=True)}" '
               f'width="{width}" height="{height}"{extra}>')
        srcset = self.webp_srcset(file)
        if not srcset:
            return Markup(img)
        return Markup(f'<picture><source type="image/webp" srcset="{srcset}" sizes="{sizes}">{img}</picture>')

    @pass_context
    def img(self, ctx, file, alt, width, height, desc="", cls="", caption="", lazy=True, note=True):
        """Render an in-body figure with WebP srcset, width, height and lazy loading.

        If `file` does not exist yet it is listed in docs/image-list.md and a crop of its stand-in
        photo (docs/image-reuse.json) is served under the same name and size, with the stand-in's alt.
        """
        page = ctx.get("page", {})
        cap = f"<figcaption>{caption}</figcaption>" if caption else ""
        cls_attr = f' class="fig {cls}"' if cls else ' class="fig"'

        lazy_attr = ' loading="lazy" decoding="async"' if lazy else ""
        fig_sizes = "(max-width: 900px) 100vw, 900px"
        if not (IMAGES / file).exists():
            if note:  # card thumbnails reuse a page's hero file; that page lists it
                self.note_missing(file, width, height, alt, desc, page.get("url", "?"))
            self.ensure_pending(file, width, height)
            alt = stand_in_alt(file)
        w, h = image_size(self.src_path(file)) or (width, height)
        shown = self.picture(file, alt, w, h, fig_sizes, lazy_attr)
        return Markup(f"<figure{cls_attr}>{shown}{cap}</figure>")

    def src_path(self, file):
        """The real photo if it exists, else its placeholder (if one was made), else None."""
        if (IMAGES / file).exists():
            return IMAGES / file
        if (PENDING / file).exists() and file in self.pending:
            return PENDING / file
        return None

    def ensure_pending(self, file, width, height):
        """Make (or reuse) the stand-in for a planned photo and copy it to dist/images/."""
        path = make_placeholder(file, width, height)
        self.pending.add(file)
        dest = self.out / "images" / file
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)

    def note_missing(self, file, width, height, alt, desc, url):
        entry = self.missing_images.setdefault(
            file, {"file": file, "size": f"{width}x{height}", "alt": alt, "desc": desc, "pages": []}
        )
        if url not in entry["pages"]:
            entry["pages"].append(url)
        if desc and not entry["desc"]:
            entry["desc"] = desc

    # ---- pages --------------------------------------------------------
    def load_pages(self):
        pages = []
        for path in sorted(PAGES.rglob("*.html")):
            rel = path.relative_to(PAGES)
            if rel.parts[0].startswith("_"):
                continue
            text = path.read_text()
            m = FM_RE.match(text)
            if not m:
                raise SystemExit(f"{rel}: missing front matter")
            meta = yaml.safe_load(m.group(1)) or {}
            meta["url"] = meta.get("url") or url_for_source(rel)
            meta["source"] = str(rel)
            meta["body"] = text[m.end():]
            pages.append(meta)
        return pages

    def render(self, page, pages):
        layout = page.get("layout", "page")
        hero = page.get("hero")
        if hero:
            want = hero.get("image")
            if want and not (IMAGES / want).exists():
                self.note_missing(want, 1920, 1080, hero.get("alt", ""), hero.get("desc", ""), page["url"])
                self.ensure_pending(want, 1920, 1080)
                hero["pending"] = True
            hero["render_image"] = want
            hero["render_alt"] = stand_in_alt(want) if hero.get("pending") else hero.get("alt", "")
            src = self.src_path(want) if want else None
            size = image_size(src) if src else None
            hero["w"], hero["h"] = size if size else (1920, 1080)
        page.setdefault("breadcrumbs", self.breadcrumbs(page))
        page["jsonld"] = self.jsonld(page)
        source = (
            '{% extends "layouts/' + layout + '.html" %}\n'
            '{% import "macros.html" as m with context %}\n' + page["body"]
        )
        tpl = self.env.from_string(source)
        return label_table_cells(tpl.render(page=page, pages=pages))

    # ---- breadcrumbs + structured data --------------------------------
    def breadcrumbs(self, page):
        url = page["url"]
        if url in ("/", "/404.html") or page.get("noindex"):
            return []
        crumbs = [{"label": "Home", "href": "/"}]
        if page.get("type") == "industry":
            crumbs.append({"label": "Industries", "href": "/ai-for/"})
        if page.get("type") == "service":
            crumbs.append({"label": "Services", "href": "/services/"})
        if page.get("type") == "guide":
            crumbs.append({"label": "Guides", "href": "/what-is-an-ai-agency/"} if page["url"] != "/what-is-an-ai-agency/" else None)
        crumbs = [c for c in crumbs if c]
        crumbs.append({"label": page.get("crumb", page.get("h1", page["title"])), "href": url})
        return crumbs

    def jsonld(self, page):
        b = self.site["business"]
        origin = b["origin"]
        url = origin + page["url"]
        org_id = origin + "/#organization"
        areas = {"@type": "Country", "name": "United States"}
        org = {
            "@type": "Organization",
            "@id": org_id,
            "name": b["name"],
            "legalName": b["legal_name"],
            "url": origin + "/",
            "logo": origin + b["logo"],
            "telephone": b["phone_tel"],
            "email": b["email"],
            "description": b["description"],
            "foundingDate": b["founded"],
            "founder": {"@type": "Person", "name": b["founder"]},
            "parentOrganization": {"@type": "Organization", "name": b["legal_name"]},
            "areaServed": areas,
            "contactPoint": {
                "@type": "ContactPoint",
                "telephone": b["phone_tel"],
                "contactType": "customer service",
                "availableLanguage": ["English"],
                "hoursAvailable": {
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                    "opens": "00:00",
                    "closes": "23:59",
                },
            },
        }
        same_as = [v for v in self.site["social"].values() if v]
        if same_as:
            org["sameAs"] = same_as
        graph = [org]
        if page["url"] == "/":
            graph.append({"@type": "WebSite", "@id": origin + "/#website", "url": origin + "/",
                          "name": b["name"], "publisher": {"@id": org_id}, "inLanguage": "en-US"})
        if page["url"] == "/404.html":
            return {"@context": "https://schema.org", "@graph": graph}
        image = origin + "/images/" + ((page.get("hero") or {}).get("render_image") or OG_DEFAULT)
        webpage = {
            "@type": "WebPage",
            "@id": url + "#webpage",
            "url": url,
            "name": page["title"],
            "description": page["description"],
            "isPartOf": {"@type": "WebSite", "@id": origin + "/#website", "url": origin + "/", "name": b["name"]},
            "about": {"@id": org_id},
            "primaryImageOfPage": {"@type": "ImageObject", "url": image},
            "inLanguage": "en-US",
        }
        if page.get("type") == "contact":
            webpage["@type"] = "ContactPage"
        if page.get("type") == "about":
            webpage["@type"] = "AboutPage"
        graph.append(webpage)
        crumbs = page.get("breadcrumbs") or []
        if crumbs:
            graph.append({
                "@type": "BreadcrumbList",
                "@id": url + "#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": i + 1, "name": c["label"], "item": origin + c["href"]}
                    for i, c in enumerate(crumbs)
                ],
            })
            webpage["breadcrumb"] = {"@id": url + "#breadcrumb"}
        svc = page.get("schema_service")
        if svc:
            service = {
                "@type": "Service",
                "@id": url + "#service",
                "name": svc["name"],
                "serviceType": svc["type"],
                "description": svc.get("description", page["description"]),
                "provider": {"@id": org_id},
                "areaServed": areas,
                "url": url,
            }
            if svc.get("audience"):
                service["audience"] = {"@type": "BusinessAudience", "name": svc["audience"]}
            offers = []
            for o in svc.get("offers") or []:  # only prices from INTAKE.md
                spec = {"@type": "UnitPriceSpecification", "price": str(o["price"]), "priceCurrency": "USD"}
                if o.get("unit"):
                    spec["unitText"] = o["unit"]
                offers.append({"@type": "Offer", "name": o["name"], "priceSpecification": spec,
                               **({"description": o["description"]} if o.get("description") else {})})
            if offers:
                service["offers"] = offers
            graph.append(service)
        if page.get("type") == "guide":
            graph.append({
                "@type": "Article",
                "@id": url + "#article",
                "headline": page["h1"],
                "description": page["description"],
                "image": image,
                "datePublished": str(page.get("published", BUILD_DATE)),
                "dateModified": str(page.get("modified", BUILD_DATE)),
                "author": page.get("author_ld") or {"@id": org_id},
                "publisher": {"@id": org_id},
                "mainEntityOfPage": {"@id": url + "#webpage"},
                "inLanguage": "en-US",
            })
        faqs = page.get("faqs") or []
        if faqs:
            graph.append({
                "@type": "FAQPage",
                "@id": url + "#faq",
                "mainEntity": [
                    {"@type": "Question", "name": strip_tags(f["q"]),
                     "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"\s+", " ", strip_tags(f["a"]))}}
                    for f in faqs
                ],
            })
        return {"@context": "https://schema.org", "@graph": graph}

    def build(self):
        if self.out.exists():
            shutil.rmtree(self.out)
        shutil.copytree(STATIC, self.out)
        pages = self.load_pages()
        index = {p["url"]: p for p in pages}
        # A page's own front matter can supply its card line and county for the shared lists
        # (service, guide and area cards), so each summary is written with the page it describes.
        for key in ("services", "guides", "industries"):
            for item in self.site[key]:
                pg = index.get(item["url"])
                if pg and pg.get("card_summary"):
                    item["summary"] = pg["card_summary"]
        failed = []
        for page in pages:
            try:
                html_out = self.render(page, index)
            except Exception as e:  # report and keep building the other pages
                failed.append(f"{page['source']}: {type(e).__name__}: {e}")
                continue
            dest = out_path_for(page["url"], self.out)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(color_breaks(html_out))
        self.write_sitemap(pages)
        self.write_robots()
        if self.write_docs:
            self.write_image_list()
        print(f"Built {len(pages) - len(failed)} pages into {self.out}")
        for f in failed:
            print("FAILED", f)
        if failed:
            raise SystemExit(1)
        if self.missing_images:
            print(f"{len(self.missing_images)} planned images still to generate (docs/image-list.md)")

    def write_sitemap(self, pages):
        origin = self.site["business"]["origin"]
        urls = [p for p in pages if not p.get("noindex") and p["url"] != "/404.html"]
        lines = ['<?xml version="1.0" encoding="UTF-8"?>',
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for p in sorted(urls, key=lambda p: (p["url"] != "/", p["url"])):
            lines.append(f"  <url><loc>{origin}{p['url']}</loc><lastmod>{BUILD_DATE}</lastmod></url>")
        lines.append("</urlset>")
        (self.out / "sitemap.xml").write_text("\n".join(lines) + "\n")

    def write_robots(self):
        origin = self.site["business"]["origin"]
        (self.out / "robots.txt").write_text(
            "User-agent: *\nAllow: /\n\n"
            f"Sitemap: {origin}/sitemap.xml\n"
        )

    PROMPT_HEAD = "Wide cinematic landscape shot, subject positioned on right third of frame, well lit."
    PROMPT_TAIL = "Bright, clearly visible, realistic photo of an American small business setting, no text, no logos, no screens with readable words, no recognizable faces."

    def artistly_prompt(self, e):
        p = (e["desc"] or e["alt"]).strip()
        if not p.lower().startswith("wide cinematic landscape shot"):
            p = self.PROMPT_HEAD + " " + p
        if "no text" not in p.lower():
            p = p.rstrip(".") + ". " + self.PROMPT_TAIL
        return p

    def write_image_list(self):
        rows = sorted(self.missing_images.values(), key=lambda e: (e["size"] != "1920x1080", e["pages"][0], e["file"]))
        heroes = sum(1 for e in rows if e["size"] == "1920x1080")
        out = [
            "# Images still needed (Artistly)",
            "",
            "Generated by `python3 build.py`. Maurice's rule: reuse first. Every page already uses generic photos reused",
            "from Dominion Web Design Pro and Maurice's lead sites (docs/photos.json). The images below are the",
            "only new ones still wanted. Each one already has its final tag on the page (file name, width, height,",
            "lazy loading in the body, eager loading and a preload for heroes), and until it is saved the build",
            "shows a crop of an existing photo under the same file name (docs/image-reuse.json, column Stand-in),",
            "with that photo's alt text, so nothing is ever broken or empty.",
            "",
            "To add one: generate it from the prompt, save it as a JPEG under the exact file name and size in",
            "`src/static/images/`, give it its alt text in the page source if needed, run `python3 build.py`, commit.",
            "",
            "Style for every image: bright, clearly visible, American small business settings (offices, front desks,",
            "shops, salons, kitchens, job sites), natural daylight, no text, no logos, no watermarks, no screens with",
            "readable words, no recognizable faces. Every prompt starts with: wide cinematic landscape shot, subject",
            "positioned on right third of frame, well lit. Heroes 1920x1080, in-body images 1200x800.",
            "",
            f"Total: {len(rows)} images ({heroes} heroes at 1920x1080 listed first, then {len(rows) - heroes} in-body images at 1200x800).",
            "",
            "| # | File name | Size | Stand-in until it arrives | Pages |",
            "|---:|---|---|---|---|",
        ]
        out += [f"| {n} | {e['file']} | {e['size']} | {REUSE[e['file']]['from']} | {len(e['pages'])} page(s) |"
                for n, e in enumerate(rows, 1)]
        out.append("")
        for n, e in enumerate(rows, 1):
            out += [
                f"## {n}. {e['file']}",
                "",
                f"- File name: `{e['file']}`",
                f"- Size: {e['size']} px",
                f"- Used on: {', '.join(e['pages'])}",
                f"- Alt text once it arrives: {REUSE[e['file']].get('alt') or e['alt']}",
                f"- Artistly prompt: {self.artistly_prompt({'desc': REUSE[e['file']].get('prompt', ''), 'alt': e['alt']})}",
                "",
            ]
        (ROOT / "docs" / "image-list.md").write_text("\n".join(out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "dist"))
    args = ap.parse_args()
    out = Path(args.out).resolve()
    Builder(out, write_docs=(out == ROOT / "dist")).build()


if __name__ == "__main__":
    sys.exit(main())
