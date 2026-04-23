from utils.embedding import get_vectorstore

def build_retriever(k: int = 4):
    store = get_vectorstore()
    return store.as_retriever(search_kwargs={"k": k})

# result = retriever.invoke("What factors contribute to operational risk in the firm?")
# for doc in result:
#     print(doc.page_content +"\n")