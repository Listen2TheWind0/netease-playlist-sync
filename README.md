# NetEase Playlist Sync Skill

English | [简体中文](README.zh-CN.md)

A Codex skill for building, configuring, and troubleshooting an automated
NetEase Cloud Music playlist export workflow.

The skill guides Codex through a local Node.js syncer and an optional GitHub
Actions schedule. It covers authenticated playlist discovery, JSON/CSV/TXT
exports, Cookie configuration, scheduled runs, failure diagnosis, and
credential-safe repository changes.

This is an instruction skill, not a standalone NetEase Cloud Music client. It
does not contain credentials, a browser profile, an API key, or a default
Cookie.

## Community

- [Contributing guide](.github/CONTRIBUTING_en.md)
- [中文贡献指南](.github/CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security policy](SECURITY.md)
- [Pull Request template](.github/PULL_REQUEST_TEMPLATE.md)

## Features

- Export owned playlists, including the liked-music playlist.
- Preserve playlist order, duplicate entries, and unavailable song IDs.
- Generate stable ID-based JSON, CSV, and TXT snapshots.
- Run locally with a `.env` file or remotely with GitHub Actions Secrets.
- Support manual and scheduled GitHub Actions runs.
- Avoid exposing or committing Cookies and other credentials.
- Diagnose current NetEase web API behavior, including the authenticated
  account endpoint `/api/nuser/account/get`.

## Install

Copy the skill directory into the Codex skills directory:

```text
$CODEX_HOME/skills/netease-playlist-sync
```

If `CODEX_HOME` is not set, use the default user skills directory:

```text
~/.codex/skills/netease-playlist-sync
```

On Windows, the default path is usually:

```text
%USERPROFILE%\.codex\skills\netease-playlist-sync
```

The directory must contain:

```text
netease-playlist-sync/
  SKILL.md
  README.md
  README.zh-CN.md
  LICENSE
  CODE_OF_CONDUCT.md
  SECURITY.md
  scripts/
    validate_skill.py
  .github/
    CONTRIBUTING.md
    CONTRIBUTING_en.md
    PULL_REQUEST_TEMPLATE.md
  agents/
    openai.yaml
```

## Use

Invoke explicitly with:

```text
$netease-playlist-sync
```

It can also be selected automatically for requests involving:

- 网易云音乐歌单导出或定时同步
- `NETEASE_COOKIE` or `MUSIC_U`
- GitHub Actions playlist-sync failures
- the JSON/CSV/TXT playlist snapshot workflow

## Credential Safety

The skill never asks users to paste credentials into chat.

Users should provide credentials only through their local `.env` file or a
GitHub Actions Secret named `NETEASE_COOKIE`. A Cookie should be treated like a
password:

- Do not commit `.env`.
- Do not print Cookie values in logs or issue reports.
- Do not include a literal `Cookie:` prefix in the environment value.
- Prefer the complete semicolon-separated Cookie header value.
- Rotate the Cookie if it is exposed.

The skill permits only redacted diagnostics such as whether a variable exists,
its length, the number of Cookie pairs, and the Cookie names. It must never
reveal values after `=`.

## Expected Target Repository

The skill is designed for a target repository containing a Node.js syncer with
commands similar to:

```powershell
npm test
npm run sync -- --dry-run
npm run sync
```

Generated snapshots normally live under:

```text
data/
  index.json
  playlists/{playlistId}.json
  csv/{playlistId}.csv
  txt/{playlistId}.txt
```

The target repository should remain private when it contains personal playlist
data. This skill itself contains no personal data and may be published
separately.

## GitHub Actions

The recommended workflow supports:

- `workflow_dispatch` for immediate manual verification.
- A daily UTC `schedule` for unattended synchronization.
- `NETEASE_COOKIE` as a repository Secret.
- Optional `NETEASE_UID` as a repository variable.
- `contents: write` only when the workflow must commit generated snapshots.

GitHub scheduled workflows may be delayed. A green run means the workflow
completed; it does not necessarily mean a new commit was created. No commit is
expected when the playlist data is unchanged.

## Development and Validation

Run the Codex skill validator from the skill-creator system skill:

```powershell
$env:PYTHONUTF8 = "1"
python path/to/skill-creator/scripts/quick_validate.py path/to/netease-playlist-sync
```

For this skill, validation should also include:

1. A scan for real Cookies, API keys, tokens, local user paths, and personal
   repository names.
2. A review of README links and install paths for portability.
3. A check that no `.env`, browser profile, generated playlist data, or runtime
   dependency is bundled accidentally.

The repository includes a dependency-free validator:

```powershell
python scripts/validate_skill.py
```

## Limitations

- NetEase web endpoints are not guaranteed to be stable public APIs.
- A Cookie can expire or be invalidated and must then be refreshed by the user.
- GitHub Actions schedule timing is approximate.
- The skill does not download audio, lyrics, covers, or other copyrighted media.
- NetEase Cloud Music and Codex are trademarks of their respective owners. This
  project is not affiliated with either company.

## License

MIT License. See [LICENSE](LICENSE).
