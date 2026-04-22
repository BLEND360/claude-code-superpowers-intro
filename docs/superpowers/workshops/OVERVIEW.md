# Claude Code Capabilities Workshops — Overview

A condensed tour of the two-workshop curriculum. Use this to orient a new reader (co-presenter, reviewer, or attendee lead) before diving into specs, presenter scripts, or demos.

- **Full spec:** [2026-04-15-claude-code-workshops-design.md](../specs/2026-04-15-claude-code-workshops-design.md)
- **Implementation plan:** [2026-04-15-claude-code-workshops.md](../plans/2026-04-15-claude-code-workshops.md)
- **Target delivery:** May 2026

## Companion resources

- **Demo notebook (NotebookLM):** https://notebooklm.google.com/notebook/182d30ca-ab5a-40cb-86d5-a91be55c9e73

**Slide deck generation note.** The most recent slide deck was generated from the per-workshop `slides.md` and `presenter-script.md` files using this prompt:

> Follow the outline in slides.md and implement the design indicated for each slide, adding relevant narrative from the presenter-script. Add a title slide (not included in the outline).

---

## Audience and goal

**Audience:** Data scientists, data engineers, AI engineers, and BI employees at a consultancy. Mixed Claude Code experience.

**Goal:** Equip attendees to use Claude Code with discipline (W1) and to extend it with professional-grade tools and authoring (W2). Across both workshops, every capability on the slide-2 diagram (CLAUDE.md, Permissions, Plan Mode, Checkpoints, Skills, Hooks, MCP, Plugins, Context, Slash Commands, Compaction, Subagents) gets airtime.

---

## Format

- Two workshops: **W1** and **W2**
- Each has a **60-min "vital"** version and a **90-min "vital + bonus"** version
- 90-min is a strict superset — vital takeaways conclude by minute 60
- Pacing: **~2/3 slides, ~1/3 demo** with two demo slots per workshop
- Demo environment: **VSCode extension** (visible status line, in-IDE checkpoints)

### Shared 60-min timing skeleton

| Time | Block |
|---|---|
| 0–5 | Hook + agenda |
| 5–25 | Theory part 1 (~20 min) |
| 25–33 | **Demo 1** (~8 min) |
| 33–48 | Theory part 2 (~15 min) |
| 48–58 | **Demo 2** (~10 min) |
| 58–60 | Close + pointer to next workshop |

### 90-min bonus add-on

| Time | Block |
|---|---|
| 60–80 | Deeper demo (~20 min) |
| 80–90 | Open Q&A and audience-driven exploration |

---

## Workshop 1 — Using Claude Code Well

Covers the everyday primitives, then pivots mid-workshop to **superpowers** as the integrating workflow.

### Topics

**Theory part 1 — everyday primitives (~20 min)**
1. CLAUDE.md (5 min)
2. Context + Compaction (4 min)
3. Plan Mode + Checkpoints (4 min)
4. Permissions (3 min)
5. Slash Commands + Plugins-as-install (4 min)

**Theory part 2 — superpowers as the workflow (~15 min)**
6. What superpowers is (3 min)
7. Brainstorming skill (3 min)
8. Writing-plans skill (3 min)
9. Subagent-driven development (3 min)
10. Why this matters for deployment-ready code (3 min)

### Demos

- **Demo 1 (~8 min) — primitives in action.** Fresh VSCode workspace: `/init` → CLAUDE.md tour → small edit → plan mode → checkpoint timeline → revert. Lands on *"this works, but for real deployment-ready code we need more discipline."*
- **Demo 2 (~10 min) — live brainstorm of PromptCraft → cooked-turkey reveal.** Run the superpowers brainstorming skill live on a fresh repo. Steer one question toward a visual/layout choice to trigger the visual companion. Then pivot: *"Imagine we ran this through writing-plans and subagent-driven implementation — here's what falls out."* Open the PromptCraft spec + plan + running Streamlit app on the `solution` branch.
- **90-min bonus (~30 min) — the curveball + Q&A.** Mid-implementation, inject a contradicting new requirement. Show how superpowers re-enters brainstorming/planning gracefully where ad-hoc prompting would kludge.

---

## Workshop 2 — Power Tools + Authoring

**~70% consume / 30% author.** Tour professional-grade MCPs, then a short authoring snack — write a custom skill in 5 minutes.

### Topics

**Theory part 1 — MCP & professional tools tour (~20 min)**
1. What is MCP, why it matters (4 min) — framed as "USB-C of AI tooling"
2. Context7 (4 min) — up-to-date library docs
3. GitHub MCP (4 min) — consultancy denominator
4. Snowflake MCP (4 min) — aligns with org cert push
5. Headless mode (`claude -p`) + plugin marketplaces (4 min)

*Plus an **MCP buffet slide** listing Azure / AWS / Jira / Linear / Confluence / Notion / Teams / Slack / Playwright / Postgres / BigQuery options for varied client stacks.*

**Theory part 2 — authoring snack (~10 min)**
6. Skills authoring (4 min) — SKILL.md anatomy, `.claude/skills/` location, discovery
7. Hooks (3 min) — PreToolUse / PostToolUse / Stop / SessionStart events
8. Custom subagents + plugin publishing (3 min) — mentioned only

### Demos

- **Demo 1 (~8 min) — install + use Context7 live in PromptCraft.** Ask vanilla Claude a Streamlit API question → stale answer. Install Context7 → re-ask → correct, current answer. Then have Claude modify `app.py` using Context7-fetched docs.
- **Demo 2 (~10 min) — write a tiny custom skill in PromptCraft.** Create `.claude/skills/review-prompt-quality/SKILL.md` (~15 lines). In a fresh Claude session, ask *"review this prompt for me"* — watch it auto-invoke. Edit, re-trigger. Lands on *"skills are this small — 10 lines, not a project."*
- **90-min bonus (~30 min) — Snowflake MCP + PreToolUse safety hook.** Install Snowflake MCP against a sandbox. Add a PreToolUse hook that intercepts `DROP`/`DELETE`/`UPDATE`/`TRUNCATE` against prod database names and requires explicit confirmation. Covers both W2 pillars (MCP + hooks) in one demo. Followed by audience-driven Q&A.

---

## Cross-workshop continuity

Both workshops use the same PromptCraft repo (this repo's `solution` branch):

- **W1 Demo 2** introduces PromptCraft as the cooked turkey after the live brainstorm reveal
- **W2 Demo 1** extends it with Context7
- **W2 Demo 2** adds a custom skill to it
- **W2 bonus** adds Snowflake MCP + safety hook to it

Attendees see the same project grow from fresh-brainstorm to production-shaped code with safety guardrails. Anyone who misses W1 can still follow W2 because the repo state is checked in.

---

## Capability coverage map

Every square on the slide-2 capability diagram gets airtime across the two workshops:

| # | Capability | Workshop | How it appears |
|---|---|---|---|
| ① | CLAUDE.md | W1 | Theory part 1 anchor topic |
| ② | Permissions | W1 | Theory part 1 |
| ③ | Plan Mode | W1 | Theory part 1 |
| ④ | Checkpoints | W1 | Theory part 1 (with Plan Mode) |
| ⑤ | Skills | W1 (consume) + W2 (author) | W1: superpowers consumes; W2: SKILL.md anatomy + live authoring |
| ⑥ | Hooks | W2 | Theory part 2 + 90-min bonus demo |
| ⑦ | MCP | W2 | Theory part 1 + Context7/GitHub/Snowflake demos |
| ⑧ | Plugins | W1 (install) + W2 (marketplace) | W1: install superpowers; W2: marketplace mention |
| ⑨ | Context | W1 | Theory part 1 (with Compaction) |
| ⑩ | Slash Commands | W1 | Theory part 1 (with Plugins-as-install) |
| ⑪ | Compaction | W1 | Theory part 1 (with Context) |
| ⑫ | Subagents | W1 (via superpowers) + W2 (mention) | W1: subagent-driven development; W2: brief mention |

---

## Deliverables produced

1. Slide-by-slide content specs — one markdown file per workshop with title/bullets/~60–90 sec speaker notes/demo cues/time markers per slide
2. Presenter scripts — full prose talking points for consistent delivery
3. Demo scripts — exact commands, prompts, expected outputs, and fallback plans
4. Engineered "magic prompts" — the W1 Demo 2 brainstorm seed + steering question that reliably triggers the visual companion
5. Pre-workshop attendee materials — install instructions, verification, pre-read pointer, FAQ (W1 and W2 versions)
6. Demo asset files — example CLAUDE.md (done), custom skill (pending), Snowflake safety hook (pending)
7. Pre-staged demo branches — `workshop-w1-demo` and `workshop-w2-demo` (pending)
8. Slide 3 rewrite — markdown spec for the corrected topic-bucketing slide
9. Rehearsal checklist + risk register — dry-run steps, failure modes, and fallbacks

**Not produced:** actual .pptx files, Snowflake sandbox provisioning, API key procurement, live demo delivery. The user and a co-presenter build the decks from these specs.

---

## Current status

**Paused after Task 17, awaiting partner review.** 17 of 21 plan tasks complete. Remaining:

- Task 18 — custom Skill asset for W2 Demo 2
- Task 19 — Snowflake safety hook asset for W2 90-min bonus
- Task 20 — pre-staged demo branches (`workshop-w1-demo`, `workshop-w2-demo`)
- Task 21 — workshops index README + final cross-link verification

All content for Tasks 18–19 is fully specified inline in the plan. To resume, ask Claude to "resume the workshops plan."

---

## Walkthrough reading order

For orienting a co-presenter or reviewer:

1. This doc (you are here)
2. [Design spec](../specs/2026-04-15-claude-code-workshops-design.md) — the "why"
3. [W1 slides](workshop-1/slides.md) + [W1 presenter script](workshop-1/presenter-script.md) side by side
4. [W2 slides](workshop-2/slides.md) + [W2 presenter script](workshop-2/presenter-script.md) side by side
5. Demo scripts for whichever demos they will own
6. [Rehearsal checklist](rehearsal-checklist.md) before any dry-run

## Open questions

Tracked but not blocking:

1. Presenter(s) — solo or co-presenters splitting W1/W2?
2. Audience size — affects Q&A format
3. Recording — will sessions be recorded?
4. Snowflake sandbox — confirmed dedicated warehouse?
5. API costs — budget confirmed, which key?
6. Client confidentiality — public PromptCraft repo only, flag any restrictions
