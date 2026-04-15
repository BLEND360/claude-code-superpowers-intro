# Workshop 2 — Demo 2 Script (Custom Skill Authoring)

**Time:** 10 min · Slot 49:30–59:30 of W2
**Reference:** `docs/superpowers/workshops/magic-prompts.md` §6 for the trigger prompt verbatim
**Reference:** `demo-assets/w2-demo2-skill/.claude/skills/review-prompt-quality/SKILL.md` for the skill file content (presenter types it live or copies it during the demo — Task 18 creates this asset file)

---

## Pre-demo setup checklist

- [ ] Same VSCode session as Demo 1 — PromptCraft repo on `workshop-w2-demo` branch
- [ ] Explorer panel visible with `.claude/` directory expanded — `.claude/skills/` is empty or absent
- [ ] `demo-assets/w2-demo2-skill/.claude/skills/review-prompt-quality/SKILL.md` open in a separate editor tab as the source-of-truth to type from
- [ ] `magic-prompts.md` §6 open in a browser tab — both auto-trigger and explicit-invocation prompts ready to paste
- [ ] Font size bumped for audience visibility (Ctrl/Cmd+= twice)
- [ ] Fallback: revert of any live SKILL.md edits prepared (`git checkout` on the asset file or re-paste from the reference tab)

---

### Step 1 — Setup state confirmation (≈30 sec)

**What presenter does:** Switch to VSCode. Show the Explorer panel with the PromptCraft repo open. Expand the `.claude/` directory. Point out that `.claude/skills/` is either absent or empty. Switch briefly to the second editor tab showing the demo-assets reference file (`SKILL.md`) so the audience sees it exists and is the source-of-truth for what gets typed next. Switch back to the main repo.

**Exact command/prompt:** *(no command — narration only)*

**Expected on screen:** VSCode workspace with PromptCraft repo open on `workshop-w2-demo`. Explorer panel shows `.claude/` with no `skills/` subdirectory (or an empty one). The second editor tab showing the reference SKILL.md is visible in the tab bar.

**What presenter says:** "We're picking up in the same session as Demo 1. PromptCraft repo, workshop-w2-demo branch. Notice the `.claude` directory — there's a `settings.json` in there from our Context7 install. There is no `skills` folder yet. That's what we're about to create. I've got the finished skill file open in another tab as a reference — that's what I'll be typing from. Let's build it live."

**Fallback if it goes wrong:** If `.claude/skills/` already has files from a previous run, run `rm -rf .claude/skills/` in the terminal (5 seconds) and confirm the directory is gone. If the repo isn't on the right branch, run `git checkout workshop-w2-demo`.

---

### Step 2 — Show the empty `.claude/skills/` directory (≈30 sec)

**What presenter does:** In the VSCode terminal panel, run `ls .claude/` to show the directory contents. Point out that `skills/` is absent. Narrate the significance of the directory. Then create the directory structure.

**Exact command/prompt:**
```bash
ls .claude/
mkdir -p .claude/skills/review-prompt-quality
```

**Expected on screen:** The first `ls` shows `settings.json` (and possibly other files) but no `skills/` entry. After `mkdir`, the Explorer panel refreshes to show `.claude/skills/review-prompt-quality/` in the tree.

**What presenter says:** "Here's the `.claude` directory right now — `settings.json` from our MCP install, nothing else. This is where Claude looks for project-local skills. Any subdirectory under `.claude/skills/` becomes a skill. The directory name becomes the skill's identifier. I'm creating `review-prompt-quality` — that's the skill we're writing. One folder, one skill."

**Fallback if it goes wrong:** If `mkdir` fails (permissions or already exists), check the path and retry. If the Explorer doesn't refresh, right-click the `.claude` folder and select Refresh. The terminal confirmation is sufficient to continue narrating.

---

### Step 3 — Create the SKILL.md file (≈150 sec)

**What presenter does:** In VSCode, create a new file at `.claude/skills/review-prompt-quality/SKILL.md`. Type or paste the content from the reference tab (`demo-assets/w2-demo2-skill/.claude/skills/review-prompt-quality/SKILL.md`). Read the frontmatter fields aloud as you type them: `name`, `description` (explain this is the trigger signal — the phrase Claude pattern-matches against to decide whether to invoke), then the body (the instructions Claude follows when the skill runs). Keep the file short — approximately 15 lines total.

**Exact command/prompt:** *(see `demo-assets/w2-demo2-skill/.claude/skills/review-prompt-quality/SKILL.md` for verbatim content — do not improvise the frontmatter)*

Skill structure reference for narration:
```
---
name: review-prompt-quality
description: Reviews an LLM prompt and gives structured improvement feedback. Use when asked to review, evaluate, or improve a prompt.
---

When invoked, analyze the given prompt and respond with exactly these four sections:

## What's Working
List the specific elements of the prompt that are effective.

## What's Vague or Missing
List what is ambiguous, underspecified, or absent.

## Suggested Refinements
List targeted, actionable improvements.

## Refined Prompt
Write a complete improved version of the prompt incorporating the suggestions above.
```

**Expected on screen:** A new file `.claude/skills/review-prompt-quality/SKILL.md` open in the editor, contents being typed or pasted. The Explorer panel shows the file in the tree under `.claude/skills/review-prompt-quality/`.

**What presenter says:** "Three parts to this file. The YAML frontmatter at the top — `name` is the identifier, `description` is what Claude reads to decide whether to invoke it. That description text is the trigger signal: if the user's message semantically matches 'reviewing a prompt,' Claude invokes this skill instead of doing its default thing. Then the body — these are the instructions Claude follows once it fires. Four sections: what's working, what's vague, what to fix, and a rewritten version. That's the whole skill. Fifteen lines. Let's save it."

**Fallback if it goes wrong:** If live typing introduces a frontmatter error (missing `---` delimiters, wrong YAML syntax), say: "Let me copy from the reference file to keep the YAML clean." Paste from the demo-assets reference tab. The reference file is the canonical source — always fall back to it rather than debugging YAML live.

---

### Step 4 — Save and start a fresh Claude session (≈30 sec)

**What presenter does:** Save the SKILL.md file (Ctrl/Cmd+S). In the Claude Code chat panel, run `/clear` to start a fresh session. Confirm the session header resets — no conversation history visible.

**Exact command/prompt:**
```
/clear
```

**Expected on screen:** The Claude Code chat panel clears. Session startup output appears. The new session initialises with the current working directory (the PromptCraft repo), which means it will pick up `.claude/skills/review-prompt-quality/SKILL.md` automatically on first invocation.

**What presenter says:** "File saved. Now I'm clearing the session — this forces Claude to re-initialise and pick up the new skill file. In practice, a fresh terminal tab or a new `claude` invocation does the same thing. The key point: no restart of Claude Code itself is required. Just a new session, which takes two seconds."

**Fallback if it goes wrong:** If `/clear` is not available (different Claude Code version or shell context), close the chat panel and reopen it, or run `exit` in the terminal and start a new `claude` session. Any method that starts a new session with the repo as the working directory will work.

---

### Step 5 — Trigger the skill with the magic prompt (≈30 sec)

**What presenter does:** In the fresh Claude Code chat session, paste the trigger prompt from `magic-prompts.md` §6 verbatim and submit. Do not add any prefix — use the auto-trigger path first.

**Exact command/prompt:** *(see `magic-prompts.md` §6 — use verbatim)*
```
Can you review this prompt for me and suggest improvements? "Generate a summary of the document."
```

**Expected on screen:** The chat panel shows the submitted prompt. The status line or processing indicator begins. Watch the status line for the skill invocation signal.

**What presenter says:** "Here's the trigger prompt — a natural-sounding request to review a prompt. I'm not explicitly naming the skill. I want to show that the description in the frontmatter is doing the matching automatically. Watch the status line at the top."

**Fallback if it goes wrong:** If auto-trigger does not fire (status line shows normal processing, no skill invocation visible), switch immediately to the explicit invocation from `magic-prompts.md` §6: `Use the review-prompt-quality skill to review this prompt: "Generate a summary of the document."` Say: "Let me invoke it explicitly — this bypasses the auto-trigger and still shows the full skill output." The explicit form is equally valid as a demonstration.

---

### Step 6 — Watch the status line show the skill being invoked (≈20 sec)

**What presenter does:** While Claude is processing, point to the status line at the top of the Claude Code interface. Call out the skill invocation label when it appears. If it has already appeared and disappeared by the time you narrate it, refer to the terminal output where the invocation is logged.

**Exact command/prompt:** *(no command — observation only)*

**Expected on screen:** The status line displays something like `Using ...review-prompt-quality` while the skill is running. The exact label matches the `name` field in the SKILL.md frontmatter. After the skill completes, the status line returns to idle.

**What presenter says:** "There — `Using ...review-prompt-quality`. Claude saw the request, matched it against the skill description, and invoked the skill instead of doing a generic response. That status line is the signal that the skill fired. If you ever wonder whether your skill triggered, that's where to look. The terminal output also logs it if the UI label is too fast."

**Fallback if it goes wrong:** If the status line label is not visible (it may flash quickly), point to the terminal output where the skill invocation is logged as a tool call. Say: "The status line flashed — here it is in the terminal log. The invocation is the same either way."

---

### Step 7 — Inspect the output (≈60 sec)

**What presenter does:** Wait for Claude's full response. Scroll through the output in the chat panel. Point out each of the four sections: What's Working, What's Vague or Missing, Suggested Refinements, Refined Prompt. Contrast this with what a default Claude response to the same prompt would look like — generic bullet points, no structure, no rewritten version.

**Exact command/prompt:** *(no command — narration only)*

**Expected on screen:** Claude's response is structured into exactly four sections as defined in the SKILL.md body: `## What's Working`, `## What's Vague or Missing`, `## Suggested Refinements`, `## Refined Prompt`. The content is specific to the input prompt ("Generate a summary of the document."). The final section contains a complete rewritten version of the prompt.

**What presenter says:** "Look at the structure of this response. Four sections, always, in the same order, because the skill specifies them. Without this skill, Claude would give you something useful but unstructured — bullet points, maybe a rewrite buried at the end. The skill enforces the output contract. Every time you invoke it, the response has this shape. That's the value: not just better output, but *predictable* output. Your whole team gets the same structure every time."

**Fallback if it goes wrong:** If Claude's output does not follow the four-section structure (frontmatter may have a YAML error, or the skill body was corrupted during typing), open SKILL.md and verify the formatting. Common issue: missing blank line between frontmatter closing `---` and the body. Fix and re-run `/clear` then repeat Step 5.

---

### Step 8 — Edit the skill live (≈60 sec)

**What presenter does:** Switch to the SKILL.md file in the editor. Make a visible, meaningful change to the skill body — for example, modify the `## Refined Prompt` section heading to `## Refined Prompt (keep it under 50 words)` or add a line at the end of the body: `Always end with one sentence explaining why the original prompt was underspecified.` Save the file (Ctrl/Cmd+S). Do not restart the session.

**Exact command/prompt:** *(edit in the SKILL.md file — no terminal command)*

Example edit — change:
```
## Refined Prompt
Write a complete improved version of the prompt incorporating the suggestions above.
```
To:
```
## Refined Prompt
Write a complete improved version of the prompt incorporating the suggestions above. Keep it under 50 words.
```

**Expected on screen:** The SKILL.md file open in the editor with the modified line highlighted. The file is saved (no unsaved indicator in the tab title).

**What presenter says:** "I'm going to edit the skill live. I'm adding a constraint to the refined prompt section — it has to be under 50 words. This is a meaningful change: now every review will produce a tight, constrained rewrite rather than an unconstrained one. I'm saving the file. No Claude restart. Let's see if it picks it up."

**Fallback if it goes wrong:** If the live edit accidentally breaks the YAML frontmatter (wrong indentation, stray character before `---`), revert to the reference file immediately: paste from the demo-assets tab. Say: "Let me go back to the clean version — YAML frontmatter is strict about whitespace." Re-apply only the body change after the frontmatter is clean.

---

### Step 9 — Re-trigger and show the changed behavior (≈60 sec)

**What presenter does:** In the same Claude Code session (no `/clear` needed), paste the same trigger prompt from `magic-prompts.md` §6 and submit. Wait for the response. Point out that the Refined Prompt section now reflects the constraint added in Step 8 — the rewritten prompt is visibly shorter and the constraint language appears.

**Exact command/prompt:** *(same prompt as Step 5 — see `magic-prompts.md` §6)*
```
Can you review this prompt for me and suggest improvements? "Generate a summary of the document."
```

**Expected on screen:** Claude's response again has the four-section structure. The `## Refined Prompt` section now produces a shorter rewrite (under 50 words) because the skill body now contains the word-count constraint. The behavior is observably different from the Step 7 output.

**What presenter says:** "Same prompt. Same session — I didn't restart anything. But the skill body changed, and the output reflects it immediately. The refined prompt is now constrained. That's the edit cycle for skills: write, save, re-trigger. No restart, no deploy step, no compilation. The file is the skill. If you work better with constraints in your prompt reviews, you add one line. If a teammate needs a different output format, they edit the body. The team's workflow lives in a file you can review, version, and ship."

**Fallback if it goes wrong:** If the behavior does not change (output looks identical to Step 7), the skill file may not have been saved correctly — check the editor tab for an unsaved dot. Also confirm the session picked up the edit by running `/clear` once and re-trying. If the edit was a body-only change (no frontmatter touch), a `/clear` is not required but will not hurt.

---

### Step 10 — Closing line (≈30 sec)

**What presenter does:** Switch back to the slides or face the audience directly. No commands.

**Exact command/prompt:** *(no command — spoken line only)*

**Expected on screen:** VSCode with `.claude/skills/review-prompt-quality/SKILL.md` visible in the editor — the live-edited version.

**What presenter says:** "Skills are this small. A YAML frontmatter block — name and description — and a body that's just instructions. If you have a workflow you do twice: a particular style of code review, a way you structure data quality reports, a checklist you run before a PR — write a skill. It's 10 lines, not a project. The same SKILL.md format that superpowers itself uses is available to you, today, in any repo you work in. That's the authoring layer."

**Fallback if it goes wrong:** N/A — this is a spoken closing line. If anything on screen is messy from a previous step, say: "We built that live — you saw the whole cycle. Let me leave the file up."

---

## Risk register

| Failure mode | Likelihood | Fallback |
|---|---|---|
| Skill not auto-invoked (status line shows normal processing, no skill label) | Medium | Use the explicit invocation from `magic-prompts.md` §6: `Use the review-prompt-quality skill to review this prompt: "Generate a summary of the document."` This bypasses the auto-trigger and still demonstrates the skill's structured output. Say: "Let me invoke it explicitly — same output, different entry point." |
| Status line does not show skill name (too fast or UI version difference) | Low | Point to the terminal output where the skill invocation is logged as a tool call. The terminal log persists and is scrollable. Say: "The status line flashed — here it is in the terminal log." |
| Live editing breaks the skill (frontmatter YAML typo, wrong indentation, stray character before `---`) | Medium | Revert to the reference file immediately: paste from `demo-assets/w2-demo2-skill/.claude/skills/review-prompt-quality/SKILL.md` open in the second editor tab. Re-apply only the body change after the frontmatter is confirmed clean. Say: "YAML frontmatter is strict — let me go back to the clean version and re-apply just the body change." |
| `/clear` does not reset session or skill is not picked up after clear | Low | Close the chat panel entirely and reopen, or `exit` the terminal session and run `claude` again. Any new session initialised in the repo directory will pick up the skill. |
| SKILL.md body produces unstructured output (sections missing or reordered) | Low | Inspect the SKILL.md body for missing `##` prefixes or a malformed body delimiter. The body must start after the closing `---` of the frontmatter with a blank line. Check and save, then re-trigger. |
| `mkdir` for the skills directory fails or Explorer doesn't update | Low | Verify path is `.claude/skills/review-prompt-quality` (not `.claude/skill` or a typo). Right-click the `.claude` folder in Explorer and select Refresh. Terminal confirmation is sufficient to continue narrating if the Explorer is slow. |
