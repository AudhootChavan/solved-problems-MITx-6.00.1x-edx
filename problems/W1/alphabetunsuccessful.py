# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 17:59:18 2017

@author: Audhoot
"""


l = []
string = ''

s = input("Enter String:")

for i in range(len(s)-1):
    if s[i+1]>=s[i]:
        string = string + s[i]
    else:
        string = string + s[i]
        l.append(string)
        string = ''
    
if not l:
    print (s)

else:
    print("Longest substring in alphabetical order is:",max(l,key=len))

    
print (l)

