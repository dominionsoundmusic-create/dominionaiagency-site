# Fact-check log: fc2 (Oct 15 2026)

Independent check by fc2 (did not write these pages), following docs/fact-check/BRIEF.md.

Method: WebFetch and curl to outside hosts are blocked in this sandbox, so claims were checked with WebSearch limited to
official domains (fcc.gov, docs.fcc.gov, federalregister.gov, ftc.gov, ctia.org, campaignregistry.com,
help.gohighlevel.com, support.google.com, tools.google.com, ibm.com). Judgments rest on the page text those searches
returned, not on opening each PDF in full. Business claims were checked against INTAKE.md.

Build check after edits: `python3 build.py --out /tmp/fc2-dist`, then `scripts/check.py --skip-links --only <url>`:
0 errors, 0 warnings on all 9 pages. `scripts/similarity.py --only <url>`: no FAIL. Highest internal pair 3.9%
(/ai-voice-agent/), sister sites at most 1.8%, no shared 8-word runs.

## /ai-voice-agent/ (19 claims checked)
Confirmed:
- FCC 24-17 (CG Docket 23-362): adopted Feb 2 2024, released Feb 8 2024, "February 2024" on the page is correct. It
  confirms the TCPA's limits on "artificial or prerecorded voice" cover current AI technologies that generate human
  voices. Such calls need prior express consent unless there is an emergency purpose or an exemption. Sources: docs.fcc.gov
  FCC-24-17A1.pdf, and the fcc.gov news release "FCC Makes AI-Generated Voices in Robocalls Illegal".
- FTC: sellers and telemarketers must delete numbers on the National Do Not Call Registry from their lists at least
  every 31 days (FTC TSR guidance, and the 2004 release on scrubbing every 31 days). The page wording matches.
- "Some states keep their own lists": the FTC's "Complying with the Telemarketing Sales Rule" says the TSR does not
  preempt state law and some states run their own registries. CORRECTED SOURCES: this FTC page was added to m.sources,
  because the Q&A source alone did not show the state-list point in my searches.
- HighLevel outbound Voice AI: started from workflow actions; the account must accept outbound calling terms; calls are
  placed between 8:00 AM and 8:00 PM in the contact's phone-number time zone (calls outside the window are moved to the
  next allowed time); HighLevel does not validate contact consent at the platform level, so the business carries that duty.
- HighLevel agent transfer: a live call can pass to another Voice AI agent. Summaries, transcripts, recap emails and
  workflow triggers cover every agent on the call.
- HighLevel multi-language: you can pick one language or several. Answers come from a connected knowledge base.
- Prices $297 / $597 / $1,097 / $1,997 and the inbound, outbound and multiple-agent split all match INTAKE.md. No setup
  time is promised. No team or results claims. Limits section is present.
Not checked: none of the claims went unchecked. The FAQ explanation of how voice agents work (speech to text, model,
synthetic voice) is general background and was not checked against a source.

## /ai-chatbot-agency/ (16 claims checked)
CORRECTED:
- "When we switch on Conversation AI for the web chat channel, the AI is part of the widget once its code is on your
  site." HighLevel's current docs say a bot is assigned to the chat widget from the bot's Deploy tab (channels and
  routing), and is not included by default. Reworded to "Once we assign a HighLevel Conversation AI bot to the chat
  widget as one of its channels...". Source: help.gohighlevel.com "Manage Conversation AI bot channels and routing" and
  "Getting started with chat widget".
- FAQ: the widget code was said to go in the "header or footer". HighLevel's docs say the footer or body, and WordPress
  uses the LeadConnector plugin. Reworded to "usually in the footer ... WordPress sites can add it with a plugin".
- Voice widget: HighLevel's docs call it beta/Labs and say call transfer is not supported or currently unavailable.
  Reworded to "still lists the voice widget as a pre-release (beta) feature and says call transfer is not available in
  it yet". The meaning is unchanged, and the wording now matches the docs.
Confirmed: human handover action (assigns a team member, creates a task, sends a closing message, pauses the bot; it
fires on a request for a person, missing information or repeated failure); knowledge source types (FAQ, web crawler,
file upload, tables, rich text); the AI response info view shows the knowledge chunks behind a reply; IBM's rule-based
(if-then, scripted) vs AI (NLP, LLM) distinction; FTC Operation AI Comply (Sept 25 2024) cases over deceptive AI claims;
the voice widget uses the browser microphone after the visitor grants permission. Prices match INTAKE.md, and no
chatbot price was invented.
Not checked: none.

## /ai-appointment-booking/ (17 claims checked)
REMOVED:
- "Google and Outlook can be mixed this way" (conflict calendars). My searches did not confirm it, so I took it out.
Confirmed (HighLevel help center): the Voice AI Appointment Booking action books during the call; it can book on one
calendar or route by intent across several, with a fallback; if enabled, it can reschedule or cancel after verifying
caller details. Linked and conflict calendars, and outside events block only when marked busy (free events leave the
slot open). Write-back to one primary work calendar is recommended, because several write-back calendars cause
duplicates. Google and Outlook sync are supported. iCloud supports one-way sync only. Per-calendar availability
settings: pre and post buffers, minimum scheduling notice, date range, maximum bookings per day. Calendar notifications
cover booking confirmations, reminders, reschedules, cancellations and follow-ups by email, SMS or in-app, and the page
correctly limits this to email until texting is live. Zoom and Google Meet meeting locations exist (supports the FAQ
line on video consultations "if your calendar is set up for them"). Texting note present, and prices match INTAKE.md.
Not checked: none.

## /missed-call-text-back/ (20 claims checked)
CORRECTED:
- HighLevel built-in setting "sends a text for every missed call, including repeat calls a few minutes apart". The docs
  say "even if the same caller tries multiple times within a brief timeframe". Reworded to match ("in a short time").
- "Once a campaign is approved it gets an ID, and carriers enable texting for the numbers tied to that ID." TCR says it
  does not itself approve campaigns: a registered campaign gets a campaign_id, numbers are assigned to it, and carriers
  may run their own review. Reworded to say that.
- "texts from our system would be filtered or blocked" softened to "could be".
- FCC revocation: the rule as stated is the current rule (FCC 24-24): any reasonable means; stop, quit, end, revoke,
  opt out, cancel and unsubscribe are per se reasonable; honor within a reasonable time not to exceed ten business days.
  An FCC September 2026 fact sheet (FCC 26-67) addresses changes to these rules and its status is moving, so I added
  "These rules can change, so check the current version." I did not add the proposed details.
- CTIA source updated from the July 2019 PDF to the current May 2023 Messaging Principles and Best Practices. The page's
  wording (appropriate consent; STOP standard; also honor end, cancel, unsubscribe, quit; one final opt-out confirmation,
  then no further messages) matches the 2023 text in the search results.
- Source label for the HighLevel workflow trigger URL (48001212511) updated, because the article is now titled "Workflow
  Trigger - Call Details".
Confirmed: The Campaign Registry is the independent registry chosen by the mobile network operators to collect brand
and campaign data for 10DLC. Brands register through a messaging provider (CSP), not directly. The EIN is used to
verify the brand. Unverified brands cannot register campaigns. A campaign is the messaging use case. HighLevel has a
built-in missed call text back in Phone System settings, where the ring timeout decides what counts as missed. A
workflow with a wait step is HighLevel's suggested fix for repeats, and running both causes duplicates. The call
trigger filters on incoming plus busy or no-answer. Texting is stated as not live throughout, and no price is given for
the texting feature.
Not checked: none. The hand-typed sample texts and the call-back-or-text table are advice, not factual claims.

## /faq/ (12 claims checked)
Confirmed: A2P 10DLC registration required for business texting from a local number (TCR); HighLevel Voice AI overview
source is real; prices match INTAKE.md; 24/7 main line matches INTAKE.md; East Texas, remote, all 50 states matches
INTAKE.md; no setup time promised; not a HIPAA compliance program; STOP opt-out matches the terms page. No corrections.

## /contact/ (8 claims checked)
Confirmed against INTAKE.md: the AI answers the main line 24/7; the address is not public; East Texas, all 50 states;
prices $597, $1,097 and $1,997, and "single services start at $97 a month" (social media automation from $97); the
email is shared with Dominion Web Design Pro; the form named by site.forms.contact (agency-contact) has the fields
name, business, email, optional phone and message, with no SMS consent checkbox; texting note present. No corrections.

## /contact/thanks/ (3 claims checked)
No response time promised, texting is not live, no texts sent from the form. No corrections.

## /privacy-policy/ (9 claims checked)
- Carrier sentence present word for word: "No mobile information will be shared with third parties/affiliates for
  marketing or promotional purposes."
- Confirmed: GA4 derives approximate location from the IP address (Google Analytics Help); Google offers the Google
  Analytics Opt-out Browser Add-on (tools.google.com); the Netlify form; the HighLevel phone platform; texting not live.
- CORRECTED: "Google Translate ... sets a cookie to remember your choice" softened to "may set a cookie". My searches did
  not confirm Google's own documentation of the translate cookie.
- The STOP and HELP wording, "Message frequency will vary" and "Message and data rates may apply" are the standard
  carrier disclosures (CTIA). Not checked line by line against a specific carrier's program brief.

## /terms/ (6 claims checked)
- Reply STOP opt-out kept, along with one confirmation and then no further messages (matches CTIA 2023). HELP, message
  frequency, data rates and "carriers are not liable for delayed or undelivered messages" are the standard carrier
  disclosures. The referral links (HighLevel, ServiceTitan) are only on /tools/, which matches CLAUDE.md. The privacy
  sentence is paraphrased here, and the exact carrier wording is on the privacy page. No corrections.

## Summary
Pages: 9. Claims checked: about 110. Corrections: 12 (10 rewordings or source fixes, 1 removal, 1 source added).
Unchecked: the standard carrier-disclosure lines in privacy and terms were not compared against a specific carrier
program brief. The general "how a voice agent works" FAQ explanation was not checked against a source.
