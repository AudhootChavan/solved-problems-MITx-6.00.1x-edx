# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 19:46:41 2017

@author: Audhoot
"""

balance =  3329
temp = 0
temp = balance
annualInterestRate = 0.2



for j in range(10,1000,10):
    for i in range(12):
        balance = balance - j
        print (balance)
        balance = balance + (balance*(annualInterestRate/12))
        
    if balance <= 0:
        print(j)
        break
    else:
        balance = temp
    
