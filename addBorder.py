def addBorder(picture):
    m = len(picture[0])
    arr = list()
    arr.append("*"*(m+2))

    for pic in picture:
        arr.append("*"+pic+"*")
    arr.append("*"*(m+2))
    return arr
