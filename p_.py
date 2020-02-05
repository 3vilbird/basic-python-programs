n=list(input())
#print(n)
s=len(n)
#print(s)
flag= 0
for i in range(0,s):

	for j in range(i+1,s):
		
		for k in range(j+1,s):
			
			if (int(n[i])*2 + int(n[j])*2)== int(n[k])*2:

				
				flag=1
				break
if flag==1:
	print ("YES")
else:
	print("NO")