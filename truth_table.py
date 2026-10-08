def truth_table(n):
    result = [()]

    for _ in range(n):
        new_result = []
        for row in result:
            new_result.append(row + (0,))
            new_result.append(row + (1,))
        result = new_result

    return result
