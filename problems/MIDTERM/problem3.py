def deep_reverse(L):
    L.reverse()
    l = []
    for i in L:
        i.reverse()
        l.append(i) 
    return l
    
print(deep_reverse([[1,2],[3,4],[5,6,7]]))