def reverseInParentheses(str):
    for i in range(len(str)):
        if str[i] == "(":
            start = i
        if str[i] == ")":
            end = i
            return reverseInParentheses(str[:start] + str[start+1:end][::-1] + str[end+1:])
    return str