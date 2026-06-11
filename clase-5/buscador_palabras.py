def existe_palabra(tablero, palabra):
    filas = len(tablero)
    columnas = len(tablero[0])

    def backtracking(fila, columna, indice):
        # Caso base: ya encontramos toda la palabra
        if indice == len(palabra):
            return True

        # Validar límites del tablero
        if fila < 0 or fila >= filas:
            return False

        if columna < 0 or columna >= columnas:
            return False

        # Validar si la letra actual coincide
        if tablero[fila][columna] != palabra[indice]:
            return False

        # Marcar la celda como visitada
        letra_original = tablero[fila][columna]
        tablero[fila][columna] = "#"

        # Probar las 4 direcciones
        encontrado = (
            backtracking(fila + 1, columna, indice + 1) or  # abajo
            backtracking(fila - 1, columna, indice + 1) or  # arriba
            backtracking(fila, columna + 1, indice + 1) or  # derecha
            backtracking(fila, columna - 1, indice + 1)     # izquierda
        )

        # Deshacer el cambio
        tablero[fila][columna] = letra_original

        return encontrado

    # Probar iniciar desde cada celda del tablero
    for fila in range(filas):
        for columna in range(columnas):
            if backtracking(fila, columna, 0):
                return True

    return False

tablero = [
    ["C", "A", "T"],
    ["D", "O", "G"],
    ["R", "A", "T"]
]

print(existe_palabra(tablero, "CAT"))
print(existe_palabra(tablero, "DOG"))
print(existe_palabra(tablero, "CAR"))