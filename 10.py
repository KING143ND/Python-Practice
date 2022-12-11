# =========== Q:10-Python Program for n-th Fibonacci number ==========


def Fibonacci(num):
	if num<= 0:
		print("Incorrect Input")
	elif num == 1:
		return 0
	elif num == 2:
		return 1
	else:
		return Fibonacci(num-1)+Fibonacci(num-2)

num = int(input("Enter Your Number: "))
print(f"The {num}th term of Fibonacci Series is {Fibonacci(num)}")
