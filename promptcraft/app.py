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
