import pandas as pd
import matplotlib.pyplot as plt


##ver el maximo de puntaje, saber que libro es e invertir mas en publicidad
##hacer un grafico de las cantidades vendidas por dia
## ver maximos y minimos de ventas en un dia en un periodo determinado


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


posicion_maximo = cantidad_de_ventas_por_fecha["cantidad_ventas"].argmax()
fecha_maximo = cantidad_de_ventas_por_fecha.index[posicion_maximo]
print('Fecha con valor maximo: ', fecha_maximo)
posicion_minimo = cantidad_de_ventas_por_fecha["cantidad_ventas"].argmin()
fecha_minimo = cantidad_de_ventas_por_fecha.index[posicion_minimo]
print('Fecha con valor minimo: ', fecha_minimo)


cantidad_de_ventas_por_fecha.plot()
plt.show()
