# Decisions (made without Maurice, per CLAUDE.md "run straight through")

Oct 15 2026. Each one can be reversed later; none costs money, deploys, merges or touches another repository.

- D1. Build system: the static Jinja2 system from Water Damage Pro Dallas (59b7e0a) instead of GHL AI Studio's SSR
  master, because CLAUDE.md says so and the repo is static. Playbook prompts are applied to it; "SSR" checks become
  raw-HTML checks of dist/.
- D2. Page list: 39 pages. 35 keyword pages (9 core including /tools/, 12 service, 9 industry, 5 guide) plus thanks,
  privacy, terms and 404. Decided from docs/keyword-plan.md; one target per page, none shared.
- D3. Home targets "ai agency" (49,500/27): the brand is literally an AI agency for small businesses. "ai automation
  agency" (4,400/13) goes to the existing /ai-automation-agency/ URL. "what is an ai agency" (9,900/24) gets its own guide.
- D4. Old service URLs kept as live pages where a page still fits: /ai-automation-agency/, /ai-chatbot-agency/ (AI
  chatbot for website + the voice widget), /ai-consulting/, /ai-crm-automation/ (CRM automation),
  /ai-workflow-automation/ (business automation services), /ai-lead-generation/ (AI marketing agency: lead
  generation, reviews, social, websites). Keeping them live means the existing `/x/* -> /x/` wildcards keep catching
  the ~5,800 retired city pages without redirect loops or extra hops.
- D5. /ai-marketing-agency/ cannot be used as a URL: the current _redirects sends it to /ai-automation-agency/ and every
  rule must stay. The AI marketing agency target therefore lives on /ai-lead-generation/.
- D6. The six /ai-for/*.html URLs and /tools/ are kept exactly. New industry pages follow the same pattern
  (/ai-for/real-estate-agents.html, plumbers.html, medical-offices.html) so the section stays consistent.
- D7. Retired single pages: /talking-website.html -> /ai-chatbot-agency/, /dominion-crm-system.html ->
  /ai-crm-automation/, /service-areas.html -> /how-it-works/ (which carries the "where we work" section). Extensionless
  forms (/talking-website etc.) get the same rules. Rules are added above the old ones; no old rule is removed.
- D8. Industries chosen from the data: law firms (1,600), restaurants (720), real estate agents (590), dentists (170 +
  170 + 170), contractors (110), medical offices (90 + 110 voice agent for healthcare), salons (50 + 50), HVAC (40 + 30 +
  30), plumbers (40). Med spas, veterinary, hotels, property management, electricians on their own: under 10 or only 10
  a month; electricians fold into contractors, property management into real estate.
- D9. The comparison guide (AI receptionist vs answering service vs hiring) has no row in the data; CLAUDE.md asks for
  it, so it is built and recorded as a zero-volume target.
- D10. "hipaa compliant ai receptionist" (40) is deliberately unused: INTAKE.md forbids the claim. The medical and
  dental pages explain plainly that the service is not a HIPAA compliance program.
- D11. Industry and business software is named by category ("your practice management software", "your booking
  system"). ServiceTitan and HighLevel may be named (INTAKE.md) without links; referral links stay only on /tools/.
  Other product names appear only in guides as cited market information.
- D12. Consulting has no price in INTAKE.md, so no consulting price is shown anywhere.
- D13. Color bands: black (#0b0b0c) for the header, footer, first band and call band; gold (#f5a623, the logo gold)
  for the FAQ band with black text. Gold text only on black. White everywhere else.
- D14. The contact form is the only form on the site (Netlify "agency-contact", fields per INTAKE.md, honeypot), copied
  from the Dallas Roofing Pro pattern. No SMS consent checkbox.
- D15. Phone CTA label: "Call (903) 636-7511" built from site.json; secondary hero CTA is page-specific.
- D16. Photos: generic photos copied (read-only) from Dominion Web Design Pro, Houston and Dallas HVAC Pro, Dallas
  Roofing Pro and Water Damage Pro Dallas, renamed with new alt text for this site (docs/photos.json). Pages that
  need a subject no reused photo shows (salons, dental, restaurants, medical, real estate) name a new file in
  docs/image-reuse.json; until Artistly makes it, a crop of a reused photo stands in under the same name.
