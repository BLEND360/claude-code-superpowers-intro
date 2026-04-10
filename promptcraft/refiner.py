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
