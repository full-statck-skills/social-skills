<div align="center">

# social-skills

**社交与沟通技能 — Slack GIF、内部沟通**

[![GitHub](https://img.shields.io/badge/github-full--statck--skills%2Fsocial--skills-green.svg)](https://github.com/full-statck-skills/social-skills)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Compatible-purple.svg)](https://agentskills.io)

[English](./README.md) | 简体中文

[简介](#-简介) · [安装](#-安装) · [技能](#-技能) · [支持的智能体](#-支持的智能体) · [生态](#-生态)

</div>

---

## 📖 简介

**Social Skills** 是面向 AI 编码智能体的精选技能集合，属于 [Full Stack Skills](https://github.com/partme-ai/full-stack-skills) 生态，由 [PartMe.AI](https://github.com/partme-ai) 维护。

本包包含 **2 个技能**。每个技能是一个独立的 `SKILL.md` 文件，AI 智能体按需加载。

## 📦 安装

```bash
npx skills add full-statck-skills/social-skills
```

或安装特定技能：`npx skills add full-statck-skills/social-skills --skill <skill-name>`

## 🎯 技能 (2)

| 技能 | 描述 |
|------|------|
| `internal-comms` | 内部沟通最佳实践 |
| `slack-gif-creator` | 创建针对 Slack 优化的动画 GIF 的知识和工具 |

## 🤖 支持的智能体

适用于 [Claude Code](https://code.claude.com)、[Codex](https://developers.openai.com/codex)、[Cursor](https://cursor.com)、[OpenCode](https://opencode.ai)、[Gemini CLI](https://geminicli.com)、[GitHub Copilot](https://github.com/features/copilot)、[Windsurf](https://codeium.com/windsurf) 及 [70+ 其他平台](https://agentskills.io/clients)。

### Claude Code 安装

**方式一：npx skills CLI（推荐）**

```bash
npx skills add full-statck-skills/social-skills
```

**方式二：手动安装**

```bash
git clone https://github.com/full-statck-skills/social-skills.git
cp -r social-skills/skills/* .claude/skills/
```

更多详情请参阅 [Claude Code 技能指南](https://code.claude.com/docs/en/skills) 和 [Agent Skills 规范](https://agentskills.io/)。

## 🌐 生态

| 资源 | 链接 |
|------|------|
| **Full Stack Skills** | [github.com/partme-ai/full-stack-skills](https://github.com/partme-ai/full-stack-skills) |
| **所有技能组** | [github.com/full-statck-skills](https://github.com/full-statck-skills) |
| **Agent Skills 规范** | [agentskills.io](https://agentskills.io) |
| **Skills CLI** | [github.com/vercel-labs/skills](https://github.com/vercel-labs/skills) |

## 📄 许可证

Apache 2.0 — 详见 [LICENSE](LICENSE)。
