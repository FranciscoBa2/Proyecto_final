
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/producto', methods=['GET'])
def consulta():
    return 'Bienvenido a la aplicacion SwapBooks, estamos muy contentos de que seas parte de nuestra comunidad.'

@app.route('/tyc', methods=['GET'])
def tyc():

    return jsonify({"tyc":"Qué puedes esperar de nosotros, donde se describe cómo proporcionamos y desarrollamos nuestros servicios. "
                          "Lo que esperamos de ti, donde se establecen ciertas reglas para utilizar nuestros servicios. "
        "Contenido en los servicios de Google, donde se describen los derechos de propiedad intelectual relacionados "
        "con el contenido que aparece en nuestros servicios, ya sea propiedad tuya, de Google o de terceros. "
        "En caso de problemas o discrepancias, donde se describen otros derechos legales que tienes y las consecuencias de infringir estos términos."
        "Al comprar un libro, aceptas que: "
          "(i) eres responsable de leer el listado completo del libro antes de comprometerte a comprarlo. "
          "(ii) La tarifa por los servicios y cualquier otro cargo que pueda incurrir en relación con tu uso del servicio, "
          "como los impuestos y las posibles tarifas de transacción, se cobrarán mensualmente a tu método de pago."
          "(iii) Aceptas brindarnos tus datos personales como tus contactos, fotos y cualquier informacion relevante para el uso"
          "de la aplicacion."})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
