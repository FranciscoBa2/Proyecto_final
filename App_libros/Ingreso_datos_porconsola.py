from App_libros import Libros
from App_libros import Cliente
from App_libros import Libros_usados
from Conexion_con_api import consulta_libros_nyt_fict
from Conexion_con_api import consulta_libros_nyt_nonfict
from App_libros import Arreglador
from App_libros import conexion_ejecucion_sentencia
from App_libros import registrar_csv
import random


def interaccion_libros():
    while True:
        print('Elija una de las siguientes opciones: ')
        print('1-Buscar/Comprar libro')
        print('2-Busqueda de best-sellers NyT')
        consulta = input('Opcion a elegir: ')
        if consulta == '1' or consulta == '2':
            break
    print('Perfecto!')
    while True:
        if consulta == '1':
            print('¿Estas buscando algun libro en particular?')
            print('1- Si')
            print('2- No')
            respuesta1 = input('Respuesta: ')

            # Libro particular

            if respuesta1 == '1':
                titulo_obra = input('Nombre del libro: ')
                instancia = Cliente(Nombre='', Apellido='', contrasenia='', numero='', mail='', dni='')
                listas = instancia.consulta_libro(titulo_obra=titulo_obra)
                lista_nueva = []
                for n in listas:
                    if len(n) > 0:
                        lista_nueva.append(n)
                if len(lista_nueva) > 0:
                    list_format = Arreglador(lista_nueva)
                    list_format = list_format.formato_dic_libros(cantidad_de_listas=0)
                    n = 0
                    for i in list_format:
                        n = n + 1
                        print('\nLibro', n, i)
                    if len(list_format) == 0:
                        print('No hay ningun libro disponible por el momento')
                        break
                    print('¿Quieres comprar alguno de estos libros?')
                    print('1- Si')
                    print('2- No')
                    respuesta2 = input('Seleccion: ')
                    if respuesta2 == '1':
                        dni = input('Ingresa tu dni: ')
                        nombre = input('Nombre: ')
                        apellido = input('Apellido: ')
                        eleccion = input('¿Que libro queres?:   ')
                        print('1- Confirmar eleccion')
                        print('2- Cancelar')
                        seguro = input('¿Estas seguro? ')

                        # Ejecucion de compra

                        if seguro == '1':
                            for lista in listas:
                                try:
                                    atributos = lista[int(eleccion) - 1]
                                    if len(atributos) > 8:
                                        instancia = Cliente(Nombre='', Apellido='', contrasenia='', numero='', mail='',
                                                            dni='')
                                        instancia.comprar_libro(id_libro=atributos[7], precio=atributos[3], dni=dni)
                                        print('Compra satisfactoria de: ', atributos[0])
                                        registrar_csv(movimiento='compra', nombre=nombre, apellido=apellido,
                                                      contrasenia='', dni=dni,
                                                      alquiler='')
                                    else:
                                        instancia = Cliente(Nombre='', Apellido='', contrasenia='', numero='', mail='',
                                                            dni='')
                                        instancia.comprar_libro(id_libro=atributos[4], precio=atributos[3], dni=dni)
                                        print('Compra satisfactoria de: ', atributos[0])
                                        registrar_csv(movimiento='compra', nombre=nombre, apellido=apellido,
                                                      contrasenia='', dni=dni,
                                                      alquiler='')
                                except:
                                    continue
                        break

                    # Si o quiere comprar le ofrcemos alquilar despues de que diga que no.

                    if respuesta2 == '2':
                        print('¿Quieres alquilar alguno de estos libros?')
                        print('1- Si')
                        print('2- No')
                        alq = input('Respuesta: ')
                        if alq == '1':
                            nombre = input('Nombre: ')
                            apellido = input('Apellido: ')
                            numero = input('Numero telefonico: ')
                            mail = input('Mail: ')
                            dni = input('Dni: ')
                            eleccion_a = input('¿Que libro queres?:   ')
                            print('1- Confirmar eleccion')
                            print('2- Cancelar')
                            seguro = input('¿Estas seguro? ')
                            if seguro == '1':
                                for lista in listas:
                                    try:
                                        atributos = lista[int(eleccion_a) - 1]
                                        if len(atributos) > 8:
                                            instancia = Cliente(Nombre=nombre, Apellido=apellido, contrasenia='', numero=numero,
                                                                mail=mail,
                                                                dni=dni)
                                            instancia.solicitud_prestamo(titulo_obra=atributos[0], id_libro=atributos[7],
                                                                         nombre=nombre, apellido=apellido,
                                                                         telefono=numero, email=mail)
                                            print('Envio de solictud exitoso de: ', atributos)
                                            registrar_csv(movimiento='compra', nombre='', apellido='', contrasenia='',
                                                          dni=dni,
                                                          alquiler='')
                                            break
                                        else:
                                            instancia = Cliente(Nombre=nombre, Apellido=apellido, contrasenia='',
                                                                numero=numero, mail=mail, dni=dni)
                                            instancia.solicitud_prestamo(titulo_obra=atributos[0],
                                                                         id_libro=atributos[4],
                                                                         nombre=nombre, apellido=apellido,
                                                                         telefono=numero, email=mail)
                                            print('Envio de solictud exitoso de: ', atributos)
                                            registrar_csv(movimiento='compra', nombre='', apellido='', contrasenia='',
                                                          dni=dni, alquiler='')
                                            break
                                    except:
                                        continue
                            break
                        break
                else:
                    print('No encontramos el libro')
                    break
                break

            # Libros cualquiera

            if respuesta1 == '2':
                while True:
                    print('Elija una de las siguientes opciones.')
                    print('1- Lista de todos los libros diponibles')
                    print('2- Libro aleatorio')
                    consulta = input('Opcion a elegir: ')
                    if consulta == '1' or consulta == '2':
                        break
                instancia = Cliente(Nombre='', Apellido='', contrasenia='', numero='', mail='', dni='')
                listas = instancia.consulta_de_libros()

                # Todos los  libros disponibles

                if consulta == '1':
                    lis = Arreglador(listas)
                    lis = lis.formato_dic_libros(cantidad_de_listas=2)
                    n = 0
                    for i in lis:
                        n = n + 1
                        print('\nLibro', n, i)
                    if len(lis) == 0:
                        print('No hay ningun libro disponible por el momento')
                        break
                    while True:
                        print('¿Quieres comprar alguno de estos libros?')
                        print('1- si')
                        print('2- no')
                        respuesta2 = input('Seleccion: ')
                        if respuesta2 == '1' or respuesta2 == '2':
                            break
                    if respuesta2 == '1':
                        dni = input('Ingresa tu dni: ')
                        eleccion = input('Que libro queres?:   ')
                        print('1- Confirmar eleccion')
                        print('2- Cancelar')
                        seguro = input('¿Estas seguro? ')
                        if seguro == '1':
                            nueva_lista = []
                            for lista in listas:
                                for list in lista:
                                    nueva_lista.append(list)
                            try:
                                atributos = nueva_lista[int(eleccion) - 1]
                                if len(atributos) > 8:
                                    instancia1 = Cliente(Nombre='', Apellido='', contrasenia='', numero='', mail='',
                                                         dni='')
                                    instancia1.comprar_libro(id_libro=atributos[7], precio=atributos[3], dni=dni)
                                    print('Compra satisfactoria de: ', atributos[0])
                                    break
                                else:
                                    instancia2 = Cliente(Nombre='', Apellido='', contrasenia='', numero='', mail='',
                                                         dni='')
                                    instancia2.comprar_libro(id_libro=atributos[4], precio=atributos[3], dni=dni)
                                    print('Compra satisfactoria de: ', atributos[0])
                                    break
                            except Exception as e:
                                print('No se pudo realizar la compra.', 'Tipo de error', e)
                                break
                        break
                    if respuesta2 == '2':
                        print('¿Quieres alquilar alguno de estos libros?')
                        print('1- Si')
                        print('2- No')
                        alq = input('Respuesta: ')
                        if alq == '1':
                            nombre = input('Nombre: ')
                            apellido = input('Apellido: ')
                            numero = input('Numero telefonico: ')
                            mail = input('Mail: ')
                            dni = input('Dni: ')
                            eleccion_a = input('¿Que libro queres?:   ')
                            print('1- Confirmar eleccion')
                            print('2- Cancelar')
                            seguro = input('¿Estas seguro? ')
                            if seguro == '1':
                                nueva_lista = []
                                for lista in listas:
                                    for list in lista:
                                        nueva_lista.append(list)
                                try:
                                    atributos = nueva_lista[int(eleccion_a) - 1]
                                    print(atributos)
                                    if len(atributos) > 8:
                                        instancia = Cliente(Nombre=nombre, Apellido=apellido, contrasenia='',
                                                            numero=numero,
                                                            mail=mail,
                                                            dni=dni)
                                        instancia.solicitud_prestamo(titulo_obra=atributos[0],
                                                                     id_libro=atributos[7],
                                                                     nombre=nombre,
                                                                     apellido=apellido,
                                                                     telefono=numero,
                                                                     email=mail)
                                        print('Envio de solictud exitoso de: ', atributos[0])
                                        registrar_csv(movimiento='solicitud', nombre='', apellido='', contrasenia='',
                                                      dni=dni,
                                                      alquiler='')
                                        break
                                    else:
                                        instancia = Cliente(Nombre=nombre, Apellido=apellido, contrasenia='',
                                                            numero=numero,
                                                            mail=mail,
                                                            dni=dni)
                                        instancia.solicitud_prestamo(titulo_obra=atributos[0],
                                                                     id_libro=atributos[4],
                                                                     nombre=nombre,
                                                                     apellido=apellido,
                                                                     telefono=numero,
                                                                     email=mail)
                                        print('Envio de solictud exitoso de: ', atributos[0])
                                        registrar_csv(movimiento='solicitud', nombre='', apellido='', contrasenia='',
                                                      dni=dni,
                                                      alquiler='')
                                        break
                                except:
                                    continue
                    break

                if consulta == '2':
                    libro = Arreglador(listas)
                    libros = libro.formato_dic_libros(cantidad_de_listas=2)
                    if len(libros) == 0:
                        print('No hay ningun libro disponible por el momento')
                        break
                    libro_elegido = random.choice(libros)
                    print('Libro random: ', libro_elegido)
                    print('¿Quieres comprar alguno de estos libros?')
                    print('1- si')
                    print('2- no')
                    respuestad = input('Seleccion: ')
                    lista_nueva = []
                    for n in listas:
                        for i in n:
                            if len(i) > 0:
                                lista_nueva.append(i)
                    if respuestad == '1':
                        dni = input('dni: ')
                        try:
                            atributos = lista_nueva[0]
                            if len(atributos) > 8:
                                instancia = Cliente(Nombre='', Apellido='', contrasenia='', numero='', mail='',
                                                    dni=dni)
                                instancia.comprar_libro(id_libro=atributos[7], precio=atributos[3], dni=dni)
                                print('Compra satisfactoria de: ', atributos[0])
                            else:
                                instancia = Cliente(Nombre='', Apellido='', contrasenia='', numero='', mail='',
                                                    dni=dni)
                                instancia.comprar_libro(id_libro=atributos[4], precio=atributos[3], dni=dni)
                                print('Compra satisfactoria de: ', atributos[0])
                            break
                        except Exception as e:
                            print('No se pudo realizar la compra.','Tipo de error', e)
                            break
                    if respuestad == '2':
                        print('¿Quieres alquilar alguno de estos libros?')
                        print('1- Si')
                        print('2- No')
                        alq = input('Respuesta: ')
                        if alq == '1':
                            nombre = input('Nombre: ')
                            apellido = input('Apellido: ')
                            numero = input('Numero telefonico: ')
                            mail = input('Mail: ')
                            dni = input('Dni: ')
                            print('1- Confirmar eleccion')
                            print('2- Cancelar')
                            seguro = input('¿Estas seguro? ')
                            if seguro == '1':
                                nueva_lista = []
                                for lista in listas:
                                    for list in lista:
                                        nueva_lista.append(list)
                                try:
                                    atributos = nueva_lista[0]
                                    print(atributos)
                                    if len(atributos) > 8:
                                        instancia = Cliente(Nombre=nombre, Apellido=apellido, contrasenia='',
                                                            numero=numero,
                                                            mail=mail,
                                                            dni=dni)
                                        instancia.solicitud_prestamo(titulo_obra=atributos[0],
                                                                     id_libro=atributos[7],
                                                                     nombre=nombre,
                                                                     apellido=apellido,
                                                                     telefono=numero,
                                                                     email=mail)
                                        print('Envio de solictud exitoso de: ', atributos[0])
                                        registrar_csv(movimiento='solicitud', nombre='', apellido='', contrasenia='',
                                                      dni=dni,
                                                      alquiler='')
                                        break
                                    else:
                                        instancia = Cliente(Nombre=nombre, Apellido=apellido, contrasenia='',
                                                            numero=numero,
                                                            mail=mail,
                                                            dni=dni)
                                        instancia.solicitud_prestamo(titulo_obra=atributos[0],
                                                                     id_libro=atributos[4],
                                                                     nombre=nombre,
                                                                     apellido=apellido,
                                                                     telefono=numero,
                                                                     email=mail)
                                        print('Envio de solictud exitoso de: ', atributos[0])
                                        registrar_csv(movimiento='solicitud', nombre='', apellido='', contrasenia='',
                                                      dni=dni,
                                                      alquiler='')
                                        break
                                except:
                                    continue
                    break
                else:
                    print('Elija un numero entre las opciones.')
                break
            break

        if consulta == '2':
            print('Elija una de las siguientes opciones: ')
            print('1- Ficcion')
            print('2- No ficcion')
            respuesta = input('Opcion a elegir: ')
            if respuesta == '1':
                consulta_libros_nyt_fict(url='https://api.nytimes.com/svc/'
                                             'books/v3/lists/current/hardcover-fiction.json')
                break
            if respuesta == '2':
                consulta_libros_nyt_nonfict(url='https://api.nytimes.com/svc/'
                                                'books/v3/lists/current/paperback-nonfiction.json')
                break
        break



def registro_clientes():
    while True:
        print('Elija una de las siguientes opciones:')
        print('1- Alta cliente')
        print('2- Baja cliente')
        print('3- Ingreso de libros')
        print('4- Eliminar mis libros')
        print('5- Modificar mis datos')
        move = input('Tipo de movimiento: ')
        if move == '1' or move == '2' or move == '3' or move == '4' or move == '5':
            break
    if move == '1':
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        contrasenia = input('Contraseña: ')
        dni = input('Ingrese su dni:')
        numero = input('Ingrese su numero: ')
        mail = input('Ingrese su mail: ')

        cliente_nuevo = Cliente(Nombre=nombre, Apellido=apellido, contrasenia=contrasenia,
                                numero=numero, mail=mail, dni=dni)
        cliente_nuevo.agregar_clientes()

        registrar_csv(movimiento='insercion', nombre=nombre, apellido=apellido, contrasenia=contrasenia,
                      dni=dni, alquiler='')

    elif move == '2':
        contrasenia = input('Contraseña: ')
        dni = input('Dni: ')

        registrar_csv(movimiento='baja', nombre='', apellido='', contrasenia='', dni=dni, alquiler='')

        cliente_a_eliminar = Cliente(Nombre='', Apellido='', contrasenia=contrasenia, numero='', mail='', dni=dni)
        cliente_a_eliminar.desactivar_clientes()
        print('Operacion exitosa')

    elif move == '3':
        print('¿Que tipo de libro deseas insertar?')
        print('1- Nuevo')
        print('2- Usado')
        opcion = input('Opcion a elegir: ')
        if opcion == '1':
            dni = input('Dni: ')
            titulo_obra = input('Titulo de la obra: ')
            genero = input('Genero: ')
            paginas = input('Paginas: ')
            precio = input('Precio: ')
            alquiler = input('¿Quieres alquilarlo? (si/no): ')

            registrar_csv(movimiento='agregar_libros', nombre='', apellido='', contrasenia='', dni=dni,
                          alquiler=alquiler)
            libro_a_agregar = Libros(titulo_obra=titulo_obra, genero=genero, paginas=paginas,
                                     precio=precio, id_number=dni, alquiler=alquiler)
            n = libro_a_agregar.agregar_libros()

            if len(n) == 0:
                print('Por favor registrese antes de agregar un libro')
            else:
                print('Publicacion exitosa del libro:', titulo_obra)
        if opcion == '2':
            dni = input('Dni: ')
            titulo_obra = input('Titulo de la obra: ')
            genero = input('Genero: ')
            paginas = input('Paginas: ')
            precio = input('Precio: ')
            condicion = input('Condicion: ')
            tiempo_de_uso = input('Tiempo de uso: ')
            Alquiler = input('¿Quieres alquilarlo? (si/no): ')

            registrar_csv(movimiento='agregar_libros', nombre='', apellido='', contrasenia='', dni=dni, alquiler='')

            libro_u_agregar = Libros_usados(titulo_obra=titulo_obra, genero=genero,
                                            paginas=paginas, precio=precio, id_number=dni,
                                            condicion=condicion, tiempo_de_uso=tiempo_de_uso, alquiler=Alquiler)
            n = libro_u_agregar.agregar_libros_usados()
            if len(n) == 0:
                print('Por favor registrese antes de agregar un libro')
            else:
                print('Publicacion exitosa del libro:', titulo_obra)
    elif move == '4':
        dni = input('Dni: ')
        # para desactivar libros, le mostramos al cliente los que tiene publicados.
        instancia = Cliente(Nombre='', Apellido='', contrasenia='', numero='', mail='', dni='')
        listas = instancia.consulta_de_libros()
        lis = Arreglador(listas)
        lis = lis.formato_dic_libros(cantidad_de_listas=2)
        n = 0
        for i in lis:
            n = n + 1
            print('\nLibro', n, i)
        eleccion = input('¿Que libro querias eliminar?')

        nueva_lista = []
        for lista in listas:
            for list in lista:
                nueva_lista.append(list)
        try:
            atributos = nueva_lista[int(eleccion) - 1]
            if len(atributos) > 8:
                instancia1 = Libros_usados(titulo_obra='', genero='', paginas='', precio='', id_number='',
                                           condicion='', tiempo_de_uso='', alquiler='')
                instancia1.desactivar_libros(id_number_libro=atributos[7])
                print('Operacion exitosa')
            else:
                instancia2 = Libros(titulo_obra='', genero='', paginas='', precio='', id_number='', alquiler='')
                instancia2.desactivar_libros(id_number_libro=atributos[4])
                registrar_csv(movimiento='baja', nombre='', apellido='', contrasenia='', dni=dni, alquiler='')
                print('Operacion exitosa')
        except Exception as e:
            print('No se pudo realizar la operacion.', 'Tipo de error', e)
    elif move == '5':
        id = input('Introduce tu dni:')
        print('Cual de las siguientes opciones querias modificar? ')
        print('1- Nombre')
        print('2- Apellido')
        print('3- Contrasenia')
        print('4- Numero')
        print('5- Mail')
        columna = input('Eleccion: ')
        dato = input('Escriba el nuevo valor de la columna seleccionada: ')
        opciones_db = {'1': 'Nombre', '2': 'Apellido', '3': 'Contrasenia', '4': 'numero', '5': 'email'}
        try:
            modificar = Cliente(Nombre='', Apellido='', contrasenia='', numero='', mail='', dni=id)
            modificar.modificar_datos_cliente(columna=opciones_db[columna], dato=dato)
        except Exception as e:
            print('No se pudo modificar la columna seleccionada, verifique nuevamente sus datos.', e)
def manejo_de_foro():
    print('Seleccione una accion')
    print('1- Crear recomendacion')
    print('2- Buscar recomendaciones')
    opcion = input('Opcion a elegir: ')
    if opcion == '1':
        titulo_obra = input('Titulo de la obra: ')
        puntaje = input('Puntaje(1-10): ')
        recomendacion = input('Recomendacion: ')
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        registrar_csv(movimiento='creacion_recomendacion', nombre=nombre, apellido=apellido, contrasenia='',
                      dni='', alquiler='')
        instancia = Cliente(Nombre='', Apellido='', contrasenia='', numero='', mail='', dni='')
        instancia.crear_recomendacion(titulo_obra=titulo_obra, puntaje=puntaje, recomendacion=recomendacion,
                                      nombre=nombre, apellido=apellido)
        print('Gracias! Valoramos mucho tu opinion.')

    if opcion == '2':
        titulo_obra = input('Titulo de la obra: ')
        foro = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Foro WHERE Titulo_obra " + "LIKE '%" +
                                                      titulo_obra + "%'", tipo_ejecucion='simple')
        try:
            if len(foro) > 0:
                for recomendacion in foro:
                    print('Titulo de la obra:', recomendacion[1], '\nPuntaje', recomendacion[2],
                            '\nRecomendacion:', recomendacion[3], '\nNombre del usuario que escribio la recomendacion:',
                          recomendacion[4], '\nSu apellido:', recomendacion[5])
            else:
                print('No encontramos una recomendacion del libro seleccionado')
        except:
            print('No encontramos una recomendacion del libro seleccionado')


while True:
    print('Bienvenido a la aplicacion SwapBooks, estamos muy contentos de que seas parte de nuestra comunidad.')
    print('Seleccione una de las tres opciones:')
    print('1- Quiero conocer/comprar los libros.')
    print('2- Quiero modificar mis libros, registrarme o darme de baja.')
    print('3- Quiero dar/buscar una reseña de un libro.')
    seleccion = input('Seleccion:')
    if seleccion == '1':
        interaccion_libros()
        break
    elif seleccion == '2':
        registro_clientes()
        break
    elif seleccion == '3':
        manejo_de_foro()
        break

