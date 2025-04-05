# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 22:49:48 2025

@author: admin
"""

def quadratic_equ(a,b,c):
    d=(b**2)-(4*a*c)
    #print(d)
    if(d>0):
        root1=(-b + d**0.5)/(2*a)
        root2=(-b - d**0.5)/(2*a)
        return(f"The Roots For {a},{b},{c} are :\n root 1 is {root1} \n root 2 is {root2}")
    elif(d<0):
        root1= -b/(2*a)
        return(f"The Roots For {a},{b},{c} are :\n root 1 is {root1} \n")
    else:
        return(f"Invalid inputs are given {a},{b},{c}")
        
a=eval(input("Enter a value for coefficent of square of x : "))
b=eval(input("Enter a value for coefficient of x : "))
c=eval(input("Enter a value for constant : "))
print(quadratic_equ(a, b, c))