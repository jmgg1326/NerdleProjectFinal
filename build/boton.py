from tkinter import Tk, Canvas, PhotoImage, Button, Entry

from pathlib import Path

from build.gui import relative_to_assets
from build.informacion import Informacion

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Juanma\build\assets\frame0")


class Boton:
    def __init__(self, canvas, imagen_archivo, x, y, width, height, interfaz, simbolo):
        self.imagen = PhotoImage(file=relative_to_assets(imagen_archivo))
        self.boton = Button(
            image=self.imagen,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: interfaz.insertar_simbolo(simbolo),
            relief="flat"
        )
        self.boton.place(x=x, y=y, width=width, height=height)


class BotonMenos(Boton):
    def __init__(self, canvas, interfaz):
        super().__init__(canvas, "button_1.png", 67.0, 431.0, 141.0, 67.0, interfaz, "-")


class BotonMultiplicacion(Boton):
    def __init__(self, canvas, interfaz):
        super().__init__(canvas, "button_2.png", 249.0, 434.0, 141.0, 67.0, interfaz, "*")


class BotonSlash(Boton):
    def __init__(self, canvas, interfaz):
        super().__init__(canvas, "button_3.png", 437.0, 436.0, 141.0, 62.0, interfaz, "/")


class BotonPunto(Boton):
    def __init__(self, canvas, interfaz):
        super().__init__(canvas, "button_4.png", 618.0, 431.0, 141.0, 67.0, interfaz, ".")


class BotonIgual(Boton):
    def __init__(self, canvas, interfaz):
        super().__init__(canvas, "button_5.png", 622.0, 356.0, 141.0, 67.0, interfaz, "=")


class BotonNumeroSeis(Boton):
    def __init__(self, canvas, interfaz):
        super().__init__(canvas, "button_6.png", 249.0, 280.0, 141.0, 67.0, interfaz, "6")


class BotonNumeroDos(Boton):
    def __init__(self, canvas, interfaz):
        super().__init__(canvas, "button_7.png", 249.0, 208.0, 141.0, 67.0, interfaz, "2")


class BotonNumeroUno(Boton):
    def __init__(self, canvas, interfaz):
        super().__init__(canvas, "button_8.png", 63.0, 206.0, 141.0, 67.0, interfaz, "1")


class BotonNumeroTres(Boton):
    def __init__(self, canvas, interfaz):
        super().__init__(canvas, "button_9.png", 433.0, 208.0, 141.0, 67.0, interfaz, "3")


class BotonNumeroSiete(Boton):
    def __init__(self, canvas, interfaz):
        super().__init__(canvas, "button_10.png", 438.0, 285.0, 141.0, 67.0, interfaz, "7")


class BotonMas(Boton):
    def __init__(self, canvas, interfaz):
        super().__init__(canvas, "button_11.png", 437.0, 356.0, 141.0, 67.0, interfaz, "+")


class BotonNumeroCinco(Boton):
    def __init__(self, canvas, interfaz):
        super().__init__(canvas, "button_12.png", 65.0, 282.0, 141.0, 67.0, interfaz, "5")


class BotonNumeroNueve(Boton):
    def __init__(self, canvas, interfaz):
        super().__init__(canvas, "button_13.png", 65.0, 358.0, 141.0, 67.0, interfaz, "9")


class BotonNumeroCero(Boton):
    def __init__(self, canvas, interfaz):
        super().__init__(canvas, "button_14.png", 249.0, 359.0, 141.0, 67.0, interfaz, "0")


class BotonNumeroCuatro(Boton):
    def __init__(self, canvas, interfaz):
        super().__init__(canvas, "button_15.png", 615.0, 219.0, 141.0, 68.0, interfaz, "4")


class BotonNumeroOcho(Boton):
    def __init__(self, canvas, interfaz):
        super().__init__(canvas, "button_16.png", 622.0, 280.0, 141.0, 67.0, interfaz, "8")


class BotonEstadisticas:
    def __init__(self, canvas, interfaz):
        self.interfaz = interfaz
        self.imagen = PhotoImage(file=relative_to_assets("button_17.png"))
        self.boton = Button(
            image=self.imagen,
            borderwidth=0,
            highlightthickness=0,
            command=self.on_click,
            relief="flat"
        )
        self.boton.place(x=639.0, y=1.0, width=71.0, height=58.0)

    def on_click(self):
        print("BotonEstadisticas clicked")
        #  poner el código para mostrar las estadísticas
        informacion = Informacion(self.interfaz.juego)
        informacion.crear_grafico()
        informacion.enviar_por_correo('direccion_de_correo@ejemplo.com')



class BotonGuia:
    def __init__(self, canvas, interfaz):
        self.imagen = PhotoImage(file=relative_to_assets("button_18.png"))
        self.boton = Button(
            image=self.imagen,
            borderwidth=0,
            highlightthickness=0,
            command=interfaz.guia,
            relief="flat"
        )
        self.boton.place(x=747.0, y=0, width=60.0, height=58.0)

    def on_click(self):
        print("BotonGuia clicked")
        # Aquí puedes poner el código para mostrar la guía


class BotonVerificar:

    def __init__(self, canvas, interfaz):
        self.imagen = PhotoImage(file=relative_to_assets("verificar.png"))
        self.boton = Button(
            image=self.imagen,
            borderwidth=0,
            highlightthickness=0,
            command=interfaz.verificar_adivinanza,
            relief="flat"
        )
        self.boton.place(x=252, y=526, width=93.0, height=62.0)


class BotonLimpiar:

    def __init__(self, canvas, interfaz):
        self.imagen = PhotoImage(file=relative_to_assets("Limpiar.png"))
        self.boton = Button(
            image=self.imagen,
            borderwidth=0,
            highlightthickness=0,
            command=interfaz.vaciar_entradas,
            relief="flat"
        )
        self.boton.place(x=432, y=526, width=93.0, height=62.0)


