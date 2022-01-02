def commonCharacterCount(s1, s2):
    s1 = getCounter(s1)
    s2 = getCounter(s2)

    s = 0
    for key in s1.keys():
        print(key)
        if key in s2:
            s += min(s1[key], s2[key])

    return s


def getCounter(str):
    arr = dict()

    for c in str:
        if c in arr:
            arr[c] += 1
        else:
            arr[c] = 1

    return arr
