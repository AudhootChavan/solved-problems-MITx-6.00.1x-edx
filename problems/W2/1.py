# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 19:44:52 2017

@author: Audhoot
"""

balance = 2
annualInterestRate = 0.2
monthlyPaymentRate  = 0.04



for i in range(12):
    balance = balance - (balance*monthlyPaymentRate)
    balance = round(balance,2)
    balance = balance + (balance*(annualInterestRate/12))
    balance = round(balance,2)
    
print(balance)