from  fastapi import APIRouter
from app.models.document import DocumentRequest
from app.models.question import QuestionRequest, AnswerResponse
from app.core.embeddings import store_embeddings, retrieve_context
from app.core.llm import ask_llm, build_prompt

router = APIRouter()

@router.post("/add-document")
def add_document(request: DocumentRequest):
	store_embeddings(request.document_name, request.content)
	return {"message":"Documento procesado y guardado correctamente."}

@router.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    context = retrieve_context(request.question)
    prompt =  build_prompt(request.question, context)
    answer = ask_llm(prompt)
    return AnswerResponse(user_name=request.user_name, question=request.question, answer=answer)
