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
