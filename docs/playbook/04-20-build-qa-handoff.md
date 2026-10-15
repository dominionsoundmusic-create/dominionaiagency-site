# Playbook 2.0, Prompts 4 to 20: build, QA and handoff (Oct 15 2026)

Prompts 1 to 3 are in 01-03-brief-architecture-routes.md. Everything below is on branch `build`; nothing is merged
or deployed (the live site deploys from `main`).

## Phase 2: configuration, brand, navigation (Prompts 4 to 6)
- Business data in src/data/site.json only (name, d/b/a, phone once, email, GA4 G-ZBZQPMRDEW with the phone-tap event,
  prices from INTAKE.md, nav, services, industries, guides, sister brands, texting note, form name). The phone number is
  never typed into a page (check.py enforces it).
- Brand: black #0b0b0c header, quote bar, footer and bands; logo gold #f5a623 buttons and FAQ band (black text); gold text
  only on black; white sections; dark-bordered form fields. Self-hosted Inter woff2, WebP 480/800/1200/1600/1920 srcset,
  preloaded hero with fetchpriority high, full-width rail `--rail: clamp(22px, 5.5vw, 140px)`.
- Header: logo, Services / Industries / Guides menus, Pricing, How It Works, About, Contact, EN/ES toggle (gold), tap-to-call.
  Footer: brand line, phone and email in one row; texting status; Services, Industries, Guides, Company and Dominion brands
  link rows; copyright and the followed "Designed by Dominion Web Design Pro" credit.

## Phase 3: pages (Prompts 7 to 12)
39 pages: home; services; 12 service pages; industries hub + 9 industry pages (six old .html URLs kept, three new);
5 guides; pricing; how it works; about; FAQ; contact + thanks; tools; privacy; terms; 404. Each written for its own
keyword (SERVICES.md, docs/keyword-plan.md), researched (docs/research/), with a sources list, 3 to 6 FAQs visible and in
FAQPage JSON-LD, a hero plus at least two in-body photos, and a "What it does not do" panel on every service and industry page.

## Phase 4: conversion, trust, media (Prompts 13 to 15)
- One Netlify form, "agency-contact", on /contact/ (pattern from Dallas Roofing Pro), thanks page /contact/thanks/.
- Social icons: slots hidden until URLs are added in site.json. No reviews, badges or trust claims (none exist).
- Media: 72 generic photos reused read-only from Dominion Web Design Pro, Houston HVAC Pro, Dallas Roofing Pro and Water
  Damage Pro Dallas, renamed with new alt text (docs/photos.json). 15 new images planned (docs/image-list.md, heroes first);
  each shows a crop of a reused photo under its final file name until made.

## Phase 5: SEO and remnant sweep (Prompts 16 to 17)
Every indexable page has a unique title and description, canonical on https://dominionaiagency.com, Open Graph and Twitter
tags with absolute image URLs, one H1, one JSON-LD @graph (Organization, WebPage, BreadcrumbList, Service/Article, FAQPage).
404 and thanks are noindex and out of the sitemap. robots.txt and sitemap.xml are generated. Sweep: no old-client names,
other numbers, placeholders, lorem ipsum, duplicate IDs or empty links (check.py); old pages moved to docs/old-site/.

## Phase 6: QA and handoff (Prompts 18 to 20)
See docs/qa.md (all checks pass) and docs/fact-check.md (556 claims checked independently).

| Route group | Status |
|---|---|
| All 39 routes: build, raw HTML (title, description, canonical, OG, JSON-LD, H1, body) | Passed |
| Responsive at 390 / 768 / 1024 / 1440 / 1920, overflow and row holes | Passed |
| Old URLs (18 sitemap URLs, every old rule, retired city wildcards) | Passed |
| Form rendering in static HTML | Passed; real submission not verified (not deployed) |
| Google Translate and GA4 live behavior | Not verified (needs the live domain) |

Remaining placeholders: the 15 Artistly images (stand-ins showing). Missing client inputs: social profile URLs, consulting
price (none shown), contract and cancellation terms (none stated). Launch blockers: none in the build; Maurice reviews,
generates images when ready, and merges `build` to `main` when he decides. Privacy and terms are written from INTAKE.md and
carrier requirements and should be read by Maurice before go-live; they are not legal advice.
