# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 19:22:46 2025

@author: admin
"""

class base1:
    def get1(self):
        self.snum = int(input("Enter the number :"))
        self.sname = input("Enter the name :")
    
    def put1(self):
        print(f"snum = {self.snum} \n sname = {self.sname}")
    
class base2(base1):
    def get2(self):
        self.mark1 =int(input("Enter the mark 1:"))
        self.mark2 = int(input("Enter the mark 2 :"))
    def put2(self):
        print(f"mark1 = {self.mark1} \n mark2 = {self.mark2}")
        
class base3:
    def get3(self):
        self.score =int(input("Enter the score :"))
    def put3(self):
        print(f"score = {self.score} ")

class child(base2, base3):
    def put4(self):
        self.get1()
        base2.get2(self)
        base3.get3(self)
        self.total = self.mark1 + self.mark2
        self.put1()
        self.put2()
        base3.put3(self)
        print(f"The total is {self.total}")
    

s1 = child()
s1.put4()
