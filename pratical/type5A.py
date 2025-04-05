# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 19:38:48 2025

@author: admin
"""

def num_rev():
    num = int(input("Enter the number :"))
    s = 0
    rev =""
    while(num >0):
        r = num % 10
        rev += str(r)
        s += r
        num = num // 10
    
    print("Sum is ",s , "Rev is ",rev)

num_rev()