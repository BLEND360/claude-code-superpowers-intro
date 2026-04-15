# Claude Code Capabilities Workshops — Design

**Date:** 2026-04-15
**Target delivery:** May 2026
**Format:** Two workshops (W1 + W2), each available in 60-min and 90-min versions
**Audience:** Data scientists, data engineers, AI engineers, BI employees at a consultancy. Mixed Claude Code experience. Focus: leveraging Claude Code for professional, deployment-ready code.

## Goal

Equip a mixed-technical audience to use Claude Code with discipline (W1) and to extend it with professional-grade tools and authoring (W2). Across both workshops, every Claude Code primitive on the slide-2 capability diagram (CLAUDE.md, Permissions, Plan Mode, Checkpoints, Skills, Hooks, MCP, Plugins, Context, Slash Commands, Compaction, Subagents) gets airtime, with superpowers as the integrating worked example.

## Constraints

- Each workshop runs in **60-min "vital"** or **90-min "vital + bonus"** form. The 90-min version is a strict superset: vital content concludes by minute 60.
- Pacing: **~2/3 slides, ~1/3 demo**. Two demo slots per workshop with the option to merge live.
- Demo environment: **VSCode extension** throughout (visible status line, in-IDE checkpoints).
- Audience is consultants — workshops must teach **transferable patterns** while showing concrete examples in the consultancy's own stack denominators (GitHub, Snowflake).

## Core narrative

- **W1 — Using Claude Code well:** Cover the everyday primitives, then pivot to superpowers as the workflow that uses those primitives with rigor (brainstorming → writing-plans → subagent-driven development).
- **W2 — Power tools + authoring snack:** Tour professional-grade MCPs and plugins to consume (~70%), then a short authoring example so attendees know how small the surface really is (~30%).

## Capability bucketing (slide-2 squares)

| Square | Workshop | How it appears |
|---|---|---|
| ① CLAUDE.md | W1 | Theory part 1 (5 min) — anchor topic |
| ② Permissions | W1 | Theory part 1 (3 min) |
| ③ Plan Mode | W1 | Theory part 1 (4 min) |
| ④ Checkpoints | W1 | Theory part 1 (4 min, with Plan Mode) |
| ⑤ Skills | W1 (consume) + W2 (author) | W1: superpowers consumes; W2: SKILL.md anatomy + live authoring demo |
| ⑥ Hooks | W2 | Theory part 2 (3 min) + 90-min bonus demo |
| ⑦ MCP | W2 | Theory part 1 (4 min concept) + Context7/GitHub/Snowflake live demos |
| ⑧ Plugins | W1 (install) + W2 (publish/marketplace) | W1: install superpowers; W2: marketplace mention |
| ⑨ Context | W1 | Theory part 1 (4 min, with Compaction) |
| ⑩ Slash Commands | W1 | Theory part 1 (4 min, with Plugins-as-install) |
| ⑪ Compaction | W1 | Theory part 1 (4 min, with Context) |
| ⑫ Subagents | W1 (used by superpowers) + W2 (mention only) | W1: superpowers' subagent-driven development; W2: brief mention as advanced |

## Shared timing skeleton (both workshops, 60-min form)

| Time | Block |
|---|---|
| 0–5 | Hook + agenda (recap of slide-2 capability diagram) |
| 5–25 | Theory part 1 (~20 min) |
| 25–33 | **Demo 1** (~8 min) |
| 33–48 | Theory part 2 (~15 min) |
| 48–58 | **Demo 2** (~10 min) |
| 58–60 | Close + pointer to next workshop |

**Live-pivot option:** if pacing slips, presenter can skip Demo 1, push all theory through min ~50, then run a single ~12–14 min combined demo.

## 90-min bonus skeleton

| Time | Block |
|---|---|
| 60–80 | Deeper demo (~20 min) |
| 80–90 | Open Q&A and audience-driven exploration |

The bonus extends, not introduces. Vital takeaways must conclude by minute 60.

---

# Workshop 1 — Primitives → Superpowers Pivot

## Theory part 1 (~20 min) — the everyday primitives

| # | Topic | Time | Notes |
|---|---|---|---|
| 1 | CLAUDE.md | 5 min | 3-level hierarchy, what to include, "keep under 200 lines." Existing slide 21 is reusable. |
| 2 | Context + Compaction | 4 min | What Claude sees per turn, when/why to compact. |
| 3 | Plan Mode + Checkpoints | 4 min | Read-only review before action; revert to any point. |
| 4 | Permissions | 3 min | allow/deny tool lists, settings.json basics. |
| 5 | Slash Commands + Plugins-as-install | 4 min | `/init`, `/plugin install`, what plugins ship. |

## Demo 1 (~8 min) — primitives in action

Open a fresh VSCode workspace. Run `/init` → show generated CLAUDE.md → make a small edit → kick off a tiny task in **plan mode** → show the checkpoint timeline → revert one step. End with: *"This works. But for real deployment-ready code we need more discipline."*

## Theory part 2 (~15 min) — superpowers as the workflow

| # | Topic | Time | Notes |
|---|---|---|---|
| 6 | What superpowers is | 3 min | A plugin (square ⑧) bundling skills (⑤), uses subagents (⑫) and slash commands (⑩) under the hood. Frame as "an opinionated workflow that wraps the squares you just learned." |
| 7 | Brainstorming skill | 3 min | One question at a time, 2–3 approach options, validated design before code. |
| 8 | Writing-plans skill | 3 min | Design → bite-sized tasks with tests + commits. |
| 9 | Subagent-driven development | 3 min | Fresh subagent per task, two-stage review (spec compliance + code quality). |
| 10 | Why this matters for deployment-ready code | 3 min | Failure modes of ad-hoc prompting; how each skill prevents one. |

## Demo 2 (~10 min) — live brainstorm of PromptCraft → reveal

1. **Live brainstorm (5–6 min):** Fresh repo, no context. Prompt: *"Let's use superpowers to brainstorm a tool that helps people write better LLM prompts."* Audience watches the one-question-at-a-time dialogue.
2. **Visual companion moment (~min 6–7):** Steer one question toward a visual/layout choice (e.g., *"how should the refined prompt be displayed — side-by-side diff, tabs, or stacked?"*) to trigger the browser companion offer. Accept; mockups render live.
3. **Pivot — the cooked turkey (~min 7–10):** *"Now imagine we ran that brainstorm to completion, then writing-plans, then subagent-driven implementation. Here's what falls out."* Open `docs/superpowers/specs/2026-04-10-promptcraft-design.md` + the plan; point out *"these came out of the workflow you just watched start."* Then `streamlit run promptcraft/app.py` and demo the running app for ~1 minute.

**Pre-empt the "but mine wouldn't produce that" objection:** *"Your brainstorm run will land somewhere different from this exact spec — that's the workflow doing its job, not a flaw. The point is the discipline, not the destination."*

**Safety net:** Keep the solution branch open in a second VSCode window. If the live brainstorm derails or visual companion doesn't trigger, pivot early with a narrated screenshot/recording fallback.

## W1 90-min bonus (30 min) — the curveball + Q&A

Continue from Demo 2 (or restart in a fresh repo). Kick off a brainstorm or plan, get a few steps in, then mid-implementation interrupt with: *"Actually, the user just told us they also need X, which contradicts the current spec."* Show how superpowers exits the current step, re-enters brainstorming/planning to integrate the new requirement, and resumes. Ad-hoc Claude Code would kludge X in; structured workflow handles it gracefully. Followed by Q&A.

## W1 close (~2 min)

Pointer to W2: *"Now you know how to use superpowers. Next time we'll cover advanced MCPs you can plug in, and how to extend Claude Code yourself."*

---

# Workshop 2 — Power Tools + Authoring Snack

## Theory part 1 (~20 min) — MCP & professional tools tour

| # | Topic | Time | Notes |
|---|---|---|---|
| 1 | What is MCP, why it matters | 4 min | Standard way to plug external tools/data into Claude. "USB-C of AI tooling." Reference square ⑦. |
| 2 | Context7 | 4 min | Up-to-date library docs; fixes the model-cutoff staleness problem. |
| 3 | GitHub MCP | 4 min | Repo/PR/issue ops. Featured because it's the consultancy denominator. |
| 4 | Snowflake MCP | 4 min | Featured because the org cert push is in flight; common at clients. |
| 5 | Headless mode (`claude -p`) + plugin marketplaces | 4 min | Scripting Claude into CI/cron; `/plugin install` + official + community marketplaces. |

**MCP buffet slide** (shown during topic 5): one slide listing client-stack-dependent options so attendees know where to look.

| Need on engagement | Look for MCP |
|---|---|
| Other cloud (Azure / AWS / GCP) | Azure MCP, AWS MCP |
| Other repo (Azure DevOps, GitLab) | Azure DevOps MCP, GitLab MCP |
| Tickets (Jira, Linear, ADO Boards) | Jira MCP, Linear MCP |
| Docs (Confluence, Notion, SharePoint) | Confluence MCP, Notion MCP |
| Chat (Teams, Slack) | Teams MCP, Slack MCP |
| Browser automation | Playwright MCP |
| Other DBs (Postgres, BigQuery, Databricks) | Postgres MCP, BigQuery MCP |

**Framing slide:** *"The MCP you install depends on your client's stack. We're demoing GitHub + Snowflake because they're the consultancy denominators. The pattern transfers."*

## Demo 1 (~8 min) — install + use Context7 live in PromptCraft

Open the PromptCraft solution branch from W1. Ask vanilla Claude: *"What's the current Streamlit API for [some recently-changed feature]?"* Show stale/wrong answer. Install Context7 MCP. Re-ask. Show correct, current answer with cited docs. Then have Claude actually modify `app.py` using Context7-fetched docs. Land on: *"This single MCP eliminates the #1 reason model output goes stale."*

## Theory part 2 (~10 min) — authoring snack

| # | Topic | Time | Notes |
|---|---|---|---|
| 6 | Skills authoring | 4 min | Anatomy of SKILL.md (frontmatter + body), location (`.claude/skills/`), how Claude discovers and triggers it. Show a short superpowers skill as the example. |
| 7 | Hooks | 3 min | PreToolUse / PostToolUse / Stop / SessionStart events; settings.json wiring; when to use them. |
| 8 | Custom subagents + plugin publishing | 3 min | Brief mention only — subagents covered in W1 via superpowers. Plugin publishing pointed at as "package skills + hooks + commands and share via marketplace." |

## Demo 2 (~10 min) — write a tiny custom skill in PromptCraft

Create `.claude/skills/review-prompt-quality/SKILL.md` — ~15 lines, frontmatter + body. Save. In a fresh Claude session in the same repo, ask *"review this prompt for me: …"* — watch the new skill auto-invoke (status line shows it). Edit the skill, re-trigger. Land on: *"Skills are this small. If you have a workflow you do twice, write a skill — it's 10 lines, not a project."*

## W2 90-min bonus (30 min) — Snowflake MCP + safety hook + Q&A

**Snowflake MCP + safety hook combo (~15 min):**

1. Install Snowflake MCP, authenticate against a sandbox warehouse, run a `SELECT` — show Claude reading schema and writing a real query.
2. Add a **PreToolUse hook** that intercepts any SQL statement starting with `DROP`, `DELETE`, `UPDATE`, or `TRUNCATE` against a production database name and *requires explicit confirmation*.

This combo:
- Aligns with the org Snowflake cert push
- Covers both pillars of W2 (MCP + hooks) in a single demo
- The "block destructive SQL on prod" pattern is literally deployment-ready code
- Is immediately portable to client engagements

**Q&A and audience-driven exploration (~15 min):** *"What MCP would help your daily work?"* — install one or two on the fly.

## W2 close (~2 min)

Where to learn more: Anthropic docs, superpowers repo, MCP registry. Encourage attendees to install one MCP this week.

---

# Cross-workshop continuity

Both workshops use the same PromptCraft repo (this repo's `solution` branch).

- **W1 Demo 2** introduces it as the cooked turkey after the live brainstorm reveal.
- **W2 Demo 1** extends it with Context7.
- **W2 Demo 2** adds a custom skill to it.
- **W2 bonus** adds the Snowflake MCP + safety hook to it.

Continuity reward: attendees see the same project grow from fresh-brainstorm to production-shaped code with safety guardrails. Anyone who misses W1 can still follow W2 because the repo state is checked in.

---

# Pre-workshop materials

**Sent ~3 days before W1:**

- Install instructions: Claude Code CLI + VSCode extension
- Install command: `/plugin install superpowers@claude-plugins-official`
- Verification: screenshot of expected status line showing skill names
- Optional pre-read: `guide/01-introduction.md` from this repo
- API key setup per org standard

**Sent between W1 and W2:**

- Context7 + GitHub MCP install instructions (ready to follow live)
- Snowflake sandbox credentials or dummy DB setup for the bonus demo
- Pointer to the PromptCraft solution branch they'll see extended

---

# Slide deck deltas needed

The existing deck (`docs/superpowers/workshops/Claude Code Capabilities Workshop.pptx`) has slides 1–5 as the workshop frame plus slides 6–35 as PRISM appendix material (unrelated). To deliver this design:

- **Slide 3 (Workshop-wise topics)** — rewrite to reflect the new bucketing (W1 = primitives + superpowers consumed; W2 = MCPs + authoring).
- **Slide 21 (CLAUDE.md)** — already drafted, reusable as W1 topic 1.
- **New W1 slides needed:** Context+Compaction, Plan Mode+Checkpoints, Permissions, Slash Commands+Plugins, What superpowers is, Brainstorming, Writing-plans, Subagent-driven development, Why this matters.
- **New W2 slides needed:** What is MCP, Context7, GitHub MCP, Snowflake MCP, Headless mode + marketplaces, MCP buffet, Framing slide, Skills authoring, Hooks, Custom subagents + plugin publishing.
- The 90-min bonus content does not need additional theory slides — it's all demo + Q&A.

---

# Open questions to resolve before delivery

Surfaced for tracking; not blocking design approval.

1. **Presenter(s)** — solo or co-presenters splitting W1/W2? Affects rehearsal of live brainstorm + demos.
2. **Audience size** — small (<15) allows real Q&A; large (50+) needs chat-moderated questions.
3. **Recording** — will sessions be recorded for async viewers?
4. **Snowflake sandbox** — confirm a dedicated sandbox warehouse exists for safe demos, or schedule setup.
5. **API costs** — confirm budget for live brainstorm + subagent demos; identify which API key the demo uses.
6. **Client confidentiality** — all demos use the public PromptCraft repo, so this should be a non-issue. Flag if any restrictions apply.

---

# Deliverables

Implementation produces the following artifacts. The user and a co-presenter build the actual slide decks themselves from these specs in their preferred MS-compatible format (pptx or similar).

1. **Slide-by-slide content specs** — one markdown file per workshop. Per slide: title, body bullets, ~60–90 sec speaker notes, demo cues, time markers.
2. **Presenter scripts / talking points** — full prose per topic so co-presenters can deliver consistently.
3. **Demo scripts** — exact commands, prompts, expected outputs, fallback plans, and what to point at on screen for each demo (W1 Demo 1, W1 Demo 2, W2 Demo 1, W2 Demo 2, W1 90-min bonus, W2 90-min bonus).
4. **Engineered "magic prompts"** — the W1 Demo 2 brainstorm seed prompt + steering question designed to reliably trigger the visual companion offer. Includes fallback narration if the offer doesn't fire.
5. **Pre-workshop attendee materials** — install instructions, verification screenshot/steps, pre-read pointer, troubleshooting FAQ. Two versions: pre-W1 and pre-W2.
6. **Demo asset files** in this repo:
   - `.claude/skills/review-prompt-quality/SKILL.md` — the W2 Demo 2 custom skill
   - Snowflake safety hook example — settings.json fragment + the hook script for the W2 90-min bonus
   - Example CLAUDE.md files for the W1 Demo 1 fresh-workspace walkthrough
7. **Pre-staged demo branches** in this repo:
   - `workshop-w1-demo` — clean state for the W1 fresh-brainstorm demo
   - `workshop-w2-demo` — solution-branch state with Context7/GitHub MCP instructions ready to follow live
8. **Slide 3 rewrite** — markdown spec for the corrected Workshop-wise topics slide reflecting the new bucketing.
9. **Rehearsal checklist + risk register** — what to dry-run, what can go wrong in each demo, and the fallback for each failure mode.

**Not produced by implementation:** actual .pptx files, custom diagrams (the slide-2 capability diagram is reused as-is), Snowflake sandbox provisioning, API key procurement, live demo delivery.

# Out of scope

- Claude Agent SDK (embedding Claude in custom apps) — could be its own future workshop.
- Deep authoring of plugins, custom subagent specifications, or MCP servers from scratch — W2 surfaces these as "you could build this" rather than teaching the build.
- Non-Claude-Code coverage (Cursor, Codex, Gemini CLI variations of these patterns).
- Workshop logistics: venue, recording infrastructure, attendee registration.
