# PromptCraft — Design Spec

**Date:** 2026-04-10
**Status:** Draft

## Overview

PromptCraft is a Streamlit app that helps users refine their LLM prompts through iterative dialogue with Claude. Users paste a rough prompt, Claude asks clarifying questions and generates improved variants, and users can compare original vs. refined prompt outputs side-by-side.

## Goals

- Help both beginners and intermediate users write better prompts
- Make the value of prompt refinement tangible through side-by-side comparison
- Provide an iterative, conversational refinement experience (not one-shot)
- Keep the app simple — single page, minimal dependencies

## Target Users

- **Beginners:** People new to LLMs who need guidance on prompt engineering concepts
- **Intermediate:** Developers and data scientists who use LLMs regularly but want to level up

The app adapts its guidance depth based on a user-selected skill level.

## Architecture

### Single-Page Streamlit App

Four Python modules:

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit app — layout, UI sections, session state management |
| `refiner.py` | Core logic — builds prompts for Claude to analyze/improve user prompts, parses responses |
| `api_client.py` | Thin wrapper around the Anthropic SDK — handles API calls, error handling, streaming |
| `config.py` | Constants — model name, max tokens, system prompts, skill-level presets |

### UI Layout (top to bottom)

1. **Sidebar** — Skill level selector (beginner/intermediate), API key input, session history navigation
2. **Input section** — Text area for the user's rough prompt, optional context field ("what is this prompt for?"), submit button
3. **Refinement dialogue** — Chat-style area where Claude asks clarifying questions and the user responds, round-by-round
4. **Refined output** — The current best version of the prompt, with a "what changed and why" explanation
5. **Side-by-side comparison** — Two columns: run the original prompt and the refined prompt against the same test input, see outputs next to each other

## Refinement Flow

1. User pastes a prompt and optionally describes its purpose
2. Claude analyzes the prompt and asks one clarifying question (e.g., "What's the target audience?" or "Should the response be structured or freeform?")
3. User answers; Claude asks another question or decides it has enough context
4. Claude generates 2-3 refined variants with explanations of what changed
5. User picks a variant or asks for more refinement
6. Loop back to steps 2-5 until satisfied

### Skill-Level Adaptation

- **Beginner mode** — Claude explains prompt engineering concepts inline ("I added few-shot examples because..."), suggests techniques proactively, uses simpler language
- **Intermediate mode** — Terse explanations, focuses on the "what changed" diff, assumes familiarity with techniques like chain-of-thought, system prompts, etc.

## Data Model

Session state stored in `st.session_state`:

```python
{
    "skill_level": "beginner" | "intermediate",
    "original_prompt": str,
    "context": str,           # what the prompt is for
    "rounds": [               # refinement history
        {
            "type": "question" | "variants",
            "content": str,          # Claude's question or variants
            "user_response": str,    # user's answer or selection
        }
    ],
    "current_best": str,      # latest refined prompt
    "comparison": {            # side-by-side test results
        "test_input": str,
        "original_output": str,
        "refined_output": str,
    }
}
```

Users can scroll through rounds to revisit earlier versions. Reverting means selecting a previous round's variant as the new `current_best`, which starts a new refinement branch from that point.

## Claude Integration

### Two API Call Types

1. **Refinement calls** — Claude acts as a prompt engineering expert via a system prompt that instructs it to:
   - Analyze the user's prompt for common issues (vague instructions, missing constraints, no output format, etc.)
   - Ask one focused clarifying question per round
   - When generating variants, explain what changed and why
   - Adapt explanation depth based on skill level
   - Know when to stop — don't over-engineer a prompt that's already good

2. **Comparison calls** — Two straightforward API calls: one with the original prompt, one with the refined prompt, same test input. No special system prompt.

### Technical Decisions

- **Model:** `claude-sonnet-4-6` for refinement (fast, affordable, good analysis). Configurable in `config.py`.
- **Streaming:** Yes — use Streamlit's `st.write_stream` for conversational feel
- **Error handling:**
  - Invalid API key → clear message with link to Anthropic console
  - Rate limits → retry with backoff, show "thinking..." indicator
  - Network errors → user-friendly message, preserve session state

## Testing Strategy

### Unit Tests (`tests/test_refiner.py`, `tests/test_config.py`)

- Prompt construction logic — given user prompt + context + skill level, verify system prompt is built correctly
- Response parsing — extract variants, questions, and explanations from Claude's responses
- Session state transitions — verify data model updates correctly through rounds
- Mock the Anthropic API — testing our logic, not Claude's

### Integration Test (`tests/test_api_client.py`)

- One live API call to verify the client works end-to-end
- Marked with `@pytest.mark.integration` (skipped by default, needs API key)
- Tests streaming, error handling, and response format

### Manual Smoke Test

- Run the app, paste a prompt, go through 2-3 refinement rounds, run a comparison
- Catches UX issues that automated tests can't

No Streamlit UI tests — the testing tools are immature. We keep the UI layer thin so most logic is testable via unit tests.

## Dependencies

- `streamlit` — UI framework
- `anthropic` — Anthropic Python SDK
- `pytest` — Testing

## Out of Scope

- Persistent storage (database, file-based history across sessions)
- Multiple LLM provider support
- User authentication
- Deployment configuration
