# Superpowers How-To Guide Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a how-to guide introducing the superpowers plugin for Claude Code, targeting data scientists and AI engineers.

**Architecture:** Three markdown files — README as entry point, introduction for context, tutorial for hands-on narrative. Blog-style tone throughout. Uses "PromptCraft" (a prompt engineering helper) as the running example.

**Tech Stack:** Markdown only. No code dependencies.

---

## File Structure

```
claude-code-superpowers-intro/
├── README.md                    # Entry point (~150-200 words)
├── guide/
│   ├── 01-introduction.md       # What and why (500-700 words)
│   └── 02-tutorial.md           # Hands-on narrative (1500-2000 words)
└── docs/superpowers/
    ├── specs/
    │   └── 2026-04-09-superpowers-guide-design.md  # (exists)
    └── plans/
        └── 2026-04-09-superpowers-guide.md         # (this file)
```

---

### Task 1: Create README.md

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write README content**

Create `README.md` with the following content:

```markdown
# Superpowers for Claude Code: A Practical Guide

This guide introduces the [superpowers](https://github.com/obra/superpowers) plugin for Claude Code — a collection of skills that bring structured workflows to AI-assisted development.

## Who This Is For

- **Data scientists** building LLM-powered tools and pipelines
- **AI engineers** working with Claude Code daily
- Both newcomers to AI-assisted coding and experienced users looking to level up

## What You'll Learn

Three key skills that transform chaotic prompting into systematic development:

1. **Brainstorming** — Turn rough ideas into validated designs before writing code
2. **Code Review** — Systematic review with technical rigor (not performative agreement)
3. **Subagent-Driven Development** — Fresh agents per task with two-stage review

## Start Here

1. [Introduction](guide/01-introduction.md) — Why structured workflows matter
2. [Tutorial](guide/02-tutorial.md) — Build a prompt engineering helper step-by-step

## The Example Project

Throughout this guide, we build **PromptCraft** — a Streamlit app that helps refine LLM prompts. It's meta (using Claude to build Claude tools), practical, and demonstrates all three skills in action.
```

- [ ] **Step 2: Commit README**

```bash
git add README.md
git commit -m "Add README with guide overview and navigation"
```

---

### Task 2: Write Introduction (01-introduction.md)

**Files:**
- Create: `guide/01-introduction.md`

- [ ] **Step 1: Write the introduction content**

Create `guide/01-introduction.md` with the following content (500-700 words):

```markdown
# Introduction: Why Structured Workflows Matter

## The Problem With Ad-Hoc AI-Assisted Coding

You know the pattern. You start with a simple request: "Help me build a data validation script." Claude gives you something. It's close, but not quite right. You clarify. It fixes one thing, breaks another. Three prompts later, you're debugging code you didn't write and don't fully understand. Ten prompts after that, you've lost track of what you even asked for.

This isn't Claude's fault. It's the nature of ad-hoc prompting:

- **Context loss** — Each prompt starts fresh. Claude doesn't remember the architectural decisions you made five messages ago.
- **Unclear requirements** — "Make it better" isn't a spec. Neither is "add error handling." What errors? Handle them how?
- **No review process** — Code ships the moment it looks right. Edge cases lurk. Bugs compound.
- **The "just one more prompt" spiral** — Small fixes pile up. Before you know it, you've spent an hour on what should have been a 15-minute task.

If this sounds familiar, you're not alone. Most developers using AI assistants hit these walls daily.

## Enter Superpowers

[Superpowers](https://github.com/obra/superpowers) is a plugin for Claude Code that adds structured workflows to your development process. Think of it as guardrails, not restrictions — patterns that make you faster by preventing the chaos described above.

It's a collection of "skills" — modular workflows that Claude invokes when appropriate. You don't have to memorize them; Claude knows when to use them. But understanding what they do helps you get the most out of them.

This guide focuses on three skills that transform how you work:

### 1. Brainstorming

Before any code is written, brainstorming guides you through a structured design dialogue. One question at a time. Multiple approaches with trade-offs. A validated design before implementation begins.

**The key insight:** Most project failures aren't technical — they're requirements failures. Brainstorming surfaces assumptions early, when they're cheap to fix.

### 2. Code Review (Requesting + Receiving)

Superpowers includes two complementary code review skills:

- **Requesting reviews** dispatches a reviewer with proper context — what was built, what the spec says, which commits to examine.
- **Receiving reviews** handles feedback with technical rigor. No performative agreement ("You're absolutely right!"). Instead: verify the feedback against the actual codebase, push back when the reviewer is wrong, implement when they're right.

**The key insight:** Code review isn't about approval. It's about catching issues before they compound.

### 3. Subagent-Driven Development

For implementation, superpowers dispatches fresh subagents — one per task. Each agent gets exactly the context it needs, completes its work, and undergoes two-stage review: first for spec compliance (did it build what was asked?), then for code quality.

**The key insight:** Fresh context per task prevents the confusion that builds up in long sessions. Systematic review catches issues while they're still small.

## What We're Building: PromptCraft

Throughout this guide, we'll build **PromptCraft** — a Streamlit app that helps users refine their LLM prompts.

The user pastes a prompt, describes what they're trying to accomplish, and PromptCraft analyzes it: identifying vague instructions, missing context, ambiguous output formats. It offers specific suggestions with explanations, then presents a refined prompt ready to copy.

Why this example?

- **You write prompts every day.** This tool solves a real problem you have.
- **It's meta.** We're using Claude Code with superpowers to build a tool that helps people work with Claude. The recursion is intentional.
- **It's the right size.** Complex enough to show why structured workflows matter, simple enough to follow in a tutorial.

Let's build it.
```

- [ ] **Step 2: Commit introduction**

```bash
git add guide/01-introduction.md
git commit -m "Add introduction explaining superpowers value proposition"
```

---

### Task 3: Write Tutorial Part 1 — Brainstorming Phase (02-tutorial.md)

**Files:**
- Create: `guide/02-tutorial.md`

- [ ] **Step 1: Write the brainstorming section**

Create `guide/02-tutorial.md` with the following content (this task covers ~600 words, more content will be appended in subsequent tasks):

```markdown
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
```

- [ ] **Step 2: Commit brainstorming section**

```bash
git add guide/02-tutorial.md
git commit -m "Add tutorial brainstorming phase"
```

---

### Task 4: Write Tutorial Part 2 — Planning Phase (02-tutorial.md)

**Files:**
- Modify: `guide/02-tutorial.md` (append to end)

- [ ] **Step 1: Append the planning section**

Append the following content to `guide/02-tutorial.md` (~200 words):

```markdown

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
```

- [ ] **Step 2: Commit planning section**

```bash
git add guide/02-tutorial.md
git commit -m "Add tutorial planning phase"
```

---

### Task 5: Write Tutorial Part 3 — Subagent-Driven Development (02-tutorial.md)

**Files:**
- Modify: `guide/02-tutorial.md` (append to end)

- [ ] **Step 1: Append the subagent development section**

Append the following content to `guide/02-tutorial.md` (~600 words):

```markdown

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
```

- [ ] **Step 2: Commit subagent development section**

```bash
git add guide/02-tutorial.md
git commit -m "Add tutorial subagent-driven development phase"
```

---

### Task 6: Write Tutorial Part 4 — Wrap-up and Quick Reference (02-tutorial.md)

**Files:**
- Modify: `guide/02-tutorial.md` (append to end)

- [ ] **Step 1: Append wrap-up and quick reference**

Append the following content to `guide/02-tutorial.md` (~400 words):

```markdown

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
```

- [ ] **Step 2: Commit wrap-up and quick reference**

```bash
git add guide/02-tutorial.md
git commit -m "Add tutorial wrap-up and quick reference"
```

---

## Self-Review Checklist

**1. Spec coverage:**
- ✓ README with overview and navigation
- ✓ Introduction (500-700 words) with hook, superpowers overview, three skills, PromptCraft intro
- ✓ Tutorial brainstorming phase with one-question-at-a-time, approaches, validated design
- ✓ Tutorial planning phase with transition to tasks
- ✓ Tutorial subagent development with two-stage review, feedback handling, escalation
- ✓ Wrap-up with what we built/avoided, flexibility message
- ✓ Quick reference with skill table, principles, try-it-yourself

**2. Placeholder scan:** No TBD, TODO, or vague steps. All content is fully specified.

**3. Consistency:** File paths match throughout. Skill names are consistent. PromptCraft example threads through all sections.

---

All spec requirements covered. Plan complete.
