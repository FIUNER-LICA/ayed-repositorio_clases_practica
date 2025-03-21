# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

class Cuadrado:
    # Define una clase que representa un cuadrado con métodos para calcular su área y perímetro.

    def __init__(self, lado):
        # Constructor de la clase. Inicializa un cuadrado con el valor del lado proporcionado.
        # Si el lado es menor o igual a 0, lanza una excepción ValueError.
        if lado <= 0:
            raise ValueError("El lado debe ser positivo")
        self.__lado = lado  # Asigna el valor del lado al atributo de la instancia.

    @property
    def lado(self):
        # Método getter para el atributo 'lado'.
        return self.__lado
    
    @lado.setter
    def lado(self, nuevo_lado):
        # Método setter para el atributo 'lado'.
        # Si el nuevo lado es menor o igual a 0, lanza una excepción ValueError.
        if nuevo_lado <= 0:
            raise ValueError("El lado debe ser positivo")
        self.__lado = nuevo_lado  # Actualiza el atributo 'lado' con el nuevo valor.

    def area(self):
        # Calcula y devuelve el área del cuadrado (lado^2).
        return self.__lado ** 2

    def perimetro(self):
        # Calcula y devuelve el perímetro del cuadrado (4 * lado).
        return 4 * self.__lado
    
cuadrado1 = Cuadrado(5) # crea un cuadrado de lado 5
area = cuadrado1.area()  # area = lado al cuadrado
print(area)
perimetro = cuadrado1.perimetro() # perimetro = lado * 4
print(perimetro)
cuadrado1.lado = 10 # cambia el lado a 10 usando el setter
largo_lado = cuadrado1.lado # muestra el largo del lado usando el getter
print(largo_lado)
area = cuadrado1.area() # lado al cuadrado
print(area)
perimetro = cuadrado1.perimetro() # lado * 4
print(perimetro)
cuadrado1.lado = -5 # lanza una excepción
# cuadrado2 = Cuadrado(-5) # lanza una excepción









# if __name__ == "__main__":

#     cuadrado1 = Cuadrado(5) # crea un cuadrado de lado 5
#     area = cuadrado1.area()  # lado al cuadrado
#     print(area)
#     perimetro = cuadrado1.perimetro() # lado * 4
#     print(perimetro)
#     cuadrado1.lado = 10 # cambia el lado a 10 usando el setter
#     largo_lado = cuadrado1.lado # muestra el largo del lado usando el getter
#     print(largo_lado)
#     area = cuadrado1.area() # lado al cuadrado
#     print(area)
#     perimetro = cuadrado1.perimetro() # lado * 4
#     print(perimetro)
#     cuadrado1.lado = -5 # lanza una excepción
#     # cuadrado2 = Cuadrado(-5) # lanza una excepción
