#======= Q:14-Python Program for Sum of squares of first n natural numbers =======


def squaresum(num) :

	sum = 0
	for i in range(1, num+1) :
		sum = sum + (i * i)
	return sum

num = int(input("Enter the Number:"))
print(f"The Sum of Squares of first {num} natural numbers is {squaresum(num)}")
