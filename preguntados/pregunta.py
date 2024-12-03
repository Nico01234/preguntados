
class Pregunta:
    def __init__(self, question, opciones, respuesta_correcta):
        self.question = question
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta
    
    def validar_respuesta(self, respuesta_usuario):
        return respuesta_usuario == self.respuesta_correcta
    