def firstNotRepeatingCharacter(s):
    d = dict()

    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = 0

    for key, value in d.items():
        if value == 1:
            return key

    return '_'
