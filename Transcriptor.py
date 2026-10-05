import whisper
import numpy as np

class Transcriptor:
    def __init__(self):
        self.transcripcion = ""
        self.idioma="es"  # Idioma por defecto

    def modificar_lenguaje(self, idioma):
        # Aquí puedes agregar la lógica para cambiar el idioma del modelo de transcripción
        self.idioma = idioma
        print(f"Cambiando el idioma a: {self.idioma}")

    def listar_idiomas(self):
        # Aquí puedes agregar la lógica para listar los idiomas disponibles
        idiomas_disponibles = ["en", "es", "fr", "de"]
        print("Idiomas disponibles:")
        for idioma in idiomas_disponibles:
            print(f"- {idioma}")

    def seleccionar_idioma(self):
        # Aquí puedes agregar la lógica para seleccionar un idioma específico
        self.listar_idiomas()
        self.modificar_lenguaje(input("Ingrese el idioma que desea seleccionar: "))
        
    def transcribir(self, audio):
        # Cargar el modelo de transcripción
        model = whisper.load_model("base")
        # Transcribir el audio
        result = model.transcribe(np.squeeze(audio))
        self.transcripcion = result["text"]
        print(f"Transcripción: {self.transcripcion}")
        return