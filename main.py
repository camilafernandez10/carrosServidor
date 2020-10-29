#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error
from DAO import mostrarCarro
from DAO import mostrarMarcas
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

impmarcas=mostrarMarcas()
print("[")
lon=len(impmarcas)
i1=1
for marca in impmarcas:
    print(json.dumps(marca.__dict__))
    if  i1<lon:
        print(",")
        i1=i1+1
print("]")



