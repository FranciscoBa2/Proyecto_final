import sqlite3
import random

ruta_base_datos = 'Applibros.db'

class Cliente:

    def __init__(self, Nombre, Apellido, contrasenia, dni):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.contrasenia = contrasenia
        self.id_number = dni
        self.act = 'activo'

    def agregar_clientes(self):
        self.id_number = str(self.id_number)
        conexion = sqlite3.connect(ruta_base_datos)
        cursor = conexion.cursor()
        sentencia = "SELECT * FROM Clientes WHERE id_number = '" + self.id_number + "'"
        cursor.execute(sentencia)
        cliente = cursor.fetchone()
        if cliente is None:
            conexion = sqlite3.connect(ruta_base_datos)
            cursor = conexion.cursor()
            m = (self.Nombre, self.Apellido, self.contrasenia, self.id_number, self.act)
            sentencia_sql = "INSERT INTO Clientes VALUES (?, ?, ?, ?, ?)"
            cursor.executemany(sentencia_sql, [m])
            conexion.commit()
            conexion.close()
            print('Este es su id_number: ', self.id_number)
        else:
            conexion = sqlite3.connect(ruta_base_datos)
            cursor = conexion.cursor()
            sentencia2 = "SELECT * FROM Clientes WHERE activo_inactivo = 'inactivo' AND Id_number = " + "'" + self.id_number + "'"
            cursor.execute(sentencia2)
            cliente = cursor.fetchone()
            if cliente is not None:
                sentencia3 = "UPDATE clientes SET 'activo_inactivo' = 'activo' WHERE id_number = '" + self.id_number + "'"
                cursor.execute(sentencia3)
                conexion.commit()
                conexion.close()

    def eliminar_clientes(self):
        conexion = sqlite3.connect(ruta_base_datos)
        cursor = conexion.cursor()
        sentencia1 = "UPDATE clientes SET 'activo_inactivo' = 'inactivo' WHERE id_number = '" + self.id_number + "'"
        sentencia2 = "UPDATE Libros SET 'activo_inactivo(cliente)' = 'inactivo' WHERE id_number_clientes = '" + self.id_number + "'"
        sentencia3 = "UPDATE Libros_usados SET 'activo_inactivo(cliente)' = 'inactivo' WHERE id_number_clientes = '" + self.id_number + "'"
        cursor.execute(sentencia1)
        cursor.execute(sentencia2)
        cursor.execute(sentencia3)
        conexion.commit()
        conexion.close()

    def consulta_libro(self, titulo_obra):
        self.titulo_obra = titulo_obra
        conexion = sqlite3.connect(ruta_base_datos)
        cursor = conexion.cursor()
        sentencia = "SELECT * FROM Libros WHERE titulo_obra " + "LIKE '%" + self.titulo_obra + "%'"
        sentencia2 = "SELECT * FROM Libros_usados WHERE titulo_obra " + "lIKE '%" + self.titulo_obra + "%'"
        cursor.execute(sentencia)
        cursor.execute(sentencia2)
        self.lista_libros = []
        libro = cursor.fetchall()
        libro2 = cursor.fetchall()
        conexion.close()
        self.lista_libros.append(libro)
        self.lista_libros.append(libro2)
        return self.lista_libros

    def consulta_de_libros(self):
        self.lista = []
        conexion = sqlite3.connect(ruta_base_datos)
        cursor = conexion.cursor()
        sentencia = "SELECT * FROM Libros"
        sentencia2 = "SELECT * FROM Libros_usados"
        cursor.execute(sentencia)
        cliente = cursor.fetchall()
        cursor.execute(sentencia2)
        cliente2 = cursor.fetchall()
        self.lista.append(cliente)
        self.lista.append(cliente2)
        conexion.close()
        return self.lista


class Libros:
    
    def __init__(self, titulo_obra, genero, paginas, precio, id_number):
        self.titulo_obra = titulo_obra
        self.genero = genero
        self.paginas = paginas
        self.precio = precio
        self.id_number = id_number
        self.act = 'activo'
        self.id_libro = int(random.uniform(1, 100000000))


    def agregar_libros(self):
        conexion = sqlite3.connect(ruta_base_datos)
        cursor = conexion.cursor()
        sentencia2 = "SELECT * FROM Libros WHERE Titulo_obra = '" + self.titulo_obra + "' AND id_number_clientes = '" + self.id_number + "'"
        cursor.execute(sentencia2)
        Libro = cursor.fetchone()
        if Libro is None:
            conexion = sqlite3.connect(ruta_base_datos)
            cursor = conexion.cursor()
            x = (self.titulo_obra, self.genero, self.paginas, self.precio, self.id_libro, self.id_number, self.act)
            sentencia_sql = "INSERT INTO Libros VALUES (?, ?, ?, ?, ?, ?, ?)"
            cursor.executemany(sentencia_sql, [x])
            conexion.commit()
            conexion.close()




    def eliminar_libros(self, id_number):
        self.id_number = id_number
        conexion = sqlite3.connect(ruta_base_datos)
        cursor = conexion.cursor()
        sentencia = "UPDATE Libros SET activo/inactivo = 'inactivo' WHERE id_number_libros = " + "'" + self.id_number + "' AND Titulo_obra = " + "'" + self.titulo_obra + "'"
        cursor.execute(sentencia)
        conexion.commit()
        conexion.close()





class Libros_usados(Libros):
    
    def __init__(self, titulo_obra, genero, paginas, precio, id_number, condicion, estado, tiempo_de_uso):
        super().__init__(titulo_obra, genero, paginas, precio, id_number)
        self.condicion = condicion
        self.estado = estado
        self.tiempo_de_uso = tiempo_de_uso
        self.act = 'activo'
        self.id_libro = int(random.uniform(1, 100000000))

    def agregar_libros_usados(self):
        conexion = sqlite3.connect(ruta_base_datos)
        cursor = conexion.cursor()
        sentencia2 = "SELECT * FROM Libros_usados WHERE id_number_clientes = " + "'" + self.id_number + "' AND Titulo_obra = " + "'" + self.titulo_obra + "'"
        cursor.execute(sentencia2)
        Libro = cursor.fetchone()
        if Libro is None:
            conexion = sqlite3.connect(ruta_base_datos)
            cursor = conexion.cursor()
            n = (self.titulo_obra, self.genero, self.paginas, self.precio, self.id_number, self.condicion, self.estado, self.tiempo_de_uso, self.id_libro, self.act)
            sentencia_sql = "INSERT INTO Libros_usados VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.executemany(sentencia_sql, [n])
            conexion.commit()
            conexion.close()

    def eliminar_libros(self, id_number):
        self.id_number = id_number
        conexion = sqlite3.connect(ruta_base_datos)
        cursor = conexion.cursor()
        sentencia = "UPDATE Libros_usados SET activo/inactivo = 'inactivo' WHERE id_number = " + "'" + self.id_number + "' AND Titulo_obra = " + "'" + self.titulo_obra + "'"
        cursor.execute(sentencia)
        conexion.commit()
        conexion.close()
