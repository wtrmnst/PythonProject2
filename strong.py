import math

def is_strong(n):
    s = str(n)

    factorial_sum = 0
    for char in s:
        digit = int(char)
        factorial_sum += math.factorial(digit)

    return factorial_sum == n

