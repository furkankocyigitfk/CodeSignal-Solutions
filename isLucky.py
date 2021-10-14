def isLucky(n):
    s = str(n)
    fstr = [int(i) for i in s[:len(s)//2]]
    sstr = [int(i) for i in s[len(s)//2:]]

    if sum(fstr) == sum(sstr):
        return True
    return False
