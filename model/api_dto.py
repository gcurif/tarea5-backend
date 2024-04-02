from pydantic import BaseModel

class RespuestaDTO(BaseModel):
    texto: str
    archivo: str

class PreguntaDTO(BaseModel):
    texto: str
    numero: int
    respuesta : RespuestaDTO = None
    pistaBack : str = ''
