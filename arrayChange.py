def arrayChange(arr):
    m = 0
    for i in range(1, len(arr)):
        if(arr[i-1] >= arr[i]):
            m += arr[i-1] - arr[i] + 1
            arr[i] = arr[i-1] + 1
    return m
