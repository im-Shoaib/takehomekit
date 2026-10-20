#!/usr/bin/env python3
"""Static site generator for TakehomeKit. Outputs plain HTML into ../takehome.
Change SITE / EMAIL below if needed, then run:  python3 build.py"""
import json, os, html, re
from tools_content import TOOLS, CATEGORIES, I
import tools_more  # noqa: F401  (appends round-two tools to TOOLS)
from blog_content import POSTS

SITE = "https://takehomekit.online"      # <-- your domain, no trailing slash
BRAND = "TakehomeKit"
EMAIL = "hello@takehomekit.online"        # <-- your contact email
GA_ID = "G-51743TY2ER"                   # <-- Google Analytics 4 Measurement ID ("" to disable)
OUT = os.environ.get("SITE_OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "takehome"))
TODAY = "2026-10-15"
UPDATED_HUMAN = "October 2026"
VERSION = "20261015i"

e = html.escape
CAT_ORDER = [c["id"] for c in CATEGORIES]
TOOLS.sort(key=lambda t: CAT_ORDER.index(t["cat"]))
BY_SLUG = {t["slug"]: t for t in TOOLS}
POSTS.sort(key=lambda p: p["date"], reverse=True)

# Scheduled publishing: posts dated in the future (Pakistan time) are left out of the build.
# Override for testing with BUILD_DATE=YYYY-MM-DD.
import datetime as _dt
PUBLISH_DATE = os.environ.get("BUILD_DATE") or (_dt.datetime.now(_dt.timezone.utc) + _dt.timedelta(hours=5)).date().isoformat()
SCHEDULED = sorted((p for p in POSTS if p["date"] > PUBLISH_DATE), key=lambda p: p["date"])
POSTS[:] = [p for p in POSTS if p["date"] <= PUBLISH_DATE]


def human_date(d):
    import datetime
    return datetime.date.fromisoformat(d).strftime("%-d %B %Y")


def read_time(p):
    words = len(re.sub(r"<[^>]+>", " ", p["body"]).split()) + sum(len((q + a).split()) for q, a in p.get("faq", []))
    return max(3, round(words / 220))


def logo_svg(uid):
    return ('<svg viewBox="0 0 40 40" aria-hidden="true"><defs><linearGradient id="lg' + uid + '" x1="0" y1="0" x2="1" y2="1">'
            '<stop offset="0" stop-color="#f3cf91"/><stop offset=".5" stop-color="#f4a3b4"/><stop offset="1" stop-color="#a08bff"/></linearGradient></defs>'
            '<rect width="40" height="40" rx="12" fill="url(#lg' + uid + ')"/>'
            '<path d="M14 11v18" stroke="#1a1033" stroke-width="3.6" stroke-linecap="round"/>'
            '<path d="M27 11l-8.5 9L27 29" fill="none" stroke="#1a1033" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/>'
            '<circle cx="30" cy="20" r="2.2" fill="#1a1033"/></svg>')


def wordmark(uid):
    return f'{logo_svg(uid)}<span>takehome<span class="kit">kit</span></span>'


CHEV = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 8l5 5 5-5"/></svg>'
MENU = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h10"/></svg>'
ARROW = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 10h12M11 5l5 5-5 5"/></svg>'
CHECK = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><circle cx="10" cy="10" r="8"/><path d="M6.5 10.2l2.4 2.3 4.6-4.8"/></svg>'
SEARCH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>'


def url(path):
    return SITE + path


def mega_menu():
    cols = ""
    for c in CATEGORIES:
        lis = "".join(f'<li><a href="/{t["slug"]}/"><span class="mi">{t["icon"]}</span>{e(t["short"])}</a></li>' for t in TOOLS if t["cat"] == c["id"])
        cols += f'<div><h2>{e(c["name"])}</h2><ul>{lis}</ul></div>'
    mobile = ('<div class="mobile-links"><a class="btn btn-small" href="/#tools">All tools</a><a class="btn btn-ghost btn-small" href="/blog/">Blog &amp; guides</a></div>')
    return f'<div class="mega" id="mega" role="region" aria-label="All tools">{mobile}{cols}</div>'


def header(active=""):
    links = [("/fiverr-fee-calculator/", "Fiverr fees"), ("/payoneer-to-pkr-calculator/", "Payoneer to PKR"), ("/invoice-generator/", "Invoice"), ("/blog/", "Blog")]
    nav = f'<button type="button" data-mega aria-expanded="false" aria-controls="mega">All tools {CHEV}</button>'
    nav += "".join(f'<a href="{h}"' + (' aria-current="page"' if h == active else '') + f'>{t}</a>' for h, t in links)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
<div class="wrap"><div class="nav-shell">
<a class="logo" href="/" aria-label="{BRAND} home">{wordmark("h")}</a>
<nav class="nav" aria-label="Main">{nav}</nav>
<a class="btn btn-small header-cta" href="/#tools">Explore tools</a>
<button class="icon-btn menu-btn" type="button" data-mega aria-label="Open menu" aria-expanded="false" aria-controls="mega">{MENU}</button>
</div></div>
{mega_menu()}
</header>'''


def footer():
    def col(title, cats):
        lis = "".join(f'<li><a href="/{t["slug"]}/">{e(t["short"])}</a></li>' for t in TOOLS if t["cat"] in cats)
        return f'<div><h2>{title}</h2><ul>{lis}</ul></div>'
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div class="foot-brand"><a class="logo" href="/" aria-label="{BRAND} home">{wordmark("f")}</a>
<p>Free calculators, generators and gig tools for freelancers on Fiverr, Upwork and beyond. Everything runs in your browser — nothing you type is uploaded.</p></div>
{col("Fees &amp; payments", ("fees", "payments"))}
{col("Pricing &amp; documents", ("pricing", "documents"))}
{col("Gig, profile &amp; tax", ("gig", "tax"))}
<div><h2>Company</h2><ul><li><a href="/blog/">Blog &amp; guides</a></li><li><a href="/about/">About</a></li><li><a href="/contact/">Contact</a></li><li><a href="/privacy-policy/">Privacy policy</a></li><li><a href="/terms/">Terms of use</a></li><li><a href="/sitemap.xml">Sitemap</a></li></ul></div>
</div>
<div class="foot-bottom"><span>© {TODAY[:4]} {BRAND}. Not affiliated with Fiverr, Upwork, Payoneer, Wise or any platform named on this site.</span><span>Fees checked {UPDATED_HUMAN}</span></div>
</div></footer>'''


def ga_tag():
    if not GA_ID:
        return ""
    return (f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>\n'
            f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA_ID}');</script>")


def page(path, title, desc, body, schema=None, scripts=(), active="", noindex=False, og_type="website", og_image="/assets/img/og.png", preload=""):
    canon = url(path)
    ld = "".join('<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False, separators=(",", ":")) + '</script>\n' for s in (schema or []))
    js = "".join(f'<script src="{s}?v={VERSION}" defer></script>' for s in ("/assets/js/core.js",) + tuple(scripts))
    robots = '<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{robots}
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#0a0918">
<meta name="color-scheme" content="dark">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITE}{og_image}">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="/assets/img/icon-180.png">
<link rel="manifest" href="/site.webmanifest">
<script>document.documentElement.classList.add("js")</script>
{ga_tag()}
<link rel="preload" href="/assets/fonts/poppins-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/poppins-700.woff2" as="font" type="font/woff2" crossorigin>
{preload}<link rel="stylesheet" href="/assets/css/style.css?v={VERSION}">
{ld}</head>
<body>
{header(active)}
<main id="main">
{body}
</main>
{footer()}
{js}
</body>
</html>
'''


def crumbs(items):
    lis = ""
    for i, (name, href) in enumerate(items):
        lis += f'<li><a href="{href}">{e(name)}</a></li>' if href and i < len(items) - 1 else f'<li aria-current="page">{e(name)}</li>'
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{lis}</ol></nav>'


def breadcrumb_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": url(h)} for i, (n, h) in enumerate(items)]}


def faq_html(faqs):
    out = '<section class="faq" aria-labelledby="faq-h"><h2 id="faq-h">Frequently asked questions</h2>'
    for q, a in faqs:
        out += f'<details><summary>{e(q)}</summary><div><p>{a}</p></div></details>'
    return out + '</section>'


def faq_ld(faqs):
    strip = lambda s: re.sub(r"<[^>]+>", "", s)
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faqs]}


def tcard(t):
    terms = (t["short"] + " " + t["blurb"] + " " + t["h1"] + " " + t["cat"]).lower()
    pop = '<span class="pill gold">Popular</span>' if t.get("popular") else ''
    return (f'<li data-search="{e(terms)}"><a class="tcard" href="/{t["slug"]}/">{pop}<span class="ti">{t["icon"]}</span>'
            f'<h3>{e(t["short"])}</h3><p>{e(t["blurb"])}</p><span class="go">Open tool {ARROW}</span></a></li>')


def guides_box(slug):
    ps = [p for p in POSTS if slug in p["tools"]][:2]
    if not ps:
        return ""
    lis = "".join(f'<li><a href="/blog/{p["slug"]}/"><span class="mi">{I[p["icon"]]}</span>{e(p["h1"][0].upper() + p["h1"][1:])}</a></li>' for p in ps)
    return f'<div class="aside-box"><h2>Guides</h2><ul class="rel">{lis}</ul></div>'


def post_card(p, big=False):
    src = p["image"] + (".webp" if big else "-card.webp")
    cover = (f'<img src="{src}" alt="{e(p["alt"])}" width="{1600 if big else 800}" height="{900 if big else 450}" loading="{"eager" if big else "lazy"}" decoding="async">'
             if p.get("image") else f'<span class="pci">{I[p["icon"]]}</span>')
    return (f'<li><a class="pcard{" pcard-big" if big else ""}" href="/blog/{p["slug"]}/"><span class="pcover{" has-img" if p.get("image") else ""}">{cover}<span class="pill">{e(p["cat"])}</span></span>'
            f'<span class="pbody"><span class="pmeta">{human_date(p["date"])} · {read_time(p)} min read</span><h3>{e(p["h1"][0].upper() + p["h1"][1:])}</h3><p>{e(p["desc"])}</p>'
            f'<span class="go">Read guide {ARROW}</span></span></a></li>')


def build_blog_index():
    path = "/blog/"
    bc = [("Home", "/"), ("Blog", path)]
    first, rest = POSTS[0], POSTS[1:]
    body = f'''<div class="wrap">
{crumbs(bc)}
<header class="page-hero hero-in">
<h1>Guides for freelancers who want to <span class="grad-text">keep more.</span></h1>
<p class="lede">Practical, up-to-date guides on fees, payments, pricing, winning clients and tax — each one paired with a free tool so you can act on it straight away.</p>
</header>
<ul class="post-grid">{post_card(first, True)}{"".join(post_card(p) for p in rest)}</ul>
<section class="cta-band reveal">
<h2>Put the guides to work.</h2>
<p>{len(TOOLS)} free calculators and generators — fees, payouts, pricing, invoices and tax.</p>
<div class="btns"><a class="btn" href="/#tools">Browse all tools {ARROW}</a></div>
</section>
</div>'''
    schema = [breadcrumb_ld(bc), {"@context": "https://schema.org", "@type": "Blog", "name": f"{BRAND} Blog", "url": url(path),
              "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": url(f'/blog/{p["slug"]}/'), "datePublished": p["date"]} for p in POSTS]}]
    return page(path, f"Freelancer Guides — Fees, Payoneer, Pricing & Tax | {BRAND} Blog",
                "Practical guides for freelancers: withdrawing from Fiverr in Pakistan, PSEB tax registration, pricing your services, Upwork proposals, Fiverr gig SEO and invoicing.",
                body, schema, active="/blog/")


def build_post(p):
    path = f'/blog/{p["slug"]}/'
    bc = [("Home", "/"), ("Blog", "/blog/"), (p["cat"], "/blog/"), (p["h1"], path)]
    bc_short = [("Home", "/"), ("Blog", "/blog/"), (p["h1"][0].upper() + p["h1"][1:], path)]
    tools = "".join(f'<li><a href="/{s}/"><span class="mi">{BY_SLUG[s]["icon"]}</span>{e(BY_SLUG[s]["short"])}</a></li>' for s in p["tools"] if s in BY_SLUG)
    more = [q for q in POSTS if q["slug"] != p["slug"]][:3]
    faq = faq_html(p["faq"]) if p.get("faq") else ""
    hero = (f'<figure class="post-cover hero-in"><img src="{p["image"]}.webp" alt="{e(p["alt"])}" width="1600" height="900" fetchpriority="high" decoding="async"></figure>'
            if p.get("image") else "")
    body = f'''<div class="wrap">
{crumbs(bc_short)}
<header class="page-hero post-hero hero-in">
<div class="post-meta"><span class="pill gold">{e(p["cat"])}</span><span>{human_date(p["date"])}</span><span>{read_time(p)} min read</span><span>By the {BRAND} team</span></div>
<h1>{e(p["h1"][0].upper() + p["h1"][1:])}</h1>
<p class="lede">{p["lede"]}</p>
</header>
{hero}
<div class="content post-content">
<article class="prose">
{p["body"]}
{faq}
<p class="disclaimer">Fees, limits and rules change. We check them regularly and date every update, but always confirm the final number with the platform, your provider or an adviser before you rely on it.</p>
</article>
<aside class="aside"><div class="aside-inner">
<div class="aside-box toc"><h2>In this guide</h2><ol id="toc"></ol></div>
<div class="aside-box"><h2>Tools for this guide</h2><ul class="rel">{tools}</ul></div>
</div></aside>
</div>
<section class="more-posts reveal" aria-labelledby="more-h"><h2 id="more-h">More guides</h2><ul class="post-grid">{"".join(post_card(q) for q in more)}</ul></section>
</div>'''
    schema = [
        {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"], "description": p["desc"],
         "datePublished": p["date"], "dateModified": p.get("updated", p["date"]), "mainEntityOfPage": url(path),
         "image": SITE + (p["image"] + "-og.jpg" if p.get("image") else "/assets/img/og.png"), "author": {"@type": "Organization", "name": BRAND, "url": SITE + "/"},
         "publisher": {"@type": "Organization", "name": BRAND, "logo": {"@type": "ImageObject", "url": SITE + "/assets/img/icon-512.png"}}},
        breadcrumb_ld(bc_short),
    ]
    if p.get("faq"):
        schema.append(faq_ld(p["faq"]))
    og = p["image"] + "-og.jpg" if p.get("image") else "/assets/img/og.png"
    pre = f'<link rel="preload" as="image" href="{p["image"]}.webp" fetchpriority="high">\n' if p.get("image") else ""
    return page(path, p["title"], p["desc"], body, schema, active="/blog/", og_type="article", og_image=og, preload=pre)


def build_tool(t):
    path = f'/{t["slug"]}/'
    cat = next(c for c in CATEGORIES if c["id"] == t["cat"])
    bc = [("Home", "/"), (cat["name"], "/#" + cat["id"]), (t["short"], path)]
    rel = "".join(f'<li><a href="/{s}/"><span class="mi">{BY_SLUG[s]["icon"]}</span>{e(BY_SLUG[s]["short"])}</a></li>' for s in t["related"] if s in BY_SLUG)
    wide = " tool-wide" if t.get("wide") else ""
    body = f'''<div class="wrap">
{crumbs(bc)}
<header class="page-hero hero-in">
<h1>{e(t["h1"])}</h1>
<p class="lede">{t["lede"]}</p>
<div class="chips"><span class="chip">{CHECK}Free forever</span><span class="chip">{CHECK}No sign-up</span><span class="chip">{CHECK}Private — runs in your browser</span><span class="chip">{CHECK}Updated {UPDATED_HUMAN}</span></div>
</header>
<section class="tool{wide}" aria-label="{e(t["short"])}">
{t["ui"]}
</section>
<div class="content">
<article class="prose reveal">
{t["content"]}
{faq_html(t["faq"])}
<p class="disclaimer">{BRAND} is independent and not affiliated with Fiverr, Upwork, Payoneer, Wise or any other company mentioned. Fees, limits and tax rules change; we check them regularly, but always confirm the final number with the platform or an adviser before you rely on it.</p>
</article>
<aside class="aside"><div class="aside-inner">
<div class="aside-box toc"><h2>On this page</h2><ol id="toc"></ol></div>
<div class="aside-box"><h2>Related tools</h2><ul class="rel">{rel}</ul></div>
{guides_box(t["slug"])}
<div class="aside-cta"><h2>21 free tools</h2><p>Fees, payouts, pricing, invoices and tax — all in one place.</p><a class="btn btn-small" href="/#tools">Browse all tools</a></div>
</div></aside>
</div>
</div>'''
    schema = [
        {"@context": "https://schema.org", "@type": "WebApplication", "name": t["h1"], "url": url(path),
         "description": t["desc"], "applicationCategory": t.get("appcat", "FinanceApplication"), "operatingSystem": "Any",
         "browserRequirements": "Requires JavaScript", "isAccessibleForFree": True,
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
         "dateModified": TODAY, "publisher": {"@type": "Organization", "name": BRAND, "url": SITE}},
        breadcrumb_ld(bc), faq_ld(t["faq"]),
    ]
    scripts = []
    if t["js"] == "contract":
        scripts.append("/assets/js/tools/pdfkit.js")
    scripts.append(f'/assets/js/tools/{t["js"]}.js')
    return page(path, t["title"], t["desc"], body, schema, scripts=tuple(scripts), active=path)


def build_home():
    n = len(TOOLS)
    demo = '''<form class="demo" id="calc" autocomplete="off" aria-label="Quick Fiverr payout check" data-nourl="1">
<input type="hidden" name="tip" value="0"><input type="hidden" name="sfee" value="20">
<input type="hidden" name="bfee" value="5.5"><input type="hidden" name="small" value="2.5"><input type="hidden" name="thr" value="50">
<input type="hidden" name="wdc" value="0"><input type="hidden" name="conv" value="2">
<div id="role-seg" hidden><input type="hidden" name="role" value="seller"><button type="button" data-v="seller">s</button></div>
<div id="seller-only" hidden></div><div id="wd-custom" hidden></div>
<div class="field"><label for="d-price">Fiverr order price</label><div class="input-money"><span class="sym">$</span><input class="input" id="d-price" name="price" inputmode="decimal" value="100"></div></div>
<input type="hidden" name="wd" value="3">
<div class="field"><label for="d-cur">Also show in</label><select class="input" id="d-cur" name="cur"></select></div>
<div class="result" id="slip" aria-live="polite"></div>
<p class="rate-status" id="rate-status"></p>
</form>'''
    cats = ""
    for c in CATEGORIES:
        lis = "".join(tcard(t) for t in TOOLS if t["cat"] == c["id"])
        cats += (f'<section class="cat reveal" id="{c["id"]}" aria-labelledby="h-{c["id"]}"><div class="section-head"><div class="cat-title"><span class="ci">{c["icon"]}</span>'
                 f'<div><h2 id="h-{c["id"]}">{e(c["name"])}</h2><p>{e(c["desc"])}</p></div></div></div><ul class="tool-grid">{lis}</ul></section>')
    tick = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M8 12.3l2.7 2.6L16 9.5"/></svg>'
    body = f'''<div class="wrap">
<section class="hero hero-in">
<span class="badge"><b>{n} tools</b>Free for every freelancer, no sign-up</span>
<h1>Keep more of <span class="grad-text">every dollar you earn.</span></h1>
<p class="lede">Fee calculators, payout converters, pricing tools, invoices and tax estimates — built for freelancers on Fiverr, Upwork and beyond.</p>
<div class="search" role="search">{SEARCH}<label class="sr-only" for="tool-search">Search tools</label><input id="tool-search" type="search" placeholder="Search tools — try “Fiverr”, “invoice” or “tax”" autocomplete="off"><kbd>/</kbd></div>
<div><span class="platforms-label">Made for freelancers on</span><div class="platforms" style="margin-top:12px"><span>Fiverr</span><span>Upwork</span><span>Payoneer</span><span>Freelancer.com</span><span>PeoplePerHour</span><span>Wise</span></div></div>
</section>

<div class="stats reveal">
<div class="stat"><b class="grad-text">{n}</b><span>free tools, no limits</span></div>
<div class="stat"><b class="grad-text">24</b><span>currencies with live rates</span></div>
<div class="stat"><b class="grad-text">0</b><span>bytes of your data uploaded</span></div>
<div class="stat"><b class="grad-text">3</b><span>countries' tax rules</span></div>
</div>

<section class="showcase reveal" aria-labelledby="show-h">
<div>
<h2 id="show-h">See the real number before you accept the order.</h2>
<p class="lede">Platform fees, withdrawal charges and exchange-rate spreads quietly take a quarter of what clients pay. Type an order price and watch where every dollar goes.</p>
<ul class="ticks">
<li>{tick}Fiverr, Upwork, Freelancer.com and PeoplePerHour fees — checked {UPDATED_HUMAN}</li>
<li>{tick}Your earnings in PKR, INR, PHP and 20+ currencies at live rates</li>
<li>{tick}Shareable links that reopen with the exact same numbers</li>
</ul>
<a class="btn" href="/fiverr-fee-calculator/">Open the full Fiverr calculator {ARROW}</a>
</div>
{demo}
</section>

<section class="cats" id="tools" aria-labelledby="tools-h">
<h2 id="tools-h">Every tool a freelancer needs</h2>
<p class="lede">From the first quote to the tax return — {n} focused tools, each on its own fast page.</p>
{cats}
<p class="no-results" id="no-results" hidden>No tool matches that search. Try “fee”, “PDF” or “rate”.</p>
</section>

<section class="home-guides reveal" aria-labelledby="guides-h">
<div class="section-head"><div><h2 id="guides-h">Guides from the blog</h2><p>Step-by-step help on getting paid, pricing and tax.</p></div><a class="btn btn-ghost btn-small" href="/blog/">All guides {ARROW}</a></div>
<ul class="post-grid">{"".join(post_card(p) for p in POSTS[:3])}</ul>
</section>

<section class="features reveal" aria-label="Why freelancers use it">
<div class="feature"><span class="fi">{I["spark"]}</span><h3>Private by design</h3><p>Every calculation runs in your browser. Invoices, contracts and client names never leave your device.</p></div>
<div class="feature"><span class="fi">{I["receipt"]}</span><h3>Fees you can trust</h3><p>We track platform and payout fees and date every update, so you're never pricing with last year's numbers.</p></div>
<div class="feature"><span class="fi">{I["globe"]}</span><h3>Built for global freelancers</h3><p>Live exchange rates, local currencies and tax tools for Pakistan, the US and the UK.</p></div>
</section>

<section class="cta-band reveal">
<h2>Price your next gig in under a minute.</h2>
<p>Work backwards from the amount you want in your bank, and let the calculator add the fees for you.</p>
<div class="btns"><a class="btn" href="/fiverr-reverse-fee-calculator/">Find my price {ARROW}</a><a class="btn btn-ghost" href="/invoice-generator/">Create an invoice</a></div>
</section>
</div>'''
    schema = [
        {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": SITE + "/",
         "description": "Free fee calculators, invoice and contract generators, gig tools and tax estimators for freelancers."},
        {"@context": "https://schema.org", "@type": "Organization", "name": BRAND, "url": SITE + "/", "logo": SITE + "/assets/img/icon-512.png"},
        {"@context": "https://schema.org", "@type": "ItemList", "name": "Freelancer tools",
         "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": url(f'/{t["slug"]}/'), "name": t["h1"]} for i, t in enumerate(TOOLS)]},
    ]
    return page("/", f"Free Freelancer Tools — Fiverr & Upwork Fee Calculators, Invoice, Tax | {BRAND}",
                f"{n} free tools for freelancers: Fiverr and Upwork fee calculators, Payoneer to PKR, invoice, quote and contract generators, proposal and bio writers, and tax calculators.",
                body, schema, scripts=("/assets/js/tools/fiverr.js",))


def simple(path, title, desc, h1, inner, noindex=False):
    body = f'<div class="wrap page-simple">{crumbs([("Home", "/"), (h1, path)])}<header class="page-hero hero-in"><h1>{e(h1)}</h1></header><div class="panel prose reveal">{inner}</div></div>'
    return page(path, title, desc, body, [breadcrumb_ld([("Home", "/"), (h1, path)])], noindex=noindex)


def write(rel, content):
    p = os.path.join(OUT, rel.lstrip("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(content)


def main():
    from pages_content import ABOUT, CONTACT, PRIVACY, TERMS, NOTFOUND
    write("index.html", build_home())
    for t in TOOLS:
        write(f'{t["slug"]}/index.html', build_tool(t))
    write("blog/index.html", build_blog_index())
    for p in POSTS:
        write(f'blog/{p["slug"]}/index.html', build_post(p))
    write("about/index.html", simple("/about/", f"About {BRAND} — Free Tools for Freelancers", f"Who builds {BRAND} and why: honest, private calculators and generators for freelancers.", f"About {BRAND}", ABOUT))
    write("contact/index.html", simple("/contact/", f"Contact {BRAND}", "Report a wrong fee, suggest a tool or ask a question. We read every message.", "Contact", CONTACT.replace("{EMAIL}", EMAIL)))
    write("privacy-policy/index.html", simple("/privacy-policy/", f"Privacy Policy — {BRAND}", f"How {BRAND} handles data: tools run in your browser and nothing you type is uploaded.", "Privacy policy", PRIVACY.replace("{EMAIL}", EMAIL).replace("{DATE}", UPDATED_HUMAN)))
    write("terms/index.html", simple("/terms/", f"Terms of Use — {BRAND}", f"Terms for using {BRAND}'s free freelancer tools.", "Terms of use", TERMS.replace("{EMAIL}", EMAIL).replace("{DATE}", UPDATED_HUMAN)))
    write("404.html", page("/404.html", f"Page not found — {BRAND}", "This page doesn't exist.", f'<div class="wrap page-simple"><header class="page-hero hero-in" style="padding-top:60px"><h1>That page isn\'t here.</h1></header><div class="panel prose">{NOTFOUND}</div></div>', noindex=True))

    urls = [("/", "1.0")] + [(f'/{t["slug"]}/', "0.9") for t in TOOLS] + [("/blog/", "0.8")] + [(f'/blog/{p["slug"]}/', "0.7") for p in POSTS] + [("/about/", "0.4"), ("/contact/", "0.3"), ("/privacy-policy/", "0.2"), ("/terms/", "0.2")]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    post_dates = {f'/blog/{q["slug"]}/': q.get("updated", q["date"]) for q in POSTS}
    newest = max([TODAY] + list(post_dates.values()))
    for u, p in urls:
        lm = post_dates.get(u, newest if u in ("/", "/blog/") else TODAY)
        sm += f'  <url><loc>{url(u)}</loc><lastmod>{lm}</lastmod><priority>{p}</priority></url>\n'
    write("sitemap.xml", sm + "</urlset>\n")
    write("CNAME", SITE.split("//", 1)[1] + "\n")   # GitHub Pages custom domain
    write(".nojekyll", "")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    write("site.webmanifest", json.dumps({
        "name": f"{BRAND} — Freelancer Tools", "short_name": BRAND, "start_url": "/", "display": "standalone",
        "background_color": "#0a0918", "theme_color": "#0a0918",
        "icons": [{"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2))
    import shutil
    for q in SCHEDULED:  # never leave a page online for a post that is now scheduled for later
        d = os.path.join(OUT, "blog", q["slug"])
        if os.path.isdir(d):
            shutil.rmtree(d)
    print("Built", len(TOOLS), "tools and", len(POSTS), "posts into", os.path.abspath(OUT), "| date", PUBLISH_DATE)
    if SCHEDULED:
        print(f"{len(SCHEDULED)} scheduled; next: {SCHEDULED[0]['date']} {SCHEDULED[0]['slug']}")


if __name__ == "__main__":
    main()
