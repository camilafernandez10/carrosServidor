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

class Caract:
    def __init__(self,id, motor,color,cilindraje,potencia,fullequipo,traccion,frenos,seguridad):
        self.id=id
        self.motor=motor
        self.color=color
        self.cilindraje=cilindraje
        self.potencia=potencia
        self.fullequipo=fullequipo
        self.traccion=traccion
        self.frenos=frenos
        self.seguridad=seguridad

