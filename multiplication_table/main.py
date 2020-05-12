def multiplication_table(size):
    a = []
    size += 1
    for n in range(1, size):
        a.append([x * n for x in range(1, size)])
    return a