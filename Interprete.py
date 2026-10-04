
class Interprete:
    def __init__(self):
        self.comando = ""

    def interpretar(self, comando):
        self.comando = comando
        # Aquí puedes agregar la lógica para interpretar el comando y ejecutar acciones
        print(f"Interpretando comando: {self.comando}")