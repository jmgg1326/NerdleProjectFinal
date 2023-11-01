from tkinter import Tk, Canvas,  Label, Toplevel,  messagebox

from pathlib import Path

import imagenes
import boton
import entrada
from build.juego import Juego

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

        self.juego = Juego()
        self.numero_vidas = self.juego.vidas

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
        self.boton_guia = boton.BotonGuia(self.canvas, self)

        # Crea un botón para verificar la adivinanza
        self.boton_verificar = boton.BotonVerificar(self.canvas, self)

        # Crea un botón para limpiar los campos de entrada
        self.boton_limpiar = boton.BotonLimpiar(self.canvas, self)

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
        self.entrada_vidas = entrada.NumeroVidas(self.canvas)

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
        self.actualizar_vidas()
        self.window.mainloop()


    def verificar_adivinanza(self):
        # Obtiene la adivinanza del jugador de las entradas
        adivinanza = [ent.entrada.get() for ent in self.entradas]

        # Comprueba la adivinanza del jugador y obtiene el feedback
        feedback = self.juego.comprobar_adivinanza(adivinanza)

        # Actualiza el color de fondo de las entradas según el feedback
        for i in range(len(feedback)):
            color = feedback[i]
            self.entradas[i].entrada.config(bg=color)  # Cambia el color de fondo del Entry según el feedback

        # Si la adivinanza es correcta, muestra un mensaje de victoria y reinicia el juego
        if feedback == ['green'] * len(self.juego.secuencia_objetivo):
            messagebox.showinfo("¡Felicidades!", "¡Has ganado! Reiniciando el juego...")
            self.juego.estadisticas['victorias'] += 1
            self.juego.guardar_estadisticas()
            self.reiniciar_juego()

        # Si la adivinanza es incorrecta, reduce las vidas del jugador
        else:
            self.juego.vidas -= 1

            # Si no quedan vidas, muestra un mensaje de derrota y reinicia el juego
            if self.juego.vidas == 0:
                messagebox.showinfo("Lo siento", "¡Has perdido! Reiniciando el juego...")
                self.juego.estadisticas['derrotas'] += 1
                self.juego.guardar_estadisticas()
                self.mostrar_secuencia_objetivo()
                self.reiniciar_juego()

        # Actualiza las vidas en la interfaz
        self.actualizar_vidas()

        # Reinicia el índice del Entry para la próxima ronda
        self.indice_entrada_actual = 0

    def reiniciar_juego(self):
        # Reinicia el juego creando una nueva instancia de Juego y vaciando los campos de entrada
        self.juego = Juego()
        self.juego.vidas = self.numero_vidas  # Asegúrate de que las vidas se actualizan correctamente
        for ent in self.entradas:
            ent.entrada.delete(0, 'end')

    def vaciar_entradas(self):
        for ent in self.entradas:
            ent.entrada.delete(0, 'end')

    def insertar_simbolo(self, simbolo):
        if self.indice_entrada_actual < len(self.entradas):
            # Inserta el símbolo en el Entry actual
            self.entradas[self.indice_entrada_actual].entrada.insert(0, simbolo)

            # Incrementa el índice para el próximo Entry
            self.indice_entrada_actual += 1

            # Actualiza la interfaz
            self.window.update_idletasks()

    def limpiar_entradas(self):
        for ent in self.entradas:
            ent.entrada.delete(0, 'end')

    def actualizar_vidas(self):
        # Borra el contenido actual
        self.entrada_vidas.entrada.delete(0, 'end')

        # Inserta la vida actual del jugador
        self.entrada_vidas.entrada.insert(0, str(self.juego.vidas))

    def mostrar_secuencia_objetivo(self):
        # Crea una nueva ventana
        ventana = Toplevel(self.window)

        # Crea una etiqueta con la secuencia objetivo
        etiqueta = Label(ventana, text="Secuencia Objetivo: " + ''.join(self.juego.secuencia_objetivo))

        # Muestra la etiqueta
        etiqueta.pack()

    def guia(self):
        # Crea una nueva ventana
        ventana_guia = imagenes.Guia()
        ventana_guia.mostrar()


interfaz = Interfaz()
interfaz.iniciar()
