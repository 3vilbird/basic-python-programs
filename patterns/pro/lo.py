n=int(input(" enter the size:"))
s=0
for _ in range(0,n):
	d=float(input("value:"))
	if int(d)==d and int(d)>0:
		s+=int(d)
print(s)
	