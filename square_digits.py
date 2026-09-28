def square_digits(n):
    result = ""
    for digit in str(n):
        result += str(int(digit)**2)
    return int(result)
