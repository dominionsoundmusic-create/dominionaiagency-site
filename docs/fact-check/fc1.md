# Fact-check log: fc1 (Oct 15 2026)

Checker: fc1, an independent sub-agent that did not write these pages.
Pages: / , /ai-receptionist/ , /ai-receptionist-for-small-business/ , /ai-answering-service/ , /how-it-works/ , /about/ , /tools/

Method: read CLAUDE.md, INTAKE.md, docs/WRITING-GUIDE.md, each page (body and FAQ front matter) and its
docs/research/ notes. WebFetch and curl to outside hosts are blocked in this sandbox, so every claim was checked
with WebSearch, limited by allowed_domains to the official site (advocacy.sba.gov, help.gohighlevel.com,
verizon.com, fcc.gov, ibm.com, research.ibm.com, bls.gov, servicetitan.com). Judgments rest on the search tool's
reading of those pages, not on a direct page load. Business claims were checked against INTAKE.md.

After edits: `python3 build.py --out /tmp/fc1-dist`, then `scripts/check.py --skip-links --only <url>`: 0 errors
on all seven pages (the 14 warnings shown for `--only /` belong to other pages: ai-consulting, ai-for, hvac, real
estate). `scripts/similarity.py --only <url>`: no FAIL. Highest figures: home 5.9% within site, 0.6% or less
against both sister sites.

## Shared HighLevel claims (used on several pages)
Confirmed on help.gohighlevel.com:
- Voice AI runs on an LC Phone number, a Twilio number or a Number Pool (Create, Test, and Deploy, 155000004107).
- Setup needs "approved business information for the prompt or Knowledge Base" (155000004107).
- Call Transfer is a built-in action that sends the caller to a human phone number (155000004107; Agent Transfer
  155000007796).
- Appointment Booking action books into a connected HighLevel calendar. AI working hours and calendar
  availability are separate settings (155000005293).
- Call log entries can show caller number, date and time, duration, actions triggered, summary, transcript,
  recording (155000005900).
- Post-call emails, sent after a call ends, can include the summary, contact details and transcript (described in
  155000005293).
- Performance summary emails can go weekly, every two weeks (fortnightly) or monthly (155000005214, titled
  "Configure Voice AI Performance Summary Emails"; also 155000007984).
- Web Call tests do not support Call Transfer; use a Phone Call test (155000004108).
- Voice AI can collect and update contact information during a call (overview 155000003911).
Not confirmed: any documented fallback to a message when a transfer goes unanswered. Wording that implied it
was a platform feature was changed (see below).

## / (home): 9 claims checked
- CORRECTED: "Most AI agencies ask you to book a call before they will say a number" is an unverified claim about
  the market. Now "Some agencies ask...".
- CORRECTED: "The same company runs Dominion Web Design Pro and AI Voice Agent Pros." INTAKE.md calls them sister
  brands but does not say who owns them. Now "Dominion Web Design Pro and AI Voice Agent Pros are sister brands."
- Confirmed against INTAKE.md: d/b/a of Dominion Digital Group, Black-owned, founded by Maurice Johnson, East
  Texas, 2022; founder sets up each system; all prices ($597, $1,097, $1,997, $297, $197, $97, $497); setup,
  training and support included; texting not live with the A2P 10DLC note; HighLevel described as widely used.
- Confirmed: The Campaign Registry handles 10DLC brand and campaign registration (source is real and fits).
- No setup or response time promised (checked).

## /ai-receptionist/: 14 claims checked
- CORRECTED (FAQ, transfer): "If nobody picks up, the agent can take a message instead" described a platform
  fallback that HighLevel's docs do not mention. Now "For the calls you do not want transferred, the agent takes
  a message instead".
- CORRECTED: "covered by the same agent, with different instructions if you want them" described a separate
  after-hours instruction setting that was not confirmed. Now "and we write what it should offer then".
- Confirmed (HighLevel): "Voice AI agents" name; approved business information; LC Phone or Twilio number;
  working hours separate from booking hours; call log fields; summary by email; Call Transfer to a number you
  choose; booking into a calendar.
- Confirmed (FCC): Declaratory Ruling FCC 24-17, adopted Feb 2 and released Feb 8 2024, says calls using AI-
  generated voices are "artificial" under the TCPA, so the TCPA's consent rules for artificial or prerecorded
  voice calls apply. The page's wording is accurate and tells the reader to see their own attorney. The source
  date (February 8, 2024) is correct.
- Confirmed against INTAKE.md: $297 and $597 with AI Starter's items; founder configures each system; remote,
  all 50 states, East Texas; texting note present.

## /ai-receptionist-for-small-business/: 12 claims checked
- Confirmed (SBA Office of Advocacy, FAQ About Small Business 2026, released Feb 3 2026): 36,207,130 small
  businesses in the U.S.; 29,811,495 have no employees (82.3%, "nonemployer firms"). Stated exactly; both SBA
  sources are in the list.
- CORRECTED (FAQ): "Many owners who look at this have no front desk at all" was an unverified claim about buyers.
  Now "Plenty of small businesses have no front desk at all", which matches the SBA nonemployer figure.
- CORRECTED (checklist): "with a message as the fallback when you cannot pick up" implied a confirmed feature.
  Now asks the buyer to find out what happens to the caller when they cannot pick up.
- CORRECTED: "Lists of the best AI receptionist ... rarely say how they ranked anything" softened to "often do
  not say", since it is opinion and was not measured.
- Confirmed (HighLevel): booking from a calendar within rules; answering hours and booking hours separate;
  transcripts, recordings and summaries; platform number with forwarding.
- Confirmed: US business texting from a standard 10-digit number needs 10DLC registration (The Campaign Registry).
- Confirmed against INTAKE.md: prices, packages, founder configures, texting note present.

## /ai-answering-service/: 12 claims checked
- CORRECTED (source): the source labeled "Configure Voice AI post-call and summary emails" (155000005214) is
  actually about scheduled performance summary emails, not post-call emails. It was cited for "A post-call email
  sends the summary". It is replaced by HighLevel's Appointment Booking in Voice AI article (155000005293), which
  describes post-call emails with the summary and transcript.
- Confirmed (Verizon, Call Forwarding: Everything You Need to Know, plus Verizon's Call Forwarding FAQs): on a
  wireless line, *71 plus the 10-digit number sets No Answer/Busy Transfer, which forwards after three or four
  rings or when busy; *73 turns it off. Stated correctly, and the page says codes differ by carrier.
- Confirmed (BLS OOH, Receptionists): receptionists answer the telephone and take messages or forward calls,
  schedule and confirm appointments, and greet visitors.
- Confirmed (HighLevel): LC Phone or Twilio number; call log fields; booking; transfer.
- Confirmed against INTAKE.md: $297, $597 with items; no human operators (INTAKE: no call center staffing);
  texting note present. The comparison table makes no claim about competitors' prices (it says ask each one).

## /how-it-works/: 13 claims checked
- Confirmed (IBM Think, What is speech recognition?): also called speech-to-text; a capability that lets a program
  process human speech into written form.
- Confirmed (IBM Think, What is text to speech?): turns text into audio. The page does not quote IBM on "natural-
  sounding", and the claim is general.
- Confirmed (IBM Research, What is RAG?): "grounding the model on external sources of knowledge" to supplement the
  LLM's internal representation. Accurate.
- Confirmed (HighLevel): browser (web) and phone test calls; transfers testable only on a phone call; performance
  summary emails weekly, every two weeks or monthly (155000005214, correctly labeled here); call logs; contact
  updates during a call.
- Confirmed in repo: /service-areas.html and /service-areas 301 to /how-it-works/ (src/static/_redirects), so "the
  old service areas page now points here" is true.
- Confirmed against INTAKE.md: no setup-time promise; monthly reporting in AI Starter and weekly in AI Pro; remote,
  all 50 states, no offices; texting note present.
- Not cited and not needed: NIST (the "language models can sound confident while being wrong" note carries no
  source or number).
- No corrections.

## /about/: 10 claims checked
- CORRECTED (FAQ): "sister brands under Dominion Digital Group" stated an ownership structure that INTAKE.md does
  not give. Now "They are sister brands, along with AI Voice Agent Pros and Dominion Review Pro."
- CORRECTED: "Dominion Digital Group runs a few brands that serve the same kind of owner" changed to "These sister
  brands serve the same kind of owner" for the same reason.
- CORRECTED: "something most sales pages cannot" changed to "something a sales page cannot" (an unmeasured
  claim about other businesses).
- Confirmed against INTAKE.md: trade name (d/b/a) of Dominion Digital Group; Maurice Johnson founder; 2022; East
  Texas; Black-owned; no address shown; no team or call center; founder sets up each system; phone answered 24/7
  by an AI receptionist; not a custom AI model builder, no legal, medical or tax advice, not HIPAA compliance;
  sister-brand URLs match src/data/site.json.
- Confirmed: HighLevel offers voice AI agents, Conversation AI for chat, calendars, CRM pipelines, workflows and
  email (help.gohighlevel.com articles on Voice AI, Conversation AI and calendars).

## /tools/: 8 claims checked
- CORRECTED: "ServiceTitan does not publish its prices on its website" was too broad. ServiceTitan's pricing page
  describes per-technician pricing and publishes prices for at least one add-on (Dispatch Pro), but no price for
  its core packages. Now: "ServiceTitan's pricing page describes per-technician pricing without listing a price
  for its core packages".
- CORRECTED (source): the Software Advice profile was cited as showing that pricing "is quote-based, not
  published", but current snapshots of that profile show "starting at" figures that conflict with each other. It
  is replaced by ServiceTitan's own pricing page (https://www.servicetitan.com/pricing).
- CORRECTED: "We list it because trade owners ask us what to run their jobs on" implied client conversations
  that INTAKE.md does not document. Now "it is the field service software we point established shops toward when
  they ask what to run their jobs on."
- Confirmed: ServiceTitan covers scheduling, dispatching, invoicing and job tracking for home service trades
  (servicetitan.com). HighLevel is also called GoHighLevel. The referral disclosure is present and the only
  referral links on the site are on this page (INTAKE.md). The ServiceTitan FAQ says the connection is confirmed
  per client.

## Not checked
- The ServiceTitan referral link (join.servicetitan.com/mzWepOS) and the HighLevel fp_ref link could not be
  opened (outbound fetch blocked). They match the old site's links.
- The live Verizon and HighLevel pages could not be opened directly; they may have changed after the search
  index's copy.
- The opinion statements on the home and small business pages ("a good voicemail can almost match", fit table)
  are judgments, not facts, so they were not checked.
