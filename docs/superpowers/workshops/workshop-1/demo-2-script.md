# Demo 2 — Brainstorm to Deployed App (10 min)

**Workshop 1, slot 48:00–58:00.**
This is the second and highest-stakes demo of Workshop 1. It shows the full superpowers brainstorm workflow live — seed prompt, Q&A exchange, visual companion offer — then pivots to a cooked-turkey reveal of the completed PromptCraft solution to demonstrate what "brainstorm to deployed app" looks like end-to-end.

**The live brainstorm is inherently non-deterministic.** Claude's questions will vary between sessions. The fallbacks in each step are not optional contingencies — rehearse them until they feel as natural as the happy path.

**Engineered prompts for this demo come from `docs/superpowers/workshops/magic-prompts.md`.**
- Seed prompt: `magic-prompts.md §W1 Demo 2 — Brainstorm Seed Prompt`
- Visual companion steering answer: `magic-prompts.md §W1 Demo 2 — Visual Companion Steering Question`

Do NOT improvise these prompts. Deviating from the verbatim text changes which behavior fires.

---

## Setup state (confirm before going live)

Two VSCode windows (or two VSCode tabs in a split-screen layout) must be arranged side by side or as two clearly labelled tabs before the demo begins.

**Window A — live brainstorm workspace**
- Empty workspace folder named `demo-w1-brainstorm` (no files, no git history).
- Claude Code VSCode extension installed and authenticated.
- The Claude Code chat panel is open and ready to accept input.
- Font size bumped for audience visibility (Ctrl+= / Cmd+= twice).

**Window B — solution reveal (this repo on the `solution` branch)**
- Repository: `claude-code-superpowers-intro`, checked out to the `solution` branch.
- The following files are open in editor tabs, in order:
  1. `docs/superpowers/specs/2026-04-10-promptcraft-design.md`
  2. `docs/superpowers/plans/2026-04-10-promptcraft.md`
- A terminal panel is open at the repo root, ready to run:
  ```
  streamlit run promptcraft/app.py
  ```
- The terminal has NOT yet run the command — the app is not running yet.

Window B serves dual purpose: it is the **safety net** (switch to it if Window A derails) and the **reveal source** (the cooked-turkey demonstration). Know the keyboard shortcut to switch between the two windows before going live.

---

## Pre-demo checklist

- [ ] Window A: empty workspace open, Claude Code chat panel visible and authenticated
- [ ] Window B: `solution` branch checked out, both files open in tabs, terminal ready
- [ ] Fallback screenshot of visual companion (three layout options) open in a pinned browser tab or second monitor — captured during rehearsal
- [ ] `streamlit` installed in the `solution` branch environment (`pip install streamlit` confirmed)
- [ ] Presenter knows keyboard shortcut to toggle between Window A and Window B
- [ ] Clock or timer visible to presenter — this demo runs to exactly 10 min

---

### Step 1 — Confirm setup state with the audience (≈30 sec)

**What presenter does:** Show both windows side by side (or name both tabs explicitly). Point out Window A (empty workspace) and Window B (solution branch, files visible in tabs but terminal idle). Do not open either file in Window B yet — just let the audience see the two environments exist.

**Exact command/prompt:** *(no command — narration only)*

**Expected on screen:** Both windows visible. Window A shows an empty Explorer and open Claude Code chat panel. Window B shows editor tabs for the spec and plan files, with an idle terminal below.

**What presenter says:** "Two environments. Window A is blank — this is where we start the live brainstorm right now. Window B is the solution branch of this repo: the spec, the implementation plan, and the app that was built from them. By the end of this demo you will have seen the whole arc — from the first question to the running product."

**Fallback if it goes wrong:** If Window B is not on the correct branch, open the terminal in Window B and run `git checkout solution`. Takes 10 seconds. Narrate it: "Switching to the solution branch — this is the completed version."

---

### Step 2 — Window A: kick off the brainstorm with the seed prompt (≈30 sec)

**What presenter does:** Switch focus to Window A. In the Claude Code chat panel, type the seed prompt verbatim from `magic-prompts.md §W1 Demo 2 — Brainstorm Seed Prompt` and submit.

**Exact command/prompt:** `see magic-prompts.md §W1 Demo 2 — Brainstorm Seed Prompt`

**Expected on screen:** The `superpowers:brainstorming` skill is invoked — the status line shows skill invocation (something like `Using superpowers:brainstorming`). Claude responds with the first 2–3 scoped questions. The response is structured, not a wall of text.

**What presenter says:** "Seed prompt in. Watch the status line — you should see the brainstorming skill fire. Claude is not just answering my question; it's running a structured workflow that explores what we actually need before we commit to anything."

**Fallback if it goes wrong:** If the skill does not auto-invoke (no status line indicator, Claude produces a direct design response), add to the chat: "Use the superpowers:brainstorming skill for this." The skill will invoke on the follow-up. Narrate: "Sometimes the explicit invocation is needed — the auto-trigger is model-version-dependent. The behavior is the same either way."

---

### Step 3 — Answer 2–3 brainstorm questions authentically (≈90 sec)

**What presenter does:** Read Claude's first questions aloud to the audience. Answer them with the prepared responses below. Keep each answer to one sentence — brevity advances the brainstorm faster and prevents the exchange from stalling on a single question. Submit each answer and wait for the next question before answering.

**Exact command/prompt:** Answer each question with one of these prepared responses (paraphrase naturally, do not read verbatim):

- **On user/workflow:** "Data scientists, writing prompts in Jupyter notebooks or a dedicated Streamlit app, not via raw API."
- **On prompt complexity:** "Multi-step and agentic prompts — not single-turn queries. The tool needs to handle chained instructions."
- **On analysis depth:** "Detailed rewrite suggestions, not just lint flags. Show what a better version of the prompt looks like."

**Expected on screen:** Claude continues the Q&A exchange, advancing toward a UI/format question. Each answer narrows the design space.

**What presenter says:** (After submitting each answer, brief commentary.) "Who is the user — data scientists, notebook-first." ... "What kinds of prompts — multi-step, agentic." ... "How much analysis — detailed rewrites, not just warnings. Watch where Claude takes this next."

**Fallback if it goes wrong:** If Claude asks questions outside this cluster (e.g., asks about authentication, deployment target, or team size), answer briefly and redirect: "Let's focus on the core UX first." If Claude skips the UI/format question entirely after three exchanges, proceed directly to Step 4 and manually paste the steering answer — do not wait for the question to appear organically.

---

### Step 4 — At the UI/format question, trigger the visual companion (≈30 sec)

**What presenter does:** When Claude asks a question about UI layout, display format, or how to present the refined prompt to the user — answer with the steering response verbatim from `magic-prompts.md §W1 Demo 2 — Visual Companion Steering Question` and submit.

**Exact command/prompt:** `see magic-prompts.md §W1 Demo 2 — Visual Companion Steering Question`

**Expected on screen:** Claude recognises the explicitly visual ask and either (a) offers to open a browser-based visual companion with rendered mockups, or (b) asks for confirmation before opening the companion. A browser tab may begin to open.

**What presenter says:** "This is the steering moment. The question is visual — layout options. I'm not asking for a text description, I'm asking to actually see the options. Watch what Claude offers next."

**Fallback if it goes wrong:** If Claude has not asked a UI/format question by this point, paste the steering answer anyway after the third question exchange. Say: "I'm steering us toward a visual question deliberately — this is the trigger for the next behavior." If the visual companion offer still does not fire after the steering answer, proceed to Step 5 with the fallback narration.

---

### Step 5 — Accept the visual companion offer (≈15 sec)

**What presenter does:** When Claude offers to open a browser-based visual companion (or asks for confirmation), accept. Type `yes` or click the confirm action. Watch for a browser tab to open.

**Exact command/prompt:**
```
yes
```
*(or click the confirm/open button if present in the UI)*

**Expected on screen:** A browser tab opens showing rendered UI mockups — side-by-side comparison, stacked diff, and tabbed view options for the refined prompt display.

**What presenter says:** "Opening it. The companion is a browser tab, not a chat message."

**Fallback if it goes wrong:** If the visual companion does not open (no browser tab, Claude produces a text description instead), say: "In a longer session here, brainstorming would offer to spin up a browser companion to show these layouts side by side. Let me show you what that looks like with a screenshot." Switch to the fallback screenshot in the pinned browser tab. Continue narration from Step 6 using the screenshot.

---

### Step 6 — Show the rendered mockups (~30 sec)

**What presenter does:** Switch to the browser tab showing the visual companion. Scroll slowly through the three layout mockups (side-by-side, stacked diff, tabbed view). Point to each one with the cursor. Do not rush — let the audience read the mockups.

**Exact command/prompt:** *(no command — narration and cursor movement)*

**Expected on screen:** A rendered browser companion page showing three distinct UI layout options for the refined prompt display, with visual differentiation between them.

**What presenter says:** "Look at what just happened. Brainstorming detected that this question was visual — not another text question — and offered a companion that renders the options in the browser. This is the system working correctly: the right tool for the right question. Side-by-side. Stacked diff. Tabbed view. You can see the trade-offs without imagining them."

**Fallback if it goes wrong:** If the mockups do not render correctly (blank page, JS error), switch to the fallback screenshot immediately. Do not attempt to debug the companion live. Narrate from the screenshot as if it were the live companion.

---

### Pre-empt the audience objection

**Presenter says — verbatim:**
*"Your brainstorm run will land somewhere different from this exact spec — that's the workflow doing its job, not a flaw. The point is the discipline, not the destination."*

Deliver this line while still looking at the browser companion or immediately as you prepare to pivot to Window B. It addresses the objection before it is raised.

---

### Step 7 — Pivot to the cooked-turkey reveal (≈30 sec)

**What presenter does:** Close or minimise the browser companion tab. Turn to face the audience briefly before switching to Window B.

**Exact command/prompt:** *(no command — spoken transition)*

**Expected on screen:** Browser companion is out of focus or closed. The transition to Window B is about to happen.

**What presenter says:** "Now imagine we ran that brainstorm to completion, then writing-plans, then subagent-driven implementation. Here's what falls out."

**Fallback if it goes wrong:** If the audience is asking questions or the brainstorm in Window A went off-track, deliver this line more deliberately and use it to hard-cut to Window B without apologising for cutting the brainstorm short. The pivot is the right call whenever the brainstorm has consumed its time budget.

---

### Step 8 — Window B: open the spec file (≈60 sec)

**What presenter does:** Switch focus to Window B. Click the tab for `docs/superpowers/specs/2026-04-10-promptcraft-design.md`. Scroll slowly from top to bottom — do not rush. Point to key sections: the user description, the core feature list, the UI format decision.

**Exact command/prompt:** *(no command — tab switch and scroll)*

**Expected on screen:** The PromptCraft design spec is visible. It is a structured document — headings, sections, decisions captured in prose.

**What presenter says:** "This is what comes out of brainstorming completed end-to-end. It's the design doc — generated from the workflow, not written from scratch. Notice the structure: audience, use case, core features, UI decisions. Every answer from the brainstorm is now a section header. This is what 'brainstorming as a discipline' produces."

**Fallback if it goes wrong:** If the spec file is not on the `solution` branch (file not found), run `git checkout solution` in the Window B terminal and re-open the file. If the file still does not exist, narrate from the plan file alone: "The spec and plan are sometimes committed together — let me show you the plan, which captures the same structured output in task form."

---

### Step 9 — Open the plan file (≈45 sec)

**What presenter does:** In Window B, click the tab for `docs/superpowers/plans/2026-04-10-promptcraft.md`. Scroll through it. Point to the task list — specific, numbered, bite-sized tasks.

**Exact command/prompt:** *(no command — tab switch and scroll)*

**Expected on screen:** The PromptCraft implementation plan is visible. It contains a numbered list of tasks, each scoped to a single concern, with file paths or component names where relevant.

**What presenter says:** "And this is what writing-plans turns the spec into. Bite-sized tasks. Each one is the right size for a subagent to execute independently. This is not a to-do list someone typed — it was generated from the spec by the writing-plans workflow. You can hand this to subagent-driven development and it will execute them."

**Fallback if it goes wrong:** If the plan file is missing, say: "The plan would look like a numbered breakdown of the spec into implementation tasks — one task per component or feature. In this case we'll go straight to the running app." Proceed to Step 10.

---

### Step 10 — Run the app (≈75 sec)

**What presenter does:** In Window B, click the terminal panel. Run the command to start the Streamlit app. Wait for the app to open in a browser tab (Streamlit auto-opens or provides a localhost URL to click). Switch to the browser. Paste a sample prompt into the app's input and submit it. Let the analysis run for ~20 seconds. Point out the output.

**Exact command/prompt:**
```
streamlit run promptcraft/app.py
```

**Expected on screen:** The terminal shows Streamlit's startup output (`You can now view your Streamlit app in your browser` with a localhost URL). A browser tab opens (or the presenter clicks the URL) showing the PromptCraft app. The app has an input field and an analysis/output area. After pasting a sample prompt (e.g., `Summarise this document.`), the app produces a structured analysis or rewrite suggestion.

**What presenter says:** "Here's the app." *(Wait for browser to open.)* "Input area, analysis output. Let me paste something in." *(Paste a prompt, wait for result.)* "There's the analysis. This is a running Streamlit app — the thing we just brainstormed is live. It took the brainstorm, the spec, the plan, and subagent-driven implementation to get here."

**Fallback if it goes wrong:** If Streamlit fails to start (import error, missing dependency, port conflict), say: "Streamlit has a dependency issue in this environment — let me show you the recorded version." Switch to the fallback screenshot or screen recording captured during rehearsal (keep it accessible in a pinned browser tab). Narrate over the static image: "This is the app running — input field, analysis output, exactly what we designed in the brainstorm."

---

### Step 11 — Closing line (≈15 sec)

**What presenter does:** Face the audience. The app is visible in the browser behind you or to the side.

**Exact command/prompt:** *(no command — spoken line)*

**Expected on screen:** The running PromptCraft app in the browser.

**What presenter says:** "Brainstorm to deployed app, structured the whole way. This is what 'using Claude Code well' looks like for deployment-ready code."

**Fallback if it goes wrong:** N/A — this is a spoken line only. Deliver it regardless of what is on screen.

---

## Risk register

| Failure mode | Likelihood | Action |
|---|---|---|
| Brainstorm does not ask a UI/format question | Medium | After the third Q&A exchange, paste the visual companion steering answer from `magic-prompts.md §W1 Demo 2 — Visual Companion Steering Question` regardless of whether a UI question was asked. Say: "I'm steering us to the visual question now." |
| Visual companion offer does not fire (Claude produces text description instead) | Medium | Use fallback narration verbatim: "In a longer session here, brainstorming would offer to spin up a browser companion to show these layouts side by side. Let me show you what that looks like with a screenshot." Switch to the fallback screenshot captured in rehearsal. Continue from Step 6 narration. |
| Streamlit app fails to start (import error, missing package, port conflict) | Medium | Switch immediately to the fallback screenshot or screen recording. Say: "Streamlit has a dependency issue in this environment — let me show you the recorded version." Do not attempt live debugging. |
| Brainstorm goes deeply off-topic (e.g., Claude pivots to architecture, authentication, or unrelated features) | Low | Answer briefly, then deliver the pivot line from Step 7 immediately: "Now imagine we ran that brainstorm to completion..." Hard-cut to Window B. The off-topic exchange becomes a teaching moment: "Brainstorming sometimes explores unexpected directions — that's when you steer it back with a short answer and keep moving." |
| `solution` branch files not found (spec or plan missing) | Low | Run `git checkout solution` in Window B terminal. If files are still absent, narrate from whatever is available and skip the missing step. The running app is the most important reveal — prioritise getting to Step 10. |
| Audience asks to see more of the brainstorm live instead of the cooked turkey | Low | Acknowledge it positively: "Great instinct — we have a longer workshop session where we run this end-to-end. Today's point is the arc, not every step." Deliver the pivot line and continue. |
| Clock runs over (brainstorm exchange takes too long) | Medium | Cut question answers to one word each. After the third question, trigger the steering answer immediately regardless of Claude's question. Pivot to Window B as soon as the visual companion offer fires (or fallback fires). The cooked-turkey reveal from Step 8 onward takes only ~3 min and must not be cut. |
