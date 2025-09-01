class Cola_list:
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
    cola_list = Cola_list()

    cola_list.agregar(5)
    cola_list.agregar(10)
    cola_list.agregar(15)

    print(cola_list.items)