# Workshop 1 — Slide-by-Slide Spec

Each slide section follows the standard convention: timing, layout, body bullets, ~75-second speaker notes, and an optional demo cue. Build the actual PPTX from this spec; deeper presenter prose lives in `presenter-script.md` and live-demo blow-by-blow lives in the `demo-N-script.md` files.

---

## Slide 1 — Workshop 1: Using Claude Code Well
**Time:** 0:00-0:30 (30 sec)
**Layout:** Title slide
**Body bullets:**
- Workshop 1: Using Claude Code Well
- James Irving · [date]
- Prerequisites: Claude Code installed, superpowers plugin active
**Speaker notes (~75 sec):**
Welcome, everyone. Over the next hour we're going to cover the foundations that separate people who get occasional value from Claude Code from people who rely on it daily for client-grade, deployment-ready work. Whether you've been using it for a month or you fired it up for the first time this morning, by the end of this session you'll understand the primitives that make everything else click — context management, plan mode, permissions — and you'll see them working together in two live demos. Let's get into it.

---

## Slide 2 — What We're Covering Today
**Time:** 0:30-2:00 (90 sec)
**Layout:** Two-column (capability diagram left, agenda list right)
**Body bullets:**
- ① CLAUDE.md — project memory
- ② Context + Compaction — what Claude sees
- ③ Plan Mode + Checkpoints — review before action
- ④ Permissions — tool safety guardrails
- ⑤ Slash Commands + Plugins — extensibility
- ⑥ What superpowers is — skills + subagents bundled
- ⑦ Brainstorm / Write-plan / Subagent-dev skills
- ⑧ Demo 1 (primitives) + Demo 2 (live brainstorm)
**Speaker notes (~75 sec):**
Here's the map for the hour. The left panel shows the capability diagram from the broader Claude Code capabilities workshop — eight squares, each a distinct superpower. Today we're living inside all eight. The right column is our agenda, roughly in the order we'll hit them. Notice the two demo blocks — those aren't slides you click through, they're live terminal sessions. The first demo shows all the primitives working in a real project context. The second demo walks through the superpowers skill workflow: brainstorm, write-plan, and subagent-driven development, end to end. If you've only ever used Claude Code as a fancy autocomplete, today is the turning point.

---

## Slide 3 — Housekeeping + Assumptions
**Time:** 2:00-5:00 (3 min)
**Layout:** Two-column (left: setup checklist; right: quick-check prompt)
**Body bullets:**
- Claude Code installed and authenticated (`claude --version`)
- superpowers plugin installed (`/plugin list` → superpowers in output)
- Status line visible in your terminal — should show skill name or idle indicator
- GitHub access confirmed (we'll push during demos)
- Raise your hand if your status line is NOT showing
**Speaker notes (~75 sec):**
Quick housekeeping before we dive in. Installation instructions were shared ahead of time — if you followed them you should have three things working: Claude Code itself, the superpowers plugin, and the status line indicator in your terminal. The status line is the fastest health check: when a skill is running you should see its name appear there. If you're not seeing anything, keep your hand up and we'll sort you out in the next two minutes — it's almost always a one-line fix in settings.json. For everyone else, I'm assuming you have a GitHub account connected and that you can run `claude` from the command line. We're not covering installation in this workshop; we're covering how to use the tool well once it's in place. Any blockers? Great — let's move.

---

## Slide 4 — CLAUDE.md: Project Memory
**Time:** 5:00-10:00 (5 min)
**Layout:** Two-column (left: hierarchy diagram; right: what-to-include list)

> **REUSE existing slide 21 from `Claude Code Capabilities Workshop.pptx` — already drafted; this section is the spec for what it should cover.**

**Body bullets:**
- What it is: a plain-text file Claude reads at the start of every session
- Three-level hierarchy: user-global → repo-root → sub-directory
- What to include: stack, conventions, repo structure, banned patterns, key contacts
- Keep it under 200 lines — beyond that, costs context and becomes stale
- `/init` scaffolds a starter CLAUDE.md from your existing files
- Iterate, don't preempt: write what's true now; update when it's wrong, not in advance
**Speaker notes (~75 sec):**
CLAUDE.md is the single highest-leverage investment you can make before your first Claude Code session on a new project. Think of it as the onboarding doc you wish existed when you joined the engagement — stack, conventions, where the bodies are buried. Claude reads the appropriate CLAUDE.md files at the start of every conversation, so anything you put there doesn't need to be re-explained every time. There are three levels: a user-global file for preferences that travel with you, a repo-root file for project-wide conventions, and sub-directory files for module-specific rules. On a consultancy project this is gold — you capture the client's naming conventions, the approved libraries, the deployment patterns, and every new conversation starts with that context pre-loaded. The 200-line cap is a practical discipline: longer files get stale and start costing meaningful context. Use `/init` to bootstrap from your existing code, then edit it down to what's actually load-bearing. And the iterate-don't-preempt rule: don't try to anticipate every edge case upfront. Write what's true today, and update the file when reality diverges. That's it.

---

## Slide 5 — Context + Compaction
**Time:** 10:00-14:00 (4 min)
**Layout:** Image + text (left: context-window diagram; right: bullet points)
**Body bullets:**
- Each Claude turn sees: CLAUDE.md files, conversation history, tool call results
- Context window is finite — older turns get compressed or dropped
- Auto-compaction triggers near the context limit; Claude summarises conversation history
- Manual `/compact` — use it before a big new task in a long session
- Signs you need `/compact`: Claude "forgets" earlier decisions; responses feel generic
- New session = clean context; use it strategically for large independent tasks
**Speaker notes (~75 sec):**
Understanding what Claude actually sees per turn is the key to understanding why sessions drift. Claude doesn't have a persistent memory outside of CLAUDE.md and the conversation history in front of it. As a session grows, you approach the context window limit, and Claude's auto-compaction kicks in — it summarises earlier parts of the conversation to free space. That summary preserves the gist but loses detail. In a consultancy context this matters a lot: if you've spent the first 20 turns aligning on architecture and then hit compaction, Claude may start giving you answers that contradict earlier decisions. The fix is proactive: before you start a large new task in a long session, run `/compact` manually to get a clean, intentional summary. And remember: a fresh `claude` session starts with zero conversation history. For large, independent tasks — like "implement the entire ingestion pipeline" — starting a new session is often cleaner than carrying an hour of context you don't need.

---

## Slide 6 — Plan Mode + Checkpoints
**Time:** 14:00-18:00 (4 min)
**Layout:** Two-column (left: plan-mode flow diagram; right: checkpoint rules)
**Body bullets:**
- Plan Mode: Claude reasons and proposes — no files written, no commands run
- Activate with `Shift+Tab` or `--plan` flag
- Review the plan before saying "go" — catch misunderstandings before they cost you
- Checkpoints: every significant step can be a commit; revert any step cleanly
- Use plan mode for: multi-file refactors, infra changes, anything irreversible
- Consultant workflow: plan → review with teammate → execute → checkpoint
**Speaker notes (~75 sec):**
Plan mode is your pre-flight checklist. When you activate it, Claude reasons through what it would do — reads relevant files, maps out the changes — but it writes nothing and runs nothing. You get a full description of the plan before a single byte changes on disk. For consultants this is invaluable: it's the difference between "I ran Claude and it deleted the config" and "I reviewed the plan, spotted the issue, corrected the instruction, and then ran it." Get into the habit of using plan mode for anything that touches multiple files or anything you couldn't quickly undo by hand. Checkpoints are the companion discipline: as Claude executes, each meaningful step should be a git commit. That gives you clean revert points if something goes sideways mid-task. Together, plan mode and checkpoints make Claude Code auditable — you can show a colleague exactly what was going to happen and exactly what did happen. On client engagements, that audit trail matters.

---

## Slide 7 — Permissions
**Time:** 18:00-21:00 (3 min)
**Layout:** Two-column (left: settings.json snippet; right: allow/deny principle)
**Body bullets:**
- Claude Code asks before running tools it hasn't been permitted
- `settings.json` → `allow` list: tools Claude can run without asking
- `settings.json` → `deny` list: tools Claude must never run
- Three scopes: user-global, project, local (gitignored)
- Safety value: deny lists prevent irreversible mistakes in production-adjacent contexts
- Start restrictive; widen permissions as you build trust with a workflow
**Speaker notes (~75 sec):**
Permissions are how you decide how much autonomy Claude has in your environment. By default Claude will ask before running most tools. You grant trust by adding tools to the allow list in settings.json; you enforce hard limits by adding them to the deny list. There are three scopes: the user-global settings travel with you across projects, the project-level settings are committed and shared with the team, and local settings are gitignored for personal overrides. For a consultancy working on client data, the deny list is your safety net: you can explicitly block anything that could exfiltrate data, modify production, or run without review. Start with a restrictive default and deliberately widen permissions as you build confidence in a workflow. This also makes Claude Code auditable — a new team member can read your settings.json and immediately understand the guardrails in place for that project. Permissions aren't about distrust; they're about making the defaults match the risk profile of your environment.

---

## Slide 8 — Slash Commands + Plugins
**Time:** 21:00-25:00 (4 min)
**Layout:** Two-column (left: slash command list; right: plugin install flow)
**Body bullets:**
- Built-in slash commands: `/init`, `/compact`, `/plan`, `/help`, `/memory`
- Plugins extend Claude Code with additional slash commands and skills
- Install: `/plugin install <name>` — superpowers is the one we use
- `/plugin list` to confirm what's installed
- Plugins ship as collections of skills (prompt libraries) Claude can invoke
- superpowers ships: brainstorming, writing-plans, subagent-driven-development, and more
**Speaker notes (~75 sec):**
Slash commands are Claude Code's built-in vocabulary — think of them as keyboard shortcuts for common actions. `/init` bootstraps your CLAUDE.md, `/compact` manages context, `/plan` enters plan mode. These work out of the box. Plugins extend that vocabulary. When you install a plugin, it registers new slash commands and skills that Claude can invoke by name. The superpowers plugin is the one this workshop is built around — it ships a curated set of skills for professional development workflows: brainstorming before you build, writing structured plans, and executing those plans through isolated subagents with review gates. You install it once with `/plugin install superpowers`, confirm with `/plugin list`, and from that point forward those skills are available in every session. Skills are the layer above raw prompting — they encode the workflow discipline so you don't have to re-invent it each time. The next few slides walk through the three core superpowers skills individually.

---

## Slide 9 — Demo 1 Coming Up
**Time:** 25:00-25:30 (30 sec)
**Layout:** Title slide (transition)
**Body bullets:**
- CLAUDE.md + context + plan mode + permissions + slash commands — all in one session
- Watch how the primitives combine in a real project context
- Live terminal — anything could happen (that's the point)
**Speaker notes (~75 sec):**
Alright — you've seen all five primitives in theory. Now let's watch them working together in a real project. I'm going to open a terminal, start a Claude Code session on a sample repo, and walk through a task that touches all of them: CLAUDE.md will be loaded, we'll use plan mode before making any changes, permissions will gate a couple of tool calls, and we'll use `/compact` to manage context as the session grows. Questions after the demo — let's roll.
**Demo cue:** transition into Demo 1 (see `docs/superpowers/workshops/workshop-1/demo-1-script.md`)

---

## Slide 10 — [DEMO 1 PLACEHOLDER] Demo 1 — Primitives in Action
**Time:** 25:00-33:00 (8 min)
**Layout:** Demo block (not a slide presenters click through)

> This is a live demo block, not a presenter slide. The full blow-by-blow is in `docs/superpowers/workshops/workshop-1/demo-1-script.md`. Return to slide deck at the 33:00 mark.

**Body bullets:**
- (No body bullets — presenter is in the terminal)
**Speaker notes (~75 sec):**
Follow the demo-1 script. Key beats: show CLAUDE.md being read at session start; use plan mode for the first meaningful change; trigger a permissions prompt and explain the allow/deny decision; hit a natural compaction moment and run `/compact` manually; finish with a clean checkpoint commit. Keep commentary live and spontaneous — the script is a safety net, not a teleprompter.

---

## Slide 11 — That Works — But Clients Need More
**Time:** 33:00-33:30 (30 sec)
**Layout:** Title slide (transition / bridge)
**Body bullets:**
- The primitives give you control
- Deployment-ready code needs repeatable discipline
- Three superpowers skills encode that discipline into the workflow
**Speaker notes (~75 sec):**
The demo showed what's possible with the primitives alone — and it's genuinely useful. But if you're delivering code to a client, "it works in my terminal" isn't enough. You need a process that consistently produces well-designed, tested, reviewable code, without depending on any individual having a good prompting day. That's what the superpowers skills are for. They encode the discipline into the workflow so it runs the same way whether it's your first task of the morning or your tenth task of the sprint. Let's look at each one.

---

## Slide 12 — What superpowers Is
**Time:** 33:30-36:30 (3 min)
**Layout:** Image + text (left: plugin architecture diagram with squares ⑤ ⑧ ⑩ ⑫ called out; right: bullets)
**Body bullets:**
- superpowers is a Claude Code plugin (square ⑧) that bundles skills (square ⑤)
- Skills invoke subagents (square ⑫) and slash commands (square ⑩) under the hood
- Install once: `/plugin install superpowers`
- Status line shows active skill name during execution
- Core skills shipped: brainstorming, writing-plans, subagent-driven-development
- Goal: repeatable, auditable, deployment-ready output on every run
**Speaker notes (~75 sec):**
Let's be precise about what superpowers actually is, because the terminology matters. A plugin is a package you install into Claude Code — it extends the slash command vocabulary and registers skills. A skill is a structured prompt workflow that Claude runs in response to a slash command. Subagents are isolated Claude sessions that skills spin up to do focused work without contaminating the main context. And slash commands are how you invoke all of this. superpowers bundles those layers into three opinionated workflows: brainstorming before you build, writing a structured plan before you code, and executing that plan through subagents with review gates. When a skill is running you'll see its name in your terminal status line — that's your signal that structured, governed work is happening. The install is a one-liner; the payoff is a workflow that consistently produces code a second engineer can review without a long explanation.

---

## Slide 13 — The Brainstorming Skill
**Time:** 36:30-39:30 (3 min)
**Layout:** Two-column (left: brainstorm flow diagram; right: example exchange)
**Body bullets:**
- Trigger: start of any new feature or significant change
- Asks one clarifying question at a time — no interrogation walls
- Surfaces 2-3 distinct design approaches with trade-offs
- Offers a visual companion (diagram / table) to support decision-making
- Ends with a validated design statement before any code is written
- Prevents: over-engineered first drafts, misunderstood requirements, rework
**Speaker notes (~75 sec):**
The brainstorming skill is the front door of the superpowers workflow. Before a single line of code is written, you run a structured design conversation. The skill asks one focused question at a time — it doesn't dump a form on you — and it listens carefully before proposing options. You get two or three distinct approaches, each with honest trade-offs, not just the one Claude thinks is coolest. For a data engineer at a consultancy, this is the difference between "I built the transformation layer and it works" and "I had a ten-minute design conversation, we picked the approach that fits the client's Snowflake contract tier, and the code was right the first time." The session ends with a validated design statement — a clear, agreed description of what you're building — which feeds directly into the next skill. No validated design, no plan. That's the gate.

---

## Slide 14 — The Writing-Plans Skill
**Time:** 39:30-42:30 (3 min)
**Layout:** Two-column (left: plan file structure; right: task breakdown example)
**Body bullets:**
- Input: validated design from brainstorming (or your own spec)
- Breaks design into bite-sized implementation tasks
- Each task: clear acceptance criteria, a test to write first, a commit message
- Output: a markdown plan file checked into the repo
- Plan file is reviewable, commentable, editable before execution starts
- Prevents: big-bang PRs, untestable commits, scope creep mid-execution
**Speaker notes (~75 sec):**
Once you have a validated design, writing-plans converts it into an execution roadmap. Each task in the plan is scoped to be independently implementable — typically under two hours of work — with explicit acceptance criteria, a test you write before the implementation, and a suggested commit message. The whole thing lands as a markdown file in your repo. That's not just organisational tidiness: it means your plan is version-controlled, shareable, and commentable in GitHub before execution starts. On a client engagement this is powerful — the tech lead can review the plan in a PR comment, flag the two tasks that conflict with the data contract, and you fix them before any code is written. The plan file also becomes the handoff document: anyone on the team can pick up execution mid-stream because the context and acceptance criteria are all there. Big-bang PRs are one of the biggest friction points in consulting delivery; this skill eliminates them by design.

---

## Slide 15 — Subagent-Driven Development
**Time:** 42:30-45:30 (3 min)
**Layout:** Two-column (left: subagent isolation diagram; right: two-stage review flow)
**Body bullets:**
- Executes the plan file one task at a time
- Each task runs in a fresh subagent — no context bleed between tasks
- Stage 1 review: did the output meet the task's spec and acceptance criteria?
- Stage 2 review: is the code quality acceptable (style, tests, edge cases)?
- Both stages must pass before the next task begins
- Produces a clean commit per task — reviewable, revertable, attributable
**Speaker notes (~75 sec):**
Subagent-driven development is the execution engine. When you invoke it, Claude works through your plan file task by task. Crucially, each task runs in a fresh subagent — an isolated Claude session that only has the context relevant to that one task. This is why context bleed doesn't accumulate: the decision you made in task 3 doesn't silently influence task 7. Each subagent starts clean. After each task completes, there are two review gates. The first checks spec compliance: did the output actually satisfy the acceptance criteria in the plan? The second checks code quality: is the implementation clean, tested, and free of obvious issues? Only when both gates pass does execution move to the next task. The result is a series of clean, purposeful commits — one per task — that any reviewer on the team can understand without context-switching into your terminal session. For clients who are skeptical of AI-assisted development, this audit trail is often the thing that builds confidence.

---

## Slide 16 — Why This Matters for Deployment-Ready Code
**Time:** 45:30-48:00 (2.5 min)
**Layout:** Two-column (left: failure modes; right: skill that prevents each)
**Body bullets:**
- Ad-hoc prompting failure: misunderstood requirements → Brainstorming prevents it
- Ad-hoc prompting failure: untestable monolithic changes → Writing-plans prevents it
- Ad-hoc prompting failure: context drift across long sessions → Subagent isolation prevents it
- Ad-hoc prompting failure: no audit trail for reviewers → Commit-per-task prevents it
- Combined: a workflow a colleague can review, a client can trust, a pipeline can validate
**Speaker notes (~75 sec):**
Let's make the case explicitly, because you will be asked to make it to sceptical colleagues. Ad-hoc prompting — "I just talk to Claude and it writes code" — has four recurring failure modes in professional delivery. First: requirements are misunderstood because there was no structured design conversation. Second: changes are monolithic and hard to review because there was no task decomposition. Third: later tasks contradict earlier decisions because context drifted in a long session. Fourth: reviewers can't audit the work because there's no trail. The superpowers workflow maps one skill to each failure mode. Brainstorming surfaces requirements disagreements before they become code. Writing-plans decomposes work into reviewable units. Subagent isolation prevents context drift. Commit-per-task creates the audit trail. The output isn't just code that runs — it's code that a second engineer can review, a CI pipeline can validate, and a client can accept without a long explanation. That's deployment-ready.

---

## Slide 17 — Demo 2 Coming Up
**Time:** 48:00-48:30 (30 sec)
**Layout:** Title slide (transition)
**Body bullets:**
- We're going to run the full workflow live: brainstorm → plan → execute
- Starting from a real feature request, ending with reviewable commits
- Watch how the skills hand off to each other
**Speaker notes (~75 sec):**
Now let's watch the three skills run end to end. I'm starting from a feature request — no pre-written spec, no pre-loaded context — and we'll run brainstorming, let it produce a validated design, pipe that into writing-plans to get the task breakdown, and then kick off subagent-driven development for at least the first two tasks so you can see the review gates in action. This is the workflow your team can run tomorrow morning on a real client task.
**Demo cue:** transition into Demo 2 (see `docs/superpowers/workshops/workshop-1/demo-2-script.md`)

---

## Slide 18 — [DEMO 2 PLACEHOLDER] Demo 2 — Live Brainstorm + Reveal
**Time:** 48:00-58:00 (10 min)
**Layout:** Demo block (not a slide presenters click through)

> This is a live demo block, not a presenter slide. The full blow-by-blow is in `docs/superpowers/workshops/workshop-1/demo-2-script.md`. Return to slide deck at the 58:00 mark.

**Body bullets:**
- (No body bullets — presenter is in the terminal)
**Speaker notes (~75 sec):**
Follow the demo-2 script. Key beats: start brainstorming with a fresh feature request; show the single-question-at-a-time flow; accept one of the 2-3 design options; watch writing-plans produce the task file; invoke subagent-driven-development; show the Stage 1 and Stage 2 review gates for the first task; show the commit. Keep commentary live. If something unexpected happens — great, narrate it. The audience learns more from one honest recovery than ten smooth rehearsed runs.

---

## Slide 19 — Closing + What's Next in Workshop 2
**Time:** 58:00-60:00 (2 min)
**Layout:** Two-column (left: W1 recap; right: W2 preview)
**Body bullets:**
- W1 recap: CLAUDE.md · Context · Plan Mode · Permissions · Slash Commands · superpowers skills
- The workflow: Brainstorm → Write Plan → Subagent-Execute → Review → Ship
- W2 preview: project-specific CLAUDE.md deep-dives, team settings, Snowflake integration patterns
- Action for this week: run the brainstorming skill on one real task before the next session
- Resources: `docs/superpowers/` in this repo; `claude.ai/docs`; team Slack channel
**Speaker notes (~75 sec):**
That's Workshop 1. You've seen the full stack: the primitives that give you control, the superpowers skills that encode repeatable discipline, and a live run of the end-to-end workflow. Your homework — genuinely, not just a thing I say — is to run the brainstorming skill on one real task this week before you write a single line of code. It takes ten minutes and it will change how you think about the tool. Workshop 2 goes deeper: we'll build project-specific CLAUDE.md files for a real engagement, configure team settings so everyone on a project shares the same guardrails, and look at Snowflake-specific patterns that are already showing up in our pipeline work. All the reference material is in the `docs/superpowers/` directory of this repo. Questions? Grab me after or drop them in the Slack channel. Thanks, everyone.
