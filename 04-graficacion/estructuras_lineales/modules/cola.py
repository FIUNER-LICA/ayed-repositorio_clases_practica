# cola implementada con nodos y referencia

#NO es aconsejable la implementación con listas. En una cola se debe poder insertar en un extremo y eliminar del otro extremo
#Con una lista, una de estas dos opciones, siempre tiene orden de complejidad n

#Las opciones con una lista son:
#Opcion 1:
#    inserción: append() -> O(1)
#    eiminacion: pop(0) -> O(n)
#opcion 2:
#    inserción: insert(0,valor) -> O(n)
#    eliminacion: pop() -> O(1)

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        
        
class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamano = 0
    
    def esta_vacia(self):
        return self.primero is None
    
    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
        
        self.tamano += 1
    
    def eliminar(self):
        if self.esta_vacia():
            raise ValueError("La cola está vacía")
        
        valor_eliminado = self.primero
        self.primero = self.primero.siguiente
        
        # Si al eliminar, la cola queda vacía
        if self.primero is None:
            self.ultimo = None
        
        self.tamano -= 1
        return valor_eliminado
    
    def obtener_primero(self):
        if self.esta_vacia():
            raise ValueError("La cola está vacía")
        
        return self.primero.dato
    
    def obtener_ultimo(self):
        if self.esta_vacia():
            raise ValueError("La cola está vacía")
                
        return self.__ultimo.dato
    
    def __str__(self):
        if self.esta_vacia():
            return "Cola vacía"
        
        elementos = []
        actual = self.primero
        while actual is not None:
            elementos.append(f'{actual.dato}')
            actual = actual.siguiente
        
        elementos.reverse()
        return " -> ".join(elementos)

if __name__ == "__main__":
    cola = Cola()
    
    # Insertar elementos
    cola.insertar(10)
    cola.insertar(20)
    cola.insertar(30)
    cola.insertar(40)
    cola.insertar(50)
    cola.insertar(60)
    
    print("Cola inicial:", cola)
    print("Tamaño:", cola.tamano)
    print("primero:", cola.primero.dato)
    print("ultimo:", cola.ultimo.dato)
    print()
    
    # Eliminar elemento
    elemento_eliminado = cola.eliminar()
    print("Elemento eliminado:", elemento_eliminado.dato)
    print("Cola después de eliminar:", cola)
    print("Nuevo tamaño:", cola.tamano)
    print()

    cola.insertar(15)
    print("Inserto el 15")
    print("Cola después de insertar:", cola)
    print("Nuevo tamaño:", cola.tamano)

