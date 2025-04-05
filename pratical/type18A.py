# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 12:30:46 2025

@author: admin
"""

file = open('Inventory' , 'w+')

file.write("The products are :\n")

for i in range(5):
    print(f"Enter the product details for {i+1}")
    pnum = input("Enter the product number :")
    pname = input("Enter the product name :")
    unit_price = float(input("Enter Unit Price: "))
    quantity = int(input("Enter Quantity: "))
    amount = unit_price * quantity
    
    file.write(f"pnum :{pnum}\npname : {pname}\nunit_price :{unit_price}\nquantity : {quantity}\nAmount :{amount}\n")

print("File is written successfully")
file.close()

file = open("Inventory" ,'r+')
contents = file.read()
print('\nFile data are')
print('\n-------------------------------------------------------')
print(contents)
print('\n-------------------------------------------------------')
print('\n the file contents is successfully retrived')
file.close()
