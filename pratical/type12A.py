# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 19:25:54 2025

@author: admin
"""

class empbase:
    def get(self):
        self.enum = int(input("Enter your rollno :"))
        self.ename = input("Enter your name :")
        self.basic = int(input("Enter your basic salary :"))
    
    def put(self):
        print(f"roll No :{self.enum} \nName : {self.ename} \nBasic Salary : {self.basic}\n")
        

class empchild(empbase):
    def get1(self):
        self.ded = eval(input("Enter the Deduction Amount :"))
        self.allowance = eval(input("Enter the allowance Amount :"))
        self.gross = self.basic + self.allowance
        self.net = self.gross - self.ded      
    
    def put2(self):
        print(f"The value of Deduction is {self.ded}")
        print(f"The value of Allowance is {self.allowance}")
        print(f"The value of gross salary is {self.gross}")
        print(f"The value of net is {self.net}")
    
    def display(self):
        self.get()
        self.get1()
        print("Details of Employee :")
        print("------------------------")
        self.put()
        self.put2()
        print("------------------------")

ch = empchild()
ch.display()