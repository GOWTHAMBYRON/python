# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 13:28:32 2025

@author: admin
"""

def prime(n):
    for i in range(1,n+1):
        if i < 2:
            print(f"The number {i} is not a prime number")
            continue
        
        flag = 0
        for j in range(2,i):
            if i % j == 0:
                flag =1
                break
            
        if(flag == 1):
            print(f"The number {i} is not a prime number")
        else:
            print(f'The number {i} is a prime number')
        
try:
    
    n = int(input("Enter a number :"))
    
    prime(n)
except ValueError :
    print("The value of n must be integer but provided another datatype")