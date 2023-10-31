# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Juanma\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Interfaz:

    def __init__(self):
        self.window = Tk()

        self.window.geometry("827x642")
        self.window.configure(bg="#74296D")
        self.window.resizable(False, False)

        self.canvas = None

        self.imagen_alien = None
        self.canva_alien = None

        self.imagen_squirtle = None
        self.canva_pokemon_squirtle = None

        self.imagen_charizard = None
        self.canva_pokemon_charizard = None

        self.imagen_estrella_uno = None
        self.canvas_estrella_uno = None

        self.imagen_estrella_dos = None
        self.canvas_estrella_dos = None

        self.imagen_estrella_tres = None
        self.canvas_estrella_tres = None

        self.imagen_estrella_cuatro = None
        self.canvas_estrella_cuatro = None

        self.imagen_estrella_cinco = None
        self.canvas_estrella_cinco = None

        self.imagen_estrella_seis = None
        self.canvas_estrella_seis = None

        self.imagen_estrella_siete = None
        self.canvas_estrella_siete = None

        self.imagen_estrella_ocho = None
        self.canvas_estrella_ocho = None

        self.imagen_boton_menos = None
        self.boton_menos = None

        self.imagen_boton_multiplicacion = None
        self.boton_multiplicacion = None

        self.imagen_boton_slash = None
        self.boton_slash = None

        self.imagen_boton_punto = None
        self.boton_punto = None

        self.imagen_boton_igual = None
        self.boton_igual = None

        self.imagen_boton_numero_seis = None
        self.boton_numero_seis = None

        self.imagen_boton_numero_dos = None
        self.boton_numero_dos = None

        self.imagen_boton_numero_uno = None
        self.boton_numero_uno = None

        self.imagen_boton_numero_tres = None
        self.boton_numero_tres = None

        self.imagen_boton_numero_siete = None
        self.boton_numero_siete = None

        self.imagen_boton_mas = None
        self.boton_mas = None

        self.imagen_boton_numero_cinco = None
        self.boton_numero_cinco = None

        self.imagen_boton_numero_nueve = None
        self.boton_numero_nueve = None

        self.imagen_boton_numero_cero = None
        self.boton_numero_cero = None

        self.imagen_boton_numero_cuatro = None
        self.boton_numero_cuatro = None

        self.imagen_boton_numero_ocho = None
        self.boton_numero_ocho = None




        self.entry_bg_1 = None
        self.imagen_entrada_uno = None
        self.entrada_uno = None

        self.entry_bg_2 = None
        self.imagen_entrada_dos = None
        self.entrada_dos = None

        self.entry_bg_3 = None
        self.imagen_entrada_tres = None
        self.entrada_tres = None

        self.entry_bg_4 = None
        self.imagen_entrada_cuatro = None
        self.entrada_cuatro = None

        self.entry_bg_5 = None
        self.imagen_entrada_cinco = None
        self.entrada_cinco = None

        self.entry_bg_6 = None
        self.imagen_entrada_seis = None
        self.entrada_seis = None

        self.entry_bg_7 = None
        self.imagen_entrada_siete = None
        self.entrada_siete = None

        self.entry_bg_8 = None
        self.imagen_entrada_ocho = None
        self.entrada_ocho = None

        self.entry_bg_9 = None
        self.imagen_entrada_nueve = None
        self.entrada_nueve = None

        self.imagen_boton_estadisticas = None
        self.boton_estadisticas = None

        self.imagen_boton_guia = None
        self.boton_guia = None

        self.imagen_corazon = None
        self.canva_corazon = None

        self.entry_bg_numero_vidas = None
        self.imagen_numero_vidas = None
        self.numero_vidas = None









    def graficos_ventana(self):

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


    def imagen_de_alien(self):
        self.imagen_alien = PhotoImage(
            file=relative_to_assets("image_1.png"))

        self.canva_alien = self.canvas.create_image(
            209.0,
            35.0,
            image=self.imagen_alien
        )

    def imagen_de_corazon(self):
        self.imagen_corazon = PhotoImage(
            file=relative_to_assets("image_4.png"))

        self.canva_corazon = self.canvas.create_image(
            558.0,
            27.77828073501587,
            image=self.imagen_corazon
        )

    def imagen_de_squirtle(self):
        self.imagen_squirtle = PhotoImage(
            file=relative_to_assets("image_2.png"))

        self.canva_pokemon_squirtle = self.canvas.create_image(
            760.0,
            592.0,
            image=self.imagen_squirtle
        )

    def imagen_de_charizard(self):
        self.imagen_charizard = PhotoImage(
            file=relative_to_assets("image_3.png"))

        self.canva_pokemon_charizard = self.canvas.create_image(
            90.0,
            573.0,
            image=self.imagen_charizard
        )

    def imagenes_de_estrellas(self):
        # 1 estrella
        self.imagen_estrella_uno = PhotoImage(
            file=relative_to_assets("image_5.png"))

        self.canvas_estrella_uno = self.canvas.create_image(
            55.000000953674316,
            61.0,
            image=self.imagen_estrella_uno
        )

        # 2 estrella
        self.imagen_estrella_dos = PhotoImage(
            file=relative_to_assets("image_6.png"))

        self.canvas_estrella_dos = self.canvas.create_image(
            518.0,
            597.0,
            image=self.imagen_estrella_dos
        )

        # 3 estrella
        self.imagen_estrella_tres = PhotoImage(
            file=relative_to_assets("image_7.png"))

        self.canvas_estrella_tres = self.canvas.create_image(
            342.0,
            63.0,
            image=self.imagen_estrella_tres
        )

        # 4 estrella
        self.imagen_estrella_cuatro = PhotoImage(
            file=relative_to_assets("image_8.png"))

        self.canvas_estrella_cuatro = self.canvas.create_image(
            222.00001525878906,
            368.0,
            image=self.imagen_estrella_cuatro
        )

        # 5 estrella
        self.imagen_estrella_cinco = PhotoImage(
            file=relative_to_assets("image_9.png"))

        self.canvas_estrella_cinco = self.canvas.create_image(
            408.0,
            278.0,
            image=self.imagen_estrella_cinco
        )

        #  6 estrella
        self.imagen_estrella_seis = PhotoImage(
            file=relative_to_assets("image_10.png"))

        self.canvas_estrella_seis = self.canvas.create_image(
            254.0,
            610.0,
            image=self.imagen_estrella_seis
        )

        # 7 estrella
        self.imagen_estrella_siete = PhotoImage(
            file=relative_to_assets("image_11.png"))

        self.canvas_estrella_siete = self.canvas.create_image(
            796.0,
            227.0,
            image=self.imagen_estrella_siete
        )

        # 8 estrella
        self.imagen_estrella_ocho = PhotoImage(
            file=relative_to_assets("image_12.png"))

        self.canvas_estrella_ocho = self.canvas.create_image(
            54.999990463256836,
            424.0,
            image=self.imagen_estrella_ocho
        )

    def boton_de_menos(self):
        self.imagen_boton_menos = PhotoImage(
            file=relative_to_assets("button_1.png"))

        self.boton_menos = Button(
            image=self.imagen_boton_menos,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.boton_menos.place(
            x=67.0,
            y=431.0,
            width=141.0,
            height=67.0
        )

    def boton_de_multiplicacion(self):
        self.imagen_boton_multiplicacion = PhotoImage(
            file=relative_to_assets("button_2.png"))

        self.boton_multiplicacion = Button(
            image=self.imagen_boton_multiplicacion,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )

        self.boton_multiplicacion.place(
            x=249.0,
            y=434.0,
            width=141.0,
            height=67.0
        )

    def boton_de_slash(self):
        self.imagen_boton_slash = PhotoImage(
            file=relative_to_assets("button_3.png"))

        self.boton_slash = Button(
            image=self.imagen_boton_slash,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )

        self.boton_slash.place(
            x=437.0,
            y=436.0,
            width=141.0,
            height=62.0
        )

    def boton_de_punto(self):

        self.imagen_boton_punto = PhotoImage(
            file=relative_to_assets("button_4.png"))

        self.boton_punto = Button(
            image=self.imagen_boton_punto,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )

        self.boton_punto.place(
            x=618.0,
            y=431.0,
            width=141.0,
            height=67.0
        )

    def boton_de_igual(self):
        self.imagen_boton_igual = PhotoImage(
            file=relative_to_assets("button_5.png"))

        self.boton_igual = Button(
            image=self.imagen_boton_igual,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )

        self.boton_igual.place(
            x=622.0,
            y=356.0,
            width=141.0,
            height=67.0
        )

    def boton_de_numero_seis(self):
        self.imagen_boton_numero_seis = PhotoImage(
            file=relative_to_assets("button_6.png"))

        self.boton_numero_seis = Button(
            image=self.imagen_boton_numero_seis,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )

        self.boton_numero_seis.place(
            x=249.0,
            y=280.0,
            width=141.0,
            height=67.0
        )

    def boton_de_numero_dos(self):
        self.imagen_boton_numero_dos = PhotoImage(
            file=relative_to_assets("button_7.png"))

        self.boton_numero_dos = Button(
            image=self.imagen_boton_numero_dos,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )

        self.boton_numero_dos.place(
            x=249.0,
            y=208.0,
            width=141.0,
            height=65.0
        )

    def boton_de_numero_uno(self):
        self.imagen_boton_numero_uno = PhotoImage(
            file=relative_to_assets("button_8.png"))

        self.boton_numero_uno = Button(
            image=self.imagen_boton_numero_uno,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )

        self.boton_numero_uno.place(
            x=63.0,
            y=206.0,
            width=141.0,
            height=67.0
        )

    def boton_de_numero_tres(self):
        self.imagen_boton_numero_tres = PhotoImage(
            file=relative_to_assets("button_9.png"))

        self.boton_numero_tres = Button(
            image=self.imagen_boton_numero_tres,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        self.boton_numero_tres.place(
            x=433.0,
            y=208.0,
            width=141.0,
            height=67.0
        )

    def boton_de_numero_siete(self):
        self.imagen_boton_numero_siete = PhotoImage(
            file=relative_to_assets("button_10.png"))

        self.boton_numero_siete = Button(
            image=self.imagen_boton_numero_siete,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        self.boton_numero_siete.place(
            x=438.0,
            y=285.0,
            width=136.0,
            height=64.0
        )

    def boton_de_mas(self):
        self.imagen_boton_mas = PhotoImage(
            file=relative_to_assets("button_11.png"))

        self.boton_mas = Button(
            image=self.imagen_boton_mas,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_11 clicked"),
            relief="flat"
        )

        self.boton_mas.place(
            x=437.0,
            y=356.0,
            width=141.0,
            height=67.0
        )

    def boton_de_numero_cinco(self):
        self.imagen_boton_numero_cinco = PhotoImage(
            file=relative_to_assets("button_12.png"))

        self.boton_numero_cinco = Button(
            image=self.imagen_boton_numero_cinco,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_12 clicked"),
            relief="flat"
        )

        self.boton_numero_cinco.place(
            x=65.0,
            y=282.0,
            width=141.0,
            height=67.0
        )

    def boton_de_numero_nueve(self):
        self.imagen_boton_numero_nueve = PhotoImage(
            file=relative_to_assets("button_13.png"))

        self.boton_numero_nueve = Button(
            image=self.imagen_boton_numero_nueve,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_13 clicked"),
            relief="flat"
        )

        self.boton_numero_nueve.place(
            x=65.0,
            y=358.0,
            width=141.0,
            height=67.0
        )

    def boton_de_numero_cero(self):
        self.imagen_boton_numero_cero = PhotoImage(
            file=relative_to_assets("button_14.png"))

        self.boton_numero_cero = Button(
            image=self.imagen_boton_numero_cero,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_14 clicked"),
            relief="flat"
        )

        self.boton_numero_cero.place(
            x=249.0,
            y=359.0,
            width=141.0,
            height=67.0
        )

    def boton_de_numero_cuatro(self):
        self.imagen_boton_numero_cuatro = PhotoImage(
            file=relative_to_assets("button_15.png"))

        self.boton_numero_cuatro = Button(
            image=self.imagen_boton_numero_cuatro,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_15 clicked"),
            relief="flat"
        )
        self.boton_numero_cuatro.place(
            x=615.0,
            y=219.0,
            width=145.0,
            height=68.0
        )

    def boton_de_numero_ocho(self):
        self.imagen_boton_numero_ocho = PhotoImage(
            file=relative_to_assets("button_16.png"))

        self.boton_numero_ocho = Button(
            image=self.imagen_boton_numero_ocho,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_16 clicked"),
            relief="flat"
        )

        self.boton_numero_ocho.place(
            x=622.0,
            y=280.0,
            width=141.0,
            height=67.0
        )

    def entrada_de_uno(self):
        self.canvas.create_rectangle(
            8.0,
            111.0,
            93.0,
            167.0,
            fill="#74296D",
            outline="")

        self.imagen_entrada_uno = PhotoImage(
            file=relative_to_assets("entry_1.png"))

        self.entry_bg_1 = self.canvas.create_image(
            49.5,
            139.5,
            image=self.imagen_entrada_uno
        )

        self.entrada_uno = Entry(
            bd=0,
            bg="#B694FF",
            fg="#000716",
            highlightthickness=0
        )

        self.entrada_uno.place(
            x=36.0,
            y=118.0,
            width=27.0,
            height=41.0
        )

    def entrada_de_numero_dos(self):
        self.canvas.create_rectangle(
            440.0,
            114.0,
            525.0,
            170.0,
            fill="#74296D",
            outline="")

        self.entrada_dos = PhotoImage(
            file=relative_to_assets("entry_2.png"))

        self.entry_bg_2 = self.canvas.create_image(
            481.5,
            142.5,
            image=self.entrada_dos
        )
        self.entrada_dos = Entry(
            bd=0,
            bg="#B694FF",
            fg="#000716",
            highlightthickness=0
        )

        self.entrada_dos.place(
            x=468.0,
            y=121.0,
            width=27.0,
            height=41.0
        )

    def entrada_de_numero_tres(self):
        self.canvas.create_rectangle(
            527.0,
            115.0,
            612.0,
            171.0,
            fill="#74296D",
            outline="")

        self.imagen_entrada_tres = PhotoImage(
            file=relative_to_assets("entry_3.png"))

        self.entry_bg_3 = self.canvas.create_image(
            568.5,
            143.5,
            image=self.imagen_entrada_tres
        )
        self.entrada_tres = Entry(
            bd=0,
            bg="#B694FF",
            fg="#000716",
            highlightthickness=0
        )

        self.entrada_tres.place(
            x=555.0,
            y=122.0,
            width=27.0,
            height=41.0
        )

    def entrada_de_numero_cuatro(self):
        self.canvas.create_rectangle(
            94.0,
            112.0,
            179.0,
            168.0,
            fill="#74296D",
            outline="")

        self.imagen_entrada_cuatro = PhotoImage(
            file=relative_to_assets("entry_4.png"))

        self.entry_bg_4 = self.canvas.create_image(
            135.5,
            140.5,
            image=self.imagen_entrada_cuatro
        )
        self.entrada_cuatro = Entry(
            bd=0,
            bg="#B694FF",
            fg="#000716",
            highlightthickness=0
        )

        self.entrada_cuatro.place(
            x=122.0,
            y=119.0,
            width=27.0,
            height=41.0
        )

    def entrada_de_numero_cinco(self):
        self.canvas.create_rectangle(
            181.0,
            112.0,
            266.0,
            168.0,
            fill="#74296D",
            outline="")

        self.imagen_entrada_cinco = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            222.5,
            140.5,
            image=self.imagen_entrada_cinco
        )
        self.entrada_cinco = Entry(
            bd=0,
            bg="#B694FF",
            fg="#000716",
            highlightthickness=0
        )
        self.entrada_cinco.place(
            x=209.0,
            y=119.0,
            width=27.0,
            height=41.0
        )

    def entrada_de_numero_seis(self):
        self.canvas.create_rectangle(
            266.0,
            113.0,
            351.0,
            169.0,
            fill="#74296D",
            outline="")

        self.imagen_entrada_seis = PhotoImage(
            file=relative_to_assets("entry_6.png"))

        self.entry_bg_6 = self.canvas.create_image(
            307.5,
            141.5,
            image=self.imagen_entrada_seis
        )

        self.entrada_seis = Entry(
            bd=0,
            bg="#B694FF",
            fg="#000716",
            highlightthickness=0
        )

        self.entrada_seis.place(
            x=294.0,
            y=120.0,
            width=27.0,
            height=41.0
        )

    def entrada_de_numero_siete(self):
        self.canvas.create_rectangle(
            353.0,
            113.0,
            438.0,
            169.0,
            fill="#74296D",
            outline="")

        self.imagen_entrada_siete = PhotoImage(
            file=relative_to_assets("entry_7.png"))

        self.entry_bg_7 = self.canvas.create_image(
            394.5,
            141.5,
            image=self.imagen_entrada_siete
        )
        self.entrada_siete = Entry(
            bd=0,
            bg="#B694FF",
            fg="#000716",
            highlightthickness=0
        )

        self.entrada_siete.place(
            x=381.0,
            y=120.0,
            width=27.0,
            height=41.0
        )

    def entrada_de_numero_ocho(self):
        self.canvas.create_rectangle(
            614.0,
            115.0,
            699.0,
            171.0,
            fill="#74296D",
            outline="")

        self.imagen_entrada_ocho = PhotoImage(
            file=relative_to_assets("entry_8.png"))

        self.entry_bg_8 = self.canvas.create_image(
            655.5,
            143.5,
            image=self.imagen_entrada_ocho
        )
        self.entrada_ocho = Entry(
            bd=0,
            bg="#B694FF",
            fg="#000716",
            highlightthickness=0
        )

        self.entrada_ocho.place(
            x=642.0,
            y=122.0,
            width=27.0,
            height=41.0
        )

    def entrada_numero_nueve(self):
        self.canvas.create_rectangle(
            701.0,
            115.0,
            786.0,
            171.0,
            fill="#74296D",
            outline="")

        self.imagen_entrada_nueve = PhotoImage(
            file=relative_to_assets("entry_10.png"))

        self.entry_bg_9 = self.canvas.create_image(
            742.5,
            143.5,
            image=self.imagen_entrada_nueve
        )
        self.entrada_nueve = Entry(
            bd=0,
            bg="#B694FF",
            fg="#000716",
            highlightthickness=0
        )

        self.entrada_nueve.place(
            x=729.0,
            y=122.0,
            width=27.0,
            height=41.0
        )


    def boton_de_estadisticas(self):
        self.imagen_boton_estadisticas = PhotoImage(
            file=relative_to_assets("button_17.png"))

        self.boton_estadisticas = Button(
            image=self.imagen_boton_estadisticas,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_17 clicked"),
            relief="flat"
        )
        self.boton_estadisticas.place(
            x=639.0,
            y=1.0,
            width=71.0,
            height=58.0
        )


    def boton_de_guia(self):
        self.imagen_boton_guia = PhotoImage(
            file=relative_to_assets("button_18.png"))

        self.boton_guia = Button(
            image=self.imagen_boton_guia,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_18 clicked"),
            relief="flat"
        )
        self.boton_guia.place(
            x=747.0,
            y=0.0,
            width=60.0,
            height=58.0
        )

    def numero_de_vidas(self):
        self.imagen_numero_vidas = PhotoImage(
            file=relative_to_assets("entry_9.png"))

        self.entry_bg_numero_vidas = self.canvas.create_image(
            475.5,
            34.5,
            image=self.imagen_numero_vidas
        )

        self.numero_vidas = Entry(
            bd=0,
            bg="#F975EC",
            fg="#000716",
            highlightthickness=0
        )

        self.numero_vidas.place(
            x=451.0,
            y=13.0,
            width=49.0,
            height=41.0
        )







