# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 17:54:56 2017

@author: Audhoot
"""

s = input("Enter string:")
x = 0

for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        x = x + 1
        
print (x)
        