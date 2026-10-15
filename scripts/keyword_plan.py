#!/usr/bin/env python3
"""Assign every keyword with a volume of 10 or more in keywords/AI-Agency-Keywords.xlsx (ALL tab) to a page as
its target or a supporting keyword, or to a deliberately-unused group with a one-line reason.
Writes docs/keyword-plan.md and docs/keywords.json (page -> target + supporting rows, read when writing pages).

CLAUDE.md: every BUYER keyword (a small business owner looking for someone to set up AI for them, or for an AI
receptionist / answering / chat / automation service) with a volume of 10+ is assigned or listed as unused with
a reason. Non-buyer rows (jobs, courses, DIY tools, named products, news, enterprise, other countries, off-topic)
are summarized by group. One page per intent cluster: no two pages share a target.

Rules run in order: explicit page map, unused groups, then page patterns. A row that matches nothing makes the
script exit 1 and print it, so every row 10+ is decided by hand.

Usage: python3 scripts/keyword_plan.py
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent

PAGES = {
    "home": "/", "services": "/services/", "industries": "/ai-for/", "pricing": "/pricing/",
    "how": "/how-it-works/", "about": "/about/", "faq": "/faq/", "contact": "/contact/", "tools": "/tools/",
    "receptionist": "/ai-receptionist/", "receptionist-sb": "/ai-receptionist-for-small-business/",
    "answering": "/ai-answering-service/", "voice": "/ai-voice-agent/", "chatbot": "/ai-chatbot-agency/",
    "mctb": "/missed-call-text-back/", "booking": "/ai-appointment-booking/", "crm": "/ai-crm-automation/",
    "bizauto": "/ai-workflow-automation/", "consulting": "/ai-consulting/", "agency": "/ai-automation-agency/",
    "marketing": "/ai-lead-generation/",
    "law": "/ai-for/law-firms.html", "hvac": "/ai-for/hvac-companies.html", "dental": "/ai-for/dentists.html",
    "salon": "/ai-for/salons.html", "contractor": "/ai-for/contractors.html", "restaurant": "/ai-for/restaurants.html",
    "realestate": "/ai-for/real-estate-agents.html", "plumber": "/ai-for/plumbers.html",
    "medical": "/ai-for/medical-offices.html",
    "g-cost": "/how-much-does-an-ai-receptionist-cost/", "g-vs": "/ai-receptionist-vs-answering-service/",
    "g-worth": "/is-an-ai-receptionist-worth-it/", "g-what": "/what-is-an-ai-agency/",
    "g-choose": "/how-to-choose-an-ai-agency/",
}
TARGETS = {
    "home": "ai agency", "services": "ai agency services", "industries": "ai for small business",
    "pricing": "ai automation agency pricing", "how": "how does ai receptionist work",
    "receptionist": "ai receptionist", "receptionist-sb": "ai receptionist for small business",
    "answering": "ai answering service", "voice": "ai voice agent", "chatbot": "ai chatbot for website",
    "mctb": "missed call text back", "booking": "ai appointment booking", "crm": "crm automation",
    "bizauto": "business automation services", "consulting": "ai consulting for small business",
    "agency": "ai automation agency", "marketing": "ai marketing agency",
    "law": "ai for law firms", "hvac": "ai receptionist for hvac", "dental": "dental ai receptionist",
    "salon": "ai receptionist for salons", "contractor": "ai for contractors", "restaurant": "ai for restaurants",
    "realestate": "ai for real estate agents", "plumber": "ai receptionist for plumbers",
    "medical": "ai receptionist for medical office",
    "g-cost": "how much does an ai receptionist cost", "g-vs": "ai receptionist vs answering service",
    "g-worth": "is ai receptionist worth it", "g-what": "what is an ai agency", "g-choose": "best ai agency",
}
# Target rows that are not in the data (volume 0 / not pulled): decided by CLAUDE.md's page list, recorded here.
TARGET_NOT_IN_DATA = {"g-vs": "CLAUDE.md asks for this comparison guide; Ubersuggest returned no row for any 'vs' phrasing of it."}

EXPLICIT = {  # keyword -> page key (supporting), decided by hand
    # home
    "ai agency near me": "home", "ai agency for small business": "home", "ai agency for business": "home",
    "ai agency usa": "home", "the ai agency": "home", "automated ai agency": "home", "ai agency automation": "home",
    "automation ai agency": "home", "ai services near me": "services", "ai agency solutions": "services",
    "ai agency consulting": "consulting", "ai agency group": "home",
    # agency guide / choose guide
    "what is an ai agency": "g-what", "what is ai agency": "g-what", "what's an ai agency": "g-what",
    "what is a ai agency": "g-what", "what is an ai automation agency": "g-what", "what is ai automation agency": "g-what",
    "what is a ai automation agency": "g-what", "what does an ai agency do": "g-what", "ai agency meaning": "g-what",
    "what is an ai agency and how does it work": "g-what", "what is ai automation": "g-what",
    "how ai automation agency works": "g-what", "ai automation agency explained": "g-what",
    "what is ai services": "g-what", "is ai a form of automation": "g-what",
    "best ai agency": "g-choose", "top ai agency": "g-choose", "top ai automation agency": "g-choose",
    "is ai automation agency legit": "g-choose", "is ai automation agency worth it": "g-choose",
    "ai automation agency examples": "g-choose", "ai automation companies": "g-choose",
    "ai automation companies near me": "g-choose", "ai automation agency near me": "agency",
    "ai automation agency services": "agency", "ai automation agency in usa": "agency", "ai automation agency usa": "agency",
    "ai automation agency business": "agency", "ai automation agency chatbot": "chatbot",
    "ai automation agency lead generation": "marketing", "ai automation agency pricing": "pricing",
    "how much does ai cost": "pricing", "ai voice agent pricing": "pricing", "ai consulting rates": "consulting",
    "how much do ai consultants charge": "consulting", "ai consultant hourly rate": "consulting",
    # receptionist
    "artificial intelligence receptionist": "receptionist", "ai receptionist services": "receptionist",
    "ai receptionist software": "receptionist", "ai receptionist service": "receptionist", "virtual ai receptionist": "receptionist",
    "24 7 ai receptionist": "receptionist", "voice ai receptionist": "receptionist", "front desk ai receptionist": "receptionist",
    "what is an ai receptionist": "receptionist", "what is ai receptionist": "receptionist", "ai receptionist meaning": "receptionist",
    "ai receptionist near me": "receptionist", "ai receptionist demo": "receptionist", "ai receptionist agency": "receptionist",
    "ai receptionist companies": "receptionist", "ai receptionist for business": "receptionist", "ai receptionist business": "receptionist",
    "gohighlevel ai receptionist": "receptionist", "go high level ai receptionist": "receptionist",
    "ai receptionist gohighlevel": "receptionist", "personal ai receptionist": "receptionist", "ai receptionist website": "chatbot",
    "how does ai receptionist work": "how", "how does an ai receptionist work": "how", "can ai answer phone calls": "g-worth",
    "ai receptionist for small business": "receptionist-sb", "best ai receptionist for small business": "receptionist-sb",
    "best ai receptionist": "receptionist-sb", "ai receptionist small business": "receptionist-sb",
    "what is the best ai receptionist": "receptionist-sb", "top ai receptionist": "receptionist-sb",
    "best ai receptionist software": "receptionist-sb", "ai virtual assistant for small business": "receptionist-sb",
    "ai voice agent for small business": "receptionist-sb", "ai assistant for small business owners": "receptionist-sb",
    "ai receptionist reviews": "g-choose", "ai receptionist for home services": "plumber",
    "is ai receptionist worth it": "g-worth", "how often is ai incorrect": "g-worth", "are ai answers accurate": "g-worth",
    "are ai answers always correct": "g-worth", "will ai replace customer service": "g-vs", "what is receptionist do": "g-vs",
    "ai receptionist cost": "g-cost", "ai receptionist pricing": "g-cost", "how much does an ai receptionist cost": "g-cost",
    "cost of ai receptionist": "g-cost", "how much is ai receptionist": "g-cost", "cheapest ai receptionist": "g-cost",
    "cheap ai receptionist": "g-cost", "ai answering service cost": "g-cost", "ai chatbot cost": "g-cost", "how much chatbot cost": "g-cost",
    # answering
    "ai phone answering service": "answering", "business answering phone service": "answering",
    "ai answering service for business": "answering", "ai answering service for small business": "answering",
    "best ai answering service": "answering", "ai answering services": "answering", "what is answering service": "answering",
    "best ai answering service for small business": "answering", "ai voice answering service": "answering",
    "best ai phone answering service": "answering", "ai business phone answering service": "answering",
    "ai telephone answering service": "answering", "how does an answering service work": "answering",
    "ai business answering service": "answering", "ai after hours answering service": "answering",
    "ai phone answering service for small business": "answering", "what is call answering service": "answering",
    "what is phone answering service": "answering", "ai business phone": "answering", "ai business phone assistant": "answering",
    "business automated phone answering system": "answering", "automated business voicemail greeting": "answering",
    "how to set up ai answering service": "how",
    # voice
    "conversational ai voice agent": "voice", "ai voice agent services for businesses": "voice", "ai voice agent for business": "voice",
    "ai voice agent business": "voice", "what is an ai voice agent": "voice", "what are ai voice agents": "voice",
    "how ai voice agents work": "voice", "what is voice agent": "voice", "ai voice agent for customer service": "voice",
    "ai voice agent for customer support": "voice", "outbound ai voice agent": "voice", "ai voice agent outbound calls": "voice",
    "ai voice agent service": "voice", "ai voice agent agency": "voice", "voice ai agency": "voice", "conversational ai agency": "voice",
    "ai voice agent companies": "voice", "ai voice agent for sales": "voice", "ai voice agent appointment setter": "booking",
    "ai voice agent call": "voice", "custom ai voice agent": "voice", "gohighlevel ai voice agent": "voice",
    "go high level ai voice agent": "voice", "ai for customer service": "voice", "ai agent phone": "voice",
    "can ai agents make phone calls": "voice", "ai voice agent for cold calling": "voice", "local ai voice agent": "voice",
    "multi language ai voice agent": "voice", "ai agent voice": "voice", "what is ai voice assistant": "voice",
    "what is ai calling": "voice", "autonomous ai customer service": "voice", "ai voice agent roi calculator": "g-worth",
    "ai voice agent for healthcare": "medical", "ai voice agent for real estate": "realestate", "ai voice agent real estate": "realestate",
    "ai voice agent for restaurant": "restaurant", "ai voice agent for restaurants": "restaurant", "voice ai for restaurants": "restaurant",
    "servicetitan ai voice agent": "hvac", "service titan ai voice agent": "hvac",
    # chatbot
    "ai chat for website": "chatbot", "ai chatbot for my website": "chatbot", "ai chatbot on website": "chatbot",
    "ai chatbot for your website": "chatbot", "best ai chatbot for website": "chatbot", "ai bot for website": "chatbot",
    "custom ai chatbot for website": "chatbot", "ai live chat for website": "chatbot", "ai powered chatbot for website": "chatbot",
    "ai chatbot widget for website": "chatbot", "ai bot on website": "chatbot", "ai chat with website": "chatbot",
    "chatbot for small business": "chatbot", "ai chatbot for small business": "chatbot", "best chatbot for small business": "chatbot",
    "best ai chatbot for small business": "chatbot", "small business chatbot": "chatbot", "chatbot for your business": "chatbot",
    "chatbot for small business owners": "chatbot", "ai chatbot companies": "chatbot", "ai chatbot benefits": "chatbot",
    "ai chatbot for customer service": "chatbot", "chatbot vs ai": "chatbot", "ai chatbot for ecommerce website": "chatbot",
    "ai chatbot website examples": "chatbot", "ai chatbot example": "chatbot",
    "ai chatbot for real estate agents": "realestate",
    # missed call text back
    "how to respond to a missed call by text": "mctb", "go high level missed call text back": "mctb",
    "missed call text back software": "mctb", "the missed call text back": "mctb", "auto missed call text back": "mctb",
    "gohighlevel missed call text back": "mctb", "ghl missed call text back": "mctb", "missed call text back service": "mctb",
    "missed call text back gohighlevel": "mctb", "the missed call text back calculator": "mctb", "missed call text back calculator": "mctb",
    "missed call text back automation": "mctb", "auto missed call text back software": "mctb", "missed call text back high level": "mctb",
    "missed call text back app": "mctb", "high level missed call text back": "mctb", "how to set up missed call text back gohighlevel": "mctb",
    "should i call back a missed call": "mctb",
    # booking
    "ai appointment": "booking", "ai appointment booking bot": "booking", "what is appointment scheduling": "booking",
    "what is appointment scheduling software": "booking", "ai appointment setting bot": "booking", "ai appointment booking system": "booking",
    "ai appointment booking agent": "booking", "what is online appointment": "booking",
    # crm
    "crm automation services": "crm", "crm automation software": "crm", "crm automation tools": "crm", "what is crm automation": "crm",
    "crm automated emails": "crm", "crm sales automation": "crm", "crm process automation": "crm", "crm automation examples": "crm",
    "crm automation company": "crm", "crm automation benefits": "crm", "crm automation definition": "crm", "crm automation meaning": "crm",
    "why crm system": "crm", "why crm is so important": "crm", "marketing crm automation": "crm", "ai lead follow up": "crm",
    "ai follow up": "crm", "marketing automation for small businesses": "crm", "marketing automation email": "crm",
    "marketing automation workflow": "crm", "marketing automation lead nurturing": "crm", "marketing automation benefits": "crm",
    "what's marketing automation": "crm", "marketing automation examples": "crm", "marketing automation agency": "crm",
    "marketing automation consultant": "crm", "marketing automation implementation services": "crm",
    "marketing automation with ai": "crm", "marketing automation ai": "crm", "marketing automation near me": "crm",
    "marketing automation meaning": "crm", "marketing automation flow": "crm", "marketing automation companies": "crm",
    "marketing automation for lead generation": "marketing", "marketing automation lead": "crm", "marketing automation roi": "crm",
    "marketing automation process": "crm", "marketing automation expert": "crm", "why marketing automation": "crm",
    "marketing automation pricing": "pricing", "marketing automation business": "crm", "marketing automation what is it": "crm",
    "marketing automation use cases": "crm", "go high level crm automation specialist": "crm", "crm automation specialist": "crm",
    # business automation
    "business automation": "bizauto", "small business automation": "bizauto", "business automation agency": "bizauto",
    "business automation service": "bizauto", "business automation consultants": "bizauto", "business automation consultant": "bizauto",
    "small business automation consultant": "bizauto", "ai business automation": "bizauto", "ai for business automation": "bizauto",
    "business automation ai": "bizauto", "what is business automation": "bizauto", "what is automation in business": "bizauto",
    "benefits of business automation": "bizauto", "business automation company": "bizauto", "business automation companies": "bizauto",
    "business automation experts": "bizauto", "business automation expert": "bizauto", "business automation solution": "bizauto",
    "business automation process": "bizauto", "business automation processes": "bizauto", "business automation examples": "bizauto",
    "business process automation examples": "bizauto", "business process automation benefits": "bizauto",
    "business automation definition": "bizauto", "business operations automation": "bizauto", "business automation workflow": "bizauto",
    "business automation system": "bizauto", "business automation specialist": "bizauto", "small business automation services": "bizauto",
    "small business automation solutions": "bizauto", "local business automation": "bizauto", "home service business automation": "plumber",
    "ai powered business automation": "bizauto", "intelligent business automation": "bizauto", "why automation is good for business": "bizauto",
    "ai agent business automation": "bizauto", "ai agents for business automation": "bizauto", "ai for small business automation": "bizauto",
    "ai for small business efficiency": "bizauto", "business automation help": "bizauto", "business growth automation": "bizauto",
    "business automation management": "bizauto", "my business automation": "bizauto", "commercial business automation": "bizauto",
    "business of automation": "bizauto", "ai agency automation ": "home", "end to end business automation": "bizauto",
    "business automation services": "bizauto", "what is office automation software": "bizauto",
    # consulting
    "ai consultant": "consulting", "ai consultant for small business": "consulting", "ai consulting for small businesses": "consulting",
    "small business ai consultant": "consulting", "ai consultant services": "consulting", "ai consultant near me": "consulting",
    "hire ai consultant": "consulting", "what does an ai consultant do": "consulting", "what does ai consultant do": "consulting",
    "what is an ai consultant": "consulting", "what is ai consultant": "consulting", "what is a ai consultant": "consulting",
    "what is ai consulting": "consulting", "who is an ai consultant": "consulting", 
    "ai consultant agency": "consulting", 
    
    "ai consultant meaning": "consulting", "ai consultant for law firms": "law",
    "how can ai help small businesses": "consulting", "what can ai do for business": "consulting", "what can ai do for my business": "consulting",
    "why ai is important for business": "consulting", "ai implementation for small business": "consulting",
    "how to use ai for small business": "industries", "how to use ai for my small business": "industries", "using ai for small business": "industries",
    "ai for small business owners": "industries", "best ai for small business": "industries", "best ai for small business owners": "industries",
    "what is the best ai for small business": "industries", "agentic ai for small business": "industries", "generative ai for small business": "industries",
    "ai agent for small business owners": "industries", "ai for small business marketing": "marketing", "best ai for small business marketing": "marketing",
    "how to use ai for small business marketing": "marketing", "ai for construction small business": "contractor",
    "ai for small construction business": "contractor", "ai training for small business owners": "consulting",
    "ai skills for small business": "consulting",
    # agency
    "ai automation agency hub": None, "ai agent building": None, "what's ai agent": None, "ai small business tools": None,
    "who ai call assistant": None, "will business analyst be automated": None,
    # marketing
    "ai marketing agency near me": "marketing", "ai digital marketing agency": "marketing", "ai powered marketing agency": "marketing",
    "best ai marketing agency": "marketing", "ai driven marketing agency": "marketing", "ai marketing agency services": "marketing",
    "ai marketing automation agency": "marketing", "what is ai marketing agency": "marketing", "what is an ai marketing agency": "marketing",
    "what is a ai marketing agency": "marketing", "ai based marketing agency": "marketing", "marketing agency with ai": "marketing",
    "ai first marketing agency": "marketing", "is ai marketing legit": "marketing", "how does ai marketing work": "marketing",
    "is a marketing agency worth it": "marketing", "ai agency digital marketing": "marketing", "growth ai marketing agency": "marketing",
    "ai marketing agency meaning": "marketing", "seo ai agency": "marketing", 
    "how can ai be used in marketing": "marketing", "how to use ai in marketing": "marketing", "how does ai help marketing": "marketing",
    # industries
    "ai receptionist for law firms": "law", "ai answering service for law firms": "law", "ai for personal injury law firms": "law",
    "ai for small law firms": "law", "best ai for law firms": "law", "ai agents for law firms": "law", "best ai for small law firms": "law",
    "agentic ai for law firms": "law", "generative ai for law firms": "law",
    "ai for hvac companies": "hvac", "hvac ai receptionist": "hvac", "how to run a hvac business": "hvac",
    "dental ai receptionist": "dental", "ai dental receptionist": "dental", "ai for dentists": "dental", "ai for dental": "dental",
    "ai receptionist for dentists": "dental", "ai receptionist for dental office": "dental", "best dental ai receptionist": "dental",
    "ai receptionist for dentist": "dental", "ai receptionist dental": "dental", "ai receptionist for dental clinic": "dental",
    "ai agents for dentists": "dental", 
    "ai receptionist for salons": "salon", "ai receptionist for salon": "salon", "ai for salons": "salon", "ai salon receptionist": "salon",
    "ai receptionist for nail salon": "salon", 
    "ai for contractors": "contractor", "ai receptionist for contractors": "contractor", "ai for general contractors": "contractor",
    "ai for electrical contractors": "contractor", "ai receptionist for electricians": "contractor", "best ai for contractors": "contractor",
    "best ai for construction business": "contractor", "how can ai help in construction": "contractor",
    "ai for restaurants": "restaurant", "ai receptionist for restaurant": "restaurant", "ai answering service for restaurants": "restaurant",
    "ai phone answering for restaurants": "restaurant", "best ai for restaurants": "restaurant", "ai for restaurant business": "restaurant",
    "ai phone answering service for restaurants": "restaurant", "ai for restaurant management": "restaurant", 
    "use of ai in restaurants": "restaurant",
    "ai for real estate agents": "realestate", "best ai for real estate agents": "realestate", 
    "ai for real estate lead generation": "realestate", "ai lead generation for real estate agents": "realestate",
    "ai receptionist for real estate": "realestate", "ai powered real estate agent": "realestate", "best ai assistant for real estate agents": "realestate",
    "how to use ai for real estate agents": "realestate", "using ai for real estate agents": "realestate", "ai for real estate brokers": "realestate",
    "ai marketing for real estate agents": "realestate", "which ai is best for real estate agents": "realestate",
    "ai receptionist for property management": "realestate", "ai for real estate marketing": "realestate", "how to use ai in real estate": "realestate",
    
    "ai receptionist for plumbers": "plumber",
    "ai receptionist for medical office": "medical", "medical ai receptionist": "medical", "ai answering service for medical office": "medical",
    "what is an answering service for a doctors office": "medical", "what is medical answering service": "medical",
    "ai receptionist for healthcare": "medical", 
    # how it works
    "ai automation agency business model": None, "ai agency model": None,
}

UNUSED = [  # (group, reason, regex) checked in order after EXPLICIT
    ("Claims the agency cannot make, services it does not offer, and industries without a page", "INTAKE.md forbids the claim (HIPAA compliant) or the service (custom AI development), or the industry has no page and too little demand for one.",
     r"development|hipaa|hotel|veterinar|vet clinic|ecommerce|retail|healthcare marketing|marketing automation healthcare|for electrical construction"),
    ("Jobs, roles and titles", "Job seekers or job titles, not buyers.",
     r"manager|coordinator|director|analyst|executive|specialist|marketing automation (?:engineer|developer|expert)|consultant (?:linkedin|website)|ai consultant business"),
    ("Content, media and research rows", "People looking for articles, images, videos, reports or trend pieces about the topic, not a service.",
     r"\bicon\b|images?\b|\bgif\b|\bppt\b|\bblog\b|events?\b|webinar|video|youtube|report|research|trends?\b|20(?:23|24|25|26)|\bllc\b|\bcorp\b|insider|marketing automation hub|dummies|linkedin|marketing automation (?:guide|basics|case study|requirements|integration|best practices|plan|goals|operations|builder|ecommerce)|ai chatbot example|ai chatbot companies|chatbot for your website which ai approach|ai voice agent (?:platform|software|make com)|best ai voice agent platform|no code|ai automation agency (?:website|model|sales call|tools)|100k ai agency|agentic|generative|gen ai|conversational ai consultant|applied ai consultant|ai transformation|ai marketing agents|ai restaurants|ai dental (?:software|app|assistant)|ai salon app|ai construction app|best ai (?:tools|app) for real estate"),
    ("Jobs, careers and salaries", "Job seekers, not buyers.",
     r"\bjobs?\b|salary|salaries|hiring|career|internship|vacature|how much (?:do|does) .* (?:make|earn)|resume|job description|\bremote\b|freelance|upwork|interview platform"),
    ("Courses, training, certification and how to start or sell an AI agency", "People learning or starting their own agency, not buyers.",
     r"course|certif|training|masterclass|mastermind|webclass|academy|101\b|tutorial|for beginners|book|pdf|handbook|guidebook|degree|learn|how to (?:start|become|be |build|make|create|sell|get|do )|become|becoming|start (?:an|your|ai)|starting|building (?:an )?ai|build(?:ing)? an ai|build ai|create (?:an )?ai|make (?:an )?ai|selling|sell ai|white ?label|business model|roadmap|step by step|how to make money|make money|arbitrage|accelerator|skool|instant ai agency|real world|reeve|hormozi|andrew tate|jordan lee|alicia lyttle|industry rockstar|cpd|program\b|owner\b|names|logo|template|theme|landing page|website template|how many ai automation agencies|saturated|get .*clients|find clients|\bn8n\b|make\.com|zapier|github|open source|huggingface|framework|architecture|design patterns|mcp\b|\bllm\b|rag\b|harness|benchmarks|hackathon|project|loop|prompt|sdk|api\b|developer|development|engineer|frameworks|ai agents? (?:explained|definition|meaning|types|list|directory|free|builder|platform|marketplace|app|ui|dashboard|governance|library|paper|ranking|hub|network|kit|hosting|names?|news|book|video|youtube|for trading|trading|gpt|gemini|chatgpt|google|browser|use cases|examples|system|patterns|workflow|design|questions|that matter|unleashed|udemy|with|what are they|talking|hiring|team|for beginners|zendesk|1|hallucination|50)|the definitive guide|which ai agent|ai agent builder|ai receptionist builder|ai voice agent builder|ai receptionist generator|ai receptionist image|ai voice agent icon|create ai receptionist|how to make ai receptionist|how to build ai receptionist|ai agency reddit|reddit|copy my ai agency|what is ai agency business|what is an ai agency business|ai agency business|ai agency 20 hours|ai agency podcast|ai agency directory|ai agency of the year|ai agency institute|start your ai agency"),
    ("Free tools and DIY software, apps and comparisons", "Shoppers for a free or do-it-yourself tool, not for someone to set it up.",
     r"\bfree\b|\bapp\b|for iphone|for android|for cell phone|iphone|personal use|software for|tools? for|ai tools|best ai for|best ai tools|best ai app|claude ai for|jasper|google ai for|chatgpt|for ecommerce|answering machine|ai size|shoe size|what is answering machine|how to answer business phone|answering a business phone|what to say on answer phone|which is the best phone|is phone business profitable|ai business automation software|business automation softwares?|business automation software|business automation tools|business automation platform|automation tools|automation software|automation platforms?|automation programs|automation vendors|marketing automation tools|marketing automation platforms|ai chat web search|web search|no filter|poly ai|chatai|ai chat website|ai salon pod|ai salon robot|ai dental rpd|x ray|design software|woodpecker|note taking|dental design|dental engineering|dental learning|dental diagnostics|construction drawings|construction design|construction estimating|construction tools|construction management|construction safety|construction video|ai builder examples|contract review|review contracts|ai receptionist open source|ai receptionist 3cx|ai website builder|ai virtual|whatsapp"),
    ("Named companies, products and platforms (other vendors)", "A search for one named product or company; CLAUDE.md rule 4: never name competitors.",
     r"ringcentral|smith\.?ai|smith ai|rosie|nextiva|beside|upfirst|weave|jobber|zoom|3cx|goto|allo\b|ulio|goodcall|nextphone|synthflow|google voice|dialpad|breezy|retell|housecall|clara|dodo|bookipi|ionos|lucy|quo\b|zenoti|atlas|webex|elevenlabs|yelp|mango|simply wise|vapi|ooma|broccoli|8x8|twilio|openphone|emma|abby|sophie|dialzara|sona\b|lindy|justcall|aircall|asterisk|salesforce|sesame|bland|grok|open ai|openai|hubspot|zoho|marketo|pardot|adobe|oracle|netsuite|dynamics|microsoft|odoo|activecampaign|monday|ibm|cloud pak|uipath|palantir|red hat|sap\b|kodah|barnabas|rtila|gartner|deloitte|accenture|ey\b|dept\b|google\b|claude|harvey|soundhound|a16z|eversana|growthx|dion\b|crm 4|agency 66|agency 6b|agency 8200|agency 00|agency agent 00|m1 ai|soundhound|ai receptionist goto|forbes|air tech|which ai companies|top leading ai companies|ai real estate companies|ai voice companies|ai defence companies"),
    ("News, celebrity, opinion and general AI curiosity", "Reading about AI in general, not looking to hire.",
     r"news|will ai|can ai|is ai\b|why has ai|why would ai|where is ai|where to ai|where has ai|why ai matters|how soon|who is responsible|how many|what is ai first|ai location|ai hours|ai ou ais|ai secretary|ai education secretary|nhs|are ai voice scams|ai agents hiring humans|ai agents with no boundaries|are ai agents overhyped|how ai agents work|which ai is leading|which ai platform|why follow|ai lead job|ai lead form|ai 623|ai consultant 500 million|will dentists|replace|human ai agency|ai agents? 101|what ai agents can do|can ai agents|which ai agent|what ai agents are free|ai agent jobs|ai agents that matter|ai agent questions|is ai coming|what is a i 9|why am i getting|how many ai"),
    ("Enterprise and large-company rows", "Enterprise platforms and B2B programs beyond a small local business.",
     r"enterprise|b2b|b2c|magic quadrant|market size|\bmarket\b|bpa\b|business process automation (?:bpa|gartner|vendors|jobs|use cases|job description)|business intelligence|it business automation|technology business automation|business automation technolog|business automation software development|business automation software solutions|business automation analyst|automation business analyst|business automation center|business document automation|business data automation|business finance automation|business rule automation|business automation framework|workflow documentation|knowledge center|digital business automation|smart business automation|business automation with python|business automation group|business automation insights|business automation content analyzer|commercial building|building automation|government contracting|ai for manufacturing|ai transformation|data (?:and|&) ai|azure|ethical ai|legal ai consultant|healthcare ai consultant|ai consultant ireland|software engineer ai consultant|automated business designs|automated business resources|automated business online|online business automation|automation business for sale|business automation bangladesh|business automation i pvt|ai healthcare consultant"),
    ("Other countries and non-US places", "Outside the United States, or a local search in a city this national service does not target.",
     r"\buk\b|london|manchester|st albans|ireland|australia|melbourne|sydney|singapore|india|indian|hindi|bangla|bahasa|indonesia|pakistan|dubai|nederland|amsterdam|toronto|canada|\bnz\b|south africa|malaysia|portugal|beirut|lebanon|brunei|cape town|vancouver|ontario|peterborough|whitehorse|tokyo|torino|shرح|شرح|verktyg|que es|là gì|clifton park|indore|san antonio|airport|miami|phoenix|st pete|nyc|california|colorado springs|south pasadena|vastu|tagalog"),
    ("Off-topic (a different meaning of the words)", "Not about AI services for a business at all (voice acting, VoIP, receptionist job, restaurant listings, real estate statistics, etc.).",
     r"voice over|voice act|voice actor|voiceover|air voice|agent for voice acting|text to speech|voice over generator|voice generator|consultant meaning|what is consultant|consultant (?:engineer|doctor|surgeon|in hospital|role|work)|what is agency|agency theory|agency cost|agency problem|agency work|what is receptionist|receptionists|receptionist (?:job|position|office|in hotel)|receptionist salary|phone receptionist job|what is marketing (?:agency|company)|what is digital marketing agency|marketing agency do|what is appointment\b|when should you have your booking|how many real estate|percentage for real estate|how to rate a real estate|what rate do real estate|how much real estate|real estate developers|real estate listings|ai certified real estate|real estate agent in portugal|how to become a dentist|american dental|dental students|dentist robot|dentist video|dental ormeau|dentistry|ai dental setup|ai dental woodpecker|hvac companies in|hvac companies profitable|hvac manufacturer|hvac technicians|hvac be replaced|ai hvac jobs|why am i contracting|ai contract jobs|ai contractor jobs|law firm garfield|law firm startup|first ai law firm|law firm wins|lawyers|law jobs|foreign law firms|law firms should i apply|restaurant (?:name|design|generator|grader|finder|logo|video|menus)|ai restaurant (?:near me|nyc|california|colorado|south|dubai|lebanon|beirut)|where am i restaurant|where to eat|book an entire restaurant|ai salon (?:hairstyle|interior|logo|name|near me|video|miami|phoenix|st pete|amsterdam|dubai|sydney|tokyo|torino)|consultant\b.*(?:doctor|hospital)|ai in advertising|ai marketing videos|ai marketing 20|ai marketing 101|ai marketing jobs|will ai take over marketing|how does ai affect marketing|ai restaurant\b|ai salon\b|what is voice|voice over lte|voice over wifi|voice over on iphone|ai voice actor|ai voice over|what is online|ai agency 2025|ai automation agency 202|ai agency là|how to make an ai voice|how to make an ai voice assistant|what is office automation|office automation|ai testing jobs|ai agents automation testing|crm automation testing|testing tools|selenium|ai dentist|construction workers|construction managers|ai in construction examples|generative ai for construction|best ai for construction|what is the best ai for construction|which companies use ai|how to build an ai company|how to start an ai company|ai small business ideas|small business ideas|chatbot business ideas|how to become a small business consultant|ai for small business (?:book|pdf|course)|ai agents for small business mark zuckerberg|ai for small business anthropic|ai agency (?:mastermind|masterclass|book|accelerator)|google ai|what is ai chatbot|what is the best ai chatbot|ai chatbot jobs|ai agent definition|ai agent meaning|the ai agency book|future ai agency|national ai agency|head ai agency|health ai agency|ai agency (?:australia|london|toronto|amsterdam|dubai|singapore|uk|manchester|south africa|in dubai|malaysia)|gen ai agency|generative ai agency|agentic ai agency|creative ai agency|ai agency website|ai agency growth|ai agency cold calling|cold calling ai agency|ai agency services|ai agency landing|ai agency white|ai agency template"),
]

PATTERNS = [  # (page, regex) fallback for buyer rows not in EXPLICIT
    ("dental", r"dental|dentist"), ("salon", r"salon"), ("law", r"law firm|lawyer|attorney"),
    ("hvac", r"\bhvac\b"), ("plumber", r"plumb"), ("restaurant", r"restaurant"), ("realestate", r"real estate|property manag"),
    ("medical", r"medical|healthcare|doctor|veterinar|clinic"), ("contractor", r"contractor|construction|electric"),
    ("mctb", r"missed call"), ("booking", r"appointment"), ("chatbot", r"chatbot|chat bot|ai chat"),
    ("answering", r"answering"), ("receptionist", r"receptionist"), ("voice", r"voice agent"),
    ("crm", r"\bcrm\b|marketing automation"), ("bizauto", r"business automation|automation (?:services?|agency|consult)"),
    ("consulting", r"consult"), ("marketing", r"marketing agency"), ("agency", r"automation agency"),
    ("home", r"\bai agency\b"),
]


def classify(kw):
    k = kw.lower().strip()
    if k in EXPLICIT:
        return ("page", EXPLICIT[k]) if EXPLICIT[k] else ("unused", 1)
    for page, t in TARGETS.items():
        if k == t:
            return ("page", page)
    for i, (g, reason, rx) in enumerate(UNUSED):
        if re.search(rx, k):
            return ("unused", i)
    for page, rx in PATTERNS:
        if re.search(rx, k):
            return ("page", page)
    return (None, None)


def main():
    wb = openpyxl.load_workbook(ROOT / "keywords" / "AI-Agency-Keywords.xlsx", read_only=True)
    rows = [r for r in list(wb["ALL"].iter_rows(values_only=True))[1:] if r[0]]
    data = {}
    for kw, typ, vol, sd, cpc, seed in rows:
        data[kw.lower().strip()] = {"kw": kw, "type": typ, "vol": int(vol or 0), "sd": int(sd or 0), "cpc": float(cpc or 0), "seed": seed}
    ten = [d for d in data.values() if d["vol"] >= 10]
    by_page, unused, missing = defaultdict(list), defaultdict(list), []
    for d in sorted(ten, key=lambda d: (-d["vol"], d["kw"])):
        kind, val = classify(d["kw"])
        if kind == "page":
            by_page[val].append(d)
        elif kind == "unused":
            unused[val].append(d)
        else:
            missing.append(d)
    # targets must exist in the data (or be listed as not in the data) and be unique
    for page, t in TARGETS.items():
        if t not in data and page not in TARGET_NOT_IN_DATA:
            missing.append({"kw": f"TARGET MISSING FROM DATA: {t} ({page})", "vol": 0, "sd": 0, "type": ""})
    if missing:
        for d in missing:
            print("UNCLASSIFIED", d["kw"], d["vol"])
        print(f"{len(missing)} rows unclassified")
        return 1

    def fmt(d):
        q = ", Question" if d["type"] == "Question" else ""
        return f"{d['kw']} ({d['vol']:,}/{d['sd']}{q})"

    assigned = sum(len(v) for v in by_page.values())
    out_json = {}
    lines = [
        "# Keyword plan: Dominion AI Agency",
        "",
        "Generated by `python3 scripts/keyword_plan.py` from keywords/AI-Agency-Keywords.xlsx (Ubersuggest, United States,",
        "pulled Oct 15 2026, ALL tab, 8,517 rows). Numbers are monthly volume / SEO difficulty, verified from the file.",
        "Every row with a volume of 10 or more is either assigned to a page (its target or a supporting keyword) or listed",
        "below as deliberately unused, summarized by group with a one-line reason. One page per intent cluster: no two",
        "pages share a target.",
        "",
        f"Rows with volume 10 or more: {len(ten):,} ({sum(d['vol'] for d in ten):,} searches a month). Assigned to pages: {assigned:,} rows "
        f"({sum(d['vol'] for v in by_page.values() for d in v):,} searches). Deliberately unused: {len(ten) - assigned:,} rows "
        f"({sum(d['vol'] for v in unused.values() for d in v):,} searches).",
        "",
        "## Keywords by page",
        "",
    ]
    for page, url in PAGES.items():
        t = TARGETS.get(page)
        lines.append(f"### {url}")
        td = data.get(t) if t else None
        if t and td:
            lines.append(f"- Target: {fmt(td)}")
        elif t:
            lines.append(f"- Target: {t} (not in the data: {TARGET_NOT_IN_DATA.get(page, '')})")
        else:
            lines.append("- Target: none (support page)")
        sup = [d for d in by_page.get(page, []) if d["kw"].lower() != t]
        if sup:
            lines.append("- Supporting: " + "; ".join(fmt(d) for d in sup))
        lines.append("")
        out_json[url] = {"target": t, "target_vol": td["vol"] if td else 0, "target_sd": td["sd"] if td else 0,
                         "supporting": [{"kw": d["kw"], "vol": d["vol"], "sd": d["sd"], "question": d["type"] == "Question"} for d in sup]}
    lines += ["## Deliberately unused rows (volume 10+), by group", ""]
    for i, (g, reason, rx) in enumerate(UNUSED):
        rows_g = unused.get(i, [])
        lines.append(f"### {g}: {len(rows_g)} rows, {sum(d['vol'] for d in rows_g):,} searches")
        lines.append(f"Reason: {reason}")
        lines.append("")
        lines.append("; ".join(fmt(d) for d in rows_g) if rows_g else "(none)")
        lines.append("")
    (ROOT / "docs" / "keyword-plan.md").write_text("\n".join(lines) + "\n")
    (ROOT / "docs" / "keywords.json").write_text(json.dumps(out_json, indent=1) + "\n")
    print(f"{len(ten)} rows 10+: {assigned} assigned, {len(ten) - assigned} unused; wrote docs/keyword-plan.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
