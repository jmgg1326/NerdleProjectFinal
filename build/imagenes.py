import os
from tkinter import PhotoImage, Tk, Canvas

from pathlib import Path

CURRENT_PATH = Path(__file__).parent
ASSETS_PATH = CURRENT_PATH / "assets" / "frame0"


def relative_to_assets(path: str) -> str:
    return os.path.join(ASSETS_PATH, path)


# clases encargadas de las imagenes, principio OPEN-CLOSED
class Imagen:
    def __init__(self, canvas, imagen_archivo, x, y):
        self.imagen = PhotoImage(file=relative_to_assets(imagen_archivo))
        self.canvas = canvas.create_image(x, y, image=self.imagen)


class ImagenSquirtle(Imagen):
    def __init__(self, canvas):
        super().__init__(canvas, "image_2.png", 760.0, 592.0)


class ImagenDeAlien(Imagen):
    def __init__(self, canvas):
        super().__init__(canvas, "image_1.png", 209.0, 35.0)


class ImagenDeCharizard(Imagen):
    def __init__(self, canvas):
        super().__init__(canvas, "image_3.png", 90.0, 573.0)


class ImagenDeCorazon(Imagen):
    def __init__(self, canvas):
        super().__init__(canvas, "image_4.png", 558.0, 27.77828073501587)


class ImagenEstrella(Imagen):
    def __init__(self, canvas, imagen_archivo, x, y):
        super().__init__(canvas, imagen_archivo, x, y)


class Guia:
    def __init__(self):
        self.image_1 = None
        self.my_image = None
        self.window = Tk()
        self.window.geometry("1440x900")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=900,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.canvas.create_text(
            1.0,
            235.00000000000006,
            anchor="nw",
            text="REALIZAR UNA ADIVINANZA: EN CADA TURNO, EL JUGADOR PROPONE UNA SECUENCIA DE 8 ELEMENTOS QUE CREE QUE COINCIDE CON LA SECUENCIA OBJETIVO. PARA HACER ESTO, EL JUGADOR DEBE HACER CLIC EN LOS BOTONES CORRESPONDIENTES EN LA INTERFAZ GRÁFICA DE USUARIO PARA INSERTAR NÚMEROS Y OPERADORES EN LAS ENTRADAS. POR EJEMPLO, UNA ADIVINANZA PODRÍA SER “3 + 7 * 2 = 17”.",
            fill="#000000",
            font=("PressStart2P Regular", 15 * -1)
        )

        self.canvas.create_text(
            48.0,
            324.00000000000006,
            anchor="nw",
            text="VERIFICAR LA ADIVINANZA: UNA VEZ QUE EL JUGADOR HA INGRESADO SU ADIVINANZA, DEBE HACER CLIC EN EL BOTÓN “VERIFICAR” PARA COMPROBAR SU ADIVINANZA. EL JUEGO PROPORCIONARÁ RETROALIMENTACIÓN SOBRE LA ADIVINANZA DEL JUGADOR.",
            fill="#000000",
            font=("PressStart2P Regular", 15 * -1)
        )

        self.canvas.create_text(
            10.0,
            659.0,
            anchor="nw",
            text="VIDAS: EL JUGADOR COMIENZA CON UN NÚMERO DETERMINADO DE VIDAS (EN TU CASO, SON 3 VIDAS). CADA VEZ QUE EL JUGADOR HACE UNA ADIVINANZA INCORRECTA, PIERDE UNA VIDA. EL NÚMERO DE VIDAS RESTANTES SE MUESTRA CONSTANTEMENTE EN LA INTERFAZ GRÁFICA DE USUARIO.",
            fill="#000000",
            font=("PressStart2P Regular", 15 * -1)
        )

        self.canvas.create_text(
            33.0,
            759.0,
            anchor="nw",
            text="FIN DEL JUEGO: EL JUEGO TERMINA CUANDO EL JUGADOR ADIVINA CORRECTAMENTE LA SECUENCIA OBJETIVO O CUANDO SE AGOTAN TODAS LAS VIDAS. SI EL JUGADOR GANA, SE MOSTRARÁ UN MENSAJE DE VICTORIA Y EL JUEGO SE REINICIARÁ. SI EL JUGADOR PIERDE, SE MOSTRARÁ UN MENSAJE DE DERROTA Y SE REVELARÁ LA SECUENCIA OBJETIVO.",
            fill="#000000",
            font=("PressStart2P Regular", 15 * -1)
        )

        self.canvas.create_text(
            33.0,
            449.00000000000006,
            anchor="nw",
            text="RETROALIMENTACIÓN: DESPUÉS DE CADA INTENTO, EL JUEGO PROPORCIONA RETROALIMENTACIÓN PRECISA EN TRES CATEGORÍAS:\nELEMENTO CORRECTO EN LA POSICIÓN CORRECTA: LOS ELEMENTOS QUE ESTÁN EN LA SECUENCIA Y EN LA POSICIÓN CORRECTA SE MARCARÁN EN VERDE.\n\nELEMENTO CORRECTO EN LA POSICIÓN INCORRECTA: LOS ELEMENTOS QUE ESTÁN EN LA SECUENCIA, PERO EN LA POSICIÓN INCORRECTA SE MARCARÁN EN AMARILLO.\n\nELEMENTO INCORRECTO: LOS ELEMENTOS QUE NO ESTÁN EN LA SECUENCIA OBJETIVO SE MARCARÁN EN GRIS.",
            fill="#000000",
            font=("PressStart2P Regular", 15 * -1)
        )

        self.canvas.create_text(
            600.0,
            36.00000000000006,
            anchor="nw",
            text="NEERDLE!\n\n",
            fill="#000000",
            font=("PressStart2P Regular", 30 * -1)
        )

        self.canvas.create_text(
            33.0,
            114.00000000000006,
            anchor="nw",
            text="INICIO DEL JUEGO: AL INICIAR EL JUEGO, SE GENERA UNA SECUENCIA OBJETIVO DE 8 ELEMENTOS. \nESTOS ELEMENTOS PUEDEN SER NÚMEROS DEL 0 AL 9, OPERACIONES MATEMÁTICAS (+, -, *, /) \nY EL SIGNO DE IGUALDAD (=). ESTA SECUENCIA ES SECRETA Y EL OBJETIVO DEL JUGADOR ES ADIVINARLA.",
            fill="#000000",
            font=("PressStart2P Regular", 15 * -1)
        )

    def mostrar(self):
        self.window.resizable(False, False)
        self.window.mainloop()
