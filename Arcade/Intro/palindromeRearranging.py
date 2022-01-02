def palindromeRearranging(str):
    str = getCounter(str)

    if(sum(str.values()) % 2 == 0):
        for val in str.values():
            if val % 2 == 1:
                return False
    else:
        count = 0
        for val in str.values():
            if val % 2 == 1:
                count += 1
                if count == 2:
                    return False

    return True


def getCounter(str):
    arr = dict()

    for c in str:
        if c in arr:
            arr[c] += 1
        else:
            arr[c] = 1

    return arr
