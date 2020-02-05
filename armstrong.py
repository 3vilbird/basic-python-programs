# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:40:14 2019

@author: User
"""


def arm(s):
    d=int(s/10)
   
    q=s-(d*10)
   
    r=int(d/10)
   
    e=d-(r*10)
   
    
    if ((q**3)+(r**3)+(e**3))==s:
        return True
    else:
        return False
    
print(arm(int (input("Enter the value:"))))
