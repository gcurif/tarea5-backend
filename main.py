from fastapi import FastAPI
from model.api_dto import PreguntaDTO, RespuestaDTO
from model.db_dto import PreguntaDB, RespuestaDB
from database_manager import get_db

app = FastAPI()

@app.post("/preguntas/")
async def crear_pregunta(PreguntaDTO: PreguntaDTO):
    pregunta_db = PreguntaDB(**PreguntaDTO.dict())
    pregunta_db.save()
    return {"mensaje": "Pregunta creada con éxito"}

@app.post("/respuestas/")
async def crear_respuesta(respuesta: RespuestaDTO):
    respuesta_db = RespuestaDB(**respuesta.dict())
    respuesta_db.save()
    return {"mensaje": "Respuesta creada con éxito"}

@app.get("/preguntas/{pregunta_id}")
async def obtener_pregunta(pregunta_id: str):
    pregunta_db = PreguntaDB.objects(id=pregunta_id).first()
    if pregunta_db:
        return pregunta_db.to_json()
    return {"mensaje": "PreguntaDTO no encontrada"}

@app.get("/respuestas/{respuesta_id}")
async def obtener_respuesta(respuesta_id: str):
    respuesta_db = RespuestaDB.objects(id=respuesta_id).first()
    if respuesta_db:
        return respuesta_db.to_json()
    return {"mensaje": "Respuesta no encontrada"}
