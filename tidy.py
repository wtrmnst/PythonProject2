def is_tidy(n):
    s = str(n)

    sorted_s = "".join(sorted(s))

    return s == sorted_s
