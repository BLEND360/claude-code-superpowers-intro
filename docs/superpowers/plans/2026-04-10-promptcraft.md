# PromptCraft Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Streamlit app that helps users iteratively refine LLM prompts through dialogue with Claude, with side-by-side comparison of original vs. refined prompt outputs.

**Architecture:** Single-page Streamlit app with four Python modules: `config.py` (constants/presets), `api_client.py` (Anthropic SDK wrapper), `refiner.py` (prompt analysis and refinement logic), and `app.py` (UI). TDD approach — tests first, then implementation.

**Tech Stack:** Python, Streamlit, Anthropic Python SDK, pytest

**Spec:** `docs/superpowers/specs/2026-04-10-promptcraft-design.md`

---

## File Structure

```
promptcraft/
├── app.py              # Streamlit UI — layout, session state, user interactions
├── config.py           # Constants — model, max tokens, system prompts, skill presets
├── api_client.py       # Anthropic SDK wrapper — streaming, error handling, retries
├── refiner.py          # Core logic — prompt construction, response parsing, round management
├── requirements.txt    # Dependencies
└── tests/
    ├── __init__.py
    ├── test_config.py      # Config constants and preset validation
    ├── test_api_client.py  # API client unit + integration tests
    └── test_refiner.py     # Refiner logic, prompt building, response parsing
```

---

### Task 1: Project Scaffolding and Config

**Files:**
- Create: `promptcraft/config.py`
- Create: `promptcraft/requirements.txt`
- Create: `promptcraft/tests/__init__.py`
- Create: `promptcraft/tests/test_config.py`

- [ ] **Step 1: Create project directory and requirements**

```
promptcraft/requirements.txt
```

```text
streamlit>=1.45.0
anthropic>=0.52.0
pytest>=8.0.0
```

- [ ] **Step 2: Write failing tests for config**

```python
# promptcraft/tests/test_config.py
from config import (
    DEFAULT_MODEL,
    MAX_TOKENS,
    SKILL_LEVELS,
    get_system_prompt,
)


def test_default_model_is_set():
    assert DEFAULT_MODEL == "claude-sonnet-4-6"


def test_max_tokens_is_positive():
    assert MAX_TOKENS > 0


def test_skill_levels_has_beginner_and_intermediate():
    assert "beginner" in SKILL_LEVELS
    assert "intermediate" in SKILL_LEVELS


def test_get_system_prompt_beginner():
    prompt = get_system_prompt("beginner")
    assert "explain" in prompt.lower()
    assert "prompt engineering" in prompt.lower()


def test_get_system_prompt_intermediate():
    prompt = get_system_prompt("intermediate")
    assert "concise" in prompt.lower() or "terse" in prompt.lower()


def test_get_system_prompt_contains_core_instructions():
    for level in SKILL_LEVELS:
        prompt = get_system_prompt(level)
        assert "clarifying question" in prompt.lower()
        assert "variant" in prompt.lower()
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `cd promptcraft && python -m pytest tests/test_config.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'config'`

- [ ] **Step 4: Implement config.py**

```python
# promptcraft/config.py
DEFAULT_MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 4096
SKILL_LEVELS = ["beginner", "intermediate"]

_BASE_INSTRUCTIONS = """You are a prompt engineering expert. Your job is to help the user improve their LLM prompt.

Rules:
- Analyze the user's prompt for issues: vague instructions, missing constraints, no output format, ambiguous scope.
- Ask ONE focused clarifying question per round to understand the user's intent.
- When you have enough context, generate 2-3 refined variants of the prompt.
- For each variant, explain what you changed and why it improves the prompt.
- Know when to stop — don't over-engineer a prompt that's already good.
- Format variants using markdown headers: ### Variant 1, ### Variant 2, etc.
- After the variants, include a ### Recommendation section explaining which variant you'd pick and why."""

_BEGINNER_ADDENDUM = """
Skill level: BEGINNER
- Explain prompt engineering concepts inline when you use them (e.g., "I added few-shot examples because...").
- Suggest techniques proactively and explain why they help.
- Use simple, approachable language. Avoid jargon without explanation."""

_INTERMEDIATE_ADDENDUM = """
Skill level: INTERMEDIATE
- Be concise and terse in explanations. Focus on what changed, not why the technique exists.
- Assume familiarity with techniques like chain-of-thought, few-shot examples, system prompts, and structured output.
- Skip basic explanations. Focus on the diff between original and refined."""


def get_system_prompt(skill_level: str) -> str:
    if skill_level == "beginner":
        return _BASE_INSTRUCTIONS + _BEGINNER_ADDENDUM
    return _BASE_INSTRUCTIONS + _INTERMEDIATE_ADDENDUM
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd promptcraft && python -m pytest tests/test_config.py -v`
Expected: All 6 tests PASS

- [ ] **Step 6: Create tests/__init__.py and commit**

```python
# promptcraft/tests/__init__.py
```

(Empty file)

```bash
cd promptcraft
git add config.py requirements.txt tests/__init__.py tests/test_config.py
git commit -m "feat: add config module with model settings and skill-level system prompts"
```

---

### Task 2: API Client

**Files:**
- Create: `promptcraft/api_client.py`
- Create: `promptcraft/tests/test_api_client.py`

- [ ] **Step 1: Write failing tests for api_client**

```python
# promptcraft/tests/test_api_client.py
from unittest.mock import MagicMock, patch
import pytest
from api_client import create_client, send_message, stream_message, APIError


def test_create_client_with_valid_key():
    client = create_client("sk-ant-test-key")
    assert client is not None


def test_create_client_with_empty_key_raises():
    with pytest.raises(APIError, match="API key"):
        create_client("")


def test_send_message_returns_text():
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.content = [MagicMock(text="Hello from Claude")]
    mock_client.messages.create.return_value = mock_response

    result = send_message(
        client=mock_client,
        system="You are helpful.",
        messages=[{"role": "user", "content": "Hi"}],
        model="claude-sonnet-4-6",
        max_tokens=1024,
    )
    assert result == "Hello from Claude"
    mock_client.messages.create.assert_called_once()


def test_send_message_propagates_api_error():
    mock_client = MagicMock()
    mock_client.messages.create.side_effect = Exception("Connection failed")

    with pytest.raises(APIError, match="Connection failed"):
        send_message(
            client=mock_client,
            system="You are helpful.",
            messages=[{"role": "user", "content": "Hi"}],
            model="claude-sonnet-4-6",
            max_tokens=1024,
        )


def test_stream_message_yields_text_chunks():
    mock_client = MagicMock()
    mock_stream_context = MagicMock()
    mock_stream = MagicMock()
    mock_stream.text_stream = iter(["Hello", " from", " Claude"])
    mock_stream_context.__enter__ = MagicMock(return_value=mock_stream)
    mock_stream_context.__exit__ = MagicMock(return_value=False)
    mock_client.messages.stream.return_value = mock_stream_context

    chunks = list(stream_message(
        client=mock_client,
        system="You are helpful.",
        messages=[{"role": "user", "content": "Hi"}],
        model="claude-sonnet-4-6",
        max_tokens=1024,
    ))
    assert chunks == ["Hello", " from", " Claude"]


@pytest.mark.integration
def test_live_api_call():
    """Requires ANTHROPIC_API_KEY env var. Run with: pytest -m integration"""
    import os
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        pytest.skip("ANTHROPIC_API_KEY not set")

    client = create_client(api_key)
    result = send_message(
        client=client,
        system="Reply with exactly: PONG",
        messages=[{"role": "user", "content": "PING"}],
        model="claude-sonnet-4-6",
        max_tokens=16,
    )
    assert "PONG" in result
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd promptcraft && python -m pytest tests/test_api_client.py -v -m "not integration"`
Expected: FAIL — `ModuleNotFoundError: No module named 'api_client'`

- [ ] **Step 3: Implement api_client.py**

```python
# promptcraft/api_client.py
import anthropic


class APIError(Exception):
    """Raised when an API call fails."""
    pass


def create_client(api_key: str) -> anthropic.Anthropic:
    if not api_key or not api_key.strip():
        raise APIError(
            "API key is required. Get one at https://console.anthropic.com/settings/keys"
        )
    return anthropic.Anthropic(api_key=api_key)


def send_message(
    client: anthropic.Anthropic,
    system: str,
    messages: list[dict],
    model: str,
    max_tokens: int,
) -> str:
    try:
        response = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=messages,
        )
        return response.content[0].text
    except Exception as e:
        raise APIError(str(e)) from e


def stream_message(
    client: anthropic.Anthropic,
    system: str,
    messages: list[dict],
    model: str,
    max_tokens: int,
):
    try:
        with client.messages.stream(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=messages,
        ) as stream:
            yield from stream.text_stream
    except Exception as e:
        raise APIError(str(e)) from e
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd promptcraft && python -m pytest tests/test_api_client.py -v -m "not integration"`
Expected: All 5 non-integration tests PASS

- [ ] **Step 5: Commit**

```bash
cd promptcraft
git add api_client.py tests/test_api_client.py
git commit -m "feat: add API client with streaming support and error handling"
```

---

### Task 3: Refiner Logic

**Files:**
- Create: `promptcraft/refiner.py`
- Create: `promptcraft/tests/test_refiner.py`

- [ ] **Step 1: Write failing tests for refiner**

```python
# promptcraft/tests/test_refiner.py
from unittest.mock import MagicMock, patch
from refiner import (
    build_messages,
    parse_response_type,
    init_session_state,
    add_round,
    get_current_best,
)


def test_init_session_state_defaults():
    state = init_session_state()
    assert state["skill_level"] == "beginner"
    assert state["original_prompt"] == ""
    assert state["context"] == ""
    assert state["rounds"] == []
    assert state["current_best"] == ""
    assert state["comparison"] is None


def test_build_messages_first_round():
    state = init_session_state()
    state["original_prompt"] = "Summarize this text"
    state["context"] = "For a blog post"

    messages = build_messages(state)
    assert len(messages) == 1
    assert messages[0]["role"] == "user"
    assert "Summarize this text" in messages[0]["content"]
    assert "For a blog post" in messages[0]["content"]


def test_build_messages_with_rounds():
    state = init_session_state()
    state["original_prompt"] = "Summarize this text"
    state["context"] = ""
    state["rounds"] = [
        {
            "type": "question",
            "content": "What audience is this for?",
            "user_response": "Technical readers",
        },
    ]

    messages = build_messages(state)
    assert len(messages) == 3  # initial + assistant question + user answer
    assert messages[0]["role"] == "user"
    assert messages[1]["role"] == "assistant"
    assert messages[1]["content"] == "What audience is this for?"
    assert messages[2]["role"] == "user"
    assert messages[2]["content"] == "Technical readers"


def test_parse_response_type_question():
    response = "Before I refine this, I need to understand: what format should the output be in?"
    assert parse_response_type(response) == "question"


def test_parse_response_type_variants():
    response = """Here are refined versions of your prompt:

### Variant 1
Summarize the following text in 3 bullet points for a technical audience.

### Variant 2
Given the text below, produce a concise technical summary.

### Recommendation
I'd go with Variant 1 because it's more specific about format."""
    assert parse_response_type(response) == "variants"


def test_add_round_appends_to_state():
    state = init_session_state()
    add_round(state, "question", "What is this for?", "")
    assert len(state["rounds"]) == 1
    assert state["rounds"][0]["type"] == "question"
    assert state["rounds"][0]["content"] == "What is this for?"


def test_get_current_best_returns_empty_when_no_variants():
    state = init_session_state()
    state["original_prompt"] = "Summarize this"
    assert get_current_best(state) == ""


def test_get_current_best_returns_latest_variant_content():
    state = init_session_state()
    state["current_best"] = "Refined prompt text here"
    assert get_current_best(state) == "Refined prompt text here"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd promptcraft && python -m pytest tests/test_refiner.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'refiner'`

- [ ] **Step 3: Implement refiner.py**

```python
# promptcraft/refiner.py
import re


def init_session_state() -> dict:
    return {
        "skill_level": "beginner",
        "original_prompt": "",
        "context": "",
        "rounds": [],
        "current_best": "",
        "comparison": None,
    }


def build_messages(state: dict) -> list[dict]:
    messages = []

    # First message: the user's original prompt + context
    first_msg = f"Here is my prompt that I'd like you to help me improve:\n\n{state['original_prompt']}"
    if state["context"]:
        first_msg += f"\n\nContext for what this prompt is for: {state['context']}"
    messages.append({"role": "user", "content": first_msg})

    # Append rounds as alternating assistant/user messages
    for round_data in state["rounds"]:
        messages.append({"role": "assistant", "content": round_data["content"]})
        if round_data["user_response"]:
            messages.append({"role": "user", "content": round_data["user_response"]})

    return messages


def parse_response_type(response: str) -> str:
    if re.search(r"###\s*Variant\s+\d", response):
        return "variants"
    return "question"


def add_round(state: dict, round_type: str, content: str, user_response: str) -> None:
    state["rounds"].append({
        "type": round_type,
        "content": content,
        "user_response": user_response,
    })


def get_current_best(state: dict) -> str:
    return state["current_best"]
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd promptcraft && python -m pytest tests/test_refiner.py -v`
Expected: All 8 tests PASS

- [ ] **Step 5: Commit**

```bash
cd promptcraft
git add refiner.py tests/test_refiner.py
git commit -m "feat: add refiner with message building, response parsing, and round management"
```

---

### Task 4: Streamlit App — Sidebar and Input Section

**Files:**
- Create: `promptcraft/app.py`

- [ ] **Step 1: Implement app.py with sidebar and input section**

```python
# promptcraft/app.py
import streamlit as st
from config import SKILL_LEVELS, DEFAULT_MODEL, MAX_TOKENS, get_system_prompt
from api_client import create_client, stream_message, APIError
from refiner import init_session_state, build_messages, parse_response_type, add_round

st.set_page_config(page_title="PromptCraft", page_icon="✨", layout="wide")
st.title("PromptCraft")
st.caption("Iteratively refine your LLM prompts with Claude")

# --- Session state initialization ---
if "state" not in st.session_state:
    st.session_state.state = init_session_state()
if "started" not in st.session_state:
    st.session_state.started = False

state = st.session_state.state

# --- Sidebar ---
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Anthropic API Key", type="password", help="Get a key at https://console.anthropic.com/settings/keys")
    state["skill_level"] = st.selectbox("Skill Level", SKILL_LEVELS, index=SKILL_LEVELS.index(state["skill_level"]))

    st.divider()
    st.header("Session History")
    if state["rounds"]:
        for i, r in enumerate(state["rounds"]):
            label = f"Round {i + 1}: {r['type']}"
            st.text(label)
    else:
        st.caption("No refinement rounds yet.")

    if st.button("Start Over"):
        st.session_state.state = init_session_state()
        st.session_state.started = False
        st.rerun()

# --- Input Section ---
if not st.session_state.started:
    st.subheader("Paste your prompt")
    prompt_input = st.text_area(
        "Your prompt",
        height=150,
        placeholder="Enter the prompt you want to improve...",
    )
    context_input = st.text_input(
        "What is this prompt for? (optional)",
        placeholder="e.g., Summarizing customer feedback for a weekly report",
    )

    if st.button("Refine This Prompt", type="primary", disabled=not prompt_input):
        if not api_key:
            st.error("Please enter your Anthropic API key in the sidebar.")
        else:
            state["original_prompt"] = prompt_input
            state["context"] = context_input
            st.session_state.started = True
            st.rerun()
```

- [ ] **Step 2: Smoke test the app**

Run: `cd promptcraft && pip install -r requirements.txt && streamlit run app.py`

Verify in browser:
- Title "PromptCraft" appears
- Sidebar has API key input, skill level dropdown, "Start Over" button
- Main area has text area, context field, and "Refine This Prompt" button
- Button is disabled when text area is empty

Stop the server with Ctrl+C.

- [ ] **Step 3: Commit**

```bash
cd promptcraft
git add app.py
git commit -m "feat: add Streamlit app with sidebar and prompt input section"
```

---

### Task 5: Streamlit App — Refinement Dialogue

**Files:**
- Modify: `promptcraft/app.py`

- [ ] **Step 1: Add refinement dialogue to app.py**

Append this code to the end of `app.py`, replacing the closing of the `if not st.session_state.started:` block:

```python
# --- Refinement Dialogue ---
if st.session_state.started:
    st.subheader("Refinement Dialogue")

    # Show original prompt
    with st.expander("Original prompt", expanded=False):
        st.markdown(state["original_prompt"])
        if state["context"]:
            st.caption(f"Context: {state['context']}")

    # Display past rounds
    for i, r in enumerate(state["rounds"]):
        with st.chat_message("assistant"):
            st.markdown(r["content"])
        if r["user_response"]:
            with st.chat_message("user"):
                st.markdown(r["user_response"])

    # If the last round has no user response yet, or there are no rounds, get Claude's next response
    needs_claude_response = (
        len(state["rounds"]) == 0
        or (state["rounds"][-1]["user_response"] != "")
    )

    if needs_claude_response:
        with st.chat_message("assistant"):
            try:
                client = create_client(api_key)
                messages = build_messages(state)
                system = get_system_prompt(state["skill_level"])

                response_text = st.write_stream(
                    stream_message(
                        client=client,
                        system=system,
                        messages=messages,
                        model=DEFAULT_MODEL,
                        max_tokens=MAX_TOKENS,
                    )
                )

                response_type = parse_response_type(response_text)
                add_round(state, response_type, response_text, "")

                if response_type == "variants":
                    state["current_best"] = response_text

            except APIError as e:
                st.error(f"API Error: {e}")

    # User input for the next round
    if state["rounds"] and state["rounds"][-1]["user_response"] == "":
        user_input = st.chat_input("Your response...")
        if user_input:
            state["rounds"][-1]["user_response"] = user_input
            st.rerun()
```

- [ ] **Step 2: Smoke test the refinement flow**

Run: `cd promptcraft && streamlit run app.py`

Verify:
- Enter API key and a test prompt, click "Refine This Prompt"
- Claude's response streams in
- A chat input appears at the bottom
- Type a response, hit enter — Claude responds again
- After 2-3 rounds, Claude should produce variants (### Variant 1, etc.)

Stop with Ctrl+C.

- [ ] **Step 3: Commit**

```bash
cd promptcraft
git add app.py
git commit -m "feat: add refinement dialogue with streaming Claude responses"
```

---

### Task 6: Streamlit App — Refined Output and Side-by-Side Comparison

**Files:**
- Modify: `promptcraft/app.py`

- [ ] **Step 1: Add refined output display and comparison section**

Append this code to the end of `app.py`, inside the `if st.session_state.started:` block, after the user input section:

```python
    # --- Refined Output ---
    if state["current_best"]:
        st.divider()
        st.subheader("Current Best Prompt")
        st.markdown(state["current_best"])

        # --- Side-by-Side Comparison ---
        st.divider()
        st.subheader("Compare: Original vs. Refined")

        test_input = st.text_area(
            "Test input (the content your prompt will process)",
            height=100,
            placeholder="Paste the text or input your prompt would typically receive...",
            key="test_input",
        )

        if st.button("Run Comparison", type="primary", disabled=not test_input):
            try:
                client = create_client(api_key)
                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("**Original Prompt Output**")
                    original_output = st.write_stream(
                        stream_message(
                            client=client,
                            system="",
                            messages=[
                                {"role": "user", "content": f"{state['original_prompt']}\n\n{test_input}"}
                            ],
                            model=DEFAULT_MODEL,
                            max_tokens=MAX_TOKENS,
                        )
                    )

                with col2:
                    st.markdown("**Refined Prompt Output**")
                    refined_output = st.write_stream(
                        stream_message(
                            client=client,
                            system="",
                            messages=[
                                {"role": "user", "content": f"{state['current_best']}\n\n{test_input}"}
                            ],
                            model=DEFAULT_MODEL,
                            max_tokens=MAX_TOKENS,
                        )
                    )

                state["comparison"] = {
                    "test_input": test_input,
                    "original_output": original_output,
                    "refined_output": refined_output,
                }

            except APIError as e:
                st.error(f"API Error: {e}")
```

- [ ] **Step 2: Smoke test the comparison**

Run: `cd promptcraft && streamlit run app.py`

Verify:
- Go through refinement until variants appear
- "Current Best Prompt" section appears below the dialogue
- "Compare" section shows a test input text area
- Enter test input, click "Run Comparison"
- Two columns stream outputs side by side: original vs. refined

Stop with Ctrl+C.

- [ ] **Step 3: Commit**

```bash
cd promptcraft
git add app.py
git commit -m "feat: add refined output display and side-by-side comparison"
```

---

### Task 7: Final Integration — Polish and Verification

**Files:**
- Modify: `promptcraft/app.py` (minor polish)

- [ ] **Step 1: Run all unit tests**

Run: `cd promptcraft && python -m pytest tests/ -v -m "not integration"`
Expected: All tests PASS (config: 6, api_client: 5, refiner: 8 = 19 total)

- [ ] **Step 2: Fix any test failures**

If any tests fail, read the error messages and fix the underlying issues. Re-run until all pass.

- [ ] **Step 3: Full smoke test**

Run: `cd promptcraft && streamlit run app.py`

Full walkthrough:
1. Enter API key in sidebar
2. Set skill level to "beginner"
3. Paste a test prompt: "Summarize this text for me"
4. Add context: "For a weekly team email"
5. Click "Refine This Prompt"
6. Answer 2-3 clarifying questions from Claude
7. Review the generated variants
8. Scroll down to "Compare" section
9. Enter test input text and run comparison
10. Verify side-by-side output appears
11. Click "Start Over" in sidebar — verify everything resets
12. Repeat steps 3-10 with skill level "intermediate" — verify explanations are more terse

Stop with Ctrl+C.

- [ ] **Step 4: Commit any polish changes**

```bash
cd promptcraft
git add -A
git commit -m "chore: final polish and verification"
```
