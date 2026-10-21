"""Option 2: Classic. The look and layout of the earlier design template (v2/index.html),
filled with Prashant's real content from content.py. Case pages are standalone pages
in the template's project-sheet style. CSS lives in option-2/style.css."""
import content as C

N = 2
NAME = "Classic"

ART = {
    "market-entry": """<rect width="840" height="360" fill="#0A1E4A"/>
<circle cx="620" cy="120" r="64" fill="#F1E9DB"/>
<polyline points="40,300 160,260 260,276 360,210 460,230 560,170 800,180" fill="none" stroke="#1F4FD8" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>""",
    "bank-partnerships": """<rect width="840" height="360" fill="#0A1E4A"/>
<circle cx="360" cy="180" r="110" fill="none" stroke="#1F4FD8" stroke-width="26"/>
<circle cx="480" cy="180" r="110" fill="none" stroke="#F1E9DB" stroke-width="26"/>""",
    "regional-growth": """<rect width="840" height="360" fill="#0A1E4A"/>
<polygon points="0,360 230,140 390,270 560,100 840,360" fill="#1F4FD8"/>
<polygon points="560,100 610,160 584,154 560,180 536,154 512,160" fill="#F1E9DB"/>
<path d="M20 110 C180 40 300 190 460 80 S720 50 820 90" fill="none" stroke="#F1E9DB" stroke-width="5"/>""",
    "mba-projects": """<rect width="840" height="360" fill="#0A1E4A"/>
<line x1="160" y1="310" x2="700" y2="310" stroke="#F1E9DB" stroke-width="3"/>
<line x1="160" y1="310" x2="160" y2="40" stroke="#F1E9DB" stroke-width="3"/>
<circle cx="280" cy="240" r="14" fill="#F1E9DB"/><circle cx="380" cy="190" r="20" fill="#F1E9DB"/>
<circle cx="480" cy="230" r="12" fill="#F1E9DB"/>
<path d="M590 60 C612 92 626 110 626 130 A36 36 0 0 1 554 130 C554 110 568 92 590 60 Z" fill="#1F4FD8"/>""",
}

CHIPS = {"market-entry": "Strategy", "bank-partnerships": "Partnerships",
         "regional-growth": "Sales leadership", "mba-projects": "MBA projects"}

MARK = ('<svg width="30" height="30" viewBox="0 0 30 30" aria-hidden="true"><circle cx="15" cy="15" r="14" fill="#1F4FD8"/>'
        '<path d="M15 4 L15 26 M4 15 L26 15" stroke="#F1E9DB" stroke-width="2" stroke-linecap="round"/></svg>')


def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#F1E9DB">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="style.css">
</head>
"""


def top(home):
    nav_home = "" if home else "index.html"
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="pv"><div class="pv-in"><a href="../index.html">&larr; Back to options</a><span>Option {N} of 4: {NAME}</span></div></div>
<div class="progress" aria-hidden="true"></div>
<header class="top">
  <div class="wrap">
    <a class="mark" href="{nav_home or '#top'}" aria-label="Prashant Kumar Jindal, home">{MARK}<span translate="no">Prashant K. Jindal</span></a>
    <nav class="nav" aria-label="Main">
      <a class="ul" href="{nav_home}#work">Work</a>
      <a class="ul" href="{nav_home}#record">Track record</a>
      <a class="ul" href="{nav_home}#about">About</a>
      <a class="pill" href="{C.MAILTO}">Book a meeting <span class="arr" aria-hidden="true">&rarr;</span></a>
    </nav>
  </div>
</header>
"""


def contact():
    return f"""<footer class="contact" id="contact">
  <div class="orb" aria-hidden="true"></div>
  <div class="wrap">
    <p class="eyebrow" style="color:rgba(241,233,219,.7)"><b style="color:#8FA9F5">05</b> &nbsp;Let&rsquo;s talk</p>
    <h2>Hiring for strategy<br>or <em>growth?</em></h2>
    <p class="lede">{C.CONTACT_INTRO}</p>
    <a class="pill light" href="{C.MAILTO}">Book a meeting <span class="arr" aria-hidden="true">&rarr;</span></a>
    <div class="ways">
      <a class="way" href="{C.MAILTO}"><span class="eyebrow">Book a meeting</span><strong>Pick a time</strong><small>Opens an email to me</small></a>
      <a class="way" href="mailto:{C.EMAIL}"><span class="eyebrow">Email</span><strong class="em">{C.EMAIL}</strong><small>For meetings and documents</small></a>
      <a class="way" href="{C.LINKEDIN}" rel="noopener"><span class="eyebrow">LinkedIn</span><strong>{C.LINKEDIN_LABEL}</strong><small>Profile</small></a>
    </div>
    <div class="foot">
      <span>&copy; 2026 Prashant Kumar Jindal, Madrid</span>
      <span class="foot-links"><a href="../index.html">Back to options</a><a href="#top">Back to top &uarr;</a></span>
    </div>
  </div>
</footer>
"""


def o2_index():
    stats = "".join(
        f'<div class="stat"><strong>{(p.strip() + "&nbsp;") if p else ""}{n}{s}</strong><span>{lbl}</span></div>'
        for p, n, s, lbl in C.STATS)
    cards = ""
    for i, c in enumerate(C.CASES):
        cards += f"""<a class="card reveal" href="{c['slug']}.html">
          <div class="art"><svg viewBox="0 0 840 360" preserveAspectRatio="xMidYMid slice" aria-hidden="true">{ART[c['slug']]}</svg></div>
          <div class="meta"><span class="num">{c['company']}, {c['years']}</span><span class="chip">{CHIPS[c['slug']]}</span></div>
          <h3>{c['home_title']}</h3>
          <p class="sub">{c['sum']}</p>
          <p class="res"><b>{c['res'][0]}</b> {c['res'][1]}</p>
          <span class="open"><i aria-hidden="true">&rarr;</i> Open case</span>
        </a>
"""
    rows = "".join(
        f'<div class="row reveal"><span class="num">{y}</span><div><h3>{r}</h3><p>{co}</p></div><p>{w}</p></div>'
        for y, r, co, w in C.CAREER)
    certs_data = [
        ("BYJU'S", "Top 10 Manager nationwide", "BYJU'S"),
        ("BYJU'S", "Top 10 Business Development Associate nationwide", "BYJU'S"),
        ("BIA", "Certificate of Excellence as Head of Strategy", "Boston Institute of Analytics"),
        ("IE", "IE Merit Scholar, International MBA", "IE Business School, 2025 to 2026"),
    ]
    certs = "".join(
        f'<article class="cert reveal"><div class="logo"><span class="lg">{lg}</span></div><h4>{h}</h4><p>{s}</p></article>'
        for lg, h, s in certs_data)
    bring = "".join(
        f'<div class="bring-i"><strong>{f}</strong><h3>{h}</h3><p>{t}</p><small>{pl}</small></div>'
        for h, t, (f, pl) in C.BRING)
    facts = "".join(
        f'<div><h4>{h}</h4><ul>' + "".join(f"<li><b>{a}</b> {b}</li>" for a, b in items) + "</ul></div>"
        for h, items in C.FACTS if h in ("Education", "Languages", "Tools", "Community"))
    return head(C.TITLE, C.DESC) + f"""<body id="top">
{top(True)}
<main id="main">
  <section class="hero">
    <div class="orb" aria-hidden="true"></div>
    <div class="wrap">
      <div class="hero-grid">
        <div>
          <p class="eyebrow fade"><b aria-hidden="true">&#9679;</b>&nbsp; Strategy and business development &nbsp;/&nbsp; EdTech</p>
          <h1>
            <span class="line"><span>From 150 calls a day</span></span>
            <span class="line"><span>to a <em>USD&nbsp;12.5M</em></span></span>
            <span class="line"><span>revenue book.</span></span>
          </h1>
          <div class="fade">
            <p class="lede">{C.HERO_LEDE}</p>
            <p class="for">This site is for
              <span class="rot" role="text" aria-label="recruiters, hiring managers and founders"><span class="rot-in" aria-hidden="true"><span>recruiters</span><span>hiring managers</span><span>founders</span><span>recruiters</span></span></span>
            </p>
            <div class="ctas">
              <a class="pill" href="{C.MAILTO}">Book a meeting <span class="arr" aria-hidden="true">&rarr;</span></a>
              <a class="pill ghost" href="#work">See the work</a>
              <a class="pill ghost" href="mailto:{C.EMAIL}">Email me</a>
            </div>
          </div>
        </div>
        <figure class="portrait" style="margin:0">
          <div class="arch"><img src="img/prashant.jpg" width="720" height="900" fetchpriority="high" alt="{C.PHOTO_ALT}"></div>
          <div class="sticker">
            <svg viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="46" fill="none" stroke="#1F4FD8" stroke-width="1.5"/><circle cx="50" cy="4" r="4" fill="#1F4FD8"/></svg>
            IE Merit Scholar
          </div>
        </figure>
      </div>
      <div class="stats fade">{stats}</div>
    </div>
    <div class="marquee" aria-hidden="true">
      <div class="track">
        <span>Market entry</span><span>Partnerships</span><span>Revenue growth</span><span>Sales leadership</span><span>Go to market</span><span>EdTech</span>
        <span>Market entry</span><span>Partnerships</span><span>Revenue growth</span><span>Sales leadership</span><span>Go to market</span><span>EdTech</span>
      </div>
    </div>
  </section>

  <section class="block" id="work" aria-labelledby="work-title">
    <div class="wrap">
      <div class="head reveal">
        <div>
          <p class="eyebrow"><b>01</b> &nbsp;Selected work</p>
          <h2 id="work-title">Four cases,<br><em>results</em> inside.</h2>
        </div>
        <p>{C.WORK_INTRO}</p>
      </div>
      <div class="grid">
{cards}      </div>
    </div>
  </section>

  <section class="block alt" id="record" aria-labelledby="record-title">
    <div class="wrap">
      <div class="head reveal">
        <div>
          <p class="eyebrow"><b>02</b> &nbsp;Track record</p>
          <h2 id="record-title">From sales calls to<br>the <em>strategy</em> table.</h2>
        </div>
        <p>{C.CAREER_INTRO}</p>
      </div>
      <div class="rows">{rows}</div>
    </div>
  </section>

  <section class="block" id="awards" aria-labelledby="awards-title">
    <div class="wrap">
      <div class="head reveal">
        <div>
          <p class="eyebrow"><b>03</b> &nbsp;Awards</p>
          <h2 id="awards-title">Recognition,<br><em>earned.</em></h2>
        </div>
        <p>Awards from BYJU'S and Boston Institute of Analytics, and a merit scholarship at IE Business School.</p>
      </div>
      <div class="certs">{certs}</div>
    </div>
  </section>

  <section class="block alt" id="about" aria-labelledby="about-title">
    <div class="wrap">
      <div class="head reveal">
        <div>
          <p class="eyebrow"><b>04</b> &nbsp;About me</p>
          <h2 id="about-title">What I bring<br>to a <em>team.</em></h2>
        </div>
      </div>
      <div class="quotes">
        <div class="qb reveal">
          <p class="big">{C.ABOUT[0]}</p>
          <p>{C.ABOUT[1]}</p>
          <p>{C.ABOUT[2]}</p>
          <p>{C.ABOUT[3]}</p>
        </div>
        <div class="qb light reveal">
          <div class="bring">{bring}</div>
        </div>
      </div>
      <div class="facts-row reveal">{facts}</div>
    </div>
  </section>
</main>

{contact()}</body>
</html>
"""


def o2_case(i):
    c = C.CASES[i]
    nx = C.CASES[(i + 1) % len(C.CASES)]
    meta = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in c["meta"])
    figs = "".join(f'<li><b>{f}</b><span>{l}</span></li>' for f, l in c["figs"])
    chapters = "".join(
        f"<h3>{h}</h3>" + (f'<p class="role">{r}</p>' if r else "") + "<ul class=\"pts\">" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
        for h, r, items in c["chapters"])
    tags = "".join(f'<span class="chip">{t}</span>' for t in c["tags"])
    note = f'<p class="note">{c["note"]}</p>' if c["note"] else ""
    return head(f'{c["title"]} | Prashant Kumar Jindal', c["sum"]) + f"""<body id="top" class="casepage">
{top(False)}
<main id="main" class="sheet-page">
  <div class="wrap">
    <div class="sheet-bar"><span class="num">Case {i + 1} of 4</span><a class="close" href="index.html#work">All work <i aria-hidden="true">&times;</i></a></div>
    <div class="stagger">
      <p class="eyebrow"><b>{c['company']}</b> &nbsp;/&nbsp; {c['years']}</p>
      <h1>{c['title']}</h1>
      <p class="lede">{c['lede']}</p>{note}
      <div class="hero-art"><svg viewBox="0 0 840 360" preserveAspectRatio="xMidYMid slice" aria-hidden="true">{ART[c['slug']]}</svg></div>
      <div class="cols">
        <div>
          <dl class="facts">{meta}</dl>
          <ul class="files" aria-label="Key figures">{figs}</ul>
        </div>
        <div class="body">
          {chapters}
          <div class="chips">{tags}</div>
          <p class="ask">{c['ask']}</p>
        </div>
      </div>
      <a class="next" href="{nx['slug']}.html"><small class="eyebrow">Next case</small><span>{nx['title']} &rarr;</span></a>
    </div>
  </div>
</main>
{contact()}</body>
</html>
"""
