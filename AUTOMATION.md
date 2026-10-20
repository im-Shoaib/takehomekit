# Publishing a blog post on takehomekit.online — playbook

This repo has two branches:
- **main** — the live static website (GitHub Pages, custom domain takehomekit.online). Never edit by hand.
- **source** — the generator: `build.py`, content files, fonts, icons, `cover.py`, this playbook and `TOPICS.md`.

The site is always rebuilt from **source** and the output copied to **main**.

## How publishing works now (since 2026-10-20)
- Posts are written **ahead of time** with a future `date` in `blog_content.py`.
- `build.py` only publishes posts whose `date` is on or before today in Pakistan time (UTC+5);
  future posts are skipped (and their folders removed if present). `BUILD_DATE=YYYY-MM-DD` overrides "today" for testing.
- `.github/workflows/scheduled-publish.yml` on **main** runs every day at 03:07 UTC (08:07 PKT),
  checks out main + source, runs `build.py` into main and commits only if something changed.
  It can also be run by hand: GitHub → Actions → "Scheduled publish" → Run workflow.
- Cover images for scheduled posts are committed to main in advance (they are unlinked until the post goes live).
- The Claude scheduled task ("TakehomeKit blog post") is **disabled**. If it is ever re-enabled, it must add
  new posts dated **after the last scheduled date** in `TOPICS.md`, not today.
- Internal `/blog/` links may only point to posts dated **earlier** than the linking post, or the link would 404 until the target publishes.

## Adding a batch of scheduled posts
1. Follow steps 0–4 below, but give each post a future `date` (one every 3 days after the last scheduled one).
2. Generate covers for all of them into `/home/claude/site`.
3. Test: `BUILD_DATE=<last date> SITE_OUT=<copy of site> python3 build.py` and check every new page; then build for today into `/home/claude/site`.
4. Update `TOPICS.md` ("Scheduled" section), push **source** first, then **main** (covers + any changed pages).

## 0. Setup (fresh session)
1. Attach the repo with push access: owner `im-Shoaib`, repo `takehomekit` (use the add_repo tool, access "push").
2. Clone both branches side by side:
   ```
   git clone --depth 1 -b source https://github.com/im-Shoaib/takehomekit /home/claude/src
   git clone --depth 1 -b main   https://github.com/im-Shoaib/takehomekit /home/claude/site
   ```
3. `pip install --break-system-packages pillow playwright` only if missing. Chromium is preinstalled (PLAYWRIGHT_BROWSERS_PATH). Never run `playwright install`.

## 1. Pick the topic
Open `TOPICS.md`, take the **first unchecked** backlog item. Check `blog_content.py` so you don't repeat an existing post.

## 2. Research
Anything that can change — fees, tax rates, limits, deadlines, procedures — must be checked with web search **today** against official or reputable sources (Fiverr/Upwork/Payoneer help centres, FBR, PSEB, IRS, HMRC, established news).
- Never invent statistics, quotes, studies, prices or people.
- If sources disagree, say so in the article ("at the time of writing… confirm on …") rather than picking one silently.
- Facts the site owner has confirmed: in Pakistan Fiverr pays out through Payoneer; Fiverr charges a flat **$3 per withdrawal** (per withdrawal, not per order). Keep all posts consistent with this and with the calculators.

## 3. Write the post
Add one dict to `POSTS` in `blog_content.py` (copy the shape of an existing post):
- `slug` — lowercase-hyphenated, keyword-led, unique.
- `title` — SEO title, ideally ≤ 65 characters. `h1` — on-page heading, sentence case.
- `desc` — 140–160 characters, includes the main keyword.
- `lede` — one or two sentences.
- `date` — the publish date in Asia/Karachi, `YYYY-MM-DD` (today, or a future date to schedule it).
- `cat` — short category (Payments, Tax, Pricing, Winning work, Fiverr, Upwork, Documents, Money).
- `icon` — a key from `I` in `tools_content.py` (receipt, brief, target, bank, fx, clock, list, pie, doc, text, image, scale, pen, user, flag, swap, people, split, send, calc, tag, spark, quote, globe, pound, moon).
- `tools` — 2–4 tool slugs (folders in the site root, e.g. `fiverr-fee-calculator`).
- `image` — `/assets/img/blog/<slug>`; `alt` — a plain description of the cover.
- `body` — HTML: start with `takeaways([...])`, then `<h2>` sections; use `<ul>/<ol>`, `<p class="formula">`, tables in `<div class="table-wrap">`, and 2–3 `cta(slug, title, text, button)` blocks to relevant tools. Link to 1–2 **earlier-dated** posts with `/blog/<slug>/`.
- `faq` — 3–5 `(question, answer)` pairs.

Style: English, plain and practical, second person, short paragraphs, no hype, no emojis, 900–1,500 words. Tax/legal posts end with a one-line "general information, not advice" note.

## 4. Cover image
Royalty-free by construction (Lucide icons, ISC licence; no stock photos — stock sites are unreachable from the sandbox):
```
cd /home/claude/src && SITE_OUT=/home/claude/site python3 cover.py <slug> <main-icon> <side-icon-1> <side-icon-2> <variant>
```
Pick icons from `icons/` that represent the topic (e.g. wallet, landmark, coins, calendar, scale, file-text, send, target, trending-up, shield-check, globe, clock, handshake). Variant = (index of the post in POSTS order) % 3. Look at the output image before continuing.

## 5. Build and check
```
cd /home/claude/src && SITE_OUT=/home/claude/site python3 build.py
```
Then verify:
- the build prints the new post count and no traceback;
- `/home/claude/site/blog/<slug>/index.html` exists and its three images exist in `assets/img/blog/`;
- every `application/ld+json` block in the new page parses as JSON;
- `git -C /home/claude/site status` only shows expected changes (new post folder + images, blog index, home, sitemap, tool pages that link the post). If unrelated pages changed, stop and investigate.
Optionally serve `/home/claude/site` with `python3 -m http.server` and open the new page with Playwright to confirm no JS errors.

## 6. Update the backlog
Tick the topic in `TOPICS.md` and append ` — <date> — <slug>`; put it under "Published" (or "Scheduled" if future-dated). If fewer than 5 unchecked topics remain, add new ones.

## 7. Commit and push (both branches)
```
cd /home/claude/src  && git add -A && git commit -m "Post: <title>" && git push origin source
cd /home/claude/site && git add -A && git commit -m "Publish: <title>" && git push origin main
```
Use the commit attribution lines your environment specifies. Push **source first**. If either push fails, do not retry in a loop — report it.

## Never
- Never delete or rewrite existing posts, tools or pages (fixing a factual error is fine — note it in the commit message).
- Never change fees/defaults in tools without verified sources.
- Never push a broken build.
