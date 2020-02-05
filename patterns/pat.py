n = int(input(" enter the number:"))

for i in range(n):
	print("@",end="")
	print(" "*(i*(n-1)),end="")
	print("*"*n,end="")
	if i==n-1 :
		print("@",end="")
		#print("@")
	print()
print("@"+" "*((n*(n-1))+1)+"@")
for _ in range(n-1):
	print(" "*((n*(n-1))+1),"@")
