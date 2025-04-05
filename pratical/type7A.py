# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 23:27:22 2025

@author: admin
"""

marks = {'sakthi' : 89 ,'vel':90 , 'chiva' : 67 ,'srini':70,'dhanush' : 56}
print(f"keys : {marks.keys()}")
print(f"values : {marks.values()}")

print(f"Minimarks scored :{min(marks, key=marks.get)}")
print(f"Maximarks scored :{max(marks , key=marks.get)}")

items = sorted(marks.items() , key=lambda x: x[1])
for key , values in items:
    print(key , values)

marks['dhanush'] = 99
print(f"The change dict is {marks}")

del marks['sakthi']
print(f"The change dict is {marks}")

print("\nTotal Key-Value Pairs in Dictionary:", len(marks))
