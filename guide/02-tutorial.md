# Tutorial: Building PromptCraft With Superpowers

Let's build PromptCraft — a prompt engineering helper — using the superpowers workflow. We'll go through the full process: brainstorming the design, planning the implementation, and building with subagent-driven development.

This isn't a transcript of an actual session, but it's representative of how the workflow feels. The key patterns are real; the specific dialogue is condensed.

---

## Phase 1: Brainstorming the Design

We start with a rough idea: "Build a tool that helps people write better prompts."

That's not a spec. It's a direction. Brainstorming turns it into something we can actually build.

### One Question at a Time

The brainstorming skill doesn't dump a questionnaire on you. It asks one question, waits for your answer, and uses that answer to inform the next question.

**Claude:** "Who will use this tool? Data scientists exploring LLMs, AI engineers building production systems, or general users trying ChatGPT for the first time?"

**You:** "Mostly data scientists and AI engineers. People who already know what prompts are but want to write better ones."

**Claude:** "What kinds of prompts? Simple queries, complex multi-step instructions, system prompts for agents, or all of the above?"

**You:** "Primarily complex instructions — the kind where structure and clarity really matter."

Each question narrows the scope. By the tenth question, we've established:
- The audience (technical users)
- The prompt types (complex instructions)
- The analysis depth (specific, actionable feedback — not generic advice)
- The UI approach (simple Streamlit — focus on the analysis, not the interface)

### Proposing Approaches

Before settling on a design, brainstorming presents options:

**Approach A: Rule-based analysis.** Check for common issues (missing output format, vague verbs, no examples) using pattern matching. Fast, predictable, but limited.

**Approach B: LLM-based analysis.** Have Claude analyze the prompt and suggest improvements. Flexible, nuanced, but slower and less predictable.

**Approach C: Hybrid.** Rule-based checks for obvious issues, LLM analysis for deeper feedback. Best of both worlds, more complexity.

Each approach comes with trade-offs. Rule-based is faster to build but less capable. Full LLM is more powerful but harder to test. Hybrid is the most capable but takes longer.

For PromptCraft, we choose **Approach C (hybrid)**. The rule-based layer catches obvious issues immediately; the LLM layer provides nuanced suggestions.

### The Validated Design

By the end of brainstorming, we have:

- **Core features:** Input area, rule-based analysis, LLM-based suggestions, refined output display
- **UI framework:** Streamlit (simple, data-science-friendly)
- **Analysis approach:** Hybrid (rules + LLM)
- **Excluded (YAGNI):** Prompt history, multiple LLM providers, user accounts

This isn't a vague direction anymore. It's a design we can implement.

**Key takeaway:** We haven't written a line of code, but we've already avoided the biggest risks — building the wrong thing, over-engineering, scope creep. The brainstorming skill made us answer hard questions before they became expensive.

---

## Phase 2: From Design to Plan

With a validated design, we transition to planning. The writing-plans skill takes the design and breaks it into bite-sized tasks.

Each task is specific:
- Exact files to create or modify
- The code to write (or in our case, the content to produce)
- How to test it
- When to commit

For PromptCraft, the plan might break down into:

1. **Set up Streamlit app skeleton** — Basic UI with input area
2. **Implement rule-based analyzer** — Pattern matching for common issues
3. **Add LLM analysis integration** — Claude API call with prompt template
4. **Build suggestion display** — Format and present feedback
5. **Create refined prompt output** — Generate improved version

Each task stands alone. You can complete task 1 without knowing the details of task 5. This independence is deliberate — it's what makes subagent-driven development possible.

**Key takeaway:** The plan isn't just a to-do list. It's a contract between the designer (you, during brainstorming) and the implementers (subagents, during development). Clear plans prevent drift.

---

## Phase 3: Subagent-Driven Development

Now we build. But instead of one long session where context accumulates and confusion grows, we use subagent-driven development.

### Fresh Agents Per Task

For each task in our plan, Claude dispatches a fresh subagent — an implementer with no prior context. The controller (Claude in your main session) provides exactly what the implementer needs:

- The task description from the plan
- Relevant code snippets and file contents
- Project conventions and constraints

The implementer doesn't inherit your session's history. It can't get confused by decisions you made three hours ago that no longer apply. It gets clean context, does its job, and reports back.

### The Two-Stage Review

After the implementer finishes, two reviewers check the work:

**Stage 1: Spec Compliance**
- Did the code do what the spec asked?
- Is anything missing?
- Is there scope creep (features that weren't requested)?

This isn't about code quality yet — it's about correctness. If the spec said "display suggestions as a bulleted list" and the implementer used a numbered list, that's a spec compliance issue.

**Stage 2: Code Quality**
- Is the code well-structured?
- Are there edge cases missed?
- Any security concerns, performance issues, or maintainability problems?

Only after passing spec compliance do we check code quality. This order matters — there's no point polishing code that doesn't meet requirements.

### Handling Feedback (Receiving Code Review)

Here's where many developers — and AI assistants — go wrong. When a reviewer says "this function should handle empty inputs," the temptation is to respond with "You're absolutely right! Let me fix that."

That's performative agreement. It feels collaborative but skips the critical step: verification.

The receiving-code-review skill enforces a different pattern:

1. **Read** the feedback completely
2. **Restate** the requirement in your own words
3. **Verify** against the actual codebase — is this a real issue?
4. **Respond** with technical acknowledgment or reasoned pushback
5. **Implement** if the feedback is valid

Sometimes the reviewer is wrong. Maybe empty inputs are already handled upstream. Maybe the suggested change would break something else. Verification catches these cases before you implement bad advice.

### The Feedback Loop

When reviews find issues, the implementer fixes them — and the reviewer reviews again. This loop continues until the review passes:

```
Implement → Review → Issues found → Fix → Re-review → Pass
```

It sounds slow. In practice, it's faster than the alternative: shipping buggy code, discovering issues in production, context-switching back to fix them weeks later.

### What If You're Blocked?

Not every task goes smoothly. The implementer might report:

- **NEEDS_CONTEXT:** Missing information. The controller provides it and re-dispatches.
- **BLOCKED:** Can't complete the task. Maybe the spec is wrong, maybe the task is too complex.

When blocked, the workflow doesn't force ahead. It escalates to you. Maybe the task needs to be broken down. Maybe the plan needs revision. Maybe you need to go back to brainstorming.

**Key takeaway:** Subagent-driven development trades session continuity for clarity. Fresh context per task, systematic review, explicit escalation when stuck. The result is higher quality with less cognitive load.

---

## Wrap-Up: What We Built and What We Avoided

We've walked through building PromptCraft using the superpowers workflow. Let's recap what the structured approach gave us:

### What We Built
- A validated design (not a vague idea)
- A clear plan (not a mental to-do list)
- Reviewed code (not "it looks right to me")

### What We Avoided
- **Requirements drift** — Brainstorming locked in decisions before they became expensive to change
- **Context pollution** — Fresh subagents per task meant no accumulated confusion
- **Review theater** — Two-stage review with verification, not rubber-stamping
- **Forcing through blockers** — Escalation paths when things went wrong

### The Flexibility You Keep

Superpowers isn't a rigid pipeline that traps you. If a major new requirement emerges during implementation, subagents escalate rather than forcing ahead. You can redirect to brainstorming or planning when needed.

The workflow adapts to reality, not the other way around.

---

## Quick Reference

### When to Use Each Skill

| Skill | Use When... |
|-------|-------------|
| **Brainstorming** | Starting any new feature, project, or significant change. Always brainstorm before coding. |
| **Code Review (Requesting)** | After completing a task, before merging, or when you want a fresh perspective. |
| **Code Review (Receiving)** | When you get feedback. Verify before implementing. Push back when appropriate. |
| **Subagent-Driven Development** | Executing a plan with multiple independent tasks. Keeps context clean, enables systematic review. |

### Key Principles

- **One question at a time** — Don't overwhelm. Brainstorming is dialogue, not interrogation.
- **Verify before implementing** — Feedback might be wrong. Check the codebase.
- **Fresh context per task** — Let subagents start clean. Don't inherit confusion.
- **Two-stage review** — Spec compliance first, code quality second.
- **Escalate when blocked** — Don't force through. Surface problems early.

### Try It Yourself

1. Install the superpowers plugin: see the [superpowers repo](https://github.com/obra/superpowers)
2. Start your next project with "Let's brainstorm this"
3. Watch how the workflow guides you from idea to implementation

The patterns feel different at first. After a few projects, they become second nature — and you'll wonder how you ever worked without them.
