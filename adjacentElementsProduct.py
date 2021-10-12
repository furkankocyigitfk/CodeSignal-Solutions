def adjacentElementsProduct(arr):
    m = min(arr) * max(arr)
    
    newArr = [m] * (len(arr) - 1)
    
    for i in range(1, len(arr)):
        newArr[i-1] = arr[i] * arr[i-1]
        
    return max(newArr)