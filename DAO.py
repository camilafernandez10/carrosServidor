import mysql.connector
from mysql.connector import Error
from Carro import Carro
from Carro import Marca
from Carro import Caract
import json

def tomarConexión():
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='carros2',
                                             user='miguel',
                                             password='Rippe2611')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
        return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        raise e

cnx=tomarConexión()
cursor=cnx.cursor()

def mostrarCarro():
    cursor.execute('select * from carros;')
    carros=[]
    for datos in cursor:
        carro=Carro(datos[0],datos[1],datos[2],datos[3],datos[4])
        carros.append(carro)
    return carros

def mostrarMarcas():
    cursor.execute('select * from marcas;')
    marcas=[]
    for datos in cursor:
        marca=Marca(datos[0],datos[1],datos[2])
        marcas.append(marca)
    return marcas

def mostrarCarac():
    cursor.execute('select * from carac;')
    caract=[]
    for datos in cursor:
        carac=Caract(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8])
        caract.append(carac)
    return caract








