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
