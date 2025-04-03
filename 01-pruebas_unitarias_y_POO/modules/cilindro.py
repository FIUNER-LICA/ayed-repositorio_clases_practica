import math

class Cilindro:
    def __init__(self, radio, altura):
        if radio <= 0 or altura <= 0:
            raise ValueError("Radio y altura deben ser positivos")
        self.__radio = radio
        self.__altura = altura

    @property
    def radio(self):
        return self.__radio
    
    @property
    def altura(self):
        return self.__altura
    
    @radio.setter
    def radio(self, nuevo_radio):
        if nuevo_radio <= 0:
            raise ValueError("El radio debe ser positivo")
        self.__radio = nuevo_radio

    @altura.setter
    def altura(self, nueva_altura):
        if nueva_altura <= 0:
            raise ValueError("La altura debe ser positiva")
        self.__altura = nueva_altura
    
    def volumen(self):
        return math.pi * (self.__radio ** 2) * self.__altura
    
    def area_superficial(self):
        area = 2 * math.pi * self.__radio * (self.__radio + self.__altura)
        return area