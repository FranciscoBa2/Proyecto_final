import sys

# la idea seria que a partir del csv donde se registran todos los movimientos te haga un resumen diario de la cantidad de inserciones, bajas y ventas.


## para resolver el tema de los prestamos que haya una tabla mas para las solicitudes de alquiler/prestamo. Que te envie un mail automatico que tambien le brinde los datos al vendedor para ponerse en contacto.

#
# import datetime
#
# now = datetime.datetime.now()
# conexion =
#
# from io import open
#
# archivo = open('app.libros.csv')
#
# lineas = archivo.readlines()
#
# x = []
# for n in lineas:
#     n = n[:-1]
#     linea = n.split(',')
#     # l = (linea[0], linea[1], linea[2], linea[3], linea[4], linea[5])
#     x.append(linea)
#

# archivo.close()
# del (archivo)
# print(x[1:])


import smtplib
from email.message import EmailMessage


def enviarmail(mensaje, receptor):
    usuario = 'f.caprarulo@wellspring.edu.ar'
    contrasenia = 'capra123'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(usuario, contrasenia)

    em = EmailMessage()
    em.set_content(mensaje)
    em['To'] = receptor
    em['From'] = usuario
    em['Subject'] = 'Venta de libro'

    server.send_message(em)
    server.quit()


    if __name__ == '__main__':
        enviarmail(mensaje, receptor)
