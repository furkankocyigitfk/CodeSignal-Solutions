def isAdmissibleOverpayment(prices, notes, res):
    arr = list()

    for i in range(len(notes)):
        x = notes[i].split(" ")
        arr.append(prices[i])

        if(x[0] != "Same" and float(x[0][:-1]) != 0):
            val = float(x[0][:-1])
            if(x[1] == "higher"):
                arr[-1] /= (1 + val / 100)
            elif(x[1] == "lower"):
                arr[-1] /= (1 - val / 100)

    return sum(prices) <= sum(arr) + res
