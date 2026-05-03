from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


template = ChatPromptTemplate([
    ("system", """You are a financial analyst assistant.Use ONLY the provided context from SEC filings
                   If answer is not in context, say that it is not found in documents"""),
    MessagesPlaceholder(variable_name="history", optional=True),
    ("human", """
     Use the following context to answer the question.
     Context:
     {retriever_context}

     Question:
     {query}
    """)
])

