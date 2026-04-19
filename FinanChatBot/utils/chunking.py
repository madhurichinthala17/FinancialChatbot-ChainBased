import utils.documentloader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from Helpers.splitter import split_by_sections
filtered_docs = utils.documentloader.filtered_docs

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=1000,
    chunk_overlap=400
    #s_separator_regex=False, This always defaults sto False
)
#This one works but it is not efficient as the context might not be stored effectively
# texts = text_splitter.split_documents(filtered_docs)

final_content = "\n".join(doc.page_content for doc in filtered_docs)

sections = split_by_sections(final_content)

final_chunks = []
for section in sections:
    chunks = text_splitter.split_text(section)
    final_chunks.extend(chunks)