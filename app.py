from flask import Flask, jsonify, request
from flask_cors import CORS
from DAO import mostrarCarac
from DAO import TestDrive
import mysql.connector
from mysql.connector import Error
import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/caract', methods=['GET'])
def all_caracteris():
    impcarac=mostrarCarac()
    arreglo = ""
    arreglo += "["
    lon=len(impcarac)
    i1=1
    for marca in impcarac:
        arreglo += json.dumps(marca.__dict__)
        if  i1<lon:
            arreglo += ","
            i1=i1+1
    arreglo += "]"
    obj = json.loads(arreglo)
    return jsonify({
        'status': 'success',
        'caract': obj
    })

@app.route('/test', methods=['POST'])
def agregar_cita():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        datos = request.get_json()
        idCliente = datos.get('idCliente')
        idCarro = datos.get('idCarro')
        hora = datos.get('hora')
        fecha = datos.get('fecha')
        comentario = datos.get('coment')
        rta = TestDrive(idCliente,idCarro,hora,fecha,comentario)
        print(rta)
        rta =str(rta)
        response_object['message'] = rta
    return jsonify(response_object)

if __name__ == '__main__':
    app.run(host="0.0.0.0")