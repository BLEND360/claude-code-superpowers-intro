# Workshop 2 — Demo 1 Script (Context7 in PromptCraft)

**Time:** 8 min · Slot 26:30–34:30 of W2
**Reference:** `docs/superpowers/workshops/magic-prompts.md` §5 for all contrast prompts verbatim

---

## Pre-demo setup checklist

- [ ] VSCode open on the `workshop-w2-demo` branch (or `solution`) of the PromptCraft repo
- [ ] PromptCraft codebase visible in the Explorer panel — `promptcraft/app.py` accessible
- [ ] Anthropic API key configured (`ANTHROPIC_API_KEY` in environment)
- [ ] Terminal panel visible inside VSCode (used for install and streamlit run)
- [ ] Font size bumped for audience visibility (Ctrl/Cmd+= twice)
- [ ] `magic-prompts.md` §5 backup queries open in a browser tab, ready to copy
- [ ] Fallback screenshot/recording of successful Context7 install prepared in rehearsal

---

### Step 1 — Setup state confirmation (≈30 sec)

**What presenter does:** Switch to VSCode. Show the Explorer panel with the PromptCraft repo open. Point out the branch indicator in the status bar (`workshop-w2-demo`). Show `promptcraft/app.py` in the Explorer. Show the terminal panel at the bottom — Streamlit is ready to run.

**Exact command/prompt:** *(no command — narration only)*

**Expected on screen:** VSCode workspace with PromptCraft repo open. Branch reads `workshop-w2-demo` (or `solution`) in the status bar. `promptcraft/app.py` is visible in the Explorer. Terminal panel is visible and idle.

**What presenter says:** "Here's the PromptCraft repo — a Streamlit app for evaluating and refining LLM prompts. This is the kind of codebase a data science team would actually build. We're on the workshop-w2-demo branch. I have the terminal ready at the bottom. In a moment I'm going to ask Claude a question about Streamlit's current API — first without Context7, then with it. Watch what changes."

**Fallback if it goes wrong:** If VSCode opened on the wrong branch, run `git checkout workshop-w2-demo` in the terminal (15 seconds). If the branch doesn't exist, checkout `solution` or `main` — the demo works on any branch that has `promptcraft/app.py`.

---

### Step 2 — Vanilla query (pre-Context7) (≈90 sec)

**What presenter does:** Open the Claude Code chat panel. Paste the vanilla prompt from `magic-prompts.md` §5 verbatim and submit. Wait for Claude to respond. Read the response aloud to the audience and point out what is stale or generic — likely an older workaround, a missing parameter, or a version-agnostic hedge.

**Exact command/prompt:**
```
What's the recommended way to display Streamlit dataframes with row selection in the latest Streamlit?
```
*(See `magic-prompts.md` §5 — Vanilla prompt)*

**Expected on screen:** Claude produces a response without version citations. The response may mention `AgGrid` as a workaround, reference `st.dataframe` without the native selection parameter introduced in a recent release, or hedge with "as of my knowledge cutoff." There is no source URL and no version pin.

**What presenter says:** "Notice what Claude says here — it's working from its training data, which has a cutoff. It may suggest a workaround that was current months ago, or it may not mention the native row-selection parameter that Streamlit added recently. No citation, no version string, no way to verify. This is the stale-docs problem. Now let's install Context7 and run the same query."

**Fallback if it goes wrong:** If the vanilla query happens to produce a fully current and accurate answer (the model's training data sometimes catches recent releases), say: "Claude got lucky here — the training data caught this one. But watch what changes when Context7 adds explicit citations and version pinning. That's the auditability story." Switch to one of the backup queries from `magic-prompts.md` §5: `What's the current syntax for st.dialog in Streamlit, and when was it introduced?`

---

### Step 3 — Install Context7 MCP (≈90 sec)

**What presenter does:** In the terminal panel, run the Context7 install command. If the MCP install requires a settings.json edit, show that too. Restart the Claude Code session if prompted. Verify that Context7 appears in the active MCP server list (status line or session info shows `context7`).

**Exact command/prompt:**
```
<context7-install-command>
```
*(Presenter fills in the exact command during rehearsal. Reference: `docs/superpowers/workshops/workshop-2/slides.md` Slide 5 shows `claude mcp add context7 -- npx -y @upstash/context7-mcp`. Confirm in rehearsal that this is current.)*

After running the install:
- If a session restart is required, restart the Claude Code chat session from the command palette: `Claude Code: Restart Session`
- Verify the MCP is loaded: the status bar or session startup message should list `context7` among active MCP servers

**Expected on screen:** The terminal shows a successful install (no error output). After session restart, the Claude Code status or startup output confirms Context7 is active. The MCP list in settings.json (`.claude/settings.json` or the user-level equivalent) now includes the Context7 server entry.

**What presenter says:** "One command. That's the full install. Context7 is now wired into this Claude Code session — every query goes through its live documentation retrieval layer. I'll restart the session to confirm it loaded." *(Restart if needed.)* "You can see `context7` in the active MCP servers. From this point forward, any library question I prefix with 'use context7' will pull live, version-pinned docs from the official source before Claude answers."

**Fallback if it goes wrong:** If the install command fails (missing Node, network error, API key prompt), say: "Let me show you what this looks like when it's working — I ran through this in rehearsal." Switch to the prepared fallback screenshot or recording. Narrate: "The install adds a server entry to settings.json and the next session startup picks it up automatically. Here's what the working version looks like." Continue the demo from the screenshot, then return to live demo at Step 5 (real edit) if the environment recovers.

---

### Step 4 — Re-run the same query with Context7 enabled (≈75 sec)

**What presenter does:** In the Claude Code chat panel, paste the identical prompt from Step 2 — but this time prepend `use context7`. Submit and wait for Claude's response. Point out the differences: source URL, version string, retrieval date, and the accurate API signature.

**Exact command/prompt:**
```
use context7 — What's the recommended way to display Streamlit dataframes with row selection in the latest Streamlit?
```
*(See `magic-prompts.md` §5 — Same prompt with Context7 enabled)*

**Expected on screen:** Claude's response cites live Streamlit documentation: a source URL pointing to the official Streamlit docs, a version string (e.g., `1.35.0` or current), the native `st.dataframe` row-selection parameter with its correct signature, and a retrieval date. The answer is substantively different from the vanilla response in Step 2.

**What presenter says:** "Same question. Different answer. Look at what's in the response now — the source URL, the version string, the actual current API. This answer is verifiable. If a client asks 'how do you know that's current?' you have a URL and a version to point to. Context7 didn't change Claude's reasoning — it changed the facts Claude was reasoning over. Now let's use that to make a real edit."

**Fallback if it goes wrong:** If Context7 fires but the response looks similar to the vanilla answer, switch to a backup query from `magic-prompts.md` §5 to make the contrast sharper. If Context7 does not appear to be active (no citation, no tool call visible in verbose mode), confirm the session was restarted after install and check `.claude/settings.json` for the server entry.

---

### Step 5 — Make a real edit using Context7-fetched info (≈90 sec)

**What presenter does:** Ask Claude to use the Context7-fetched documentation to improve a specific piece of `promptcraft/app.py`. Target a Streamlit API call in the file that uses an older pattern — for example, a dataframe display without row selection, a deprecated `st.experimental_*` method, or an older layout API. Watch Claude make the edit in the editor.

**Exact command/prompt:**
```
use context7 — Look at the dataframe display in promptcraft/app.py. Update it to use the current Streamlit row-selection API you just retrieved. Only change the dataframe display call; leave everything else as-is.
```

**Expected on screen:** Claude reads `promptcraft/app.py`, identifies the relevant `st.dataframe` call, and makes the targeted edit using the API signature it retrieved in Step 4. The editor shows the diff or the updated file. The change is narrow — only the dataframe display call is touched.

**What presenter says:** "Now I'm asking Claude to apply what it just retrieved to a real file. Watch the edit — it should only touch the dataframe call, nothing else." *(Pause while Claude writes.)* "There it is. Claude used the live-fetched API signature, not its training data. The edit is scoped exactly to what I asked. That's the full loop: fresh docs in, real change out."

**Fallback if it goes wrong:** If Claude refuses to make the edit or makes it too broadly, say: "Let me narrow the prompt." Re-submit with a more specific instruction: `Update only line <N> in promptcraft/app.py — replace the st.dataframe call with the selection_mode parameter from the docs you just retrieved.` If `app.py` does not have a relevant API call to update, switch to: `Add a new dataframe display section to promptcraft/app.py that demonstrates the row-selection API from the docs you just retrieved.`

---

### Step 6 — Test the change (≈45 sec)

**What presenter does:** In the terminal panel, run `streamlit run promptcraft/app.py`. If the app launches without error, point to the browser window briefly. If time is tight or Streamlit fails, show the diff instead (`git diff` in the terminal).

**Exact command/prompt:**
```bash
streamlit run promptcraft/app.py
```
*(If time is short or Streamlit is unavailable, use instead:)*
```bash
git diff promptcraft/app.py
```

**Expected on screen:** Either the Streamlit app opens in a browser tab showing the updated dataframe display — or the `git diff` output in the terminal shows the targeted change: the old `st.dataframe` call on one side, the updated call with the row-selection parameter on the other.

**What presenter says:** *(If Streamlit runs)* "App launches clean. The row-selection feature is there — it wasn't before. One Context7 query, one edit, one working feature." *(If showing diff instead)* "Here's the diff — old call on the left, new call on the right. The row-selection parameter wasn't in the original file. Context7 gave us the right API, Claude applied it, and the change is exactly what we asked for. Clean."

**Fallback if it goes wrong:** If Streamlit fails to launch (import error, port conflict, environment issue), say: "Rather than debug the environment live, let me show the diff — that's the artifact that matters." Switch to `git diff`. If `git diff` shows no change (the file wasn't modified), verify the edit was saved: check the tab in the editor for an unsaved dot, then show the file content directly.

---

### Step 7 — Closing line (≈30 sec)

**What presenter does:** Switch back to the slides or face the audience directly. No commands.

**Exact command/prompt:** *(no command — spoken line only)*

**Expected on screen:** VSCode with the updated `promptcraft/app.py` visible, or the Streamlit app in the browser.

**What presenter says:** "This single MCP eliminates the number one reason model output goes stale. Same pattern works for any library — pandas, scikit-learn, dbt, anything. You're not trusting the model's training data; you're grounding it in the live docs every time. That's what we mean by consuming power tools — one install, every session, for every library you touch."

**Fallback if it goes wrong:** N/A — this is a spoken line only. If anything on screen is messy, say: "Let me leave that up and we'll carry the principle forward."

---

## Risk register

| Failure mode | Likelihood | Fallback |
|---|---|---|
| Context7 install fails (missing Node.js, network error, MCP config error) | Medium | Use a screenshot or recording from rehearsal. Narrate: "I ran this before the session — here's what the working install and first query looks like." Continue from Step 5 (real edit) if the live environment recovers. |
| Context7 install prompts for an API key not pre-configured | Low | Pre-configure the Upstash API key in the environment before the session. If it fires live, say: "Context7 may require an Upstash account in some configurations — I've pre-configured mine. The install experience you'll see at your desk is one extra step." Switch to fallback recording. |
| Vanilla query happens to give a current, accurate answer | Low | Switch to a backup query from `magic-prompts.md` §5: `What's the current syntax for st.dialog in Streamlit, and when was it introduced?` or `How do I use Streamlit's native fragment rerun feature introduced in 1.33?` Have these in a browser tab, ready to paste. |
| Claude refuses to make the edit or over-scopes the change | Low | Narrow the prompt: add a specific line number or a shorter scope. Alternatively, pick a smaller change — e.g., updating a single parameter name rather than a full API migration. |
| Streamlit fails to launch (port conflict, import error, missing dependency) | Low | Show `git diff promptcraft/app.py` instead. The diff is equally compelling as evidence that the edit happened correctly. Pre-run `streamlit run promptcraft/app.py` in rehearsal to confirm the environment is clean. |
| Claude Code session fails to show Context7 as active after install | Low | Check `.claude/settings.json` for the server entry. If missing, manually add the server block and restart the session. Show the settings.json edit as part of the narration: "Here's what the config looks like under the hood." |
