# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 16:24:55 2025

@author: admin
"""
class empbase:
    def get1(self):
        self.Enum = int(input("Enter the Enum value :"))
        self.ename = input("Enter the name :")
        self.basic = eval(input("Enter the basic pay :"))
    
    def put1(self):
        print(f"The value of Enum is {self.Enum}")
        print(f"The value of Name is {self.ename}")
        print(f"The value of Basic pay is {self.basic}")

class empchild1(empbase):
    def get2(self):
        self.ded = eval(input("Enter the Deduction Amount :"))
        self.allowance = eval(input("Enter the allowance Amount :"))
    
    def put2(self):
        print(f"The value of Deduction is {self.ded}")
        print(f"The value of Allowance is {self.allowance}")
        
class empchild2(empchild1):
   def get3(self):
       self.gross = self.basic + self.allowance
       self.net = self.gross - self.ded      


   def put3(self):
       print(f"The value of gross salary is {self.gross}")
       print(f"The value of net is {self.net}")
       
   def display(self):
        
        self.get1()
        self.get2()
        self.get3()
        print("\nDetails")
        print('--------------------------------')
        self.put1()
        self.put2()
        self.put3()
        print('--------------------------------')
        

obj = empchild2()
obj.display()