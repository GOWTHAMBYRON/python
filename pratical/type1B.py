# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 17:14:26 2025

@author: admin
"""

import mysql.connector as sql

mycon = sql.connect(host="localhost", user="root", password="", database="college")

if mycon.is_connected():
    while(True):
        print("\nWelcome to database Program \nChoose a Choice to do operations \nEnter 1 to create table \nEnter 2 to insert the rows \nEnter 3 Update the rows \nEnter 4 to Delete the rows \nEnter 5 to Display the rows \n6 To Exit")
        
        ch = int(input("Enter a choice :"))
        mycur = mycon.cursor()
        
        if(ch == 1):
            qry = "CREATE TABLE IF NOT EXISTS student(snum integer(2) , sname varchar(20) , m1 integer(3) , m2 integer(3) , total integer(3) )"
            
            mycur.execute(qry)
            print("\nTable successfully created ")
            
        elif(ch == 2):
            num = int(input("Enter the rollNo :"))
            name = input("Enter your name :")
            m1 = int(input("Enter your mark for m1 :"))
            m2 = int(input("Enter your mark for m1 :"))
            tot = m1 + m2
            #qry = f"INSERT into student values({num} , '{name}',{m1},{m2},{tot})"
            qry = "INSERT into student values(%s , %s , %s , %s , %s)"
            mycur.execute(qry,[num , name , m1 , m2, tot])
            chk = mycur.rowcount
            mycon.commit()
            if chk > 0:
                print("\nSuccessfully inserted")
            
        elif(ch == 3):
            num = int(input("Enter the roll no to update :"))
            name = input("Enter the updated name :")
            m1 = int(input("Enter the updated m1 mark :"))
            m2 = int(input("Enter the updated m2 mark :"))
            tot = m1 + m2
            qry = f"UPDATE student set sname = %s , m1 = %s , m2 = %s , total = %s where snum = {num}"
            mycur.execute(qry, [name, m1, m2, tot])
            mycon.commit()
            print("\nUpdated Successfully")
            
        elif(ch == 4):
            num = int(input("Enter the roll no to delete :"))
            qry = "Delete from student where snum = %s"
            mycur.execute(qry,(num ,))
            mycon.commit()
            print("\nDeleted successfully")    
        elif(ch == 5):
            mycur.execute("select * from student")
            print("The rows are:")
            rows = mycur.fetchall()
            for i in rows:
                print(i)
               
        elif(ch == 6):
               break
else:
    print("Not connected")