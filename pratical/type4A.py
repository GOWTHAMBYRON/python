# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 19:00:21 2025

@author: admin
"""

def check(s):
    pal = s[::-1]
    if(s == pal):
        print(f"The given {s} is palindrome")
        return pal
    else:
        print(f"The given {s} is not palindrome")
        return pal

def count_char(txt):
    lower = upper = space = special = number = 0
    
    for ch in txt:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower +=1
        elif ch.isspace():
            space +=1
        elif ch.isdigit():
            number +=1
        else:
            special += 1
    
    print(f"The text contains \nUpper :{upper}\nLower :{lower}\nSpace :{space}\nDigits :{number}\nSpecial :{special}\n ")
    

s = input("Enter the string :")
print(f"Length of the {s} is {len(s)}")
another = check(s)
print("the given two str is equal :" , s== another)

s1 = input("Enter a another string :")
print("Counting how many 'the' in the text")

words = s1.split()
print(words.count("the"))

count_char(s1)

print("Toggle the case :" , s1.swapcase())
    