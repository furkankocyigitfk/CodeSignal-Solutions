def arrayMaxConsecutiveSum(arr, k):
    m = sum(arr[:k])
    s = m
    for i in range(1, len(arr)-k+1):
        s = s - arr[i-1] + arr[i+k-1]
        if s > m:
            m = s

    return m
