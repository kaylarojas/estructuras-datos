def permutaciones(nums, actual):

    if len(actual) == len(nums):
        print(actual)
        return

    for num in nums:

        if num not in actual:

            actual.append(num)

            permutaciones(nums, actual)

            actual.pop()

permutaciones([1, 2, 3], [])