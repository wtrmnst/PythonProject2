def are_equivalent(f, g, n):
    table = [()]

    for _ in range(n):
        new_table = []
        for row in table:
            new_table.append(row + (0,))
            new_table.append(row + (1,))
        table = new_table

    for row in table:
        result_f = f(*row)
        result_g = g(*row)

        if result_f != result_g:
            return False

    return True

