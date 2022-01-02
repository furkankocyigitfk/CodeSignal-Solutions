def allLongestStrings(arr):
    m = len(arr[0])

    for i in range(1, len(arr)):
        if(len(arr[i]) > m):
            m = len(arr[i])

    res = list()

    for var in arr:
        if(len(var) == m):
            res.append(var)

    return res
