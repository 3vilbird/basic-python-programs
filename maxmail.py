def mail(s):
	try:
		d=open(s)
		b=dict()
		#c=0
		for line in d:
			line.lower()
			if line.startswith("from"):
				
				#d=line.find("@")
				s=line.find(" ")
				g=line.find(" ",s+2)
				sun=line[s+2:g]
				if sun not in b :
					b[sun]=1
				else:
					b[sun]=b[sun]+1


		d=list(b.values())
		q=list(b.keys())
		r=dict()
		r[ q[d.index(max(d)) ]  ]=max(d)




		print( r)
        
        	




	except:
		print("file not found")


s=input("Enter the file name")


mail(s)