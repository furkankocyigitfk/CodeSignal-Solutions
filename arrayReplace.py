def arrayReplace(inputArray, elemToReplace, substitutionElem):
    arr = list()

    for i in inputArray:
        if i == elemToReplace:
            arr.append(substitutionElem)
        else:
            arr.append(i)
    return arr
