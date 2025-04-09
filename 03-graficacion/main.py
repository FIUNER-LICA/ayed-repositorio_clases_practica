from matplotlib import pyplot as plt
from random import randint
import time
from modules.ordenamiento_por_seleccion import ordenamiento_por_seleccion

tamanos = [1, 10, 100, 200, 500, 700, 1000]

tiempos_ordenamiento_por_seleccion = []

# figsize es el tamaño de la figura en pulgadas (width, height)
plt.figure(figsize=(10, 6))

for n in tamanos:
    # datos = []
    # for _ in range(n):
    #     datos.append(randint(1, 10000))
    datos = [randint(1, 10000) for _ in range(n)]

    inicio = time.perf_counter()
    ordenamiento_por_seleccion(datos.copy())
    fin = time.perf_counter()
    tiempos_ordenamiento_por_seleccion.append(fin - inicio)        

# plt.plot(tamanos, tiempos_ordenamiento_por_seleccion, marker='o', label="ordenamiento_por_seleccion")
plt.plot(tamanos, tiempos_ordenamiento_por_seleccion)

plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos de ordenamiento')
plt.legend() # para mostrar el nombre del método de ordenamiento. Es el "label" del metodo plot
plt.grid() # cuadriculado
plt.show()