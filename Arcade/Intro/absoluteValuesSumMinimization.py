def absoluteValuesSumMinimization(arr):
    m = max(arr) * len(arr)
    k = 0
    for i in range(len(arr)):
        x = 0
        for j in range(len(arr)):
            x += abs(arr[j] - arr[i])

        print(x)
        if x < m:
            m = x
            k = i

    return arr[k]
