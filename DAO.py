import mysql.connector
from mysql.connector import Error
from Carro import Carro
import json

def tomarConexión():
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='carros2',
                                             user='miguel',
                                             password='Rippe2611')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
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








