balance = 1000
annualInterestRate = 0.18
lowerbound = balance/12
temp = 0
temp1 = balance
number = 0
upperbound = (balance*(1+(annualInterestRate)/12)**12)/12
avg = (upperbound + lowerbound)/2

for x in range(100):
    for i in range(12):
        balance = balance - avg
        balance = balance + (balance*(annualInterestRate/12))
        temp = balance 
    number = number + 1
    
            
    if temp < 0 and balance < -0.01:
        upperbound = avg
        avg = (lowerbound + avg)/2
        temp = 0
        balance = temp1
    elif temp > 0 and  balance > 0.01:
        lowerbound = avg
        avg = (upperbound +avg)/2
        temp = 0
        balance = temp1
    elif  balance <= 0.01:
        avg = round(avg,2)
        print(avg) 
        break
        
print('Number of Guesses:', number)

#  