import pdfplumber
import fitz  # PyMuPDF
import os

def extract_text_from_pdf(filepath):
    text = ""
    try:
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception as e:
        print(f"pdfplumber failed: {e}, trying PyMuPDF")
        doc = fitz.open(filepath)
        for page in doc:
            text += page.get_text()
    return text

def load_documents(folder_path):
    documents = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            path = os.path.join(folder_path, filename)
            text = extract_text_from_pdf(path)
            documents[filename] = text
    return documents
