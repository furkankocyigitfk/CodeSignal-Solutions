def deleteDigit(n):
    n = str(n)
    m = 0

    for i in range(len(n)):
        x = int(n[:i] + n[(i+1):])
        if x > m:
            m = x

    return m
