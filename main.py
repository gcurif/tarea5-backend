from fastapi import FastAPI, HTTPException
from model.api_dto import PreguntaDTO, RespuestaDTO
from model.db_dto import PreguntaDB, RespuestaDB
from database_manager import get_db
from typing import List

app = FastAPI()
get_db()

@app.get("/preguntas", response_model=List[PreguntaDTO])
def obtener_preguntas():
    preguntas = PreguntaDB.objects()

    # PISTA MODIFICANDO BACK

    # aqui transformo los objetos obtenidos en base de datos en objetos de api
    preguntasDTOs = []
    for pregunta in preguntas:
        preguntasDTOs.append(PreguntaDTO(**pregunta.to_mongo().to_dict()))


    # hola, soy la pregunta 0, y me van a modificar :D
    print('hola, soy la pregunta 0, y me van a modificar desde el back :D', preguntasDTOs[0])
    preguntasDTOs[0].pistaBack = "Hola, yo vengo modificada desde el back :D"
    preguntasDTOs[0].respuesta.texto = preguntasDTOs[0].respuesta.texto  + " (ya wn aki viene una pista del back, esto esta re izi)"

    return preguntasDTOs

@app.get("/preguntas/{numero}", response_model=PreguntaDTO)
def obtener_pregunta(numero: int):
    pregunta = PreguntaDB.objects(numero=numero).first()
    if pregunta:
        return PreguntaDTO(**pregunta.to_mongo().to_dict())
    raise HTTPException(status_code=404, detail="Pregunta no encontrada")

@app.post("/preguntas", response_model=PreguntaDTO)
def crear_pregunta(pregunta: PreguntaDTO):
    nueva_pregunta = PreguntaDB(**pregunta.dict())
    nueva_pregunta.save()
    return PreguntaDTO(**nueva_pregunta.to_mongo().to_dict())

@app.post("/preguntas/{numero}/respuesta", response_model=PreguntaDTO)
def agregar_respuesta(numero: int, respuesta: RespuestaDTO):

    #PISTA FUNCIÓN DE LA API
    print("holaaaa, soy un endpoint de api indefensoooo 1313")
    print("dame tu respuesta papuuu 1313")
    pregunta = PreguntaDB.objects(numero=numero).first()
    if pregunta:
        pregunta.respuesta = RespuestaDB(**respuesta.dict())
        pregunta.save()
        return PreguntaDTO(**pregunta.to_mongo().to_dict())
    raise HTTPException(status_code=404, detail="Pregunta no encontrada")
