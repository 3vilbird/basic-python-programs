'''
array A ,and sum K ,find is there any pair, whose sum is equal to K
with time complexity O(n) 
'''

def code_it(a,pair_sum):
	s=list()
	for i in a:
		lol=pair_sum-int(i)
		
		if ( lol in s):
			return "YES"
		else:
			s.append(int(i))
	#rint(s)
	return "NO"



n=input(" Enter the array:").split()
k=int(input("enter the k value:"))
print(code_it(n,k))

