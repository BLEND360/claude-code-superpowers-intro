# Workshop 2 — Slide-by-Slide Spec

Each slide section follows the standard convention: timing, layout, body bullets, ~75-second speaker notes, and an optional demo cue. Build the actual PPTX from this spec; deeper presenter prose lives in `presenter-script.md` and live-demo blow-by-blow lives in the `demo-N-script.md` files. Workshop 2 extends the W1 primitives by adding MCP tooling (the "consume" layer) and skills/hooks authoring (the "author" layer).

---

## Slide 1 — Workshop 2: Power Tools + Authoring
**Time:** 0:00-0:30 (30 sec)
**Layout:** Title slide
**Body bullets:**
- Workshop 2: Power Tools + Authoring
- James Irving · [date]
- Prerequisites: Workshop 1 complete, Claude Code + superpowers installed

**Speaker notes (~75 sec):**
Welcome back. Workshop 1 gave you the foundation — CLAUDE.md, context management, plan mode, permissions, and the superpowers skill workflow. Today we go a level deeper on two fronts. The first, larger chunk is about consuming power tools: MCP servers that wire Claude Code directly into the systems you already use at a client engagement. The second chunk is about authoring: writing your own skills and hooks so the extensions you build are as first-class as the ones you install. By the end of the hour you'll have installed at least one MCP server, seen two of them in a live demo, and written a working skill from scratch. Let's start.

---

## Slide 2 — Hook + Recap of W1
**Time:** 0:30-2:00 (90 sec)
**Layout:** Two-column (left: W1 primitives recap; right: bridge to W2)
**Body bullets:**
- W1 covered: CLAUDE.md · Context · Plan Mode · Permissions · Slash Commands · superpowers skills
- The superpowers workflow: Brainstorm → Write Plan → Subagent-Execute → Review → Ship
- W1 payoff: a repeatable, auditable path from feature request to reviewable commit
- W2 shifts the question: *what can Claude reach beyond your local repo?*
- Answer: any system you plug in via MCP — databases, repos, ticket trackers, docs, browsers
- And: anything you author yourself — custom skills and lifecycle hooks

**Speaker notes (~75 sec):**
Quick recap before we extend. Workshop 1 was about control: making Claude Code behave predictably and produce deployment-ready output on a real engagement. You learned the primitives, the superpowers workflow, and why the brainstorm-plan-execute chain matters for consulting delivery. The honest summary of W1 is: you can now direct Claude Code with precision inside your local repository. Today's question is: what about everything else? A data engineer doesn't live in one repo — they live across GitHub, Snowflake, Jira, Confluence, maybe Azure DevOps. What if Claude could read your Snowflake schema, open a GitHub PR, and check a Confluence doc in a single conversation? That's what MCP unlocks. And if a workflow you need doesn't exist yet, today's authoring section shows you how small it is to build it.

---

## Slide 3 — Today's Roadmap
**Time:** 2:00-5:00 (3 min)
**Layout:** Two-column (left: session flow with timing; right: consume/author split diagram)
**Body bullets:**
- ~70% CONSUME: MCP servers — what they are and which ones matter here
- Featured MCPs: Context7 · GitHub · Snowflake
- Headless mode + plugin marketplaces
- MCP buffet: categories × examples for any engagement stack
- ~30% AUTHOR: skills + hooks + custom subagents
- Two live demos: Demo 1 wires Context7; Demo 2 writes a skill
- Framing: install tools that match your client's stack; author when you do it twice

**Speaker notes (~75 sec):**
Here's how the hour is structured. Roughly the first forty minutes is the consume layer: understanding what MCP is, seeing three specific servers that matter for this consultancy — Context7 for docs freshness, GitHub because every engagement touches it, Snowflake because of the org-wide cert push — then a quick look at headless mode and a buffet slide of everything else. The final twenty minutes flips to the author layer: how to write a skill, how to wire lifecycle hooks, and a brief pointer to custom subagents and marketplace publishing. The two demos are spaced across the session — one mid-way through the MCP section, one at the authoring section. The mental model to hold is: consume to get value fast; author when you do the same thing twice and want it to be a first-class skill for the whole team.

---

## Slide 4 — What Is MCP, Why It Matters
**Time:** 5:00-9:00 (4 min)
**Layout:** Image + text (left: reference architecture diagram; right: bullets)
**Body bullets:**
- MCP = Model Context Protocol — open standard for connecting AI models to external tools
- "USB-C of AI tooling" — one protocol, any server, any client
- Architecture: Claude Code (host) ↔ MCP client ↔ MCP server ↔ external system
- Servers expose: tools (actions), resources (data), prompts (templates)
- Install once in `settings.json`; available in every session automatically
- Each server is sandboxed — Claude calls the tool, never touches the system directly
- Hundreds of servers: first-party (Anthropic + vendors) and community-maintained

**Speaker notes (~75 sec):**
MCP is the layer that turns Claude Code from a local coding assistant into something that can operate across your whole engagement stack. The analogy that lands best is USB-C: before USB-C you needed a different cable for every device. Before MCP you needed a different integration — different API, different auth, different context plumbing — for every external tool. MCP standardises that. You declare the server in settings.json once, and from that point forward Claude can call tools on that server exactly the way it calls built-in tools. The architecture is worth understanding briefly: Claude Code is the host, it runs an MCP client, that client connects to one or more MCP servers, and each server wraps some external system — GitHub, Snowflake, whatever. The server exposes three kinds of things: tools (actions Claude can invoke), resources (data Claude can read), and prompt templates. From a security standpoint: Claude never has direct credentials to the external system. The server owns the auth; Claude just calls the tool. That matters when you're explaining this to a client's security team.

---

## Slide 5 — Context7
**Time:** 9:00-13:00 (4 min)
**Layout:** Two-column (left: model-cutoff timeline diagram; right: bullets + install command)
**Body bullets:**
- Problem: Claude's training data has a cutoff — library docs may be stale by months
- Context7 resolves live, version-pinned docs at query time from official sources
- Without it: Claude may suggest deprecated APIs, removed parameters, wrong defaults
- With it: Claude cites the exact page, version string, and date of the doc it used
- Install: `claude mcp add context7 -- npx -y @upstash/context7-mcp`
- In use: prepend `use context7` to any library question and get a cited answer
- High-value on engagements: Snowflake connector, dbt, pandas, PySpark — all move fast

**Speaker notes (~75 sec):**
Context7 solves a problem that anyone who has used Claude for more than a month will have hit: the model has a training cutoff, and popular libraries ship breaking changes regularly. If you ask Claude about a Snowflake Connector method that changed its signature six months ago, you may get a confidently wrong answer. Context7 fixes this by pulling live, version-pinned documentation from official sources at the moment you ask. The citation it returns includes the source URL, the version string, and the retrieval date — which means you can verify it, and more importantly, you can show a client exactly where the recommendation came from. The install is a single command; you're adding it to your project or user MCP config in settings.json. From that point, prefixing any library question with "use context7" triggers the live lookup. For our stack — Snowflake Connector, dbt Core, PySpark, pandas — this is immediately load-bearing. These are libraries that move fast and where a wrong API call costs hours of debugging.

---

## Slide 6 — GitHub MCP
**Time:** 13:00-17:00 (4 min)
**Layout:** Two-column (left: GitHub MCP capability map; right: bullets)
**Body bullets:**
- Featured because every engagement at this consultancy touches GitHub
- Capabilities: create/review PRs, manage issues, search code across repos, read file contents
- Also: branch management, commit history, repo metadata, GitHub Actions status
- In practice: "show me all open PRs touching the ingestion pipeline" — answered in context
- In practice: "open a draft PR with this diff and tag Alice for review" — one command
- Auth: GitHub PAT or GitHub App — configure once in settings.json under the MCP server
- Pair with superpowers writing-plans: plan lands as a PR, subagent commits per task

**Speaker notes (~75 sec):**
GitHub MCP is on this slide because it's the consultancy denominator — I don't know an engagement we're on that doesn't live in GitHub. The MCP server exposes the full GitHub API surface as Claude-callable tools: you can read and write PRs, manage issues, search code across the organisation's repos, check Actions run status, read file contents at a specific ref. The practical payoff is that your whole development workflow can happen in one context. You write code, create the PR, tag the reviewer, and check CI status without leaving the Claude Code session. For the superpowers workflow specifically, the writing-plans skill produces a plan file — that file can land as a PR and the subagent-driven-development execution produces one commit per task, which maps cleanly to a reviewable PR history. Auth is straightforward: a GitHub Personal Access Token scoped to the repos you need, declared once in settings.json. If your client uses a GitHub organisation with SSO, you'll need to authorise the PAT for that org — the GitHub docs for this are two clicks.

---

## Slide 7 — Snowflake MCP
**Time:** 17:00-21:00 (4 min)
**Layout:** Two-column (left: Snowflake MCP capability map; right: bullets + safety note)
**Body bullets:**
- Featured because of the org-wide Snowflake certification push
- Capabilities: read schema metadata, list databases/schemas/tables/columns, run queries
- Schema reads: "what columns does `PROD.ANALYTICS.CUSTOMER_EVENTS` have?" — instant
- Query execution: SELECT queries in conversation; results returned as structured data
- Safety considerations: read-only role recommended; avoid `INSERT`/`UPDATE`/`DELETE` unless intentional
- Auth: Snowflake account URL + user + role — declare in settings.json under the MCP server
- Use case: "does our schema support this transformation?" — answered without leaving Claude

**Speaker notes (~75 sec):**
Snowflake MCP is on this slide because of the org cert push — everyone in this room is expected to be proficient in Snowflake, and this integration makes that proficiency dramatically more productive. The MCP server gives Claude the ability to read your schema metadata and execute queries inside the conversation. The schema read capability alone is high-value: instead of switching to the Snowflake web UI to look up column names, you just ask. Query execution is powerful but deserves a safety note: configure the connection with a read-only role. The MCP server will execute whatever SQL Claude generates, and while Claude is generally careful about destructive operations, a narrow role is a hard guarantee. For exploration and debugging — the primary use case — read-only is all you need. The auth pattern is the same as the GitHub MCP: credentials declared once in settings.json, available in every session. On a client engagement, the Snowflake role should come from the client's access management team and be documented in your CLAUDE.md so every team member connects with the same permissions profile.

---

## Slide 8 — Headless Mode + Plugin Marketplaces
**Time:** 21:00-25:00 (4 min)
**Layout:** Two-column (left: headless CLI diagram; right: marketplace screenshots / bullets)
**Body bullets:**
- Headless mode: `claude -p "<prompt>"` — runs Claude Code non-interactively
- Use cases: CI pipelines, cron jobs, pre-commit hooks, scheduled reports
- Example: `claude -p "run tests and summarise failures" >> build-report.txt`
- Plugin install: `/plugin install <name>` inside an interactive session
- Official marketplace: `claude.ai/plugins` — Anthropic-curated, verified servers
- Community marketplace: `mcp.so` — broad catalog, check trust signals before installing
- Best practice: pin server versions in settings.json; review `CHANGELOG` before upgrading

**Speaker notes (~75 sec):**
Two quick topics before the buffet slide. Headless mode is how you take Claude Code out of the interactive terminal and into automation. The `-p` flag accepts a prompt string and runs the full Claude Code session non-interactively — MCP servers, skills, permissions all active. This means you can wire Claude into your CI pipeline, run it as a cron job to generate daily summaries, or use it as a pre-commit hook to check for obvious issues before a push lands. For data engineers this is immediately useful: scheduled Snowflake health checks, automated PR summaries, pipeline failure narration. On the plugin marketplace side, there are two places to look. The official marketplace at `claude.ai/plugins` is Anthropic-curated and includes first-party servers from major vendors — GitHub, Snowflake, Atlassian, and others. The community marketplace at `mcp.so` is broader and community-maintained. Both are worth bookmarking. The operational discipline: pin the server version in your settings.json so a background update doesn't break your workflow mid-engagement.

---

## Slide 9 — MCP Buffet
**Time:** 25:00-26:00 (1 min)
**Layout:** Full-width table (let it linger as Demo 1 setup happens)
**Body bullets:**

| Need on engagement | Look for MCP |
|---|---|
| Other cloud (Azure / AWS / GCP) | Azure MCP, AWS MCP |
| Other repo (Azure DevOps, GitLab) | Azure DevOps MCP, GitLab MCP |
| Tickets (Jira, Linear, ADO Boards) | Jira MCP, Linear MCP |
| Docs (Confluence, Notion, SharePoint) | Confluence MCP, Notion MCP |
| Chat (Teams, Slack) | Teams MCP, Slack MCP |
| Browser automation | Playwright MCP |
| Other DBs (Postgres, BigQuery, Databricks) | Postgres MCP, BigQuery MCP |

**Speaker notes (~75 sec):**
This slide is the one to screenshot. The MCP you install depends on your client's stack. We're demoing GitHub and Snowflake because they're the consultancy denominators. The pattern transfers. If your next engagement is on Azure DevOps instead of GitHub, the Azure DevOps MCP gives you the same PR and issue capabilities. If the client is on BigQuery instead of Snowflake, the BigQuery MCP gives you the same schema-read and query execution. Jira for tickets, Confluence for docs, Slack or Teams for chat — all covered. Playwright MCP deserves a call-out: it lets Claude drive a real browser, which is useful for testing web UIs and for scraping client-facing portals that don't have an API. Leave this slide up while I set up the demo — it's meant to linger.
**Demo cue:** transition into Demo 1 here

---

## Slide 10 — Demo 1 Transition
**Time:** 26:00-26:30 (30 sec)
**Layout:** Title slide (transition)
**Body bullets:**
- We've installed Context7 in settings.json before this session
- Let's see it intercept a stale-docs question live
- Watch for the citation: source URL, version string, retrieval date

**Speaker notes (~75 sec):**
Let's wire it up and watch it work. I've already added Context7 to settings.json for this demo environment — the install is the command we saw on slide 5, one line. I'm going to ask Claude a question about a Snowflake Connector method and you'll see Context7 pull live documentation, cite the exact version, and give us an answer we can stand behind. Keep an eye on what Claude says it's reading — that's the MCP tool call happening in real time.
**Demo cue:** transition into Demo 1 (see workshop-2/demo-1-script.md)

---

## Slide 11 — [DEMO 1 PLACEHOLDER] Demo 1 — Context7 in PromptCraft
**Time:** 26:30-34:30 (8 min)
**Layout:** Demo block (not a slide presenters click through)

> This is a live demo block, not a presenter slide. The full blow-by-blow is in `docs/superpowers/workshops/workshop-2/demo-1-script.md`. Return to slide deck at the 34:30 mark.

**Body bullets:**
- (No body bullets — presenter is in the terminal)

**Speaker notes (~75 sec):**
Follow the demo-1 script. Key beats: show the Context7 MCP server active in settings.json; ask a Snowflake Connector question without "use context7" first (show the ungrounded answer); repeat with "use context7" prefix (show the cited, version-pinned answer); optionally show a GitHub MCP tool call — list open PRs or read a file at a specific ref. Keep commentary live. If the live retrieval is slow, narrate what's happening — the latency is the MCP round-trip to the live docs source, which is a feature not a bug.

---

## Slide 12 — Authoring Snack Intro
**Time:** 34:30-35:30 (1 min)
**Layout:** Title slide (transition / bridge)
**Body bullets:**
- You've seen what's available in the MCP ecosystem
- Now see how small the authoring surface really is
- Skills: a markdown file + frontmatter
- Hooks: a JSON entry in settings.json
- That's it — no SDK, no compile step, no deployment pipeline

**Speaker notes (~75 sec):**
The MCP consume layer is large — hundreds of servers, growing weekly. The authoring surface for skills and hooks is deliberately tiny. A skill is a markdown file with a YAML frontmatter block. A hook is a JSON entry in settings.json. There's no SDK to import, no compile step, no service to deploy. If you can write a markdown file, you can ship a skill that your whole team picks up automatically. This section is short by design — I want you to leave with the accurate mental model that authoring is not a second speciality on top of Claude Code usage. It's the same tool, one abstraction up.

---

## Slide 13 — Skills Authoring
**Time:** 35:30-39:30 (4 min)
**Layout:** Two-column (left: SKILL.md anatomy with frontmatter callout; right: bullets)
**Body bullets:**
- Location: `.claude/skills/<skill-name>.md` in your repo (or user-global `~/.claude/skills/`)
- Frontmatter fields: `name`, `description`, `triggers` (exact phrases that invoke it)
- Body: the prompt Claude executes when the skill is triggered — plain markdown prose
- Discovery: Claude reads skills at session start from the `.claude/skills/` directory
- Triggering: user types the trigger phrase → Claude loads and runs the skill body
- Best practice: one skill per file; keep the body under 150 lines; version-control it
- Example trigger: `"run data quality check"` → skill body orchestrates DQ assertions

**Speaker notes (~75 sec):**
Skills live in `.claude/skills/` relative to your repo root, or in `~/.claude/skills/` for personal skills that travel with you across projects. Each skill is a markdown file with a YAML frontmatter block at the top. The frontmatter declares the name, a description, and one or more trigger phrases — these are the exact phrases a user types to invoke the skill. The body is the prompt Claude executes: plain markdown, as detailed as you need, referencing your project's conventions and the tools Claude should use. Claude reads the skills directory at session start, so adding a new skill is as simple as dropping a file in the directory — no restart required for the next session. For a consultancy context, this is how you institutionalise workflow patterns. You write a "run data quality check" skill once, check it into the repo, and every team member on the engagement has it available from that point forward. The skill encodes the team's current best practice for running DQ assertions — and when that practice evolves, you update one file.

---

## Slide 14 — Hooks
**Time:** 39:30-42:30 (3 min)
**Layout:** Two-column (left: settings.json hooks snippet; right: event types + use cases)
**Body bullets:**
- Hooks: lifecycle callbacks that run at specific Claude Code events
- Four event types: `PreToolUse` · `PostToolUse` · `Stop` · `SessionStart`
- Wired in `settings.json` under the `hooks` key — project or user scope
- `PreToolUse`: validate or block a tool call before it executes (e.g. lint SQL before running)
- `PostToolUse`: react to a completed tool call (e.g. log every file write to an audit trail)
- `Stop`: run cleanup or notification when Claude finishes a task (e.g. send Slack ping)
- `SessionStart`: pre-load context or run setup commands when a session opens
- Hooks receive tool call metadata as JSON; exit code 0 = proceed, non-zero = block

**Speaker notes (~75 sec):**
Hooks are how you wire Claude Code into your team's operational infrastructure at the lifecycle level. There are four events you can hook into: before a tool call runs, after a tool call completes, when Claude stops, and when a session starts. Each hook is a command or script declared in settings.json — no different from a git hook in concept. The exit code convention is clean: zero means proceed, non-zero means block. For a data engineering team, the PreToolUse hook on the Bash tool is immediately useful: before Claude runs any SQL, validate it against your client's naming conventions or check that it's not touching a production table without a flag. The Stop hook is useful for notifications: when Claude finishes a long subagent execution, fire a Slack message so you can step away and come back when it's done. SessionStart hooks can pre-load environment variables, run a quick schema validation, or print a reminder of the current sprint's guardrails. These are small additions that make Claude Code feel native to your team's existing workflow rather than separate from it.

---

## Slide 15 — Custom Subagents + Plugin Publishing
**Time:** 42:30-45:30 (3 min)
**Layout:** Two-column (left: custom subagent pattern; right: marketplace publishing flow)
**Body bullets:**
- Custom subagents: skills that spin up isolated Claude sessions for focused subtasks
- Pattern: orchestrator skill reads plan → dispatches subagent per task → collects results
- Already covered in W1 via the superpowers subagent-driven-development skill
- To author your own: a skill body that uses the `dispatch_subagent` tool call pattern
- Plugin publishing: bundle skills + hooks + MCP config into a `.claude/plugin.json` manifest
- Publish to community marketplace at `mcp.so/publish` — public or org-scoped
- Use case: publish a "client-stack" plugin per engagement type (e.g. GitHub+Snowflake+dbt bundle)

**Speaker notes (~75 sec):**
Two brief topics to close the authoring section. Custom subagents extend the skills model: instead of Claude doing everything in one context, your skill orchestrates a set of isolated sub-sessions — each focused on one task, no context bleed between them. You saw this pattern in Workshop 1 via the superpowers subagent-driven-development skill; the underlying mechanic is a skill body that dispatches to isolated agents and collects their results. If you have a recurring multi-step workflow that doesn't fit the superpowers pattern exactly, you can author a custom orchestrator skill. Plugin publishing is the distribution layer: once you've built a collection of skills, hooks, and MCP configs that work well together for a particular engagement type, you can bundle them into a plugin manifest and publish to the community marketplace. The practical opportunity here is an engagement-type bundle — a "GitHub plus Snowflake plus dbt" plugin that a new team member can install with one command and immediately have the full consultancy stack wired in.

---

## Slide 16 — Demo 2 Transition
**Time:** 45:30-46:00 (30 sec)
**Layout:** Title slide (transition)
**Body bullets:**
- We're going to write a skill from scratch in under 5 minutes
- Starting from a blank file, ending with a working trigger in the session
- Watch how little boilerplate is involved

**Speaker notes (~75 sec):**
Let's build something. I'm going to open a blank file in `.claude/skills/`, write a frontmatter block and a short skill body, save it, and then trigger it in a live Claude Code session — all in under five minutes. This is the part I want to stick: authoring is not a speciality. It's a ten-minute task you do once when you notice a workflow you're repeating, and after that the skill is there for everyone.
**Demo cue:** transition into Demo 2 (see workshop-2/demo-2-script.md)

---

## Slide 17 — Closing on Consume vs Author
**Time:** 46:00-49:30 (3.5 min)
**Layout:** Two-column (left: consume ladder; right: author ladder)
**Body bullets:**
- Consume to get value fast: install an MCP, gain new capability immediately
- Author when you do it twice: if you've typed the same prompt three times, make it a skill
- The consume/author boundary is fluid — a skill can wrap an MCP tool call
- Team pattern: one person authors; everyone consumes via plugin install
- Engagement pattern: CLAUDE.md captures conventions; skills capture repeated workflows
- The compounding effect: each authored skill raises the team's floor, not just your ceiling
- Action this week: identify one repeated workflow, write a 30-line skill for it

**Speaker notes (~75 sec):**
Here's the mental model to take away. Consuming MCP servers is how you get value fast — install a server, gain a new capability in the next session. No authoring required. Authoring skills and hooks is how you compound that value across the team. The rule of thumb: if you've written the same prompt three times, make it a skill. If you've forgotten a guardrail twice, make it a hook. The two layers reinforce each other: a skill body can call an MCP tool, so you can author a "run Snowflake health check" skill that uses the Snowflake MCP under the hood. The team economics are worth naming explicitly. If one person authors a skill that saves everyone five minutes per day, the leverage is immediate and it compounds with team size. On a ten-person engagement, a five-minute skill saves fifty minutes a day. That's a rounding error in your sprint velocity until you count it up. Your action item for this week: identify one workflow you've repeated more than twice this month and write a thirty-line skill for it. Drop it in the team repo. That's the habit.

---

## Slide 18 — [DEMO 2 PLACEHOLDER] Demo 2 — Custom Skill Authoring
**Time:** 49:30-59:30 (10 min)
**Layout:** Demo block (not a slide presenters click through)

> This is a live demo block, not a presenter slide. The full blow-by-blow is in `docs/superpowers/workshops/workshop-2/demo-2-script.md`. Return to slide deck at the 59:30 mark.

**Body bullets:**
- (No body bullets — presenter is in the terminal)

**Speaker notes (~75 sec):**
Follow the demo-2 script. Key beats: open a blank skill file in `.claude/skills/`; write the frontmatter (name, description, trigger phrase); write a short skill body that does something demonstrable — a code review summary, a DQ check, a PR description generator; save the file; open a new Claude Code session; type the trigger phrase; show the skill executing. Optionally show a hooks entry in settings.json for a PostToolUse notification. Keep commentary live — if the audience asks to change the skill mid-demo, do it; live editing reinforces that the authoring cycle is minutes, not hours.

---

## Slide 19 — Closing + Where to Learn More
**Time:** 59:30-60:00 (30 sec)
**Layout:** Two-column (left: W2 recap; right: resources list)
**Body bullets:**
- W2 recap: MCP protocol · Context7 · GitHub MCP · Snowflake MCP · headless mode · skills · hooks
- The pattern: consume what exists; author what you repeat; publish what the team needs
- Anthropic docs: `docs.anthropic.com/claude-code`
- superpowers repo: `docs/superpowers/` in this repository
- MCP registry: `mcp.so` (community) and `claude.ai/plugins` (official)
- Next: apply to a real engagement task this week; share what you built in the team channel

**Speaker notes (~75 sec):**
That's Workshop 2. You've seen the full consume-to-author spectrum: MCP servers that connect Claude to your engagement stack, headless mode for automation, skills authoring that takes ten minutes, and lifecycle hooks that make Claude Code native to your team's workflow. The resources are all live: the Anthropic docs have the MCP server configuration reference, the superpowers repo has the skills and workshop materials, and the MCP registries are where you browse for new servers as engagements shift. The ask for this week is the same as last time: apply it to something real. Install one MCP server you didn't have before. Write one skill for a workflow you've repeated. Share it with the team — not because it's polished, but because the habit of sharing authored extensions is what raises the team's floor. Questions? Grab me after or drop them in the channel. Thanks, everyone.
