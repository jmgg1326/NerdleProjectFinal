import json
import random


class Juego:
    def __init__(self):
        # Los posibles elementos que pueden formar parte de la secuencia objetivo
        self.elementos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '=']

        # Genera la secuencia objetivo al inicio del juego
        self.secuencia_objetivo = self.generar_secuencia_objetivo()

        self.vidas = 3

        self.estadisticas = self.cargar_estadisticas()

    def cargar_estadisticas(self):
        try:
            with open('estadisticas.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"victorias": 0, "derrotas": 0}

    def guardar_estadisticas(self):
        with open('estadisticas.json', 'w') as f:
            json.dump(self.estadisticas, f)

    def generar_secuencia_objetivo(self):
        # Genera una secuencia aleatoria de 8 elementos
        return [random.choice(self.elementos) for _ in range(8)]
        # return "123456789"

    def comprobar_adivinanza(self, adivinanza):
        # Comprueba si la adivinanza del jugador coincide con la secuencia objetivo
        feedback = []
        for i in range(min(len(adivinanza), len(self.secuencia_objetivo))):
            if adivinanza[i] == self.secuencia_objetivo[i]:
                feedback.append('green')  # Elemento correcto en la posición correcta
            elif adivinanza[i] in self.secuencia_objetivo:
                feedback.append('yellow')  # Elemento correcto en la posición incorrecta
            else:
                feedback.append('red')  # Elemento incorrecto

        return feedback
