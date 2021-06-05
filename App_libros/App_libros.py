import sqlite3
class cliente:

## como defiir una primary key
## foreign key( como se relacionan dos tablas)
    def __init__(self, Nombre, Apellido, id_number, contrasenia):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.contrasenia = contrasenia
        self.id_number = id_number

    def agregar_clientes(self):

        conexion = sqlite3.connect('C:/Users/franc/PycharmProjects/Practicas fundamentos/Proyecto_final/App_libros/Applibros.db')
        cursor = conexion.cursor()
        sentencia = "SELECT * FROM clientes WHERE contrasenia = '" + self.contrasenia + "' and  id_number = '" + self.id_number + "'"
        cursor.execute(sentencia)
        cliente = cursor.fetchone()
        if cliente is None:
            conexion = sqlite3.connect('C:/Users/franc/PycharmProjects/Practicas fundamentos/Proyecto_final/App_libros/Applibros.db')
            cursor = conexion.cursor()
            m = (self.Nombre, self.Apellido, self.id_number, self.contrasenia)
            sentencia_sql = "INSERT INTO clientes VALUES (?, ?, ?, ?)"
            cursor.executemany(sentencia_sql, [m])
            conexion.commit()
            conexion.close()

    def eliminar_clientes(self):
        conexion = sqlite3.connect('C:/Users/franc/PycharmProjects/Practicas fundamentos/Proyecto_final/App_libros/Applibros.db')
        cursor = conexion.cursor()
        sentencia1 = "DELETE FROM clientes WHERE contrasenia = '" + self.contrasenia + "' and id_number = '" + self.id_number + "'"
        cursor.execute(sentencia1)
        conexion.commit()
        conexion.close()




## a traves de base de datos que se actualiza nosotros le damos informacion importante a los cientes. ejemplo vacunas.
class libros:
    lista = []
    def __init__(self, titulo_obra, genero, paginas, precio, id_number):
        self.titulo_obra = titulo_obra
        self.genero = genero
        self.paginas = paginas
        self.precio = precio
        self.id_number = id_number
    def agregar_libros(self):
        conexion = sqlite3.connect('C:/Users/franc/PycharmProjects/Practicas fundamentos/Proyecto_final/App_libros/Applibros.db')
        cursor = conexion.cursor()
        sentencia1 = "SELECT * FROM clientes WHERE id_number = '" + self.id_number + "'"
        sentencia2 = "SELECT * FROM Libros WHERE titulo_obra = '" + self.titulo_obra + "' and id_number = '" + self.id_number + "'"
        cursor.execute(sentencia1)
        id = cursor.fetchone()
        cursor.execute(sentencia2)
        Libro = cursor.fetchone()
        if Libro is None and id is not None:
            conexion = sqlite3.connect('C:/Users/franc/PycharmProjects/Practicas fundamentos/Proyecto_final/App_libros/Applibros.db')
            cursor = conexion.cursor()
            x = (self.titulo_obra, self.genero, self.paginas, self.precio, self.id_number)
            sentencia_sql = "INSERT INTO Libros VALUES (?, ?, ?, ?, ?)"
            cursor.executemany(sentencia_sql, [x])
            conexion.commit()
            conexion.close()




    def eliminar_libros(self):
        conexion = sqlite3.connect('C:/Users/franc/PycharmProjects/Practicas fundamentos/Proyecto_final/App_libros/Applibros.db')
        cursor = conexion.cursor()
        sentencia = "DELETE FROM Libros WHERE id_number = " + "'" + self.id_number + "' and titulo_obra = " + "'" + self.titulo_obra + "'"
        cursor.execute(sentencia)
        conexion.commit()
        conexion.close()





class libros_usados(libros):
    lista = []
    def __init__(self, titulo_obra, genero, paginas, precio, id_number, condicion, estado, tiempo_de_uso):
        super().__init__(titulo_obra, genero, paginas, precio, id_number)
        self.condicion = condicion
        self.estado = estado
        self.tiempo_de_uso = tiempo_de_uso

    def agregar_libros_usados(self):
        conexion = sqlite3.connect('C:/Users/franc/PycharmProjects/Practicas fundamentos/Proyecto_final/App_libros/Applibros.db')
        cursor = conexion.cursor()
        sentencia1 = "SELECT * FROM clientes WHERE id_number = '" + self.id_number + "'"
        sentencia2 = "SELECT * FROM Libros_usados WHERE id_number = " + "'" + self.id_number + "' and titulo_obra = " + "'" + self.titulo_obra + "'"
        cursor.execute(sentencia1)
        id = cursor.fetchone()
        cursor.execute(sentencia2)
        Libro = cursor.fetchone()
        if Libro is None and id is not None:
            conexion = sqlite3.connect('C:/Users/franc/PycharmProjects/Practicas fundamentos/Proyecto_final/App_libros/Applibros.db')
            cursor = conexion.cursor()
            n = (self.titulo_obra, self.genero, self.paginas, self.precio, self.id_number, self.condicion, self.estado, self.tiempo_de_uso)
            sentencia_sql = "INSERT INTO libros_usados VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.executemany(sentencia_sql, [n])
            conexion.commit()
            conexion.close()

    def eliminar_libros(self):

        conexion = sqlite3.connect('C:/Users/franc/PycharmProjects/Practicas fundamentos/Proyecto_final/App_libros/Applibros.db')
        cursor = conexion.cursor()
        sentencia = "DELETE FROM Libros_usados WHERE id_number = " + "'" + self.id_number + "' and titulo_obra = " + "'" + self.titulo_obra + "'"
        cursor.execute(sentencia)
        conexion.commit()
        conexion.close()
