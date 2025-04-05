# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 16:12:23 2025

@author: admin
"""

class base1:
    def get1(self):
        self.num1 = int(input("Enter the num1 value :"))
    
    def put1(self):
        print(f"The value of num1 is {self.num1}")

class base2:
    def get2(self):
        self.num2 = int(input("Enter the num2 value :"))
    
    def put2(self):
        print(f"The value of num1 is {self.num2}")
        
class child(base1, base2):
    def arthmetic(self):
        print(f"Addition of {self.num1} AND {self.num2} is {self.num1 + self.num2}")
        print(f"Subtraction of {self.num1} AND {self.num2} is {self.num1 - self.num2}")
        print(f"Multiplication of {self.num1} AND {self.num2} is {self.num1 * self.num2}")
        print(f"Division of {self.num1} AND {self.num2} is {self.num1 / self.num2}")
    
    def find_lar(self):
        self.res = self.num1 if(self.num1 > self.num2) else self.num2
        print(f"Largest of {self.num1} AND {self.num2} is {self.res}")
    
    def put3(self):
        self.get1()
        self.get2()
        self.put1()
        self.put2()
        print("Arithmetic operations :")
        print('---------------------------------------------')
        self.arthmetic()
        print("Largest Number ")
        print('---------------------------------------------')
        self.find_lar()

obj = child()
obj.put3()