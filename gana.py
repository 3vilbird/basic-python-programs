'''s=input("Enter the string:")

for x in range(0,len(s)):
	print(s[:x])
for i in range(len(s),0,-1):
	print(s[:i])
'''
array=[5,0,5,7,9,5,3]
gana=list()
k=10
for i in range(0,len(array)-1):
	
	for j in range(i+1,len(array)):
		
		
		if ((array[i]+array[j])%k)==0 and (array[i],array[j]) not in gana :
			gana.append((array[i],array[j]))
print(gana)

	