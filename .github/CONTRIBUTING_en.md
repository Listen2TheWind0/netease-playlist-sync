# Contribution Guide

English | [简体中文](CONTRIBUTING.md)

Contributions through Issues and Pull Requests are welcome. Before submitting
a change, read this guide and the [Pull Request template](PULL_REQUEST_TEMPLATE.md).

## About Issues

For substantial changes, open an Issue first and wait for maintainer feedback.
This is recommended for:

- New Skill capabilities, directory changes, or automation workflows;
- Changes to credential handling, GitHub Actions permissions, or external APIs;
- Uncertain bugs or behavior whose intended semantics are unclear;
- Changes that may affect compatibility with other Agent environments.

Use the Issue templates when reporting problems. Never paste Cookies, API keys,
access tokens, browser profiles, personal playlist data, or other private
information into an Issue, screenshot, or log.

## Submitting Changes

1. Fork the repository and create a dedicated branch from `main`, such as
   `docs/update-cn-readme`;
2. Keep one Pull Request focused on one change;
3. Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
   with prefixes such as `feat:`, `fix:`, `docs:`, and `chore:`;
4. Explain what changed, why it changed, and how it was verified;
5. Explain any skipped check and provide an alternative verification;
6. For Skill changes, a redacted conversation sample is welcome. Do not include
   live credentials or personal data.

## Repository Structure

- `SKILL.md`: Skill entrypoint and core behavior constraints;
- `README.md`, `README.zh-CN.md`: bilingual usage and release documentation;
- `agents/openai.yaml`: Codex UI metadata;
- `.github/`: contribution guide, Issue/PR templates, and CI;
- `scripts/validate_skill.py`: dependency-free local validation;
- `LICENSE`, `CODE_OF_CONDUCT.md`, `SECURITY.md`: project governance documents.

This repository publishes the Skill only. Do not submit a personal syncer's
source code, playlist snapshots, `.env`, browser profile, or runtime logs.

## Welcomed Contributions

- Fixes to genuine comprehension issues in `SKILL.md`, README files, or links;
- Improvements to loading the Skill in other Agent environments;
- Verified troubleshooting guidance and reproducible failure reports;
- English/Chinese documentation and translation improvements;
- Credential-safety, sensitive-data scanning, and validation improvements;
- Real-world feedback, including failures and reproduction conditions.

## Contributions We Will Not Merge

- Real Cookies, API keys, access tokens, email addresses, phone numbers, account
  details, or personal playlists;
- Credentials written into examples, tests, screenshots, logs, Issues, PRs, or
  Git history;
- Bulk harassment of third-party services, unrelated automated PRs, or attempts
  to bypass service limits;
- Personal project files, build artifacts, or dependency directories unrelated
  to this Skill;
- Changes made only to manufacture a diff or inflate contribution history.

## No-op Commits

Unless a change fixes a clear problem, improves rendering, or satisfies a format
requirement, do not submit changes that only:

- Replace correct punctuation with equally correct punctuation;
- Add or remove spaces, blank lines, line breaks, or indentation;
- Mechanically rearrange layout without changing content or rendering;
- Mass-replace unrelated text.

If a formatting issue has a real impact, describe its location, impact, and
verification in the Pull Request.

## Pre-submission Checks

Run:

```powershell
$env:PYTHONUTF8 = "1"
python scripts/validate_skill.py
python path/to/skill-creator/scripts/quick_validate.py .
```

Also confirm:

- `.env`, Cookies, API keys, tokens, and personal data are not staged;
- README relative links work;
- No `data/`, browser profile, `node_modules/`, or private local path was added;
- Local validation and CI checks pass.
