# Fact-check log: fc5 (Oct 15 2026)

Independent checker; did not write these pages. Method: WebFetch and curl to outside hosts are blocked in
this sandbox (WebFetch to eia.gov failed with ENOTFOUND), so every claim below was checked with WebSearch,
restricted with allowed_domains to the official site (eia.gov, energystar.gov, cpsc.gov, phmsa.dot.gov,
epa.gov, bls.gov, consumer.ftc.gov, ftc.gov, esfi.org, fcc.gov, census.gov, nist.gov, ibm.com, sba.gov,
campaignregistry.com, help.gohighlevel.com), and judged from the search result text from those pages.
Business claims were checked against INTAKE.md.

After edits: `build.py --out /tmp/fc5-dist` built 39 pages; `check.py --skip-links --only <url>` shows
0 errors for all five pages (one informational WARN on HVAC about the EIA 88% figure, which is cited in
Sources); `similarity.py --only <url>` shows no FAIL (max 2.1% within the site, 0.0 to 0.2% against both
sister sites).

## /ai-for/hvac-companies.html (16 claims checked)

CORRECTED
- CPSC carbon monoxide advice. The page said "call 911 from a fresh-air location" and cited an old CPSC
  talking points PDF (blk_pdf_Talking_Points.pdf). That PDF exists but is old media talking points. CPSC's
  current wording (2026 winter weather release; CO fact sheet) is: never ignore an alarm, get outside
  immediately, then call 911 (fact sheet: call from outside). Changed the sentence to that wording and
  replaced the source with the 2026 CPSC release and the CPSC CO fact sheet.
- HighLevel source URL slug updated to the article's current URL (155000003911-ai-voice-agents-overview);
  same article ID.

CONFIRMED
- EIA, 2020 RECS: 88% of U.S. households use air conditioning (Today in Energy id=52558; EIA's headline
  rounds to "nearly 90%", the body text states 88%). Stated exactly; cited.
- ENERGY STAR maintenance checklist: contractors get busy once summer and winter come, so check cooling in
  spring and heating in fall. Matches the page (both mentions).
- PHMSA: for a suspected gas leak, leave the area first and call 911 from a safe location (neighbor's
  house or other location well away from the leak). Matches "leave first, call from a safe distance".
- HighLevel Voice AI: Call Transfer action sends the caller to a human phone number (Voice AI agent
  transfer article); agents answer calls, book appointments, trigger workflows and webhooks (overview and
  appointment-booking articles). Supports the transfer and "pass call details along through workflows" lines.
- Prices $297, $597, $1,097 and package contents match INTAKE.md; setup, training and support included.
- Texting described as not live (FAQ and texting_note); outbound calling only on AI Pro, per INTAKE.md.
- Field service software connection described as confirmed per client; "ServiceTitan" appears only as a
  search phrase with no integration claim.
- No team, client, result, setup-time or "never misses" claims found.

NOT CHECKED
- None of the cited facts; the triage table and checklist are the agency's own process descriptions, not
  factual claims.

## /ai-for/plumbers.html (12 claims checked)

CORRECTED
- BLS wording. The page said plumbers "often work nights and weekends". BLS OOH says "Most plumbers,
  pipefitters, and steamfitters work full time, including nights and weekends. They are often on call to
  handle emergencies." Changed to "most plumbers work full time, including nights and weekends, and are
  often on call to handle emergencies."
- HighLevel source URL slug updated (same article ID).

CONFIRMED
- PHMSA gas leak advice: leave, call 911 from a neighbor's house or another location well away from the
  leak, and do not use phones or switches near it. Matches the page.
- EPA WaterSense: household leaks can waste nearly 1 trillion gallons of water annually nationwide (current
  Fix a Leak Week page wording; older EPA pages said "more than 1 trillion"). Stated as the current page
  states it; cited.
- HighLevel call transfer to a human phone number (two mentions).
- Prices and package contents match INTAKE.md; texting not live stated in FAQ and texting_note; software
  connection confirmed per client; no arrival-time or setup-time promises.

NOT CHECKED
- None of the cited facts.

## /ai-for/contractors.html (14 claims checked)

CORRECTED
- FTC "demand for qualified contractors usually exceeds the supply". That line exists only in a 2003 FTC
  press release; I could not find it on any current consumer.ftc.gov page. Replaced the sentence with what
  the current FTC pages say: ask for IDs, licenses and proof of insurance before paying (How to avoid scams
  after weather emergencies and natural disasters) and a contractor knocking because they are "in the
  area" is a warning sign (Home repair scams). Replaced the 2003 release source with the current
  consumer.ftc.gov disaster page and added the Home repair scams page.
- FTC "Hiring a Contractor" brochure (govinfo PDF, old) replaced with the current consumer.ftc.gov article
  "How to avoid a home improvement scam", which supports both statements on the page: get estimates from
  more than one contractor, and do not just pick the lowest bid but ask for an explanation if there is a
  big difference in price. Sentence reworded to name that article.
- ESFI downed power line source: replaced the Safety+Health magazine article with ESFI's own page
  ("Downed power line safety: always assume downed lines are live"), which says to stay away and call 911.
- HighLevel source URL slug updated (same article ID).

CONFIRMED
- BLS OOH Roofers: "In northern states, roofing work may be limited during the winter months. During the
  busy summer months, roofers may work overtime to complete jobs." Matches the page.
- ESFI: stay away from a downed line and call 911. Matches the page (table and paragraph).
- Prices $297, $597, $1,097 and AI Pro contents (outbound calling, full CRM automation, AI lead generation,
  a website) match INTAKE.md. Texting not live stated in texting_note. Demo link is the INTAKE.md CTA.
- No competitor names, no team or results claims, no setup-time promises; software connection confirmed
  per client.

NOT CHECKED
- None of the cited facts.

## /what-is-an-ai-agency/ (13 claims checked)

CORRECTED
- IBM automation definition. The page quoted IBM as defining automation as "the completion of tasks without
  human intervention" and cited IBM's AI orchestration page. IBM's own wording that comes closest is in
  "Automation vs. orchestration": automation uses technology to run defined, repetitive tasks with minimal
  or no human intervention. Changed the sentence to that wording and replaced the source with that page.
- HighLevel source URL slug updated (same article ID).

CONFIRMED
- NIST AI 100-1 (AI RMF 1.0): an AI system is "an engineered or machine-based system that can, for a given
  set of objectives, generate outputs such as predictions, recommendations, or decisions". Matches.
- IBM: intelligent automation is the combination of AI and automation technologies (What is intelligent
  automation?). Matches the body text and the FAQ.
- U.S. Census Bureau, May 2026 story "Large firms with at least 20 employees biggest AI users" (BTOS):
  overall business AI use hovered between 17% and 20% from December 2025 to May 2026; use increased at
  firms with at least 20 employees and showed no significant change at firms with fewer than 20. Matches.
- SBA AI for small business: "start small" and many AI tools offer basic services free or at lower cost;
  test them. Matches.
- FTC, Sept. 25, 2024, Operation AI Comply: actions against companies using AI hype or selling AI tools
  used to deceive; Chair Khan: "there is no AI exemption from the laws on the books." Matches.
- Business facts (East Texas, Dominion Digital Group, all 50 states, HighLevel, Maurice Johnson configures
  each one, prices on the pricing page, texting note) match INTAKE.md.

NOT CHECKED
- "Nearly all [AI automation agencies] charge a monthly fee ... sometimes with a setup charge" is a general
  market characterization with no source; I did not verify it (left as a general description, no number).

## /how-to-choose-an-ai-agency/ (17 claims checked)

CORRECTED
- Air AI settlement. The page said the March 2026 settlement "bans" the company and owners. The FTC
  release (Mar. 24, 2026) describes a proposed stipulated order under which they "will be banned" from
  marketing business opportunities. Reworded to "Under a settlement announced in March 2026, the company
  and its owners will be banned from marketing business opportunities," and the source label to match.
- Automators AI (Feb. 2024). The page said the owners "agreed to a ban on offering business opportunities"
  and that "most clients" did not make promised earnings. The FTC release says each defendant other than
  one individual and his company is permanently banned from offering business opportunities or coaching
  related to online marketplace e-commerce, and alleges the "vast majority" of clients did not make the
  promised earnings or even recoup their investment. Reworded to match.

CONFIRMED
- Operation AI Comply announced Sept. 25, 2024, five actions, including multiple companies claiming AI
  could help consumers make money through online storefronts; Chair Lina Khan: "Using AI tools to trick,
  mislead, or defraud people is illegal." Matches.
- FTC Aug. 2025 suit against a seller of AI agent software (Air AI): deceptive claims about business
  growth, earnings potential and refund guarantees; consumers, many of them small business owners, lose as
  much as $250,000. Matches. The company is not named in visible copy (only in the ftc.gov URL slug).
- FTC Consumer Reviews and Testimonials Rule: announced Aug. 14, 2024, in effect Oct. 21, 2024; bans fake
  reviews including AI-generated reviews attributed to people who do not exist. Matches body and FAQ.
- FTC Business Opportunity Rule: sellers must give a one-page disclosure document and, if they make
  earnings claims, a separate earnings claim statement. Matches.
- FCC Declaratory Ruling FCC 24-17 (adopted Feb. 2, released Feb. 8, 2024): AI-generated voices are
  "artificial" voices under the TCPA, so such calls need prior express consent absent an emergency purpose
  or exemption. Page says "generally require"; matches.
- FCC porting guide: you can usually keep your number when switching providers in the same geographic
  area. Matches "generally keep your number ... in the same area".
- The Campaign Registry: 10DLC brand and campaign registration for business texting, done through a
  messaging provider. Supports the A2P 10DLC line.
- Business facts: AI receptionist on the main line, prices published, HighLevel, Maurice sets up each
  system, no published standard contract terms, texting note. All consistent with INTAKE.md. No competitor
  names in visible copy.

NOT CHECKED
- "Many [ranking lists] are written by companies that earn a fee from the firms they rank, or by the
  agencies themselves" is a general observation with no source; not verified (no number attached).

## Totals
5 pages, 72 claims checked, 12 corrections (including 4 HighLevel URL slug updates and 6 source
replacements), 0 claims removed outright, 2 general statements not checked.
