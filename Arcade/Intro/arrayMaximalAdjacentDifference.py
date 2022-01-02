def arrayMaximalAdjacentDifference(arr):
    prediff = [abs(arr[i] - arr[i+1]) for i in range(0, len(arr)-1)]

    return max(prediff)
