def longestDigitsPrefix(arr):
    for i in range(len(arr)):
        if not arr[i].isdigit():
            return arr[:i]
    return arr
