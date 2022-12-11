#======= Q:15-Python Program for Sum of cubes of first n natural numbers =======


def cubesum(num) :

	sum = 0
	for i in range(1, num+1) :
		sum = sum + (i * i * i)
	return sum

num = int(input("Enter the Number:"))
print(f"The Sum of Cubes of first {num} natural numbers is {cubesum(num)}")
