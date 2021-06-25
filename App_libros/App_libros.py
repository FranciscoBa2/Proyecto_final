import sqlite3
from datetime import datetime
import random
import csv
from Script_automatizado import ejecutar_mail

ruta_base_datos = 'Applibros.db'

ruta_csv = 'app.libros.csv'


def registrar_csv(movimiento, nombre, apellido, contrasenia, dni, alquiler):
    with open(ruta_csv, 'a', newline='\n') as archivo:
        campos = ['movimiento', 'fecha', 'nombre', 'apellido', 'contrasenia', 'id', 'alquiler']
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writerow({
            'movimiento': movimiento, 'fecha': datetime.now(), 'nombre': nombre, 'apellido': apellido,
            'contrasenia': contrasenia, 'id': dni, 'alquiler': alquiler
        })

def conexion_ejecucion_sentencia(sentencia, tipo_ejecucion='', tupla=None):
    conexion = sqlite3.connect(ruta_base_datos)
    cursor = conexion.cursor()
    if tipo_ejecucion == 'simple':
        cursor.execute(sentencia)
    else:
        cursor.executemany(sentencia, [tupla])
    material = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return material


# def eliminar_registros_para_prueba():
#     conexion_ejecucion_sentencia(sentencia="DELETE from Clientes WHERE (lo que se necesite)",
#     tipo_ejecucion='simple', tupla=None)
#     conexion_ejecucion_sentencia(sentencia="DELETE from Libros WHERE (lo que se necesite)",
#     tipo_ejecucion='simple', tupla=None)
#     conexion_ejecucion_sentencia(sentencia="DELETE from Libros_usados WHERE (lo que se necesite)",
#     tipo_ejecucion='simple', tupla=None)


class Cliente:

    def __init__(self, Nombre, Apellido, contrasenia, numero, mail, dni):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.contrasenia = contrasenia
        self.numero = numero
        self.mail = mail
        self.id_number = dni
        self.act = 'activo'

    def agregar_clientes(self):

        cliente = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Clientes WHERE id_number = '" +
                                                         self.id_number + "'", tipo_ejecucion='simple')
        try:
            if len(cliente) == 0:
                conexion_ejecucion_sentencia(sentencia="INSERT INTO Clientes VALUES (?, ?, ?, ?, ?, ?, ?)",
                                            tupla=(self.Nombre, self.Apellido, self.contrasenia, self.id_number,
                                                    self.numero, self.mail, self.act))
                print('Registro exitoso!', 'Bienvenido a nuestra comunidad ', self.Nombre, self.Apellido)
            else:
                cliente = conexion_ejecucion_sentencia(sentencia="UPDATE Clientes SET 'activo_inactivo' = 'activo'"
                                                       " WHERE id_number = '" + self.id_number + "'",
                                                       tipo_ejecucion='simple')
                if len(cliente) > 0:
                    print('Registro exitoso!', 'Bienvenido a nuestra comunidad ', self.Nombre, self.Apellido)
                else:
                    print('Ya se encuentra activo como cliente')
        except Exception as e:
            print('Compruebe que los datos ingresados sean correctos', e)

    def desactivar_clientes(self):
        conexion_ejecucion_sentencia(sentencia="UPDATE clientes SET 'activo_inactivo' = 'inactivo' WHERE id_number = '"
                                               + self.id_number + "'", tipo_ejecucion='simple')
        conexion_ejecucion_sentencia(sentencia="UPDATE Libros SET activo_inactivo_cliente = 'inactivo' WHERE "
                                               "id_number_clientes = '" + self.id_number + "'", tipo_ejecucion='simple')
        conexion_ejecucion_sentencia(sentencia="UPDATE Libros_usados SET activo_inactivo_cliente = 'inactivo' WHERE "
                                               "id_number_clientes = '" + self.id_number + "'", tipo_ejecucion='simple')

    def consulta_libro(self, titulo_obra):
        self.titulo_obra = titulo_obra
        self.lista_libros = []
        resultado = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Libros WHERE Titulo_obra " + "LIKE '%" +
                                                   self.titulo_obra + "%' AND activo_inactivo_cliente = 'activo'",
                                                 tipo_ejecucion='simple')
        resultado2 = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Libros_usados WHERE Titulo_obra " + "LIKE '%"
                                                            + self.titulo_obra + "%'", tipo_ejecucion='simple')
        if len(resultado) > 0:
            self.lista_libros.append(resultado)
        else:
            self.lista_libros.append([])
        if len(resultado2) > 0:
            self.lista_libros.append(resultado2)
        else:
            self.lista_libros.append([])
        return self.lista_libros

    def consulta_de_libros(self):
        self.lista = []
        resultado = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Libros WHERE activo_inactivo_cliente = "
                                                           "'activo'", tipo_ejecucion='simple')
        resultado2 = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Libros_usados WHERE activo_inactivo_cliente"
                                                            " = 'activo'", tipo_ejecucion='simple')
        self.lista.append(resultado)
        self.lista.append(resultado2)
        return self.lista

    def comprar_libro(self, id_libro, precio, dni):

        #repasar lo del mail
        self.id_libro = str(id_libro)
        self.dni = dni
        self.precio = precio
        self.id_transaccion = None
        conexion_ejecucion_sentencia(sentencia="INSERT INTO Ventas VALUES (?, ?, ?, ?)",
                                     tupla=(self.id_transaccion, self.id_libro, self.precio, self.dni))
        conexion_ejecucion_sentencia(sentencia="UPDATE Libros SET activo_inactivo_cliente = 'inactivo' "
                                               "WHERE Id_number_libros = '" + self.id_libro + "'",
                                     tipo_ejecucion='simple')
        conexion_ejecucion_sentencia(sentencia="UPDATE Libros_usados SET activo_inactivo_cliente = 'inactivo' "
                                               "WHERE Id_number_libros = '" + self.id_libro + "'",
                                     tipo_ejecucion='simple')
        resultado = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Libros WHERE Id_number_libros = '" +
                                                           self.id_libro + "'", tipo_ejecucion='simple')
        resultado2 = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Libros_usados WHERE Id_number_libros = '" +
                                                            self.id_libro + "'",
                                                  tipo_ejecucion='simple')
        id_cliente = None
        if len(resultado) != 0:
            id_cliente = resultado[0]
            id_cliente = id_cliente[5]
        if len(resultado2) != 0:
            id_cliente = resultado2[0]
            id_cliente = id_cliente[4]
        client = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Clientes WHERE Id_number = '" +
                                                        str(id_cliente) + "'", tipo_ejecucion='simple')
        mail = client[0]
        email = mail[5]
        mensaje = "Buenos dias, nos comunicamos para informarte que vendiste tu libro {}".format(self.id_libro)
        ejecutar_mail(mensaje=mensaje, receptor=email)

    def crear_recomendacion(self, titulo_obra, puntaje, recomendacion, nombre, apellido):
        self.titulo_obra = titulo_obra
        self.puntaje = puntaje
        self.recomendacion = recomendacion
        self.nombre = nombre
        self.apellido = apellido
        self.id = None
        conexion_ejecucion_sentencia(sentencia="INSERT INTO Foro VALUES (?, ?, ?, ?, ?, ?)",
                                     tupla=(self.id, self.titulo_obra, self.puntaje, self.recomendacion, self.nombre,
                                            self.apellido))

    def solicitud_prestamo(self, titulo_obra, id_libro, nombre, apellido, telefono, email):
        self.id_solicitud = None
        self.fecha = datetime.now()
        self.id_libro = id_libro
        self.titulo_obra = titulo_obra
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        conexion_ejecucion_sentencia(sentencia="INSERT INTO Solicitudes_prestamos VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                                     tupla=(self.id_solicitud, self.fecha, self.titulo_obra, self.id_libro, self.nombre,
                                            self.apellido, self.telefono, self.email))

    def modificar_datos_cliente(self, columna, dato):
        conexion_ejecucion_sentencia(sentencia="UPDATE Clientes SET " + columna + "=" + "'" + dato + "'"
                                               "WHERE Id_number = '" + self.id_number + "'",
                                     tipo_ejecucion='simple')

class Libros:
    
    def __init__(self, titulo_obra, genero, paginas, precio, id_number, alquiler):
        self.titulo_obra = titulo_obra
        self.genero = genero
        self.paginas = paginas
        self.precio = precio
        self.id_number = id_number
        self.act = 'activo'
        self.alquiler = alquiler
        self.id_libro = None

    def agregar_libros(self):
        # Al tener dos tables teniamos que verificar que el id_libro sea realmente unico y que no se repita en niguna
        # de las dos, es por eso que se verifica entes de crear el cliente. Se utiliza una funcion y no el
        # autoincremental del sqlite ya que este ultimo toma en cuenta solo la tabla a la que se le indica.

        # hay que verificar de que exista el cliente que quiere insertar los libros

        cliente = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Clientes WHERE Id_number = '" +
                                                         self.id_number + "'",
                                               tipo_ejecucion='simple')
        if len(cliente) != 0:

            Libro = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Libros WHERE Titulo_obra = '" +
                                                           self.titulo_obra + "' AND Id_number_clientes = '" +
                                                           self.id_number + "'", tipo_ejecucion='simple')
            Libro2 = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Libros_usados WHERE Titulo_obra = '" +
                                                           self.titulo_obra + "' AND Id_number_clientes = '" +
                                                           self.id_number + "'", tipo_ejecucion='simple')
            if len(Libro) == 0 and len(Libro2) == 0:
                conexion_ejecucion_sentencia(sentencia="INSERT INTO Libros VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                                             tupla=(self.titulo_obra, self.genero, self.paginas, self.precio,
                                                    self.id_libro, self.id_number, self.act, self.alquiler))
        return cliente

    def desactivar_libros(self, id_number_libro):
        self.id_number = id_number_libro
        conexion_ejecucion_sentencia(sentencia="UPDATE Libros_usados SET activo_inactivo_cliente = 'inactivo' "
                                               "WHERE Id_number_libros = '" + self.id_number + "'",
                                     tipo_ejecucion='simple')


class Libros_usados(Libros):
    
    def __init__(self, titulo_obra, genero, paginas, precio, id_number, condicion, tiempo_de_uso, alquiler):
        super().__init__(titulo_obra, genero, paginas, precio, id_number, alquiler)
        self.condicion = condicion
        self.tiempo_de_uso = tiempo_de_uso
        self.act = 'activo'
        self.id_libro = None

    def agregar_libros_usados(self):

        # Al tener dos tables teniamos que verificar que el id_libro sea realmente unico y que no se repita en niguna
        # de las dos, es por eso que se verifica entes de crear el cliente. Se utiliza una funcion y no el
        # autoincremental del sqlite ya que este ultimo toma en cuenta solo la tabla a la que se le indica.

        cliente = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Clientes WHERE Id_number = '" +
                                                         self.id_number + "'",
                                               tipo_ejecucion='simple')
        if len(cliente) != 0:
            Libro = conexion_ejecucion_sentencia(
                sentencia="SELECT * FROM Libros_usados WHERE Id_number_clientes = " + "'"
                          + self.id_number + "' AND Titulo_obra = " + "'"
                          + self.titulo_obra + "'", tipo_ejecucion='simple')
            Libro2 = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Libros WHERE Titulo_obra = '" +
                                                            self.titulo_obra + "' AND Id_number_clientes = '" +
                                                            self.id_number + "'", tipo_ejecucion='simple')
            if len(Libro) == 0 and len(Libro2) == 0:
                conexion_ejecucion_sentencia(
                    sentencia="INSERT INTO Libros_usados VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    tupla=(self.titulo_obra, self.genero, self.paginas, self.precio,
                           self.id_number, self.condicion, self.tiempo_de_uso, self.id_libro,
                           self.act, self.alquiler))
        return cliente

    def desactivar_libros(self, id_number_libro):
        self.id_number = id_number_libro
        conexion_ejecucion_sentencia(sentencia="UPDATE Libros_usados SET activo_inactivo_cliente = 'inactivo' "
                                               "WHERE Id_number_libros = '" + self.id_number + "'",
                                     tipo_ejecucion='simple')


class Arreglador:

    def __init__(self, listas):
        self.listas = listas

    def formato_dic_libros(self, cantidad_de_listas):
        n = 0
        lis = []
        if cantidad_de_listas == 2:
            for lista in self.listas:
                for libro in lista:
                    n = n + 1
                    try:
                        columnas = ['Titulo de la obra', 'Genero', 'Paginas', 'Precio ',
                                    'Id number', 'Condicion', 'Tiempo de uso', 'Id libro',
                                    'activo_inactivo:', 'Alquiler']
                        if len(libro) > 8:
                            lib = (dict(zip(columnas, libro)))
                            lis.append(lib)
                        else:
                            columnas2 = ['Titulo de la obra', 'Genero', 'Paginas', 'Precio ',
                                        'Id number libro', 'Id number cliente', 'activo_inactivo', 'Alquiler']
                            lib = (dict(zip(columnas2, libro)))
                            lis.append(lib)
                    except:
                        continue
        if cantidad_de_listas == 1:
            for datos in self.listas:
                n = n + 1
                try:
                    columnas = ['Titulo de la obra', 'Genero:', 'Paginas:', 'Precio: ',
                                'Id number:', 'Condicion:', 'Tiempo de uso:', 'Id libro:',
                                'activo_inactivo:', 'Alquiler']
                    if len(datos) > 8:
                        lib = (dict(zip(columnas, datos)))
                        lis.append(lib)
                    else:
                        columnas2 = ['Titulo de la obra:', 'Genero:', 'Paginas:', 'Precio: ',
                                     'Id number libro:', 'Id number cliente:', 'activo_inactivo:', 'Alquiler']
                        l = (dict(zip(columnas2, datos)))
                        lis.append(l)
                except:
                    continue
        if cantidad_de_listas == 0:
            libro = random.choice(self.listas[0])
            try:
                columnas = ['Titulo de la obra', 'Genero:', 'Paginas:', 'Precio: ',
                            'Id number:', 'Condicion:', 'Tiempo de uso:', 'Id libro:',
                            'activo_inactivo:', 'Alquiler']
                if len(libro) > 7:
                    libro = (dict(zip(columnas, libro)))
                    lis.append(libro)
            except:
                columnas2 = ['Titulo de la obra:', 'Genero:', 'Paginas:', 'Precio: ',
                             'Id number libro:', 'Id number cliente:', 'activo_inactivo:', 'Alquiler']
                libro = (dict(zip(columnas2, libro)))
                lis.append(libro)
        return lis

    def formato_dic_cliente(self):
        n = 0
        lis = []
        columnas = ['Nombre', 'Apellido', 'contrasenia', 'dni', 'numero', 'mail']
        for datos in self.listas:
            n = n + 1
            try:
                libro = (dict(zip(columnas, datos)))
                lis.append(libro)
            except:
                continue
        return lis


