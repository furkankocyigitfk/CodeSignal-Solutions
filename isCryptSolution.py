def isCryptSolution(crypt, solution):
    d = dict()

    for line in solution:
        d[line[0]] = line[1]

    arr = list()

    for val in crypt:
        if d[val[0]] == "0" and len(val) > 1:
            return False
        s = ""
        for c in val:
            s += d[c]
        arr.append(int(s))

    return arr[2] == arr[1] + arr[0]
