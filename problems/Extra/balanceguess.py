import matplotlib.pyplot as plt


#Lst for number of tries
tries = []
#List for initial balance
xbalance = []

for balance in range(10,10000,10):
    #Calculating upper, lower bound and average
    annualInterestRate = 0.18
    lowerbound = balance/12
    temp = 0
    temp1 = 0
    temp1 = balance
    upperbound = (balance*(1+(annualInterestRate)/12)**12)/12
    number = 0
    xbalance.append(balance)
    avg = (upperbound + lowerbound)/2
    
    for x in range(10000):
        for i in range(12):
            balance = balance - avg
            balance = balance + (balance*(annualInterestRate/12))
            #this line is redundant 
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
            break
    
    #Appending number of guesses for a particular balance to the list
    tries.append(number)
    #Clearing number to restart count
    number = 0 
    

plt.plot(xbalance,tries)
plt.ylabel('Number of Guesses')
plt.xlabel('Initial Balance')
