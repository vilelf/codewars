def josephus(l, n):
    n -= 1
    i, order = 0, []
    while len(l) > 0:
        i = (i + n) % len(l)
        order.append(l.pop(i))
    return order