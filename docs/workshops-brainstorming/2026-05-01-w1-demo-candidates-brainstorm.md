# Workshop 1 Demo Project — Candidate Brainstorm

**Date:** 2026-05-01
**Author:** James Irving + Claude (Opus 4.7)
**Status:** Brainstorm — no decision committed yet

## Context

Workshop 1 of a Claude Code workshop series is being prepared for a consultancy
audience (data scientists, data engineers, AI engineers, BI folks). The pivotal
pedagogical moment is **planning the same demo project twice**:

1. First using plain Claude Code plan mode (showing the failure modes of ad-hoc
   prompting).
2. Then using the superpowers plugin's brainstorming + writing-plans +
   subagent-driven-development workflow (showing the discipline).

The contrast must be striking. This document brainstorms candidate demo
projects for that slot, plus considers how each candidate would extend into
Workshop 2 (MCP integration, custom skill, safety hook).

The existing canonical demo across both workshops is **PromptCraft** (a
Streamlit prompt-refinement assistant on the repo's `solution` branch). This
brainstorm treats PromptCraft as one option among many, not a fixture.

> **Scope of this doc:** this is the *trimmed* version. A wider field of 9
> candidates was evaluated in conversation; only the candidates that appear in
> the top recommendations for interpretation A or interpretation C are
> profiled here.

---

## Background — How the rubric was derived

Before generating candidates, the brainstorming skill itself was researched so
the "what makes brainstorming better than plan mode" rubric (Section 1) was
grounded in the skill's actual mechanics, not vibes.

### What was researched

- **`superpowers/skills/brainstorming/SKILL.md`** (v5.0.7, installed locally at `~/.claude/plugins/cache/claude-plugins-official/superpowers/5.0.7/skills/brainstorming/SKILL.md`) — the skill's full prompt and mandatory checklist.
- **`superpowers/skills/brainstorming/visual-companion.md`** — the detailed guide for the visual companion's behaviour and triggers.
- **`superpowers/skills/writing-plans/SKILL.md`** — what the brainstorming skill hands off to.
- **`superpowers/skills/subagent-driven-development/SKILL.md`** — the implementation step after writing-plans.
- The **PromptCraft repo state** and **existing workshop materials** (W1/W2 scripts, magic-prompts.md, design spec) to understand the baseline this brainstorm is replacing or augmenting.

### The brainstorming skill, in mechanics

The skill enforces a **HARD-GATE**: no implementation skill may be invoked, no
code written, no project scaffolded, until a design has been presented and the
user has approved it. This applies even to "simple" projects — the skill's
own "This Is Too Simple To Need A Design" anti-pattern explicitly covers
todo lists, single-function utilities, config changes.

The mandatory checklist is:

1. Explore project context (files, docs, recent commits) before asking anything
2. Offer Visual Companion (in its own message, no other content) if upcoming questions will involve visual content
3. Ask clarifying questions **one at a time**, focused on purpose / constraints / success criteria
4. Propose **2-3 approaches** with trade-offs and a recommendation
5. Present the design in sections (architecture, components, data flow, error handling, testing), getting approval per section
6. Write the validated design to `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md` and commit it
7. Self-review the spec (placeholders, internal contradictions, scope, ambiguity) — fix inline
8. Wait for the user to review the written spec
9. Transition to writing-plans (the **only** skill that may follow brainstorming)

Key principles enforced throughout: **YAGNI ruthlessly**, **multiple-choice over
open-ended**, **incremental validation per section**, **design for isolation**
(smaller units, well-defined interfaces), and for brownfield work: **explore
existing structure first, follow existing patterns, include only targeted
improvements**.

### The visual companion, in mechanics

The visual companion is a browser-based tool — not a mode. Mechanically: a
local Node server watches a directory and serves HTML fragments with
click-to-select options; selections write to `$STATE_DIR/events` for Claude
to read on the next turn. Mockups, wireframes, A/B/C clickable layouts, and
side-by-side visual comparisons render in the browser.

The **offer is a standalone message** (no other content) made when Claude
anticipates upcoming questions will involve visual content. After the user
accepts, each subsequent question gets a per-question decision via the test:
*"would the user understand this better by seeing it than reading it?"*

- **Browser:** mockups, wireframes, layout comparisons, architecture diagrams, side-by-side visual designs.
- **Terminal:** requirements questions, conceptual choices, tradeoff lists, A/B/C/D text options, scope decisions.

A question about a UI topic is **not automatically a visual question** — the
test is whether the *content* is visual, not whether the *subject* is UI.

### The handoff chain

Brainstorming → writing-plans → subagent-driven-development. This chain is
strict: brainstorming may invoke *only* writing-plans (not frontend-design,
mcp-builder, or any other implementation skill). writing-plans then produces
a numbered task list that subagent-driven-development executes one task at a
time in fresh subagents with two-stage review gates (functional + code-quality)
between tasks. The whole chain produces a dated spec doc, a dated plan doc,
and per-task review artifacts — every step leaves a reviewable artifact in
git.

This matters for the rubric because it explains why brainstorming's
"output a committed design doc" criterion is load-bearing: the spec is the
input contract for everything downstream. A vague spec produces a vague plan
produces buggy implementation.

### Where brainstorming does NOT add value over plan mode

Worth saying explicitly so the rubric isn't one-sided:

- Trivial single-function bug fixes
- One-line config tweaks
- Mechanical refactors with an obvious target (rename, extract method)
- Work where the user has already written a spec themselves

The skill's own anti-pattern section concedes the design can be "a few
sentences" for genuinely simple work — but the gate is still mandatory. The
overhead is real even when the contrast with plan mode is small.

### How this maps to the rubric (Section 1)

The five things plan mode structurally cannot do — intent interrogation,
multi-architecture trade-offs, scope decomposition, visual companion, and the
self-reviewed committed spec — come directly from the checklist above. The
demo-relevant scoring axes (architectural fork depth, visual choice strength,
consultant relatability, curveball drama, live-demo brittleness) are the
projection of those mechanics onto the workshop's specific demo constraints
in Section 2.

---

## Section 1 — Rubric: when brainstorming meaningfully beats plan mode

### Confirmed / corrected list of project characteristics

| Characteristic | Confirmed? | Notes |
|---|---|---|
| Multiple valid architectural approaches | ✅ | Skill *mandates* 2-3 options with trade-offs + recommendation; plan mode commits to first plausible. |
| Easily miscommunicated requirements | ✅ | One-question-at-a-time intent interrogation before any design exists. |
| Visual/UX choice points | ✅ | Visual companion exists (browser mockups, A/B/C clickable options); offered as a standalone message when Claude anticipates visual questions. |
| Realistic scope-creep risk | ✅ | Explicit early scope-decomposition step + YAGNI principle. |

### Add to the list

- **Sectioned domain modelling** — architecture / components / data flow / errors / testing presented in sequence with per-section approval. Surfaces conceptual confusion early.
- **Reviewable artifact production** — writes a dated, git-committed spec doc, runs self-review for placeholders/contradictions, then human-gates before writing-plans.
- **Brownfield exploration discipline** — explicit instruction to read existing structure and follow existing patterns. Plan mode just plans against what's described.
- **Greenfield boundary-setting** — the "isolation and clarity" directive shapes interfaces *before* file paths get locked in.

### Rubric summary (~120 words)

Plan mode converts a *stated request* into an ordered task list. Brainstorming
converts an *idea* into a *validated, committed spec* before any planning
happens. It does five things plan mode structurally cannot: (1) interrogates
intent one question at a time instead of assuming the request is complete; (2)
surfaces 2-3 architectural alternatives with trade-offs rather than committing
to the first; (3) decomposes oversized requests into sub-project specs upfront;
(4) offers a Visual Companion that renders clickable HTML mockups in the
browser when UI choice points appear; (5) produces a dated, git-committed
design doc that self-reviews for placeholders/ambiguity/scope and then
human-reviews before writing-plans runs.

### Demo-relevant scoring axes (derived from the rubric)

- **Architectural fork depth** — how many genuinely different valid architectures exist
- **Visual choice strength** — how naturally the design forces visual mockups
- **Consultant relatability** — does every consultant in the room recognise the problem
- **Curveball drama** — how sharply a mid-implementation pivot would reframe the design
- **Live-demo brittleness** — what could flake during a live presentation

---

## Section 2 — Workshop demo constraints

Each candidate must satisfy ALL of:

1. Buildable as a small Streamlit / notebook-ish Python app (`pip install + streamlit run`)
2. ~5–6 minute live brainstorm budget before pivot to pre-built solution
3. **Must** reach a visual / UI / layout choice point during brainstorm (visual companion offer must fire)
4. Multiple plausible architectural approaches (rule-based vs LLM, sync vs async, hybrid, etc.)
5. Small enough to pre-build a `solution` branch with full spec + plan + working code (the cooked-turkey reveal)
6. Consultant-relatable (data / AI / BI consultants recognise the problem instantly)
7. At least one natural curveball-injection point for the W1 90-minute bonus demo
8. **No external services** (no DBs, no cloud, no auth — single repo, fully local)

---

## Section 3 — Candidate profiles (only those appearing in top recommendations)

### Eval Lab — *interpretation A's #1*

- **Pitch:** Paste a prompt, run it across N model configs (model × temperature × system prompt), see outputs side-by-side, mark winners, accumulate a scoreboard.
- **Architectures:** (a) Manual win-marking only; (b) LLM-as-judge with rubric; (c) both with disagreement flagging; orthogonal fork: in-memory only vs JSON-on-disk vs SQLite.
- **Visual choice point:** Comparison grid — N-column side-by-side vs tabbed vs accordion; scoreboard layout.
- **Curveball:** "Add automatic LLM-judge scoring on a custom rubric."
- **Why harder for plan mode:** Two orthogonal forks (judge type × persistence) compound — plan mode picks one path through a 2D space without acknowledging the other dimension exists.
- **W2 fit:** ★★★ Filesystem MCP for prompt/eval libraries, ★★★ Context7 for Anthropic SDK refs, ★★★ GitHub MCP for shared eval repos, ★★ rubric-author custom skill, **★★★ token-cost guardrail hook** (block runs over $X — the most natural hook in the shortlist).
- **Risk:** Comparison-panel UX overlaps PromptCraft's — if PromptCraft is also kept, audience may pattern-match.

### Insight Cards — *appears in every top recommendation*

- **Pitch:** Drop a CSV, get 3-5 auto-generated insight cards — each is a chart + a one-line LLM takeaway. The "BI starter pack."
- **Architectures:** (a) Rule-based candidate enumeration (categorical breakdowns, time series, correlations) → LLM ranks → render; (b) LLM picks columns directly from schema; (c) heuristic-only, no LLM.
- **Visual choice point:** Card grid — uniform grid vs masonry vs vertical scroll; chart-on-top vs chart-on-side; "explore deeper" affordance. **Strongest visual-companion trigger in the entire shortlist** — any honest brainstorm of card layout demands mockups.
- **Curveball:** "Add NL query — user asks for a specific insight, not just sees auto-generated ones."
- **Why harder for plan mode:** The rule-vs-LLM column-selection fork is non-obvious unless explicitly surfaced; plan mode plans the backend pipeline first and treats layout as an afterthought.
- **W2 fit:** ★★★ Filesystem MCP for CSVs, ★★ Context7 for chart-lib docs, ★★★ narration-style custom skill, ★ no obvious killer hook (the W2 weakness — would need to engineer one rather than have it fall out of the design).
- **Risk:** Live chart generation can flake (matplotlib/altair quirks under Streamlit). Mitigate by pre-vetting the demo CSV.

### CSV Sentinel — *interpretation A's #3 (balanced honourable mention)*

- **Pitch:** Drop a CSV, get an automated data-quality report — missing values, type drift, suspect outliers, plain-English narration of issues, downloadable Markdown.
- **Architectures:** (a) Pure-rule statistical (pandas-profiling-style); (b) LLM-narrated insights from rule-derived stats; (c) hybrid — rules detect, LLM explains in plain English with severity. **Cleanest triple-architecture fork in the shortlist.**
- **Visual choice point:** Report layout — single scrolling page vs tabbed (overview/columns/correlations/issues) vs sidebar drill-down.
- **Curveball:** "Actually we want to *compare two CSVs* (this week vs last week) not profile one" — completely different feature shape.
- **Why harder for plan mode:** Audience hears "CSV quality report", plan mode commits to a pandas-profiling clone in 30 seconds, missing the LLM-narration option entirely. The hybrid third option only emerges from explicit trade-off prompting.
- **W2 fit:** ★★★ Filesystem MCP for folder-of-CSVs, ★★ Context7 for pandas docs, ★★★ data-quality-rubric custom skill, ★★ PII-detection PreToolUse hook (plausible but not as crisp as Eval Lab's cost guardrail).
- **Risk:** Close to existing libs (ydata-profiling) — someone may say "why not just use the library?" Easy to deflect ("we want LLM narration tuned to this dataset's quirks").

### Customer Email Triager — *interpretation C's W2 winner (only viable under C)*

- **Pitch:** Drop a folder of customer emails, classify by issue type, auto-draft responses in the company's tone of voice.
- **Architectures:** (a) Rule-based classification (keyword); (b) zero-shot LLM classifier; (c) few-shot LLM with examples; orthogonal fork: single-classifier vs hierarchical (issue type → subtype).
- **Visual choice point:** Triage UI layout — list view vs kanban-by-category vs swipeable card stack.
- **Curveball:** "Actually we need to also auto-draft responses, not just classify."
- **Why harder for plan mode:** Classifier architecture has real cost/accuracy trade-offs; plan mode picks LLM-only and skips the keyword baseline that consultants often want for cost reasons.
- **W2 fit:** ★★★ Filesystem MCP scans the email folder (no auth needed), **★★★ company-tone-of-voice custom skill — the most natural skill fit in the entire shortlist** (every consultancy has a tone guide), **★★★ PreToolUse hook blocks drafts containing competitor names / unredacted PII / unapproved promises — the most viscerally consultant-relatable hook in the shortlist** ("we almost sent the wrong thing" stories everywhere).
- **Risk:** "Sending" must be faked (write to a file, not actually send) — minor yak-shave. **Build cost: high** — needs a fresh codebase and sample inbox.
- **Why this candidate exists only under interpretation C:** Its W1 forks are mid-strength; only worth picking when W2 can be optimised independently.

### PromptCraft — *baseline; interpretation C's pragmatic W2*

- **Pitch:** Paste a rough LLM prompt, get clarifying Qs and 2-3 refined variants with side-by-side test output.
- **Architectures:** (a) Pure-LLM iterative refinement (current); (b) rule-based template substitution; (c) hybrid — rules choose a template, LLM fills slots; sub-fork: single-shot vs multi-turn refinement.
- **Visual choice point:** Comparison panel layout — chat-style vs side-by-side columns vs diff-view.
- **Curveball:** Multi-turn refinement requirement (already wired into the W1 90-min bonus injection prompt in `magic-prompts.md`).
- **Why harder for plan mode:** Seed prompt "help refine prompts" is genuinely vague — plan mode picks the first interpretation. Single-shot vs multi-turn is the exact spec contradiction the curveball exploits.
- **W2 fit:** Already wired — Context7 MCP, custom skill, Snowflake hook all proven and documented in existing W2 materials. **Zero build cost.**
- **Risk:** Slight narrative incoherence if used as W2-only ("abandoned baseline reused for W2") — minor.

---

## Section 4 — Interpretation A: single project for both workshops, no Snowflake

### What "no Snowflake" means

Snowflake MCP would require the presenter to use a personal account during a
client-facing demo. That's off the table. The MCPs available without personal
auth are:

- **Context7** — library docs (already used in W2 Demo 1 of existing materials)
- **Filesystem** — local files
- **GitHub** — token-based, viable
- **Sequential thinking, Memory, Time, Fetch** — built-ins

Off the table without auth: Snowflake, Notion, Gmail, Calendar, Slack, Google Drive.

### Top picks for interpretation A

#### 🥇 Eval Lab — best **combined** story

- **W1 brainstorm:** two orthogonal forks (judge type × persistence) plus a comparison-grid layout question for the visual companion. Solid, not the most visual.
- **W2:** the only candidate where MCP + custom skill + hook all line up naturally. The token-cost guardrail hook is genuinely useful and immediately legible to the audience — no contrivance.
- **Curveball:** "Add automatic LLM-as-judge with a custom rubric" — forces re-brainstorm of the scoring architecture mid-implementation.
- **Trade-off:** W1 visual companion fires on a comparison grid (medium-strength visual), not on something as naturally mock-able as Insight Cards.

> *Plan mode would look* **flat** — pick a single architecture, build a comparison view, ignore the judge/persistence forks. *Superpowers would look* **structured** — surface both axes, fire the visual companion on the grid layout, produce a spec that anticipates the curveball.

#### 🥈 Insight Cards — best **W1** if you accept a weaker W2

- **W1 brainstorm:** strongest visual-companion trigger in the entire shortlist. Cleanest "wow" moment for the most important pedagogical demo.
- **W2:** Filesystem MCP for CSVs and Context7 for chart-lib docs both fit. A "narration-style" custom skill is natural. **But the hook story is weak** — there's no obvious safety check that doesn't feel contrived.
- **Trade-off:** if the W2 90-min bonus has to land hard, this candidate forces you to invent a hook rather than have one fall out of the design.

> *Plan mode would look* **blind to UX** — design the chart pipeline first, treat layout as a footnote. *Superpowers would look* **design-led** — fire the visual companion early, mock card-grid options before code is planned.

#### 🥉 CSV Sentinel — strongest **balance**, no individual peak

- W1 has the cleanest triple-architecture fork (rule / LLM-narrated / hybrid).
- W2 hook (PII detection on file reads) is plausible but not as crisp as Eval Lab's cost guardrail.
- Universal consultant magnetism is its main asset.

### Recommendation under interpretation A

If the **W2 hook demo matters as much as the W1 brainstorm**, pick **Eval Lab**.
It's the only candidate where every workshop component falls out of the design
naturally.

If the **W1 brainstorm-vs-plan moment is genuinely the most important**, pick
**Insight Cards** and accept that you'll have to engineer a W2 hook rather than
have one emerge naturally.

---

## Section 5 — Interpretation C: different projects per workshop allowed

### What C unlocks

1. **W1 can be ruthlessly optimised for the brainstorm-vs-plan-mode contrast.** Best architectural forks, hardest visual-companion trigger, cleanest curveball. No "but does this also host an MCP nicely?" trade-off.
2. **W2 can be ruthlessly optimised for the MCP / custom-skill / hook trio.** No "but does this also have a 5-min brainstorm with three valid architectures?" trade-off.

It also opens **Customer Email Triager** as a W2 candidate — previously
dismissed under interpretation A because its W1 forks are mid-strength.

### The pedagogical question first

Picking different projects for W1 and W2 isn't free — it costs a *narrative*.
Under interpretation A you get *"we built this in W1, now let's harden it in
W2."* Under C you get *"the workflow generalises across project shapes."* Both
are valid; pick deliberately:

- **A's narrative wins** if the audience is junior — they get to deepen one mental model and see it productionise.
- **C's narrative wins** if the audience might suspect *"this only works for prompt-refinement-shaped problems"* — different W1 and W2 shapes proves generality.

### Suggested pairings under C

W1 winner is **Insight Cards** in every pairing — its visual-companion trigger
and architectural forks dominate the W1-only lens. The W2 choice is the
variable.

| Pairing | W1 | W2 | Build cost | Narrative |
|---|---|---|---|---|
| **🥇 Best demo** | Insight Cards | Customer Email Triager | High (two new builds) | "Same workflow, very different problems — BI tool *and* customer ops automation" |
| **🥈 Best balance** | Insight Cards | Eval Lab | Medium-high | "Two AI/data tools, both via the same workflow" |
| **🥉 Pragmatic** | Insight Cards | PromptCraft | Low (W2 already built) | "Optimise the W1 moment, reuse the existing W2" |

### Recommendation under interpretation C

**🥇 Insight Cards + Customer Email Triager** is the strongest *demo* pair.
Insight Cards gives the most dramatic W1 visual-companion moment in the
shortlist; Customer Email Triager gives W2 the most viscerally
consultant-relatable hook. Different problem shapes (BI dashboard vs customer
ops automation) prove generality. **Cost:** Customer Email Triager would need
to be built from scratch with a fake-send affordance.

**🥉 Insight Cards + PromptCraft** is the strongest *operational* choice. Only
one new app to build (Insight Cards for W1); PromptCraft stays for W2 since
it's already wired with Context7 + skill + hook. The slight narrative
awkwardness ("baseline" → "W2-only") is real but minor.

**Tie-breaker:** how much build budget exists between now and the workshop. If
there's time to build Customer Email Triager properly, the demo lands harder.
If not, pair Insight Cards with PromptCraft and ship.

---

## Section 6 — Decision summary across both interpretations

| Interpretation | Top recommendation | Why |
|---|---|---|
| **A** (one project, both workshops, no Snowflake) | **Eval Lab** | Only candidate where W1 forks AND W2 MCP/skill/hook all line up naturally |
| **A** (W1 demo prioritised over W2) | **Insight Cards** | Strongest visual-companion trigger; weaker W2 hook story |
| **C** (different projects allowed, max budget) | **Insight Cards (W1) + Customer Email Triager (W2)** | Each demo individually optimised; proves generality |
| **C** (different projects allowed, low budget) | **Insight Cards (W1) + PromptCraft (W2)** | One new build only; reuses existing W2 work |

### The most likely shortlist for final choice

1. **Eval Lab** as a single-project cross-workshop demo (interpretation A)
2. **Insight Cards + PromptCraft** as a pragmatic split (interpretation C)
3. **Insight Cards + Customer Email Triager** as an aspirational split (interpretation C)

---

## Section 7 — Open questions and next steps

### Open questions before picking

- **How much build budget exists?** Determines whether C-aspirational is on the table.
- **Is the workshop arc more about "generality" or "depth"?** Determines A vs C.
- **How important is a strong W2 hook demo specifically?** If very, Eval Lab or Customer Email Triager are required; if not, Insight Cards opens up.
- **Is there appetite to retire PromptCraft entirely?** If yes, all three top recommendations are viable. If no, the pragmatic C split wins.

### Suggested next step

Once a candidate (or pair) is chosen, run the brainstorming skill *for real*
on it (Socratically, with the presenter as user) to produce a spec — then
writing-plans, then subagent-driven-development to pre-build the `solution`
branch. This becomes the cooked-turkey reveal for the W1 Demo 2.
