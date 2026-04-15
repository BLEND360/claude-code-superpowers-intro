# Superpowers for Claude Code: A Practical Guide

This guide introduces the [superpowers](https://github.com/obra/superpowers) plugin for Claude Code — a collection of skills that bring structured workflows to AI-assisted development.

## Who This Is For

- **Data scientists** building LLM-powered tools and pipelines
- **AI engineers** working with Claude Code daily
- Both newcomers to AI-assisted coding and experienced users looking to level up

## What You'll Learn

Three key skills that transform chaotic prompting into systematic development:

1. **Brainstorming** — Turn rough ideas into validated designs before writing code
2. **Code Review** — Systematic review with technical rigor (not performative agreement)
3. **Subagent-Driven Development** — Fresh agents per task with two-stage review

## Start Here

1. [Introduction](guide/01-introduction.md) — Why structured workflows matter
2. [Tutorial](guide/02-tutorial.md) — Build a prompt engineering helper step-by-step

## The Example Project

Throughout this guide, we build **PromptCraft** — a Streamlit app that helps refine LLM prompts. It's meta (using Claude to build Claude tools), practical, and demonstrates all three skills in action.

## Proposed Workshops

A two-workshop curriculum built on top of this guide, aimed at a consultancy audience (data scientists, data engineers, AI engineers, BI employees) for shipping deployment-ready code with Claude Code. Each workshop is available in **60-min** (vital) and **90-min** (vital + bonus) versions; the 90-min is a strict superset.

### Workshop 1 — Using Claude Code Well

Covers the everyday primitives, then pivots mid-workshop to superpowers as the integrating workflow. Demo arc: live brainstorm of PromptCraft → reveal of the existing solution branch as the cooked-turkey payoff.

Topics: CLAUDE.md · Context · Compaction · Plan Mode · Checkpoints · Permissions · Slash Commands · Plugins (install) · Brainstorming · Writing-plans · Subagent-driven development.

### Workshop 2 — Power Tools + Authoring

~70% consume / 30% author. Tour of professional-grade MCPs (Context7, GitHub MCP, Snowflake MCP) followed by a short authoring snack — write a custom skill in 5 minutes. The 90-min bonus combines Snowflake MCP with a PreToolUse safety hook that blocks destructive SQL on prod databases.

Topics: MCP concept · Context7 · GitHub MCP · Snowflake MCP · Headless mode · Plugin marketplaces · Skills authoring · Hooks · Custom subagents (mention) · Plugin publishing (mention).

### Workshop materials

The full design, plan, and content artifacts live in `docs/superpowers/`:

- **Spec:** [docs/superpowers/specs/2026-04-15-claude-code-workshops-design.md](docs/superpowers/specs/2026-04-15-claude-code-workshops-design.md)
- **Plan:** [docs/superpowers/plans/2026-04-15-claude-code-workshops.md](docs/superpowers/plans/2026-04-15-claude-code-workshops.md)
- **Slide-by-slide content specs:** [workshop-1/slides.md](docs/superpowers/workshops/workshop-1/slides.md), [workshop-2/slides.md](docs/superpowers/workshops/workshop-2/slides.md)
- **Presenter scripts:** [workshop-1/presenter-script.md](docs/superpowers/workshops/workshop-1/presenter-script.md), [workshop-2/presenter-script.md](docs/superpowers/workshops/workshop-2/presenter-script.md)
- **Demo scripts (4 main + 2 bonus):** [workshop-1/](docs/superpowers/workshops/workshop-1/), [workshop-2/](docs/superpowers/workshops/workshop-2/)
- **Engineered demo prompts:** [magic-prompts.md](docs/superpowers/workshops/magic-prompts.md)
- **Pre-workshop attendee checklists:** [pre-workshop-w1.md](docs/superpowers/workshops/pre-workshop-w1.md), [pre-workshop-w2.md](docs/superpowers/workshops/pre-workshop-w2.md)
- **Rehearsal + risk register:** [rehearsal-checklist.md](docs/superpowers/workshops/rehearsal-checklist.md)
- **Slide 3 rewrite:** [slide-3-rewrite.md](docs/superpowers/workshops/slide-3-rewrite.md) (corrects the existing pptx)
- **Demo asset files:** [demo-assets/](demo-assets/) — example CLAUDE.md, custom skill, Snowflake safety hook

The current draft pptx (and PDF export) lives at [docs/superpowers/workshops/Claude Code Capabilities Workshop.pptx](docs/superpowers/workshops/). The user and a co-presenter build the actual decks themselves from the content specs above.

### Status — paused for partner review

Workshop content is complete (17 of 21 plan tasks done). The remaining 4 tasks are paused pending partner review of the slide specs, presenter scripts, and demo scripts. Once approved, these can be resumed:

- **Task 18 — custom Skill asset** for the W2 Demo 2 authoring demo (`demo-assets/w2-demo2-skill/.claude/skills/review-prompt-quality/SKILL.md`)
- **Task 19 — Snowflake safety hook asset** for the W2 90-min bonus demo (`demo-assets/w2-bonus-snowflake-hook/` — settings fragment + `safety_hook.py` + README)
- **Task 20 — pre-staged demo branches** (`workshop-w1-demo`, `workshop-w2-demo`) so demos can `git checkout` to known-good states
- **Task 21 — workshops index README + final cross-link verification** (`docs/superpowers/workshops/README.md`)

All content for Tasks 18–19 is fully specified inline in [the plan](docs/superpowers/plans/2026-04-15-claude-code-workshops.md). To resume, ask Claude to "resume the workshops plan."

### Topic coverage map

| Capability (slide-2 diagram) | Workshop |
|---|---|
| ① CLAUDE.md | W1 |
| ② Permissions | W1 |
| ③ Plan Mode | W1 |
| ④ Checkpoints | W1 |
| ⑤ Skills | W1 (consume via superpowers) + W2 (author) |
| ⑥ Hooks | W2 (90-min bonus) |
| ⑦ MCP | W2 |
| ⑧ Plugins | W1 (install) + W2 (marketplace) |
| ⑨ Context | W1 |
| ⑩ Slash Commands | W1 |
| ⑪ Compaction | W1 |
| ⑫ Subagents | W1 (used by superpowers) + W2 (mention) |
