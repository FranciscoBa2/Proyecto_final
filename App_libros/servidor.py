from flask import Flask, jsonify
from App_libros import conexion_ejecucion_sentencia, Arreglador



app = Flask(__name__)


@app.route('/tyc', methods=['GET'])
def tyc():

    return jsonify({"tyc":"Qué puedes esperar de nosotros, donde se describe cómo proporcionamos y desarrollamos"
                          " nuestros servicios. Lo que esperamos de ti, donde se establecen ciertas reglas para"
                          " utilizar nuestros servicios. Contenido en los servicios de SwapBooks, donde se describen"
                          " los derechos de propiedad intelectual relacionados con el contenido que aparece en nuestros"
                          " servicios, ya sea propiedad tuya, de SwapBooks o de terceros. En caso de problemas o"
                          " discrepancias, donde se describen otros derechos legales que tienes y las consecuencias de"
                          " infringir estos términos. Al comprar un libro, aceptas que: (i) eres responsable de leer el"
                          " listado completo del libro antes de comprometerte a comprarlo. (ii) La tarifa por los"
                          " servicios y cualquier otro cargo que pueda incurrir en relación con tu uso del servicio, "
                          "como los impuestos y las posibles tarifas de transacción, se cobrarán mensualmente a tu"
                          " método de pago. (iii) Aceptas brindarnos tus datos personales como tus contactos, fotos y"
                          " cualquier informacion relevante para el uso de la aplicacion."})


@app.route('/estado_de_cuenta/<dni>', methods=['GET'])
def productosget(dni):
    data_cliente = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Clientes WHERE Id_number = '" + dni + "'",
                                                tipo_ejecucion='simple')
    data_libros_cliente = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Libros WHERE Id_number_clientes = '" +
                                                                 dni + "'",
                                                       tipo_ejecucion='simple')
    data_libros_cliente2 = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Libros_usados WHERE "
                                                                  "Id_number_clientes = '" + dni + "'",
                                                        tipo_ejecucion='simple')
    data_ventas = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Ventas",
                                               tipo_ejecucion='simple')
    solicitudes = conexion_ejecucion_sentencia(sentencia="SELECT * FROM Solicitudes_prestamos",
                                               tipo_ejecucion='simple')
    dta = []
    dta.append(data_libros_cliente)
    dta.append(data_libros_cliente2)
    libros_vendidos = []
    libros_solicitados = []
    for n in data_libros_cliente:
        for i in data_ventas:
            if n[4] == i[1]:
                libros_vendidos.append(n)
        for i in solicitudes:
            if n[4] == i[1]:
                libros_solicitados.append(n)
    for n in data_libros_cliente2:
        for i in data_ventas:
            if n[7] == i[1]:
                libros_vendidos.append(n)
        for i in solicitudes:
            if n[7] == i[1]:
                libros_solicitados.append(n)

    cliente = Arreglador(data_cliente)
    cliente = cliente.formato_dic_cliente()
    libros_cliente = Arreglador(dta)
    libros_cliente = libros_cliente.formato_dic_libros(cantidad_de_listas=2)
    ventas = Arreglador(libros_vendidos)
    ventas = ventas.formato_dic_libros(cantidad_de_listas=1)
    solicitados = Arreglador(libros_solicitados)
    solicitados = solicitados.formato_dic_libros(cantidad_de_listas=1)
    return jsonify({"datos_cliente": cliente, "data libros cliente": libros_cliente, "libros_vendidos": ventas,
                    "libros solicitados": solicitados, "status": "ok"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)



## quiero consultar que libros tengo.
##la api te dice en que estado se encuentra el libro/cliente.
