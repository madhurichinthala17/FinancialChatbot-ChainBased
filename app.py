import streamlit as st
from utils.chat_service import get_response

st.title("Hey, Welcome to Chase-bot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

query = st.chat_input("Ask any Question about JP Morgan 10K report 2026")

if query:
    st.session_state.chat_history.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    try:
        answer = get_response(query, st.session_state.chat_history)
    except Exception as e:
        answer = f"Error: {str(e)}"

    st.session_state.chat_history.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)