import re
f=open('g.txt')
for line in f:
	line=line.rstrip()
	x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]',line)
	if len(x)>0:
		print(x)