def almostIncreasingSequence(arr):
    if checkSorted(arr):
        return True

    for i in range(1, len(arr)):
        if arr[i-1] >= arr[i]:

            newArr1 = [arr[j] for j in range(len(arr))]
            newArr1.pop(i)
            newArr2 = [arr[j] for j in range(len(arr))]
            newArr2.pop(i-1)
            if (checkSorted(newArr1) == False and checkSorted(newArr2) == False):
                return False
    return True


def checkSorted(arr):
    for i in range(1, len(arr)):
        if(arr[i] <= arr[i - 1]):
            return False
    return True
