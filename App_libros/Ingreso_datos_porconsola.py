from App_libros import libros, cliente, libros_usados
import sqlite3
def consulta_de_libros():
    print('Elija una de las siguientes opciones: ')
    print('1-Buscar libro')
    print('2- Busqueda de best-sellers NyT')
    consulta = input('Opcion a elegir: ')
    print('perfecto!')
    while True:
        if consulta == '1':
            print('Estas buscando algun libro en particular?')
            print('1 - si')
            print('2- no')
            respuesta = input('respuesta: ')
            if respuesta == '1':
                titulo_obra = input('Nombre del libro: ')
                conexion = sqlite3.connect('C:/Users/franc/PycharmProjects/Practicas fundamentos/App_libros/Applibros.db')
                cursor = conexion.cursor()
                sentencia = "SELECT * FROM Libros WHERE titulo_obra = " + "'" + titulo_obra + "'"
                cursor.execute(sentencia)
                cliente = cursor.fetchone()
                print(cliente)
                if cliente is None:
                    conexion = sqlite3.connect(
                        'C:/Users/franc/PycharmProjects/Practicas fundamentos/App_libros/Applibros.db')
                    cursor = conexion.cursor()
                    sentencia = "SELECT * FROM Libros WHERE id_number = " + "'" + titulo_obra + "'"
                    cursor.execute(sentencia)
                    cliente = cursor.fetchone()
                    print(cliente)
                    if cliente is None:
                        conexion = sqlite3.connect(
                            'C:/Users/franc/PycharmProjects/Practicas fundamentos/App_libros/Applibros.db')
                        cursor = conexion.cursor()
                        sentencia = "SELECT * FROM titulo_obra WHERE id_number = " + "'" + titulo_obra + "'"
                        cursor.execute(sentencia)
                        cliente = cursor.fetchone()
                        print(cliente)
                        if cliente is None:
                            print('No encontramos el libro')
                break
            if respuesta == '2':
                conexion = sqlite3.connect('C:/Users/franc/PycharmProjects/Practicas fundamentos/App_libros/Applibros.db')
                cursor = conexion.cursor()
                sentencia = "SELECT * FROM Libros"
                cursor.execute(sentencia)
                cliente = cursor.fetchall()
                for n in cliente:
                    print(n)
                sentencia2 = "SELECT * FROM Libros_usados"
                cursor.execute(sentencia2)
                cliente = cursor.fetchall()
                for n in cliente:
                    print(n)
                break
            else:
                print('elija un numero entre las opciones.')

# consulta_de_libros()

#



from datetime import datetime

import csv

def registro_clientes():
    print('Elija una de las siguientes opciones:')
    print('1- Alta cliente')
    print('2 - Baja cliente')
    print('3- Modificacion de datos cliente')
    move = input('tipo de movimiento: ')
    if move == '1':
        movimiento = 'Alta'
        fecha = datetime.now()
        nombre = input('nombre: ')
        apellido = input('apellido: ')
        id_number = input('id_number: ')
        contrasenia = input('contrasenia: ')

        with open('C:/Users/franc/PycharmProjects/Practicas fundamentos/App_libros/app.libros.csv', 'a', newline='\n') as archivo:
            campos = ['movimiento', 'fecha', 'nombre', 'apellido', 'id_number', 'contrasenia', 'libros']
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writerow({
                'movimiento': movimiento, 'fecha': fecha, 'nombre': nombre, 'apellido': apellido, 'id_number': id_number, 'contrasenia': contrasenia
            })

        cliente_nuevo = cliente(Nombre=nombre, Apellido=apellido, id_number=id_number, contrasenia=contrasenia)
        cliente_nuevo.agregar_clientes()

    elif move == '2':
        movimiento = 'Baja'
        fecha = datetime.now()
        id_number = input('id_number: ')
        contrasenia = input('contrasenia: ')

        with open('C:/Users/franc/PycharmProjects/Practicas fundamentos/App_libros/app.libros.csv', 'a',
                  newline='\n') as archivo:
            campos = ['movimiento', 'fecha', 'nombre', 'apellido', 'id_number', 'contrasenia', 'libros']
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writerow({
                'movimiento': movimiento, 'fecha': fecha, 'nombre': '', 'apellido': '',
                'id_number': id_number, 'contrasenia': contrasenia
            })
        cliente_nuevo = cliente(Nombre='', Apellido='', id_number=id_number, contrasenia=contrasenia)
        cliente_nuevo.agregar_clientes()

#
#
#
# cliente1 = registro_clientes()
