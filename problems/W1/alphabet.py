# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 18:55:21 2017

@author: Audhoot
"""
s = input("Enter a string:")

t = ""
l = []

for i in s:
    if t == "":
        t = t + i
    else:
        if i >= t[-1]:
            t = t + i
            if i == s[-1]:
                l.append(t)
        else:
            l.append(t)
            t = ""
            t = t + i
            

print("Longest substring in alphabetical order is:", max(l, key = len))


