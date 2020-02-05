n= int(input())
for i in range(n+1):
	print(" "*(n-i+1),end=" ")
	for j in range(i,0,-1):
		print(j,end="")
	for s in range(0,i+1):
		print(s,end="")
	print()
