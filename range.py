# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:39:29 2019

@author: User
"""


def prim(x,y):

    c=0 
    print("The prime numbers are:")       
    for j in range(x,y+ 1):
               
               if j > 1:
                   for i in range(2,j):
                       if (j % i) == 0:
                           break
                   else:
                       print(j)
                       c+=1
    print("Total prime numbers generated are:",c)
                       
prim((int (input("enter the lower range:"))),(int (input("Enter the upper range:"))))
