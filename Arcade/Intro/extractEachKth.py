def extractEachKth(arr, k):
    a = list()

    for i in range(len(arr)):
        if (i+1) % k != 0:
            a.append(arr[i])

    return a
