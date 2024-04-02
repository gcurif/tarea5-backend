from pydantic import BaseModel

class PreguntaDTO(BaseModel):
    texto: str
    numero: int

class RespuestaDTO(BaseModel):
    texto: str
    id_pregunta: str

