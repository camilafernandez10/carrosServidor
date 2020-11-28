from flask import Flask, jsonify
from flask_cors import CORS
from DAO import mostrarCarac
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
    arreglo + "["
    lon=len(impcarac)
    i1=1
    for marca in impcarac:
        arreglo + json.dumps(marca.__dict__)
        if  i1<lon:
            arreglo + ","
            i1=i1+1
    arreglo + "]"

    return jsonify({
        'status': 'success',
        'caract': arreglo
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0")