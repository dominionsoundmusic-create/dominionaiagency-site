# Dominion AI Agency (dominionaiagency.com): PLAYBOOK 2.0 REBUILD. INSTRUCTIONS FOR CLAUDE CODE

You are rebuilding Maurice Johnson's AI automation agency site from scratch by running Dominic &
Dalton's Website Builder Prompt Playbook 2.0 (PLAYBOOK.md), Prompts 1 to 20, in full. About 33
pages, every one researched and written by hand for its own keyword. NO TEMPLATES.

## RUN STRAIGHT THROUGH. DO NOT STOP.
Maurice is not watching this session and cannot approve anything. Do NOT pause at the end of each
playbook phase, do NOT ask "continue?", do NOT wait for input. Make reasonable decisions yourself,
write them down in docs/decisions.md, and keep going until Prompt 20 is finished and every check
below passes. Commit and push the `build` branch after each phase so work is never lost (the live
site deploys from `main`, so pushing `build` does not go live). The only reasons to stop early:
something would cost money, deploy, merge to main, or change a repository other than this one.

## Source files (read all of them first)
- INTAKE.md: the facts. It wins over anything else. UNKNOWN means leave it off the site. READ THE
  "WHAT THE BUSINESS ACTUALLY IS" AND "TEXTING IS NOT LIVE YET" SECTIONS TWICE.
- PLAYBOOK.md: the playbook (Operating Rules, then Prompts 1 to 20). It was written for GHL AI
  Studio; apply its rules and its 20 steps to this static build system.
- keywords/AI-Agency-Keywords.xlsx: Ubersuggest, United States, pulled Oct 15 2026. 8,517 rows on
  an ALL tab plus 24 seed tabs, columns Keyword, Type (Suggestion or Question), Volume, SEO
  Difficulty, CPC, Seed. Every BUYER keyword with a volume of 10 or more (a small business owner
  looking for someone to set up AI for them, or for an AI receptionist/answering/chat/automation
  service) must be assigned to a page as a target or supporting keyword, or listed in
  docs/keyword-plan.md as deliberately unused with a one-line reason. Summarize unused rows by
  group: jobs and careers ("ai agency jobs", salaries), courses and "how to start an AI agency",
  free tools and DIY software comparisons, named companies or products (Lindy, Smith.ai, Ruby,
  Dialpad and so on), news and celebrity rows, enterprise-only rows, other countries. A first pass
  found about 531 buyer terms at 10+ (about 85,700 searches a month). The biggest:
  ai receptionist 12,100 (SD 33); ai automation agency 4,400 (SD 13, mixed intent);
  ai answering service 2,400; ai receptionist for small business 1,600 (SD 24, CPC $61);
  ai phone answering service 880; business answering phone service 720 (SD 11, CPC $103);
  ai consultant for small business 590 and ai consulting for small business 590;
  missed call text back 390; best ai receptionist for small business 260 (SD 10);
  dental ai receptionist 170 (SD 11, CPC $152). Verify every number yourself from the file.
- The CURRENT site in this repo (index.html, ai-automation-agency/, ai-chatbot-agency/,
  ai-consulting/, ai-crm-automation/, ai-lead-generation/, ai-workflow-automation/, ai-for/ (hub
  plus law-firms, hvac-companies, dentists, salons, contractors, restaurants), talking-website.html,
  dominion-crm-system.html, service-areas.html, tools/). Read every page. Keep the honest parts
  (the "What it does not do" sections, the texting status, the /tools/ referral disclosure).
  DROP every unverified claim the old pages make ("30-40% of calls go unanswered", "most leads go
  cold within 5 minutes", "double their reviews in 60 days", "live in 48 hours", "live in 7 days",
  "battle tested", the fake same-day plumbing conversation). Never copy the old layout.

## Copy the build system from Water Damage Pro Dallas (NOT its words)
Clone dominionsoundmusic-create/water-damage-pro-dallas, branch `main` (commit 59b7e0a or later:
the newest finished Playbook 2.0 site, live Oct 15 2026, with GA4 phone-tap tracking, full-width
layout, centered card rows, left-to-right footer rows, photo reuse script and similarity script).
Copy its BUILD SYSTEM: build.py (Jinja2, writes dist/), scripts/check.py, scripts/similarity.py,
scripts/apply_image_reuse.py and the docs/image-reuse.json + docs/photos.json pattern,
src/templates/, src/static/css/site.css and JS, the macros, the site.json structure, netlify.toml
(publish = "dist") and the docs/ document set as a pattern. For the one contact form, copy the
Netlify form pattern (and thanks page) from dominionsoundmusic-create/dallas-roofing-pro, branch
`main`. For the old-URL check, copy scripts/check_old_urls.py from dallas-roofing-pro `main`.
Adapt every value to Dominion AI Agency (black and gold, national, an agency that does the work).
NEVER copy page text, paragraphs, FAQs or sentence runs from any other site.

SISTER BRANDS: AI Voice Agent Pros (dominionsoundmusic-create/aivoiceagentpros-site) and Dominion
Web Design Pro (dominionsoundmusic-create/dominionwebdesignpro-site, `main`) target some of the
same buyers. Maurice WANTS this site to go after the AI receptionist and answering service terms
too ("the more real estate on the page, the better"). Clone both READ-ONLY, and make the
similarity script compare every page here against every page of both; any pair above 15% gets
rewritten. Never edit, commit to or push those repositories.

Keep the speed fix exactly (WebP 480/800/1200/1600/1920 srcset, preloaded hero with fetchpriority
high, self-hosted woff2 font) and the full-width layout (`--rail: clamp(22px, 5.5vw, 140px)`;
header, hero content, bands, text, photos, cards and footer all on the same left and right edge).
Card rows: 3 / 2 / 1 columns, any short last row CENTERED, never a hole on the right.

## OLD URLS MUST KEEP WORKING
Every URL in today's sitemap.xml must still return a page or a 301 to the closest new page:
/, /ai-automation-agency/, /ai-chatbot-agency/, /ai-consulting/, /ai-crm-automation/,
/ai-lead-generation/, /ai-workflow-automation/, /ai-for/, /ai-for/contractors.html,
/ai-for/dentists.html, /ai-for/hvac-companies.html, /ai-for/law-firms.html,
/ai-for/restaurants.html, /ai-for/salons.html, /dominion-crm-system.html, /service-areas.html,
/talking-website.html, /tools/. KEEP the six /ai-for/*.html industry URLs and /tools/ exactly
(rewrite their content, keep the URL). Keep EVERY rule in the current _redirects (the retired blog
posts, the retired URL structures and the wildcards that catch the ~5,800 retired city pages), and
make sure no new redirect breaks them. Write scripts/check_old_urls.py that lists every old URL
and proves it resolves in dist/ or has a redirect. Move the old page files into docs/old-site/ with
`git mv` so they are not published. Keep images/dominion-logo.svg, the favicons and robots.txt in
the new static folder.

## Pages to build (decide the exact list from the keywords, then follow it)
- Core (about 11): home, services overview, industries hub (/ai-for/), pricing, how it works,
  about (Maurice, Dominion Digital Group, East Texas, Black-owned, started 2022: nothing more),
  FAQ, contact + thanks, privacy, terms, 404. Tools page (/tools/) stays.
- Service pages (about 8), one per buyer cluster with demand: AI receptionist (and the "for small
  business" / "best" variants), AI answering service / AI phone answering, AI voice agent, AI
  chatbot and voice widget for a website, missed call text back (honest: texting not live yet),
  AI appointment booking, CRM and business automation, AI consulting for small business, AI
  automation agency, plus anything else the data supports. Reuse the old service URLs where a
  page still fits; 301 the rest.
- Industry pages (about 9): the six existing /ai-for/ pages rewritten, plus the industries the
  data supports (for example real estate agents, HVAC, plumbers, med spas: check volumes).
  Industry receptionist terms ("dental ai receptionist" and the like) go on the industry page.
- Guide pages (about 5) for the strongest question keywords, each researched and sourced, for
  example: how much an AI receptionist costs (published price ranges of the market, cited, and
  the line's own prices only as shown in INTAKE.md), AI receptionist vs answering service vs
  hiring a receptionist, is an AI receptionist worth it for a small business, what an AI
  automation agency does, how to choose one (questions to ask, red flags).
- Write SERVICES.md (every page, URL, target keyword with volume/SEO difficulty, supporting
  keywords) and docs/keyword-plan.md BEFORE writing pages. One page per intent cluster: never two
  pages targeting the same main term.

## KEYWORDS ON THE PAGE
Each page targets ONE main term: in the title tag, H1, opening paragraph, URL where it can be.
Its supporting terms go in naturally: subheadings, body text, image alt text where true, and the
FAQ questions written word for word the way people search (use the Question rows). Never stuff,
never repeat a phrase unnaturally. A term that will not fit naturally goes to the page it fits, or
the unused list with a reason.

## Hard rules for every page
1. This agency does the work, so "we set up", "we build", "we configure" are fine. Never claim a
   team, staff, engineers, developers, offices, client counts, client names, case studies,
   results, reviews, ratings, awards, certifications or partnerships that INTAKE.md does not list.
2. Never invent statistics. Any number about missed calls, response times, customer behavior or
   AI adoption must come from a real, cited source, stated exactly as the source states it. If a
   statistic cannot be verified, leave it out.
3. Texting is NOT live. Every mention of SMS, text reminders, missed call text back or texted
   review requests says plainly that voice works today and texting switches on once carrier
   approval clears. Never promise any setup time or response time.
4. Never name a competitor or a specific other agency. HighLevel may be named as the platform the
   agency builds on; HighLevel and ServiceTitan referral links stay only on /tools/ with its
   disclosure. Product names in the guides only as general market information, cited.
5. Prices: only the numbers in INTAKE.md as the agency's prices. Market price ranges in the guides
   must be cited and say real quotes vary.
6. Keep honest limits on every service and industry page ("What it does not do"): no legal advice,
   not a HIPAA compliance program, no clinical detail, integrations confirmed per client.
7. Never say an AI receptionist "never misses a call", "replaces your staff" or "works perfectly";
   describe what it does and what it does not.
8. No em dashes or en dashes in visible copy (except the Duplantis credit). No eyebrow labels. No
   emoji decorations. American spelling.
9. Every page except privacy, terms and 404 has 3 to 6 FAQs written the way people ask (use the
   Question rows), rendered visibly AND as FAQPage JSON-LD.
10. Every page has a full-width hero image plus at least two in-body images, each with filename,
    alt, width, height and loading="lazy" (hero eager), following the PHOTOS section below.
11. Facts must be real and current. Research each page on the web and cite every source in the
    page's sources list. If you cannot verify a fact, leave it out.
12. Each page is written for its own keyword. Measure Jaccard similarity on 5-word shingles between
    every pair of pages here, and every page here against every page of AI Voice Agent Pros and
    Dominion Web Design Pro; any pair above 15% gets rewritten. Record the numbers in docs/qa.md.
    Industry pages must be researched for THAT industry (how its calls actually come in, its busy
    seasons or hours, what callers ask, what the software it already uses can connect to) and
    each gets a different outline and angle.
13. Banned phrases: "your trusted partner", "one-stop solution", "look no further", "unmatched
    excellence", "we've got you covered", plus the WORDS TO AVOID in INTAKE.md.
14. Privacy policy must include, word for word: "No mobile information will be shared with third
    parties/affiliates for marketing or promotional purposes." Terms must include how to opt out of
    texts (reply STOP) for when texting goes live. These are carrier requirements.
15. Mark every page with the HTML comment `dwdp:handwritten 2026-10-15` in the first 4KB.

## PHOTOS: REUSE FIRST (Maurice's standing rule)
1. Reuse GENERIC photos from dominionsoundmusic-create/dominionwebdesignpro-site (`main`,
   src/static/images/body and other non-city folders): small business owners, desks, laptops,
   phones, storefronts. Skip any photo that shows a named city, skyline or landmark.
2. For industry pages, reuse generic trade photos from Maurice's lead sites where they fit (HVAC
   from dallas-hvac-pro or houston-hvac-pro, roofing from dallas-roofing-pro, plumbing and offices
   from water-damage-pro-dallas). Write new alt text for this site. Read-only: copy files, never
   edit those repositories.
3. One photo may fill several spots across the site, but never twice on the same page.
4. Only after that, list what is still needed in docs/image-list.md (heroes first). Aim for 15 or
   fewer new Artistly images. Each needed image shows a reused photo (never broken, never an empty
   box) until it arrives.

## Design (Maurice's standing rules, check each one)
- Header/menu bar in a real brand color (black with gold), never dull gray. Phone visible with
  tap-to-call. EN/ES Google Translate toggle in the header on every page, in brand colors.
- Hero stretches edge to edge on every page: full-strength photo, dark left-to-right fade behind
  the headline, logo/headline/buttons aligned to the left rail at 1440, 1920 and 2560 wide. Hero
  stays above the fold (max-height about 700px) with the call button visible.
- Body text, photos and cards run FULL WIDTH on the rail. Never box text into a narrow center strip.
  A photo standing alone in the text run is capped at about 560px tall (object-fit: cover).
- Mostly WHITE sections broken by occasional bold color bands (hero, white, black band, white, a
  gold band). Never pale off-white or cream tints. Never every section tinted.
- No white text or white boxes on white. Gold text only on black, never on white. Every card, box,
  form field and button has clear contrast (Maurice has trouble seeing light controls on white:
  give form fields and checkboxes dark borders).
- Footer: brand line, email and phone in one row; links as left-to-right rows.

## Before you finish (all must pass)
- `python3 build.py` then `python3 scripts/check.py`: 0 errors.
- `python3 scripts/check_old_urls.py`: every old URL resolves or redirects.
- Grep the built site for: em/en dashes in visible text (except the Duplantis credit),
  "guarantee", "#1", "never miss", "48 hours", "7 days", "our team of", "engineers", "HIPAA
  compliant", "double your", "30-40%", "award", "top-rated", "seamless", "unlock", "supercharge",
  "game-changer", "cutting-edge", "Johnson Plumbing", "(469)", "(832)", "(689)". Fix every hit
  (a sourced, cited statistic is the only allowed number of its kind).
- Every page mentioning text, SMS or "text back" also carries the texting-not-live note.
- No horizontal overflow at 1440, 1024, 768 and 390 px wide (do not hide overflow to pass).
  Scan every page for card, step and photo rows that leave a hole on the right at 390, 768, 1024,
  1440 and 1920 wide, and fix them. Screenshot the home page and two service pages at 1440, 1920
  and 2560, scroll so every photo loads, and look at each section yourself: hero content near the
  left edge, nothing invisible, no white on white, rows centered, footer in rows, no broken images.
- The Netlify form "agency-contact" present in the static HTML of /contact/ with its exact fields,
  and no other forms on the site.
- Independent fact-check: start separate sub-agents that did not write the pages (split the pages
  among several), have them check every factual claim and source on every page, and fix what they
  find. Record it in docs/fact-check.md. Never say "fact-checked" unless this was run.
- docs/image-list.md lists every image still needed, heroes first: File name, Size (heroes
  1920x1080, in-body 1200x800), then an Artistly prompt (bright, clearly visible, American small
  business settings, no text, no logos, no screens with readable words, no recognizable faces,
  "wide cinematic landscape shot, subject positioned on right third of frame, well lit").

## Git
- Work on the branch `build`. Commit as you go with clear messages and push `build` after each
  phase.
- Do NOT merge to main, do NOT push to main, do NOT change Netlify settings, do NOT pay for
  anything. Maurice decides when it goes live.

## Final report (Maurice reads on his phone, 5 lines max)
Pages built (count by type), checks passed, old URLs all resolving (yes/no), duplication range,
fact-check result, how many images need Artistly, and the one thing Maurice must do next.
