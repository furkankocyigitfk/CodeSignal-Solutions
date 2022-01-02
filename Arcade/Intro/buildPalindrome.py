def buildPalindrome(st):
    if st == st[::-1]:
        return st

    i = 0
    subStr = st[i:]

    while subStr != subStr[::-1]:
        i += 1
        subStr = st[i:]

    return st + st[i - 1::-1]
