# Independent fact-check (Oct 15 2026)

Six sub-agents that did not write the pages checked every factual claim and source on every page (brief:
docs/fact-check/BRIEF.md). Logs: docs/fact-check/fc1.md to fc6.md.

| Checker | Pages | Claims checked |
|---|---|---:|
| fc1 | /, /ai-receptionist/, /ai-receptionist-for-small-business/, /ai-answering-service/, /how-it-works/, /about/, /tools/ | 78 |
| fc2 | /ai-voice-agent/, /ai-chatbot-agency/, /ai-appointment-booking/, /missed-call-text-back/, /faq/, /contact/, /contact/thanks/, /privacy-policy/, /terms/ | 110 |
| fc3 | /ai-crm-automation/, /ai-workflow-automation/, /ai-consulting/, /ai-automation-agency/, /ai-lead-generation/, /services/, /pricing/ | 112 |
| fc4 | /ai-for/, law firms, dentists, medical offices, salons, restaurants, real estate agents | 66 |
| fc5 | HVAC, plumbers, contractors, /what-is-an-ai-agency/, /how-to-choose-an-ai-agency/ | 144 |
| fc6 | /how-much-does-an-ai-receptionist-cost/, /ai-receptionist-vs-answering-service/, /is-an-ai-receptionist-worth-it/ | 46 |
| Total | 37 content pages (404 has no claims) | 556 |

About 60 corrections were made in place. The ones that matter most:
- Review management was described as in every package; INTAKE.md has it in AI Starter and AI Pro only (fixed on the CRM page,
  and removed from AI Empire in site.json). Outbound calls are AI Pro only, not "Pro and above".
- HighLevel features were narrowed to what its help center documents (no message fallback after an unanswered transfer,
  the voice widget is beta without call transfer, Won/Lost are statuses not stages, iCloud sync is one-way).
- Vendor prices in the cost guide were corrected or removed where the vendor's own page did not confirm them (Goodcall plan,
  Ruby rounding, Retell chat rate); the guide says prices change and real quotes vary.
- Outdated sources replaced with current ones (FTC contractor pages, CPSC carbon monoxide advice, CTIA 2023 principles, ESFI's
  own page, Cochrane review URL); the BLS salon figure moved to the 2025 data year.
- Claims about sister-brand ownership removed (not in INTAKE.md). "Most agencies" claims softened.

Limit of this check, stated plainly: outbound page fetches (WebFetch, curl) are blocked in this sandbox, so every claim was
verified through web search restricted to the official or vendor domain, not by loading the page. Nothing was marked
verified that the search results did not support; the few items not fully checked are listed in each log, and two general
statements that could not be sourced were rewritten so they state no fact.
