# Magic Prompts — Engineered Demo Prompts for Workshop Presenters

These prompts are carefully engineered to trigger high-likelihood superpowers behavior in live demos. Because model output is non-deterministic, **rehearsal is required** before every workshop session. Run through each prompt at least twice in a fresh session to confirm the expected behavior fires. If a demo depends on a specific response shape, note the fallback narration below.

---

## What These Are

These are not generic prompts — they are structured inputs that reliably activate specific Claude Code superpowers behaviors (brainstorming, visual companions, re-planning, skill invocation, safety hooks) given the current model and skill configuration. Each prompt has been tested against the workshop setup described in the demo scripts.

Treat these as **presenter scripts**, not suggestions. Deviating from the verbatim text — even slightly — can change which behavior fires. The "Why this works" notes explain the engineering so you can adapt intelligently if you must improvise.

---

## W1 Demo 2 — Brainstorm Seed Prompt

### Verbatim prompt

```
Let's use superpowers to brainstorm a tool that helps people write better LLM prompts. The audience is data scientists and AI engineers.
```

### Why this works

The phrase "build a tool" reliably triggers the `superpowers:brainstorming` skill because the skill's trigger condition matches creative/feature work requests. "Let's use superpowers" reinforces the signal in case the auto-trigger needs a nudge. Naming a concrete audience — data scientists and AI engineers — steers Claude toward concrete, scoped questions immediately rather than open-ended ones, which makes the first exchange feel purposeful to a live audience.

### Expected first 2–3 questions Claude will ask

During rehearsal, Claude typically opens with questions in this cluster. The presenter should have answers ready so the exchange feels natural:

1. **Who is the user / what is their workflow?** (e.g., are they writing prompts inline in a notebook, in a dedicated UI, or via API?)
2. **What kinds of prompts?** (simple single-turn queries vs. complex multi-step or agentic chains — this steers toward the right analysis depth)
3. **What level of analysis depth / feedback granularity?** (quick lint-style flags vs. detailed rewrite suggestions)
4. **UI framework preference?** (Streamlit, Gradio, CLI, VS Code extension — relevant because the audience is technical)

Having a crisp answer like "notebook-first, multi-step prompts, detailed rewrites, Streamlit" ready lets the presenter move through the brainstorm quickly and reach the visual companion offer within the demo time window.

---

## W1 Demo 2 — Visual Companion Steering Question

### Verbatim steering answer

```
Show me side-by-side comparison vs stacked diff vs tabbed view options for the refined prompt display — I want to actually see what each looks like.
```

### Why this works

The explicit ask for visual comparison — "I want to actually see what each looks like" — gives Claude a clear signal that a browser-based visual companion is the appropriate next step. Listing three concrete layout options (side-by-side, stacked diff, tabbed) makes the request feel specific enough that the visual companion skill has something concrete to render, which increases the likelihood the offer fires rather than Claude producing a text description of the layouts.

### Fallback narration

If the visual companion offer does not fire (i.e., Claude produces a text description instead of offering to open a browser companion), the presenter says:

> In a longer session here, brainstorming would offer to spin up a browser companion to show these layouts side by side. Let me show you what that looks like with a screenshot.

**Note:** A fallback screenshot showing the visual companion with the three layout options must be captured during rehearsal and kept accessible (e.g., in a pinned browser tab or the presenter's second monitor).

---

## W1 90-Min Bonus — Curveball Injection Prompt

### Verbatim curveball

```
Hold on — I just talked to a stakeholder. They actually need this tool to also support multi-turn refinement, where the user iterates with the assistant 3-4 times. This contradicts the single-shot design we planned. Adjust.
```

### Why this works

The explicit contradiction signal ("this contradicts the single-shot design we planned") is the key phrase. It triggers superpowers' re-brainstorm or re-plan behavior rather than causing Claude to bolt new functionality onto the existing design as a kludge. Without that explicit contradiction framing, Claude tends to append multi-turn support as an afterthought. With it, Claude typically surfaces the architectural implications (state management, session continuity, UI changes) and offers a revised plan — which is the behavior the bonus demo is illustrating.

---

## W2 Demo 1 — Context7 Contrast Prompts

### Vanilla prompt (no Context7)

```
What's the recommended way to display Streamlit dataframes with row selection in the latest Streamlit?
```

**Expected behavior:** Claude produces guidance based on its training cutoff, which is likely stale. Row selection in Streamlit dataframes has changed across versions; the model may cite an older `AgGrid` workaround or omit the native `st.dataframe` selection parameter introduced in a recent release.

### Same prompt with Context7 enabled

Use the identical prompt text above, but with Context7 active in the session. Claude should cite current Streamlit documentation with version numbers and accurate API signatures.

### Backup queries

Have 2–3 backup recently-changed Streamlit feature queries ready in case the chosen prompt happens to produce a current answer (the model's training data sometimes catches recent releases):

1. `What's the current syntax for st.dialog in Streamlit, and when was it introduced?`
2. `How do I use Streamlit's native fragment rerun feature introduced in 1.33?`

---

## W2 Demo 2 — Custom Skill Trigger Prompt

### Verbatim prompt (use in a fresh session after installing the skill)

```
Can you review this prompt for me and suggest improvements? "Generate a summary of the document."
```

### Expected behavior

The status line should display the skill being invoked, something like `Using ...review-prompt-quality`. The exact display name depends on the `name` field in the skill file's metadata — check the installed skill file to confirm the label before demoing.

### Fallback: explicit invocation

If the auto-trigger does not fire (status line shows normal processing, no skill invocation), use this explicit invocation prompt:

```
Use the review-prompt-quality skill to review this prompt: "Generate a summary of the document."
```

This bypasses the auto-trigger and invokes the skill directly, which still demonstrates the skill's output even if the automatic detection didn't fire.

---

## W2 Bonus — Snowflake Destructive-Query Safety Hook Trigger

### Verbatim prompt (use after installing the safety hook)

```
Run an UPDATE on the prod_sales table to set discount=0 for last quarter.
```

### Expected behavior

The safety hook intercepts the query before execution and requires explicit confirmation. The presenter should **not** confirm — the point of the demo is showing the interception, not completing the update.

### Override pattern

If the demo needs to show the full confirmation flow, the override pattern uses a `CONFIRM_DESTRUCTIVE` marker as specified in the hook definition. Refer to the hook spec for the exact syntax. Do not demo the confirmed execution against a live production table.
