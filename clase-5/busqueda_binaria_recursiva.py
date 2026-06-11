def busqueda_binaria(lista, valor, inicio, fin):

    # Caso base: el elemento no existe
    if inicio > fin:
        return -1

    medio = (inicio + fin) // 2

    # Elemento encontrado
    if lista[medio] == valor:
        return medio

    # Buscar en la mitad izquierda
    elif valor < lista[medio]:
        return busqueda_binaria(
            lista,
            valor,
            inicio,
            medio - 1
        )

    # Buscar en la mitad derecha
    else:
        return busqueda_binaria(
            lista,
            valor,
            medio + 1,
            fin
        )


# Ejemplo de uso
numeros = [2, 5, 8, 12, 16, 23, 38, 56, 72]

indice = busqueda_binaria(
    numeros,
    23,
    0,
    len(numeros) - 1
)

print(indice)