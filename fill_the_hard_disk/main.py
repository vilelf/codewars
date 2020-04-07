def save(files, storage):
    saved = 0
    for _file in files:
        if storage >= _file:
            saved += 1
            storage -= _file
        else:
            break
    return saved
