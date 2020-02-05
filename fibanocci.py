# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:36:15 2019

@author: User
"""

def fib(x):
    s=0
    n0,n1=0,1
    try:
        
        if x==1:
            print(0)
        elif x==2:
            print(0,1)
        else:
            print(0,1,end=" ")
            for i in range(3,x+1):
                s=n0+n1
                n0=n1
                n1=s
                print(s,end=" ")   
    except:
        print("enter a valid number")
        
fib(int(input("enter the number:")))
