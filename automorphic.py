def is_automorphic(n):
    square = n * n

    str_n = str(n)
    str_square = str(square)

    length = len(str_n)
    tail = str_square[-length:]

    return tail == str_n
