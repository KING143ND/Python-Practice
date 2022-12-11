# ======= Q:8-Python program to print all Prime numbers in an Interval ======


def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

starting_range = int(input("Enter First Number: "))
ending_range = int(input("Enter Second Number: "))

list1 = prime(starting_range, ending_range)

if len(list1) == 0:
    print("There are No Prime Numbers in this Range")
else:
    print(f"The Prime Numbers in this Range are: {list1}")
