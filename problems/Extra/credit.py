s = input("CARD NUMBER:")
t = ''
p = ''
temp = 0
sum = 0
temp1 = 0

for i in range(1,len(s),2):
    t = t + s[i]

for l in range(0,len(s),2):
    p = p + s[l]

for m in range(len(p)):
    temp = int(p[m])
    temp1 = temp1 + temp
    
for j in range(0,len(t)):
    temp = int(t[j])
    temp = temp*2
    if temp >= 10:
        temp = str(temp)
        for k in range(1):
            temp = int(temp[k])+ int(temp[k+1])
            sum = sum + temp
            temp = 0
    else:
        sum = sum + temp
        temp = 0
        
sum = sum + temp1


if sum%10 == 0:
    print("VALID")
else:
    print("INVALID")
#            
        
            
    
