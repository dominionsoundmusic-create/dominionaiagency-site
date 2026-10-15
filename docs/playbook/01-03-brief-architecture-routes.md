# Playbook 2.0, Prompts 1 to 3: fact brief, architecture, baseline and route plan

Dominion AI Agency (dominionaiagency.com). Oct 15 2026. Source of truth: INTAKE.md, then CLAUDE.md. PLAYBOOK.md was
written for GHL AI Studio (TanStack Start SSR); this build applies its rules and 20 steps to the static Jinja build
system copied from Water Damage Pro Dallas (decision D1 in docs/decisions.md).

## Prompt 1: client fact brief

| Item | Value | Status |
|---|---|---|
| Official name | Dominion AI Agency, a d/b/a of Dominion Digital Group | Confirmed |
| Category | Small AI automation agency: sets up and manages AI tools for small local businesses on HighLevel (AI receptionists / voice agents, website chat and voice widgets, CRM pipelines and email follow-up, review requests, websites, AI consulting). Does the work itself ("we set up / build / configure" is true). Not a software company, not a lead line. | Confirmed |
| Services not offered | Custom AI models or software products, legal or medical advice, HIPAA compliance work, call center staffing with humans | Confirmed |
| Service area | All 50 states, set up remotely. No city pages (retired Sep 11 2026, wildcards keep redirecting). Industry pages are the local axis. | Confirmed |
| Address | DO NOT DISPLAY (East Texas only) | Confirmed |
| Phone | (903) 636-7511, tel:+19036367511, answered 24/7 by an AI receptionist (a live example of the product). Lives once in src/data/site.json. | Confirmed |
| Email | maurice@dominionwebdesignpro.com (shared across brands) | Confirmed |
| Hours | The line is answered 24 hours a day, 7 days a week by an AI receptionist | Confirmed |
| Founded / owner | Dominion Digital Group started 2022; founder Maurice Johnson; Black-owned. Nothing more specific. | Confirmed |
| Prices | AI Starter $597/mo, AI Pro $1,097/mo, AI Empire $1,997/mo (setup, training and support included); voice agents from $297/mo; AI lead generation from $197/mo; website design from $497 one time; review management from $197/mo; social media automation from $97/mo | Confirmed (only these numbers) |
| Texting (SMS) | NOT live. A2P 10DLC carrier registration pending. Every texting mention says voice works today and texting switches on once carrier approval clears. | Confirmed, launch rule |
| Main CTA | Call (903) 636-7511 and hear the AI receptionist answer (header + hero tap-to-call on every page) | Confirmed |
| Second CTA | One Netlify form "agency-contact" on /contact/ only (name, business name, email, phone optional, what you want automated). No SMS consent box. Thanks page /contact/thanks/. | Confirmed |
| Third CTA | "See a free website demo" to https://dominionwebdesignpro.com/demo.html where it fits | Confirmed |
| Brand | Black and gold, logo images/dominion-logo.svg (gold wordmark, cyan mark). Header black with gold. Mostly white sections, black band, gold band. No cream tints. | Confirmed |
| Top bar | "John 3:16" left; "I believe the unbelievable, I receive the impossible, because it's doable." credited "— Jesse Duplantis" | Confirmed |
| Footer | "© 2026 Dominion Digital Group. All rights reserved." + followed credit link "Designed by Dominion Web Design Pro"; sister brand links (Dominion Web Design Pro, AI Voice Agent Pros, Dominion Review Pro); links in left-to-right rows | Confirmed |
| Language | EN/ES Google Translate toggle in the header, brand colors | Confirmed |
| Analytics | GA4 G-ZBZQPMRDEW with the phone-tap event | Confirmed |
| Social / GBP | None yet; icon slots data-driven and hidden | Missing but deferrable |
| Reviews, team, client counts, case studies, certifications, awards | None. Never invent. | Confirmed (none) |
| Partnerships | Only the HighLevel and ServiceTitan referral links disclosed on /tools/ | Confirmed |
| Photos | Only the logo exists. Reuse generic photos from Dominion Web Design Pro and the lead sites (read-only copies), then Artistly list. | Missing but deferrable (stand-ins) |
| Domain / canonical | https://dominionaiagency.com (deploys from `main`; work stays on `build`) | Confirmed |
| Consulting price | Not in INTAKE.md | Missing but deferrable: no price shown for consulting on its own |
| Contract length, cancellation, refunds, setup timelines | Not in INTAKE.md | Missing: never stated |

Contradictions found: the old site said "live in 48 hours", "live in 7 days", "30-40% of calls go unanswered", "double their
reviews in 60 days", "100+ city SEO pages", "unlimited review requests", "review management (SMS)". INTAKE.md wins: all dropped;
SMS review requests carry the texting note; Empire is described with INTAKE.md's words ("SEO pages").

Launch blockers: none for the build. Before go-live Maurice decides (merge to main). Texting stays "not live" until A2P clears.

## Prompt 2: architecture

Not the GHL AI Studio SSR master. This repo held hand-written static HTML (index.html, folders per service, /ai-for/*.html,
tools/). Per CLAUDE.md the build system is copied from Water Damage Pro Dallas (commit 59b7e0a): `build.py` (Python 3,
Jinja2, PyYAML, Pillow) renders `src/pages/**.html` (YAML front matter + Jinja body) through `src/templates/` into `dist/`.
Every page is complete static HTML: title, description, canonical, Open Graph, one JSON-LD @graph, H1 and all copy are in
the initial response (the static equivalent of SSR). Netlify publishes `dist/` (netlify.toml `publish = "dist"`, no build
command); `_redirects` lives in `src/static/` and is copied to `dist/`. Shared data (business, phone, nav, services,
industries, guides, footer, analytics, forms) lives in `src/data/site.json`. Commands:

- `python3 build.py` (build, writes docs/image-list.md)
- `python3 scripts/check.py` (rules + SEO + links + images + JSON-LD + forms)
- `python3 scripts/check_old_urls.py` (every old URL resolves or redirects)
- `python3 scripts/similarity.py --report docs/qa-similarity.md` (Jaccard, 5-word shingles, this site and both sister sites)
- `python3 scripts/apply_image_reuse.py` (photo reuse report)
- `python3 scripts/grep_check.py` (CLAUDE.md final grep list)
- `python3 scripts/keyword_plan.py` (docs/keyword-plan.md)
- `node scripts/responsive_check.js` (Playwright: overflow + row holes at 390/768/1024/1440/1920, screenshots)

## Prompt 3: baseline and route matrix

Baseline: the old site had no build, no checks. Its pages are moved with `git mv` to docs/old-site/ (not published).
Pre-existing problems recorded: unverified statistics and setup-time promises (dropped), emoji decoration, eyebrow labels,
em dashes, a fake plumbing conversation on talking-website.html, an old sitemap of 18 URLs.

| Route | Type | Source | Nav | Sitemap | Index | Old URL? |
|---|---|---|---|---|---|---|
| / | home | src/pages/index.html | logo | yes | yes | kept |
| /services/ | services overview | services.html | Services | yes | yes | new |
| /ai-receptionist/ | service | ai-receptionist.html | Services menu | yes | yes | new |
| /ai-receptionist-for-small-business/ | service | | Services menu | yes | yes | new |
| /ai-answering-service/ | service | | Services menu | yes | yes | new |
| /ai-voice-agent/ | service | | Services menu | yes | yes | new |
| /ai-chatbot-agency/ | service (chat + voice widget) | | Services menu | yes | yes | kept (talking-website.html 301s here) |
| /missed-call-text-back/ | service (texting not live) | | Services menu | yes | yes | new |
| /ai-appointment-booking/ | service | | Services menu | yes | yes | new |
| /ai-crm-automation/ | service | | Services menu | yes | yes | kept (dominion-crm-system.html 301s here) |
| /ai-workflow-automation/ | service (business automation services) | | Services menu | yes | yes | kept |
| /ai-consulting/ | service | | Services menu | yes | yes | kept |
| /ai-automation-agency/ | service | | Services menu | yes | yes | kept |
| /ai-lead-generation/ | service (AI marketing agency) | | Services menu | yes | yes | kept |
| /ai-for/ | industries hub | ai-for/index.html | Industries | yes | yes | kept |
| /ai-for/law-firms.html, hvac-companies.html, dentists.html, salons.html, contractors.html, restaurants.html | industry | ai-for/*.html (front matter url) | Industries menu | yes | yes | kept exactly |
| /ai-for/real-estate-agents.html, plumbers.html, medical-offices.html | industry | | Industries menu | yes | yes | new |
| /how-much-does-an-ai-receptionist-cost/, /ai-receptionist-vs-answering-service/, /is-an-ai-receptionist-worth-it/, /what-is-an-ai-agency/, /how-to-choose-an-ai-agency/ | guide | | Guides menu | yes | yes | new |
| /pricing/ | pricing | | Pricing | yes | yes | new |
| /how-it-works/ | support | | How It Works | yes | yes | new (service-areas.html 301s here) |
| /about/, /faq/ | support | | About, FAQ | yes | yes | new |
| /contact/ | contact + the one form | contact/index.html | Contact | yes | yes | new |
| /contact/thanks/ | thanks | contact/thanks.html | no | no | noindex | new |
| /tools/ | referral disclosure page | tools.html | footer | yes | yes | kept exactly |
| /privacy-policy/, /terms/ | legal | | footer | yes | yes | new |
| /404.html | 404 | 404.html | no | no | noindex | new |

Stage plan: Phase 1 (this file, docs/keyword-plan.md, SERVICES.md, docs/decisions.md); Phase 2 (build system, site.json,
brand CSS, header/footer/nav, redirects, old files moved); Phase 3 (pages: home, services, 12 service pages, hub + 9
industry pages, 5 guides, about/FAQ/how it works/pricing); Phase 4 (contact form + thanks, social slots, photos and
image list); Phase 5 (SEO pass, remnant sweep); Phase 6 (responsive and accessibility QA in Chromium, functional QA,
independent fact-check, similarity, final handoff in docs/playbook/04-20-build-qa-handoff.md).
