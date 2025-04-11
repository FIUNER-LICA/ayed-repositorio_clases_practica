
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
    mi_lista = [5, 3, 8, 6, 2, 7, 4, 1] 
    print(ordenamiento_por_seleccion(mi_lista))





    # M, N = 5000, 8000    
    # datos = [randint(-M, M) for _ in range(N)]
    # # datos = []
    # # for _ in range(N):
    # #     datos.append(randint(-M, M))    

    # datos_sel = ordenamiento_por_seleccion(datos.copy())
    # # print(datos)



    # datos_sorted = sorted(datos)




    # if datos_sel == datos_sorted:
    #     print("La lista está ordenada")
    # else:
    #     print("La lista no está ordenada")



    # assert datos_sel == datos_sorted


    # # Medicion de tiempo
    # inicio = time.time()
    # ordenamiento_por_seleccion(datos.copy())
    # fin = time.time()
    # print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")


