# Workshop 1 — Presenter Script

This document is the prose companion to `slides.md`. Use it to read or paraphrase the talking points for each substantive topic slide. There is one section per content topic — skip it if you are covering a transition, housekeeping, or demo placeholder slide. A backup presenter can deliver the full workshop from this script alone.

---

## CLAUDE.md: Project Memory

Before you can understand why CLAUDE.md matters, you need to feel the failure mode it prevents. Picture this: you spend the first fifteen minutes of a Claude Code session re-explaining the project — the stack is dbt on Snowflake, the naming convention is snake_case everywhere, the client insists on `staging` schemas before anything lands in `prod`, and there are two banned libraries because of a licensing issue discovered six months ago. You write it all out, Claude confirms it, the session goes well. Next morning you open a new session and type your first prompt. Claude has no memory of any of it. You start over.

**CLAUDE.md is the fix.** It is a plain-text file — or a small set of them — that Claude reads at the start of every conversation. Anything you put there does not need to be re-explained. For a data engineer at a consultancy, this is transformative: you capture the client's conventions once, correctly, and every session — yours, a colleague's, a backup presenter's — starts with that context pre-loaded. The file lives in the repo, so it travels with the code.

There is a **three-level hierarchy** to understand. The user-global CLAUDE.md lives in `~/.claude/CLAUDE.md` and contains preferences that travel with you across all projects: your preferred testing framework, your style for commit messages, the fact that you want plan mode on by default. The repo-root CLAUDE.md is committed to the project and shared with the team: stack details, key architectural decisions, deployment patterns, banned patterns, key contacts. Sub-directory CLAUDE.md files let you add module-specific rules — for example, the `ingestion/` directory might note that all connectors must implement a retry interface. Claude reads all applicable files for the current working directory, so the rules compose naturally.

The **200-line cap** is a practical discipline, not an arbitrary limit. Beyond that, the file starts costing meaningful context on every turn, and it almost certainly contains stale guidance. The rule of thumb: only write what is true and load-bearing right now. Use `/init` to bootstrap a starter CLAUDE.md from your existing codebase — Claude will read your files and draft the onboarding doc. Then edit it down to what's actually necessary. And follow the **iterate-don't-preempt principle**: do not try to anticipate every edge case upfront. Write what is true today; update the file when reality diverges from what it says. A short, accurate CLAUDE.md is worth ten times a long, aspirational one.

For consultants specifically, this is one of the highest-leverage habits you can build. Each engagement has unique conventions, unique guardrails, unique contact points. A well-maintained CLAUDE.md means every team member — and every Claude session — starts from the same shared understanding. It is the onboarding doc that actually stays current.

**Transition into next topic:** "Now that Claude starts every session with your conventions pre-loaded, let's talk about what happens to that context as the session grows — because it doesn't last forever."

---

## Context + Compaction

Think of a Claude Code session as a meeting with a finite number of minutes on the whiteboard. Every turn you take — your message, Claude's response, any tool calls — uses some of those minutes. The whiteboard has a hard limit. When you approach it, Claude's auto-compaction kicks in automatically: it summarises the earlier parts of the conversation, preserving the gist but losing detail, and replaces the verbose history with that summary. The session continues, but it is no longer working from the full record.

**What Claude actually sees per turn** is: all the CLAUDE.md files for the current context, the conversation history up to the context limit, and the results of any tool calls. That is it. There is no background memory, no cross-session persistence beyond CLAUDE.md. This is the key insight most people miss: the intelligence is real, but the memory is bounded and session-scoped. A colleague asking "does Claude remember what we decided last week?" is asking the wrong question. The answer is only yes if you put it in CLAUDE.md or are still in the same session.

The **practical signs you need `/compact`** are specific: Claude starts contradicting earlier decisions, or its responses become noticeably generic — it stops referencing the specific conventions and context you established at the start of the session and starts giving answers that would apply to any project. When you see those signs, run `/compact` manually. This triggers an intentional, controlled summarisation rather than waiting for auto-compaction to fire at an unpredictable moment. You can optionally give `/compact` a focus hint — "summarise with emphasis on the architecture decisions" — to guide what gets preserved.

**Starting a fresh session is a deliberate tool, not a sign of failure.** For large, independent tasks — "implement the entire ingestion pipeline," "refactor all the dbt models to use a new macro" — a new session is often cleaner than carrying an hour of conversational context you no longer need. The fresh session reads your CLAUDE.md, which has the persistent conventions, and starts without the accumulated drift. In a consultancy workflow, a natural rhythm is: one session per meaningful chunk of work, `/compact` within a session when you change focus significantly, and CLAUDE.md as the persistent layer that links everything together.

The analogy that lands well for this audience: think of CLAUDE.md as the written brief that survives every meeting, and the context window as the meeting itself. The meeting can only hold so much; the brief is what carries knowledge across meetings. Manage them both deliberately and you will not spend time re-establishing ground truth that should have been captured once.

**Transition into next topic:** "So now we know how to give Claude the right context and how to manage it over time. The next question is: how do we make sure Claude does the right thing with that context before it changes anything on disk?"

---

## Plan Mode + Checkpoints

Every engineer has a story about running a tool that did more than they expected. Plan mode is what prevents that story from involving Claude Code. When you activate plan mode — with `Shift+Tab` in the interactive session or the `--plan` flag from the command line — Claude enters a reasoning-only state. It reads the relevant files, maps out the changes it would make, and presents the full plan to you. **Nothing is written. Nothing is executed.** You see exactly what would happen before anything does.

The value for consultants is not just catching bugs — it is catching misunderstandings. You ask Claude to "refactor the transformation layer to use the new macro." Claude's plan tells you it intends to modify eleven dbt models, including three in the `finance` directory that you were pretty sure should be left alone. You catch that before a single file changes. You correct the instruction, review the new plan, and then proceed. The cost of that conversation is two minutes. The cost of fixing a bad refactor that touched the wrong models — and untangling what changed — is much higher.

**Get into the habit of using plan mode for anything that touches multiple files or anything you could not quickly undo by hand.** The specific trigger list that works well in practice: multi-file refactors, any change to infrastructure or configuration, anything in a production-adjacent context, and the first time you are asking Claude to do a task it has not done before in this project. For quick, targeted edits — "fix this one function's return type" — plan mode adds friction without much benefit. Develop the judgment for when the upfront review is worth it, and default to using it when you are uncertain.

**Checkpoints are the companion discipline.** As Claude executes a plan, each meaningful step should be a git commit. This is not just good git hygiene — it gives you clean, named revert points. If task 4 of an eight-task plan produces something unexpected, you revert to the task 3 checkpoint and re-examine rather than trying to figure out which of eight changes went wrong. The combination of plan mode and checkpoints makes Claude Code auditable in a way that raw prompting is not: you can show a colleague the plan that was reviewed and the commits that resulted from executing it. On client engagements, that traceability is often the difference between "we used AI and it worked" and "we can show you exactly what the AI did and why."

One more framing that connects this to deployment-ready code: plan mode and checkpoints are how you extend the code review process to cover AI-assisted changes. The plan is reviewable before execution. The commits are reviewable after. Neither the reviewer nor the presenter needs to have been in the terminal session to understand what happened.

**Transition into next topic:** "Plan mode controls what Claude does; permissions control what Claude is allowed to do. Those are different, and both matter — especially if you are working in a client environment."

---

## Permissions

Permissions are how you decide, deliberately, how much autonomy Claude Code has in your environment. The default behavior is that Claude will ask before running most tools — you will see a prompt like "I need to run this shell command; allow once, allow always, or deny?" That interaction-by-interaction approach is fine for getting started, but it does not scale to a team or a sensitive client environment. The `settings.json` file is where you encode your decisions so Claude behaves consistently without asking every time.

The **allow list** contains tools Claude can run without asking. If you have decided that running `pytest` in the project directory is always acceptable, you add it to the allow list and Claude runs it whenever it needs to without interrupting the flow. The **deny list** is harder: tools in the deny list Claude must never run, regardless of what you ask it to do in the conversation. For a consultancy working with client data, the deny list is your safety net. You might explicitly block any tool that could write outside the project directory, any network call to an external endpoint, or any command that modifies a production database. Those hard limits exist in the config file — they are not dependent on Claude making good judgment calls in a long session.

**There are three scopes**, and choosing the right scope for each setting matters. User-global settings travel with you across all projects — these are your personal defaults. Project-level settings are committed to the repo and shared with everyone on the team — these encode the guardrails that apply to this engagement. Local settings are gitignored and let you add personal overrides on top of the project defaults without affecting anyone else. For a team project, the right mental model is: the project settings.json is a team agreement about what Claude is allowed to do here, and everyone works within those constraints.

The consultancy reality that makes this concrete: you may be in a client environment where certain tools must not run automatically under any circumstances — not because Claude will misuse them, but because the client's security posture requires it, because the audit log needs to show human-approved actions, or because the consequence of a mistaken run is irreversible. Permissions let you encode that reality into the tool configuration rather than relying on everyone remembering to say "no" correctly in every session. **Start restrictive; widen deliberately.** A new team member joining the project reads the settings.json and immediately understands the guardrails. That is a form of documentation, and it is better than a README that gets out of date.

A common pattern that works well: project settings deny any write operations outside the project root and any network calls not on an explicit allowlist. Individual engineers add personal overrides in local settings for the specific tools their current task needs. When the task is done, the local override goes away. The project-level safety net is always there.

**Transition into next topic:** "So far we have covered the five primitives: CLAUDE.md, context management, plan mode, permissions, and now we are going to look at slash commands — which are how you invoke all of this efficiently, and which are also the gateway to the superpowers plugin we are about to install."

---

## Slash Commands + Plugins

Slash commands are Claude Code's built-in vocabulary for common operations. Rather than typing "please summarise the conversation and compress it," you type `/compact`. Rather than "enter plan mode for the next task," you type `/plan`. They are shorthand for actions the tool was designed to support, and building fluency with them is the difference between a deliberate, efficient session and one where you are constantly writing prose instructions for things that have first-class support.

The commands you will use most often in practice: **`/init`** bootstraps a CLAUDE.md from your existing codebase; **`/compact`** triggers a manual context summarisation; **`/plan`** enters plan mode; **`/memory`** opens your CLAUDE.md files for editing without leaving the session; and **`/help`** lists everything available if you cannot remember the syntax. These work out of the box with no configuration. They are the foundation, not the ceiling.

**Plugins extend that vocabulary.** A plugin is a package you install into Claude Code — it registers new slash commands and skills that become available in every session after installation. Installing a plugin is a one-liner: `/plugin install <name>`. Confirm what is installed with `/plugin list`. The mechanism is straightforward: plugins ship as collections of structured prompt workflows — skills — that Claude invokes in response to slash commands. When you install the superpowers plugin, you are adding a curated set of professional-development workflows on top of the built-in command set.

The key concept to understand before the next slides is the difference between a raw prompt and a skill. A raw prompt is you writing natural language instructions and hoping Claude interprets them consistently. A skill is a structured, opinionated workflow that runs the same way every time. It asks the right questions in the right order, applies the right discipline, and produces output in a predictable format. You do not need to remember how to run a good design conversation — the brainstorming skill encodes that. You do not need to remember how to structure a task breakdown — the writing-plans skill encodes that. The consistency is not in Claude's mood on a given day; it is in the workflow definition.

**Skills also compose.** The three core superpowers skills hand off to each other: brainstorming produces a validated design, writing-plans converts that design into a task file, subagent-driven development executes the task file with review gates. That chain runs the same way whether it is your first time or your fiftieth. The `superpowers` plugin is the container for all of it, and we are about to see all of this come together.

**Transition into next topic:** "Let's be precise about what superpowers actually is — because the terminology matters when you are explaining it to a colleague or a client."

---

## What superpowers Is

superpowers is a Claude Code plugin that bundles three opinionated development workflow skills into a single installable package. The install is one command: `/plugin install superpowers@claude-plugins-official`. That registers the skills, and from that point forward they are available in every Claude Code session. Confirm it is active with `/plugin list` — superpowers should appear in the output. During execution, **your terminal status line will show the active skill name** — that is your real-time signal that a structured, governed workflow is running rather than a free-form conversation.

It helps to be precise about the layer model. A **plugin** is the installable package — it is what you install once. A **skill** is a structured prompt workflow registered by the plugin — it is what runs when you invoke a slash command. A **subagent** is an isolated Claude session that skills spin up to do focused work — it is what executes your tasks without contaminating the main context. And **slash commands** are the invocation mechanism — they are what you type. superpowers wraps all four layers into a coherent system. When you see "subagent-driven development" in the status line, that means a skill is orchestrating subagents through a plan file with review gates — not just Claude typing code in your terminal.

The framing that connects this to the earlier primitives: **superpowers is an opinionated workflow that wraps the squares you just learned.** CLAUDE.md is still in play — the skills read it. Context management is still in play — the skills are designed to work within bounded contexts by using subagents for isolation. Plan mode principles are baked into the skill workflows — you review before execution. Permissions apply to everything the skills invoke. Slash commands are how you drive the skills. The plugin does not replace the primitives; it orchestrates them.

The goal is **repeatable, auditable, deployment-ready output on every run**. Not "good output when the prompt is right and the session is young." Every run. That is the claim, and the next three sections explain how the three skills deliver on it. The brainstorming skill handles requirements. The writing-plans skill handles design-to-task decomposition. The subagent-driven development skill handles execution with review. Together they address the four recurring failure modes of ad-hoc AI-assisted development — and we will map those explicitly at the end of this section.

For a data engineer or AI engineer at a consultancy, the concrete promise is: you can hand a superpowers-generated PR to a tech lead who has never touched the AI-assisted workflow, and they can review it the same way they review any other PR. The commits are clean, the tasks are documented, the acceptance criteria are stated. The AI involvement is legible rather than opaque. That matters for client trust and for team adoption.

**Transition into next topic:** "Let's start with the first skill — brainstorming — which is the front door of the workflow and the one that prevents the most expensive class of mistake."

---

## The Brainstorming Skill

The most expensive mistake in software development — especially in consulting delivery — is building the right thing wrong, or the wrong thing entirely, and only discovering this in review. The brainstorming skill is designed to prevent that. It runs a structured design conversation before a single line of code is written. The output is a **validated design statement**: a clear, agreed description of what you are building and how, which feeds directly into the writing-plans skill as its input.

The discipline that makes it work is **one question at a time**. This sounds like a small detail, but it changes the quality of the conversation significantly. When a tool dumps twelve questions on you at once, you skim and answer shallowly. When it asks one focused question, waits for your answer, and then asks the next relevant question based on what you said, the conversation surfaces detail that a form never would. After a handful of turns, the skill presents two or three distinct design approaches — not just the one Claude thinks is best — with honest trade-offs stated for each. You pick the approach that fits your constraints, the skill confirms the decision, and that confirmation is the validated design.

For a data engineer at a consultancy, consider what this looks like in practice. Your feature request is: "add a new transformation that calculates 30-day rolling average revenue by customer segment, broken down by product line." The brainstorming skill might ask: "Is the calculation window calendar days or business days?" Then: "Should this handle customers with fewer than 30 days of history, and if so, how?" Then: "Does the output need to land in the `reporting` schema or the `intermediate` schema?" Each of those is a decision that would have been made implicitly if you went straight to code. Here they are made explicitly, on record, before execution. The three approaches it might surface: a dbt incremental model with a rolling window, a Python transformation using a Snowflake UDF, and a pure SQL CTE-based approach. Each with the relevant trade-offs for your context.

The **visual companion offer** is worth mentioning to audiences who work with complex data models. For questions where a diagram or table would aid decision-making — "should I use a star schema or a normalised model here?" — the skill offers to generate a visual companion alongside the prose analysis. Data engineers and BI developers tend to find this genuinely useful for schema design questions.

The gate is strict: **no validated design, no plan.** That is the hand-off condition into the writing-plans skill. You cannot bypass it by going straight to planning, because the plan has nothing to plan from. The validated design statement is the contract between the design phase and the implementation phase, and it is the artefact that a tech lead can review before any code is written.

**Transition into next topic:** "Once you have a validated design, the writing-plans skill converts it into an execution roadmap — one that any team member can pick up and run."

---

## The Writing-Plans Skill

The writing-plans skill takes a validated design as its input and produces a markdown plan file as its output. That plan file is checked into the repo. It is the bridge between the design decision and the code that implements it, and the discipline it enforces is task decomposition: every significant piece of work is broken into independently implementable chunks before execution starts.

Each task in the plan has **four mandatory components**: a clear description of what to implement, explicit acceptance criteria that define what "done" looks like, a test to write before the implementation code, and a suggested commit message. The acceptance criteria are not vague — "the function should work correctly" is not an acceptance criterion. A good acceptance criterion is: "given a customer with 45 days of transaction history, the 30-day rolling average should equal the mean of days 16 through 45, with null for days 1 through 29." That is testable and specific. The test-first requirement is not optional; it is how each task produces reviewable evidence that the acceptance criteria were met.

The analogy for consultants: **the plan file is the SOW for the implementation phase.** Just as a statement of work is reviewed and agreed before a project starts, the plan file is reviewed and agreed before code execution starts. It is version-controlled — you can PR it, comment on it in GitHub, mark specific tasks as needing revision before any implementation runs. For a tech lead reviewing work from a junior engineer using AI assistance, the plan PR is the opportunity to catch architectural issues, scope creep, or misunderstood requirements before they become code. On a client engagement, catching a misunderstood requirement at plan-review time costs an hour. Catching it after the implementation is complete costs a day, and possibly a difficult conversation.

The structure of the resulting plan file also serves as the handoff document for the subagent-driven development skill. Each task entry is a self-contained brief: the subagent that executes it gets the task description, the acceptance criteria, and the test requirement. It does not need the broader session history to do its job correctly. That is by design — the plan file is the common language between the design phase, the implementation phase, and the review phase, and it is readable by humans at every step.

**Big-bang PRs are one of the most persistent friction points in consulting delivery**, and the writing-plans skill eliminates them structurally. A PR that is one task from the plan is small, purposeful, and reviewable in minutes. A PR that represents a week of AI-assisted work with no decomposition is impossible to review meaningfully. The plan file enforces the discipline before execution begins.

**Transition into next topic:** "Now let's look at how the plan actually gets executed — through the subagent-driven development skill, which handles isolation, review, and audit in a single workflow."

---

## Subagent-Driven Development

Subagent-driven development is the execution engine of the superpowers workflow. When you invoke it, it works through your plan file task by task. But the important detail is not the sequencing — it is the isolation. **Each task runs in a fresh subagent**: an independent Claude session that has only the context relevant to that one task. It sees the plan file entry for its task, the relevant CLAUDE.md files, and the current state of the codebase. It does not see the two-hour design conversation that preceded the plan, the failed approach from task 2, or the context drift that accumulates in a long session. Every task starts clean.

This solves a problem that is subtle but significant in practice. In a long-running Claude Code session, early decisions can silently influence later ones in ways that are hard to trace. If you spent the first 40 turns establishing that you are using a particular pattern, then hit compaction, and then started a new phase of work, the summary may not preserve every nuance. Later tasks might be influenced by a compressed version of your architecture that omits a constraint. With subagent isolation, **the decision from task 3 cannot silently contaminate task 7**. Each task is judged against the acceptance criteria in the plan, which were written when the full design context was clear.

The **two-stage review** after each task is what makes the output auditable. Stage 1 checks spec compliance: did the subagent's output satisfy the acceptance criteria stated in the plan file? This is a structured check, not a vibe check — the criteria are explicit, so the review is deterministic. Stage 2 checks code quality: is the implementation clean, tested, and free of obvious issues? Style, edge case handling, test coverage. Both stages must pass before execution moves to the next task. If either stage fails, the task is flagged and the issue is addressed before proceeding. **No passing review, no next task.**

The result is a series of clean commits — one per task — each with a commit message that was specified in the plan. A reviewer who joins the project mid-stream can read the commit history and the plan file and understand exactly what was built, why each task was scoped the way it was, and what evidence exists that the acceptance criteria were met. For clients who are skeptical of AI-assisted development, this audit trail is often what builds confidence. They are not asked to trust that Claude Code did good work; they are shown the evidence at the commit level.

For a data engineering team managing a Snowflake pipeline, the practical rhythm looks like this: one session per feature, starting with brainstorming, moving to a plan file that the team reviews in GitHub, and then subagent-driven development executing the plan with clean commits per task. The AI involvement is visible and auditable throughout. The team can see exactly what was planned and exactly what was built. That is not just a technical discipline — it is a professional practice.

**Transition into next topic:** "Let's make the case explicitly for why this matters — because you will be asked to make it to a skeptical colleague, a cautious tech lead, or a client who has heard bad things about AI-assisted code."

---

## Why This Matters for Deployment-Ready Code

The case for the superpowers workflow is not "Claude is powerful." Everyone has seen Claude write impressive-looking code in a demo. The case is more specific: **ad-hoc prompting has four recurring failure modes in professional delivery**, and the superpowers workflow maps one skill to each of them. Let's name them, because naming them makes them defensible.

Failure mode one: **misunderstood requirements.** You write a feature based on what you think the requirement means. The code ships. In review or in client UAT, it becomes clear that two people had different mental models of what the feature should do. This happens in human-only teams; it happens more often when the implementation is accelerated by an AI and there was no structured design conversation. The brainstorming skill prevents this by making requirements explicit, on record, before any code is written. The validated design statement is the artifact that demonstrates alignment.

Failure mode two: **untestable, monolithic changes.** A PR arrives that is 800 lines of changes across 15 files, produced in a single AI-assisted session. Reviewing it is exhausting. Finding the bug buried in it is nearly impossible. No one wants to be the reviewer who approved it when it broke something. The writing-plans skill prevents this structurally: work is decomposed before execution, and each task is scoped to be independently implementable and reviewable. PRs become small and purposeful by design.

Failure mode three: **context drift across long sessions.** This is the insidious one. The session starts strong — you established a clear architecture in the first 30 turns — but as the session grows and compaction kicks in, later tasks drift from the early decisions. You do not notice until a colleague points out that the new module contradicts the pattern established three weeks ago. Subagent isolation prevents this: each task gets a clean context derived from the plan file, not from a compressed version of a long conversation.

Failure mode four: **the just-one-more-prompt spiral.** You run Claude, the output is 90% right, you prompt to fix it, it introduces a different issue, you prompt again, eventually the code is tangled and you have lost track of what you intended. The two-stage review gate in subagent-driven development breaks that spiral: if a task does not pass review, it is flagged and addressed before you proceed, not discovered after three more tasks have been built on top of it.

The combined output of the superpowers workflow — validated design, structured plan, isolated execution, two-stage review, clean commits — is code that a second engineer can review, a CI pipeline can validate, and a client can accept without a long explanation. That is the definition of deployment-ready in a consulting context. **We are consultants. Our code ships to clients. We do not have the luxury of ad-hoc.** Now let's watch this happen live.

---
