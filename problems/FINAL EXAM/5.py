def general_poly(L):
    def inner(x):
        total = 0
        for i in range(len(L)):
            total = total + (L[i] * (x**(len(L)-1-i)))
        return total
    return inner
    
    #after returning just the function the last line becomes in_poly(10)
    
    
#print(general_poly([1, 2, 3, 4])(10))