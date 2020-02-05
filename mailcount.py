def mail(s):
	try:
		d=open(s)
		b=dict()
		#c=0
		for line in d:
			line.lower()
			if line.startswith("from"):
				
				#d=line.find("@")
				s=line.find(" ",line.find("@"))
				g=line.find(" ",s+1)
				sun=line[s+1:g]
				if sun not in b :
					b[sun]=1
				else:
					b[sun]=b[sun]+1

		print(b)	
			
			




	except:
		print("file not found")


s=input("Enter the file name")
mail(s)