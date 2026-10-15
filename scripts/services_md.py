#!/usr/bin/env python3
"""Write SERVICES.md: every page, its URL, target keyword (volume / SEO difficulty), supporting keywords and the angle
it is written from. Keyword numbers come from docs/keywords.json (scripts/keyword_plan.py). Run after keyword_plan.py."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KW = json.loads((ROOT / "docs" / "keywords.json").read_text())

GROUPS = [
    ("Core pages", [
        ("/", "Home", "What Dominion AI Agency is (a small AI agency that does the setup), the call-the-line proof, the services in plain words, prices, texting status, industries, guides."),
        ("/services/", "Services overview", "Every service grouped by the job it does (answer the phone, answer the website, follow up and book, get found, plan), each with its price from INTAKE.md and a link."),
        ("/ai-for/", "Industries hub", "AI for small business, by trade: how the same tools change from a law office to a roofing crew; links to the nine industry pages; honest note on what AI does not fix."),
        ("/pricing/", "Pricing", "The three packages and five single services exactly as INTAKE.md lists them, what each line means, what is not promised (texting, setup time), how this compares with what the market publishes (link to the cost guide)."),
        ("/how-it-works/", "How it works", "From the first call to a working system, without setup-time promises; how an AI receptionist works on a call; where the agency works (all 50 states, remote; the old service-areas page lands here)."),
        ("/about/", "About", "Maurice Johnson, Dominion Digital Group, East Texas, Black-owned, started 2022: nothing more. Why HighLevel. What the agency is not."),
        ("/faq/", "FAQ", "General questions grouped: the phone line, texting, prices, setup, data, limits."),
        ("/contact/", "Contact", "Call first (hear the product), or the agency-contact form; email."),
        ("/tools/", "Tools", "HighLevel and ServiceTitan referral links with the disclosure, rewritten; the only page with referral links."),
    ]),
    ("Service pages", [
        ("/ai-receptionist/", "AI receptionist", "What an AI receptionist is and does on a real business line: greeting, questions it answers from your facts, messages, booking, transfers; what it does not do; hear ours on the main line."),
        ("/ai-receptionist-for-small-business/", "AI receptionist for small business", "The owner-operator angle: which small businesses it fits by call pattern, what 'best' means for a small shop (a buyer's checklist), what we set up for one, prices."),
        ("/ai-answering-service/", "AI answering service", "Answering service angle: after-hours and overflow answering, message taking, call forwarding from your existing number, AI answering compared with a staffed answering service."),
        ("/ai-voice-agent/", "AI voice agent", "The agent itself: inbound and outbound, one agent or several, customer service calls, the consent rules that govern outbound AI calls (FCC/TCPA), what we configure."),
        ("/ai-chatbot-agency/", "AI chatbot for website (and voice widget)", "The website side: a chat widget and a talking voice widget trained on your facts, lead capture, handoff, limits. Replaces the old talking-website page."),
        ("/missed-call-text-back/", "Missed call text back", "Honest page: what missed call text back is, why it is not live here yet (A2P 10DLC registration pending), what works today (the voice agent answers), consent and STOP rules, how to text back by hand meanwhile."),
        ("/ai-appointment-booking/", "AI appointment booking", "Booking by phone and chat into a calendar: availability rules, confirmations by email (text reminders once carrier approval clears), what booking software can connect is confirmed per client."),
        ("/ai-crm-automation/", "CRM automation", "Pipelines, automated email follow-up, lead nurturing, review requests and reporting on HighLevel; what marketing automation means for a small business. Replaces the old Dominion CRM System page."),
        ("/ai-workflow-automation/", "Business automation services", "Small business automation beyond the CRM: mapping the repeat tasks, workflows, internal notifications and handoffs; what to automate and what to leave to people."),
        ("/ai-consulting/", "AI consulting for small business", "What an AI consultant does for a small business, how we decide what to automate first, the questions we ask, what you get; no consulting price is published."),
        ("/ai-automation-agency/", "AI automation agency", "Dominion as an AI automation agency: what is included, how work is split between you and us, why HighLevel, packages."),
        ("/ai-lead-generation/", "AI marketing agency (lead generation)", "AI lead generation, review management, social media automation, websites and SEO pages, priced from INTAKE.md; review requests by email now and by text once carrier approval clears."),
    ]),
    ("Industry pages", [
        ("/ai-for/law-firms.html", "Law firms", "Intake: who calls a firm and when, what the intake agent collects, the ethics guardrails (no legal advice, no attorney-client relationship, conflict checks stay with staff, ABA guidance on AI)."),
        ("/ai-for/hvac-companies.html", "HVAC companies", "Seasonal peaks and no-heat / no-cool calls, triage questions, maintenance agreements, dispatch software stays in charge."),
        ("/ai-for/dentists.html", "Dentists", "New-patient and overflow calls, insurance questions, recall; not a HIPAA compliance program, no clinical detail, practice software connection confirmed per office."),
        ("/ai-for/salons.html", "Salons", "Hands-busy booking, service menus and durations, consultations for color and extensions, no-shows and cancellations, booking software checked first."),
        ("/ai-for/contractors.html", "Contractors", "Estimate requests from the job site, scope questions, no pricing sight unseen, electricians and general contractors."),
        ("/ai-for/restaurants.html", "Restaurants", "Service-hour calls: hours, reservations, catering and large parties; works beside the reservation system; no payment taking promised."),
        ("/ai-for/real-estate-agents.html", "Real estate agents", "Buyer and seller inquiries, showing requests, speed to answer, Fair Housing guardrails, outbound consent rules."),
        ("/ai-for/plumbers.html", "Plumbers", "Emergency calls at all hours, triage (active leak or not), dispatch handoff, home service businesses."),
        ("/ai-for/medical-offices.html", "Medical offices", "Scheduling and general calls only, emergency instruction to call 911, not a HIPAA compliance program, business associate questions answered honestly."),
    ]),
    ("Guides", [
        ("/how-much-does-an-ai-receptionist-cost/", "Cost guide", "Published market price models and ranges (cited, real quotes vary), receptionist wages from BLS, answering service pricing models, and Dominion's own prices from INTAKE.md only."),
        ("/ai-receptionist-vs-answering-service/", "AI receptionist vs answering service vs hiring", "What a receptionist does (BLS), what a staffed answering service does, what an AI receptionist does; a side-by-side table; which fits which business."),
        ("/is-an-ai-receptionist-worth-it/", "Worth it?", "A decision guide: when it pays, when it does not, accuracy and limits, how to test one before you buy (call ours)."),
        ("/what-is-an-ai-agency/", "What is an AI agency", "Definition, what an AI automation agency does day to day, how it differs from software and from a marketing agency, what a small business should expect."),
        ("/how-to-choose-an-ai-agency/", "How to choose (best AI agency)", "Questions to ask, red flags (FTC actions on deceptive AI claims), who owns the account and phone number, contracts, data."),
    ]),
]


def main():
    out = ["# SERVICES.md: page plan for dominionaiagency.com", "",
           "Written before the pages (CLAUDE.md). One page per intent cluster; no two pages share a target. Volumes are",
           "monthly US searches / SEO difficulty from keywords/AI-Agency-Keywords.xlsx (Ubersuggest, Oct 15 2026), verified by",
           "scripts/keyword_plan.py. The full assignment, including every deliberately unused row, is docs/keyword-plan.md.", ""]
    total = 0
    for title, pages in GROUPS:
        out += [f"## {title} ({len(pages)})", ""]
        for url, name, angle in pages:
            total += 1
            k = KW.get(url, {})
            t = k.get("target")
            tline = f"{t} ({k['target_vol']:,}/{k['target_sd']})" if t and k.get("target_vol") else (f"{t} (no row in the data; see keyword-plan.md)" if t else "none (support page)")
            sup = "; ".join(f"{s['kw']} ({s['vol']:,}/{s['sd']}{', Q' if s['question'] else ''})" for s in k.get("supporting", [])) or "none"
            out += [f"### {name}: `{url}`", f"- Target: {tline}", f"- Supporting: {sup}", f"- Angle: {angle}", ""]
    out += ["## Not keyword pages", "", "- /contact/thanks/ (noindex), /privacy-policy/, /terms/, /404.html (noindex)", "",
            f"Total pages with a keyword plan: {total}; with thanks, privacy, terms and 404: {total + 4}.", ""]
    (ROOT / "SERVICES.md").write_text("\n".join(out))
    print("wrote SERVICES.md", total)


if __name__ == "__main__":
    main()
