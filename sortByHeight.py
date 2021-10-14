def sortByHeight(a):
    b = sorted(list(filter(lambda x: x != -1, a)))
    j = 0

    for i in range(len(a)):
        if(a[i] != -1):
            a[i] = b[j]
            j += 1
    return a
