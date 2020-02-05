def in_space(s):
	print(" "*s,end="")
def func(n):
	in_space(n)
	print("*"*n+"@"+" "*(n-2)+"@"+"*"*n)
	
def reverse_tri(height,n):
	max_stars=n-2
	space=1
	for i in range(1,height):
		
		in_space(n)
		print(" "*space+"*"*max_stars+" "*(n+space)+(" "*space)+"*"*max_stars)
		max_stars -=2
		space +=1





n = int(input("number:"))
height=int(n/2)+1
space=height-1
min_stars=1
for i in range(0,height):
	in_space(n) # function call to get initial spaces
	in_space(n) # function call to get initial spaces
	
	print(" "*space,end="")
	print("*"*min_stars)
	min_stars +=2
	space -=1
# to print @ in the middle
print()
for i in range(0,n-2):
  	in_space(n)
  	in_space(n)
  	print("@"+" "*(n-2)+"@")

func(n)
reverse_tri(height,n)





