# Workshop 2 — 90-min Bonus Demo Script (Snowflake + Safety Hook + Q&A)

**Time:** Slot 60:00–90:00, 30 min total (~15 min demo + ~15 min Q&A)
**Reference:** `docs/superpowers/workshops/magic-prompts.md` §7 for the destructive-query trigger prompt verbatim
**Reference:** `demo-assets/w2-bonus-snowflake-hook/` for the safety hook source files (`settings.json` fragment, `safety_hook.py`, and `README`) — created in Task 19
**Pre-requisite:** A Snowflake sandbox warehouse and credentials. (Open question in the spec — if not available on the day, see the Snowflake unavailable row in the risk register below.)

---

## Setup state (confirm before going live)

- [ ] PromptCraft repo open in VSCode on the `workshop-w2-demo` branch — same session as Demo 2 if possible
- [ ] Snowflake sandbox warehouse credentials available and verified in advance (test a SELECT in rehearsal)
- [ ] `demo-assets/w2-bonus-snowflake-hook/` open in a separate editor tab: `settings.json.fragment`, `safety_hook.py`, and `README` all visible
- [ ] `magic-prompts.md` §7 open in a browser tab — destructive-query trigger prompt ready to paste
- [ ] Terminal panel visible and authenticated to the Snowflake sandbox
- [ ] Font size bumped for audience visibility (Ctrl/Cmd+= twice)
- [ ] Timer visible to presenter — ~15 min demo, ~15 min Q&A

---

## Demo Block (~15 min)

### Step 1 — Setup state confirmation (≈60 sec)

**What presenter does:** Switch to VSCode. Show the Explorer panel with the PromptCraft repo open. Expand the `.claude/` directory — point out `settings.json` from the Context7 install in Demo 1. Switch to the `demo-assets/w2-bonus-snowflake-hook/` tab and show all three files briefly: `settings.json.fragment`, `safety_hook.py`, and the `README`. Switch back to the main repo. Confirm the terminal is open.

**Exact command/prompt:** *(no command — narration only)*

**Expected on screen:** VSCode workspace with PromptCraft repo open on `workshop-w2-demo`. Explorer panel shows `.claude/settings.json` but no `hooks/` subdirectory. The second editor tab showing the demo-assets hook files is visible in the tab bar.

**What presenter says:** "We're in the same session as Demo 2. PromptCraft repo, workshop-w2-demo branch. Over in the other tab I've got the three files we'll be using: a settings fragment, a Python hook script, and a README explaining what the hook does. Right now there are no hooks installed. We're about to add one. But first — let's give Claude access to a Snowflake database."

**Fallback if it goes wrong:** If the repo is on the wrong branch, run `git checkout workshop-w2-demo` (5 seconds). If the demo-assets tab is missing, open `demo-assets/w2-bonus-snowflake-hook/` from the Explorer.

---

### Step 2 — Install Snowflake MCP (≈120 sec)

**What presenter does:** In the Claude Code chat panel, install the Snowflake MCP server. Use the install command for the Snowflake MCP — the exact package name may vary by release; confirm the current name during rehearsal and update the placeholder below. Walk through the authentication flow: account identifier, username, and password/private key as prompted. After install completes, verify the MCP is loaded by checking the status line for the MCP indicator and confirming the Snowflake tool appears in the MCP tool list.

**Exact command/prompt:**
```bash
claude mcp add snowflake-mcp --transport stdio -- npx -y @snowflake-labs/snowflake-mcp
```
*(Confirm this exact invocation during rehearsal — the package name and transport flag may differ in the current release. See the `demo-assets/w2-bonus-snowflake-hook/README` for the rehearsal-verified command.)*

**Expected on screen:** The install runs in the terminal. Claude Code prompts for Snowflake credentials (account, user, password/key). After authentication, the MCP status line confirms the server is connected. Running `/mcp` or the equivalent list command shows `snowflake-mcp` in the active server list.

**What presenter says:** "This is the MCP install flow — same pattern as Context7 in Demo 1, different server. I'm passing in the Snowflake account identifier and credentials. In a team setup these would come from environment variables — not typed live. Watch the status line. Once that confirms connected, Claude has a live read-write channel into Snowflake. That's what makes the next step powerful — and why the step after that matters."

**Fallback if it goes wrong:** If the install fails (network issue, package not found, authentication error), switch to the screenshot from rehearsal that shows the installed and connected state. Say: "The install isn't completing in this environment — let me show you what success looks like from rehearsal and we'll proceed from there." Narrate as if the install succeeded and continue with Step 3 using the pre-recorded demo or screenshots.

---

### Step 3 — Run a SELECT query (≈120 sec)

**What presenter does:** In the Claude Code chat panel, submit a natural-language query that asks Claude to read the schema of a sandbox table and generate an aggregation query. Use the sandbox table name confirmed during rehearsal (replace `<sandbox_table>` with the actual name). Watch Claude use the Snowflake MCP tool to introspect the schema and return a SQL query, then execute it and show the results.

**Exact command/prompt:**
```
Read the schema of <sandbox_table> and write a query that aggregates revenue by month for the last 12 months.
```
*(Replace `<sandbox_table>` with the actual sandbox table name from rehearsal.)*

**Expected on screen:** Claude calls the Snowflake MCP tool to describe the table schema. The schema columns are shown in the chat. Claude writes a SQL query using the correct column names from the schema. The query is executed against the sandbox and results (a small table of month/revenue rows) appear in the chat panel.

**What presenter says:** "Claude read the schema directly from Snowflake — not from a description I gave it, but from the live catalog. It built the query from that. Then it ran it and returned real data. This is what MCP access looks like: Claude is not guessing at your table structure, it is reading it. Now here's the question: if Claude can read and aggregate, can it also write? Yes. And that's where we need to be careful."

**Fallback if it goes wrong:** If the query returns an error (wrong table name, permission issue, or MCP tool call fails), run a simpler fallback query: `SELECT COUNT(*) FROM <sandbox_table>`. If even that fails, switch to a rehearsal screenshot of a successful query. Say: "Let me show you a run from rehearsal — the point is the schema introspection, not the specific data."

---

### Step 4 — Show the safety problem without the hook installed (≈90 sec)

**What presenter does:** Without making any changes to the session or settings, ask Claude to perform an UPDATE on a production-named table. Emphasize to the audience that this is the sandbox. Watch Claude execute the UPDATE — it will succeed because there is no hook installed yet. Show the result.

**Exact command/prompt:**
```
Run an UPDATE on the prod_sales table to set discount=0 for last quarter.
```

**Expected on screen:** Claude calls the Snowflake MCP tool and executes the UPDATE. The chat panel shows the query and a success response (rows affected count). No warning, no confirmation step — it just ran.

**What presenter says:** "This is what we do NOT want. Claude just ran a destructive UPDATE on a table named `prod_sales` — no confirmation, no warning, no pause. This is the sandbox, so no real harm done. But imagine this prompt was accidentally aimed at the production warehouse. Rows changed. No undo. That is the failure mode we're installing a hook to prevent. The MCP gave Claude access. Now we need to put guardrails on that access."

**Fallback if it goes wrong:** If the UPDATE fails (permissions, table does not exist, or the MCP rejects it), say: "The sandbox rejected that one — but the behavior without a hook is that Claude attempts it with no confirmation. In a permissive environment it would succeed. Let me show you the hook, which is what you'd deploy to prevent this regardless of database-level permissions." Proceed to Step 5.

---

### Step 5 — Install the safety hook (≈120 sec)

**What presenter does:** Switch to the demo-assets tab. Open `settings.json.fragment` and read the relevant lines aloud — the `hooks` block with `PreToolUse` and the pattern that matches Snowflake tool calls. Then perform the install: (a) copy the hooks block into `.claude/settings.json` in the PromptCraft repo; (b) create the `.claude/hooks/` directory and copy `safety_hook.py` into it; (c) make the script executable; (d) start a fresh Claude Code session with `/clear` or by restarting the session.

**Exact command/prompt:**
```bash
# Step a — merge hooks block into .claude/settings.json (edit the file in VSCode)

# Step b and c — place the hook script and make it executable
mkdir -p .claude/hooks
cp demo-assets/w2-bonus-snowflake-hook/safety_hook.py .claude/hooks/safety_hook.py
chmod +x .claude/hooks/safety_hook.py
```
Then in the Claude Code chat panel:
```
/clear
```

**Expected on screen:** The `.claude/settings.json` file in the editor now contains a `hooks` block with a `PreToolUse` entry pointing to `safety_hook.py`. The Explorer panel shows `.claude/hooks/safety_hook.py` in the tree. After `/clear`, the session restarts cleanly.

**What presenter says:** "Three things. First, I'm adding the hooks configuration to `settings.json` — this tells Claude Code to run `safety_hook.py` before any tool call that matches the pattern we specify. Second, I'm placing the hook script at `.claude/hooks/safety_hook.py` and making it executable. The script is the logic — it reads the tool call from stdin, checks whether the SQL matches a destructive pattern on a prod-named table, and exits with a non-zero code if so. Third, `/clear` to restart the session and pick up the new hook. Hooks are just executables — they could be Python, Bash, Node. The contract is stdin/stdout JSON and an exit code."

**Fallback if it goes wrong:** If `chmod +x` is not available (Windows without WSL), use `python safety_hook.py` as the executable path in `settings.json` rather than relying on the executable bit. If the `settings.json` merge produces a JSON syntax error, switch to the reference fragment in the demo-assets tab and paste only that block. Say: "JSON syntax is strict — let me copy the exact fragment from the reference file." See also the risk register for hook-fails-to-load fallback.

---

### Step 6 — Trigger the hook with the destructive prompt (≈30 sec)

**What presenter does:** In the fresh Claude Code session, paste the destructive-query trigger prompt from `magic-prompts.md` §7 verbatim and submit. Do not add any prefix or context. Use the exact text.

**Exact command/prompt:** *(see `magic-prompts.md` §7 — use verbatim)*
```
Run an UPDATE on the prod_sales table to set discount=0 for last quarter.
```

**Expected on screen:** The prompt is submitted. Claude begins preparing the Snowflake tool call. The hook fires before the tool executes — the status line or terminal output shows the hook being invoked (`PreToolUse: safety_hook.py`).

**What presenter says:** "Same prompt as before. Watch what happens differently this time."

**Fallback if it goes wrong:** If the hook does not visibly fire in the status line, check the terminal output for the hook invocation log. If neither is visible, check whether the session restart in Step 5 completed — run `/clear` again and re-submit the prompt.

---

### Step 7 — Show the intercept (≈90 sec)

**What presenter does:** Wait for the hook output to appear. Do not type anything. Point out the hook's output message in the chat panel or terminal: it should explain what was intercepted (destructive SQL pattern matched on a prod-named table), what was blocked (the tool call was not executed), and how to override (re-issue the prompt with `-- CONFIRM_DESTRUCTIVE` in the SQL comment). Emphasize that Claude has not executed the query.

**Exact command/prompt:** *(no command — observation and narration)*

**Expected on screen:** Claude's response shows the hook's output: a message explaining that the query was intercepted because it matched a destructive pattern (`UPDATE`) on a production-named table (`prod_sales`). The tool call was blocked — no rows were changed. The hook output includes the override instruction: add `-- CONFIRM_DESTRUCTIVE` to the query to proceed.

**What presenter says:** "The hook fired. Claude tried to call the Snowflake tool, the PreToolUse hook ran first, and the hook said: 'This looks like a destructive operation on a prod-named table — I'm not letting this through without explicit confirmation.' No rows changed. The override path is auditable — you have to explicitly add `-- CONFIRM_DESTRUCTIVE` to the query. You can log that marker. You can audit who added it, when, and for which query. That is what deployment-grade access control looks like for an AI that has write access to your data."

**Fallback if it goes wrong:** If the hook fires but the output message is missing or truncated (the hook exited with the right code but wrote nothing to stdout), check `safety_hook.py` for the print statement that writes the explanation message. If the hook did not fire at all and Claude executed the query, the `settings.json` merge may have a syntax error — open the file live and check the hooks block. Say: "The hook didn't load — let me check the settings file. This is what hook misconfiguration looks like; it is usually a JSON syntax error."

---

### Step 8 — Override and execute (≈60 sec)

**What presenter does:** Re-issue the prompt with the `-- CONFIRM_DESTRUCTIVE` marker added. Watch the hook allow the call through and Claude execute the UPDATE in the sandbox. Show the result.

**Exact command/prompt:**
```
Run an UPDATE on the prod_sales table to set discount=0 for last quarter. -- CONFIRM_DESTRUCTIVE
```

**Expected on screen:** Claude submits the Snowflake tool call. This time the hook sees the `-- CONFIRM_DESTRUCTIVE` marker and exits with code 0 (allowing the call). The UPDATE executes in the sandbox. The chat panel shows the success response (rows affected). The terminal may show the hook log entry noting that override was granted.

**What presenter says:** "Now I've added the confirmation marker. The hook sees it, validates it, and steps aside. The UPDATE runs. In a real deployment you would log that marker — you would know that a human consciously said 'I understand this is destructive and I confirm it.' That's the audit trail. Compare this to the run in Step 4: no confirmation, no log, just execution. The hook adds one explicit decision point. That's all it takes."

**Fallback if it goes wrong:** If the override does not work (hook still blocks even with the marker), check that the marker string in `safety_hook.py` matches exactly what was typed — the check is case-sensitive. If the sandbox is unavailable, narrate the expected behavior: "In a live sandbox, the hook would see the marker, exit 0, and the UPDATE would run. We're showing the intercept behavior — the override is symmetric."

---

### Step 9 — Closing line (≈30 sec)

**What presenter does:** Face the audience. Stop any running process. No commands needed.

**Exact command/prompt:** *(no command — spoken line only)*

**Expected on screen:** The chat panel showing the successful override run. The `.claude/hooks/safety_hook.py` file visible in the Explorer panel.

**What presenter says:** "MCPs give Claude access. Hooks let you put guardrails on that access. Together: deployment-ready."

**Fallback if it goes wrong:** N/A — this is a spoken closing line. Deliver it regardless of what is on screen.

---

## Q&A topics to be ready for

Allow ~15 minutes for questions. Speak to each topic fluently — do not read verbatim.

---

**"What if the hook misfires on a legitimate query?"**

False positives are a real cost: the developer has to add the `-- CONFIRM_DESTRUCTIVE` marker even for intentional updates, which adds friction. The trade-off is explicit: a small false-positive cost on legitimate writes versus the catastrophic cost of an unconfirmed destructive write on production data. The regex pattern in the hook is tunable — you can narrow it to match only specific table-name prefixes (like `prod_` or `live_`) and exclude tables you know are safe. The override mechanism is intentionally explicit and produces an auditable marker in every query where confirmation was given. If false positives are too frequent for a specific workflow, the pattern in `safety_hook.py` is one line to change.

---

**"Can hooks call external systems?"**

Yes — a hook is any executable, and it runs with full network access. You can write a hook that posts a Slack message when a destructive query is attempted, that logs to Splunk before allowing execution, or that hits a Slack approval-flow webhook and blocks until a human approves the action. A simple example: replace the `print` in `safety_hook.py` with a `requests.post` to a Slack incoming webhook, then log the query text, the table name, and the timestamp. The hook still blocks or allows based on the same exit-code contract — the external call is just a side effect.

---

**"Can I write a hook in Python / JS / Bash?"**

Yes — any executable works. The contract is: read the tool call as JSON from stdin, write a response message to stdout, and exit with code 0 to allow or non-zero to block. The hook in this demo is Python, but the same logic works in Bash (`jq` to parse the JSON), Node.js, or any other language available on the machine. The only requirement is that the file is executable and on the path specified in `settings.json`.

---

**"What's the performance impact?"**

Hooks add roughly 50–200 milliseconds per intercepted tool call, depending on the hook's logic and startup time. For human-paced work — a developer issuing queries interactively — this is imperceptible. It may matter for high-volume CI pipelines where Claude is executing dozens of tool calls in rapid succession, though even there the overhead is usually dominated by the tool call itself, not the hook. If performance is a concern, keep hook logic lightweight: no heavy imports, no network calls on the allow path, fast exit for non-matching patterns.

---

**"Audience-driven: 'What MCP would help your daily work?'"**

Take a few suggestions from the audience. If someone names an MCP that is installable in under two minutes (a local SQLite MCP, the filesystem MCP, a simple REST API MCP), offer to install it live and run a quick query. This is a high-value moment: demonstrating that MCP installation is a two-minute operation, not a project. Have a fallback ready — if installation takes too long or fails, say: "Let's take that offline — I'll send you the install command after the session and we can compare notes on how it went."

---

**"What about hook security — can a malicious hook do bad things?"**

Yes — hooks run with full user permissions, and a malicious hook script could do anything the user can do: exfiltrate data, modify files, make network calls. Treat hook scripts exactly like any other code in your repository: read them before running them, version-control them so changes are visible in diffs, review them in pull requests, and do not blindly run third-party hooks you have not inspected. The security model is the same as any other shell script you add to your project. The `demo-assets/w2-bonus-snowflake-hook/README` documents what `safety_hook.py` does — use that as the template for how to document your own hooks.

---

## Risk register

| Failure mode | Action |
|---|---|
| Snowflake sandbox unavailable on the day | Switch to a local SQLite database with a fake "snowflake" MCP shim, or run pure narration with screenshots from rehearsal. The hook behavior (intercept and override) can be demonstrated against any MCP tool — the Snowflake branding is illustrative, not essential. Say: "We don't have the Snowflake sandbox today — I'll walk you through what this looks like using screenshots from rehearsal. The hook mechanics are identical regardless of the database." |
| Hook script fails to load (file not executable, JSON syntax error in settings.json, missing python in PATH) | Debug live as a teaching moment. Say: "This is what hook misconfiguration looks like — let me show you the three most common causes." Check in order: (1) `ls -la .claude/hooks/safety_hook.py` — confirm the executable bit is set; (2) open `.claude/settings.json` and check the hooks block for JSON syntax errors (missing comma, wrong key name); (3) run `which python` or `which python3` to confirm Python is on the PATH and update the shebang or the settings reference accordingly. The live debug is more instructive than a clean run. |
| Live MCP install fails (network issue, package not found, authentication error) | Switch to a screenshot or recording from rehearsal. Say: "The install isn't completing here — let me show you what success looks like from rehearsal and we'll proceed from the installed state." Continue the demo from Step 3 using a pre-authenticated session or screenshots. |
| Audience asks a question with no good answer | Say so directly: "That's a good question and I don't have a confident answer right now. Let me take that offline and follow up." Capture the question visibly — write it down or paste it into a note. Do not speculate. |
| Override marker check is case-sensitive and the live demo adds the wrong casing | Open `safety_hook.py` in the editor and point to the exact string being checked. Re-issue the prompt with the correct casing. Say: "The check is case-sensitive — here's the exact string the hook is looking for." This is a quick fix and a good teaching moment about hook implementation hygiene. |
