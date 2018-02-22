def g(i):
    return i > 5
    
def f(i):
    return i + 2

L = [0, -10, 5, 6, -4]

def applyF_filterG(L,f,g):
    l1 = []
    for i in L:
        if g(f(i)) == True:
            l1.append(i)
    del L[:]
    for k in l1:
        L.append(k)
    if L == []:
        return -1
    return max(L)

print(applyF_filterG(L,f,g))
print(L)