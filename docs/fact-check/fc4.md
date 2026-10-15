# Fact-check log: fc4 (Oct 15 2026)

Checker: independent sub-agent fc4 (did not write these pages). Brief: docs/fact-check/BRIEF.md.

Method: WebFetch and curl to outside hosts are blocked in this sandbox, so no page was opened directly. Every claim
below was checked with WebSearch, mostly restricted with allowed_domains to the official site (census.gov, sba.gov,
fcc.gov, ftc.gov, americanbar.org, hhs.gov, cochrane.org, 911.gov, 988lifeline.org, samhsa.gov, bls.gov, irs.gov,
fda.gov, restaurant.org, nar.realtor, hud.gov, ecfr.gov, help.gohighlevel.com), and judged from the result text
quoting those pages. "Confirmed" below means confirmed that way.

Business claims on all seven pages were checked against INTAKE.md: only INTAKE.md prices ($297 voice agent, $597
Starter, $1,097 Pro, $1,997 Empire; outbound only on AI Pro); no team, staff, client counts, results, reviews or
awards; no setup or response time promises; texting described as not live wherever SMS or reminders come up (each
page carries m.texting_note or the FAQ says so); no "never misses", "replaces your staff", "works perfectly"; no
"HIPAA compliant" (dental and medical pages say plainly the service is not a HIPAA compliance program); no competitor
or product names; integrations always "confirmed per office/firm before promised". No problems found.

Build checks after edits: `python3 build.py --out /tmp/fc4-dist` then `scripts/check.py --skip-links --only <url>`:
0 errors on all seven pages. `scripts/similarity.py --only <url>`: no FAIL; highest pair 2.1% (salons, industry
group); 0.2% or lower against Dominion Web Design Pro and AI Voice Agent Pros.

## /ai-for/ (index.html): 9 claims checked, 0 corrected
Confirmed:
- Census BTOS story "Large Firms With at Least 20 Employees Biggest AI Users" (May 2026): data Dec 14 2025 to May 3
  2026; overall AI use "hovered between 17% and 20%"; fewer than 20% of firms with four or fewer employees; question
  changed in November 2025 from "in producing goods or services" to "in any business function". Page wording matches.
- SBA launched the AI for Small Businesses Resource Hub at the inaugural AI Small Business Summit at Georgia Tech,
  December 2024 (release dated Dec 11 2024). Matches.
- FCC Declaratory Ruling, February 2024: AI-generated voices are "artificial" voices under the TCPA; consent rules
  apply. Matches (adopted Feb 2, released Feb 8 2024).
- FTC business blog "Keep your AI claims in check" (Feb 2023) warns against exaggerating what AI can do. Matches.
- "Nine industry pages": nine /ai-for/*.html pages exist. Matches.
- HighLevel cited only as the platform. OK.

## /ai-for/law-firms.html: 14 claims checked, 1 corrected
Corrected:
- Source label for the ABA news page used a wrong title. The page at that URL is titled "ABA issues first guidance on
  a lawyer's use of AI tools". Label fixed (americanbar.org).
Confirmed:
- ABA Formal Opinion 512 issued July 29, 2024; first ABA formal ethics opinion on generative AI; covers competence,
  confidentiality, communication, supervision and fees; boilerplate engagement-letter consent is not enough.
- Model Rule 5.3 title "Responsibilities Regarding Nonlawyer Assistance" and URL; paragraph (a) "measures giving
  reasonable assurance"; Opinion 512 applies 5.1/5.3 to AI tools.
- Model Rule 1.18 "Duties to Prospective Client": confidentiality even if no client relationship; conflict from
  significantly harmful information; (d) screening exception turns on reasonable measures to avoid more
  disqualifying information than reasonably necessary. URL real.
- Model Rule 1.6(c) reasonable efforts to prevent unauthorized disclosure; title "Confidentiality of Information".
- Model Rule 7.3 current title "Solicitation of Clients" (URL slug keeps the old "direct contact" name, and is the
  ABA's live URL); (b) bars live person-to-person solicitation when a significant motive is pecuniary gain.
- FCC Feb 2024 TCPA AI-voice ruling with prior consent requirement.
- Statute-of-limitations line makes no claim beyond "varies by state". OK.

## /ai-for/dentists.html: 10 claims checked, 3 corrected
Corrected:
- Cochrane recall review: the page said intervals "made no difference". The review says "little to no difference"
  for adults between six-monthly and risk-based check-ups in tooth decay, gum disease and quality of life (after four
  years). Wording fixed. The source URL was the old address; replaced with the current Cochrane page
  https://www.cochrane.org/evidence/CD004346_how-often-should-you-see-your-dentist-check and its current title.
- HHS FAQ 198 label: the FAQ's real title is "May physician's offices or pharmacists leave messages for patients at
  their homes...". Label fixed (URL unchanged, confirmed on hhs.gov).
- HHS sample BAA page label: the page is titled "Business Associate Contracts" (sample provisions). Label fixed.
Confirmed:
- HHS business associate definition (performs functions/services for a covered entity involving PHI); written
  contract generally required to safeguard PHI; subcontractors handling PHI for a business associate are business
  associates; HHS publishes sample provisions.
- FAQ 198: messages permitted, keep them minimal (name, number, what is needed to confirm an appointment).
- HHS minimum necessary requirement page exists and supports the "collect as little as possible" framing.
- Not a HIPAA compliance program; no clinical detail. OK.

## /ai-for/medical-offices.html: 9 claims checked, 2 corrected
Corrected:
- 911.gov definition paraphrased loosely; now matches the source: "any situation that requires immediate assistance
  from the police, fire department or ambulance".
- HHS FAQ 198 label fixed as on the dental page.
Confirmed:
- 988 Suicide and Crisis Lifeline: call or text 988 (988lifeline.org, samhsa.gov).
- BLS OOH Secretaries and Administrative Assistants: answer phones, take messages, transfer calls, schedule
  appointments; medical secretaries may take simple medical histories and process insurance payments.
- HHS minimum necessary, business associates and written agreement points (as above).
- Description of medical answering services is general, not a sourced claim. OK.

## /ai-for/salons.html: 7 claims checked, 2 corrected
Corrected:
- BLS self-employment year: the Occupational Outlook Handbook now uses 2025 data (BLS projections release of Aug 27
  2026, 2025-35 decade). The 48 percent self-employed share for hairdressers, hairstylists and cosmetologists is
  reported for 2025. Changed "in 2024" to "in 2025".
- Manicurists and pedicurists "about 210,100 jobs in 2024": superseded by the 2025 edition, and the current count
  could only be found on secondary sites (201,800), so the number was REMOVED. Kept the confirmed point that they
  mainly work in nail salons, spas and hair salons.
Confirmed:
- BLS: schedules often include evenings and weekends, the busiest times for shops and salons.
- IRS Publication 4902: a booth renter "leases space from an existing business and operates their own business as
  an independent contractor" (indexed copy is the 2-2011 edition, still on irs.gov).
- HighLevel help: Voice AI offers open times and confirms bookings during a live call; Call Transfer sends the call
  to a human at a phone number (the transfer article contrasts Call Transfer and Agent Transfer).

## /ai-for/restaurants.html: 7 claims checked, 1 corrected
Corrected:
- National Restaurant Association source URL normalized to the indexed address (www, no trailing slash) and the
  release date (February 12, 2026) added to the label.
Confirmed:
- NRA release title "Persistent Cost Increases and Enduring Demand Will Shape the Restaurant Industry in 2026"; page
  only restates the title. No NRA numbers are used.
- FDA nine major allergens (milk, eggs, fish, crustacean shellfish, tree nuts, peanuts, wheat, soybeans, sesame);
  sesame effective January 1, 2023 (FASTER Act).
- 2022 FDA Food Code: person in charge demonstrates knowledge of major food allergens and symptoms of a reaction, and
  ensures employees are trained in food allergy awareness as it relates to their assigned duties; Food Code applies
  only where adopted ("local adoption varies").
- HighLevel booking and transfer articles (as on salons).

## /ai-for/real-estate-agents.html: 10 claims checked, 2 corrected, 1 source added
Corrected:
- HighLevel calendar detail: "how many days ahead, how many slots to offer" could not be confirmed from the help
  article text found; softened to "the calendar settings you control, which decide which times can actually be
  booked" (the article says calendar settings control which times can be booked).
- Steering claim cited no source for HUD's regulation: added eCFR 24 CFR 100.70 (Other prohibited sale and rental
  conduct), which defines steering. Claim itself confirmed.
Confirmed:
- NAR 2025 Profile of Home Buyers and Sellers (released Nov 4 2025, transactions July 2024 to June 2025): 88% of
  buyers used an agent or broker. Confirmed through several reports of the Profile and NAR's own "nine in 10" press
  release subtitle; the exact 88% sentence was not seen on the nar.realtor press release itself.
- HUD "Fair Housing: Rights and Obligations" page (URL real): race, color, national origin, religion, sex, familial
  status and disability.
- FCC 24-17 (adopted Feb 2, released Feb 8 2024): TCPA artificial/prerecorded voice restrictions cover AI-generated
  voices; prior express consent absent an emergency purpose or exemption. Both FCC URLs real.
- FTC TSR DNC Q&A: a specific request not to be called must be honored, even with an established business
  relationship.

## Not checked
- Practice-area call timing table on the law page, the dental call types, salon menu durations and restaurant call
  types are descriptive industry framing with no source or number. Not checked as facts.
- The full text of each official page (not opened directly because of the sandbox), including the exact NAR 88%
  sentence and the current BLS manicurist count.

## Lead follow-up (Oct 15 2026)
- NAR 88%: confirmed by WebSearch limited to nar.realtor. NAR press release "First-Time Home Buyer Share Falls to Historic Low of 21%, Median Age Rises to 40" lists 88% of buyers purchased through an agent or broker (2025 Profile). Page unchanged.
