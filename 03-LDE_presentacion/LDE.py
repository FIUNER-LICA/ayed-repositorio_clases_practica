# Lista Doble Enlazada utilizando nodos y referencias

"""
A medida que completen los métodos de la clase Nodo y ListaDobleEnlazada, el "pass" debe ser reemplazado por la implementación correspondiente
"""

# *********** Clase Nodo ***********
class Nodo:
    def __init__(self, dato):
        # Inicializa un nodo con el dato proporcionado y sin referencias a otros nodos
        pass

# *********** Clase ListaDobleEnlazada ***********
class ListaDobleEnlazada:
    def __init__(self):
        # El inicializador __init__ debe crear una lista originalmente vacía
        pass

    def agregar_al_inicio(self, dato):
        # Agrega un nuevo ítem al inicio de la lista.
        pass

    def agregar_al_final(self, dato):
        # Agrega un nuevo ítem al final de la lista.
        pass

    def insertar(self, dato, posicion):
        """
        Agrega un nuevo ítem a la lista en "posicion". 
        Si la posición no se pasa como argumento, el ítem debe añadirse al final de la lista. 
        "posicion" es un entero que indica la posición en la lista donde se va a insertar el nuevo elemento. 
        Si se quiere insertar en una posición inválida, que se arroje la debida excepción.

        """
        pass

    def extraer(self, posicion=None):
        """
        elimina y devuelve el ítem en "posición". 
        Si no se indica el parámetro posición o este es igual a -1, se elimina y devuelve el último elemento de la lista. 
        La complejidad de extraer elementos de los extremos de la lista debe ser O(1). 
        Si se quiere extraer de una posición indebida, que se arroje la debida excepción.

        """
        pass

    def copiar(self):
        """
        Realiza una copia de la lista elemento a elemento y devuelve la copia. 
        Verificar que el orden de complejidad de este método sea O(n) y no O(n^2).

        """
        pass

    def invertir(self):
        # Invierte el orden de los elementos de la lista.
        pass

    def concatenar(self, otra_lista):
        # Recibe una lista como argumento y retorna la lista actual con la lista pasada como parámetro concatenada al final de la primera.
        pass

    def esta_vacia(self):
        # Devuelve True si la lista está vacía.
        pass

    def __len__(self):
        # Devuelve el número de ítems de la lista.
        pass

    def __add__(self, otra_lista):
        pass

    def __iter__(self):
        # permite que la lista sea recorrida con un ciclo for
        pass
    
    def __str__(self):
        # sirve para poder mostrar el contenido de una LDE por consola con la función print
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <-> ".join(elementos)

if __name__ == "__main__":
    # pruebas de uso

    LDE1 = ListaDobleEnlazada()
    LDE1.agregar_al_final(1)
    LDE1.agregar_al_final(2)
    LDE1.agregar_al_final(3)
    LDE1.agregar_al_final(4)
    print(LDE1)

    # LDE1.agregar_al_final(5)
    # ....
    # probar todos los métodos
