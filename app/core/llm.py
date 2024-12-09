import cohere
from app.core.config import COHERE_API_KEY

cohere_client = cohere.Client(COHERE_API_KEY)


def build_prompt(question, context):
	return (f"Context: {context}\n"
		f"Question: {question}\n"
		f"Answer in one sentence, in  third person, in  the same language, and with emojis.")

def  ask_llm(prompt):
	response = cohere_client.generate(
		model ="command-xlarge-nightly",
        #model ="embed-multilingual-v2.0",
		prompt=prompt,
		max_tokens = 50,
		temperature= 0
	)
	return response.generations[0].text.strip()


