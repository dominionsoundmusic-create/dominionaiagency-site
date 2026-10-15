# WRITING GUIDE for page writers (Dominion AI Agency, Oct 15 2026)

Read CLAUDE.md, INTAKE.md and this file before writing a word. INTAKE.md is the source of truth. Every page is written
by hand for its own keyword, researched on the web, and cites its sources. NO TEMPLATES, no copied sentences.

## 1. Who we are (the only facts you may state about the business)
- Dominion AI Agency, a d/b/a of Dominion Digital Group. Founder Maurice Johnson. Dominion Digital Group started in
  2022, is Black-owned, based in East Texas. Serves all 50 states, set up remotely. Address never shown.
- A small AI automation AGENCY that DOES THE WORK: "we set up", "we build", "we configure", "we manage" are true.
  Built on HighLevel (GoHighLevel). What we set up: AI voice agents / AI receptionists that answer calls 24/7, take
  messages, answer common questions and book appointments; AI chat and voice widgets on websites; CRM pipelines and
  automated email follow-up; review requests; websites; AI consulting (what to automate first).
- Main line (903) 636-7511 is answered 24/7 by an AI receptionist: a live example of the product ("call it and hear it").
  NEVER type the number. Use {{ site.business.phone_display }} and tel:{{ site.business.phone_tel }} or the call_box macro.
- Email: {{ site.business.email }}.
- Prices (the ONLY numbers you may give as our prices): AI Starter $597/month (AI voice agent inbound, CRM automation
  setup, review management, monthly reporting, email support); AI Pro $1,097/month (voice agent inbound and outbound,
  full CRM automation, review management, AI lead generation, a professional website, social media automation, weekly
  reporting); AI Empire $1,997/month (multiple AI voice agents, complete automation suite, advanced lead generation,
  SEO pages, full social media management, a dedicated account manager). Setup, training and support included in all
  packages. Single services: AI voice agents from $297/month; AI lead generation from $197/month; website design from
  $497 one time; review management from $197/month; social media automation from $97/month. No consulting price exists.
  No contract terms, setup fees, trials, refunds or cancellation terms exist: never state any.
- NOT offered: custom AI models or software products, legal or medical advice, HIPAA compliance work, human call center staff.
- TEXTING IS NOT LIVE. A2P 10DLC carrier registration is pending. Any mention of SMS, texts, text reminders, missed call
  text back, texted review requests or text follow-up must say plainly that voice works today and texting switches on
  once carrier approval clears. Put {{ m.texting_note() }} (optionally with extra text) in the body of every page that
  mentions texting at all. Never present any text feature as working today.
- No team, staff, engineers, developers, offices, client counts, client names, case studies, results, reviews,
  ratings, awards, certifications or partnerships (other than the HighLevel and ServiceTitan referral links that live
  only on /tools/). Never write "our clients ..." as if we had named ones; write "a business that uses it", "you".
- Never promise a setup time or a response time. Never say the AI "never misses a call", "replaces your staff",
  "works perfectly", "understands everything". Describe what it does and what it does not.

## 2. Hard copy rules
- No em dashes or en dashes anywhere (use commas, colons, periods, "to" for ranges). No emoji. No eyebrow labels.
  American spelling. Plain, specific, human sentences; short paragraphs; no hype.
- Banned words/phrases: guarantee(d), #1, best in the industry, top-rated, award-winning, industry-leading, cutting-edge,
  revolutionary, game-changer, unlock, supercharge, seamless, leverage, "in today's fast-paced world", never miss,
  48 hours, 7 days (except "7 days a week"), live in X, double your, our team (of), engineers, HIPAA compliant,
  lawyer approved, your trusted partner, one-stop solution, look no further, unmatched excellence, we've got you covered,
  battle tested, testimonials, case study, five-star, award.
- Never name a competitor or another agency or vendor (RingCentral, Smith.ai, Ruby, Dialpad, Nextiva, Rosie, Goodcall,
  Jobber, Housecall Pro, Weave, Calendly, Square, Vagaro, OpenTable, Toast, Clio, Dentrix, HubSpot, Zapier, etc.) on
  service, industry or core pages. Name software by category ("your booking system", "your practice management
  software", "your field service software"). HighLevel may be named as our platform; ServiceTitan may be named on
  HVAC/plumbing pages without a link. GUIDES only may name products as cited general market information.
- Statistics: never invent. Any number about missed calls, response times, customer behavior, AI adoption, wages,
  market prices must come from a real source you opened, stated exactly as the source states it (same number, same
  population, same year), and that source must be in the page's sources list. If you cannot verify it, leave it out.
  Prefer government and primary sources (BLS, FCC, FTC, HHS, ABA, NAR, Census, SBA, EIA, ENERGY STAR, CTIA) over blogs.
  Market price ranges (guides only) must cite published pricing pages and say real quotes vary.
- Honest limits on every service and industry page: use {{ m.limits([...]) }} with page-specific items (e.g. no
  legal advice and no attorney-client relationship; not a HIPAA compliance program and no clinical or patient-record
  detail; does not price a job sight unseen; integrations with your booking or practice software confirmed per client).
- Do not give legal, medical or tax advice. When describing laws (TCPA, FCC rules, HIPAA, Fair Housing, ABA opinions),
  describe them factually, cite the primary source, and tell the reader to check with their own attorney/compliance help.

## 3. Keywords
- docs/keywords.json has each URL's target and supporting keywords (volume, SEO difficulty, question flag).
- Target term: in the title tag, the H1, the first paragraph of the body (the lead), naturally. Title <= 65 chars ideally
  (70 max), unique. Meta description 120 to 160 chars, unique, includes the target.
- Supporting terms: subheadings, body, image alt text where true, and FAQ questions. FAQ questions (3 to 6 per page,
  5 is ideal) are written word for word the way people search: use the Question rows and supporting rows as questions
  ("How much does an AI receptionist cost?", "What is an answering service?"). Never stuff; a term that does not fit
  naturally is left out (tell me in your report).

## 4. Page file format (src/pages/<slug>.html; industry pages src/pages/ai-for/<name>.html with `url:` set)
```
---
type: service            # service | industry | guide | page | about | contact | pricing
url: /ai-for/law-firms.html   # ONLY for the kept .html industry URLs; otherwise omit (folder URL from file name)
title: "..."
description: "..."
h1: "..."
crumb: "Short name"      # breadcrumb label
card_summary: "One sentence, about 20 to 28 words, shown on cards elsewhere."
schema_service:          # service and industry pages only
  name: "AI receptionist setup for small businesses"
  type: "AI receptionist"
  audience: "Dental offices"        # industry pages
  offers:                            # optional, ONLY INTAKE.md prices
    - {name: "AI voice agent", price: 297, unit: "MONTH", description: "From $297 a month"}
hero:
  image: <assigned hero file>
  alt: "<alt text describing what the photo actually shows>"   # for a planned image use its planned alt
  lead: "One or two sentences under the H1."
  secondary_label: "..."          # second hero button, page-specific (an anchor on the page or another page)
  secondary_href: "#section-id"
  note: "optional line under the buttons (default: call our line and judge for yourself)"
faq_title: "..."
faqs:
  - q: "Question written the way people search?"
    a: "<p>Answer, 50 to 110 words, HTML allowed, may link to other pages.</p>"
published: 2026-10-15     # guides only
---
{% block content %}
<section class="prose"> ... </section>
<section class="band band--tint"><div class="wide"> ... </div></section>   <!-- becomes a BLACK band: use at most once or twice -->
...
{{ m.sources([{'label': '...', 'url': 'https://...'}, ...]) }}   <!-- last thing inside the last prose section -->
{% endblock %}
```
The FAQ block (gold band) and the black call band are added by the layout. Do not add your own FAQ section.

## 5. Building blocks (CSS classes and macros that exist; use a different mix per page)
- Sections: `<section class="prose">` (white, full-width text on the rail); `<section class="band band--tint"><div class="wide">`
  (bold black band with white text, gold headings: max 2 per page; keep pages mostly white).
- Layout: `<div class="split">text div + img()</div>` (text beside photo; photo may come first); `<div class="grid-2">` /
  `<div class="grid-3">` of `<div class="panel"><h3>..</h3>..</div>`; `<ol class="steps"><li><strong>Title.</strong> text</li></ol>`;
  `<ul class="checks">`; `<ul class="facts"><li><strong>Label</strong>text</li></ul>`; `<div class="note"><p>..</p></div>`;
  `<div class="table-wrap"><table><thead><tr><th>..</th></tr></thead><tbody>..</tbody></table></div>` (stacks on phones);
  `<p class="lead">` for the opening paragraph; `<p class="section-intro">`.
- Macros: `{{ m.call_box('text') }}` (hear our AI receptionist, with call button); `{{ m.texting_note('extra') }}`;
  `{{ m.limits(['...', '...'], 'What it does not do') }}`; `{{ m.packages() }}` (three price cards);
  `{{ m.single_prices() }}` (table of single services); `{{ m.related(['ai-receptionist', 'ind:dentists', 'guide:cost'], 'Title') }}`
  (link pills; service slugs: ai-receptionist, ai-receptionist-small-business, ai-answering-service, ai-voice-agent,
  ai-chatbot, missed-call-text-back, ai-appointment-booking, crm-automation, business-automation, ai-consulting,
  ai-automation-agency, ai-marketing; industry slugs: law-firms, dentists, medical-offices, hvac-companies, plumbers,
  contractors, salons, restaurants, real-estate-agents; guide slugs: cost, vs, worth-it, what-is, choose);
  `{{ m.demo_link('text') }}` (link to the free website demo; use where a website fits); `{{ m.sources([...]) }}`;
  `{{ m.service_cards([...]) }}` / `{{ m.industry_cards([...]) }}` / `{{ m.guide_cards([...]) }}` (cards with photos: avoid
  on most pages; if used, none of their card photos may appear again on that page).
- Images: `{{ img('file.jpg', 'alt text', 1200, 800) }}` (1920, 1080 for -hero files). Every content page needs the hero
  plus AT LEAST TWO in-body img() figures (three is good). Only files from the photo list below. The SAME photo may
  never appear twice on one page (hero included). Alt text describes what the photo really shows (copy the alt below or
  adjust it truthfully); never claim a photo shows a client or our work.

## 6. Internal links (all planned pages; link 6 to 12 of them naturally in the copy)
/ /services/ /pricing/ /how-it-works/ /about/ /faq/ /contact/ /tools/ /ai-for/ /ai-receptionist/
/ai-receptionist-for-small-business/ /ai-answering-service/ /ai-voice-agent/ /ai-chatbot-agency/ /missed-call-text-back/
/ai-appointment-booking/ /ai-crm-automation/ /ai-workflow-automation/ /ai-consulting/ /ai-automation-agency/
/ai-lead-generation/ /ai-for/law-firms.html /ai-for/dentists.html /ai-for/medical-offices.html /ai-for/hvac-companies.html
/ai-for/plumbers.html /ai-for/contractors.html /ai-for/salons.html /ai-for/restaurants.html /ai-for/real-estate-agents.html
/how-much-does-an-ai-receptionist-cost/ /ai-receptionist-vs-answering-service/ /is-an-ai-receptionist-worth-it/
/what-is-an-ai-agency/ /how-to-choose-an-ai-agency/ /privacy-policy/ /terms/

## 7. Length, structure, originality
- Service, industry and guide pages: 1,400 to 2,200 words of your own copy (body + FAQ), 5 to 9 H2 sections, at least
  one distinctive design treatment for that page (a comparison table, a call-flow walk-through, a checklist, a
  decision table, a "who it fits / who it does not" pair). Do NOT reuse the same outline across your pages: each page
  gets its own angle, order and section types. Industry pages must be researched for THAT industry: how its calls come
  in, busy seasons or hours, what callers ask, what its existing software category can connect to, rules that apply.
- Never copy text from the old site (docs/old-site), from Water Damage Pro Dallas or from the sister sites
  (/home/user/dominionsoundmusic-create/aivoiceagentpros-site and dominionwebdesignpro-site). Sister pages target the
  same buyers: your wording, outline and examples must be your own. Similarity limit: 15% Jaccard on 5-word shingles
  against every other page; also no shared 8-word runs with the sister sites.
- Do not reuse the home page's sentences. Do not paste the same boilerplate paragraph into each of your pages.
- No fake call transcripts with names, no invented example businesses presented as real. A described sample call flow
  is fine if clearly generic ("a caller asks whether you are open Saturday; the agent answers from your hours").

## 8. Research and sources
- Use WebSearch / WebFetch. Open each source you cite and confirm the fact on the page. Cite 3 to 8 sources per
  service/industry/guide page in m.sources (official .gov, regulator, professional association and the platform's own
  documentation first). Write your research notes to docs/research/<page-slug>.md: each fact used, the exact quote or
  number, and its URL.
- HighLevel facts (what its voice AI / conversation AI / calendars / workflows do) must come from HighLevel's own help
  center or site (help.gohighlevel.com, gohighlevel.com, ideas/blog pages are weaker). If unsure, describe generally.

## 9. Check your work (do not touch shared files)
- Do NOT edit build.py, src/templates, src/static, src/data/site.json, scripts/ or other writers' pages. If you need
  something shared changed, say so in your final report.
- Build to your own folder and check only your pages:
  `python3 build.py --out /tmp/<yourname>-dist && python3 scripts/check.py --dist /tmp/<yourname>-dist --skip-links --only <url>`
  Fix every ERROR. WARNs about statistics mean: confirm it is cited. Then
  `python3 scripts/similarity.py --dist /tmp/<yourname>-dist --only <url>` and rewrite anything above 15% or any shared
  8-word run it reports for YOUR page (ignore pairs that do not involve your pages).
- Final report to me: files written, word counts, sources count, anything you could not verify and left out, any
  keyword you could not fit.

## 10. Photo list (docs/photos.json, plus planned new images that show a stand-in until Artistly makes them)
- attic-air-handler-insulation.jpg (1200x686): Air handler and flexible ducts in an attic over pink insulation
- attic-flashlight-rafters.jpg (1200x800): Person in an attic shining a flashlight along the rafters and roof decking
- bakery-owner-bread-shelves-hero.jpg (1920x1080): Bakery owner stocking shelves of fresh bread by the front window
- brick-ranch-home-oak-hero.jpg (1920x1080): Single-story brick home with a shingle roof under a large oak tree
- cafe-owner-laptop-window-hero.jpg (1920x1080): Owner working on a laptop at a small cafe counter beside the front window
- coffee-shop-counter-laptops.jpg (1200x800): Coffee shop with a barista at the counter and laptops on the tables
- contract-papers-table.jpg (1200x800): Person reviewing printed forms on a table by a window
- contractor-phone-truck-sunset.jpg (1200x500): Contractor in a hard hat and safety vest checking his phone beside a work truck at sunset
- couple-reviewing-papers-kitchen.jpg (1200x686): Older couple reviewing papers and a tablet at a kitchen table
- customer-phone-call-sunroom.jpg (1200x686): Woman smiling during a phone call in a bright sunroom
- desk-phone-laptop-lamp.jpg (1200x800): Desk with an office phone, a laptop and a sketch pad under a lamp
- east-texas-pine-woods.jpg (1200x800): Tall pine trees along a quiet road in the East Texas woods
- estimate-phone-kitchen-table.jpg (1200x800): Phone propped up on a kitchen table beside printed pages and a coffee mug
- florist-phone-map.jpg (1200x800): Florist looking at a map on her phone among buckets of fresh flowers
- gas-furnace-open-panel.jpg (1200x686): Gas furnace with its front panel open, lit by a flashlight
- hands-papers-coffee-counter.jpg (1200x800): Hands resting on printed pages at a counter next to a coffee cup and a phone
- homeowner-clipboard-pickup-truck-hero.jpg (1920x1080): Man holding a clipboard in front of a brick two-story house with a pickup truck at the curb
- homeowner-porch-phone-hero.jpg (1920x1080): Man on a phone call on the front walk of a brick home on a tree-lined street
- homeowner-thermostat-window.jpg (1200x500): Woman standing by a sliding glass door near a wall thermostat
- hvac-installers-new-condenser.jpg (1200x686): Two installers setting a new condenser on a pad beside a house
- hvac-tech-crouched-condenser.jpg (1200x686): HVAC technician crouched beside a condenser unit in a fenced back yard
- hvac-tech-furnace-closet-hero.jpg (1920x800): HVAC technician working on an indoor furnace and duct connection
- hvac-tech-gauges-condenser.jpg (1200x686): HVAC technician reading gauges on an outdoor condenser beside a brick house
- hvac-tech-gauges-side-yard-hero.jpg (1920x800): HVAC technician checking pressures on a condenser in a side yard
- hvac-techs-condenser-side-yard-hero.jpg (1920x800): Two HVAC technicians working on a condenser beside a white house
- kitchen-sink-cabinet-open.jpg (1200x675): Bright kitchen with the cabinet under the sink open and towels on the floor
- laptop-notebook-bright-desk.jpg (1200x800): Man typing on a laptop at a bright desk with an open notebook
- laptop-paperwork-kitchen.jpg (1200x800): Laptop and paperwork on a kitchen table with a coffee cup
- laundry-washer-water-heater.jpg (1200x800): Laundry room with a front-load washer and a tank water heater
- map-notes-laptop-coffee.jpg (1200x800): Person writing notes over a road map beside a laptop and a coffee
- new-store-owner-shelves.jpg (1200x800): Owner arranging stock on the shelves of a new store
- notebook-pen-coffee-desk.jpg (1200x800): Open notebook and pen on a desk by a window, with a coffee cup and a plant
- notebook-pen-table-window.jpg (1200x800): Spiral notebook and pen on a table beside a window
- notes-laptop-coffee-desk.jpg (1200x500): Person writing notes beside a laptop and a coffee cup
- office-laptop-files-glasses.jpg (1200x800): Laptop, a stack of file folders and reading glasses on an office desk
- office-laptop-folders.jpg (1200x800): Person at an office desk with a laptop, folders and a coffee
- office-tablet-front-window.jpg (1200x800): Man reading a tablet at a desk by the glass front of a small office
- owner-laptop-kitchen-table-hero.jpg (1920x1080): Small business owner in a work vest at a kitchen table with a laptop and notebook
- owner-laptop-tablet-shop-window-hero.jpg (1920x1080): Owner working on a laptop and tablet at a counter by the front window of a shop
- person-phone-hallway.jpg (1200x675): Person on a phone call walking down a hallway toward the back door
- phone-counter-rainy-window.jpg (1200x675): Phone lying on a kitchen counter in front of a rainy window
- phone-notes-desk-window-hero.jpg (1920x1080): Phone and a notepad on a desk beside a window looking out at a house
- phone-photo-house-front.jpg (1200x686): Hand holding up a phone to photograph the front of a house
- phone-planner-desk.jpg (1200x800): Hands holding a phone over an open planner on a desk
- plumber-kneeling-toolbox.jpg (1200x800): Plumber in overalls and ear protection kneeling by a wall with a toolbox
- porch-reading-paperwork.jpg (1200x675): Man reading paperwork on a porch, a white service van parked at the curb
- printed-plans-highlighter-desk-hero.jpg (1920x1080): Printed plan sheets with a pen and a highlighter on a desk beside a laptop
- quiet-waiting-room-armchairs-hero.jpg (1920x1080): Two armchairs and a side table in a quiet, sunlit waiting room
- reading-paperwork-glasses.jpg (1200x800): Two people reading printed pages at a table with reading glasses
- roof-new-decking-sheets.jpg (1200x800): New plywood decking sheets laid on a roof during a tear-off
- roofer-kneeling-shingles-hero.jpg (1920x800): Roofer kneeling on a shingle roof on a sunny day
- roofer-ladder-brick-home.jpg (1200x800): Roofer standing at the foot of a ladder set against the gutter of a brick home
- roofer-sealing-vent-hero.jpg (1920x800): Roofer sealing around a roof vent pipe with a caulk gun
- roofers-shingle-roof-hero.jpg (1920x800): Crew of roofers working on a shingle roof under a clear blue sky
- service-van-evening-call-hero.jpg (1920x800): Service technician walking from a red van to a house at dusk
- sewer-cleanout-yard.jpg (1200x800): White sewer cleanout pipe in a front yard flower bed
- shop-owner-laptop-counter-hero.jpg (1920x1080): Shop owner typing on a laptop at a wooden counter lined with shelves of jars
- shop-owner-laptop-gift-shop-hero.jpg (1920x1080): Woman working on a laptop at the counter of a gift shop
- shop-owner-laptop-shelves.jpg (1200x800): Shop owner on a laptop at the counter of a store with shelves of goods
- shop-owner-phone-call-notes-hero.jpg (1920x1080): Store owner on a phone call, writing notes at the counter of a small shop
- shop-owner-phone-laptop-register-hero.jpg (1920x1080): Shop owner holding a phone beside a laptop and register at the counter
- shop-owner-phone-shelves.jpg (1200x800): Shop owner checking her phone among shelves of packaged goods
- shop-owner-tablet-counter-hero.jpg (1920x1080): Woman at a shop counter looking at a tablet, shelves of goods behind her
- sketches-laptop-desk-hero.jpg (1920x1080): Hand-drawn sketches spread on a desk beside a laptop
- small-meeting-room-round-table.jpg (1200x800): Small meeting room with a round table, two chairs and a yellow legal pad
- thermostat-hand-warm-light.jpg (1200x686): Hand adjusting a wall thermostat in a warmly lit living room
- tradesman-laptop-workshop.jpg (1200x686): Tradesman in overalls typing on a laptop at his workshop bench
- two-story-brick-home-street-hero.jpg (1920x1080): Two-story brick home on a quiet residential street
- waiting-room-sofa-lamp.jpg (1200x800): Gray sofa, floor lamp and plant in a calm waiting room
- walk-up-cafe-window.jpg (1200x800): Small walk-up cafe window beside a tree-lined path, a bicycle parked by the door
- water-shutoff-valve-box.jpg (1200x800): Gloved hand turning a brass water shutoff valve in a ground box
- woodshop-owner-phone-call-hero.jpg (1920x1080): Woodworker on a phone call at his workbench with the garage door open behind him
PLANNED
- dental-office-front-desk-hero.jpg: Bright dental office front desk with a phone and an appointment screen turned away, chairs in the waiting area (planned new image; stand-in until made)
- salon-stylist-station-hero.jpg: Hair salon with a stylist working at a chair while a phone sits on the front counter (planned new image; stand-in until made)
- restaurant-host-stand-hero.jpg: Busy restaurant dining room at dinner service with a host stand and phone near the door (planned new image; stand-in until made)
- medical-office-reception-hero.jpg: Clean medical office reception desk with a phone and a quiet waiting area (planned new image; stand-in until made)
- real-estate-agent-home-tour-hero.jpg: Real estate agent walking up the front path of a two-story home for a showing (planned new image; stand-in until made)
- law-firm-reception-hero.jpg: Small law office reception area with a desk phone, legal pads and shelves of binders (planned new image; stand-in until made)
- dental-front-desk-phone.jpg: Dental office front desk phone beside an appointment book and a cup of pens (planned new image; stand-in until made)
- salon-front-desk-booking.jpg: Salon front counter with a phone, a booking tablet and shelves of hair products (planned new image; stand-in until made)
- restaurant-host-stand-phone.jpg: Restaurant host stand with a cordless phone and a reservation book (planned new image; stand-in until made)
- medical-office-check-in-desk.jpg: Medical office check-in desk with a phone, a clipboard and hand sanitizer (planned new image; stand-in until made)
- real-estate-agent-front-door-keys.jpg: Hand holding house keys in front of the door of a home for sale (planned new image; stand-in until made)
- law-office-intake-notes.jpg: Legal pad with handwritten intake notes beside a desk phone in a law office (planned new image; stand-in until made)
- salon-stylist-blow-dry.jpg: Stylist blow-drying a client's hair at a salon station (planned new image; stand-in until made)
- restaurant-kitchen-pass-service.jpg: Plates lined up at a restaurant kitchen pass during dinner service (planned new image; stand-in until made)
- plumber-under-kitchen-sink-hero.jpg: Plumber working under a kitchen sink with a flashlight and tools (planned new image; stand-in until made)
