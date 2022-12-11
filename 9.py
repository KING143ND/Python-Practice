# ======= Q:9-Python program to check whether a number is Prime or not =====


num = int(input("Enter Your Number: "))

if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(f"The Number {num} is not Prime")
            break
    else:
        print(f"The Number {num} is Prime")
else:
    print(f"The Number {num} is not Prime")
