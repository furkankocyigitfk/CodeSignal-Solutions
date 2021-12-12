def fileNaming(names):
    res = []

    for name in names:
        if name in res:
            k = 1
            while "{}({})".format(name, k) in res:
                k += 1
            name = "{}({})".format(name, k)
        res.append(name)

    return res
