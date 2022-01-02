def firstDigit(inputString):
    for c in inputString:
        if '0' <= c <= '9':
            return c
