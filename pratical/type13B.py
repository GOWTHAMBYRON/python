# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 20:07:43 2025

@author: admin
"""

class Employee:
    
    company_name = "Tech Corp"
    
    def __init__(self, name, salary):
        """Constructor: Initializes object variables"""
        self.name = name  
        self.salary = salary  
        print(f"Employee {self.name} is created.")
    
    def display_info(self):
        """Member function: Displays employee details"""
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company_name}")

    def __del__(self):
        """Destructor: Called when an object is deleted"""
        print(f"Employee {self.name} is deleted.")

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)


emp1.display_info()
emp2.display_info()


print(f"Company Name: {Employee.company_name}")


del emp1
