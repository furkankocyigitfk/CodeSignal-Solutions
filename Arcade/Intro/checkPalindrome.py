def checkPalindrome(str):
    flag = True
    for i in range(len(str)//2):
        if str[i] != str[len(str) - i - 1]:
            flag = False
    return flag
