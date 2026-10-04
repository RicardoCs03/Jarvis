#Imports
import Microfono as mic
#Class Definitions


class Javis():
    def __init__(self):
        pass

    def greet(self):
        print("Hello! I am Javis, your personal assistant.")

    def perform_task(self, task):
        print(f"Performing the task: {task}")

if __name__ == "__main__":
    assistant = Javis()
    assistant.greet()
    #task = input("What task would you like me to perform? ")
    #assistant.perform_task(task)
    microfono = mic.Microfono()
    microfono.usuario_solicita_dispositivo()
    microfono.grabar(duration=5)
    microfono.reproducir()
