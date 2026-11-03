def are_equivalent(f, g, n):
    for number in range(2 ** n):
        row = []
        for i in range(n):
            row.append(bool((number >> i) & 1))
        if f(*row) != g(*row):
            return False
        return True

