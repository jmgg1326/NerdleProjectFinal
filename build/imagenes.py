from tkinter import Tk, Canvas, PhotoImage, Button, Entry

from pathlib import Path

from build.gui import relative_to_assets

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Juanma\build\assets\frame0")


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