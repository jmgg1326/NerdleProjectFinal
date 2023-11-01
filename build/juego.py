import random


class Juego:
    def __init__(self):
        # Los posibles elementos que pueden formar parte de la secuencia objetivo
        self.elementos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '=']

        # Genera la secuencia objetivo al inicio del juego
        self.secuencia_objetivo = self.generar_secuencia_objetivo()

        self.vidas = 3

    def generar_secuencia_objetivo(self):
        # Genera una secuencia aleatoria de 8 elementos
        return [random.choice(self.elementos) for _ in range(8)]

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


