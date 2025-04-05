# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 18:26:18 2025

@author: admin
"""
def divisible_checker(lst):
    l1 = []
    l2 =[]
    for i in lst:
        if i % 3 == 0:
            l1.append(i)
        else:
            l2.append(i)
            
    return l1 , l2
print("List Operations :")

mylist = [42,23,542,34,4,21]
print("Type of Mylist :",type(mylist))
# for i in range(10):
#     mylist.append(int(input("Enter the integer to add in the list :")))

mylist.sort()
print("sort in ascending order :",mylist)
mylist.sort(reverse=True)
print("sort in descending order :",mylist)

l1 , l2 = divisible_checker(mylist)
print(f"The List divisible by 3 : {l1}\n The List not divisible by 3 {l2}")

mx = max(l1)
if mx in l1 :
    l1.remove(mx)

mi = min(l2)
if mi in l2:
    l2.remove(mi)
    
print(f"The List L1 has : {l1} and the removed value is {mx}\n The List L2 has :{l2} and the removed value is {mi}")


