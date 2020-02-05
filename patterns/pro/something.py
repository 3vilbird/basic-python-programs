n= int(input("Enter the number"))
space=n #total spaces 
for k in range(0,n+1):
	print("  "*space,end="") #spaces 
	space =space-1 #decrease  space by one count
	for i in  range(1,k+1):  #for left triangle which is increamenting
		print(i,end=" ")
	for g in range(k-1,0,-1 ): #this is for the right triangle which  is decreamenting  
		print(g,end=" ")
	print()
#time to code the lower part lol..................:)
space=1
for i in range(n-1,0,-1):
	print("  "*space,end="")
	space +=1
	for j in range(1,i+1):
		print(j,end=" ")
		
	for c in range(i-1,0,-1):

		print(c,end=" ")
	print()
