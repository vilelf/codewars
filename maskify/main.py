def maskify(cc):
    s = cc[-4:]
    if len(cc) > 4:
        return '#' * (len(cc) - 4) + s
    return s