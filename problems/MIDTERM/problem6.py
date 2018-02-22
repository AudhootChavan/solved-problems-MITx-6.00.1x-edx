def f(a,b):
    return a > b


def dict_interdiff(d1,d2):
    l1 = list(d1.keys())
    l2 = list(d2.keys())
    l3 = []
#elements of uncommon l1
    l4 = []
#elements of unncommon l2
    l5 = []
    d = {}
    e = {}
    for i in l1:
        if i in l2:
            l3.append(i)
        else:
            l4.append(i)
    #print(l4)
            
    for k in l2:
        if k not in l1:
            l5.append(k)
    #print(l5)
            
    for j in l3:
        d[j] = f(d1[j],d2[j])
    
    for i in l4:
        e[i] = d1[i]

    for i in l5:
        e[i] = d2[i]

    return (d,e)
    
#print(dict_interdiff({1:30, 2:20, 3:30, 5: 80},{1:40, 2:50, 3:60, 4:70, 6:90}))
print(dict_interdiff({1:30, 2:20, 3:30},{1:40, 2:50, 3:60}))
