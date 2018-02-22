def closest_power(base,num):
    l = []
    m = []
    temp = 0
    temp1 = base
    
    if num == 1 or base > num:
        return 0

    else:
        while base < num + 20:
            l.append(num-base)
            base = base*temp1
            temp = temp + 1
            
    for i in l:
        m.append(abs(i))

    return 1 + m.index(min(m))
        
        
print(closest_power(4,1))