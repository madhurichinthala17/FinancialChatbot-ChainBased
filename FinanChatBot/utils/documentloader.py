from langchain_community.document_loaders import PyMuPDFLoader
from Helpers.cleaner import clean_text

filepath = "C:\\Users\\madhu\\FinancialChatbot-ChainBased\\FinanChatBot\\testdata\\JPmorgan10kReport.pdf"

loader = PyMuPDFLoader(
    filepath,
    extract_tables="markdown"
    #mode = "single",
    #pages_delimiter= "-----This is the end of the page-----"
    )

#I can load document using load() method but it will load the entire document in memory and 
# if the document is large it may cause memory issues. So I can use lazy_load() method which will load the document in chunks 
# and I can process each chunk separately.

# pages = []
# for doc in loader.lazy_load():
#     pages.append(doc)

# print(pages[14].page_content) # This prints the content of the first page of the PDF document.
#print(pages[0].metadata) # This prints the metadata of the first page of the PDF document.
#print(len(pages)) This prints 482.

# docs = loader.load()
# print(docs[0].page_content[:5780]) 


filtered_docs = []

kept =0
for doc in loader.lazy_load():

    page_num = doc.metadata.get("page", 0)
    content = doc.page_content.lower()

    # Skip early pages
    if page_num < 3:
        kept=kept+1
        continue

    # Skip noisy pages
    if "glossary of terms and acronyms" in content:
        kept=kept+1
        continue

    if "signatures" in content:
        kept=kept+1
        continue

    cleaned_content = clean_text(doc.page_content)
    doc.page_content = cleaned_content
    filtered_docs.append(doc)

print(filtered_docs[0].page_content[:5780]) 
print(f"Number of pages removed: {kept}")