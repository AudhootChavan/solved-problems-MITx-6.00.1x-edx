def longest_run(L):
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    l6 = []
    for i in range(len(L)):
        if i == 0:
            l1.append(L[i])
        else:
            if L[i] >= L[i-1]:
                l1.append(L[i])
                if i == len(L) - 1:
                    l3.append(l1)
            elif L[i] < L[i-1]:
                l3.append(l1)
                l1 = []
                l1.append(L[i]) 
                if i == len(L) - 1:
                    l3.append(l1)
        
    for i in range(len(L)):
        if i == 0:
            l2.append(L[i])
        else:
            if L[i] > L[i-1]:
                l4.append(l2)
                l2 = []
                l2.append(L[i])
                if i == len(L) - 1:
                    l4.append(l2)
            elif L[i] <= L[i-1]:
                l2.append(L[i])
                if i == len(L) - 1:
                    l4.append(l2)
                
    for k in l3:
        l5.append(len(k))
        
    for k in l4:
        l6.append(len(k))
    
    if max(l5) > max(l6):
        print (sum(l3[l5.index(max(l5))]))
    elif max(l5) < max(l6):
        print (sum(l4[l6.index(max(l6))]))
    elif max(l5) == max(l6):
        if l5.index(max(l5)) < l6.index(max(l6)):
            print (sum(l3[l5.index(max(l5))]))
        else:
            print (sum(l4[l6.index(max(l6))]))
        
            
        
        
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    return None 
            
    
            
        