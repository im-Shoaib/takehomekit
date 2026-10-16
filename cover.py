#!/usr/bin/env python3
"""Render a blog cover image in the TakehomeKit style (no text, open-source Lucide icons, ISC licence).

Usage:
  python3 cover.py SLUG MAIN_ICON SIDE_ICON_1 SIDE_ICON_2 [VARIANT 0-2]
Example:
  python3 cover.py payoneer-annual-fee wallet coins calendar 1

Writes into ../takehome/assets/img/blog/ (or $SITE_OUT/assets/img/blog/):
  SLUG.webp (1600x900), SLUG-card.webp (800x450), SLUG-og.jpg (1200x630)
Icon names are file names in ./icons without .svg (browse https://lucide.dev/icons).
"""
import os, re, sys, asyncio, io
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.environ.get("SITE_OUT", os.path.join(HERE, "..", "takehome"))
OUT = os.path.join(SITE, "assets", "img", "blog")

VARIANTS = [
    # (glow A, glow B, accent gradient stops)
    ("rgba(124,102,255,.55)", "rgba(243,207,145,.35)", ("#f3cf91", "#f4a3b4", "#a08bff")),
    ("rgba(244,163,180,.45)", "rgba(124,102,255,.50)", ("#ffd9a8", "#f4a3b4", "#8f7bff")),
    ("rgba(94,230,171,.30)", "rgba(160,139,255,.50)", ("#b6f5d8", "#f3cf91", "#a08bff")),
]


def icon_inner(name):
    path = os.path.join(HERE, "icons", name + ".svg")
    if not os.path.exists(path):
        sys.exit(f"Icon not found: {name} (look in {os.path.join(HERE, 'icons')})")
    svg = open(path, encoding="utf-8").read()
    m = re.search(r"<svg[^>]*>(.*)</svg>", svg, re.S)
    return m.group(1)


def html(main, s1, s2, v):
    ga, gb, (c1, c2, c3) = VARIANTS[v % 3]
    def ic(name, size, grad, sw):
        return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="url(#{grad})" stroke-width="{sw}" '
                f'stroke-linecap="round" stroke-linejoin="round">{icon_inner(name)}</svg>')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1600px;height:900px;overflow:hidden;background:#0a0918;position:relative}}
.a{{position:absolute;border-radius:50%;filter:blur(90px)}}
.a1{{width:900px;height:700px;left:-120px;top:-260px;background:{ga}}}
.a2{{width:900px;height:700px;right:-200px;bottom:-320px;background:{gb}}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:64px 64px;
-webkit-mask-image:radial-gradient(60% 60% at 50% 50%,#000,transparent)}}
.floor{{position:absolute;left:50%;top:700px;width:900px;height:120px;transform:translateX(-50%);border-radius:50%;background:radial-gradient(closest-side,{gb},transparent);filter:blur(20px);opacity:.9}}
.tile{{position:absolute;display:grid;place-items:center;border-radius:64px;
background:linear-gradient(150deg,rgba(255,255,255,.16),rgba(255,255,255,.03));border:2px solid rgba(255,255,255,.22);
box-shadow:0 60px 120px -30px rgba(0,0,0,.8),inset 0 2px 0 rgba(255,255,255,.25);backdrop-filter:blur(18px)}}
.main{{width:400px;height:400px;left:600px;top:220px;border-radius:96px;transform:rotate(-6deg)}}
.main svg{{filter:drop-shadow(0 0 28px {c2}) drop-shadow(0 0 60px {c3})}}
.s1{{width:220px;height:220px;left:300px;top:390px;transform:rotate(-14deg);opacity:.92}}
.s2{{width:220px;height:220px;left:1090px;top:200px;transform:rotate(12deg);opacity:.92}}
.s1 svg,.s2 svg{{filter:drop-shadow(0 0 18px {c1})}}
.spark{{position:absolute;width:26px;height:26px;background:{c1};clip-path:polygon(50% 0,62% 38%,100% 50%,62% 62%,50% 100%,38% 62%,0 50%,38% 38%);filter:drop-shadow(0 0 10px {c1})}}
</style></head><body>
<svg width="0" height="0" style="position:absolute"><defs>
<linearGradient id="g" gradientUnits="userSpaceOnUse" x1="2" y1="2" x2="22" y2="22"><stop offset="0" stop-color="{c1}"/><stop offset=".5" stop-color="{c2}"/><stop offset="1" stop-color="{c3}"/></linearGradient>
<linearGradient id="g2" gradientUnits="userSpaceOnUse" x1="2" y1="2" x2="22" y2="22"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="{c1}"/></linearGradient>
</defs></svg>
<div class="a a1"></div><div class="a a2"></div><div class="grid"></div><div class="floor"></div>
<div class="tile s1">{ic(s1, 110, "g2", 1.6)}</div>
<div class="tile s2">{ic(s2, 110, "g2", 1.6)}</div>
<div class="tile main">{ic(main, 220, "g", 1.5)}</div>
<div class="spark" style="left:560px;top:190px"></div>
<div class="spark" style="left:1050px;top:560px;width:18px;height:18px"></div>
<div class="spark" style="left:470px;top:300px;width:14px;height:14px;opacity:.7"></div>
<div class="spark" style="left:1240px;top:470px;width:16px;height:16px;opacity:.8"></div>
</body></html>"""


async def render(markup):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1600, "height": 900})
        await pg.set_content(markup)
        await pg.wait_for_timeout(300)
        png = await pg.screenshot(type="png")
        await b.close()
        return png


def main():
    if len(sys.argv) < 5:
        sys.exit(__doc__)
    slug, mi, s1, s2 = sys.argv[1:5]
    v = int(sys.argv[5]) if len(sys.argv) > 5 else 0
    os.makedirs(OUT, exist_ok=True)
    im = Image.open(io.BytesIO(asyncio.run(render(html(mi, s1, s2, v))))).convert("RGB")
    im.save(os.path.join(OUT, slug + ".webp"), "WEBP", quality=80, method=6)
    im.resize((800, 450), Image.LANCZOS).save(os.path.join(OUT, slug + "-card.webp"), "WEBP", quality=78, method=6)
    og = im.crop((0, 30, 1600, 870)).resize((1200, 630), Image.LANCZOS)
    og.save(os.path.join(OUT, slug + "-og.jpg"), "JPEG", quality=84, optimize=True, progressive=True)
    print("cover written:", os.path.join(OUT, slug + ".webp"))


if __name__ == "__main__":
    main()
