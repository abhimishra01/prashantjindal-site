"""Builds option-1 (Annual Report), option-2 (Classic) and option-3 (Studio Board) from content.py.
Option-4 is the earlier Version 2, copied by hand from v2-miranda.

Run: python3 _build/build.py   (from the repo root or anywhere)
CSS, JS, fonts and images live in each option folder and are edited by hand.
"""
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(__file__))
import content as C  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OPTIONS = {
    1: {"name": "The Annual Report", "theme": "#f2ede3"},
    2: {"name": "Classic", "theme": "#F1E9DB"},
    3: {"name": "The Studio Board", "theme": "#ece6dc"},
}


def head(n, title, desc, preload_img=False, fonts=()):
    pre = "".join(
        f'<link rel="preload" href="fonts/{f}" as="font" type="font/woff2" crossorigin>\n' for f in fonts)
    img = '<link rel="preload" as="image" href="img/prashant.jpg">\n' if preload_img else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="{OPTIONS[n]['theme']}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<script>if(window.matchMedia&&matchMedia("(prefers-reduced-motion: no-preference)").matches&&"IntersectionObserver" in window)document.documentElement.classList.add("motion")</script>
{pre}{img}<link rel="stylesheet" href="style.css">
<script src="app.js" defer></script>
</head>
"""


def preview_bar(n):
    return (f'<div class="pv"><div class="pv-in"><a href="../index.html">&larr; Back to options</a>'
            f'<span>Option {n} of 4: {OPTIONS[n]["name"]}</span></div></div>\n')


def skip():
    return '<a class="skip" href="#main">Skip to content</a>\n'


def count(prefix, num, suffix, small_prefix=True):
    p = f'<small>{prefix.strip()}</small>' if (prefix and small_prefix) else prefix
    return f'{p}<span data-count>{num}</span>{suffix}'


def ol(items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def facts_lists():
    out = []
    for h, items in C.FACTS:
        lis = "".join(f"<li><strong>{a}</strong>{b}</li>" for a, b in items)
        out.append((h, f"<ul>{lis}</ul>"))
    return out


def next_case(i):
    return C.CASES[(i + 1) % len(C.CASES)]


def footer(cls="foot"):
    return (f'<footer class="{cls}"><div class="wrap"><span>&copy; 2026 Prashant Kumar Jindal, Madrid</span>'
            f'<span class="foot-links"><a href="../index.html">Back to options</a><a href="#main">Back to top</a></span></div></footer>\n')


def contact_lines():
    return (f'<a href="mailto:{C.EMAIL}"><span class="k">Email</span><span class="v">{C.EMAIL}</span></a>'
            f'<a href="{C.LINKEDIN}" rel="noopener"><span class="k">LinkedIn</span><span class="v">{C.LINKEDIN_LABEL}</span></a>')


# ---------------------------------------------------------------- Option 1
def o1_header():
    return f"""<header class="mast"><div class="wrap">
<a class="name" href="index.html">Prashant Kumar Jindal</a>
<nav aria-label="Main"><a href="index.html#work">Work</a><a href="index.html#career">Career</a><a href="index.html#about">About</a><a class="btn sm" href="{C.MAILTO}">Book a meeting</a></nav>
</div></header>
"""


def o1_index():
    stats = "".join(
        f'<div class="kf" data-reveal><span class="fig">{count(p, n, s)}</span><p>{lbl}</p></div>'
        for p, n, s, lbl in C.STATS)
    career = "".join(
        f'<li data-reveal><span class="yr">{y}</span><div><h3>{r}</h3><p class="co">{co}</p></div><p class="what">{w}</p></li>'
        for y, r, co, w in C.CAREER)
    cases = ""
    for i, c in enumerate(C.CASES):
        cases += (f'<a class="story s{i+1}" href="{c["slug"]}.html" data-reveal>'
                  f'<p class="where">{c["company"]}, {c["years"]}</p>'
                  f'<h3>{c["home_title"]}</h3><p class="sum">{c["sum"]}</p>'
                  f'<p class="res"><span class="fig">{c["res"][0]}</span><span>{c["res"][1]}</span></p>'
                  f'<span class="more">Read the case <span aria-hidden="true">&rarr;</span></span></a>')
    bring = "".join(
        f'<div class="tenet" data-reveal><p class="fig">{f}</p><div><h3>{h}</h3><p>{t}</p><p class="proof">{pl}</p></div></div>'
        for h, t, (f, pl) in C.BRING)
    about = "".join(f"<p>{p}</p>" for p in C.ABOUT)
    facts = "".join(f'<div class="fact"><h3>{h}</h3>{ul}</div>' for h, ul in facts_lists())
    return head(1, C.TITLE, C.DESC, True, ("newsreader-latin-opsz-normal.woff2", "public-sans-latin-wght-normal.woff2")) + f"""<body>
{skip()}{preview_bar(1)}{o1_header()}<main id="main">

<section class="hero" aria-labelledby="hero-title"><div class="wrap">
<div class="hero-copy">
<p class="kicker">Strategy and business development</p>
<h1 id="hero-title">{C.HERO_H1_PRE}<em>{C.HERO_H1_EM}</em>{C.HERO_H1_POST}</h1>
<p class="lede">{C.HERO_LEDE}</p>
<div class="ctas"><a class="btn" href="{C.MAILTO}">Book a meeting <span aria-hidden="true">&rarr;</span></a><a class="link" href="#work">See the work</a></div>
</div>
<figure class="photo"><img src="img/prashant.jpg" width="720" height="900" fetchpriority="high" alt="{C.PHOTO_ALT}"></figure>
</div></section>

<section class="figures" aria-label="Results in numbers"><div class="wrap">{stats}</div></section>

<section class="sec" id="work" aria-labelledby="work-title"><div class="wrap">
<h2 id="work-title">Selected work</h2>
<p class="intro">{C.WORK_INTRO}</p>
<div class="stories">{cases}</div>
</div></section>

<section class="sec ledger-sec" id="career" aria-labelledby="career-title"><div class="wrap">
<h2 id="career-title">{C.CAREER_H2}</h2>
<p class="intro">{C.CAREER_INTRO}</p>
<ol class="ledger">{career}</ol>
</div></section>

<section class="sec" aria-labelledby="bring-title"><div class="wrap">
<h2 id="bring-title">{C.BRING_H2}</h2>
<div class="tenets">{bring}</div>
</div></section>

<section class="sec about" id="about" aria-labelledby="about-title"><div class="wrap">
<div class="bio"><h2 id="about-title">About me</h2>{about}</div>
<div class="facts">{facts}</div>
</div></section>

<section class="contact" id="contact" aria-labelledby="contact-title"><div class="wrap">
<h2 id="contact-title">{C.CONTACT_H2}</h2>
<p class="intro">{C.CONTACT_INTRO}</p>
<a class="btn light" href="{C.MAILTO}">Book a meeting <span aria-hidden="true">&rarr;</span></a>
<div class="lines">{contact_lines()}</div>
</div></section>
</main>
{footer()}</body>
</html>
"""


def o1_case(i):
    c = C.CASES[i]
    nx = next_case(i)
    meta = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in c["meta"])
    chapters = "".join(
        f'<section class="chapter" data-reveal><h2>{h}</h2>' + (f'<p class="role">{r}</p>' if r else "") + ol(items) + "</section>"
        for h, r, items in c["chapters"])
    figs = "".join(f'<div class="kfig"><span class="fig">{f}</span><span>{l}</span></div>' for f, l in c["figs"])
    tags = "".join(f"<li>{t}</li>" for t in c["tags"])
    note = f'<p class="note">{c["note"]}</p>' if c["note"] else ""
    return head(1, f'{c["title"]} | Prashant Kumar Jindal', c["sum"], False, ("newsreader-latin-opsz-normal.woff2",)) + f"""<body class="casepage">
{skip()}{preview_bar(1)}{o1_header()}<main id="main">
<article>
<header class="case-head"><div class="wrap">
<a class="crumb" href="index.html#work">&larr; All work</a>
<p class="kicker">{c["company"]}, {c["years"]}</p>
<h1>{c["title"]}</h1>
<p class="lede">{c["lede"]}</p>{note}
<dl class="meta">{meta}</dl>
</div></header>
<div class="case-body"><div class="wrap">
<div class="chapters">{chapters}</div>
<aside class="side" aria-label="Key figures">{figs}
<ul class="tags" aria-label="Skills used">{tags}</ul>
<p class="ask">{c["ask"]}</p></aside>
</div></div>
</article>
<nav class="next" aria-label="Next case"><div class="wrap"><a href="{nx["slug"]}.html"><span class="k">Next case</span><span class="t">{nx["title"]} <span aria-hidden="true">&rarr;</span></span></a></div></nav>
</main>
{footer()}</body>
</html>
"""


from classic import o2_index, o2_case  # noqa: E402


# ---------------------------------------------------------------- Option 3 (Studio Board)
def o3_header():
    return f"""<header class="bar"><div class="wrap"><div class="bar-in">
<a class="chip-name" href="index.html"><span class="mono" aria-hidden="true">PJ</span><span>Prashant Kumar Jindal</span></a>
<nav aria-label="Main"><a href="index.html#career">Career</a><a href="index.html#work">Work</a><a href="index.html#about">About</a><a class="btn sm" href="{C.MAILTO}">Book a meeting</a></nav>
</div></div></header>
"""


def o3_index():
    tints = ["t-navy", "t-card", "t-sky", "t-card"]
    stats = "".join(
        f'<div class="tile stat {tints[k]}" data-reveal><span class="fig">{count(p, n, s)}</span><p>{lbl}</p></div>'
        for k, (p, n, s, lbl) in enumerate(C.STATS))
    tools = "".join(f"<li>{t}</li>" for t in C.TOOLS)
    career = "".join(
        f'<li class="cc{" last" if k == len(C.CAREER) - 1 else ""}"><span class="yr">{y}</span><h3>{r}</h3><p class="co">{co}</p><p class="what">{w}</p></li>'
        for k, (y, r, co, w) in enumerate(C.CAREER))
    wtint = ["w-navy", "w-card", "w-card", "w-sky"]
    cases = "".join(
        f'<a class="tile wcard {wtint[k]}" href="{c["slug"]}.html" data-reveal><span class="chip">{c["company"]}, {c["years"]}</span>'
        f'<h3>{c["home_title"]}</h3><p class="sum">{c["sum"]}</p>'
        f'<p class="res"><span class="fig">{c["res"][0]}</span><span>{c["res"][1]}</span></p><span class="go" aria-hidden="true">&rarr;</span></a>'
        for k, c in enumerate(C.CASES))
    bring = "".join(
        f'<div class="b"><p class="fig">{f}</p><h3>{h}</h3><p>{t}</p><p class="proof">{pl}</p></div>'
        for h, t, (f, pl) in C.BRING)
    about = "".join(f"<p>{p}</p>" for p in C.ABOUT)
    facts = "".join(
        f'<details{" open" if k == 0 else ""}><summary>{h}</summary>{ul}</details>'
        for k, (h, ul) in enumerate(facts_lists()))
    return head(3, C.TITLE, C.DESC, True, ("plus-jakarta-sans-latin-wght-normal.woff2",)) + f"""<body>
{skip()}{preview_bar(3)}{o3_header()}<main id="main">

<section class="wrap bento hero-b" aria-labelledby="hero-title">
<div class="tile intro-t" data-reveal>
<h1 id="hero-title">{C.HERO_H1_PRE}<em>{C.HERO_H1_EM}</em>{C.HERO_H1_POST}</h1>
<p class="lede">{C.HERO_LEDE}</p>
<div class="ctas"><a class="btn" href="{C.MAILTO}">Book a meeting <span aria-hidden="true">&rarr;</span></a><a class="btn ghost" href="#work">See the work</a></div>
</div>
<figure class="tile photo-t" data-reveal><img src="img/prashant.jpg" width="720" height="900" fetchpriority="high" alt="{C.PHOTO_ALT}"></figure>
{stats}
<div class="tile tools-t" data-reveal><p class="tl-lbl">Tools I work with</p><div class="mq"><ul class="mq-track">{tools}</ul><ul class="mq-track" aria-hidden="true">{tools}</ul></div></div>
</section>

<section class="sec" id="career" aria-labelledby="career-title"><div class="wrap">
<div class="sec-head"><div><h2 id="career-title">{C.CAREER_H2}</h2><p class="intro">{C.CAREER_INTRO}</p></div>
<div class="rail-btns"><button type="button" class="rb" data-dir="-1" aria-label="Previous steps">&larr;</button><button type="button" class="rb" data-dir="1" aria-label="Next steps">&rarr;</button></div></div>
</div>
<ol class="rail-x" tabindex="0" aria-label="Career steps, scroll sideways">{career}</ol>
</section>

<section class="sec" id="work" aria-labelledby="work-title"><div class="wrap">
<h2 id="work-title">Selected work</h2>
<p class="intro">{C.WORK_INTRO}</p>
<div class="works">{cases}</div>
</div></section>

<section class="sec" aria-labelledby="bring-title"><div class="wrap">
<h2 id="bring-title">{C.BRING_H2}</h2>
<div class="tile bring" data-reveal>{bring}</div>
</div></section>

<section class="sec" id="about" aria-labelledby="about-title"><div class="wrap about-g">
<div class="tile bio" data-reveal><h2 id="about-title">About me</h2>{about}</div>
<div class="tile facts" data-reveal>{facts}</div>
</div></section>

<section class="sec" id="contact" aria-labelledby="contact-title"><div class="wrap">
<div class="tile contact" data-reveal>
<h2 id="contact-title">{C.CONTACT_H2}</h2>
<p class="intro">{C.CONTACT_INTRO}</p>
<a class="btn beam" href="{C.MAILTO}">Book a meeting <span aria-hidden="true">&rarr;</span></a>
<div class="lines">{contact_lines()}</div>
</div>
</div></section>
</main>
{footer()}</body>
</html>
"""


def o3_case(i):
    c = C.CASES[i]
    nx = next_case(i)
    meta = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in c["meta"])
    chapters = "".join(
        f'<section class="tile chapter" data-reveal><h2>{h}</h2>' + (f'<p class="role">{r}</p>' if r else "") + ol(items) + "</section>"
        for h, r, items in c["chapters"])
    tint = ["t-navy", "t-sky", "t-card", "t-card", "t-card"]
    figs = "".join(f'<div class="tile kfig {tint[k]}" data-reveal><span class="fig">{f}</span><span>{l}</span></div>'
                   for k, (f, l) in enumerate(c["figs"]))
    tags = "".join(f"<li>{t}</li>" for t in c["tags"])
    note = f'<p class="note">{c["note"]}</p>' if c["note"] else ""
    return head(3, f'{c["title"]} | Prashant Kumar Jindal', c["sum"], False, ("plus-jakarta-sans-latin-wght-normal.woff2",)) + f"""<body class="casepage">
{skip()}{preview_bar(3)}{o3_header()}<main id="main">
<section class="wrap bento case-b">
<div class="tile title-t" data-reveal>
<a class="crumb" href="index.html#work">&larr; All work</a>
<span class="chip">{c["company"]}, {c["years"]}</span>
<h1>{c["title"]}</h1>
<p class="lede">{c["lede"]}</p>{note}
</div>
<div class="tile meta-t t-navy" data-reveal><dl class="meta">{meta}</dl></div>
</section>
<section class="wrap figs n{len(c["figs"])}" aria-label="Key figures">{figs}</section>
<div class="wrap chapters">{chapters}</div>
<section class="wrap"><div class="tile skills" data-reveal><ul class="tags" aria-label="Skills used">{tags}</ul><p class="ask">{c["ask"]}</p></div></section>
<nav class="wrap next" aria-label="Next case"><a class="tile" href="{nx["slug"]}.html"><span class="k">Next case</span><span class="t">{nx["title"]}</span><span class="go" aria-hidden="true">&rarr;</span></a></nav>
</main>
{footer()}</body>
</html>
"""


def write(path, text):
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as f:
        f.write(text)


def main():
    builders = {1: (o1_index, o1_case), 2: (o2_index, o2_case), 3: (o3_index, o3_case)}
    for n, (idx, case) in builders.items():
        write(f"option-{n}/index.html", idx())
        for i, c in enumerate(C.CASES):
            write(f"option-{n}/{c['slug']}.html", case(i))
        if n != 2:
            shutil.copy(os.path.join(ROOT, "_build", "app.js"), os.path.join(ROOT, f"option-{n}", "app.js"))
    print("built")


if __name__ == "__main__":
    main()
