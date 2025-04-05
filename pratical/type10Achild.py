# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 16:58:58 2025

lst = list(map(int, input("Enter the numbers : ").split()))

@author: admin
"""
import type10AModule as m 

try:
    lst =[]
    for i in range(int(input("Enter the number of element :"))):
        lst.append(eval(input("Enter element :")))
    
    print("The sum of list is :" , m.findsum(lst))
    print("The minimum of list is :" , m.findmin(lst))
    print("The maximum of list is :" , m.findmax(lst))
    print("The Average of list is :" , m.findavg(lst))

except Exception as e:
    print(e)
    
    