from langchain_ollama import OllamaEmbeddings
import utils.chunking
chunks = utils.chunking.final_chunks


embeddings = OllamaEmbeddings(model="llama3.2:latest")

vectorstore = embeddings.embed_documents(chunks)

