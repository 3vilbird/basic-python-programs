st=input()
ss=list(set(st))
count=0
for i in ss:
	c=st.count(i)
	if c>count:
		count=c
print(count)

