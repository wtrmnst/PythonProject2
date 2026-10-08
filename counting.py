def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def arrangements(n, k):
    if n < 0 or k < 0 or k > n:
        return 0


    result = 1
    for i in range(k):
        result *= (n - i)
    return result


def combinations(n, k):
    if n < 0 or k < 0 or k > n:
        return 0

    return arrangements(n, k) // factorial(k)
