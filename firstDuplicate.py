def firstDuplicate(arr):
    a = set()

    for val in arr:
        if val not in a:
            a.add(val)
        else:
            return val

    return -1
