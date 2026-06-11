def suma_objetivo(nums, objetivo, indice, actual):

    if sum(actual) == objetivo:
        print(actual)

    if indice >= len(nums):
        return

    actual.append(nums[indice])

    suma_objetivo(nums, objetivo,
                  indice + 1, actual)

    actual.pop()

    suma_objetivo(nums, objetivo,
                  indice + 1, actual)

suma_objetivo([2, 4, 6, 8], 10, 0, [])