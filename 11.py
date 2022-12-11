#  Q:11-Python Program for How to check if a given number is Fibonacci number? 


num = int(input("Enter Your Number: "))

a = 1
b = 1
c = 0

while(c<num):
	c = a+b
	a=b
	b=c

if(num==c):
	print(f"{num} is Fibonacci Number")	
else:
	print(f"{num} is not Fibonacci Number")	
