class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def avanzar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)
    
if __name__ == "__main__":
    cola = Cola()

    cola.agregar(5)
    cola.agregar(10)
    cola.agregar(15)

    print(cola.items)