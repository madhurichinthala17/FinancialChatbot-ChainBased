from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from utils.documentloader import load_filtered_docs
from utils.chunking import build_chunks

#When we do this data duplication might happen when we run multiple times
#So its better to instantiate once and then add documents
# chromastore = Chroma.from_documents(
#     documents = final_docs,
#     collection_name="JPMorganSEC",
#     embedding=embeddings,
#     persist_directory="./chroma_langchain_db",
# )
CHROMA_DIR = "C:\\Users\\madhu\\FinancialChatbot-ChainBased\\FinanChatBot\\vectorstore\\chroma_langchain_db"


# results = chromastore.similarity_search(query="What are JPMorgan risk factors?", k=4)
# for doc in results:
#     print(f"* {doc.page_content} [{doc.metadata}]")

def get_vectorstore() -> Chroma:
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    store = Chroma(
        collection_name="JPMorganSEC",
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )
    if store._collection.count() == 0:
        filtered_docs = load_filtered_docs()
        chunks = build_chunks(filtered_docs)
        store.add_documents(chunks)
    return store