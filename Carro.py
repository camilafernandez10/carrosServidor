class Carro:
    def __init__(self,id, idMarca,logoCarro,modelo,precio):
        self.id=id
        self.idMarca=idMarca
        self.logoCarro=logoCarro
        self.modelo=modelo
        self.precio=precio

class Marca:
    def __init__(self,id, nombreMarca,logoMarca):
        self.id=id
        self.nombreMarca=nombreMarca
        self.logoMarca=logoMarca
