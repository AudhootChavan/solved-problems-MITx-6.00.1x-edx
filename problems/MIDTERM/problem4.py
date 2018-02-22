def flatten(aList):
    l = []
    for i in aList:
        if type(i) == int:
            l.append(i)
        else:
            for j in i:
                if type(j) == list:
                    for k in j:
                        if type(k) == list:
                            for m in k:
                                l.append(m)
                        else:
                            l.append(k)
                else:
                    l.append(j)
    return l
        
        
print(flatten([[1,'a',['cat'],1],[[[3]], 'dog'],4, 5]))
    