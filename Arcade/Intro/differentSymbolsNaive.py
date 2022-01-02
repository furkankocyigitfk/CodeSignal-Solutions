def differentSymbolsNaive(s):
    arr = dict()

    for key in s:
        if key not in arr.keys():
            arr[key] = 0

    return len(arr)
