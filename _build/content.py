"""Single content source for all three options.

Every fact comes from v2-miranda (Prashant's CV content). US spelling.
No phone numbers (public preview): email and LinkedIn only.
"""

NAME = "Prashant Kumar Jindal"
EMAIL = "prashant.k.jindal@gmail.com"
MAILTO = "mailto:prashant.k.jindal@gmail.com?subject=Meeting%20request"
LINKEDIN = "https://www.linkedin.com/in/prashantjindalie"
LINKEDIN_LABEL = "in/prashantjindalie"

TITLE = "Prashant Kumar Jindal | Strategy and Business Development"
DESC = ("Prashant Kumar Jindal: six years of business development and strategy in EdTech. "
        "International MBA candidate at IE Business School, Madrid.")

HERO_H1_PRE = "From 150 calls a day to a "
HERO_H1_EM = "USD&nbsp;12.5M"
HERO_H1_POST = " revenue book."
HERO_LEDE = ("Strategy, business development and go to market. Six years in EdTech, "
             "now an International MBA candidate at IE Business School, Madrid.")
PHOTO_ALT = "Portrait of Prashant Kumar Jindal in a grey jacket and navy T-shirt."

# (prefix, number, suffix, label)
STATS = [
    ("USD ", "12.5", "M", "Revenue book managed across 10 cities at BYJU'S"),
    ("", "120", "+", "People in the sales organization I scaled"),
    ("", "6", "", "Cities in the market entry strategy I built"),
    ("", "2,000", "+", "Sales professionals trained, in batches of 70 to 100"),
]

CAREER_H2 = "From sales calls to the strategy table, in seven steps."
CAREER_INTRO = "Five roles in sales and strategy, then an MBA and a startup."
CAREER = [
    ("2018", "Senior Business Development Executive", "BYJU'S", "150+ outbound calls a day across India and the UAE"),
    ("2019", "Business Development Manager", "BYJU'S", "Led a 20-person team to USD 2M in revenue"),
    ("2021", "Senior Business Development Manager", "BYJU'S", "8 managers, 120 reps, 10 cities, USD 12.5M book"),
    ("2023", "Senior Business Development Manager", "upGrad", "Funnel conversion up 30% in 2 quarters"),
    ("2024", "Head of Strategy and Operations", "Boston Institute of Analytics", "Key strategic partner to the Managing Director"),
    ("2025", "International MBA", "IE Business School, Madrid", "IE Merit Scholar, GPA 3.66 of 4.0"),
    ("2026", "Cofounder", "BingeMind, AI automation", "AI voice receptionist agents, built as a proof of concept"),
]

WORK_INTRO = "Each case page gives the context, what I did and the results."

ASK = 'Want more detail? <a href="%s">Ask me by email</a>.' % MAILTO

CASES = [
    {
        "slug": "market-entry",
        "company": "Boston Institute of Analytics",
        "years": "2024 to 2025",
        "title": "A six-city market entry plan that leadership funded",
        "short": "A six-city market entry plan",
        "sum": "Investment cases, revenue forecasts and competitor benchmarking that set the FY25 growth priorities.",
        "res": ("5", "B2B partnerships structured and closed"),
        "lede": "As Head of Strategy and Operations at Boston Institute of Analytics, an EdTech company, I was the Managing Director's key strategic partner.",
        "note": None,
        "meta": [("Company", "Boston Institute of Analytics"), ("Role", "Head of Strategy and Operations"),
                 ("Place", "Lucknow, India"), ("Dates", "March 2024 to August 2025")],
        "chapters": [
            ("Market entry", None, [
                "Drove a 6-city market entry strategy. It paired investment cases, revenue forecasts and competitor benchmarking.",
                "The strategy set the FY25 growth priorities that leadership funded.",
                "Built a competitor benchmarking framework that is now used for capital allocation."]),
            ("Partnerships", None, [
                "Structured and closed 5 B2B partnerships, and negotiated the commercial terms.",
                "Redesigned the partner onboarding process. Onboarding time went down 25%."]),
            ("Customers and product", None, [
                "Ran 200+ customer interviews.",
                "Turned the findings into 3 product launches and 18% cross sell growth.",
                "Set up new CRM and KPI systems. Outreach conversion went up 28%."]),
            ("A new regional center", None, [
                "Held full P&amp;L ownership of a regional center.",
                "The center generated USD 35K in revenue within 4 months of launch."]),
        ],
        "figs": [("6", "Cities in the market entry strategy"), ("5", "B2B partnerships closed"),
                 ("25%", "Less partner onboarding time"), ("200+", "Customer interviews"),
                 ("USD 35K", "Revenue from a new center in its first 4 months")],
        "tags": ["Market entry", "Business cases", "Revenue forecasting", "Competitive benchmarking", "Partnerships", "P&amp;L ownership"],
        "ask": 'In this role I received a Certificate of Excellence as Head of Strategy. Want more detail? <a href="%s">Ask me by email</a>.' % MAILTO,
    },
    {
        "slug": "bank-partnerships",
        "company": "upGrad",
        "years": "2023 to 2024",
        "title": "Bank partnerships and a sales funnel rebuilt end to end",
        "short": "Bank partnerships and a rebuilt funnel",
        "sum": "Executive education deals with ICICI Bank and HDFC Bank, and a B2C funnel with 30% higher conversion.",
        "res": ("USD 420K", "Learner lifetime value added"),
        "lede": "As Senior Business Development Manager at upGrad, I worked on enterprise deals, B2C acquisition and a large channel partner network.",
        "note": None,
        "meta": [("Company", "upGrad"), ("Role", "Senior Business Development Manager"),
                 ("Place", "Indore, India"), ("Dates", "March 2023 to March 2024")],
        "chapters": [
            ("Enterprise partnerships", None, [
                "Won executive education partnerships with ICICI Bank and HDFC Bank through consultative, account based selling.",
                "The deals added USD 420K in learner lifetime value.",
                "Beat revenue targets by 15%."]),
            ("The B2C funnel", None, [
                "Rebuilt the B2C acquisition funnel end to end: pipeline structure, customer segments and CRM led follow-up.",
                "Conversion went up 30% in 2 quarters."]),
            ("Channel partners", None, [
                "Scaled a 40-member channel partner team across 6 regions.",
                "Managed a wider network of 500+ enrollment partners in 50+ countries.",
                "Pipeline volume grew 22%."]),
            ("The team", None, [
                "Coached a 20-person team with performance dashboards and behavioral data.",
                "Team productivity went up 42%."]),
        ],
        "figs": [("USD 420K", "Learner lifetime value from bank partnerships"), ("15%", "Above revenue target"),
                 ("30%", "Higher funnel conversion in 2 quarters"), ("50+", "Countries in the enrollment partner network"),
                 ("42%", "Higher team productivity")],
        "tags": ["Account based selling", "Enterprise partnerships", "Funnel design", "Customer segmentation", "Channel sales", "Coaching"],
        "ask": ASK,
    },
    {
        "slug": "regional-growth",
        "company": "BYJU'S",
        "years": "2018 to 2023",
        "title": "From first sales calls to a USD 12.5M regional book",
        "short": "From first calls to a USD 12.5M book",
        "sum": "Three roles, a 120-rep sales team, the Disney BYJU'S Early Learn launch and 2,000+ people trained.",
        "res": ("120%+", "Quota attainment"),
        "lede": "Nearly five years at BYJU'S, in K12 and test prep EdTech. I held three roles, and each one came with more people and more revenue.",
        "note": None,
        "meta": [("Company", "BYJU'S"), ("Roles", "Executive to Senior Manager, Business Development"),
                 ("Place", "Lucknow and Mumbai, India"), ("Dates", "June 2018 to January 2023")],
        "chapters": [
            ("Senior Business Development Manager", "2021 to 2023", [
                "Directed regional commercial operations and P&amp;L across 2 states and 10 cities.",
                "Managed 8 managers and 120 reps against a USD 12.5M revenue book, with 120%+ quota attainment.",
                "Delivered the national Manager Bootcamp to 50 managers across India and the Middle East (Dubai, Oman).",
                "Trained 2,000+ sales professionals in batches of 70 to 100, at an 80% conversion rate.",
                "Rolled out LeadSquared lead scoring. Conversion efficiency went up 18%."]),
            ("Business Development Manager", "2019 to 2020", [
                "Led a 20-person regional team to USD 2M in revenue through territory planning, pipeline management and coaching.",
                "Cut team attrition from 15% to under 5% in 4 months.",
                "Launched Disney BYJU'S Early Learn with Disney's US team, on product localization and channel design.",
                "The launch opened a partner led channel worth USD 135K in 4 months."]),
            ("Senior Business Development Executive", "2018 to 2019", [
                "Started with 6 months of B2C sales across India and the UAE: 150+ outbound calls a day and 15 to 20 qualified demos a week.",
                "Moved into B2B. Built a USD 1M qualified pipeline and about USD 250K in revenue through outbound prospecting and consultative selling.",
                "Grew repeat business 25%."]),
        ],
        "figs": [("USD 12.5M", "Revenue book across 10 cities"), ("120%+", "Quota attainment"),
                 ("2,000+", "Sales professionals trained"),
                 ("USD 135K", "Partner channel from the Disney BYJU'S Early Learn launch, in 4 months"),
                 ("Top 10", "Manager nationwide, and Top 10 Business Development Associate nationwide")],
        "tags": ["Regional P&amp;L", "Sales leadership", "Sales training", "Lead scoring", "Product launch", "B2B and B2C sales"],
        "ask": ASK,
    },
    {
        "slug": "mba-projects",
        "company": "IE Business School",
        "years": "2025 to 2026",
        "title": "MBA case work at IE Business School",
        "home_title": "MBA case work on Oatly, Patagonia, Sport Obermeyer and Aqualia",
        "short": "MBA case work at IE Business School",
        "sum": "Projects on supply chains, forecasting, digital product passports and ESG reporting.",
        "res": ("4", "Company case projects"),
        "lede": "Projects from my International MBA in Digital Business and International Transformation. Each project applies strategy and operations tools to a real company.",
        "note": "These are academic projects. The companies were not clients.",
        "meta": [("School", "IE Business School"), ("Program", "International MBA"),
                 ("Place", "Madrid, Spain"), ("Dates", "September 2025 to December 2026")],
        "chapters": [
            ("Oatly: supply chain transformation", None, [
                "Diagnosed Oatly as stuck between two supply chain models.",
                "Mapped a 5-year roadmap to move the company from reactive to resilient: cloud ERP, outside-in demand sensing and modular manufacturing."]),
            ("Sport Obermeyer: operations and forecasting", None, [
                "The case: USD 5M of production commitments, made 4 months before demand data was available, for a skiwear line with high uncertainty.",
                "Restructured the commitments with fabric postponement and risk based sourcing: Hong Kong for uncertain styles, China for predictable classics.",
                "The aim was lower inventory exposure."]),
            ("Patagonia: digital innovation", None, [
                "Devised LoopID, a digital product passport that uses an NFC chip and blockchain.",
                "LoopID is designed to cut resale processing from 15 minutes to under 2, at under USD 1 per unit.",
                "It is also designed to put Patagonia ahead of the incoming EU Digital Product Passport regulation."]),
            ("Aqualia: CSRD materiality", None, [
                "Assessed double materiality against a significance threshold of 3.5 out of 5.",
                "Found the ESG topics most material to Aqualia's 2027 to 2030 strategy, ahead of mandatory CSRD reporting."]),
        ],
        "figs": [("3.66", "GPA out of 4.0, as an IE Merit Scholar"), ("680", "GMAT"),
                 ("11", "IE's QS Global MBA rank (2026)")],
        "tags": ["Corporate Finance: DCF, WACC, LBO", "Applied Data Analytics", "Six Sigma, DMAIC",
                 "Digital Business Strategy", "Supply chain", "ESG and CSRD"],
        "ask": 'The full project reports are available on request. <a href="%s">Ask me by email</a>.' % MAILTO,
    },
]

for c in CASES:
    c.setdefault("home_title", c["title"])

BRING_H2 = "What I bring to a team"
BRING = [
    ("I start from the customer",
     "At Boston Institute of Analytics I ran 200+ customer interviews. The findings became 3 product launches.",
     ("18%", "Cross sell growth from those launches")),
    ("I close partnerships",
     "I structure B2B deals and negotiate the terms. I won executive education partnerships with ICICI Bank and HDFC Bank.",
     ("25%", "Less partner onboarding time at Boston Institute of Analytics, after I redesigned the process")),
    ("I fix the funnel",
     "I rebuild sales funnels with clear segments, CRM follow-up and lead scoring. At upGrad, B2C conversion went up 30% in 2 quarters.",
     ("28%", "Higher outreach conversion from new CRM and KPI systems at Boston Institute of Analytics")),
    ("I grow the team",
     "I coach with dashboards and data. At BYJU'S I cut team attrition from 15% to under 5% in 4 months.",
     ("42%", "Productivity gain in a 20-person team at upGrad")),
]

ABOUT = [
    "I am Prashant. I started in sales in 2018 at BYJU'S, on the phone, with 150+ calls a day.",
    "Over the next six years I moved from B2C sales to B2B, then to running a region with 8 managers and 120 reps. At Boston Institute of Analytics I moved into strategy, as the Managing Director's key strategic partner.",
    "Today I live in Madrid. I am doing an International MBA at IE Business School, in Digital Business and International Transformation. I also cofounded BingeMind, an AI automation startup.",
    "Outside work, I organized blood donation drives with partner hospitals and the &ldquo;Run For All&rdquo; community marathon.",
]

FACTS = [
    ("Education", [
        ("IE Business School, Madrid", "International MBA, 2025 to 2026. GPA 3.66 of 4.0, GMAT 680, IE Merit Scholar. QS Global MBA rank 11 (2026)."),
        ("Dr. A.P.J. Abdul Kalam Technical University", "B.Tech, Electronics and Communication Engineering, 2013 to 2017. First Division."),
    ]),
    ("Awards", [
        ("Top 10 Manager nationwide", "BYJU'S"),
        ("Top 10 Business Development Associate nationwide", "BYJU'S"),
        ("Certificate of Excellence as Head of Strategy", "Boston Institute of Analytics"),
    ]),
    ("Languages", [("English", "C2"), ("Hindi", "Native"), ("Spanish", "B1")]),
    ("Tools", [
        ("CRM and prospecting", "Salesforce, HubSpot, LeadSquared, Lusha, ZoomInfo"),
        ("Analysis", "Financial modeling, SQL, Tableau, Advanced Excel, Six Sigma, Lean"),
    ]),
    ("Community", [
        ("Youth Empowerment and Education Trust", "Ran 10+ policy feedback sessions with the Ministry of Housing and Urban Affairs, with input from 500+ families."),
        ("PM Skill Development Scheme", "Trained 200+ students on sustainability and organized the &ldquo;Run For All&rdquo; marathon."),
        ("Community Health Consulting", "Organized 3+ blood donation drives with 100+ volunteers, who collected 250+ blood units."),
    ]),
]

TOOLS = ["Salesforce", "HubSpot", "LeadSquared", "Lusha", "ZoomInfo", "Financial modeling",
         "SQL", "Tableau", "Advanced Excel", "Six Sigma", "Lean"]

CONTACT_H2 = "Hiring for strategy or growth? Let's talk."
CONTACT_INTRO = ("Recruiters, hiring managers and founders: send me an email to book a meeting, "
                 "or message me on LinkedIn. I am in Madrid.")
