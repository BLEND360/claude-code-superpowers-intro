# Workshop 1 — 90-min Bonus Demo Script (Curveball + Q&A)

**Slot: 60:00–90:00, 30 min total.**
Two sub-blocks: the curveball demo (~15–20 min, Steps 1–8) and Q&A (~10–15 min).

The curveball demo illustrates what happens when a contradicting requirement arrives mid-implementation. The goal is to show that structured superpowers workflows — brainstorming, writing-plans, subagent-driven development — handle a spec change gracefully by returning to the design layer rather than patching the existing code.

**Engineered prompt for this demo comes from `docs/superpowers/workshops/magic-prompts.md`.**
- Curveball injection prompt: `magic-prompts.md §W1 90-Min Bonus — Curveball Injection Prompt`

Do NOT improvise the curveball prompt. The explicit contradiction signal is load-bearing — deviating from the verbatim text changes which behavior fires.

---

## Setup state (confirm before going live)

Continue from Demo 2's `demo-w1-brainstorm` workspace if possible. This avoids a context-switch overhead and lets the audience see a continuous thread from brainstorm to mid-implementation to curveball recovery. A fresh repo is acceptable if the Demo 2 workspace is unavailable.

The workspace must be in the following state when this block begins:

- **Brainstorm completed.** If continuing from Demo 2, use the PromptCraft design that emerged from that session. If starting fresh, use a pre-rehearsed PromptCraft brainstorm output (spec already written and visible in the workspace).
- **writing-plans run.** The plan file exists and is committed to the repo. The plan should show at least 3 tasks, with task 1 marked complete and task 2 marked in-progress.
- **Subagent-driven development started.** At least one task has been executed by a subagent; there is a partial commit history (`git log --oneline` shows at least 2 commits beyond the plan commit).
- **Status line shows a subagent dispatched.** The Claude Code status line should read something like `Dispatching subagent for task 2` or similar. If the status line is not showing this, narrate from the terminal output instead (see Risk register).

### Pre-demo checklist

- [ ] `demo-w1-brainstorm` workspace open with Claude Code chat panel visible and authenticated
- [ ] Plan file exists in `docs/superpowers/plans/` (or equivalent path) and is committed
- [ ] `git log --oneline` shows at least 2 commits beyond the initial brainstorm/plan commit
- [ ] At least one source file created by a subagent is visible in the Explorer
- [ ] Font size bumped for audience visibility (Cmd/Ctrl+= twice)
- [ ] Curveball prompt text from `magic-prompts.md §W1 90-Min Bonus` is in the presenter's clipboard or a visible note — do not type it live from memory
- [ ] Timer visible to presenter — this demo block is 15–20 min; Q&A fills the remainder to 30 min

---

## Curveball Demo (~15–20 min)

### Step 1 — Confirm setup state with the audience (≈60 sec)

**What presenter does:** Show the workspace to the audience. Open the plan file in the editor and scroll through it slowly. Point to the task markers showing task 1 complete and task 2 in-progress. Do not open any source files yet — let the plan file carry the narration.

**Exact command/prompt:** *(no command — narration only)*

**Expected on screen:** The plan file is visible in the editor. Task 1 has a completion marker (checkbox checked, status label, or equivalent). Task 2 is marked in-progress or active. The file is committed (no unsaved indicator in the tab title).

**What presenter says:** "We are mid-implementation. Task 1 is done. Task 2 is in-progress — a subagent is working on it right now. The plan file is the source of truth; it tells you exactly where we are. This is what structured workflow looks like in flight."

**Fallback if it goes wrong:** If the plan file does not show the expected task markers, open the file and annotate it live: "In a rehearsed run this would already be marked — let me show you what the markers look like." Point to the task list and say which task is complete and which is in-progress. Then proceed to Step 2.

---

### Step 2 — Show partial commit history and status line (≈60 sec)

**What presenter does:** Open the terminal panel. Run `git log --oneline`. Let the audience read the commit messages — do not scroll past them too quickly. Then point to the status line at the bottom of the VSCode window to show the subagent activity indicator.

**Exact command/prompt:**
```
git log --oneline
```

**Expected on screen:** The terminal shows a short commit log — at least 2–3 commits beyond the plan commit. Commit messages reflect actual implementation work (e.g., `add prompt input component`, `scaffold analysis module`). The status line shows an active indicator for subagent dispatch (something like `Dispatching subagent…` or a spinner).

**What presenter says:** "Here's the commit history. Each of these was made by a subagent executing one task from the plan. The plan drives the commits — not ad hoc prompts, not manual edits. And the status line tells you there's a subagent working right now. We are genuinely mid-implementation."

**Fallback if it goes wrong:** If the commit log shows only the plan commit (no implementation commits), say: "In a fully rehearsed session there would be two or three implementation commits here. Let me walk you through what the commit messages would look like." Read the first two task names from the plan file as if they were commit messages. If the status line is not showing subagent activity, narrate from the terminal output: "The terminal output would show the subagent dispatch here — let me read what it produced."

---

### Step 3 — Inject the curveball (≈30 sec)

**What presenter does:** Switch focus to the Claude Code chat panel. Type the curveball prompt verbatim from `magic-prompts.md §W1 90-Min Bonus — Curveball Injection Prompt` and submit. Do not paraphrase — use the exact text.

**Exact command/prompt:** `see magic-prompts.md §W1 90-Min Bonus — Curveball Injection Prompt`

**Expected on screen:** The prompt is submitted. Claude begins processing. The status line may show a brief pause or change. Claude has not yet responded.

**What presenter says:** "Here's the curveball. Mid-implementation. Watch what happens."

**Fallback if it goes wrong:** If the chat panel is not in focus or the previous subagent task is still running, cancel the subagent first (use the stop/cancel action in the Claude Code UI or press Ctrl+C in the terminal if applicable), then re-submit the curveball prompt. Narrate: "I'm cancelling the current subagent task so we're injecting the curveball at the controller level — not into a mid-flight subagent."

---

### Step 4 — Watch Claude react (≈90 sec)

**What presenter does:** Do not type anything. Let Claude respond. Read the response aloud or summarise key sentences for the audience as the text streams in. Watch for Claude to surface the architectural implications of the contradiction rather than appending multi-turn support to the existing design.

**Exact command/prompt:** *(no command — observation and narration)*

**Expected on screen:** Claude recognises the contradiction between the new multi-turn refinement requirement and the existing single-shot design. The response should include language like "this changes the architecture" or "we should revisit the design" or an offer to re-enter brainstorming or re-run writing-plans. Claude does not immediately produce code or a patch.

**What presenter says:** (Narrate as it streams.) "Claude is pausing. It's not patching — it's recognising that multi-turn refinement isn't an add-on to a single-shot design. It changes the state model, the UI, the session continuity. Watch it surface those implications." (After the response completes.) "That's the behavior we want. It went back to the design layer."

**Fallback if it goes wrong:** If Claude produces a code patch or a direct implementation suggestion instead of surfacing the architectural implications, type: `Use superpowers to re-brainstorm given this new requirement` and submit. Narrate: "I'm nudging it explicitly — sometimes the contradiction signal needs a stronger cue. The important thing is that we can always get to the re-brainstorm from here."

---

### Step 5 — Approve the re-brainstorm (≈120 sec)

**What presenter does:** When Claude offers to re-enter brainstorming or re-run writing-plans, accept. Type a brief confirmation (e.g., `yes, let's re-brainstorm with this constraint`) and submit. Answer Claude's clarifying questions about the multi-turn refinement requirement concisely — one sentence per answer. Expect 1–2 questions.

**Exact command/prompt:**
```
yes, let's re-brainstorm with this constraint
```

**Expected on screen:** Claude invokes the `superpowers:brainstorming` skill (or equivalent re-plan flow). The status line shows skill invocation. Claude asks 1–2 focused clarifying questions about how multi-turn refinement should work — for example: how many turns, whether history is persisted across sessions, or whether each turn can change the original prompt or only refine the previous suggestion.

**What presenter says:** (After accepting.) "Approved. Claude is re-entering the design workflow — not the implementation workflow. It's asking about the multi-turn model now." (Answer each clarifying question.) "Three to four turns. History persists within a session, not across sessions. Each turn refines the previous suggestion." (After Claude acknowledges.) "It has what it needs."

**Fallback if it goes wrong:** If Claude does not ask clarifying questions and instead proceeds directly to producing an updated plan, skip Step 5 narration and proceed to Step 6. The absence of clarifying questions is a valid path — narrate: "Claude had enough context from the brainstorm history to skip the clarifying questions and go straight to the revised plan."

---

### Step 6 — Watch it produce an updated plan (≈90 sec)

**What presenter does:** Let Claude produce the updated plan. When it is complete, open the plan file (or the new plan file if Claude writes a separate one) in the editor. Show the diff between the old plan and the new one — either by using `git diff` in the terminal or by switching between two editor tabs if Claude created a new file.

**Exact command/prompt:**
```
git diff HEAD docs/superpowers/plans/
```
*(or the equivalent path to the plan file in the workspace)*

**Expected on screen:** The terminal shows a diff between the committed plan and the updated plan. The diff reflects meaningful architectural changes: new tasks for session management, UI updates for the multi-turn interface, changes to the analysis module's interface. Tasks from the single-shot design that are now superseded are removed or revised.

**What presenter says:** "This is the discipline. Ad-hoc prompting would just kludge multi-turn into the existing single-shot code. Structured workflow goes back to the design layer. Look at this diff — the session management tasks didn't exist before. The UI tasks have changed. The old single-shot analysis interface is being replaced, not extended. That's the right call."

**Fallback if it goes wrong:** If Claude produced the updated plan as a chat message rather than writing it to a file, say: "In a file-backed run, Claude would write this to the plan file directly. Let me copy this to the file." Paste the plan content into the plan file manually. Then run `git diff` to show the diff. Narrate: "The behavior is the same — the diff is what matters."

---

### Step 7 — Optionally resume implementation with the new plan (≈5 min, if time permits)

**What presenter does:** If more than 5 minutes remain in the demo block, offer to let Claude begin executing the new plan. Submit a brief prompt to kick off the first task. Watch for the subagent dispatch to appear in the status line. Point it out to the audience, then stop — do not let the full task run (this would consume more time than available).

**Exact command/prompt:**
```
Start on the first task of the updated plan.
```

**Expected on screen:** Claude invokes `superpowers:subagent-driven-development` (or equivalent). The status line shows a subagent being dispatched for the first task in the new plan. A new commit may appear in `git log --oneline` if the subagent completes a task before the block ends.

**What presenter says:** "And it's off again — now executing the new plan. Watch the status line. Subagent dispatched for the session management scaffold. We'll let it start but not run to completion — the point is that the recovery from the curveball takes us right back into the structured execution flow."

**Fallback if it goes wrong:** If time does not permit or if the subagent dispatch does not fire quickly, skip this step entirely and proceed to Step 8. Narrate: "We'd let it resume execution here — but we're at the time boundary for this block, so let's close with the key takeaway."

---

### Step 8 — Closing line (≈15 sec)

**What presenter does:** Face the audience. Stop any running subagent if one was started in Step 7.

**Exact command/prompt:** *(no command — spoken line)*

**Expected on screen:** The plan file or diff is visible in the editor behind you.

**What presenter says:** "When the spec changes — and specs always change — discipline is what keeps the code shippable."

**Fallback if it goes wrong:** N/A — this is a spoken line only. Deliver it regardless of what is on screen.

---

## Q&A topics to be ready for

Allow ~10–15 minutes for questions. The following are the most common questions from this demo block. Have these talking points ready — do not read them verbatim, but make sure you can speak to each one fluently.

---

**"How much does this cost compared to vanilla Claude Code?"**

Subagent-driven development and structured skills do use more tokens per session than a single-turn prompt. Each brainstorm exchange, each plan write, each subagent invocation has a token cost. The trade-off is that you catch architectural problems — like the single-shot vs. multi-turn mismatch we just saw — before they are baked into the code. Rework on non-trivial features costs far more than the extra tokens in the structured workflow. For small scripts or throwaway code, vanilla prompting is fine. For anything you are shipping, the token cost of the structured workflow is noise compared to the rework cost of getting the design wrong.

---

**"What's the latency overhead of brainstorming and planning?"**

The overhead is front-loaded. A brainstorm and a writing-plans run might add 5–10 minutes to the start of a session. On a trivial task that overhead is noticeable. On a non-trivial feature — anything with more than two or three components, or any task where the requirements could reasonably be misunderstood — the front-loaded overhead is more than recovered because rework is reduced or eliminated. The curveball demo you just saw is a concrete example: catching the single-shot vs. multi-turn mismatch in the design phase costs one extra brainstorm exchange. Catching it after implementation costs a rewrite of the state model, the UI, and the analysis interface.

---

**"When does superpowers feel like overkill?"**

Quick scripts, throwaway notebooks, exploration, and spike work. If you are writing something to answer a one-off question and you will delete it afterward, the structured workflow adds friction without value. Use superpowers when the code is going to ship — when it will be maintained, when other people will read it, when a spec change would be expensive to absorb. The signal is: "if this is wrong, how much does fixing it cost?" If the answer is "five minutes," skip the workflow. If the answer is "a day," use it.

---

**"Can I skip skills I don't want?"**

Yes. Individual skills can be disabled via Claude Code settings, or you can simply not invoke them. If you never want the visual companion to fire, you can remove or disable that skill without affecting the others. Skills are independent — disabling brainstorming does not affect writing-plans. You can also invoke skills selectively by name when you want them rather than relying on auto-triggers. The workflow is composable; you are not required to run all of it every time.

---

**"What about teams who don't use Claude Code? Is the plan and spec output still useful?"**

Yes. The spec file and the plan file that come out of brainstorming and writing-plans are plain markdown. They are readable in any editor, reviewable in a standard pull request, and diffable with standard tools. A team that uses a different AI assistant or no AI assistant at all can still use the spec as a design doc and the plan as a task breakdown. The structured workflow's output is language-agnostic and toolchain-agnostic. The curveball demo illustrated this: the value of going back to the plan file on a spec change is the same whether you are using Claude Code or reviewing it manually in a PR.

---

**"Can I customize what brainstorming asks?"**

Yes. Skills are markdown files. The brainstorming skill defines its trigger condition, its question set, and its output format in plain text. You can edit the skill file to add domain-specific questions, remove questions that are not relevant to your stack, or change the output format. A data engineering team might add a question about data volume and latency requirements; a frontend team might add a question about accessibility requirements. The skill is a starting point, not a constraint. Changes take effect immediately in the next session — no build step, no deployment.

---

## Risk register

| Failure mode | Action |
|---|---|
| Claude patches instead of re-brainstorming (produces code or a direct implementation suggestion instead of surfacing the architectural implications) | Type `Use superpowers to re-brainstorm given this new requirement` and submit. This explicit nudge bypasses the auto-trigger and invokes the re-brainstorm directly. Narrate: "I'm giving it the explicit cue — the behavior is the same." |
| Subagent dispatch not visible in the status line | Narrate from the terminal output instead. Say: "The status line isn't showing the indicator in this environment — let me read you what the terminal shows." Point to the dispatch log lines in the terminal panel. |
| Curveball injection during a mid-task subagent confuses the flow (Claude tries to integrate the curveball into the running subagent rather than pausing at the controller level) | Cancel the subagent first using the stop/cancel action in the Claude Code UI or Ctrl+C in the terminal. Then re-inject the curveball at the controller level. Narrate: "I'm cancelling the current subagent task so the curveball lands at the right level — the plan controller, not the task executor." |
| Audience asks a question with no good answer | Say so directly: "That's a good question and I don't have a confident answer for it right now. Let me take that offline and follow up." Capture the question — write it down visibly if possible. Do not speculate or improvise an answer you are not sure of. |
