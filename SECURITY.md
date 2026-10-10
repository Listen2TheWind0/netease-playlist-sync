# Security Policy

## Scope

This policy covers the Skill instructions, repository automation, validation
script, and documentation in this repository.

The Skill handles guidance around credentials such as NetEase Cookies and
GitHub Actions Secrets. It must never contain a real Cookie, API key, access
token, browser profile, personal playlist export, or other private data.

## Reporting a Vulnerability

Please do not open a public Issue for a suspected security vulnerability.

Use GitHub's private vulnerability reporting or Security Advisory feature when
available. If those features are unavailable, contact the repository
maintainers privately through GitHub and provide only the minimum redacted
details needed to reproduce the problem.

Never include live credentials in a report. Use placeholders such as
`<redacted-cookie>` and revoke or rotate any credential that may have been
exposed.

## Before Reporting

- Confirm the issue is reproducible with placeholder credentials.
- Remove Cookies, API keys, tokens, account identifiers, personal playlist
  data, local paths, and browser profile files from logs and screenshots.
- Include the affected file, a minimal reproduction, impact, and a suggested
  mitigation when possible.

## Response

Maintainers will acknowledge valid reports, assess impact, and publish a
sanitized fix or advisory when appropriate. Do not disclose an unresolved
issue publicly before maintainers have had a reasonable opportunity to respond.
