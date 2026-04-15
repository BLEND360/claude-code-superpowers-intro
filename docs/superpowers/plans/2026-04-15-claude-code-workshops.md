# Claude Code Capabilities Workshops Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce all Bundle A deliverables for the two-workshop plan defined in `docs/superpowers/specs/2026-04-15-claude-code-workshops-design.md`: slide-by-slide content specs, presenter scripts, demo scripts, demo asset files, pre-staged demo branches, attendee pre-workshop materials, and a rehearsal checklist.

**Architecture:** Markdown-driven content artifacts under `docs/superpowers/workshops/` (excluding the existing pptx/pdf which stay untouched). Demo asset files live in `demo-assets/` at the repo root so they can be checked out cleanly during demos. Pre-staged demo branches (`workshop-w1-demo`, `workshop-w2-demo`) provide known-good starting states. The user and a co-presenter build actual slide decks themselves from these specs.

**Tech Stack:** Markdown for content. Python (settings.json + a small hook script) for the Snowflake safety hook asset. Git branches for pre-staged demo states.

---

## Status (2026-04-15)

**Paused after Task 16, awaiting partner review of the workshop content before generating demo assets and pre-staged branches.**

| Task | Status | Artifact |
|---|---|---|
| 1 | ✅ Done | Workshops directory tree |
| 2 | ✅ Done | `slide-3-rewrite.md` |
| 3 | ✅ Done | `magic-prompts.md` |
| 4 | ✅ Done | `workshop-1/slides.md` |
| 5 | ✅ Done | `workshop-1/presenter-script.md` |
| 6 | ✅ Done | `workshop-1/demo-1-script.md` |
| 7 | ✅ Done | `workshop-1/demo-2-script.md` |
| 8 | ✅ Done | `workshop-1/bonus-demo-script.md` |
| 9 | ✅ Done | `workshop-2/slides.md` (note: 1.5 min timeline drift; closing currently 0:30 instead of 2:00 — adjust during slide build) |
| 10 | ✅ Done | `workshop-2/presenter-script.md` |
| 11 | ✅ Done | `workshop-2/demo-1-script.md` |
| 12 | ✅ Done | `workshop-2/demo-2-script.md` |
| 13 | ✅ Done | `workshop-2/bonus-demo-script.md` |
| 14 | ✅ Done | `pre-workshop-w1.md` |
| 15 | ✅ Done | `pre-workshop-w2.md` |
| 16 | ✅ Done | `rehearsal-checklist.md` |
| 17 | ⏸ Paused | `demo-assets/w1-demo1-claude-md/CLAUDE.md.example` |
| 18 | ⏸ Paused | `demo-assets/w2-demo2-skill/.claude/skills/review-prompt-quality/SKILL.md` |
| 19 | ⏸ Paused | `demo-assets/w2-bonus-snowflake-hook/` (settings fragment + `safety_hook.py` + README) |
| 20 | ⏸ Paused | Pre-staged demo branches `workshop-w1-demo`, `workshop-w2-demo` |
| 21 | ⏸ Paused | `docs/superpowers/workshops/README.md` (workshops index) + final verification pass |

**To resume:** ask Claude to "resume the workshops plan" and Tasks 17–21 will execute. Task 17–19 content is fully specified inline in this plan (no judgment needed). Task 20 is mechanical git branch creation. Task 21 is the index + cross-link verification.

---

## File Structure

```
claude-code-superpowers-intro/
├── docs/superpowers/
│   ├── specs/
│   │   └── 2026-04-15-claude-code-workshops-design.md   (exists — the spec)
│   ├── plans/
│   │   └── 2026-04-15-claude-code-workshops.md          (this file)
│   └── workshops/
│       ├── Claude Code Capabilities Workshop.pptx       (existing — untouched)
│       ├── Claude Code Capabilities Workshop.pdf        (existing — untouched)
│       ├── slide-3-rewrite.md                           (Task 2)
│       ├── magic-prompts.md                             (Task 3)
│       ├── workshop-1/
│       │   ├── slides.md                                (Task 4)
│       │   ├── presenter-script.md                      (Task 5)
│       │   ├── demo-1-script.md                         (Task 6)
│       │   ├── demo-2-script.md                         (Task 7)
│       │   └── bonus-demo-script.md                     (Task 8)
│       ├── workshop-2/
│       │   ├── slides.md                                (Task 9)
│       │   ├── presenter-script.md                      (Task 10)
│       │   ├── demo-1-script.md                         (Task 11)
│       │   ├── demo-2-script.md                         (Task 12)
│       │   └── bonus-demo-script.md                     (Task 13)
│       ├── pre-workshop-w1.md                           (Task 14)
│       ├── pre-workshop-w2.md                           (Task 15)
│       └── rehearsal-checklist.md                       (Task 16)
└── demo-assets/
    ├── w1-demo1-claude-md/
    │   └── CLAUDE.md.example                            (Task 17)
    ├── w2-demo2-skill/
    │   └── .claude/skills/review-prompt-quality/SKILL.md (Task 18)
    └── w2-bonus-snowflake-hook/
        ├── settings.json.fragment                       (Task 19)
        └── safety_hook.py                               (Task 19)
```

Pre-staged branches (Task 20):
- `workshop-w1-demo` — clean state for the W1 fresh-brainstorm demo
- `workshop-w2-demo` — solution-branch state with attendee-following install instructions ready

---

## Conventions used throughout

- **Slides specs** use this format per slide:
  ```
  ## Slide N — <Title>
  **Time:** Hh:MM-Hh:MM (X min)
  **Layout:** <title slide / two-column / image+text / etc.>
  **Body bullets:**
  - <bullet 1>
  - <bullet 2>
  **Speaker notes (~75 sec):**
  <prose>
  **Demo cue (if any):** <"transition into Demo 1 here">
  ```
- **Demo scripts** use this format:
  ```
  ### Step N — <action> (≈X sec)
  **What presenter does:** <action>
  **Exact command/prompt:** `<verbatim>`
  **Expected on screen:** <what audience sees>
  **What presenter says:** "<spoken line>"
  **Fallback if it goes wrong:** <plan B>
  ```
- **Commit messages** follow conventional commit style (`docs:`, `chore:`, `feat:` for asset files).

---

### Task 1: Create workshops directory tree

**Files:**
- Create: `docs/superpowers/workshops/workshop-1/.gitkeep`
- Create: `docs/superpowers/workshops/workshop-2/.gitkeep`
- Create: `demo-assets/w1-demo1-claude-md/.gitkeep`
- Create: `demo-assets/w2-demo2-skill/.claude/skills/review-prompt-quality/.gitkeep`
- Create: `demo-assets/w2-bonus-snowflake-hook/.gitkeep`

- [ ] **Step 1: Create directories with .gitkeep markers**

```bash
mkdir -p docs/superpowers/workshops/workshop-1
mkdir -p docs/superpowers/workshops/workshop-2
mkdir -p demo-assets/w1-demo1-claude-md
mkdir -p demo-assets/w2-demo2-skill/.claude/skills/review-prompt-quality
mkdir -p demo-assets/w2-bonus-snowflake-hook
touch docs/superpowers/workshops/workshop-1/.gitkeep
touch docs/superpowers/workshops/workshop-2/.gitkeep
touch demo-assets/w1-demo1-claude-md/.gitkeep
touch demo-assets/w2-demo2-skill/.claude/skills/review-prompt-quality/.gitkeep
touch demo-assets/w2-bonus-snowflake-hook/.gitkeep
```

- [ ] **Step 2: Verify directories created**

Run: `ls -la docs/superpowers/workshops/ demo-assets/`
Expected: shows `workshop-1/`, `workshop-2/`, and the three `demo-assets/` subdirs.

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/workshops/workshop-1/.gitkeep \
        docs/superpowers/workshops/workshop-2/.gitkeep \
        demo-assets/
git commit -m "chore: scaffold workshop content and demo asset directories"
```

---

### Task 2: Write slide 3 rewrite spec

**Files:**
- Create: `docs/superpowers/workshops/slide-3-rewrite.md`

- [ ] **Step 1: Write the corrected slide 3 spec**

Create `docs/superpowers/workshops/slide-3-rewrite.md` with the following content:

```markdown
# Slide 3 Rewrite — Workshop-wise Topics

**Replaces:** existing slide 3 in `Claude Code Capabilities Workshop.pptx`.

**Title:** Workshop-wise topics

**Layout:** Two-column.

**Left column — Workshop 01: Using Claude Code Well**

- CLAUDE.md & project memory
- Context, Compaction, Permissions
- Plan Mode + Checkpoints
- Slash Commands & Plugins (install)
- **Pivot:** Superpowers as the integrating workflow
  - Brainstorming → Writing-plans → Subagent-driven development

**Right column — Workshop 02: Power Tools + Authoring**

- MCP concept + the consultancy denominators
  - Context7 (docs)
  - GitHub MCP (repos/PRs/issues)
  - Snowflake MCP (data warehouse)
- Headless mode + plugin marketplaces
- "MCP buffet" — picking by client stack
- Authoring snack: writing your own Skill
- Hooks (W2 90-min bonus)

**Footer note:** Each workshop available in 60-min (vital) and 90-min (vital + bonus) versions.

**Speaker notes (~60 sec):**
Workshop 1 covers the everyday primitives of Claude Code, then shows how the superpowers plugin ties them together into a workflow that produces deployment-ready code instead of vibe-coded scripts. Workshop 2 takes the same project and extends it with professional MCPs you can use on any client engagement, plus a short look at how to author your own skills. Across the two workshops every capability on the slide-2 diagram gets airtime.
```

- [ ] **Step 2: Verify file**

Run: `wc -l docs/superpowers/workshops/slide-3-rewrite.md`
Expected: ~30-40 lines.

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/workshops/slide-3-rewrite.md
git commit -m "docs(workshops): add slide 3 rewrite spec for new bucketing"
```

---

### Task 3: Write magic-prompts file

**Files:**
- Create: `docs/superpowers/workshops/magic-prompts.md`

- [ ] **Step 1: Write magic-prompts content**

Create `docs/superpowers/workshops/magic-prompts.md` covering:

1. **Header explaining what these are** — engineered prompts with high-likelihood superpowers behavior, used in demo scripts. Include caveat: model output is non-deterministic; rehearsal required.

2. **W1 Demo 2 — brainstorm seed prompt:**
   - Verbatim seed: `Let's use superpowers to brainstorm a tool that helps people write better LLM prompts. The audience is data scientists and AI engineers.`
   - Why this works: "build a tool" triggers the brainstorming skill reliably; named audience steers toward concrete questions fast.
   - Expected first 2-3 questions Claude asks (so presenter can react fluidly).

3. **W1 Demo 2 — visual companion steering question:**
   - When Claude reaches a UI/output-format question, presenter answer: `Show me side-by-side comparison vs stacked diff vs tabbed view options for the refined prompt display — I want to actually see what each looks like.`
   - Why this works: explicit ask for visual comparison gives Claude clear signal that the visual companion is appropriate.
   - Fallback narration if Claude doesn't offer the companion: `In a longer session here, brainstorming would offer to spin up a browser companion to show these layouts side by side. Let me show you what that looks like with a screenshot.` (Reference fallback screenshot to be captured during rehearsal.)

4. **W1 90-min bonus — curveball injection prompt:**
   - When mid-implementation, presenter pastes: `Hold on — I just talked to a stakeholder. They actually need this tool to also support multi-turn refinement, where the user iterates with the assistant 3-4 times. This contradicts the single-shot design we planned. Adjust.`
   - Why this works: explicit contradiction signal triggers superpowers' re-brainstorm/re-plan behavior rather than a kludge fix.

5. **W2 Demo 1 — Context7 contrast prompts:**
   - Vanilla (pre-Context7): `What's the recommended way to display Streamlit dataframes with row selection in the latest Streamlit?` (likely produces stale guidance)
   - With Context7: same prompt — show citation of current docs.

6. **W2 Demo 2 — custom skill trigger prompt:**
   - After installing the review-prompt-quality skill, in a fresh session: `Can you review this prompt for me and suggest improvements? "Generate a summary of the document."`
   - Expected: status line shows `Using superpowers...review-prompt-quality` (or similar — exact name depends on skill file).

7. **W2 bonus — Snowflake destructive-query trigger:**
   - After installing the safety hook, ask: `Run an UPDATE on the prod_sales table to set discount=0 for last quarter.`
   - Expected: hook intercepts, requires confirmation.

- [ ] **Step 2: Verify file structure**

Run: `grep -c "^##" docs/superpowers/workshops/magic-prompts.md`
Expected: at least 7 (one per section).

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/workshops/magic-prompts.md
git commit -m "docs(workshops): add engineered demo prompts with fallbacks"
```

---

### Task 4: Write W1 slides spec

**Files:**
- Create: `docs/superpowers/workshops/workshop-1/slides.md`

- [ ] **Step 1: Write W1 slides spec**

Create `docs/superpowers/workshops/workshop-1/slides.md` containing one slide section per slide following the convention defined at the top of this plan. Required slides:

1. **Title slide** — "Workshop 1: Using Claude Code Well" (0:00-0:30, 30 sec)
2. **Hook + agenda** — show slide-2 capability diagram, name the 8 W1 squares (0:30-2:00, 90 sec)
3. **What this workshop assumes + housekeeping** — install was pre-shared; quick "raise hand if your status line shows superpowers" check (2:00-5:00, 3 min)
4. **CLAUDE.md** — reuse existing slide 21 content as spec basis. Cover: what it is, 3-level hierarchy, what to include, 200-line cap, /init scaffold, iterate-don't-preempt rule (5:00-10:00, 5 min)
5. **Context + Compaction** — what Claude sees per turn; compaction triggers; when to manually `/compact` (10:00-14:00, 4 min)
6. **Plan Mode + Checkpoints** — read-only review before action; revert any step (14:00-18:00, 4 min)
7. **Permissions** — allow/deny tool lists; settings.json basics; the safety value (18:00-21:00, 3 min)
8. **Slash Commands + Plugins-as-install** — `/init`, `/plugin install`, what plugins ship (21:00-25:00, 4 min)
9. **Demo 1 transition** — "now let's see all of this in action" (25:00-25:30, 30 sec)
10. **[DEMO 1]** — see `demo-1-script.md` (25:00-33:00, 8 min)
11. **Bridge: this works, but for deployment-ready code we need more discipline** (33:00-33:30, 30 sec)
12. **What superpowers is** — plugin (⑧) bundling skills (⑤), uses subagents (⑫) and slash commands (⑩); install command; status line indicator (33:30-36:30, 3 min)
13. **Brainstorming skill** — one question at a time; 2-3 approach options; visual companion offer; validated design before code (36:30-39:30, 3 min)
14. **Writing-plans skill** — design → bite-sized tasks with tests + commits; produces a markdown plan file (39:30-42:30, 3 min)
15. **Subagent-driven development** — fresh subagent per task; two-stage review (spec compliance + code quality) (42:30-45:30, 3 min)
16. **Why this matters for deployment-ready code** — failure modes of ad-hoc prompting; how each skill prevents one (45:30-48:00, 2.5 min)
17. **Demo 2 transition** — "let's watch this happen live" (48:00-48:30, 30 sec)
18. **[DEMO 2]** — see `demo-2-script.md` (48:00-58:00, 10 min)
19. **Closing + pointer to W2** (58:00-60:00, 2 min)

For each slide section include: time slot, layout suggestion, body bullets, ~75 sec speaker notes, and any demo cues. Mark slide 4 as "reuse existing slide 21 — already drafted, see pptx."

- [ ] **Step 2: Verify slide count and time math**

Run: `grep -c "^## Slide" docs/superpowers/workshops/workshop-1/slides.md`
Expected: 19 (matching the list above).

Manually verify the time slots sum to 60:00.

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/workshops/workshop-1/slides.md
git commit -m "docs(workshops): add W1 slide-by-slide content spec"
```

---

### Task 5: Write W1 presenter script

**Files:**
- Create: `docs/superpowers/workshops/workshop-1/presenter-script.md`

- [ ] **Step 1: Write W1 presenter script**

Create `docs/superpowers/workshops/workshop-1/presenter-script.md` containing one section per topic from W1 slides spec. Each section should be:

- Section header matching the slide title
- 3-5 paragraphs of full prose the presenter can read or paraphrase
- Bolded key points the presenter must hit
- Optional analogy or relatable example for the audience (consultants doing data/AI work)

Cover all topics 4-8 (theory part 1) and 12-16 (theory part 2) from the slides spec. Skip slides that are pure transitions, demo cues, or housekeeping — those don't need full prose.

For consistency, end each section with a `**Transition into next topic:** "..."` line giving the bridge sentence.

Topic-specific guidance:
- **CLAUDE.md** section: lead with the failure mode (Claude forgets context; you re-explain every session), then introduce CLAUDE.md as the fix.
- **Context + Compaction** section: explain "context" by analogy (a meeting with finite minutes; eventually old discussion gets paged out).
- **Why this matters for deployment-ready code** section: this is the emotional close — connect back to "we're consultants, our code ships to clients, we can't afford ad-hoc."

- [ ] **Step 2: Verify section coverage**

Run: `grep -c "^## " docs/superpowers/workshops/workshop-1/presenter-script.md`
Expected: at least 10 (covering all theory slides).

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/workshops/workshop-1/presenter-script.md
git commit -m "docs(workshops): add W1 presenter script with full talking points"
```

---

### Task 6: Write W1 Demo 1 script

**Files:**
- Create: `docs/superpowers/workshops/workshop-1/demo-1-script.md`

- [ ] **Step 1: Write W1 Demo 1 script**

Create `docs/superpowers/workshops/workshop-1/demo-1-script.md` covering "primitives in action" demo (8 min), using the demo-script convention defined at the top of this plan.

Required steps:

1. **Setup state:** Open VSCode in an empty workspace named `demo-w1-primitives`. Have the `demo-assets/w1-demo1-claude-md/CLAUDE.md.example` open in another tab as the reference for what `/init` would scaffold.
2. **Run /init** — observe Claude scaffold a CLAUDE.md. Show the file content for ~15 seconds. Compare briefly with the example.
3. **Edit CLAUDE.md** — add 2 lines (e.g., a stack note and a "never edit migrations directly" rule). Save.
4. **Switch to plan mode** — show the keyboard shortcut/UI cue. Prompt: `Add a function in src/utils.py that validates a date range and returns true if start < end.`
5. **Show the plan** — read out what Claude proposes. Approve it.
6. **Show the checkpoint timeline** — point to the VSCode panel/status line indicator showing the new checkpoint.
7. **Make a deliberate "mistake"** — accept the change, then prompt: `Actually I want it to also handle null inputs.` Watch Claude make the change.
8. **Revert** — use the checkpoint UI to roll back to before the null handling. Verify file content reverted.
9. **Closing line:** "This works for small tasks. But for real deployment-ready code, we need more than plan-mode-and-pray. That's where superpowers comes in."

For each step: presenter actions, exact prompts/commands, expected on-screen result, spoken line, fallback if it fails.

**Total time budget:** 8 minutes. Aim for each step to be 30-90 seconds.

**Risk register at end of file:** What can go wrong, what to do.
- `/init` produces unexpected output → have the reference example open, narrate "in your repo it would also include X."
- Plan mode UI not visible → use the verbal `claude --plan` flag or just narrate the concept.
- Checkpoint revert doesn't work → use git as the fallback (`git checkout src/utils.py`).

- [ ] **Step 2: Verify structure**

Run: `grep -c "^### Step" docs/superpowers/workshops/workshop-1/demo-1-script.md`
Expected: at least 9 (one per major step).

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/workshops/workshop-1/demo-1-script.md
git commit -m "docs(workshops): add W1 Demo 1 script for primitives-in-action"
```

---

### Task 7: Write W1 Demo 2 script

**Files:**
- Create: `docs/superpowers/workshops/workshop-1/demo-2-script.md`

- [ ] **Step 1: Write W1 Demo 2 script**

Create `docs/superpowers/workshops/workshop-1/demo-2-script.md` covering the live brainstorm + visual companion + cooked turkey reveal demo (10 min). Reference `magic-prompts.md` for the verbatim engineered prompts (do not duplicate them in the script — link to the magic-prompts file).

Required steps:

1. **Setup state:** Two VSCode windows open:
   - Window A: empty workspace `demo-w1-brainstorm` for the live brainstorm.
   - Window B: this repo on the `solution` branch, with `docs/superpowers/specs/2026-04-10-promptcraft-design.md` and `docs/superpowers/plans/2026-04-10-promptcraft.md` open in tabs, plus a terminal ready to `streamlit run promptcraft/app.py`. This is the safety net + reveal source.
2. **In Window A — kick off brainstorm** with the seed prompt from `magic-prompts.md` §2.
3. **Answer 2-3 brainstorm questions** authentically (audience type, prompt complexity, etc.) — keep answers short to advance fast.
4. **At UI/format question — trigger visual companion** with the steering answer from `magic-prompts.md` §3.
5. **Accept the visual companion offer** when Claude proposes it. Browser opens.
6. **Show the rendered mockups** for ~30 sec. Point out: "this is brainstorming detecting that the question is visual and offering a companion — it didn't just ask another text question."
7. **Pivot to the cooked turkey** with the line from spec section "Demo 2 (~10 min) — live brainstorm of PromptCraft → reveal" step 3.
8. **Switch to Window B** — open the spec file. Scroll, point out: "this is what comes out of brainstorming completed end-to-end. It's the design doc, generated from the workflow."
9. **Open the plan file** — point to the bite-sized tasks. "And this is what writing-plans turns the spec into."
10. **Run the app** — `streamlit run promptcraft/app.py`. Use it for ~60 sec (paste a prompt, see the analysis).
11. **Closing line:** "Brainstorm to deployed app, structured the whole way. This is what 'using Claude Code well' looks like for deployment-ready code."

For each step: presenter actions, expected on-screen result, spoken line, fallback if visual companion doesn't trigger or brainstorm derails.

**Pre-empt slide:** Include the line from the spec — *"Your brainstorm run will land somewhere different from this exact spec — that's the workflow doing its job, not a flaw."*

**Risk register:**
- Brainstorm doesn't ask a UI question → manually paste the steering question after question 3 regardless.
- Visual companion not offered → use the fallback narration from `magic-prompts.md` §3.
- Streamlit app fails to start → show the running version from a screenshot/recording prepared in rehearsal.

- [ ] **Step 2: Verify structure**

Run: `grep -c "^### Step" docs/superpowers/workshops/workshop-1/demo-2-script.md`
Expected: at least 11.

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/workshops/workshop-1/demo-2-script.md
git commit -m "docs(workshops): add W1 Demo 2 script for brainstorm-and-reveal"
```

---

### Task 8: Write W1 90-min bonus demo script

**Files:**
- Create: `docs/superpowers/workshops/workshop-1/bonus-demo-script.md`

- [ ] **Step 1: Write W1 bonus demo script**

Create `docs/superpowers/workshops/workshop-1/bonus-demo-script.md` covering the curveball demo (15-20 min) + Q&A (10-15 min), total 30 min.

Required steps:

1. **Setup state:** A fresh repo or the `demo-w1-brainstorm` workspace from Demo 2. Brainstorm fully completed; writing-plans run; subagent-driven development started on the first 1-2 tasks.
2. **Get visibly mid-implementation** — show one task complete, code committed, currently working on task 2. Status line shows subagent dispatched.
3. **Inject the curveball** with the prompt from `magic-prompts.md` §4.
4. **Watch Claude react** — it should pause, recognize the contradiction, and propose re-entering brainstorming or writing-plans rather than just patching.
5. **Approve the re-brainstorm** — let it ask 1-2 clarifying questions about the multi-turn refinement requirement.
6. **Watch it produce an updated plan** — point to: "this is the discipline. Ad-hoc prompting would just kludge multi-turn into the existing single-shot code. Structured workflow goes back to the design layer."
7. **Optionally let it resume implementation** with the new plan — if time permits.
8. **Closing line:** "When the spec changes — and specs always change — discipline is what keeps the code shippable."
9. **Q&A (10-15 min)** — common questions presenter should be ready for: cost, latency, when does superpowers feel like overkill, can you skip skills you don't want.

For each step: presenter actions, expected behavior, spoken line, fallback.

**Risk register:**
- Claude patches instead of re-brainstorming → presenter explicitly types `Use superpowers to re-brainstorm given this new requirement` to nudge it.
- Subagent dispatch not visible → narrate from terminal output instead of status line.

- [ ] **Step 2: Verify structure**

Run: `grep -c "^### Step" docs/superpowers/workshops/workshop-1/bonus-demo-script.md`
Expected: at least 9.

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/workshops/workshop-1/bonus-demo-script.md
git commit -m "docs(workshops): add W1 90-min bonus demo script (curveball + Q&A)"
```

---

### Task 9: Write W2 slides spec

**Files:**
- Create: `docs/superpowers/workshops/workshop-2/slides.md`

- [ ] **Step 1: Write W2 slides spec**

Create `docs/superpowers/workshops/workshop-2/slides.md` using the same convention as Task 4. Required slides:

1. **Title slide** — "Workshop 2: Power Tools + Authoring" (0:00-0:30, 30 sec)
2. **Hook + recap of W1** — what we learned; bridge to "now we extend it" (0:30-2:00, 90 sec)
3. **Today's roadmap** — ~70% consume (MCPs/tools), ~30% author (skills); show the "MCP buffet" preview (2:00-5:00, 3 min)
4. **What is MCP, why it matters** — protocol definition, "USB-C of AI tooling" framing, architecture diagram from slide 2 (5:00-9:00, 4 min)
5. **Context7** — model cutoff problem, what Context7 fixes, install command, citation example (9:00-13:00, 4 min)
6. **GitHub MCP** — featured because it's the consultancy denominator; what it does (PRs, issues, code search across repos) (13:00-17:00, 4 min)
7. **Snowflake MCP** — featured because of org cert push; what it does (schema reads, query execution); safety considerations preview (17:00-21:00, 4 min)
8. **Headless mode + plugin marketplaces** — `claude -p` for CI/cron; `/plugin install`; the official + community marketplaces (21:00-25:00, 4 min)
9. **MCP buffet slide** — single dense slide of categories x examples (25:00-26:00, 1 min — let it linger as Demo 1 setup happens)
10. **Demo 1 transition** — "let's wire Context7 in and see it work" (26:00-26:30, 30 sec)
11. **[DEMO 1]** — see `demo-1-script.md` (25:00-33:00, 8 min)
12. **Authoring snack intro** — "you've seen what's available; now see how small the surface really is" (33:00-34:00, 1 min)
13. **Skills authoring** — anatomy of SKILL.md (frontmatter + body), location, discovery/triggering (34:00-38:00, 4 min)
14. **Hooks** — PreToolUse / PostToolUse / Stop / SessionStart events; settings.json wiring; common use cases (38:00-41:00, 3 min)
15. **Custom subagents + plugin publishing** — brief mention of authoring custom agents; pointer to plugin marketplace publishing (41:00-44:00, 3 min)
16. **Demo 2 transition** — "let's write a tiny skill in 5 minutes" (44:00-44:30, 30 sec)
17. **Closing on consume vs author** — "consume to get value fast; author when you do it twice" (44:30-48:00, 3.5 min)
18. **[DEMO 2]** — see `demo-2-script.md` (48:00-58:00, 10 min)
19. **Closing + where to learn more** (58:00-60:00, 2 min)

For each slide section include time slot, layout suggestion, body bullets, ~75 sec speaker notes, demo cues.

**Buffet slide content (slide 9):**

| Need on engagement | Look for MCP |
|---|---|
| Other cloud (Azure / AWS / GCP) | Azure MCP, AWS MCP |
| Other repo (Azure DevOps, GitLab) | Azure DevOps MCP, GitLab MCP |
| Tickets (Jira, Linear, ADO Boards) | Jira MCP, Linear MCP |
| Docs (Confluence, Notion, SharePoint) | Confluence MCP, Notion MCP |
| Chat (Teams, Slack) | Teams MCP, Slack MCP |
| Browser automation | Playwright MCP |
| Other DBs (Postgres, BigQuery, Databricks) | Postgres MCP, BigQuery MCP |

Plus the framing line: *"The MCP you install depends on your client's stack. We're demoing GitHub + Snowflake because they're the consultancy denominators. The pattern transfers."*

- [ ] **Step 2: Verify slide count and time math**

Run: `grep -c "^## Slide" docs/superpowers/workshops/workshop-2/slides.md`
Expected: 19.

Manually verify time slots sum to 60:00.

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/workshops/workshop-2/slides.md
git commit -m "docs(workshops): add W2 slide-by-slide content spec"
```

---

### Task 10: Write W2 presenter script

**Files:**
- Create: `docs/superpowers/workshops/workshop-2/presenter-script.md`

- [ ] **Step 1: Write W2 presenter script**

Create `docs/superpowers/workshops/workshop-2/presenter-script.md` containing full prose for each W2 theory slide (slides 4-8 and 13-15 from the slides spec). Use the same conventions as Task 5 (one section per slide, 3-5 paragraphs, bolded key points, transition line at end).

Topic-specific guidance:
- **What is MCP** section: define the problem (every tool needed its own integration before MCP) before defining the solution.
- **Context7** section: include the concrete example — "ask Claude about a Streamlit feature added 3 months after its training cutoff; without Context7 it confabulates, with Context7 it cites the actual current docs."
- **GitHub MCP** section: emphasize the "consultancy denominator" framing — most clients have GitHub even if their internal stack is Azure DevOps.
- **Snowflake MCP** section: tie to org cert push; preview the safety hook from the bonus demo.
- **Skills authoring** section: emphasize how *small* a useful skill is — "10 lines, not a project." Show a snippet of SKILL.md anatomy.
- **Hooks** section: each event type gets one sentence + one example use case.

End with **transition lines** between sections.

- [ ] **Step 2: Verify section coverage**

Run: `grep -c "^## " docs/superpowers/workshops/workshop-2/presenter-script.md`
Expected: at least 8 (covering all theory slides).

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/workshops/workshop-2/presenter-script.md
git commit -m "docs(workshops): add W2 presenter script with full talking points"
```

---

### Task 11: Write W2 Demo 1 script (Context7)

**Files:**
- Create: `docs/superpowers/workshops/workshop-2/demo-1-script.md`

- [ ] **Step 1: Write W2 Demo 1 script**

Create `docs/superpowers/workshops/workshop-2/demo-1-script.md` covering the Context7-in-PromptCraft demo (8 min). Reference `magic-prompts.md` §5 for the contrast prompts.

Required steps:

1. **Setup state:** VSCode open on the `workshop-w2-demo` branch (or `solution`) of this repo. PromptCraft codebase visible.
2. **Vanilla query (pre-Context7)** — paste the vanilla prompt from `magic-prompts.md` §5. Show Claude's response. Point out any stale or generic answer.
3. **Install Context7 MCP** — show the install command, restart Claude session if required, verify it's loaded (status line).
4. **Re-run the same query** — show Claude now references current Streamlit docs with citations.
5. **Make a real edit** — ask Claude to use the Context7-fetched info to improve a piece of `app.py`. Watch the edit happen.
6. **Test the change** — `streamlit run promptcraft/app.py` if time permits, or just show the diff.
7. **Closing line:** "This single MCP eliminates the #1 reason model output goes stale. Same pattern works for any library — pandas, scikit-learn, dbt, anything."

For each step: presenter actions, exact commands, expected on-screen result, spoken line, fallback.

**Risk register:**
- Context7 install fails or requires API key not pre-configured → use a screenshot/recording fallback prepared in rehearsal.
- Vanilla query happens to give a current answer → switch to a different recently-changed Streamlit feature. Have 2-3 backup queries ready.

- [ ] **Step 2: Verify structure**

Run: `grep -c "^### Step" docs/superpowers/workshops/workshop-2/demo-1-script.md`
Expected: at least 7.

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/workshops/workshop-2/demo-1-script.md
git commit -m "docs(workshops): add W2 Demo 1 script for Context7-in-PromptCraft"
```

---

### Task 12: Write W2 Demo 2 script (custom skill)

**Files:**
- Create: `docs/superpowers/workshops/workshop-2/demo-2-script.md`

- [ ] **Step 1: Write W2 Demo 2 script**

Create `docs/superpowers/workshops/workshop-2/demo-2-script.md` covering the custom-skill authoring demo (10 min). Reference `magic-prompts.md` §6 for the trigger prompt.

Required steps:

1. **Setup state:** Same VSCode session as Demo 1 (PromptCraft repo). The `demo-assets/w2-demo2-skill/.claude/skills/review-prompt-quality/SKILL.md` file is the reference for what the presenter will create live.
2. **Show an empty `.claude/skills/` directory** in the repo. Point out: "this is where Claude looks for project-local skills."
3. **Create the SKILL.md file** — type or paste the contents from the demo-assets reference. Keep it short (~15 lines). Read out the frontmatter as you type it: `name`, `description` (this is what triggers it), and the body (the instructions Claude follows).
4. **Save and start a fresh Claude session** in the same repo (close + reopen, or `/clear`).
5. **Trigger the skill** with the prompt from `magic-prompts.md` §6.
6. **Watch the status line** — show the new skill being invoked (`Using ...review-prompt-quality`).
7. **Inspect the output** — Claude follows the skill's instructions, producing structured prompt-review feedback rather than generic suggestions.
8. **Edit the skill live** — change one line in the body (e.g., add "Always suggest a refined version at the end"). Save.
9. **Re-trigger** — show the changed behavior immediately.
10. **Closing line:** "Skills are this small. If you have a workflow you do twice, write a skill — it's 10 lines, not a project. Same SKILL.md format superpowers itself uses."

For each step: presenter actions, exact commands/file content, expected on-screen result, spoken line, fallback.

**Risk register:**
- Skill not auto-invoked → in the trigger prompt, explicitly say `Use the review-prompt-quality skill to review this prompt: ...`
- Status line doesn't show skill name → point to terminal output where it's logged.

- [ ] **Step 2: Verify structure**

Run: `grep -c "^### Step" docs/superpowers/workshops/workshop-2/demo-2-script.md`
Expected: at least 10.

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/workshops/workshop-2/demo-2-script.md
git commit -m "docs(workshops): add W2 Demo 2 script for custom skill authoring"
```

---

### Task 13: Write W2 90-min bonus demo script (Snowflake + hook)

**Files:**
- Create: `docs/superpowers/workshops/workshop-2/bonus-demo-script.md`

- [ ] **Step 1: Write W2 bonus demo script**

Create `docs/superpowers/workshops/workshop-2/bonus-demo-script.md` covering the Snowflake MCP + safety hook demo (15 min) + Q&A (15 min), total 30 min. Reference `magic-prompts.md` §7 for the destructive-query trigger.

Required steps for the demo (~15 min):

1. **Setup state:** PromptCraft repo open. A Snowflake sandbox warehouse and credentials available (per the open question in the spec). Hook script and settings fragment available at `demo-assets/w2-bonus-snowflake-hook/`.
2. **Install Snowflake MCP** — show install command and authentication flow. Confirm it's loaded.
3. **Run a SELECT query** — ask Claude to read the schema of a table and write a query against it. Watch it succeed with real data.
4. **Show what the safety problem looks like** — ask Claude to do an UPDATE without the hook installed. Watch it execute (in sandbox — emphasize "this is sandbox; on prod this would be terrifying").
5. **Install the safety hook** — copy `demo-assets/w2-bonus-snowflake-hook/settings.json.fragment` into the project's `.claude/settings.json`. Place `safety_hook.py` accordingly. Restart Claude session.
6. **Trigger the hook** with the destructive prompt from `magic-prompts.md` §7.
7. **Show the intercept** — hook fires; Claude is blocked from executing without explicit confirmation.
8. **Override and execute** — confirm the action; watch it proceed.
9. **Closing line:** "MCPs give Claude access. Hooks let you put guardrails on that access. Together: deployment-ready."

Q&A topics to be ready for (~15 min):
- "What if the hook misfires on a legitimate query?" — discuss the false-positive cost vs. the safety value.
- "Can hooks call external systems?" — yes, briefly explain.
- "Can I write a hook in Python / JS / Bash?" — yes, any executable.
- Audience-driven: "What MCP would help your daily work?" — install one or two on the fly if possible.

**Risk register:**
- Snowflake sandbox unavailable → use a local SQLite + a fake "snowflake" MCP shim, or pure narration with screenshots from rehearsal.
- Hook script fails to load → debug live as a teaching moment ("this is what hook misconfiguration looks like; here's how you'd fix it").

- [ ] **Step 2: Verify structure**

Run: `grep -c "^### Step" docs/superpowers/workshops/workshop-2/bonus-demo-script.md`
Expected: at least 9.

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/workshops/workshop-2/bonus-demo-script.md
git commit -m "docs(workshops): add W2 90-min bonus demo script (Snowflake + hook)"
```

---

### Task 14: Write pre-workshop W1 attendee materials

**Files:**
- Create: `docs/superpowers/workshops/pre-workshop-w1.md`

- [ ] **Step 1: Write pre-workshop W1 doc**

Create `docs/superpowers/workshops/pre-workshop-w1.md` containing:

1. **Header** — "Pre-workshop checklist for Workshop 1: Using Claude Code Well." Send ~3 days before.
2. **Why prep matters** — 1 paragraph: workshop time is for learning, not installing.
3. **Required setup (must complete before workshop):**
   - Install Claude Code CLI — link to official docs.
   - Install Claude Code VSCode extension — link.
   - Install superpowers plugin: `/plugin install superpowers@claude-plugins-official`
   - Configure your Anthropic API key per org standard.
4. **Verification steps:**
   - Open VSCode. Open the Claude Code panel.
   - Run a trivial command: `Hello, are you working?`
   - Confirm the status line shows session activity.
5. **What "working" looks like** — placeholder for screenshot to be captured during rehearsal: status line showing skill invocation when you ask for help with a task.
6. **Optional pre-read** — link to `guide/01-introduction.md` in this repo (~5 min read).
7. **Troubleshooting FAQ** — common issues:
   - Status line not showing → check VSCode extension version.
   - `/plugin install` fails → check Claude Code CLI version, restart session.
   - API key issues → org-specific contact.
8. **What to bring on the day** — laptop with the above set up; nothing else.

- [ ] **Step 2: Verify file**

Run: `wc -l docs/superpowers/workshops/pre-workshop-w1.md`
Expected: at least 50 lines.

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/workshops/pre-workshop-w1.md
git commit -m "docs(workshops): add pre-workshop W1 attendee checklist"
```

---

### Task 15: Write pre-workshop W2 attendee materials

**Files:**
- Create: `docs/superpowers/workshops/pre-workshop-w2.md`

- [ ] **Step 1: Write pre-workshop W2 doc**

Create `docs/superpowers/workshops/pre-workshop-w2.md` containing:

1. **Header** — "Pre-workshop checklist for Workshop 2: Power Tools + Authoring." Send between W1 and W2.
2. **Recap** — 1 paragraph: what we covered in W1; how W2 builds on it.
3. **Required setup (assumes W1 prep is done):**
   - Confirm Claude Code + VSCode extension + superpowers still working from W1.
   - Clone or `git pull` this repo: `git clone <url>` or `git pull origin solution`.
   - Run the PromptCraft app once to verify it works: `streamlit run promptcraft/app.py`.
4. **Optional setup (we'll demo these live; install ahead if you want to follow along):**
   - Context7 MCP — link + install command.
   - GitHub MCP — link + install command + auth setup.
5. **For the 90-min bonus (optional):**
   - Snowflake sandbox access — request from your client/IT well in advance.
   - The Snowflake MCP install will be demoed live; you don't need to pre-install.
6. **Pre-read (optional)** — `guide/02-tutorial.md` for context on the PromptCraft project we'll extend.
7. **Troubleshooting FAQ** — extend W1's FAQ with MCP-specific issues.

- [ ] **Step 2: Verify file**

Run: `wc -l docs/superpowers/workshops/pre-workshop-w2.md`
Expected: at least 40 lines.

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/workshops/pre-workshop-w2.md
git commit -m "docs(workshops): add pre-workshop W2 attendee checklist"
```

---

### Task 16: Write rehearsal checklist + risk register

**Files:**
- Create: `docs/superpowers/workshops/rehearsal-checklist.md`

- [ ] **Step 1: Write rehearsal checklist**

Create `docs/superpowers/workshops/rehearsal-checklist.md` containing:

1. **Purpose** — why dry-run before delivery; what "rehearsed" means.
2. **One-week-before checklist:**
   - Confirm presenters and roles.
   - Confirm pre-workshop materials sent to attendees.
   - Confirm Snowflake sandbox provisioned (W2 bonus).
   - Confirm API key budget cleared for live demos.
3. **Three-days-before — full dry run:**
   - Run W1 end-to-end timing: theory parts + both demos. Note actual times vs. budget.
   - Run W2 end-to-end timing.
   - For each demo, capture a backup screen recording in case live fails.
   - For W1 Demo 2: confirm visual companion offer triggers reliably with the magic prompts. If not, either tune the steering question or commit to using the fallback narration.
   - For W2 Demo 1: capture the vanilla-vs-Context7 contrast in a screenshot pair as backup.
4. **Day-of checklist:**
   - VSCode windows pre-arranged per each demo's setup state.
   - Browser tabs for visual companion ready.
   - Solution branch + workshop-w1-demo + workshop-w2-demo branches all checked out and verified.
   - Streamlit can run.
   - All MCPs that the demo *uses* (not installs live) already authenticated.
   - Phone on silent. Notifications muted.
5. **Risk register — consolidated from all demo scripts:**
   - Each demo's known failure modes, with the fallback for each.
   - "Demo derails entirely" universal fallback: pivot to slides + narrate the recording.
6. **Live-pivot decisions:**
   - If running short on time in theory part 1: drop topic 7 (Permissions) to a quick mention.
   - If running short on time in theory part 2 (W1): merge topics 9 + 10 into a single "writing-plans + subagent-driven dev" pass.
   - If Demo 1 (either workshop) runs long: skip the second demo's setup explanation and jump straight in.
7. **Post-workshop:**
   - Capture audience questions for FAQ updates.
   - Note any demos that worked / didn't for next iteration.

- [ ] **Step 2: Verify file**

Run: `grep -c "^## " docs/superpowers/workshops/rehearsal-checklist.md`
Expected: at least 7 (one per major section).

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/workshops/rehearsal-checklist.md
git commit -m "docs(workshops): add rehearsal checklist and consolidated risk register"
```

---

### Task 17: Create W1 Demo 1 example CLAUDE.md asset

**Files:**
- Create: `demo-assets/w1-demo1-claude-md/CLAUDE.md.example`

- [ ] **Step 1: Write CLAUDE.md.example**

Create `demo-assets/w1-demo1-claude-md/CLAUDE.md.example` with the following content (this is what the presenter shows as "what /init would scaffold" if the live `/init` produces something different):

```markdown
# CLAUDE.md — Demo Project

This is an example CLAUDE.md used in Workshop 1 Demo 1.

## Project Overview

Small Python utility project. Used purely for live workshop demos.

## Build & Test Commands

- Run tests: `pytest`
- Lint: `ruff check .`
- Format: `ruff format .`

## Code Standards

- Python 3.12+
- Type hints on all public functions
- Two-space indent (just because — don't argue with the project rule)

## Architecture

- `src/utils.py` — shared helpers (date, string, validation)
- `tests/` — pytest tests, mirror src layout

## Gotchas

- Never edit migrations directly. Use the migration tool.
- The `legacy/` directory is read-only — don't modify.
```

- [ ] **Step 2: Verify file content**

Run: `cat demo-assets/w1-demo1-claude-md/CLAUDE.md.example | head -20`
Expected: shows the header and project overview.

- [ ] **Step 3: Commit**

```bash
git add demo-assets/w1-demo1-claude-md/CLAUDE.md.example
git commit -m "feat(demo-assets): add W1 Demo 1 example CLAUDE.md"
```

---

### Task 18: Create W2 Demo 2 custom skill asset

**Files:**
- Create: `demo-assets/w2-demo2-skill/.claude/skills/review-prompt-quality/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

Create `demo-assets/w2-demo2-skill/.claude/skills/review-prompt-quality/SKILL.md` with the following content:

```markdown
---
name: review-prompt-quality
description: Use when the user asks to review, critique, improve, or refine an LLM prompt — produces structured feedback on clarity, specificity, and output format
---

# Reviewing LLM Prompts

When the user shares a prompt and asks for review or improvement, produce structured feedback in this format:

## What's Working
2-3 bullet points on what the prompt does well.

## What's Vague or Missing
Identify specific issues — vague verbs ("handle", "process", "deal with"), missing output format, no examples, no constraints, ambiguous audience.

## Suggested Refinements
For each issue, give a concrete change (not "be more specific" — show the rewritten line).

## Refined Prompt
Produce a complete refined version the user can copy-paste.

Keep the tone direct. Don't pad with platitudes.
```

- [ ] **Step 2: Verify file content**

Run: `cat demo-assets/w2-demo2-skill/.claude/skills/review-prompt-quality/SKILL.md | head -10`
Expected: shows the frontmatter (name, description) and start of body.

- [ ] **Step 3: Commit**

```bash
git add demo-assets/w2-demo2-skill/
git commit -m "feat(demo-assets): add W2 Demo 2 review-prompt-quality SKILL.md"
```

---

### Task 19: Create W2 bonus Snowflake safety hook asset

**Files:**
- Create: `demo-assets/w2-bonus-snowflake-hook/settings.json.fragment`
- Create: `demo-assets/w2-bonus-snowflake-hook/safety_hook.py`
- Create: `demo-assets/w2-bonus-snowflake-hook/README.md`

- [ ] **Step 1: Write settings.json.fragment**

Create `demo-assets/w2-bonus-snowflake-hook/settings.json.fragment` with the following content:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__snowflake__.*",
        "hooks": [
          {
            "type": "command",
            "command": "python ${CLAUDE_PROJECT_DIR}/.claude/hooks/safety_hook.py"
          }
        ]
      }
    ]
  }
}
```

- [ ] **Step 2: Write safety_hook.py**

Create `demo-assets/w2-bonus-snowflake-hook/safety_hook.py` with the following content:

```python
#!/usr/bin/env python3
"""PreToolUse hook for Snowflake MCP. Blocks destructive SQL on prod-named DBs unless explicitly confirmed."""

import json
import re
import sys

DESTRUCTIVE_RE = re.compile(r"^\s*(DROP|DELETE|UPDATE|TRUNCATE|ALTER|INSERT)\b", re.IGNORECASE)
PROD_DB_RE = re.compile(r"\b(prod|production|prd)[_-]?\w*", re.IGNORECASE)
CONFIRM_TOKEN = "CONFIRM_DESTRUCTIVE"

def main():
    payload = json.load(sys.stdin)
    tool_input = payload.get("tool_input", {})
    sql = ""
    for key in ("query", "sql", "statement"):
        if key in tool_input:
            sql = tool_input[key]
            break

    if not DESTRUCTIVE_RE.search(sql):
        sys.exit(0)
    if not PROD_DB_RE.search(sql):
        sys.exit(0)
    if CONFIRM_TOKEN in sql:
        sys.exit(0)

    print(json.dumps({
        "decision": "block",
        "reason": (
            f"Destructive SQL ({DESTRUCTIVE_RE.search(sql).group(1).upper()}) "
            f"detected against a production database name. "
            f"To proceed, re-issue the query with the marker '{CONFIRM_TOKEN}' "
            f"in a comment, e.g. '-- {CONFIRM_TOKEN}'."
        )
    }))
    sys.exit(2)

if __name__ == "__main__":
    main()
```

- [ ] **Step 3: Write README.md**

Create `demo-assets/w2-bonus-snowflake-hook/README.md` with the following content:

```markdown
# Snowflake Safety Hook (W2 90-min bonus demo asset)

A `PreToolUse` hook that intercepts Snowflake MCP tool calls and blocks destructive SQL (DROP / DELETE / UPDATE / TRUNCATE / ALTER / INSERT) against database names matching `prod`, `production`, or `prd` unless the query contains a `CONFIRM_DESTRUCTIVE` marker.

## Install (during the demo)

1. Copy `safety_hook.py` to `.claude/hooks/safety_hook.py` in the demo project. Make it executable.
2. Merge `settings.json.fragment` into the project's `.claude/settings.json`.
3. Restart the Claude Code session.

## Verify

Issue this query in Claude:

```
Run: UPDATE prod_sales SET discount = 0 WHERE quarter = 'Q4'
```

Expected: hook fires, query is blocked with the override instruction.

To override:

```
Run: -- CONFIRM_DESTRUCTIVE
UPDATE prod_sales SET discount = 0 WHERE quarter = 'Q4'
```

## Customize for your client

- Adjust `PROD_DB_RE` to match your client's prod naming convention.
- Adjust `DESTRUCTIVE_RE` to add or remove statement types.
- Replace `CONFIRM_TOKEN` with your team's preferred marker.
```

- [ ] **Step 4: Verify all three files**

Run: `ls demo-assets/w2-bonus-snowflake-hook/`
Expected: shows `README.md`, `safety_hook.py`, `settings.json.fragment`.

- [ ] **Step 5: Commit**

```bash
git add demo-assets/w2-bonus-snowflake-hook/
git commit -m "feat(demo-assets): add Snowflake safety hook for W2 90-min bonus demo"
```

---

### Task 20: Create pre-staged demo branches

**Files:**
- Create branches: `workshop-w1-demo`, `workshop-w2-demo`

- [ ] **Step 1: Create workshop-w1-demo branch from master**

Run:
```bash
git checkout master
git pull
git checkout -b workshop-w1-demo
```

- [ ] **Step 2: Add a workshop-readiness marker file on workshop-w1-demo**

Create `WORKSHOP_DEMO_README.md` at repo root with:

```markdown
# Workshop 1 Demo Branch

This branch is the known-good starting state for Workshop 1's live demos.

- **Demo 1** uses the file `demo-assets/w1-demo1-claude-md/CLAUDE.md.example` as a reference for the `/init` output.
- **Demo 2** is a from-scratch live brainstorm — no setup required from this branch beyond a clean working tree.
- **90-min bonus** continues from the Demo 2 brainstorm — no extra branch state needed.

To start a demo: `git checkout workshop-w1-demo` and confirm clean working tree.
```

- [ ] **Step 3: Commit and push workshop-w1-demo**

```bash
git add WORKSHOP_DEMO_README.md
git commit -m "chore: workshop-w1-demo branch readiness marker"
git push -u origin workshop-w1-demo
```

- [ ] **Step 4: Create workshop-w2-demo branch from solution**

Run:
```bash
git checkout solution
git pull
git checkout -b workshop-w2-demo
```

- [ ] **Step 5: Add a workshop-readiness marker on workshop-w2-demo**

Create `WORKSHOP_DEMO_README.md` at repo root with:

```markdown
# Workshop 2 Demo Branch

This branch is the known-good starting state for Workshop 2's live demos. It branches from `solution` so the PromptCraft app is fully built and runnable.

## Pre-demo verification

- Confirm `streamlit run promptcraft/app.py` works.
- Confirm the API key is configured.

## Demo 1 (Context7)

- Install Context7 MCP live during the demo (per `docs/superpowers/workshops/workshop-2/demo-1-script.md`).
- Backup contrast screenshots are at `demo-assets/w2-demo1-context7-screenshots/` (capture during rehearsal).

## Demo 2 (custom skill)

- Reference the asset at `demo-assets/w2-demo2-skill/.claude/skills/review-prompt-quality/SKILL.md`.
- During the demo, type the file out live in the project's `.claude/skills/` directory.

## 90-min bonus (Snowflake + safety hook)

- Reference assets at `demo-assets/w2-bonus-snowflake-hook/`.
- Snowflake sandbox credentials must be configured before the workshop.
```

- [ ] **Step 6: Commit and push workshop-w2-demo**

```bash
git add WORKSHOP_DEMO_README.md
git commit -m "chore: workshop-w2-demo branch readiness marker"
git push -u origin workshop-w2-demo
```

- [ ] **Step 7: Return to master**

```bash
git checkout master
```

- [ ] **Step 8: Verify branches exist**

Run: `git branch -a | grep workshop`
Expected: shows `workshop-w1-demo`, `workshop-w2-demo`, and remote tracking entries.

---

### Task 21: Final verification and index file

**Files:**
- Create: `docs/superpowers/workshops/README.md`

- [ ] **Step 1: Write workshops index README**

Create `docs/superpowers/workshops/README.md` with a navigable index of every artifact:

```markdown
# Claude Code Capabilities Workshops

Two-workshop curriculum for teaching Claude Code to a consultancy audience (data scientists, data engineers, AI engineers, BI employees) for deployment-ready code.

- **Spec:** [../specs/2026-04-15-claude-code-workshops-design.md](../specs/2026-04-15-claude-code-workshops-design.md)
- **Plan:** [../plans/2026-04-15-claude-code-workshops.md](../plans/2026-04-15-claude-code-workshops.md)

## Slide deck (existing)

- [Claude Code Capabilities Workshop.pptx](Claude%20Code%20Capabilities%20Workshop.pptx) — current deck (4 framing slides + appendix)
- [Claude Code Capabilities Workshop.pdf](Claude%20Code%20Capabilities%20Workshop.pdf) — PDF export

## Slide rewrites and prompt assets

- [slide-3-rewrite.md](slide-3-rewrite.md) — corrected workshop topics slide
- [magic-prompts.md](magic-prompts.md) — engineered prompts for live demos

## Workshop 1: Using Claude Code Well

- [workshop-1/slides.md](workshop-1/slides.md) — slide-by-slide content spec
- [workshop-1/presenter-script.md](workshop-1/presenter-script.md) — full talking points
- [workshop-1/demo-1-script.md](workshop-1/demo-1-script.md) — primitives in action
- [workshop-1/demo-2-script.md](workshop-1/demo-2-script.md) — live brainstorm + reveal
- [workshop-1/bonus-demo-script.md](workshop-1/bonus-demo-script.md) — 90-min bonus (curveball + Q&A)

## Workshop 2: Power Tools + Authoring

- [workshop-2/slides.md](workshop-2/slides.md) — slide-by-slide content spec
- [workshop-2/presenter-script.md](workshop-2/presenter-script.md) — full talking points
- [workshop-2/demo-1-script.md](workshop-2/demo-1-script.md) — Context7 in PromptCraft
- [workshop-2/demo-2-script.md](workshop-2/demo-2-script.md) — custom skill authoring
- [workshop-2/bonus-demo-script.md](workshop-2/bonus-demo-script.md) — 90-min bonus (Snowflake + hook)

## Pre-workshop attendee materials

- [pre-workshop-w1.md](pre-workshop-w1.md) — sent ~3 days before W1
- [pre-workshop-w2.md](pre-workshop-w2.md) — sent between W1 and W2

## Operational

- [rehearsal-checklist.md](rehearsal-checklist.md) — dry-run + risk register

## Demo asset files

- [../../../demo-assets/w1-demo1-claude-md/CLAUDE.md.example](../../../demo-assets/w1-demo1-claude-md/CLAUDE.md.example)
- [../../../demo-assets/w2-demo2-skill/.claude/skills/review-prompt-quality/SKILL.md](../../../demo-assets/w2-demo2-skill/.claude/skills/review-prompt-quality/SKILL.md)
- [../../../demo-assets/w2-bonus-snowflake-hook/](../../../demo-assets/w2-bonus-snowflake-hook/)

## Pre-staged branches

- `workshop-w1-demo` — clean state for W1 demos
- `workshop-w2-demo` — solution branch state for W2 demos
```

- [ ] **Step 2: Verify all referenced files exist**

Run:
```bash
for f in docs/superpowers/workshops/slide-3-rewrite.md \
         docs/superpowers/workshops/magic-prompts.md \
         docs/superpowers/workshops/workshop-1/slides.md \
         docs/superpowers/workshops/workshop-1/presenter-script.md \
         docs/superpowers/workshops/workshop-1/demo-1-script.md \
         docs/superpowers/workshops/workshop-1/demo-2-script.md \
         docs/superpowers/workshops/workshop-1/bonus-demo-script.md \
         docs/superpowers/workshops/workshop-2/slides.md \
         docs/superpowers/workshops/workshop-2/presenter-script.md \
         docs/superpowers/workshops/workshop-2/demo-1-script.md \
         docs/superpowers/workshops/workshop-2/demo-2-script.md \
         docs/superpowers/workshops/workshop-2/bonus-demo-script.md \
         docs/superpowers/workshops/pre-workshop-w1.md \
         docs/superpowers/workshops/pre-workshop-w2.md \
         docs/superpowers/workshops/rehearsal-checklist.md \
         demo-assets/w1-demo1-claude-md/CLAUDE.md.example \
         demo-assets/w2-demo2-skill/.claude/skills/review-prompt-quality/SKILL.md \
         demo-assets/w2-bonus-snowflake-hook/safety_hook.py \
         demo-assets/w2-bonus-snowflake-hook/settings.json.fragment \
         demo-assets/w2-bonus-snowflake-hook/README.md; do
  test -f "$f" && echo "OK: $f" || echo "MISSING: $f"
done
```
Expected: all entries print `OK:`.

- [ ] **Step 3: Verify branches exist**

Run: `git branch -a | grep -E 'workshop-w[12]-demo'`
Expected: both branch names appear (locally and on origin).

- [ ] **Step 4: Commit index README**

```bash
git add docs/superpowers/workshops/README.md
git commit -m "docs(workshops): add index README listing all workshop artifacts"
```

- [ ] **Step 5: Final summary**

Run: `git log --oneline master ^origin/master`
Expected: shows ~20 commits added in this implementation, all on master.

Print a summary of:
- Files created (count + tree)
- Branches created (`workshop-w1-demo`, `workshop-w2-demo`)
- Open follow-ups for the user (rehearsal, screenshot capture during dry-run, Snowflake sandbox provisioning — all listed in `rehearsal-checklist.md`)

---

## Spec coverage check

| Spec section | Implementing task(s) |
|---|---|
| Goal + constraints + core narrative | Embedded throughout — Tasks 4, 5, 9, 10 (presenter scripts and slide specs) |
| Capability bucketing table | Tasks 4 (W1 slides) + 9 (W2 slides) |
| Shared timing skeleton (60-min) | Tasks 4 + 9 (slide-by-slide time slots) |
| 90-min bonus skeleton | Tasks 8 (W1 bonus) + 13 (W2 bonus) |
| W1 theory part 1 (5 topics) | Task 4 slides 4-8 + Task 5 presenter script sections |
| W1 Demo 1 | Task 6 + Task 17 (CLAUDE.md asset) |
| W1 theory part 2 (5 topics) | Task 4 slides 12-16 + Task 5 presenter script sections |
| W1 Demo 2 (live brainstorm + reveal) | Task 7 + Task 3 (magic prompts) |
| W1 90-min bonus (curveball) | Task 8 + Task 3 (magic prompts) |
| W2 theory part 1 (5 topics) | Task 9 slides 4-8 + Task 10 presenter script sections |
| W2 Demo 1 (Context7) | Task 11 + Task 3 (magic prompts) |
| W2 theory part 2 (3 topics) | Task 9 slides 13-15 + Task 10 presenter script sections |
| W2 Demo 2 (custom skill) | Task 12 + Task 18 (SKILL.md asset) + Task 3 (magic prompts) |
| W2 90-min bonus (Snowflake + hook) | Task 13 + Task 19 (hook assets) + Task 3 (magic prompts) |
| Cross-workshop continuity | Task 20 (pre-staged branches) + Task 21 (index) |
| Pre-workshop materials | Tasks 14 (W1) + 15 (W2) |
| Slide deck deltas — slide 3 rewrite | Task 2 |
| Open questions to resolve | Task 16 (rehearsal checklist surfaces these) |
| Out of scope | Honored — no Agent SDK, no plugin authoring deep dive |
