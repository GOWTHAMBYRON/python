# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 11:53:49 2025

@author: admin
"""

def divisible_by_3(mylist):
    for i in mylist:
        if i%3 == 0:
            l1.append(i)
        else:
            l2.append(i)

mylist =[11, 2, 31, 23, 12, 8, 9, 13, 5, 37]
for i in range(10):
    mylist.append(int(input(f"Enter {i} number in the list :")))
    
print("The full List :" , mylist)

mylist.sort()
print("Ascending order :" , mylist)
mylist.sort(reverse=True)
print("Descending order :" , mylist)

l1 = []
l2 =[]

divisible_by_3(mylist)
print(f"Divisible by 3 :{l1}")
print(f"Not Divisible by 3 :{l2}")

l1.remove(max(l1))
l2.remove(min(l2))
print("After removing biggest number from L1 :",l1)
print("After removing smallest number from L2 :",l2)
