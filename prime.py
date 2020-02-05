# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:38:20 2019

@author: User
"""

def pck(x):
    #f=0
    if x>1:
        f=0
        for i in range(2,x):
            if (x%i)==0:
                f=1
                break
            
            
        else:
            print(x,"is a prime number")
            
        if f==1:
            print(x,"is not a prime number")
                  
        
            
    else:
        print("Enter a valid number: ")
        
pck(int(input("Enter the number :  ")))

