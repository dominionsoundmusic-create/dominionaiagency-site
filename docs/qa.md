# QA record (Oct 15 2026, final build)

| Check | Command | Result |
|---|---|---|
| Build | `python3 build.py` | 39 pages, 0 failures |
| Rules + SEO + links + images + JSON-LD + forms | `python3 scripts/check.py` | 0 errors, 14 warnings (7 cited statistics on non-guide pages, 7 cited vendor names in guides) |
| Old URLs | `python3 scripts/check_old_urls.py` | 101 old URLs and rules checked, 0 problems (docs/qa-urls.md) |
| CLAUDE.md grep list | `python3 scripts/grep_check.py` | 0 hits |
| Duplication | `python3 scripts/similarity.py` | max 5.9% between pages here (pricing vs home, shared price cards); max 1.8% vs Dominion Web Design Pro; max 0.6% vs AI Voice Agent Pros; no shared 8-word runs (docs/qa-similarity.md) |
| Responsive | `node scripts/responsive_check.js` | 0 overflow, 0 row holes, 0 broken images on all pages at 390, 768, 1024, 1440, 1920 |
| Screenshots | `node scripts/responsive_check.js --shots / /ai-receptionist/ /missed-call-text-back/` | Looked at each section at 1440, 1920 and 2560: hero content on the left rail, call button visible, black header with gold, white sections with black and gold bands, no white on white, rows centered, footer links in rows, stand-in photos showing (no broken images) |
| Form | check.py | exactly one Netlify form, "agency-contact", only on /contact/, fields form-name, bot-field, name, business, email, phone (optional), message; no checkbox; thanks page /contact/thanks/ (noindex) |
| Texting | check.py | every page whose body mentions texting carries "Texting is not live yet"; the footer carries it on every page |
| Fact-check | docs/fact-check.md | 556 claims checked by 6 independent sub-agents |

Duplication detail by group (Jaccard, 5-word shingles): guide pairs max 1.6%, industry max 2.1%, service max 3.4%,
core pages max 1.4%, mixed max 5.9%. Carrier-required SMS wording and the legal d/b/a line are exempt from the 8-word
run check (identical by design across Dominion sites).

Not verified here: real form submission to Netlify (not deployed; Maurice decides go-live), Google Translate in a live
browser session (requires the live domain), GA4 events in the GA4 property.
