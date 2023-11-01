import matplotlib.pyplot as plt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


# clase encargada de la informacion de estadisticas y correos
class Informacion:
    def __init__(self, juego):
        self.juego = juego

    def crear_grafico(self):
        victorias = self.juego.estadisticas['victorias']
        derrotas = self.juego.estadisticas['derrotas']

        plt.scatter(['Victorias', 'Derrotas'], [victorias, derrotas])
        plt.ylabel('Cantidad')
        plt.title('Victorias vs Derrotas')

        plt.savefig('grafico.png')

    def enviar_por_correo(self, direccion_correo):
        msg = MIMEMultipart()
        msg['From'] = 'tu_correo@gmail.com'
        msg['To'] = direccion_correo
        msg['Subject'] = 'Gráfico de Victorias vs Derrotas'

        with open('grafico.png', 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="grafico.png"')
            msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('tu_correo@gmail.com', 'tu_contraseña')
        server.send_message(msg)
        server.quit()
