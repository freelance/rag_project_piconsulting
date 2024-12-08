from pydantic import BaseModel

class QuestionRequest(BaseModel):
	user_name: str
	question: str


class AnswerResponse(BaseModel):
	user_name: str
	question: str
	answer: str

