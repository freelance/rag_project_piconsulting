from sentence_transformes import SentenceTransformer
import chromadb
from app.core.config import CHROMA_DB_PATH, MODEL_NAME

model = SentenceTransformer(MODEL_NAME)
client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
db_collection = client.create_collection("documents")


def chunk_documnet(content, chunk_size=500):
	words =content.split()
	for i in range(0, len(words), chunk_size):
		yield " ".join(words[i:1 + chunk_size])

def store_embeddings(document_name, content):
	for i, chunk in enumerate(chunk_document(content)):
		embedding = model.encode(chunk).tolist()
		db_collection.add(
			documents=[chunk],
			metadatas=[{"document_name": document_name, "chunk_index":i}],
			embeddings=[embedding]
		)


def retrieve_context(question):
	question_embedding = model.encode(question).tolist()
	results = db_collection.query(embeddings=[question_embedding], n_results=1)
	return results["documents"][0] if results ["documents"] else  "No encontramos un contexto relevante"
