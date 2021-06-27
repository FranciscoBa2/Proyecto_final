# import sys
# from App_libros import Cliente
# from App_libros import Arreglador

#
# argv = sys.argv
# if len(argv) == 1:
#     print('introduce el nombre del libro por favor')
# else:
#     info = Cliente(nombre='', apellido='', contrasenia='', telefono='', mail='', dni='')
#     listas = info.consulta_libro(argv[1])
#     lista_nueva = []
#     for n in listas:
#         if len(n) > 0:
#             lista_nueva.append(n)
#     if len(lista_nueva) > 0:
#         list_format = Arreglador(lista_nueva)
#         list_format = list_format.formato_dic_libros(cantidad_de_listas=0)
#         n = 0
#         for i in list_format:
#             n = n + 1
#             print('\nLibro', n, i)
#         if len(list_format) == 0:
#             print('No encontramos el libro')







