def digitsProduct(n):
    for i in range(1, 22655+1):  # 2*2*6*5*5 = 600
        cc = str(i)
        j = 1

        for c in cc:
            j *= int(c)

        if j == n:
            return i

    return -1
