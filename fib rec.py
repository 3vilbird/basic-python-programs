
"""
Created on Wed Feb 20 21:37:18 2019

@author: User
"""

def fib(x):
    if x==1:
        return 0
    elif x==2:
        return 1
    else:
        return fib(x-2)+fib(x-1)
    
    

for i in range(1,(int(input("Enter the value:")))+1):
    print(fib(i),end=" " )
