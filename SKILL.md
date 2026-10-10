---
name: netease-playlist-sync
description: Build, maintain, and troubleshoot a private Git/GitHub Actions workflow that exports authenticated NetEase Cloud Music playlists to JSON, CSV, and TXT snapshots. Use when the user asks about 网易云歌单导出、定时同步、NETEASE_COOKIE, MUSIC_U, GitHub Actions sync failures, or this repository's playlist-sync setup.
metadata:
  short-description: Automate NetEase playlist export and sync
---

# NetEase Playlist Sync

Use this skill for automating NetEase Cloud Music playlist exports with a local Node.js CLI and GitHub Actions. The expected shape is a private repository that reads `NETEASE_COOKIE`, exports owned playlists, writes `data/`, and commits only real playlist changes.

## Secret Safety

- Treat `NETEASE_COOKIE`, `MUSIC_U`, browser Cookie headers, GitHub Secrets, Personal Access Tokens, API keys, and `.env` contents as credentials.
- Never print, quote, summarize, commit, or paste credential values into chat, logs, files, tests, documentation, or Git history.
- Do not ask the user to send a Cookie or token in chat. Tell them where to paste it locally or in GitHub Secrets.
- When inspecting local credentials, report only safe metadata such as whether a key exists, total length, cookie-pair count, cookie names, or whether the value accidentally starts with `Cookie:`.
- Before committing or pushing, verify `.env` is ignored and not staged. If `.env` appears in `git status`, stop and fix `.gitignore` or unstage it before continuing.

## Current Workflow

For this project, the syncer should:

- Use Node.js ESM with no required runtime dependencies unless the repo already chose otherwise.
- Read local configuration from `.env` and remote configuration from GitHub Actions Secret `NETEASE_COOKIE`; optional `NETEASE_UID` may be a GitHub Actions variable.
- Resolve the logged-in account through `/api/nuser/account/get`. The older `/api/user/account` may return API code `404`.
- Fetch playlists through `/api/user/playlist`, playlist track IDs through `/api/v6/playlist/detail`, and song metadata through `/api/song/detail`.
- Export stable ID-based files under:
  - `data/index.json`
  - `data/playlists/{playlistId}.json`
  - `data/csv/{playlistId}.csv`
  - `data/txt/{playlistId}.txt`
- Preserve playlist order, duplicate song entries, deleted/unavailable song IDs, and empty playlists.
- Avoid generating empty Git commits; if generated `data/` has no changes, the workflow should succeed without committing.

## Cookie Guidance

When the user asks how to fill Cookie values:

- Tell them to log in to `https://music.163.com/`, open browser DevTools Network, select a `music.163.com` request, and copy the value of the `Cookie` request header.
- The value should be a single line of semicolon-separated `name=value` pairs. It must not include the literal `Cookie:` header name.
- The most important login cookie is usually `MUSIC_U`; a value starting at `MUSIC_U=` may work for current endpoints, but copying the complete request-header value is more robust.
- If the user sees extra cookie names such as device, analytics, or session identifiers, do not tell them to delete those names unless they are clearly outside the Cookie header.

## Local Validation

Use these checks without revealing secrets:

```powershell
npm test
npm run sync -- --dry-run
```

If a credential sanity check is needed, inspect only metadata. For example, in PowerShell it is acceptable to report `NETEASE_COOKIE` presence, value length, pair count, cookie names, and whether the value begins with `Cookie:`; do not print values after `=`.

Successful dry-run output should show prepared playlists and a final count, for example `Validated N playlists and M tracks`. If the user has not configured a Cookie, a clean failure saying `NETEASE_COOKIE is required` is expected.

## GitHub Actions

The workflow should support both:

- `workflow_dispatch` for manual runs.
- `schedule` for automatic UTC cron runs. For China time, `17 19 * * *` is approximately daily 03:17 Asia/Shanghai.

Tell the user that a green check and `Status: Success` means the workflow completed. A successful run may not create a commit when no playlist data changed. A screenshot showing `on: workflow_dispatch` means that specific run was manual; scheduled runs should show `on: schedule`.

GitHub Actions warnings about a deprecated Node runtime are not the same as sync failure. Treat them as non-blocking unless the job actually fails or the user asks to remove the warning.

## Troubleshooting

- `Unable to resolve the authenticated NetEase account (API code 404)`: check that the client uses `/api/nuser/account/get`, not `/api/user/account`.
- `NETEASE_COOKIE is required`: `.env` or GitHub Secret is missing or not readable.
- API code `301` or `20001`: login session is invalid or expired; instruct the user to refresh the Cookie locally and in GitHub Secrets.
- Private/liked playlists missing: verify the Cookie belongs to the intended account and that the sync uses the authenticated account ID unless `NETEASE_UID` is intentionally set.
- Scheduled workflow did not run at the exact minute: GitHub schedules are UTC and may be delayed; use manual `Run workflow` for immediate validation.

## Before Pushing

- Run tests.
- Run a dry-run if a Cookie is available; otherwise document that live sync was not run because credentials are absent.
- Confirm no credentials are staged.
- Inspect generated `data/` counts if a real sync was run.
- Push only code, workflow, documentation, tests, and generated playlist snapshots that the user expects to store in the private repository.
