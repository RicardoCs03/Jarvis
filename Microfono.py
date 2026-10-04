#Importaciones
import sounddevice as sd

#Clase Microfono
class Microfono():
    def __init__(self):
        self.id_dispositivo = None
        self.frecuencia = 44100
        self.canales = 1
        self.grabacion_actual = None

        


    def listen(self):
        print("Listening for commands...")

    def listar_dispositivos(self):
        devices = sd.query_devices()
        for i, device in enumerate(devices):
            print(f"{i}: {device['name']}")

    def seleccionar_microfono(self, indice:int):
        devices = sd.query_devices()    
        if 0 <= indice < len(devices):
            selected_device = devices[indice]
            print(f"Selected microphone: {selected_device['name']}")
            self.id_dispositivo = selected_device['index']
            sd.default.device[0] = self.id_dispositivo
            print(f"Device ID set to: {sd.default.device}")
        else:
            print("Invalid index. Please select a valid microphone index.")
            return

    def grabar(self, duration=5, fs=44100):
        print(f"Recording for {duration} seconds...")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=self.canales)
        sd.wait()  # Wait until recording is finished
        print("Recording finished.")
        self.grabacion_actual = recording

    def reproducir(self):
        if self.grabacion_actual is not None:
            print("Playing back the recording...")
            sd.play(self.grabacion_actual, samplerate=self.frecuencia)
            sd.wait()  # Wait until playback is finished
            print("Playback finished.")
        else:
            print("No recording available to play.")

    def usuario_solicita_dispositivo(self):
        self.listar_dispositivos()
        try:
            indice = int(input("Select a microphone by index: "))
            return self.seleccionar_microfono(indice)
        except ValueError:
            print("Please enter a valid integer.")
            return None
