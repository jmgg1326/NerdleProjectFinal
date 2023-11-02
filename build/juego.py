import json
import random


class Juego:
    def __init__(self):
        # Los posibles elementos que pueden formar parte de la secuencia objetivo
        self.elementos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '=']

        # Genera la secuencia objetivo al inicio del juego
        self.secuencia_objetivo = self.generar_secuencia_objetivo()

        self.vidas = 3

        # se crea el archivo json para almacenar victorias y derrotas
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
        # Genera cuatro números aleatorios
        num1 = str(random.randint(10, 99))
        num2 = str(random.randint(10, 99))

        # Genera una operación aleatoria
        operacion = random.choice(['+', '-', '*', '/'])

        # Calcula el resultado de la operación
        resultado = str(int(eval(num1 + operacion + num2)))

        # Crea la secuencia objetivo
        secuencia_objetivo = list(num1 + operacion + num2 + "=" + resultado)

        return secuencia_objetivo

    def comprobar_adivinanza(self, adivinanza):
        # Comprueba si la adivinanza del jugador coincide con la secuencia objetivo
        feedback = []
        for i in range(min(len(adivinanza), len(self.secuencia_objetivo))):
            if adivinanza[i] == self.secuencia_objetivo[i]:
                feedback.append('green')  # Elemento correcto en la posición correcta
            elif adivinanza[i] in self.secuencia_objetivo:
                feedback.append('yellow')  # Elemento correcto en la posición incorrecta
            else:
                feedback.append('#808080')  # Elemento incorrecto gray color

        return feedback
