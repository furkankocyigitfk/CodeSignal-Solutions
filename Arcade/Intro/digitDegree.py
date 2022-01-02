def digitDegree(n):
    i = 0

    while n > 9:
        n = sum(list(map(int, str(n))))
        i += 1

    return i
