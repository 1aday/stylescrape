# Contributing

Thanks for improving StyleScrape. Keep changes focused, easy to review, and respectful of the site being accessed.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install firecrawl-py
```

Use a local Firecrawl API key only. Never commit credentials, generated thread archives, virtual environments, or operating-system metadata.

## Before opening a pull request

- Explain the problem and why the proposed change is useful.
- Test against a very small page range before attempting a full archive.
- Preserve or strengthen the delay between requests.
- Keep generated Markdown out of the repository.
- Update the README when setup or behavior changes.
- Confirm the source site's terms and rate limits still permit the intended use.

## Pull-request scope

Prefer one clear change per pull request. Good contributions include safer configuration, current Firecrawl SDK compatibility, resumable runs, clearer errors, and tests that do not make live network requests.
