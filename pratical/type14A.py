# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 20:10:42 2025

@author: admin
"""

class base:
    def get(self):
        self.num1 = eval(input("Enter the number 1 value :"))
        self.num2 = eval(input("Enter the number 2 value :"))
        
    def put(self):
        print(f"The num1 is {self.num1} \nThe num2 is {self.num2}")
    
class child1(base):
    def arithmetic(self):
        self.add = self.num1 + self.num2
        self.sub = self.num1 - self.num2
        self.mul = self.num1 * self.num2
        self.div = self.num1 / self.num2
    
    def put1(self):
        self.get()
        self.arithmetic()
        print(f"Addition is {self.add} \nSubtraction is {self.sub} \nMultiplication is {self.mul} \nDivision is {self.div}")
    
class child2(base):
    def logical(self):
        self.andOper = (self.num1 > self.num2) and (self.num1 < self.num2)
        self.orOper = (self.num1 < self.num2) or (self.num1 > self.num2)
        self.notOper = not(self.num1 > self.num2)
    
    def put2(self):
        print("Values For Logical Operation")
        self.get()
        self.logical()
        print(f"(self.num1 > self.num2) and (self.num1 < self.num2) is {self.andOper} \n(self.num1 < self.num2) or (self.num1 > self.num2) is {self.orOper} \n not(self.num1 > self.num2) is {self.notOper}")
   

obj1 = child1()
obj1.put1()

obj2 = child2()
obj2.put2()