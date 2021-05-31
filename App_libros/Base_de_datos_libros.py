# from Ingreso_datos_porconsola import libros, cliente, libros_usados
import sqlite3
from App_libros import libros_usados

# conexion = sqlite3.connect('C:/Users/franc/PycharmProjects/Practicas fundamentos/App_libros/Applibros.db')
# cursor = conexion.cursor()
# x = []
# for n in libros.lista:
#     n = n.tuplatype()
#     x.append(n)
# sentencia_sql = "INSERT INTO Libros VALUES (?, ?, ?, ?, ?)"
# cursor.executemany(sentencia_sql, x)
# conexion.commit()
# conexion.close()
#

## conexion_usados


conexion = sqlite3.connect('C:/Users/franc/PycharmProjects/Practicas fundamentos/App_libros/Applibros.db')
cursor = conexion.cursor()
x = []
for n in libros_usados.lista:
    n = n.tuplatype()
    x.append(n)
sentencia_sql = "INSERT INTO Libros_usados VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
cursor.executemany(sentencia_sql, x)
conexion.commit()
conexion.close()

