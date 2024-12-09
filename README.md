# rag_project_piconsulting
challenge

Para correr :...
==============
cd embeddings
rm -rf chroma.sqlite
cd .. 
uvicorn main:app  --reload
Acceder al  link local 127.0.0.1:8000/docs 
usar http://127.0.0.1:8000/docs#/default/add_document_add_document_post para cargar el documento ubicado en "./documents"
presiona el boton "Try it now" y modifica el texto de la siguiente manera

{
  "document_name": "documento",
  "content": "string"
}

Presiona el boton azul "execute"  para cargar el documento.

obtendra la respuesta correcta: 	
Response body
Download
{
  "message": "Documento procesado y guardado correctamente."
}

Luego presionar try it now!! del POST "ASK Question" 
pasar estos parametros usuario y pregunta
{
  "user_name": "Alice",
  "question": "Quien es Zara?"
}
presiona el boton ejecutar-..
obtendras:...
Response body
Download
{
  "user_name": "Alice",
  "question": "Quien es Zara?",
  "answer": "Zara es un valiente explorador que descubre un artefacto antiguo en la galaxia de Zenthoria, capaz de traer la paz a dos civilizaciones alienígenas al borde de la guerra. 🌌🛸🛡️"
}

