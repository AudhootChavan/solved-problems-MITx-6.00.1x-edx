# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 04:15:36 2017

@author: Audhoot
"""

s = input("Enter string:")
x = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        x = x + 1
        
print ("The number of times 'bob occurs is:", x)
    