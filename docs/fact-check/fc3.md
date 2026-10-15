# Fact-check log: fc3 (Oct 15 2026)

Independent checker (did not write these pages). Pages: /ai-crm-automation/, /ai-workflow-automation/, /ai-consulting/,
/ai-automation-agency/, /ai-lead-generation/, /services/, /pricing/.

Method and access note: WebFetch and curl to outside hosts are blocked in this sandbox, so no source URL was opened
directly. Every claim below marked "confirmed" was confirmed from WebSearch results restricted (allowed_domains) to the
official site (ftc.gov, fcc.gov, gao.gov, nist.gov, sba.gov / advocacy.sba.gov, support.google.com,
developers.google.com, help.gohighlevel.com, gohighlevel.com, campaignregistry.com), judged from the official page
excerpts the search returned. One claim (the FTC "Keep your AI claims in check" blog post) was confirmed only from
secondary coverage that quotes the ftc.gov URL; noted below. Prices were checked line by line against INTAKE.md and
src/data/site.json (site.json matches INTAKE.md exactly; AI Empire has no review management in either).

Build check after edits: `build.py --out /tmp/fc3-dist`, `check.py --skip-links --only <url>`: 0 errors on all seven
pages (/ai-consulting/ keeps 2 informational warnings for the SBA Advocacy statistic, which is cited in Sources).
`similarity.py --only <url>`: no FAIL on any of the seven (max internal pair 5.9%, sister sites 0.2% or less, no
shared 8-word runs).

## /ai-crm-automation/ (21 claims checked)
CORRECTED
- "Review management ... is included in every package" was wrong: INTAKE.md lists review management in AI Starter and
  AI Pro only, not AI Empire. Now "included in AI Starter and AI Pro".
- "HighLevel's opportunities dashboard shows pipeline value, how many leads sit in each stage and how many were won":
  the cited article (48001152117) could not be found. HighLevel's "What Are Dashboard Widgets" article lists
  Opportunity Value, Conversion Rate, Funnel and Stages Distribution widgets. Reworded to match, source replaced
  (155000001212).
- Pipeline table listed Won and Lost as stages. HighLevel's "Getting Started: Setup Pipelines and Opportunities" says
  Won and Lost are opportunity statuses, not stages. Column renamed "Stage or status" and one sentence added; source
  added (155000005062).
- Review section: added Google's policy line that businesses may not discourage negative reviews or selectively solicit
  positive ones (review gating), confirmed on Google's Maps content policy pages; added the "Incentivized or biased
  reviews" policy page (16597558) as a source.
CONFIRMED
- HighLevel pipelines track opportunities through stages of a sales or service process (155000001982).
- Workflows: trigger then actions; Send Internal Notification; Add Task with or without a contact (155000002294).
- Send Review Request workflow action, example trigger Appointment Completed, channel Email or SMS (155000003291).
- CAN-SPAM per the FTC compliance guide: covers commercial email, no exception for business-to-business; no false or
  misleading header info; no deceptive subject lines; identify the message as an ad; valid physical postal address;
  clear way to opt out; honor opt-outs within 10 business days; a business that hires another company "can't contract
  away" its legal responsibility; transactional messages exempt from most provisions but may not contain false or
  misleading routing information.
- FTC fake reviews rule: announced Aug 14 2024, effective Oct 21 2024 ("in effect since October 2024" is right);
  bans fake reviews and incentives conditioned on a particular sentiment.
- Google Maps policy: no incentives such as payment, discounts, free goods or services in exchange for reviews.
- Prices: AI Starter $597 (CRM automation setup, inbound voice agent, review management, monthly reporting, email
  support), AI Pro $1,097 (full CRM automation), review management from $197, monthly/weekly reporting: all match.
- Texting: FAQ and band say texting is not live; texting_note present.
NOT CHECKED: none.

## /ai-workflow-automation/ (14 claims checked)
REMOVED
- Source "SBA: AI for small business" removed: nothing on this page uses it.
CORRECTED (sources only)
- Added "A List of Workflow Triggers" (155000002292) and "Workflow Action, Internal Notification" (155000003202),
  which support the trigger list and the notification claim already on the page.
CONFIRMED
- Workflow = trigger, optional filters, then actions (155000002288, 155000002445).
- Triggers named on the page exist: Form Submitted, Appointment Status / booked, Pipeline Stage Changed, Customer
  Replied, Contact Tag (added or removed).
- Wait action: fixed time, until a date, until a condition is met (155000002470).
- If/Else splits contacts into branches by conditions (155000002471, article exists).
- Internal notifications to users; Add Task with or without contact (155000002294).
- Workflow AI Builder: HighLevel says AI cannot test workflows and output must be reviewed and tested manually before
  publishing (155000006100).
- Prices: AI Pro $1,097 full CRM automation; AI Empire $1,997 complete automation suite, multiple voice agents,
  dedicated account manager: match INTAKE.md.
- Texting note present where internal text alerts are mentioned.
NOT CHECKED: none.

## /ai-consulting/ (13 claims checked)
CORRECTED
- GAO-26-107828 (May 4 2026): page said the report listed "over-reliance on AI". The report's wording is automation
  bias, "the tendency for people to over-trust automated outputs", and that "including human review" can mitigate some
  risks. Reworded to match.
- "Most small businesses are still deciding" overstated the SBA figure. Now "most small businesses are not using it yet"
  (8.8 percent use).
CONFIRMED
- SBA Office of Advocacy, Sept 24 2025, Census BTOS data: small firms (under 250 employees) AI use rose from 6.3 percent
  to 8.8 percent over six months. Stated exactly; both Advocacy URLs in Sources.
- SBA "AI for small business": "AI is relatively new, so start small" (confirmed on sba.gov). The "have another person
  review all AI products" advice for free AI tools was confirmed on sba.gov, in the search excerpt of the guide
  (one result attributed it to the legacy.sba.gov copy of the same guide).
- GAO-26-107828 names inaccurate outputs and data security and privacy concerns as risks.
- FTC Operation AI Comply, Sept 2024; Chair Khan: "there is no AI exemption from the laws on the books".
- FTC business blog "Keep your AI claims in check", Feb 2023 (author Michael Atleson): confirmed from secondary
  coverage quoting the ftc.gov URL; the ftc.gov page itself did not appear in search.
- NIST AI RMF 1.0: voluntary; four functions govern, map, measure, manage.
- No consulting price stated (none exists in INTAKE.md). Limits present.
NOT CHECKED: none beyond the blog-post caveat above.

## /ai-automation-agency/ (14 claims checked)
CORRECTED
- "outbound calls on AI Pro and above" and "Outbound calling, included from AI Pro": INTAKE.md lists outbound only in
  AI Pro (Empire lists "multiple AI voice agents", no inbound/outbound wording). Now "part of AI Pro" / "included in
  AI Pro".
- FCC source URL www.fcc.gov/document/fcc-makes-ai-generated-voices-robocalls-illegal could not be confirmed; replaced
  with the confirmed news release (docs.fcc.gov DOC-400393A1.pdf) and the Declaratory Ruling FCC 24-17.
CONFIRMED
- FCC Declaratory Ruling (adopted Feb 2, released Feb 8 2024): AI-generated voices are "artificial" under the TCPA,
  so calls need prior express consent absent an emergency purpose or exemption.
- HighLevel combines CRM, calendars, workflows, Voice AI and a chat widget (gohighlevel.com, help center).
- The Campaign Registry is the 10DLC brand and campaign registry (supports the texting note's A2P 10DLC line).
- FTC: AI claims must be truthful and supported (blog, see caveat above).
- Prices $597 / $1,097 / $1,997, voice agent from $297, setup/training/support included, monthly reporting on Starter,
  weekly on Pro, SEO pages on Empire: match INTAKE.md. Founder sets up each system, East Texas, 50 states: INTAKE.md.
- No team, client count or setup-time promise found. Texting note present.
NOT CHECKED: none.

## /ai-lead-generation/ (12 claims checked)
CORRECTED (sources only)
- Added HighLevel "Getting Started: Set Up Social Planner" (155000005063) to support the Social Planner scheduling
  claim, which had no source on the page.
CONFIRMED
- FTC fake reviews rule announced Aug 2024, covers AI-generated fake reviews, bars sentiment-conditioned incentives.
- Google Maps policy: no payment, discounts or free services for reviews.
- Google Search Central "Do you need an SEO?": "No one can guarantee a #1 ranking on Google" (paraphrased as "no one
  can promise a top spot", because the banned-word check blocks the exact wording).
- CAN-SPAM applies to commercial email.
- Operation AI Comply targeted AI income/business-opportunity schemes ("oversold AI income schemes" is fair).
- HighLevel Review Request action; Social Planner schedules posts to connected accounts.
- Prices: lead generation from $197, review management from $197, social media automation from $97, website from $497
  one time, SEO pages part of AI Empire, full social media management on Empire, website in AI Pro: all match.
- Texting note present.
NOT CHECKED: none.

## /services/ (16 claims checked)
No corrections. Every price matches INTAKE.md (voice agent from $297; lead generation and review management from
$197; social from $97; website from $497 one time; packages via the shared macro). "Inbound and outbound on AI Pro;
multiple agents on AI Empire" matches. "All twelve services" matches the twelve linked service pages. Missed call text
back described as not available yet; texting note present. No third-party facts on the page. Limits present.

## /pricing/ (22 claims checked)
CORRECTED
- "Most agencies ask for a discovery call before they share a number": no source; softened to "Many agencies".
- AI lead generation line said "Campaigns and capture forms that bring in inquiries", which contradicted the
  /ai-lead-generation/ page (no list buying, no promised new leads). Now "Capture and follow-up for the inquiries you
  already get ... logged in your pipeline and answered by email".
CONFIRMED
- Line-item table vs INTAKE.md: inbound voice agent in Starter; inbound and outbound in Pro; multiple agents in Empire;
  CRM setup in Starter, full in Pro; complete automation suite in Empire; review management in Starter and Pro only
  (correct, not Empire); lead generation in Pro, advanced in Empire; website in Pro; SEO pages in Empire; social
  automation in Pro, full management in Empire; monthly reporting Starter, weekly Pro; email support Starter, account
  manager Empire. All correct.
- No contract, trial, refund or setup-time terms stated. Texting note present.
NOT CHECKED: none.

## Shared file noted (not edited)
src/data/site.json prices and package items match INTAKE.md exactly.
