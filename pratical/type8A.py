# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 16:04:50 2025

@author: admin
"""


T = ("blue", "red", "black", "green", "brown")


try:
    T[1] = "yellow"  
except TypeError as e:
    print("Tuples are immutable! Error:", e)


print("Individual elements of tuple T:")
for color in T:
    print(color)
    
l1 =[]
l2 = []
for i in T:
    if i.startswith('b') :
        l1.append(i)
    else:
        l2.append(i)

T1 = tuple(l1)
T2 = tuple(l2)

print("\nTuple T1 (colors starting with 'b'):", T1)
print("Tuple T2 (other colors):", T2)


print("Is 'orange' in T?", "orange" in T)


chk_duplicate = ("blue", "red", "blue", "green", "red")
print("Tuple with duplicates:", chk_duplicate)
