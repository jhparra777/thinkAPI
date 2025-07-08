from pydantic import BaseModel, Field
from fastapi import APIRouter

routerChat = APIRouter()

# Definicion del Modelo de los datos
class Query(BaseModel):
    question: str

# Definicion del e 
@routerChat.post("/chat")
def chat(query: Query):
    # Aquí puedes invocar LangChain o cualquier lógica
    response = f"Recibí tu pregunta: {query.question}"
    return {"answer": response}
