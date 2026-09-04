# StyleScrape

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-prototype-F59E0B)
![Pull requests welcome](https://img.shields.io/badge/PRs-welcome-2EA44F)

StyleScrape is a small Python utility that exports the public S.E.H. Kelly discussion on Styleforum to one Markdown file per page using Firecrawl.

## What it does

- Iterates through pages 1–414 of the configured thread.
- Requests Markdown containing the page's main content.
- Writes numbered files such as `page_001.md` to `seh_kelly_thread/`.
- Waits two seconds between requests and continues after individual page errors.

## Requirements

- Python 3.10 or newer
- A Firecrawl API key
- Permission to access and archive the source material

Install the dependency in an isolated environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install firecrawl-py
```

## Run locally

1. Open `scrape.py`.
2. Replace the `API KEY HERE` placeholder locally with your Firecrawl API key.
3. Run:

```bash
python scrape.py
```

Generated Markdown is written to `seh_kelly_thread/`.

Never commit a real API key. This repository is a focused prototype and uses the Firecrawl SDK conventions that existed when it was written; newer SDK releases may require small API adjustments.

## Responsible use

Before scraping, review the source site's terms, robots policy, copyright rules, and rate limits. Reduce the page range while testing, preserve the built-in delay, and avoid creating unnecessary load.
