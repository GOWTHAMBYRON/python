# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 18:03:46 2025

@author: admin
"""

def check_perfect_number(num):
    lst =[]
    for j in range(1,num +1): 
        summ=0
        for i in range(1,j):
            if (j % i==0):
                summ += i
        if (j == summ):
            lst.append(j)
    
    print(f"The perfect number is {lst}")
        
n=eval(input("Enter a range number: "))
check_perfect_number(n)