"""Generates favicon, app icons and the social share image (needs Pillow).
Poppins .woff files are read from build-tools/fonts if present, else a system font is used."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "takehome")
IMG = os.path.join(OUT, "assets", "img")
os.makedirs(IMG, exist_ok=True)
BG = (10, 9, 24); INK = (26, 16, 51); TEXT = (246, 244, 255); TEXT2 = (196, 191, 228)
G1, G2, G3 = (243, 207, 145), (244, 163, 180), (160, 139, 255)

SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f3cf91"/><stop offset=".5" stop-color="#f4a3b4"/><stop offset="1" stop-color="#a08bff"/></linearGradient></defs><rect width="40" height="40" rx="12" fill="url(#g)"/><path d="M14 11v18" stroke="#1a1033" stroke-width="3.6" stroke-linecap="round"/><path d="M27 11l-8.5 9L27 29" fill="none" stroke="#1a1033" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="30" cy="20" r="2.2" fill="#1a1033"/></svg>'''
open(os.path.join(IMG, "favicon.svg"), "w").write(SVG)


def lerp(a, b, t): return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def grad(w, h):
    g = Image.new("RGB", (w, h))
    px = g.load()
    for y in range(h):
        for x in range(w):
            t = (x / w + y / h) / 2
            px[x, y] = lerp(G1, G2, t / .5) if t < .5 else lerp(G2, G3, (t - .5) / .5)
    return g


def icon(size):
    S = 4; W = size * S; u = W / 40
    base = grad(W, W)
    mask = Image.new("L", (W, W), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, W - 1, W - 1], radius=12 * u, fill=255)
    im = Image.new("RGBA", (W, W), (0, 0, 0, 0)); im.paste(base, (0, 0), mask)
    d = ImageDraw.Draw(im); lw = int(3.6 * u)
    d.line([(14 * u, 11 * u), (14 * u, 29 * u)], fill=INK, width=lw)
    d.line([(27 * u, 11 * u), (18.5 * u, 20 * u), (27 * u, 29 * u)], fill=INK, width=lw, joint="curve")
    for (cx, cy) in [(14, 11), (14, 29), (27, 11), (27, 29)]:
        r = lw / 2; d.ellipse([cx * u - r, cy * u - r, cx * u + r, cy * u + r], fill=INK)
    r = 2.2 * u; d.ellipse([30 * u - r, 20 * u - r, 30 * u + r, 20 * u + r], fill=INK)
    return im.resize((size, size), Image.LANCZOS)


for s, name in [(180, "icon-180.png"), (192, "icon-192.png"), (512, "icon-512.png")]:
    bg = Image.new("RGBA", (s, s), BG + (255,)) if name == "icon-180.png" else None
    ic = icon(s)
    if bg: bg.alpha_composite(ic); ic = bg
    ic.save(os.path.join(IMG, name), optimize=True)
icon(64).save(os.path.join(OUT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])


def font(w, size):
    for p in [os.path.join(HERE, "fonts", f"poppins-latin-{w}-normal.woff"), "/usr/share/fonts/opentype/inter/Inter-Bold.otf"]:
        try: return ImageFont.truetype(p, size)
        except Exception: pass
    return ImageFont.load_default()


W, H = 1200, 630
im = Image.new("RGB", (W, H), BG)
glow = Image.new("RGB", (W, H), BG)
gd = ImageDraw.Draw(glow)
gd.ellipse([-200, -260, 620, 420], fill=(60, 45, 150))
gd.ellipse([760, -220, 1400, 300], fill=(110, 85, 60))
glow = glow.filter(ImageFilter.GaussianBlur(140))
im = Image.blend(im, glow, .9)
d = ImageDraw.Draw(im)
logo = icon(72); im.paste(logo, (72, 64), logo)
d.text((160, 76), "takehome", font=font(700, 40), fill=TEXT)
tw = d.textlength("takehome", font=font(700, 40))
d.text((160 + tw, 76), "kit", font=font(800, 40), fill=G1)
d.text((72, 190), "Keep more of", font=font(800, 76), fill=TEXT)
# gradient line
f2 = font(800, 76)
txt = "every dollar you earn."
tw2 = int(d.textlength(txt, font=f2)) + 10
gl = grad(tw2, 110); m = Image.new("L", (tw2, 110), 0)
ImageDraw.Draw(m).text((0, 0), txt, font=f2, fill=255)
im.paste(gl, (72, 282), m)
d.text((72, 420), "21 free tools for freelancers — Fiverr & Upwork fees,", font=font(500, 28), fill=TEXT2)
d.text((72, 460), "Payoneer to PKR, invoices, contracts and tax calculators.", font=font(500, 28), fill=TEXT2)
d.rounded_rectangle([72, 528, 72 + 300, 528 + 56], radius=28, fill=G1)
d.text((96, 541), "takehomekit.online", font=font(600, 24), fill=INK)
im.save(os.path.join(IMG, "og.png"), optimize=True)
print("images done")
