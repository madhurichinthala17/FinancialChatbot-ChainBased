from langchain_ollama import OllamaEmbeddings
from utils.chunking import final_docs
from langchain_chroma import Chroma

#When we do this data duplication might happen when we run multiple times
#So its better to instantiate once and then add documents
# chromastore = Chroma.from_documents(
#     documents = final_docs,
#     collection_name="JPMorganSEC",
#     embedding=embeddings,
#     persist_directory="./chroma_langchain_db",
# )
embeddings = OllamaEmbeddings(model="nomic-embed-text")
chromastore = Chroma(
    collection_name="JPMorganSEC",
    embedding_function=embeddings,
    persist_directory="C:\\Users\\madhu\\FinancialChatbot-ChainBased\\FinanChatBot\\vectorstore\\chroma_langchain_db",
)

# ONLY add if DB is empty or new docs exist
if chromastore._collection.count() == 0:
    chromastore.add_documents(final_docs)

# results = chromastore.similarity_search(query="What are JPMorgan risk factors?", k=4)
# for doc in results:
#     print(f"* {doc.page_content} [{doc.metadata}]")