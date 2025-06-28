from langchain_community.document_loaders import PyPDFLoader

def extract_pdf_text(file_path: str) -> str:
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    text = "\n".join([doc.page_content.strip() for doc in docs])
    return text
