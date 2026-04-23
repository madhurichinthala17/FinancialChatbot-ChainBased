import os
from pathlib import Path
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from utils.documentloader import load_filtered_docs
from utils.chunking import build_chunks

# Resolves to  <project_root>/vectorstore/chroma_langchain_d
CHROMA_DIR = str(
    Path(__file__).resolve().parent.parent / "vectorstore" / "chroma_langchain_db"
)


def get_vectorstore() -> Chroma:
    """Return the Chroma store, populating it on first run if empty."""

    # Create the directory if it doesn't exist yet
    os.makedirs(CHROMA_DIR, exist_ok=True)

    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    store = Chroma(
        collection_name="JPMorganSEC",
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )

    if store._collection.count() == 0:
        print(f"[embedding] Vector store empty — building chunks and embedding now...")
        print(f"[embedding] Persisting to: {CHROMA_DIR}")
        filtered_docs = load_filtered_docs()
        chunks = build_chunks(filtered_docs)
        store.add_documents(chunks)
        print(f"[embedding] Done. {store._collection.count()} chunks stored.")
    else:
        print(f"[embedding] Loaded existing store ({store._collection.count()} chunks) from {CHROMA_DIR}")

    return store

# When we do this data duplication might happen when we run multiple times
# So its better to instantiate once and then add documents
# chromastore = Chroma.from_documents(
#     documents = final_docs,
#     collection_name="JPMorganSEC",
#     embedding=embeddings,
#     persist_directory="./chroma_langchain_db",
# )

# results = chromastore.similarity_search(query="What are JPMorgan risk factors?", k=4)
# for doc in results:
#     print(f"* {doc.page_content} [{doc.metadata}]")