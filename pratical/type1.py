# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 16:41:46 2025

@author: admin
"""
class ZeroError(Exception):
    def __init__(self, num, message = "There integer must be greater than 0"):
        self.num = num
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message} : Provided value is {self.num}"


def arth_log_bitwise(a,b):
    print("Arithmetic operations :")
    print(f"{a} + {b}= {a+b}")
    print(f"{a} - {b}= {a-b}")
    print(f"{a} * {b}= {a*b}")
    print(f"{a} / {b}= {a/b} \n")
    print("Logical operations :")
    print(f"{a}>{b} and {a} < {b} = {(a>b) and (a<b)}")
    print(f"{a}<{b} or {a} > {b} = {(a<b) or (a>b)}")
    print(f"not {a} < {b} = {not(a<b)} \n")
    print("Bitwise operations")
    print(f"{a} & {b} = {a & b}")
    print(f"{a} | {b} = {a | b}")
    print(f"{a} ^ {b} = {a ^ b}")
    print(f"{a} << {b} = {a << b}")
    print(f"{a} >> {b} = {a >> b}")
    print(f"~{b} = {~b}")
 
try:
    a = int(input("Enter a integer value :"))
    b = int(input("Enter a integer value :"))
    if a == 0:
        raise ZeroError(a)
    elif  b == 0:
        raise ZeroError(b)
    else:
        arth_log_bitwise(a, b)
except ZeroError as e :
    print(e.message)
    print(e)
    print(f"But provided :{e.num}")