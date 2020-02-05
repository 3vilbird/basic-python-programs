n = int(input("Enter the number"))
space=0
for x in range(n-1):
	print("@"+" "*space+"*"*n)
	space += (n-1)
print("@"+" "*space+"*"*n+"@")
for x in range(n-1):
	print(" "*(n*(n-1)+2)+"@")
	