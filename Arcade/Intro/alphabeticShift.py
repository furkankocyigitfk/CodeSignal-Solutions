def alphabeticShift(inputString):
    s = ""
    for c in inputString:
        s += chr((ord(c) - ord("a") + 1) % 26 + ord("a"))

    return s
