from utils.prompt import template
from utils.buildretriever import retriever

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory, RunnableLambda
from langchain_community.chat_message_histories import ChatMessageHistory
from utils.model import chatmodel
from operator import itemgetter

# query = "What are the main categories of risk faced by JPMorgan?"

# result = retriever.invoke(query)

# retrived_chunks = "\n".join(doc.page_content for doc in result)

# llm_chain = template | chatmodel | StrOutputParser()

# response = llm_chain.invoke({"retrieved_chunks" : retrived_chunks,"question" : query})
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

store = {}
def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

#The below chain works when we are only passing the query without history , but with history we npass dictionary so we need to extract query from history
# chain = (
#     {"retriever_context": retriever | format_docs , "query": RunnablePassthrough()}
#     | template
#     | chatmodel
#     | StrOutputParser()
# )

#We always need to pass all the variables in the prompt first
chain = (
    {
    "retriever_context": RunnableLambda(lambda x : format_docs(retriever.invoke(x["query"]))),
    "query": RunnableLambda(lambda x : x["query"]), 
    "history":  itemgetter("history") 
    }
    | template
    | chatmodel
    | StrOutputParser()
)

chain_with_message_history= RunnableWithMessageHistory(
    chain ,
    get_session_history,
    #lambda session_id : ChatMessageHistory(), This doesnot store presistently
    input_messages_key="query",
    history_messages_key="history"
)
# 2. Invoke the chain directly with the query
query= "What are the main categories of risk faced by JPMorgan?"
response = chain_with_message_history.invoke({"query" : query}, config = {"configurable" : {"session_id" : "madhuri"}})

print(response)

# The "Real-World" Analogy
# Imagine an assembly line for making a sandwich:

# Station A (Retriever): Grabs bread from a bin.
# Station B (RunnablePassthrough): Just holds onto the customer's original order ticket so the next station can read it.
# Station C (Prompt Template): Combines the bread (from A) and the ticket (from B) into a clear instruction for the chef.
# Without RunnablePassthrough, the "ticket" would disappear after Station A ran, and the chef would never know what kind of sandwich the customer wanted!

# High-level helpers (create_retrieval_chain, etc.) are designed to be "batteries-included." They know that if you give them a retriever and a prompt, your most likely goal is to format those documents into a string for an LLM. They have internal logic to look for a context key, extract the .page_content from your list of Document objects, and join them with newlines.
# LCEL (your current path) is a functional "programming language" for chains. It treats components like generic data transformers. It is "dumb" by design: it doesn't assume you want your documents joined with \n. Maybe you want them joined with commas, or maybe you want to pass them to a model as a structured tool call. Because LCEL doesn't know your intent, it does not perform any implicit formatting.
# What you need to do in LCEL
# Since you are using raw LCEL, you must bridge that gap manually using a Runnable. The most common way to do this is by adding a small transformation step before your prompt: