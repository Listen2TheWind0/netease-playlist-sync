# 网易云歌单同步 Skill

[English](README.md) | 简体中文

这是一个 Codex Skill，用于搭建、配置和排查网易云音乐歌单自动导出流程。

该 Skill 会指导 Codex 创建或维护一个本地 Node.js 同步器，并可配合 GitHub
Actions 定时运行。它覆盖已登录账号的歌单发现、JSON/CSV/TXT 导出、Cookie
配置、定时任务、失败诊断，以及避免泄露凭据的仓库修改流程。

这是一个说明型 Skill，不是独立的网易云音乐客户端。它不包含任何凭据、浏览器
配置文件、API key 或默认 Cookie。

## 社区文档

- [中文贡献指南](.github/CONTRIBUTING.md)
- [English Contribution Guide](.github/CONTRIBUTING_en.md)
- [行为准则](CODE_OF_CONDUCT.md)
- [安全策略](SECURITY.md)
- [Pull Request 模板](.github/PULL_REQUEST_TEMPLATE.md)

## 功能

- 导出账号自建歌单，包括“喜欢的音乐”歌单。
- 保留歌单顺序、重复歌曲条目和不可用歌曲 ID。
- 生成稳定的、以 ID 命名的 JSON、CSV 和 TXT 快照。
- 支持通过本地 `.env` 文件运行，也支持通过 GitHub Actions Secrets 远程运行。
- 支持 GitHub Actions 手动触发和定时触发。
- 避免暴露或提交 Cookie 等凭据。
- 诊断当前网易云网页接口行为，包括已登录账号接口 `/api/nuser/account/get`。

## 安装

将 Skill 目录复制到 Codex skills 目录：

```text
$CODEX_HOME/skills/netease-playlist-sync
```

如果没有设置 `CODEX_HOME`，使用默认用户 skills 目录：

```text
~/.codex/skills/netease-playlist-sync
```

在 Windows 上，默认路径通常是：

```text
%USERPROFILE%\.codex\skills\netease-playlist-sync
```

目录应包含：

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

## 使用

可以显式调用：

```text
$netease-playlist-sync
```

当请求涉及以下内容时，也可以由 Codex 自动选择：

- 网易云音乐歌单导出或定时同步
- `NETEASE_COOKIE` 或 `MUSIC_U`
- GitHub Actions 歌单同步失败
- JSON/CSV/TXT 歌单快照工作流

## 凭据安全

该 Skill 不会要求用户把凭据粘贴到聊天中。

用户只应通过本地 `.env` 文件或名为 `NETEASE_COOKIE` 的 GitHub Actions
Secret 提供凭据。Cookie 应像密码一样对待：

- 不要提交 `.env`。
- 不要在日志或 issue 中打印 Cookie 值。
- 环境变量值中不要包含字面量 `Cookie:` 前缀。
- 推荐使用完整的、以分号分隔的 Cookie 请求头值。
- 如果 Cookie 泄露，应重新获取并替换。

该 Skill 只允许经过脱敏的诊断信息，例如变量是否存在、长度、Cookie 对数量和
Cookie 名称。绝不能展示 `=` 后面的值。

## 目标仓库形态

该 Skill 面向包含 Node.js 同步器的目标仓库，命令通常类似：

```powershell
npm test
npm run sync -- --dry-run
npm run sync
```

生成的快照通常位于：

```text
data/
  index.json
  playlists/{playlistId}.json
  csv/{playlistId}.csv
  txt/{playlistId}.txt
```

当目标仓库包含个人歌单数据时，应保持私有。该 Skill 本身不包含个人数据，可以
单独开源发布。

## GitHub Actions

推荐的工作流支持：

- 使用 `workflow_dispatch` 立即手动验证。
- 使用每日 UTC `schedule` 定时同步。
- 将 `NETEASE_COOKIE` 配置为仓库 Secret。
- 可选地将 `NETEASE_UID` 配置为仓库变量。
- 仅在工作流需要提交生成快照时启用 `contents: write` 权限。

GitHub 定时工作流可能延迟执行。绿色运行表示工作流已完成，但不一定产生新
commit。歌单数据没有变化时，不产生 commit 是正常情况。

## 开发与校验

使用 skill-creator 系统 Skill 中的 Codex Skill 校验器：

```powershell
$env:PYTHONUTF8 = "1"
python path/to/skill-creator/scripts/quick_validate.py path/to/netease-playlist-sync
```

对该 Skill 进行发布前检查时，还应包括：

1. 扫描真实 Cookie、API key、token、本机用户路径和个人仓库名。
2. 检查 README 链接和安装路径是否具有可移植性。
3. 确认没有意外打包 `.env`、浏览器配置文件、生成的歌单数据或运行时依赖。

仓库还提供了一个不依赖第三方包的校验脚本：

```powershell
python scripts/validate_skill.py
```

## 限制

- 网易云网页接口不是稳定的公开 API。
- Cookie 可能过期或失效，届时需要用户重新获取。
- GitHub Actions 定时任务的执行时间不是精确闹钟。
- 该 Skill 不下载音频、歌词、封面或其他受版权保护的媒体文件。
- 网易云音乐和 Codex 是各自所有者的商标。本项目不隶属于任何一方。

## 许可证

MIT License。见 [LICENSE](LICENSE)。
