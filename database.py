# -*- coding: utf-8 -*-
"""
Created on Wed May 15 22:17:27 2019

@author: Black_devil
"""

 
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="events")
mycursor= mydb.cursor()

def insert():
    print("Call from insert")
    na =input("Enter the student name:")
    us = input("Enter the student usn:")
    br =input("Enter the branch name ")
    
    sql = "INSERT INTO student (name, usn,branch) VALUES (%s, %s,%s)"
    val = (na,us ,br)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    
    
    
def display():
    #print("call from display")
    mycursor.execute("SELECT * FROM student")
    myresult = mycursor.fetchall()
    print("sl_no\t\t\tName\t\t\tUsn\t\t\tBranch  "   )
    print("<====================================================================================>")
    for x in myresult:
       
        for i in x:
            print (i,end="\t\t\t")
            
        print()

    


s=1
while (s==1):

    c = int(input('''\n\n\n\n\nEnter  your choice 
              
                          1.Insert  
                                            2.Display  
                                                            3.exit
                                                            
                                                            
                                                            
                            =======> '''))
    if c==1:
        insert()
    
    if c==2:
        display()
    
    if c==3:
        s=0
        

    

    
    
