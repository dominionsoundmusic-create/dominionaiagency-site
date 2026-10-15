# Independent fact-check brief (Dominion AI Agency, Oct 15 2026)

You are an independent fact-checker. You did NOT write these pages. Repo: /home/user/dominionaiagency-site.
Read CLAUDE.md, INTAKE.md and docs/WRITING-GUIDE.md first (rules, and the business facts that are already confirmed
by INTAKE.md: name, d/b/a, founder, 2022, East Texas, Black-owned, prices, texting not live, HighLevel).

For EACH page assigned to you (src/pages/<file>.html, plus its notes in docs/research/ when they exist):
1. List every factual claim on the page that is not common knowledge and not an INTAKE.md fact: numbers, statistics,
   dates, laws and regulations (TCPA, FCC rulings, CAN-SPAM, HIPAA, Fair Housing, ABA opinions), what a government
   source or association says, what HighLevel's product does, market prices and vendor plans (guides), wages, and what
   each cited source says. Include the FAQ answers in the front matter.
2. Verify claims with WebSearch against official or primary sources (fcc.gov, ftc.gov, hhs.gov, hud.gov, bls.gov,
   census.gov, americanbar.org, nar.realtor, energystar.gov, ctia.org, help.gohighlevel.com, vendor pricing pages).
   WebFetch may not reach outside sites here; judge from search results when it fails. Combine claims per query.
3. Check every statistic is stated exactly as the source states it (number, population, year), and that it is in the
   page's m.sources list. Check each source in m.sources is real and supports something on the page; remove ones you
   cannot confirm.
4. Check the business claims against INTAKE.md: only INTAKE.md prices; no team, staff, engineers, client counts,
   results, reviews, awards, certifications, partnerships; no setup or response time promises; texting described as
   not live wherever it appears; no "never misses a call", "replaces your staff", "works perfectly"; no competitor
   names outside the guides; no claims of integrations that are not "confirmed per client"; HighLevel features
   described only as HighLevel documents them.
5. FIX the page directly: correct wrong facts; remove or soften claims you cannot verify (leave it out rather than
   guess); never add new unverified facts. Keep the page's keyword targeting and length roughly intact.
6. Keep the page valid after edits: `python3 build.py --out /tmp/<yourname>-dist && python3 scripts/check.py
   --dist /tmp/<yourname>-dist --skip-links --only <url>` must show 0 errors for your pages, and
   `python3 scripts/similarity.py --dist /tmp/<yourname>-dist --only <url>` no FAIL for your pages.
7. Write your log to docs/fact-check/<yourname>.md: per page, the number of claims checked, each claim CORRECTED or
   REMOVED with the reason and source, claims confirmed, and claims you could not check (say "not checked", never
   "verified" for those).

Do not edit shared files (templates, CSS, site.json, scripts) or pages not assigned to you. Do not commit.
Finish with a short report: pages done, corrections made, what remains unchecked.
