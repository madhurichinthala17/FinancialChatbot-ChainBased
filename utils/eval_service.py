# utils/eval_service.py

from utils.chat_service import chain_with_message_history
from utils.buildretriever import build_retriever
from Helpers.sessionhistory import clear_session_history

retriever = build_retriever()

def serialize_docs(docs):
    return [
        {
            "content": d.page_content,
            "metadata": d.metadata
        }
        for d in docs
    ]

def get_response_with_context(query: str, session_id: str):
    """Returns (answer, retrieved_chunks) using the same chain as get_response,
    but with a single retrieval call so both are guaranteed to match."""

    # Retrieve once
    retrieved_docs = retriever.invoke(query)
    retrieved_chunks = serialize_docs(retrieved_docs)

    # Reuse the same chain from chat_service, inject pre-fetched context
    answer = chain_with_message_history.invoke(
        {"query": query, "retriever_context": retrieved_chunks},
        config={"configurable": {"session_id": session_id}}
    )

    return answer, retrieved_chunks