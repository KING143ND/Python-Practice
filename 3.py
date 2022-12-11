# ============== Q:3-Python Program for factorial of a number ==============


def factorial(n):
     
    return 1 if (n==1 or n==0) else n * factorial(n - 1);

num = int(input("Enter Your Number: "))

print(f"The Factorial of {num} is {factorial(num)}")
