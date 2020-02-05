# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:32:24 2019

@author: User
"""

def fact(x):
    if x==0 or x==1 :
        return 1
    else:
        fac=1
        for i in range(1,x+1):
            fac *=i
            
        
        return fac
    
print("Factorial of given number is :",fact(int(input("Enter the number:"))))
