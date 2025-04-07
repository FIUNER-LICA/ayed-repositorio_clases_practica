from modules.ordenamiento_por_seleccion import ordenamiento_por_seleccion
from modules.ordenamiento_burbuja import ordenamiento_burbuja_corto
from modules.ordenamiento_burbuja import ordenamiento_burbuja
from modules.ordenamiento_shell import ordenamiento_shell
import time
import matplotlib.pyplot as plt
from random import randint

def medir_tiempos(metodo_ord, tamanos, caso):
    tiempos = []
    for n in tamanos:
        if caso == "mejor":
            lista = list(range(n))  # Lista ordenada
        elif caso == "promedio":
            lista = [randint(-1000, 1000) for _ in range(n)]  # Caso promedio: lista aleatoria
        elif caso == "peor":
            lista = list(range(n, 0, -1))  # Peor caso: lista en orden inverso

        inicio = time.perf_counter()
        metodo_ord(lista.copy())  # Ordenar una copia de la lista
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return tiempos

def graficar_casos():
    tamanos = [1, 10, 100, 200, 500, 700, 1000]
    metodos = [
        ordenamiento_por_seleccion,
        ordenamiento_burbuja_corto,
        ordenamiento_burbuja,
        ordenamiento_shell
    ]

    fig, axs = plt.subplots(1, 3, figsize=(18, 6))  # Crear una figura con 3 subgráficas

    casos = ["mejor", "promedio", "peor"]
    titulos = ["Mejor Caso", "Caso Promedio", "Peor Caso"]

    # Variable para rastrear el valor máximo de tiempo
    max_tiempo = 0

    # Calcular los tiempos y graficar
    for i, caso in enumerate(casos):
        for metodo in metodos:
            tiempos = medir_tiempos(metodo, tamanos, caso)
            axs[i].plot(tamanos, tiempos, marker='o', label=metodo.__name__)
            max_tiempo = max(max_tiempo, max(tiempos))  # Actualizar el tiempo máximo

        axs[i].set_title(titulos[i])
        axs[i].set_xlabel('Tamaño de la lista')
        axs[i].set_ylabel('Tiempo (segundos)')
        axs[i].legend()
        axs[i].grid()

    # Establecer la misma escala para todas las gráficas
    for ax in axs:
        ax.set_ylim(0, max_tiempo * 1.1)  # Escala uniforme con un margen del 10%

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    graficar_casos()