from pydantic import BaseModel, Field
from fastapi import APIRouter

routerChat = APIRouter()

# Definicion del Modelo de los datos
class Query(BaseModel):
    question: str

# Definicion del e 
@routerChat.post("/chat")
def chat(query: Query):
    '''
    <strong>Devuelve un diccionario año, cantidad de items y porcentaje de contenido libre por empresa desarrolladora</strong>
             
    Parametro
    ---------  
            question : Pregunta que se le hace al agente de IA, por ejemplo:
            "¿Cuántos videojuegos desarrolló Nintendo en 2022 y qué porcentaje de ellos son gratuitos?"
    
    Retorna
    -------
            answer   : Respuesta del agente de IA

    '''
    # Aquí puedes invocar LangChain o cualquier lógica
    response = f"Recibí tu pregunta: {query.question}"
    return {"answer": response}
