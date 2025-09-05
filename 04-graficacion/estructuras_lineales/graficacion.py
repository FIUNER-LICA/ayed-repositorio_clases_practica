from matplotlib import pyplot as plt #pip install matplotlib
from random import randint
import time
from modules.cola import Cola
from modules.cola_list import Cola_list

tamanos = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

tiempos_eliminar_cola = []
tiempos_eliminar_cola_list = []

for n in tamanos:
    cola = Cola()
    cola_list = Cola_list()

    for _ in range(n):
        dato = randint(1, 100)
        cola.insertar(dato)
        cola_list.agregar(dato)
    
    contador = 0
    for _ in range(n):
        inicio = time.perf_counter()
        cola.eliminar()
        fin = time.perf_counter()
        contador += (fin - inicio)/n
    tiempos_eliminar_cola.append(contador)

    contador = 0
    for _ in range(n):
        inicio = time.perf_counter()
        cola_list.avanzar()
        fin = time.perf_counter()
        contador += (fin - inicio)/n
    tiempos_eliminar_cola_list.append(contador)

# Gráfico para inserción
plt.figure(figsize=(10, 6))
plt.plot(tamanos, tiempos_eliminar_cola, marker='o', label="eliminar cola - O(1)")
plt.plot(tamanos, tiempos_eliminar_cola_list, marker='o', label="eliminar cola_list - O(n)")
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos de eliminación')
plt.legend()
plt.grid()
plt.show()
