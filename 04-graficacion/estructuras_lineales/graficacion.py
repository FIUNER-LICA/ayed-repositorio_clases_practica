from matplotlib import pyplot as plt
from random import randint
import time
from modules.cola import Cola
from modules.cola_list import Cola_list

tamanos = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

tiempos_agregar_cola = []
tiempos_agregar_cola_list = []

for n in tamanos:
    cola = Cola()
    cola_list = Cola_list()
    
    contador = 0
    for _ in range(n):
        inicio = time.perf_counter()
        dato = randint(1, 100)
        cola.insertar(dato)
        fin = time.perf_counter()
        contador += fin - inicio
    tiempos_agregar_cola.append(contador)

    contador = 0
    for _ in range(n):
        inicio = time.perf_counter()
        dato = randint(1, 100)
        cola_list.agregar(dato)
        fin = time.perf_counter()
        contador += fin - inicio
    tiempos_agregar_cola_list.append(contador)

# Gráfico para inserción
plt.figure(figsize=(10, 6))
plt.plot(tamanos, tiempos_agregar_cola, marker='o', label="agregar cola - O(1)")
plt.plot(tamanos, tiempos_agregar_cola_list, marker='o', label="agregar cola_list - O(n)")
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos de inserción')
plt.legend()
plt.grid()
plt.show()
