s=input()
sa=list(s)
s=set(s)
flag=0
count=0
for i in s:
	co=sa.count(i)
	if co%2 !=0:
		count +=1
		if count >1:
			flag=1
			break
if flag==1:
	print("No")
else:
	print("Yes")


