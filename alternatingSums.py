def alternatingSums(a):
    b = [a[i] for i in range(0, len(a), 2)]
    c = [a[i] for i in range(1, len(a), 2)]
    
    return [sum(b), sum(c)]