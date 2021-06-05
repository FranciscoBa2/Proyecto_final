from App_libros import libros, cliente, libros_usados
import sqlite3
import random



def consulta_de_libros():
    print('Elija una de las siguientes opciones: ')
    print('1-Buscar libro')
    print('2- Busqueda de best-sellers NyT')
    consulta = input('Opcion a elegir: ')
    print('perfecto!')
    while True:
        if consulta == '1':
            print('¿Estas buscando algun libro en particular?')
            print('1 - si')
            print('2- no')
            respuesta = input('respuesta: ')
            if respuesta == '1':
                titulo_obra = input('Nombre del libro: ')
                conexion = sqlite3.connect('C:/Users/franc/PycharmProjects/Practicas fundamentos/Proyecto_final/App_libros/Applibros.db')
                cursor = conexion.cursor()
                sentencia = "SELECT * FROM Libros WHERE titulo_obra " + "LIKE '%" + titulo_obra + "%'"
                cursor.execute(sentencia)
                cliente = cursor.fetchone()
                if cliente is None:
                    conexion = sqlite3.connect('C:/Users/franc/PycharmProjects/Practicas fundamentos/Proyecto_final/App_libros/Applibros.db')
                    cursor = conexion.cursor()
                    sentencia = "SELECT * FROM Libros_usados WHERE titulo_obra " + "lIKE '%" + titulo_obra + "%'"
                    cursor.execute(sentencia)
                    cliente = cursor.fetchone()
                if cliente is None:
                    print('No encontramos el libro')
                else:
                    print(cliente)
                break



            if respuesta == '2':
                print('Elija una de las siguientes opciones.')
                print('1- Lista de todos los libros diponibles')
                print('2- Random')
                consulta = input('Opcion a elegir: ')
                x = []
                conexion = sqlite3.connect('C:/Users/franc/PycharmProjects/Practicas fundamentos/Proyecto_final/App_libros/Applibros.db')
                cursor = conexion.cursor()
                sentencia = "SELECT * FROM Libros"
                cursor.execute(sentencia)
                cliente = cursor.fetchall()
                for n in cliente:
                    x.append(n)
                sentencia2 = "SELECT * FROM Libros_usados"
                cursor.execute(sentencia2)
                cliente = cursor.fetchall()
                for n in cliente:
                    x.append(n)
                if consulta == '1':
                    print(x)
                if consulta == '2':
                    print(random.choice(x))

                break
            else:
                print('elija un numero entre las opciones.')

consulta_de_libros()

#



from datetime import datetime

import csv

def registro_clientes():
    print('Elija una de las siguientes opciones:')
    print('1- Alta cliente')
    print('2 - Baja cliente')
    print('3- ingreso de libros')
    move = input('tipo de movimiento: ')
    if move == '1':
        movimiento = 'Alta'
        fecha = datetime.now()
        nombre = input('nombre: ')
        apellido = input('apellido: ')
        contrasenia = input('contrasenia: ')
        id_number = input('id_number: ')

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
        contrasenia = input('contrasenia: ')
        id_number = input('id_number: ')

        with open('C:/Users/franc/PycharmProjects/Practicas fundamentos/Proyecto_final/App_libros/app.libros.csv', 'a',
                  newline='\n') as archivo:
            campos = ['movimiento', 'fecha', 'nombre', 'apellido', 'contrasenia']
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writerow({
                'movimiento': movimiento, 'fecha': fecha, 'nombre': '', 'apellido': '', 'contrasenia': contrasenia
            })
        cliente_a_eliminar = cliente(Nombre='', Apellido='', id_number=id_number, contrasenia=contrasenia)
        cliente_a_eliminar.eliminar_clientes()

    elif move == '3':
        print('que tipo de libro deeas insertar?')
        print('1- nuevo')
        print('2- usado')
        opcion = input('opcion a elegir: ')
        if opcion == '1':
            movimiento = 'Modificacion'
            fecha = datetime.now()
            id_number = input('id_number: ')
            titulo_obra = input('titulo_obra: ')
            genero = input('contrasenia: ')
            paginas = input('paginas: ')
            precio = input('precio: ')

            with open('C:/Users/franc/PycharmProjects/Practicas fundamentos/Proyecto_final/App_libros/app.libros.csv',
                      'a',
                      newline='\n') as archivo:
                campos = ['movimiento', 'fecha', 'nombre', 'apellido', 'contrasenia']
                writer = csv.DictWriter(archivo, fieldnames=campos)
                writer.writerow({
                    'movimiento': movimiento, 'fecha': fecha, 'nombre': '', 'apellido': '', 'contrasenia': ''
                })
            libro_a_agregar = libros(titulo_obra=titulo_obra, genero=genero, paginas=paginas, precio=precio, id_number=id_number)
            libro_a_agregar.agregar_libros()

        if opcion == '2':
            movimiento = 'Modificacion'
            fecha = datetime.now()
            id_number = input('id_number: ')
            titulo_obra = input('titulo_obra: ')
            genero = input('contrasenia: ')
            paginas = input('id_number: ')
            precio = input('precio: ')
            condicion = input('condicion: ')
            estado = input('estado: ')
            tiempo_de_uso = input('tiempo_de_uso: ')

            with open('C:/Users/franc/PycharmProjects/Practicas fundamentos/Proyecto_final/App_libros/app.libros.csv',
                      'a',
                      newline='\n') as archivo:
                campos = ['movimiento', 'fecha', 'nombre', 'apellido', 'contrasenia']
                writer = csv.DictWriter(archivo, fieldnames=campos)
                writer.writerow({
                    'movimiento': movimiento, 'fecha': fecha, 'nombre': '', 'apellido': '', 'contrasenia': ''
                })
            libro_u_agregar = libros_usados(titulo_obra=titulo_obra, genero=genero, paginas=paginas, precio=precio, id_number=id_number, condicion=condicion, estado=estado, tiempo_de_uso=tiempo_de_uso)
            libro_u_agregar.agregar_libros_usados()
#
#
# cliente1 = registro_clientes()
