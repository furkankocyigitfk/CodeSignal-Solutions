def sumUpNumbers(inputString):
    arr = list()
    number = ""

    for c in inputString:
        if not c.isnumeric() and len(number) != 0:
            arr.append(int(number))
            number = ""
        elif c.isnumeric():
            number += c

    if len(number) != 0:
        arr.append(int(number))

    return sum(arr)
