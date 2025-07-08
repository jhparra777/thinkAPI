from pydantic import BaseModel, Field
from fastapi import APIRouter

routerChat = APIRouter()

# Definicion del Modelo de los datos
class Query(BaseModel):
    question: str

# Definicion del endpoint /chat

@routerChat.post("/chat")
def chat(query: Query):
    '''
    ## Endpoint `/ask`
    Devuelve una respuesta generada por un agente de IA basada en la pregunta del usuario.

    ### Parámetros (Body)
    - **question**: Pregunta que se le hace al agente de IA (ejemplo: _"¿Cuántos videojuegos desarrolló Nintendo en 2022 y qué porcentaje de ellos son gratuitos?"_).

    ### Respuesta
    - **answer**: Respuesta generada por el modelo de IA.
    '''
    # Aquí puedes invocar LangChain o cualquier lógica
    response = f"Recibí tu pregunta: {query.question}"
    return {"answer": response}
