def dotProduct(listA,listB):
    total = 0
    
    for i in range(len(listA)):
        total = total + (listA[i] * listB[i])
    return total
    
    

print(dotProduct([1,2,3],[4,5,6]))