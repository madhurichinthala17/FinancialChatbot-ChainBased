from utils.embedding import chromastore

retriever = chromastore.as_retriever(
    search_kwargs = {"k" : 4,}
)

# result = retriever.invoke("What factors contribute to operational risk in the firm?")
# for doc in result:
#     print(doc.page_content +"\n")