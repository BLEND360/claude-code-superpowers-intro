# Superpowers Plugin How-To Guide — Design Spec

**Date:** 2026-04-09
**Status:** Approved
**Repository:** claude-code-superpowers-intro

---

## Overview

A how-to guide introducing the superpowers plugin for Claude Code, focusing on three key skills: brainstorming, code review (requesting + receiving), and subagent-driven development.

## Goals

1. Help team members (data scientists and AI engineers) adopt the superpowers plugin
2. Show the value of structured workflows through a hands-on narrative
3. Enable readers to apply these skills to their own work

## Target Audience

- **Primary:** Professional data scientists and AI engineers
- **Experience levels:** Both newcomers to AI-assisted coding and experienced Claude Code users
- **What they need:** Foundational context for newcomers, workflow improvements for experienced users

## Success Criteria

- Reader understands why structured workflows beat ad-hoc prompting
- Reader can apply brainstorming, code review, and subagent-driven development to their own work
- Reader feels motivated to try superpowers on their next project

## Format and Tone

- **Format:** Blog-style introduction followed by hands-on tutorial ("Day in the Life" narrative)
- **Tone:** Conversational, opinionated, story-driven — like a good blog post, not dry documentation
- **Use case:** Internal team resource with blog readability

## Example Project: PromptCraft

A Streamlit app that helps users refine their prompts for LLM tasks.

### Core Features

1. **Input area** — User pastes their initial prompt and describes what they're trying to accomplish
2. **Analysis** — The tool identifies issues (vague instructions, missing context, ambiguous output format)
3. **Suggestions** — Offers specific improvements with explanations
4. **Refined output** — Shows the improved prompt, ready to copy

### Why This Example

- Relatable to both data scientists and AI engineers (everyone writes prompts)
- Shows brainstorming value — "What makes a good prompt analysis?" has real design questions
- Shows code review value — Prompt templates and LLM integration benefit from systematic review
- Shows subagent value — Natural task breakdown: UI, analysis logic, LLM integration, prompt templates
- Meta appeal — Using Claude Code to build a tool that helps people work with Claude

### Excluded (YAGNI)

- Prompt history/saving
- Multiple LLM provider support
- User accounts
- Prompt templates library

## Document Structure

### Part 1: Introduction (500-700 words)

**File:** `guide/01-introduction.md`

Contents:
- **Hook:** The problem with ad-hoc AI-assisted coding — context loss, unclear requirements, no review process, "just one more prompt" spirals
- **What is superpowers:** A plugin that adds structured workflows to Claude Code — not restrictions, but guardrails that make you faster
- **The three skills:** Brainstorming, code review (requesting + receiving), subagent-driven development
- **What we're building:** A prompt engineering helper in Streamlit — and why this example matters

### Part 2: Tutorial (1500-2000 words)

**File:** `guide/02-tutorial.md`

Follows the natural workflow in real-time:

1. **Brainstorming phase**
   - Show the one-question-at-a-time approach
   - Show proposing 2-3 approaches with trade-offs
   - End with a validated design
   - Key takeaway: Brainstorming surfaces assumptions and prevents building the wrong thing

2. **Planning phase**
   - Brief mention of writing-plans skill (bridges brainstorming to implementation)
   - Show transition from design to actionable tasks

3. **Subagent-driven development phase**
   - Breaking the project into independent tasks
   - Dispatching implementer subagents with full context
   - Two-stage review: spec compliance first, then code quality
   - Handling feedback with technical rigor (receiving-code-review patterns)
   - The feedback loop: fix → re-review → repeat until approved
   - Key takeaway: Fresh context per task + systematic review = higher quality with less cognitive load

4. **Wrap-up**
   - What we built
   - How the workflow prevented common pitfalls
   - Flexibility message: Escalation points let you pivot back to brainstorming or planning when new requirements emerge

### Part 3: Quick Reference (200-300 words)

Included at the end of `guide/02-tutorial.md`:

- When to use each skill
- Links to full skill documentation
- "Try it yourself" call to action

## Skills Coverage

### Brainstorming

**What to show:**
- Exploring what "prompt engineering helper" actually means
- Asking clarifying questions one at a time
- Proposing 2-3 approaches (e.g., rule-based vs. LLM-based vs. hybrid analysis)
- Arriving at a validated design before any code

**Key message:** Brainstorming surfaces assumptions and prevents building the wrong thing.

### Code Review (Requesting + Receiving)

**What to show:**
- Requesting: Dispatch reviewer with proper context (what was built, spec reference, git range)
- Receiving: Handle feedback with technical rigor — restate requirements, verify against codebase, push back when appropriate
- Anti-pattern: Performative agreement ("You're absolutely right!")

**Key message:** Code review catches issues before they compound; receiving feedback is a skill, not just acceptance.

### Subagent-Driven Development

**What to show:**
- Breaking work into independent tasks
- Dispatching implementers with full context (not making them read files)
- Two-stage review: spec compliance first, then code quality
- Handling statuses: DONE, DONE_WITH_CONCERNS, NEEDS_CONTEXT, BLOCKED
- The feedback loop until approved

**Key message:** Fresh context per task + systematic review = higher quality with less cognitive load.

## Flexibility and Escalation

The guide will emphasize that superpowers doesn't trap you in a rigid pipeline:

- Subagents escalate blockers (BLOCKED status) rather than forcing ahead
- If the plan is wrong, escalate to the human
- The human can redirect to brainstorming or planning when major new requirements emerge
- The workflow adapts to reality, not the other way around

## Deliverables

```
claude-code-superpowers-intro/
├── README.md                    # Overview and how to use this guide
├── guide/
│   ├── 01-introduction.md       # The "what and why" intro (500-700 words)
│   └── 02-tutorial.md           # The hands-on narrative (1500-2000 words)
└── docs/
    └── superpowers/
        └── specs/
            └── 2026-04-09-superpowers-guide-design.md   # This design doc
```

**Total word count:** ~2500-3000 words across guide files

## Not Included

- The actual PromptCraft Streamlit app code (the guide describes building it, doesn't ship it)
- Video or screenshots (text-only for now)
- Translations
