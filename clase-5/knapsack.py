def knapsack(capacidad, pesos, valores, n):

    if n == 0 or capacidad == 0:
        return 0

    if pesos[n-1] > capacidad:
        return knapsack(capacidad,
                        pesos,
                        valores,
                        n-1)

    incluir = valores[n-1] + knapsack(
        capacidad - pesos[n-1],
        pesos,
        valores,
        n-1
    )

    excluir = knapsack(
        capacidad,
        pesos,
        valores,
        n-1
    )

    return max(incluir, excluir)


pesos = [5, 4, 3]
valores = [10, 8, 6]

print(knapsack(10, pesos, valores, len(pesos)))