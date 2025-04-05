# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 13:05:46 2025

@author: admin
"""

def check_pal(s):
    a = s[::-1]
    if a == s:
        return True
    else:
        return False

def char_count(txt="hello"):
    lower = upper = space = special = number = 0
    for i in txt:
        if i.isupper():
            upper += 1
        elif(i.islower()):
            lower += 1
        elif(i.isspace()):
            space +=1
        elif(i.isdigit()):
            number +=1
        else:
            special +=1
    
    print(f"This text contains lowerCase : {lower} \nUpperCase :{upper} \nBlankSpace : {space} \nSpecial Char : {special} \nNumbers : {number}")

def count_the(txt='Hellllo the world'):
    a = txt.split()
    c=a.count('the')
    print(f"\nThis text contains {c} 'the' \n")

s = input("Enter a string :")
s1 = input("Enter another string :")
print('----------------------------------------------------------------')
print(f'\nThe length of string {s}',len(s))
print('\n checking palindrome :')
if(check_pal(s)):
    print("The given string is palindrome \n")
else:
    print("Not a palindrome \n")

print(f"Checking two string {s} and {s1} is equal or not ", s == s1 ,"\n")

para = ''' Consider function f(n) the time complexity of an algorithm and g(n) is the most significant term.
If f(n) <= C g(n) for all n >= 1, C > 0, then we can represent f(n) as O(g(n) '''

char_count(para)

count_the(para)                                                                        

print(para.swapcase())
    
    
    
    