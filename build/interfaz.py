from tkinter import Tk, Canvas, PhotoImage, Button, Entry

from pathlib import Path

from build.gui import relative_to_assets

import imagenes
import boton
import entrada

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Juanma\build\assets\frame0")


class Interfaz:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("827x642")
        self.window.configure(bg="#74296D")
        self.window.resizable(False, False)
        self.canvas = Canvas(
            self.window,
            bg="#74296D",
            height=642,
            width=827,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Crear instancias de las clases de botones
        self.boton_menos = boton.BotonMenos(self.canvas, self)
        self.boton_multiplicacion = boton.BotonMultiplicacion(self.canvas, self)
        self.boton_slash = boton.BotonSlash(self.canvas, self)
        self.boton_igual = boton.BotonIgual(self.canvas, self)
        self.boton_mas = boton.BotonMas(self.canvas, self)
        self.boton_punto = boton.BotonPunto(self.canvas, self)

        self.boton_numero_cero = boton.BotonNumeroCero(self.canvas, self)
        self.boton_numero_uno = boton.BotonNumeroUno(self.canvas, self)
        self.boton_numero_dos = boton.BotonNumeroDos(self.canvas, self)
        self.boton_numero_tres = boton.BotonNumeroTres(self.canvas, self)
        self.boton_numero_cuatro = boton.BotonNumeroCuatro(self.canvas, self)
        self.boton_numero_cinco = boton.BotonNumeroCinco(self.canvas, self)
        self.boton_numero_seis = boton.BotonNumeroSeis(self.canvas, self)
        self.boton_numero_siete = boton.BotonNumeroSiete(self.canvas, self)
        self.boton_numero_ocho = boton.BotonNumeroOcho(self.canvas, self)
        self.boton_numero_nueve = boton.BotonNumeroNueve(self.canvas, self)

        self.boton_estadisticas = boton.BotonEstadisticas(self.canvas)
        self.boton_guia = boton.BotonGuia(self.canvas)



        self.indice_entrada_actual = 0

        self.imagen_squirtle = imagenes.ImagenSquirtle(self.canvas)
        self.imagen_alien = imagenes.ImagenDeAlien(self.canvas)
        self.imagen_charizard = imagenes.ImagenDeCharizard(self.canvas)
        self.imagen_corazon = imagenes.ImagenDeCorazon(self.canvas)

        self.imagen_estrella_uno = imagenes.ImagenEstrella(self.canvas, "image_5.png", 55.000000953674316, 61.0)
        self.imagen_estrella_dos = imagenes.ImagenEstrella(self.canvas, "image_6.png", 518.0, 597.0)
        self.imagen_estrella_tres = imagenes.ImagenEstrella(self.canvas, "image_7.png", 342.0, 63.0)
        self.imagen_estrella_cuatro = imagenes.ImagenEstrella(self.canvas, "image_8.png", 222.00001525878906, 368.0)
        self.imagen_estrella_cinco = imagenes.ImagenEstrella(self.canvas, "image_9.png", 408.0, 278.0)
        self.imagen_estrella_seis = imagenes.ImagenEstrella(self.canvas, "image_10.png", 254.0, 610.0)
        self.imagen_estrella_siete = imagenes.ImagenEstrella(self.canvas, "image_11.png", 796.0, 227.0)
        self.imagen_estrella_ocho = imagenes.ImagenEstrella(self.canvas, "image_12.png", 54.999990463256836, 424.0)

        self.entrada_uno = entrada.EntradaUno(self.canvas)
        self.entrada_dos = entrada.EntradaCuatro(self.canvas)
        self.entrada_tres = entrada.EntradaCinco(self.canvas)
        self.entrada_cuatro = entrada.EntradaSeis(self.canvas)
        self.entrada_cinco = entrada.EntradaSiete(self.canvas)
        self.entrada_seis = entrada.EntradaDos(self.canvas)
        self.entrada_siete = entrada.EntradaTres(self.canvas)
        self.entrada_ocho = entrada.EntradaOcho(self.canvas)
        self.entrada_nueve = entrada.EntradaNueve(self.canvas)
        self.numero_vidas = entrada.NumeroVidas(self.canvas)

        self.entradas = [
                self.entrada_uno,
                self.entrada_dos,
                self.entrada_tres,
                self.entrada_cuatro,
                self.entrada_cinco,
                self.entrada_seis,
                self.entrada_siete,
                self.entrada_ocho,
                self.entrada_nueve
            ]

    def iniciar(self):
        self.window.mainloop()

    def insertar_simbolo(self, simbolo):
        if self.indice_entrada_actual < len(self.entradas):
            # Inserta el símbolo en el Entry actual
            self.entradas[self.indice_entrada_actual].entrada.insert(0, simbolo)

            # Incrementa el índice para el próximo Entry
            self.indice_entrada_actual += 1

            # Actualiza la interfaz
            self.window.update_idletasks()

interfaz = Interfaz()
interfaz.iniciar()
