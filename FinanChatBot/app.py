from utils.chat import response
import streamlit as st

st.title("Hey, Welcome to Chase-bot")

# ✅ Initialize session state properly
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show existing chat
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

query = st.chat_input("Ask any Question about JP Morgan 10K report 2026")

if query:
    # user message
    st.session_state.chat_history.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # assistant response
    try:
        answer = response(query, "madhuri")
    except Exception as e:
        answer = f"Error: {str(e)}"

    st.session_state.chat_history.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.markdown(answer)