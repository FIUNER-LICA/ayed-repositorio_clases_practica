from modules.LDE import ListaDobleEnlazada

class Mazo:
        
    def __init__(self):
        # utiliza la lista doble enlazada para crear un mazo
        pass
    
    def poner_carta_arriba(self, carta):
        # agrega una carta a la parte de arriba del mazo
        # relacionar con algunos de los métodos de la clase ListaDobleEnlazada
        pass
        
    
    def sacar_carta_arriba(self, mostrar = False):
        # saca una carta de la parte de arriba del mazo
        # PROBAR la clase carta
        # si mostrar es true, se debe mostrar la carta sacada
        pass
    
    def poner_carta_abajo(self, carta):
        # agrega una carta a la parte de abajo del mazo
        # relacionar con algunos de los métodos de la clase ListaDobleEnlazada
        pass

    def __len__(self):
        # Retorna la cantidad de cartas en el mazo
        pass
    

class DequeEmptyError(Exception):
    # esto cumple el requerimiento de:
    # En caso de querer extraer una carta de un mazo vacío, 
    # se deberá lanzar la excepción DequeEmptyError (debe estar definido en el mismo archivo que la clase Mazo).
    # dejar así como está
    pass