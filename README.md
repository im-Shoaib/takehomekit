# TakehomeKit — site source

This branch holds the generator for https://takehomekit.online. The live site is the `main` branch (built output only).

- `build.py` — builds the whole site (`SITE_OUT=/path/to/main-checkout python3 build.py`)
- `tools_content.py`, `tools_more.py` — the 21 tools (UI, articles, FAQs)
- `blog_content.py` — blog posts
- `pages_content.py` — About, Contact, Privacy, Terms, 404
- `cover.py` — blog cover image generator (Lucide icons, ISC)
- `make_images.py` — favicon, app icons, social image
- `AUTOMATION.md` — step-by-step playbook for publishing a post
- `TOPICS.md` — topic backlog
