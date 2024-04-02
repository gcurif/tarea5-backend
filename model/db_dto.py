from mongoengine import Document, StringField, IntField

class PreguntaDB(Document):
    texto = StringField(required=True)
    numero = IntField(required=True)

class RespuestaDB(Document):
    texto = StringField(required=True)
    id_pregunta = StringField(required=True)
