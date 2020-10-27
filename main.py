#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error
from DAO import mostrarCarro
import json
import cgi

print('Content-Type: text/json')
print('')

data=cgi.FieldStorage()

impcarros=mostrarCarro()
print("[")
longitud=len(impcarros)
i=1
for carro in impcarros:
    print(json.dumps(carro.__dict__))
    if  i<longitud:
        print(",")
        i=i+1
print("]")




