# this will creates  a new object to store result

class time:
	def __init__(self, hour,minute,second):
		self.hour=hour
		self.minute=minute
		self.second=second
	def addition(t1,t2):
		su = time(0,0,0)
		su.hour =t1.hour + t2.hour
		su.minute =t1.minute + t2.minute
		su.second = t1.second + t2.second

		while su.second >59:
			su.minute += 1
			su.second -= 60

		while su.minute >59:
			su.hour += 1
			su.minute -= 60
			print('%.2d:%.2d:%.2d' %(su.hour,su.minute,su.second))
		

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
	