# Fact-check log: fc6 (Oct 15 2026)

Checker: fc6, independent (did not write these pages). Brief: docs/fact-check/BRIEF.md.

METHOD: WebFetch and curl to outside hosts are blocked in this sandbox, so no page was opened directly.
Every claim was checked with WebSearch, restricted with allowed_domains to the vendor's own domain or the
official source (smith.ai, heyrosie.com, goodcall.com, help.gohighlevel.com / gohighlevel.com, retellai.com,
ruby.com, intercom.com, bls.gov, onetonline.org, nist.gov, ftc.gov, fcc.gov). Results are judged from the
search engine's snapshot of those pages. Where the vendor's own pages disagreed with each other, that is noted.

Build check after edits: `python3 build.py --out /tmp/fc6-dist` then `scripts/check.py --skip-links --only <url>`:
0 errors on all three pages (warnings are the expected "vendor name only in guides, cited" notices).
`scripts/similarity.py --only <url>`: no FAIL; max 3.0% within the site, 0.2% or lower against both sister sites.

---

## /how-much-does-an-ai-receptionist-cost/ (src/pages/how-much-does-an-ai-receptionist-cost.html)

Claims checked: 24.

CORRECTED
1. Goodcall row: "Entry plan / Plans start at $79 a month", sourced to the home page. Goodcall's own pricing page
   lists Starter at $79 per agent per month with 100 unique customers a month (repeat calls from one number count
   once). Row now reads "Starter / $79 a month per agent, with 100 unique customers a month included"; source
   changed to https://www.goodcall.com/pricing. (Older Goodcall-hosted pages show $59/$39 starts; not used.)
2. Ruby billing increment: "rounded up in 30-second increments" REMOVED. Ruby's comparison page still says 30
   seconds, but its current Terms of Use and FAQ say 60-second increments. Now says Ruby bills by the receptionist
   minute and tells the reader to ask how partial minutes are rounded.
3. Ruby plan prices: kept ($250/50 min, $395/100, $720/200, $1,725/500, per ruby.com/plans-and-pricing/; the
   $250 and $1,725 ends also appear in Ruby's 2026 cost guide). Added a note that other Ruby pages show slightly
   different figures (its live receptionist page says plans start at $245) and to confirm the current price.
   FAQ reworded to "one provider's plans page listed $250 a month for 50 receptionist minutes... Prices change
   and real quotes vary."
4. Retell chat "$0.002 per message on its pricing page" REMOVED (body and FAQ). The $0.002 figure appears on
   Retell's home page; the pricing page lists per-model message rates (from $0.0005 to $0.10), so the claim as
   attributed was wrong. Now says chat is priced per message at rates that depend on the language model.
5. Intercom Fin: $0.99 per resolution confirmed on the "How Fin pricing works" help article; the resolution
   definition ("no further help is requested after the last AI answer") comes from the Fin AI Agent outcomes
   article, now added to sources. Added that the rate requires an active Intercom plan (stated in the article).
6. Added to the table note: prices change, promotions come and go, and a real quote may differ.

CONFIRMED (vendor's own domain)
- Smith.ai AI Receptionist Free: $0/month, 25 calls, $3.00 per call after, overages off by default (smith.ai
  pricing and AI receptionist pages). Pro at $2.00 a call is in Smith.ai's pricing table; $150/month for 75 calls
  appears on Smith.ai's own comparison pages (75 x $2.00 = $150). Other Smith.ai blog pages quote $270 and $500
  figures; the page uses only the pricing-table plan. Treat Pro as confirmed with that caveat.
- Rosie: Professional $49/250 min, Scale $149/1,000 min, Growth $299/2,000 min (heyrosie.com/pricing).
- HighLevel AI Employee Growth $50/month per enabled location with 100 Voice AI minutes; Unlimited $97/month per
  location, fair use; phone charges separate; Voice AI pay per use voice engine $0.045/min (from May 20 2026)
  plus TTS plus LLM tokens (help.gohighlevel.com AI product pricing article, modified Sep 28 2026).
- Retell AI pay as you go $0.07 to $0.31 per minute depending on models, voice, add-ons (retellai.com/pricing).
- Ruby per-minute vs per-call comparison page exists and contrasts the two models.
- BLS OOH receptionists: 2025 median pay $38,010 per year, $18.27 per hour, May 2025.
- BLS ECEC June 2026 (released Sep 9 2026): private industry $46.89 per hour worked; wages $32.82; benefits $14.07.
- FAQ range "$0 capped free tier, then $49 to a few hundred dollars a month" matches the confirmed rows.
- Dominion prices ($297 voice agent, packages and single prices via macros) match INTAKE.md. Texting note present.
  No setup-time promise ("We do not quote a setup time").

NOT CHECKED: none of the vendor rows could be opened live; all are judged from search snapshots of the vendor's
own pages, as stated above.

---

## /ai-receptionist-vs-answering-service/ (src/pages/ai-receptionist-vs-answering-service.html)

Claims checked: 12.

CORRECTED
- Sources: added the HighLevel "during-call and post-call actions in Voice AI" article, which documents the
  Trigger Workflow and Update Contact Field actions behind "trigger follow-up automations". No copy changed.

CONFIRMED
- BLS OOH receptionist summary (answering phones, receiving visitors, providing general information) and typical
  duties (answer and forward calls, schedule and confirm appointments, greet visitors, enter customer information
  into the database).
- O*NET 43-4171.00: operate switchboard to answer, screen or forward calls, providing information, taking messages
  or scheduling appointments; receive payment and record receipts for services (core tasks).
- BLS OOH customer service representatives: employment projected to decline 5 percent 2025 to 2035; automation
  and self-service cited; some companies keep in-house centers for complex inquiries; about 289,500 openings a
  year ("hundreds of thousands" in the FAQ is accurate).
- Ruby bills per minute and its comparison page contrasts per-minute and per-call billing.
- HighLevel Voice AI: answers from a knowledge base, collects caller details, books appointments, transfers;
  Call Transfer sends the call to a human at a phone number (help.gohighlevel.com).
- NIST AI 600-1 (July 2024) confabulation: "confidently stated but erroneous or false content".
- Texting note, limits block and no-competitor rule (Ruby named only as cited market information) OK.

NOT CHECKED: none.

---

## /is-an-ai-receptionist-worth-it/ (src/pages/is-an-ai-receptionist-worth-it.html)

Claims checked: 10.

CORRECTED
- HighLevel testing source URL slug fixed to the live article path
  (.../155000004108-testing-voice-ai-agents). Added the during/post-call actions article as a source for
  "update contact records, trigger follow-up".

CONFIRMED
- NIST AI 600-1 is the Generative AI Profile, a companion to the AI RMF; confabulation wording; suggested action
  MS-2.5-003 "Review and verify sources and citations in GAI system outputs" (final July 2024 text).
- FTC business blog "Keep your AI claims in check" (Feb 27 2023): AI claims need evidence.
- FTC Operation AI Comply (announced Sep 25 2024): enforcement sweep against deceptive AI claims and schemes.
- FCC Declaratory Ruling FCC 24-17 (adopted Feb 2 2024, released Feb 8 2024): TCPA "artificial or prerecorded
  voice" covers AI-generated voices; prior express consent required.
- HighLevel Voice AI features (knowledge base answers, collect info, book, route to a person) and testing guidance
  (web call and phone call; Call Transfer not supported in Web Call tests, so validate transfers on a phone call).
- No invented statistics: the worksheet leaves every number to the reader. $297 price matches INTAKE.md.
  Texting note present.

NOT CHECKED: none.

---

Totals: 46 claims checked across 3 pages; 6 corrections on the cost page (2 removals of unconfirmed details, 1
plan/price correction, 3 clarifications or added caveats), source fixes on all 3 pages. Research notes in
docs/research/ were not edited; where they differ (Ruby 30-second rounding, Retell $0.002 on pricing page, Goodcall
source), this log supersedes them.
