from tkinter import Tk, Canvas, PhotoImage, Button, Entry
from pathlib import Path

from build.gui import relative_to_assets

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Juanma\build\assets\frame0")


class Entrada:
    def __init__(self, canvas, imagen_archivo, x_imagen, y_imagen, x_entrada, y_entrada):
        canvas.create_rectangle(
            x_imagen - 20,
            y_imagen - 20,
            x_imagen + 20,
            y_imagen + 20,
            fill="#74296D",
            outline=""
        )
        self.imagen = PhotoImage(file=relative_to_assets(imagen_archivo))
        self.entry_bg = canvas.create_image(x_imagen, y_imagen, image=self.imagen)
        self.entrada = Entry(
            bd=1,  # Cambiado de 0 a 1 para agregar un borde
            bg="#B694FF",
            fg="#000716",
            highlightthickness=0
        )
        self.entrada.place(x=x_entrada, y=y_entrada, width=50, height=20)  # Agregué width y height aquí


class EntradaUno(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_1.png", 36.0, 118.0, 27.0, 41.0)


class EntradaDos(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_2.png", 468.0, 121.0, 27.0, 41.0)


class EntradaTres(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_3.png", 555.0, 122.0, 27.0, 41.0)


class EntradaCuatro(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_4.png", 122.0, 119.0, 27.0, 41.0)


class EntradaCinco(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_5.png", 209.0, 119.0, 27.0, 41.0)


class EntradaSeis(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_6.png", 294.0, 120.0, 27.0, 41.0)


class EntradaSiete(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_7.png", 381.0, 120.0, 27.0, 41.0)


class EntradaOcho(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_7.png", 642.0, 122.0, 27.0, 41.0)


class EntradaNueve(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_8.png", 729.0, 122.0, 27.0, 41.0)


class NumeroVidas(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_9.png", 451.0, 13.0, 49.0, 41.0)
