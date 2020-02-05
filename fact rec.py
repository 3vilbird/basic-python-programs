# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:33:26 2019

@author: User
"""

def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)
    
print("The factorial of given number is:",fact(int(input("Enter the number:"))))
