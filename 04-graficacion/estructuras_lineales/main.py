from matplotlib import pyplot as plt
from random import randint
import time
from modules.cola import Cola
from modules.cola_list import Cola_list

tamanos = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
# tamanos = range(1,1000,10)

tiempos_agregar_cola = []
tiempos_agregar_cola_list = []
tiempos_eliminar_cola = []
tiempos_eliminar_cola_list = []

# figsize es el tamaño de la figura en pulgadas (width, height)
plt.figure(figsize=(10, 6))

cola = Cola()
cola_list = Cola_list()

for n in tamanos:
    
    for _ in range(n):
        count = 0
        dato = randint(1, 100)
        inicio = time.perf_counter()
        cola.insertar(dato)
        fin = time.perf_counter()  
        count += (fin - inicio)  
    tiempos_agregar_cola.append(count)   

    for _ in range(n):
        count = 0
        dato = randint(1, 100)
        inicio = time.perf_counter()
        cola_list.agregar(dato)
        fin = time.perf_counter()  
        count += (fin - inicio)  
    tiempos_agregar_cola_list.append(count)      

# plt.plot(tamanos, tiempos_ordenamiento_por_seleccion, marker='o', label="ordenamiento_por_seleccion")
plt.plot(tamanos, tiempos_agregar_cola, marker='o', label="agregar cola - O(1)")
plt.plot(tamanos, tiempos_agregar_cola_list, marker='o', label="agregar cola_list - O(n)")

plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos de ordenamiento')
plt.legend() # para mostrar el nombre del método de ordenamiento. Es el "label" del metodo plot
plt.grid() # cuadriculado
plt.show()