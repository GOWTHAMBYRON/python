# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 00:00:13 2025

@author: admin
"""
from scipy import linalg
import numpy as np

d = np.array([[1,1,1],[6,-4,5],[5,2,2]])
v = np.array([[2],[31],[13]])

a = linalg.solve(d, v)
print("The result of solve :")
for i in a.flat:
    print(round(i), end=' ')
print()
ch = d.dot(a) - v

for i in ch.flat:
    print(round(i), end=' ')
    
a = np.array([[4,-3,0],[2,-1,-2],[1,5,7]])
res = linalg.det(a)
print(f"\nDeterminant of \n{a}\n is :{res}")

