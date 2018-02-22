import math 
i = int(input("Enter n for nth fibonacci series:"))
phi = (math.sqrt(5)+1)/2
def fibo(n):
    l = []
    for x in range(n+1):
        l.append(round(((phi)**x - (-phi)**-x)/math.sqrt(5)))
    print(l)
    return 
fibo(i)