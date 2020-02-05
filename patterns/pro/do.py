n=int(input())
major=list()

for i in range(0,n):
	n_m_x=major.append(input().split())
	l1=major.append(input().split())
	l2=major.append(input().split())

for i in range(0,n*3,3):
	#print(major[i])
	count=0
	for j in range(0,int(major[i][0])):
		
		for x in range(int(major[i][1])):
			#print(int(major[i+2][2]
			if (int(major[i+1][j])+int(major[i+2][x]))==int(major[i][2]):
				print(major[i+1][j]+","+major[i+2][j],end=" ")
				count +=1
	print()
	if count==0:
		print("noooooo")
	