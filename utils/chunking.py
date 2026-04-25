from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from Helpers.splitter import split_by_sections

# text_splitter = RecursiveCharacterTextSplitter(
#     # Set a really small chunk size, just to show.
#     chunk_size=1000,
#     chunk_overlap=400
#     #s_separator_regex=False, This always defaults sto False
# )
# #This one works but it is not efficient as the context might not be stored effectively
# # texts = text_splitter.split_documents(filtered_docs)

# final_content = "\n".join(doc.page_content for doc in filtered_docs)


# sections = split_by_sections(final_content)
# # #if we do this, we would loose metadata like page details
# # final_chunks = []
# # for section in sections:
# #     chunks = text_splitter.split_text(section)
# #     final_chunks.extend(chunks)

# final_docs=[]
# for i, section in enumerate(sections):
#     chunks = text_splitter.split_text(section)

#     for chunk in chunks:
#         final_docs.append(
#             Document(
#                 page_content=chunk,
#                 metadata={"section_id": i}
#             )
#         )
def build_chunks(filtered_docs) -> list:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=500)
    full_text = "\n".join(doc.page_content for doc in filtered_docs)
    sections = split_by_sections(full_text)
    final_docs = []
    for i, section in enumerate(sections):
        for chunk in text_splitter.split_text(section):
            final_docs.append(Document(page_content=chunk, metadata={"section_id": i}))
    return final_docs