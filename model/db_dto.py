from mongoengine import Document, EmbeddedDocument, StringField, IntField, EmbeddedDocumentField

class RespuestaDB(EmbeddedDocument):
    texto = StringField(required=True)
    archivo = StringField(required=True)

class PreguntaDB(Document):
    texto = StringField(required=True)
    numero = IntField(required=True)
    respuesta = EmbeddedDocumentField(RespuestaDB)
    pistaBack = StringField(required=False)