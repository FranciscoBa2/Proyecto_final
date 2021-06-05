
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/producto', methods=['GET'])
def consulta():
    return 'Bienvenido!'


if __name__ == '__main__':
    app.run(debug=True, port=4000)