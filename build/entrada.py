from tkinter import PhotoImage, Entry
from pathlib import Path

CURRENT_PATH = Path(__file__).parent
ASSETS_PATH = CURRENT_PATH / "build" / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# clases de entradas , donde aparecera escogencias del usuario, principio OPEN-CLOSED
class Entrada:
    def __init__(self, canvas, imagen_archivo, x_imagen, y_imagen, x_entrada, y_entrada):
        self.imagen = PhotoImage(file=relative_to_assets(imagen_archivo))
        self.entry_bg = canvas.create_image(x_imagen, y_imagen, image=self.imagen)
        self.entrada = Entry(
            bd=0,  # Sin borde
            bg="#B694FF",
            fg="#000716",
            highlightthickness=0,  # Sin resaltado
            exportselection=False  # Deshabilita la opción de copiar
        )

        self.entrada.bind("<Key>", lambda e: "break")

        self.entrada.place(x=x_entrada + 10, y=y_entrada + 10, width=50, height=20)  # Ajusta las coordenadas aquí


class EntradaUno(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_1.png", 69, 139.5, 36.0, 118.0)


class EntradaDos(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_2.png", 501.5, 142.5, 468.0, 121.0)


class EntradaTres(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_3.png", 588.5, 143.5, 555.0, 122.0)


class EntradaCuatro(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_4.png", 155, 140.5, 122.0, 119.0)


class EntradaCinco(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_5.png", 241, 140.5, 209.0, 119.0)


class EntradaSeis(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_6.png", 327.5, 141.5, 294.0, 120.0)


class EntradaSiete(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_7.png", 413.5, 141.5, 381.0, 120.0)


class EntradaOcho(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_7.png", 674.5, 143.5, 642.0, 122.0)


class EntradaNueve(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_8.png", 762.5, 143.5, 729.0, 122.0)


class NumeroVidas(Entrada):
    def __init__(self, canvas):
        super().__init__(canvas, "entry_9.png", 475.5, 34.5, 440.0, 13.0)
