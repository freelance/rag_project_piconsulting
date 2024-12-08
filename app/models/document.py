from pydantic import BaseModel

class DocumentRequest(BaseModel):
	document_name: str
	content: str

