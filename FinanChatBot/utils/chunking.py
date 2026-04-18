import utils.documentloader
from langchain_text_splitters import RecursiveCharacterTextSplitter
filtered_docs = utils.documentloader.filtered_docs

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=1000,
    chunk_overlap=100
    #s_separator_regex=False, This always defaults sto False
)

texts = text_splitter.split_documents(filtered_docs)
print(texts[0].page_content)

print("-----------")

print(texts[1].page_content)

print("-----------")

print(texts[2].page_content)