# 贡献指南

[English Contribution Guide](CONTRIBUTING_en.md) | 简体中文

欢迎通过 Issue 和 Pull Request 参与本项目。提交改动前，请先阅读本文件和
[Pull Request 模板](PULL_REQUEST_TEMPLATE.md)。

## 关于 Issue

涉及较大改动时，请先创建 Issue 讨论方案，等待维护者确认后再提交 PR。以下情况
建议先开 Issue：

- 新增 Skill 能力、目录结构或自动化流程；
- 修改凭据处理、GitHub Actions 权限或外部接口；
- 不确定是否为 Bug，或不确定当前行为是否有意设计；
- 可能影响其他 Agent 环境兼容性的改动。

报告问题时请使用 Issue 模板。不要在 Issue、截图或日志中粘贴 Cookie、API key、
访问令牌、浏览器配置文件、个人歌单数据或其他隐私信息。

## 提交变更

1. Fork 本仓库，并从 `main` 创建独立分支，例如 `docs/update-cn-readme`；
2. 一个 Pull Request 只处理一项聚焦的改动；
3. 提交信息使用 [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)，
   例如 `feat:`、`fix:`、`docs:`、`chore:`；
4. PR 描述应说明变更内容、变更原因和验证方式；
5. 如果无法完成某项检查，请说明原因以及替代验证方式；
6. 修改 Skill 时，欢迎附上经过脱敏的用户请求和 Agent 回复示例，不要附带真实
   凭据或个人数据。

## 项目结构

- `SKILL.md`：Skill 入口和核心行为约束；
- `README.md`、`README.zh-CN.md`：双语使用与发布说明；
- `agents/openai.yaml`：Codex 界面元数据；
- `.github/`：贡献指南、Issue/PR 模板和 CI；
- `scripts/validate_skill.py`：不依赖第三方包的本地校验；
- `LICENSE`、`CODE_OF_CONDUCT.md`、`SECURITY.md`：开源治理文档。

本仓库只发布 Skill，不接收个人同步项目的源码、歌单快照、`.env`、浏览器
Profile 或运行日志。

## 欢迎的贡献

- 修复 `SKILL.md`、README 或链接中的真实理解问题；
- 改进其他 Agent 环境中的加载兼容性；
- 增加经过验证的故障排查说明；
- 完善中英文文档和翻译；
- 改进凭据安全、敏感信息扫描和校验脚本；
- 提供真实运行反馈，包括失败案例和复现条件。

## 不予合并的贡献

- 提交真实 Cookie、API key、访问令牌、邮箱、电话、账号信息或个人歌单；
- 将凭据写入示例、测试、截图、日志、Issue、PR 或 Git 历史；
- 批量骚扰第三方服务、自动提交无关 PR 或绕过服务限制；
- 与本 Skill 无关的个人项目文件、构建产物或依赖目录；
- 只为制造 diff 或刷贡献记录的无实质内容改动。

## 禁止无实质内容的提交

除非修复了明确的问题、改善了渲染或满足格式规范，否则不要单独提交以下改动：

- 只替换同样正确的标点；
- 只增删空格、空行、换行或缩进；
- 不影响内容或渲染结果的机械排版调整；
- 大量无关的批量替换。

如果确实发现格式问题，请在 PR 中说明位置、实际影响和验证方式。

## 提交前检查

在创建 PR 前运行：

```powershell
$env:PYTHONUTF8 = "1"
python scripts/validate_skill.py
python path/to/skill-creator/scripts/quick_validate.py .
```

并确认：

- `.env`、Cookie、API key、token 和个人数据没有被暂存；
- README 中的相对链接有效；
- 没有添加 `data/`、浏览器 Profile、`node_modules/` 或本机私有路径；
- CI 和本地校验均通过。
