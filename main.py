from fastapi import FastAPI, Body, Path, Query, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from typing import List, Optional
import uvicorn
from pathlib import Path
import os
from routers.agents import routerChat

# from fastapi.security import HTTPBearer
#from user_jwt import crearTokenJWT, validateTokenJWT
#from db.database import Session, engine, Base
#from models.movie import Movie as ModelMovie  
# from fastapi.encoders import jsonable_encoder  
#from routers.movie import routerMovie
#from routers.user import routerLogin


app = FastAPI(
    title = "Implementación de un agente de IA",
    description= "API construida con LangChain que implementa un agente de IA",
    version = "0.0.1"
)

app.include_router(routerChat, tags=["Chat"])

# Ruta absoluta al archivo HTML
HTML_PATH = Path(__file__).parent / "./templates" / "inicio.html"

@app.get("/", tags=["Inicio"])
def read_root(): 
    print (HTML_PATH) 
    return FileResponse(HTML_PATH)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)