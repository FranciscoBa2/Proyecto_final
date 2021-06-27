import matplotlib.pyplot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


##ver el maximo de puntaje, saber que libro es e invertir mas en publicidad
##ver el minimo de ventas sabes que libro es y reducir compras=oferta
##Los que mas ventas se realicen subir el precio
## si se da la coincidencia de que los mas vendidos tienen el mismo genero comprar mas de ese genero
##hacer un grafico del genero mas vendido


import sqlite3

## queremos ver cuantos libros hay en el foro con putnaje 10
conn = sqlite3.connect('Applibros.db')

frame = pd.read_sql('SELECT * FROM Foro', conn)
print(frame)
conn.close()
maximo_puntaje = frame["Puntaje(1-10)"].max()
print(maximo_puntaje)

libros_con_mejor_puntaje = frame["Nombre"].loc[(frame["Puntaje(1-10)"] == 10)]
print(libros_con_mejor_puntaje)


## queremos analizar cuantas ventas se registraron por dia para poder tomar una decision de negocio.

conn = sqlite3.connect('Applibros.db')

frame1 = pd.read_sql('SELECT * FROM Ventas', conn)
frame2 = frame1.drop(columns=['Id_libro', 'Dni_comprador', 'Precio'])
cantidad_de_ventas_por_fecha = frame2.groupby(frame2['fecha']).count()
cantidad_de_ventas_por_fecha.rename(columns={'id_transaccion':'cantidad_ventas'}, inplace=True)
print(cantidad_de_ventas_por_fecha)

cantidad_de_ventas_por_fecha.plot()
plt.show()
