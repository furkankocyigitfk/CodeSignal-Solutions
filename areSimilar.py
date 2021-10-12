def areSimilar(a, b):
    s = list()

    for i in range(len(a)):
        if(a[i] != b[i]):
            s.append(i)
          
    if(len(s)  == 0):
        return True
    
    if(len(s) > 2):
        return False
    
    return a[s[0]] == b[s[1]] and a[s[1]] == b[s[0]] 