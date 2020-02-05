# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:23:29 2019

@author: User
"""

def s(x):
    try:
        if x>0:
            return (x*(x+1))/2 
        
    except:
        print("Enter a valid number")
        
print("the sum of given number is:",s(int(input("Enter the number:"))))

