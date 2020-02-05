# this will modifies the existing object...........

class time:
	def __init__(self, hour,minute,second):
		self.hour=hour
		self.minute=minute
		self.second=second
	def addition(t1,t2):
		
		t1.hour =t1.hour + t2.hour
		t1.minute =t1.minute + t2.minute
		t1.second = t1.second + t2.second

		while t1.second >59:
			t1.minute += 1
			t1.second -= 60

		while t1.minute >59:
			t1.hour += 1
			t1.minute -= 60
		print('%.2d:%.2d:%.2d' %(t1.hour,t1.minute,t1.second))
		
print("enter the hour ,minute and second for 1st object"  )
s =int(input("hour:"))
a =int(input("minute:"))
n =int(input("second:"))
t11 = time(s,a,n)

print("enter the hour ,minute and second for 2nd object"  )
s =int(input("hour:"))
a =int(input("minute:"))
n =int(input("second:"))
t22 = time(s,a,n)
time.addition(t11,t22)
	