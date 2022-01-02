def evenDigitsOnly(n):
    n = str(n)

    for c in n:
        if(int(c) % 2 == 1):
            return False

    return True
