from sentence_transformers import SentenceTransformer
import chromadb
from docx import Document
# from app.core.embeddings import chunk_document, store_embeddings

from app.core.config import CHROMA_DB_PATH, MODEL_NAME

model = SentenceTransformer(MODEL_NAME)
client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
db_collection = client.create_collection("documents")



def process_docx(file_path):
    doc = Document(file_path)
    content = ""
    for  paragraph in doc.paragraphs:
        if paragraph.text.strip():
            content += paragraph.text.strip() + " "
    return content

def process_and_store_document(document_name, file_path):
    content = process_docx(file_path)
    store_embeddings(document_name, content)


def chunk_document(content, chunk_size=500):
	words =content.split()
	for i in range(0, len(words), chunk_size):
		yield " ".join(words[i:1 + chunk_size])

def store_embeddings(document_name, content):
	for i, chunk in enumerate(chunk_document(content)):
		embedding = model.encode(chunk).tolist()
		db_collection.add(
            ids=[f"{document_name}-{i}"],
			documents=[chunk],
			metadatas=[{"document_name": document_name, "chunk_index":i}],
			embeddings=[embedding]
		)


def retrieve_context(question):
	question_embedding = model.encode(question).tolist()
	results = db_collection.query(query_embeddings=[question_embedding], n_results=1)
	return results["documents"][0] if results ["documents"] else  "No encontramos un contexto relevante"
