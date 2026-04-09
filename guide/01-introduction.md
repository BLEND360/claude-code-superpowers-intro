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

**To install:**

```bash
/plugin install superpowers@claude-plugins-official
```

(See the [superpowers repo](https://github.com/obra/superpowers) for other installation options including Cursor, Codex, and Gemini CLI.)

It's a collection of "skills" — modular workflows that trigger automatically when Claude recognizes a relevant situation. Start building something, and Claude will invoke brainstorming before jumping into code. Finish a task, and it triggers code review.

Sometimes Claude falls back to default behavior and skips the skill. When that happens, you can get it back on track by being explicit: **"Let's use superpowers to brainstorm this"** or **"Use superpowers to write a plan"**. Understanding what each skill does helps you notice when to nudge Claude back.

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
