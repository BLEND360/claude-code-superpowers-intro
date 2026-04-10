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
