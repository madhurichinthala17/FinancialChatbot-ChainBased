import streamlit as st

st.title("Hey, Welcome to Chase-bot")

# Lazy import — shows a spinner and surfaces any startup error visibly
# instead of a blank page.
@st.cache_resource(show_spinner="Loading model and vector store...")
def load_chain():
    from utils.chat_service import get_response
    return get_response

try:
    get_response = load_chain()
except Exception as e:
    st.error(f"Failed to load the chain: {e}")
    st.stop()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

query = st.chat_input("Ask any question about the JP Morgan 10K report")

if query:
    st.session_state.chat_history.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    try:
        answer = get_response(query, "madhuri")
    except Exception as e:
        answer = f"Error: {str(e)}"

    st.session_state.chat_history.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)