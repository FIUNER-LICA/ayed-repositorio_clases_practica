# orden de complejidad del ordenamiento burbuja es O(n^2)
# en el mejor caso es O(n) y en el peor caso es O(n^2)
# el mejor caso se da cuando la lista está ordenada
# el peor caso se da cuando la lista está ordenada en orden inverso

# el ordenamiento burbuja es un algoritmo de ordenamiento simple
# que compara cada elemento de la lista con el siguiente y los intercambia si están en el orden incorrecto
# el algoritmo se repite varias veces
# en cada pasada se coloca el elemento más grande en su lugar correcto
# el algoritmo se detiene cuando no se realizan intercambios en una pasada

# orden de complejidad del ordenamiento burbuja corto es O(n^2)

from random import randint

def ordenamiento_burbuja(lista):
    for num_pasadas in range(len(lista)-1, 0, -1):
        for j in range(num_pasadas):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def ordenamiento_burbuja_corto(lista):
    intercambiado = True
    num_pasadas = len(lista)-1
    while num_pasadas > 0 and intercambiado:
        intercambiado = False
        for j in range(num_pasadas):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambiado = True
        num_pasadas -= 1

if __name__ == '__main__':
    # ordena numeros y palabras

    numeros = [5, 3, 8, 6, 7, 2]
    numeros = ordenamiento_burbuja(numeros)
    print(numeros)

    # palabras = ["empanada", "arepa", "asado", "pizza", "ravioles", "tacos", "sushi", "hamburguesa", "pancho", "papas fritas", "milanesa", "choripan", "huevo frito"]
    # palabras = ordenamiento_burbuja(palabras)
    # print(palabras)

    # M, N = 5000, 8000
    # datos = [randint(-M, M) for i in range(N)]
    # # datos = []
    # # for _ in range(N):
    # #     datos.append(randint(-M, M)) 
    # datos = ordenamiento_burbuja(datos)
    # print(datos)




