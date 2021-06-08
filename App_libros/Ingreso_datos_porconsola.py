from App_libros import Libros
from App_libros import Cliente
from App_libros import Libros_usados
from App_libros import ruta_base_datos
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
                conexion = sqlite3.connect(ruta_base_datos)
                cursor = conexion.cursor()
                sentencia = "SELECT * FROM Libros WHERE titulo_obra " + "LIKE '%" + titulo_obra + "%'"
                cursor.execute(sentencia)
                cliente = cursor.fetchone()
                conexion.close()
                if cliente is None:
                    conexion = sqlite3.connect(ruta_base_datos)
                    cursor = conexion.cursor()
                    sentencia = "SELECT * FROM Libros_usados WHERE titulo_obra " + "lIKE '%" + titulo_obra + "%'"
                    cursor.execute(sentencia)
                    cliente = cursor.fetchone()
                    conexion.close()
                try:
                    print('Titulo de la obra:', cliente[0], '\nGenero:', cliente[1],
                            '\nPaginas:', cliente[2], '\nprecio:', cliente[3], '\nid_number:', cliente[4],
                            '\ncondicion:', cliente[5], '\nestado: ', cliente[6], '\ntiempo de uso: ', cliente[7])
                    break
                except IndexError:
                    print('Titulo de la obra:', cliente[0], '\nGenero:', cliente[1],
                        '\nPaginas:', cliente[2], '\nprecio:', cliente[3], '\nid_number:', cliente[4])
                    break
                except:
                    print('No encontramos el libro')


            if respuesta == '2':
                print('Elija una de las siguientes opciones.')
                print('1- Lista de todos los libros diponibles')
                print('2- Random')
                consulta = input('Opcion a elegir: ')
                x = []
                conexion = sqlite3.connect(ruta_base_datos)
                cursor = conexion.cursor()
                sentencia = "SELECT * FROM Libros"
                cursor.execute(sentencia)
                cliente = cursor.fetchall()
                for n in cliente:
                    x.append(n)
                sentencia2 = "SELECT * FROM Libros_usados"
                cursor.execute(sentencia2)
                cliente = cursor.fetchall()
                conexion.close()
                for n in cliente:
                    x.append(n)
                if consulta == '1':
                    n = 0
                    for cliente in x:
                        n = n + 1
                        try:
                            print('Libro', n, ' = Titulo de la obra:', cliente[0], ', Genero:', cliente[1],
                                  ', Paginas:', cliente[2], ', precio:', cliente[3], ', id_number:', cliente[4],
                                  ', condicion:', cliente[5], ', estado: ', cliente[6], ', tiempo de uso: ', cliente[7])
                        except:
                            print('Libro', n, ' = Titulo de la obra:', cliente[0], ', Genero:', cliente[1],
                                  ', Paginas:', cliente[2], ', precio:', cliente[3], ', id_number:', cliente[4])

                if consulta == '2':
                    cliente = random.choice(x)
                    try:
                        print('Titulo de la obra:', cliente[0], '\nGenero:', cliente[1],
                              '\nPaginas:', cliente[2], '\nprecio:', cliente[3], '\nid_number:', cliente[4],
                              '\ncondicion:', cliente[5], '\nestado: ', cliente[6], '\ntiempo de uso: ', cliente[7])
                    except:
                        print('Titulo de la obra:', cliente[0], '\nGenero:', cliente[1],
                              '\nPaginas:', cliente[2], '\nprecio:', cliente[3], '\nid_number:', cliente[4])
                break
            else:
                print('elija un numero entre las opciones.')




from datetime import datetime

import csv

ruta_csv = 'C:/Users/franc/PycharmProjects/Practicas fundamentos/App_libros/app.libros.csv'

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

        with open(ruta_csv, 'a', newline='\n') as archivo:
            campos = ['movimiento', 'fecha', 'nombre', 'apellido', 'id_number', 'contrasenia', 'libros']
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writerow({
                'movimiento': movimiento, 'fecha': fecha, 'nombre': nombre,
                'apellido': apellido, 'id_number': id_number, 'contrasenia': contrasenia
            })

        cliente_nuevo = Cliente(Nombre=nombre, Apellido=apellido,
                                id_number=id_number, contrasenia=contrasenia)
        cliente_nuevo.agregar_clientes()

    elif move == '2':
        movimiento = 'Baja'
        fecha = datetime.now()
        contrasenia = input('contrasenia: ')
        id_number = input('id_number: ')

        with open(ruta_csv, 'a', newline='\n') as archivo:
            campos = ['movimiento', 'fecha', 'nombre', 'apellido', 'contrasenia']
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writerow({
                'movimiento': movimiento, 'fecha': fecha,
                'nombre': '', 'apellido': '', 'contrasenia': contrasenia
            })
        cliente_a_eliminar = Cliente(Nombre='', Apellido='', id_number=id_number, contrasenia=contrasenia)
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

            with open(ruta_csv, 'a', newline='\n') as archivo:

                campos = ['movimiento', 'fecha', 'nombre', 'apellido', 'contrasenia']
                writer = csv.DictWriter(archivo, fieldnames=campos)
                writer.writerow({
                    'movimiento': movimiento, 'fecha': fecha,
                    'nombre': '', 'apellido': '', 'contrasenia': ''
                })
            libro_a_agregar = Libros(titulo_obra=titulo_obra, genero=genero, paginas=paginas,
                                     precio=precio, id_number=id_number)
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

            with open(ruta_csv, 'a', newline='\n') as archivo:
                campos = ['movimiento', 'fecha', 'nombre', 'apellido', 'contrasenia']
                writer = csv.DictWriter(archivo, fieldnames=campos)
                writer.writerow({
                    'movimiento': movimiento, 'fecha': fecha, 'nombre': '', 'apellido': '', 'contrasenia': ''
                })
            libro_u_agregar = Libros_usados(titulo_obra=titulo_obra, genero=genero, paginas=paginas, precio=precio,
                                            id_number=id_number, condicion=condicion, estado=estado, tiempo_de_uso=tiempo_de_uso)
            libro_u_agregar.agregar_libros_usados()



def manejo_de_foro():
    print('Seleccione una accion')
    print('1- Crear recomendacion')
    print('2- Buscar recomendaciones')
    opcion = input('opcion a elegir: ')
    if opcion == '1':
        titulo_obra = input('titulo_obra: ')
        puntaje = input('puntaje(1-10): ')
        recomendacion = input('recomendacion: ')
        conexion = sqlite3.connect(ruta_base_datos)
        cursor = conexion.cursor()
        m = (titulo_obra, puntaje, recomendacion)
        sentencia = "INSERT INTO foro VALUES (?, ?, ?)"
        cursor.executemany(sentencia, [m])
        conexion.commit()
        conexion.close()
        print('Gracias! Valoramos mucho tu opinion.')
    if opcion == '2':
        titulo_obra = input('titulo_obra: ')
        conexion = sqlite3.connect(ruta_base_datos)
        cursor = conexion.cursor()
        sentencia = "SELECT * FROM foro WHERE titulo_obra " + "LIKE '%" + titulo_obra + "%'"
        cursor.execute(sentencia)
        foro = cursor.fetchone()
        conexion.close()
        try:
            print('Titulo de la obra:', foro[0], '\nPuntaje', foro[1],
                    '\nRecomendacion:', foro[2])
        except:
            print('No encontramos el libro')


while True:

    print('Seleccione uno o dos:')
    print('1- Quiero conocer los libros')
    print('2- quiero modificar mis libros, registrarme, darme de baja.')
    print('3- quiero participar en el foro')
    seleccion = input('seleccion:')
    if seleccion == '1':
        consulta_de_libros()
        break
    elif seleccion == '2':
        registro_clientes()
        break
    elif seleccion == '3':
        manejo_de_foro()
        break

