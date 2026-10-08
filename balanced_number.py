def is_balanced_number(n):
    s = str(n)
    length = len(s)

    if length % 2 != 0:
        left_end = (length - 1) // 2
    else:
        left_end = (length - 2) // 2


    right_start = length - left_end


    left_part = s[:left_end]
    right_part = s[right_start:]


    left_sum = 0
    for char in left_part:
        left_sum += int(char)


    right_sum = 0
    for char in right_part:
        right_sum += int(char)

    if left_sum == right_sum:
        return "Balanced"
    else:
        return "Not Balanced"

