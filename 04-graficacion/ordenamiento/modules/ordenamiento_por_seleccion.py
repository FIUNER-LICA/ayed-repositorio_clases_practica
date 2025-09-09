
from random import randint
import time

# esta version coloca el elemento más grande en su lugar correcto (al final de la lista)
def ordenamiento_por_seleccion(una_lista):
    for llenar_ranura in range(len(una_lista) - 1, 0, -1):
       posicion_del_mayor = 0
       for ubicacion in range(1, llenar_ranura + 1):
           if una_lista[ubicacion] > una_lista[posicion_del_mayor]:
               posicion_del_mayor = ubicacion

       temp = una_lista[llenar_ranura]
       una_lista[llenar_ranura] = una_lista[posicion_del_mayor]
       una_lista[posicion_del_mayor] = temp
    return una_lista


if __name__ == '__main__':
    numeros = [5, 3, 8, 6, 2, 7, 4, 1] 
    print(ordenamiento_por_seleccion(numeros))

    # palabras = ["empanada", "arepa", "asado", "pizza", "ravioles", "tacos", "sushi", "hamburguesa", "pancho", "papas fritas", "milanesa", "choripan", "huevo frito"]
    # palabras = ordenamiento_por_seleccion(palabras)
    # print(palabras)

    # M, N = 5000, 8000    
    # datos = [randint(-M, M) for _ in range(N)]
    # # datos = []
    # # for _ in range(N):
    # #     datos.append(randint(-M, M)) 
    # datos = ordenamiento_por_seleccion(datos)
    # print(datos)



