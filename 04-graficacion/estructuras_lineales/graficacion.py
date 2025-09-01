from matplotlib import pyplot as plt
from random import randint
import time
from modules.cola import Cola
from modules.cola_list import Cola_list

tamanos = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]

tiempos_agregar_cola = []
tiempos_agregar_cola_list = []
tiempos_remover_cola = []
tiempos_remover_cola_list = []

plt.figure(figsize=(10, 6))

for n in tamanos:
    cola = Cola()
    cola_list = Cola_list()
    
    # Medir tiempo para agregar Cola    
    for _ in range(n):
        contador = 0
        inicio = time.perf_counter()
        dato = randint(1, 100)
        cola.insertar(dato)
        fin = time.perf_counter()
        contador += (fin - inicio)
    tiempos_agregar_cola.append(contador)

    # Medir tiempo para agregar Cola_list
    contador = 0
    for _ in range(n):
        inicio = time.perf_counter()
        dato = randint(1, 100)
        cola_list.agregar(dato)
        fin = time.perf_counter()
        contador += (fin - inicio)
    tiempos_agregar_cola_list.append(contador)

plt.plot(tamanos, tiempos_agregar_cola, marker='o', label="agregar cola - O(1)")
plt.plot(tamanos, tiempos_agregar_cola_list, marker='o', label="agregar cola_list - O(n)")
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos de inserción')
plt.legend()
plt.grid()
plt.show()