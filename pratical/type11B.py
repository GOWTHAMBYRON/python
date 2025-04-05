# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 19:24:01 2025

@author: admin
"""

class Sample:
    def __init__(self, var):
        self.var = var

    
    def __sub__(self, other):
        return self.var - other.var

    def __mul__(self, other):
        return self.var * other.var

   
    def __lt__(self, other):
        return self.var < other.var

    def __gt__(self, other):
        return self.var > other.var

    def __eq__(self, other):
        return self.var == other.var

    
    def __and__(self, other):
        return self.var & other.var

    def __or__(self, other):
        return self.var | other.var

    # Display method for easy output
    def __str__(self):
        return str(self.var)



a = Sample(10)
b = Sample(5)


print("Subtraction:", a - b)  
print("Multiplication:", a * b)  

# Logical operations
print("a < b:", a < b)  
print("a > b:", a > b) 
print("a == b:", a == b)  

# Bitwise operations
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b) 
