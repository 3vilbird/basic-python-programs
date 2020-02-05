n=int(input("enter the number: "))
#top part
for i in range(0,int(n/2)+1):
	print(" "*(int(n/2)-i)+"*"*(i+1))
space=1
for i in range(int(n/2),1, -1):
	print(" "*space+"*"*i)
	space +=1
print(" "*space+"*"+"@"*n)
#middle part
space=n-2
for i in range(1,int(n/2)+1):
	print(" "*((int(n/2)+1)+(n-1)),end="")
	print("*"*i+" "*space+"*"*i)
	space -=2
print(" "*((int(n/2)+1)+(n-1))+"*"*n)
space=1
for i in range(int(n/2), 0,-1):
	print(" "*((int(n/2)+1)+(n-1))+"*"*i+" "*space+"*"*i)
	space +=2
#last part
print(" "*((int(n/2)+(2*n)-1))+"@"*n+"*")
#last triangle
for i in range(2,int(n/2)+2):
	print(" "*(int(n/2)+int(2*n)+int(n-1))+"*"*i)
for x in range(int(n/2),0,-1):
	print(" "*(int(n/2)+int(2*n)+int(n-1))+"*"*x)

# code by Black_devil......!
#can  be reduced by using functions


