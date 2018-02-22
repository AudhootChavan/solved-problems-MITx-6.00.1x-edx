s = input("Enter String:")
k = int(input("Enter key:"))
output = ""
temp = ""

#for using chr function in c, just write %c and pass value 

for i in range(len(s)):
        temp = ord(s[i])
        if temp > 64 and temp < 91:
            temp = (temp + k) % 26
            if temp > 12 and temp < 26:
                temp = temp + 52
                output = output + chr(temp)
            elif temp >= 0 and temp < 13:
                temp = temp + 78
                output = output + chr(temp)
        elif temp > 96 and temp < 123:
            temp = (temp + k) % 26
            if temp >= 19 and temp < 26:
                temp = temp + 78
                output = output + chr(temp)
            elif temp >= 0 and temp < 19:
                temp = temp + 104
                output = output + chr(temp)
        else:
            temp = s[i]
            output = output + temp
            
            
        
print(output)
    
    
