# orden de complejidad del ordenamiento shell es O(n^2)
# en el mejor caso es O(n log n) y en el peor caso es O(n^2)
# el mejor caso se da cuando la lista está casi ordenada
# el peor caso se da cuando la lista está ordenada en orden inverso

# el ordenamiento shell es una variante del ordenamiento por inserción
# que divide la lista en sublistas más pequeñas
# y luego ordena las sublistas

from random import randint

def ordenamiento_shell(una_lista):
    # Inicializa el contador de sublistas con la mitad del tamaño de la lista
    contador_sublistas = len(una_lista) // 2
    # Mientras el contador de sublistas sea mayor que 0
    while contador_sublistas > 0:

        # Para cada posición de inicio en el rango del contador de sublistas
        for posicion_inicio in range(contador_sublistas):
            # Realiza el ordenamiento por brechas
            brecha(una_lista, posicion_inicio, contador_sublistas)

        # Imprime el estado de la lista después de cada incremento de tamaño
        #print("Después de los incrementos de tamaño", contador_sublistas, "La lista es", una_lista)

        # Reduce el contador de sublistas a la mitad
        contador_sublistas = contador_sublistas // 2

    return una_lista

def brecha(una_lista, inicio, brecha):
    # Para cada elemento en la lista comenzando desde el inicio más la brecha
    for i in range(inicio + brecha, len(una_lista), brecha):

        # Guarda el valor actual y la posición del elemento
        valor_actual = una_lista[i]
        posicion = i

        # Mientras la posición sea mayor o igual a la brecha y el valor en la posición menos la brecha sea mayor que el valor actual
        while posicion >= brecha and una_lista[posicion - brecha] > valor_actual:
            # Mueve el valor en la posición menos la brecha a la posición actual
            una_lista[posicion] = una_lista[posicion - brecha]
            # Actualiza la posición restando la brecha
            posicion = posicion - brecha

        # Coloca el valor actual en la posición correcta
        una_lista[posicion] = valor_actual

if __name__ == '__main__':
    # ordena numeros y palabras
    numeros = [5, 3, 8, 6, 7, 2]
    numeros = ordenamiento_shell(numeros)
    print(numeros)

    # palabras = ["empanada", "arepa", "asado", "pizza", "ravioles", "tacos", "sushi", "hamburguesa", "pancho", "papas fritas", "milanesa", "choripan", "huevo frito"]
    # palabras = ordenamiento_shell(palabras)
    # print(palabras)

    # M, N = 500, 800
    # datos = [randint(-M, M) for i in range(N)]
    # datos = ordenamiento_shell(datos)
    # print(datos)