def isBeautifulString(inputString):
    arr = dict()

    for key in inputString:
        if key not in arr:
            arr[key] = 1
        else:
            arr[key] += 1

    arr = dict(sorted(arr.items(), key=lambda item: item[0]))
    values = list(arr.values())

    if list(arr.keys())[-1] != chr(ord('a') + len(arr) - 1):
        return False

    for i in range(len(values)-1):
        if values[i] < values[i+1]:
            return False

    return True
