# Demo 1 — Primitives in Action (8 min)

**Workshop 1, minutes 25–33.**
This is the first of two demos in Workshop 1. It concretises the theory from the CLAUDE.md, context, and plan mode slides by showing all three in a single live session inside the Claude Code VSCode extension.

**No prompts come from `magic-prompts.md` for this demo.** All prompts are written out verbatim below.

**Reference file for `/init` output:** `demo-assets/w1-demo1-claude-md/CLAUDE.md.example`
Keep this file open in a separate VSCode tab before the demo starts. Use it to anchor the narration if `/init` produces unexpected or sparse output.

---

## Pre-demo checklist (run before you go live)

- [ ] VSCode open with workspace folder `demo-w1-primitives` (empty folder, no files)
- [ ] Claude Code VSCode extension installed and authenticated
- [ ] `demo-assets/w1-demo1-claude-md/CLAUDE.md.example` open in a separate tab
- [ ] Terminal panel visible inside VSCode
- [ ] Git initialised in `demo-w1-primitives` (`git init` already run — checkpoints need a git repo)
- [ ] Font size bumped for audience visibility (Cmd/Ctrl+= twice)

---

### Step 1 — Orient the audience to the workspace (≈30 sec)

**What presenter does:** Switch to VSCode. Show the empty Explorer panel (no files). Point to the Claude Code status bar item at the bottom of the window and the chat panel if it is open.

**Exact command/prompt:** *(no command — this is narration only)*

**Expected on screen:** Empty VSCode workspace named `demo-w1-primitives`. The Claude Code status bar icon is visible at the bottom. The Explorer shows no files.

**What presenter says:** "Here's where we start — completely empty workspace, the way you'd begin a new engagement or a new repo. The only thing installed is the Claude Code extension. Watch what happens when I ask Claude to bootstrap the project memory file."

**Fallback if it goes wrong:** If VSCode launched with a previous workspace by mistake, close the folder (File > Close Folder) and reopen the correct empty directory. Takes 15 seconds.

---

### Step 2 — Run `/init` and observe the scaffolded CLAUDE.md (≈75 sec)

**What presenter does:** Open the Claude Code chat panel (click the status bar icon or use the command palette: `Claude Code: Open Chat`). Type the `/init` command and press Enter. Wait for Claude to finish writing the file, then click through to `CLAUDE.md` in the Explorer.

**Exact command/prompt:**
```
/init
```

**Expected on screen:** Claude streams a response describing what it found (or didn't find) in the workspace, then creates `CLAUDE.md` in the root. The Explorer updates to show the new file. The file contains sections for project description, stack, conventions, and notes.

**What presenter says:** "Claude reads whatever is in the workspace — package files, config, source — and writes a starter CLAUDE.md. In an empty repo like this one it generates a minimal template. In a real project with a `pyproject.toml` or `dbt_project.yml` it would pull in your actual stack. Let me show you what a fuller version looks like." *(Switch to the `CLAUDE.md.example` tab for 10 seconds, then switch back.)* "That's the shape we're aiming for."

**Fallback if it goes wrong:** If `/init` errors or produces only a one-liner, say: "Sometimes on a completely empty workspace `/init` gives a skeleton — that's normal. Let me show you the full version." Switch to the `CLAUDE.md.example` tab and narrate the sections directly.

---

### Step 3 — Edit CLAUDE.md to add real conventions (≈60 sec)

**What presenter does:** Open `CLAUDE.md` in the editor. Add two lines under the stack section (or at the end of the file if no stack section exists):

**Exact command/prompt:** Manually type these two lines into the file and save (Ctrl+S / Cmd+S):
```
## Stack
Python 3.12, Streamlit, pandas — no additional data libraries without team sign-off.

## Hard rules
Never edit migration files directly. Create a new migration instead.
```

**Expected on screen:** The two lines appear in the editor. The file is saved (no dot on the tab).

**What presenter says:** "This is where CLAUDE.md earns its keep. Two lines. Now every session in this workspace — mine, a colleague's — starts knowing the stack and the one rule the team always forgets to mention. It takes thirty seconds to write and it never has to be said again."

**Fallback if it goes wrong:** If the file is read-only or the editor doesn't respond, open the file from the terminal with `code CLAUDE.md` or use File > Open File. Save with Ctrl+S.

---

### Step 4 — Switch to plan mode and submit the first prompt (≈45 sec)

**What presenter does:** In the Claude Code chat panel, activate plan mode. The keyboard shortcut is **Shift+Tab** before submitting (the input toggles to show a "Plan" badge or the status bar shows "Plan mode"). Then type the prompt and submit.

**Exact command/prompt:**
```
Add a function in src/utils.py that validates a date range and returns true if start < end.
```

**Expected on screen:** The chat input shows a plan mode indicator (badge, icon, or status bar label reading "Plan"). After submitting, Claude responds with a written plan — a numbered list of steps describing what it will do — rather than immediately writing code.

**What presenter says:** "Plan mode. Shift+Tab to toggle it on. I'm about to ask Claude to create a file we don't have yet. With plan mode on, it has to show me its thinking before it touches anything. Watch the status bar — you'll see the Plan indicator."

**Fallback if it goes wrong:** If the Shift+Tab shortcut doesn't activate plan mode, use the command palette: `Claude Code: Toggle Plan Mode`. If that also fails, say: "The UI shortcut is extension-version-dependent — the concept is the same. I'll proceed without it and we'll narrate what the plan would look like." Then submit the prompt normally and walk through the output as if reviewing a plan.

---

### Step 5 — Read the plan aloud and approve it (≈60 sec)

**What presenter does:** Read Claude's plan response in the chat panel. Point out the key steps (e.g., "create `src/` directory", "create `utils.py`", "add `validate_date_range` function with the specified signature"). Then click Approve (or type `yes` / press Enter depending on the extension version).

**Exact command/prompt:**
```
yes
```
*(or click the Approve button in the chat panel)*

**Expected on screen:** Claude's plan is visible as a numbered list. After approval, Claude executes the plan: `src/utils.py` appears in the Explorer and the file opens in the editor showing the new function.

**What presenter says:** "Here's the plan. It wants to create the `src` directory, add `utils.py`, and write a `validate_date_range` function that takes `start` and `end` and returns `start < end`. That is exactly what I asked for. I can see the full scope before anything is written. I'm approving it." *(Click approve.)* "And there's the file."

**Fallback if it goes wrong:** If Claude executes without showing a plan (plan mode didn't activate), say: "Let me show you what the plan would have contained before execution." Read out the code that was generated and narrate it as if it were a plan. The checkpoint step still works.

---

### Step 6 — Show the checkpoint in the VSCode timeline (≈45 sec)

**What presenter does:** In the Explorer panel, right-click `src/utils.py` and select **Open Timeline** (or click the Timeline icon in the Explorer panel footer). Point to the checkpoint entry that Claude Code created when it wrote the file.

**Exact command/prompt:** *(no command — mouse navigation)*

**Expected on screen:** The Timeline panel shows at least one entry labelled with a Claude Code checkpoint (or a git commit if checkpoints are commit-backed). The entry timestamp matches the moment Claude wrote the file.

**What presenter says:** "See this timeline entry? Every time Claude completes a plan step, it creates a checkpoint here. This is my revert point. If anything that follows looks wrong, I can come straight back to this exact state — one click, no git archaeology."

**Fallback if it goes wrong:** If the Timeline panel shows no entries, switch to the Source Control panel (Ctrl+Shift+G) and show the git log instead (`git log --oneline` in the terminal). Say: "The checkpoint is backed by a git commit — you can see it here. Same concept, different UI."

---

### Step 7 — Make a deliberate change request (≈60 sec)

**What presenter does:** In the Claude Code chat panel (plan mode can be left off for this quick follow-up), type the next prompt and submit.

**Exact command/prompt:**
```
Actually I want it to also handle null inputs — if either start or end is None, return False.
```

**Expected on screen:** Claude edits `src/utils.py` in place. The function now has a null-guard at the top. The editor shows the diff or the updated file.

**What presenter says:** "Now I'm adding a requirement I forgot. Claude updates the function. Watch the file change." *(Pause while Claude writes.)* "There's the null guard. The function is more complete — but now I'm second-guessing myself. Maybe the caller should be responsible for null checking. Let me roll this back."

**Fallback if it goes wrong:** If Claude rewrites the whole file instead of adding a guard, say: "It rewrote more than I expected — this is exactly why we have checkpoints." Proceed to the revert step.

---

### Step 8 — Revert to the checkpoint (≈60 sec)

**What presenter does:** Open the Timeline panel for `src/utils.py` again. Click the checkpoint entry from before the null-handling change. Select **Restore** (or equivalent action in the timeline context menu).

**Exact command/prompt:** *(right-click the earlier checkpoint entry → Restore)*

**Expected on screen:** `src/utils.py` reverts to the version without the null guard. The editor refreshes and shows the earlier, simpler function body.

**What presenter says:** "One click. We're back to the version before the null handling. The file content matches the state right after plan approval — no null guard, clean return. If I'd spent twenty minutes building on top of that change before deciding I didn't want it, this single revert would still work." *(Verify the file in the editor.)* "Confirmed — reverted."

**Fallback if it goes wrong:** If the Timeline restore doesn't work, run in the terminal:
```bash
git checkout HEAD~1 -- src/utils.py
```
Say: "The checkpoint is a git commit under the hood. Here's the git command that does the same thing." Show the file content after the checkout to confirm the revert.

---

### Step 9 — Closing line (≈15 sec)

**What presenter does:** Switch back to the slides or face the audience directly.

**Exact command/prompt:** *(no command)*

**Expected on screen:** VSCode with the reverted `src/utils.py` visible.

**What presenter says:** "This works for small tasks. But for real deployment-ready code, we need more than plan-mode-and-pray. That's where superpowers comes in."

**Fallback if it goes wrong:** N/A — this is a spoken line only.

---

## Risk register

| Failure mode | Likelihood | Fallback |
|---|---|---|
| `/init` produces sparse or unexpected output (empty workspace gives minimal template) | Medium | Keep `demo-assets/w1-demo1-claude-md/CLAUDE.md.example` open in a second tab. Switch to it and say: "In a repo with actual source files, `/init` would produce something like this." Narrate the sections. |
| Plan mode UI not visible (Shift+Tab does nothing, no badge shown) | Medium | Use the command palette (`Claude Code: Toggle Plan Mode`). If that also fails, submit the prompt without plan mode and narrate: "What you'd normally see here is a numbered plan before any file is touched. Let me walk through what Claude produced as if reviewing that plan." |
| Claude executes immediately without showing a plan | Low | See plan mode fallback above. The demo still works — emphasise the checkpoint timeline as the primary safety net. |
| Checkpoint revert doesn't restore the file | Low | Run `git checkout HEAD~1 -- src/utils.py` in the terminal. Say: "Checkpoints are backed by git — here's the underlying command. Same result, one more step." |
| Extension not authenticated / Claude Code chat panel blank | Low | Have a terminal fallback session open (`claude` CLI). Run the same prompts there. The concepts are identical; only the UI differs. |
| `src/utils.py` not created (Claude creates file with wrong path) | Low | Open the correct file from wherever Claude created it. Update the timeline narration to match. The revert step still works on whatever file Claude touched. |
| VSCode workspace loads previous project instead of empty `demo-w1-primitives` | Low | File > Close Folder, then File > Open Folder, select the empty `demo-w1-primitives` directory. Takes ~15 seconds. |
