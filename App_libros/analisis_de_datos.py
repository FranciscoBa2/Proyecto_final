import matplotlib.pyplot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


##ver el maximo de puntaje, saber que libro es e invertir mas en publicidad
##ver el minimo de ventas sabes que libro es y reducir compras=oferta
##Los que mas ventas se realicen subir el precio
## si se da la coincidencia de que los mas vendidos tienen el mismo genero comprar mas de ese genero
##hacer un grafico del genero mas vendido

data = {"nombre": ["Las venas abiertas de America Latina",
                            "Los siete maridos de Evelin Hugo",
                            "la bailarina de Auschwitz", "Rayuela",
                            "El principito",  "Cuando aprendas a amar",
                            "Civilizacion y barbarie", "El ninio de pijamas rayas"],
        "precio": [5000, 7000, 9000, 6000, 3000, 5000, 7800, 9000],
        "genero": ["Historia", "Romance", "Ficcion historica", "Ficcion historica",
                   "Fantasia", "Romance", "Historia", "Ficcion Historica"],
        "puntaje": [8, 10, 5, 10, 7, 9, 4, 9],
        "ventas_por_mes": [40, 80, 20, 55, 37, 20, 17, 70]}


import sqlite3

conn = sqlite3.connect('Applibros.db')

frame = pd.read_sql('SELECT * FROM Foro', conn)
print(frame)

### print(data)
frame = pd.DataFrame(data, index= [1, 2, 3, 4, 5, 6, 7, 8])
frame.index.name = "id"
frame.columns.name = 'item'
print(frame)
##print(frame.describe())
##print(frame.dtypes)


ventas = data["ventas_por_mes"]
genero = data["genero"]
ven_gen = pd.DataFrame({"ventas" : ventas,
"genero": genero})
frame2 = pd.DataFrame(data, columns=["nombre", "precio"])
#rint(frame2)

## print(ven_gen.plot.bar(rot=0))

maximo_puntaje = frame["puntaje"].max()
##print(maximo_puntaje)

p = frame["nombre"].loc[(frame["puntaje"] == 10)]
print(p)

minimo_de_ventas = frame["ventas_por_mes"].min()
print(minimo_de_ventas)
