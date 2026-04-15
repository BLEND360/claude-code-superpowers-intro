# Workshop 2 — Presenter Script

This script is the prose companion to `slides.md`. It provides 3–5 paragraphs of substantive talking points per content topic so a presenter or co-presenter can read verbatim or paraphrase in their own voice. The slides carry ~75 seconds of speaker notes each; this script goes deeper on the "why" and the consulting-specific angles that reward extra time on a slide.

---

## What Is MCP

Before MCP existed, connecting an AI assistant to an external tool meant building a custom integration every single time. You needed a different API client, a different authentication scheme, a different way to pass context back into the model's window — for GitHub, for Snowflake, for Jira, for Confluence, for every tool on every engagement stack. The result was that "AI-augmented development" in practice meant a lot of copy-pasting between browser tabs and terminal windows. The AI sat in one window; the tools lived everywhere else.

**MCP — the Model Context Protocol — is the open standard that eliminates that gap.** It defines a single protocol that any AI host (Claude Code in our case) can use to talk to any external system, so long as that system has an MCP server wrapping it. The analogy that resonates is USB-C: before USB-C, every device needed its own cable. After USB-C, one cable standard handles power, data, display, and more. MCP is USB-C for AI tooling. You write — or install — a server once, declare it in `settings.json`, and from that point on Claude can call tools on it exactly the way it calls its built-in tools.

The architecture is worth making concrete. Claude Code is the host. It runs an MCP client. That client connects to one or more MCP servers, each of which wraps some external system. The server exposes three kinds of things: **tools** (actions Claude can invoke, like "run this SQL" or "open a PR"), **resources** (data Claude can read, like "return the schema of this table"), and **prompt templates** (pre-authored prompt fragments the server makes available). From the model's perspective, a GitHub MCP tool call looks no different from a file read — it's just another capability in the context.

**The security model is worth calling out explicitly**, especially if you're setting this up on a client engagement. Claude never holds credentials to the external system. The MCP server owns the authentication; Claude calls the tool and gets back structured data. If a client's security team asks "does this AI have my Snowflake password?", the honest answer is no — the MCP server does, and you control which server you install and how you scope its credentials. That separation of concerns is one of the protocol's deliberate design decisions.

For a consultancy context, the practical upshot is this: you can now ask Claude to do work that spans your full engagement stack in a single conversation. Read a Snowflake schema, check a GitHub PR, look up the latest dbt docs, draft a Confluence page — without leaving the Claude Code session. That is the unlock. The individual MCP servers we'll look at in the next three slides are examples of what that unlock looks like in practice.

**Transition into next topic:** "Let's look at the first MCP server — Context7 — which solves a specific and very practical problem with library documentation."

---

## Context7

If you have used Claude for library-specific coding questions, you have probably hit the training cutoff problem at least once. Claude's knowledge has a cutoff date — typically several months before you're talking to it — and popular libraries ship breaking changes faster than that. **Ask Claude about a Streamlit feature added three months after its training cutoff and it will confabulate: it will give you a confident, syntactically plausible answer that references an API that no longer exists, or never existed in quite that form.** The model isn't hallucinating randomly; it's extrapolating from what it knew, which is the wrong version.

Context7 solves this at the retrieval layer. When you prepend "use context7" to a library question, Context7 intercepts the query, fetches live documentation from the library's official source, pins it to the version you're using, and injects that real content into the model's context window before Claude answers. The citation it returns includes the source URL, the exact version string, and the retrieval date. You get an answer you can verify, and — critically for client-facing work — an answer you can show the provenance of.

**The install is a single command.** You add the Context7 MCP server to your `settings.json` and from that point on it's available in every session. The "use context7" trigger is a convention: you type it at the start of a library question and Context7 activates. You do not have to use it on every prompt — only on the ones where you need current docs. For general code tasks, Claude's built-in knowledge is fine. For anything touching a library that's been active in the last year, Context7 is the right move.

This works for any library in the catalog, not just the ones we're demoing. Pandas, scikit-learn, dbt Core, PySpark, the Snowflake Connector for Python, FastAPI, Polars — all of them move fast, all of them have breaking changes in recent releases. **For a data engineering engagement, the libraries that matter most are exactly the ones that change most often.** Context7 means you stop having to add "give me the current version of this" to every prompt you write and trust that the answer reflects reality.

From a team practice standpoint, it's worth making "use context7" a house habit for any library question. Put it in your CLAUDE.md as a recommendation. When a teammate posts a Claude answer that looks suspicious, the first diagnostic question is: did you use Context7? That shared vocabulary makes the tool's value visible and its use consistent across the engagement.

**Transition into next topic:** "Context7 handles the docs freshness problem. The next server — GitHub MCP — handles the repo and workflow layer."

---

## GitHub MCP

GitHub MCP is on this slide because it is the consultancy denominator. Every engagement this team is on touches GitHub in some form — source control, PR reviews, issue tracking, Actions for CI. The MCP server exposes the full GitHub API surface as Claude-callable tools, which means your entire development workflow can live in one context window instead of bouncing between the terminal, the GitHub web UI, and Claude.

**Specific use cases worth naming.** PR reviews from inside Claude: you can ask "show me the open PRs touching the ingestion pipeline and summarize what each one does" and get a synthesized answer, without leaving the session. Cross-repo code search: if the engagement spans multiple repos (a common pattern in data platform work — a transformation repo, an ingestion repo, an infra repo), you can search across all of them in a single query. Issue triage: "list all open issues labeled `data-quality` and group them by affected table" is a natural language query that GitHub MCP can answer by calling the API. Writing PRs: "open a draft PR with this diff, assign it to the `data-eng` team, and add a description summarizing the task" is one Claude command.

For the superpowers workflow specifically, GitHub MCP closes the loop in a useful way. The writing-plans skill produces a plan file; the subagent-driven-development skill executes it, one task per commit. **With GitHub MCP active, the orchestrator can also open the PR, tag the reviewer, and set the milestone** — all from within the same Claude session that wrote the code. The plan-to-reviewable-PR cycle can run with minimal human hand-offs.

Auth is straightforward: a GitHub Personal Access Token scoped to the repositories you need, declared once in your `settings.json` under the MCP server block. If the client uses a GitHub organisation with SSO enforcement, you'll need to authorise the PAT for that org — it's two clicks in the GitHub UI and worth doing in advance of a demo or engagement kickoff. For team use, the CLAUDE.md is a good place to document which scope the PAT should have and where to file for access, so every new team member follows the same setup path.

The consultancy angle worth emphasising: GitHub MCP is not a novelty feature. It removes friction from tasks you do every day. The five minutes you spend switching to a browser, navigating to the PR, copying a commit hash, and pasting it back into Claude — that's avoidable. At ten engineers, ten times a day, across a twelve-week engagement, that friction is measurable. MCP is about reclaiming it.

**Transition into next topic:** "From GitHub to Snowflake — the other system that's central to this org right now."

---

## Snowflake MCP

Snowflake MCP is on this slide specifically because of the org-wide Snowflake certification push. Everyone in this room is expected to build fluency with Snowflake, and **this integration makes your existing SQL knowledge dramatically more productive by removing the friction between where you're thinking and where you're working.** Instead of switching to the Snowflake web UI to look up a column name, you ask Claude. Instead of copying a query into a Snowflake worksheet to debug it, you debug it in context.

The two capabilities worth understanding are schema reads and query execution. Schema reads are the higher-frequency use case: "what columns does `PROD.ANALYTICS.CUSTOMER_EVENTS` have, and which ones are nullable?" is a question you'd normally answer by navigating to the web UI, expanding a tree, and reading a table. With Snowflake MCP it's a single query, answered in the session, and the result is available for follow-on reasoning — "now write me a SELECT that aggregates by the date column and filters on non-null customer IDs." That chain of context is what changes the workflow.

Query execution is powerful and deserves a safety note. **Configure your Snowflake MCP connection with a read-only role.** The server will execute whatever SQL Claude generates, and while Claude is conservative about destructive operations, a narrow role is a hard guarantee that a stray `DELETE` or `TRUNCATE` never reaches production. For exploration, debugging, and query-writing assistance — the primary use cases in a consulting context — `SELECT`-only access is all you need. If your client has a dedicated analytics role that's already read-only scoped to the relevant schemas, that's the right credential to use.

The common consulting use cases for Snowflake MCP are schema exploration, query writing assistance, and debugging slow queries. Schema exploration is immediately useful on any new engagement: you can ask "give me an overview of the tables in `PROD.ANALYTICS`" and get a structured summary you can share in a doc or use as context for the rest of the session. Query writing assistance means you can describe the business question in plain language and get SQL back that's grounded in the actual schema, not a made-up one. Slow query debugging: paste the query and the query profile output and ask Claude to diagnose — with the live schema available, it can reason about join cardinalities and filter pushdowns concretely.

In the next demo section, you'll see a safety hook pattern built on top of Snowflake MCP — a `PreToolUse` hook that intercepts SQL before it executes and validates it against a set of guardrails. **That's the "make this safe for prod" pattern we'll plant the seed for here and develop fully in the bonus demo.** The point to carry forward: Snowflake MCP is powerful raw, and with a hook layer it becomes something you can hand to a junior engineer or deploy in an automated pipeline with confidence.

**Transition into next topic:** "Those are the three featured MCP servers. Before we get to the live demo, two quick topics: headless mode and the plugin marketplaces."

---

## Headless Mode + Plugin Marketplaces

Headless mode is how you take Claude Code out of the interactive terminal and put it into automation. **The `-p` flag — `claude -p "<prompt>"` — runs a full Claude Code session non-interactively**: all your MCP servers are active, your skills load, your permissions apply, and the output comes back to stdout. That means you can pipe it into a file, chain it with other shell commands, or call it from a CI step exactly like any other CLI tool.

For data engineers, the immediate use cases are: scheduled Snowflake health checks that run as a cron job and post a summary to Slack, CI pipeline steps that ask Claude to summarize test failures in plain English before the build email goes out, pre-commit hooks that run a quick review of staged SQL before a push, and ad-hoc report generation from Markdown templates. **Think of `claude -p` as the unix-pipe interface for Claude** — the same model, the same capabilities, but composable with the rest of your toolchain in the way a unix filter is composable. Any workflow you'd automate with a bash script is now a candidate for a Claude-augmented version.

Plugin marketplaces are the distribution layer for MCP configurations and skill bundles. There are two to know. The official marketplace at `claude.ai/plugins` is Anthropic-curated and includes first-party servers from major vendors — GitHub, Snowflake, Atlassian, and others. These are reviewed for correctness and security and are the right first stop. The community marketplace at `mcp.so` is broader, community-maintained, and the right place to look for long-tail tools — specific SaaS integrations, domain-specific utilities, experimental servers. **Before installing from the community marketplace, check the trust signals: repo stars, recent activity, maintainer identity, and whether the server has a clear audit trail of what it can access.**

The operational discipline that matters most in a consulting context is version pinning. Declare the exact server version in your `settings.json`, not just the package name. A background update to an MCP server can change tool signatures, add new capabilities, or — rarely but importantly — change the auth behaviour. On an engagement where you're operating inside a client's systems, you want control over when and how your tooling changes. Pin the version; review the `CHANGELOG` before upgrading; treat MCP server upgrades the same way you'd treat a library dependency upgrade in production code.

Plugin install within a session is as simple as running `/plugin install <name>` in an interactive Claude Code session. The plugin manifest handles the wiring — it declares which MCP servers to register, which skills to copy into `.claude/skills/`, and which hooks to add to `settings.json`. **For a consultancy team, the practical pattern is one "engagement-type plugin" per client stack:** bundle the GitHub, Snowflake, and dbt MCP configs together with the team's skills and hooks, publish it internally, and new team members get the full stack with one install command.

**Transition into next topic:** "Now we shift from consuming what exists to authoring what you need. Let's start with skills."

---

## Skills Authoring

The most important thing to understand about skills authoring is how small it is. **A useful skill is ten lines of markdown, not a project.** There is no SDK to import, no compile step, no service to deploy, no CI pipeline to configure. If you can write a markdown file, you can ship a skill that your whole team picks up automatically at their next session start.

A skill lives in `.claude/skills/<skill-name>.md` relative to your repo root, or in `~/.claude/skills/` for personal skills that travel with you across projects. Every skill file has the same structure: a YAML frontmatter block followed by a markdown body. The frontmatter is short:

```markdown
---
name: skill-name
description: When to use this skill
---
# Body
Instructions Claude follows...
```

**The `description` field is what drives auto-invocation.** Claude reads the description of every available skill at session start and uses it to decide when a skill is relevant. Write the description as a trigger condition — "Use this skill when the user asks to run a data quality check on a dbt model" — and Claude will invoke it automatically when the context matches, without the user needing to know the skill name. The body is the full prompt Claude executes when the skill is triggered: plain markdown prose, as detailed as you need, referencing your project's file paths, naming conventions, and the tools Claude should use.

For a consultancy context, skills are how you institutionalise workflow patterns. Write a "run data quality check" skill once, commit it to the repo, and every team member on the engagement has it. When a new analyst joins mid-engagement, they don't need to be briefed on the team's DQ process — they start a Claude Code session and the skill is there. When the process evolves, you update one file and the whole team gets the update at their next session. **The skill encodes current best practice; git history encodes how that practice evolved.** That combination is worth more than a Confluence page.

Best practice on skill authoring: one skill per file, keep the body under 150 lines, and give the file a name that matches the trigger concept — `data-quality-check.md`, `pr-description-generator.md`, `schema-explorer.md`. If a skill body is growing past 150 lines, it's usually a sign that it's doing two things and should be split. Shorter skills are easier to maintain, easier to debug when they behave unexpectedly, and easier for teammates to read and contribute to.

**Transition into next topic:** "Skills handle workflow patterns. Hooks handle lifecycle events — they're how you wire Claude Code into your team's existing operational infrastructure."

---

## Hooks

Hooks are lifecycle callbacks that run at specific Claude Code events. **They are declared in `settings.json` under the `hooks` key — no different in concept from a git hook — and they receive tool call metadata as JSON.** The exit code convention is clean: zero means proceed, non-zero means block. There are four event types, each with a distinct use case profile.

`PreToolUse` fires before a tool call executes. This is the right hook for validation and blocking. **Example use case: before Claude runs any SQL via the Snowflake MCP, a PreToolUse hook validates the query against your client's naming conventions and checks that it's not touching a production table without an explicit flag.** The hook receives the full tool call — including the SQL string — as JSON, runs your validation script, and returns zero to proceed or non-zero to block with an error message. This is the pattern behind the Snowflake safety hook mentioned in the demo section.

`PostToolUse` fires after a tool call completes. This is the right hook for logging, formatting, and side-effects. **Example use case: every file write Claude makes gets logged to an audit trail file** — who wrote what, when, in which session. For a client engagement where you need to demonstrate what changes were made and by what automated process, a PostToolUse hook on the file write tool provides that audit log automatically, without any manual process.

`Stop` fires when Claude finishes a task — when it stops generating and hands control back. **Example use case: when a long subagent-driven execution completes, fire a Slack notification** so the engineer who kicked it off can step away and come back when it's done. On a task that takes fifteen minutes to run, this is the difference between polling and being notified.

`SessionStart` fires when a new Claude Code session opens. **Example use case: pre-load environment variables from a `.env` file, run a quick schema validation to confirm the Snowflake connection is live, or print a sprint-specific reminder** — "this sprint, don't touch the `PROD.STAGING` schema, use `PROD.DEV` instead." SessionStart hooks turn each session open into a light-weight briefing that reflects the current state of the engagement.

**Transition into next topic:** "That covers the two authoring primitives — skills and hooks. The last topic in the authoring section is custom subagents and how to share what you build with the broader community."

---

## Custom Subagents + Plugin Publishing

Custom subagents and plugin publishing are the "you could build more" layer on top of everything you've seen today. They're not required — you can get enormous value from skills, hooks, and MCP servers without touching either — but they're where the pattern scales from personal productivity to team infrastructure to community asset.

**Custom subagents extend the skills model by letting a skill orchestrate multiple isolated Claude sessions.** Instead of Claude doing everything in one context, your orchestrator skill dispatches a set of sub-sessions — each focused on one task, with no context bleed between them. You saw this pattern in Workshop 1 via the superpowers subagent-driven-development skill; the mechanic is a skill body that dispatches to isolated agents and collects their results. The agents live in `.claude/agents/` in your project, as markdown files with their own frontmatter, analogous to skill files. If you have a recurring multi-step workflow that doesn't fit the superpowers pattern exactly — say, a nightly data pipeline review that checks three different systems and produces a consolidated report — you can author a custom orchestrator skill with purpose-built subagents for each system check.

**Plugin publishing is the distribution layer.** Once you've built a collection of skills, hooks, and MCP configs that work well together for a particular engagement type, you bundle them into a `plugin.json` manifest and publish to the community marketplace at `mcp.so/publish`. A published plugin can be scoped to your organisation — visible only to team members — or made public. The install experience for consumers is one command: `/plugin install <name>`, and they get your full skill and hook set, the MCP configs pre-wired, and whatever defaults you've baked in.

The practical opportunity here is an engagement-type plugin. A "GitHub plus Snowflake plus dbt" bundle — the MCP servers configured, the team's skills checked in, the PreToolUse safety hooks for Snowflake included — is something you build once per engagement type and install once per team member. For a consultancy that runs variations of the same data engineering engagement repeatedly, **that bundle is a compounding asset**: it encodes everything the team has learned about working safely and effectively on that stack, and it gets better as the team adds skills and hooks over time.

The callback to Workshop 1 is worth making explicit: subagents were presented there as a capability you consume via the superpowers skill. Here, you're seeing that you can author them. The skills you write become the skills your subagents execute. The hooks you configure apply across the whole session, including subagent sessions. **The full stack — MCP servers, skills, hooks, subagents — is designed to be authored at every layer**, and the authoring surface at each layer is intentionally small. A custom subagent is a markdown file. A plugin manifest is a JSON file. The ceiling is high; the floor is close.

**Transition into next topic:** "That's the full authoring section. Let's close with the mental model that ties consume and author together."
