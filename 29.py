# ==== Q:29-Python program to find sum of elements in list =======


total = 0

list1 = [11, 5, 17, 18, 23]

for i in range(0, len(list1)):
	total = total + list1[i]

print(f"Sum of all elements in given list: {total}")

# Example 2 : Using while() loop 

total = 0
i = 0

while(i < len(list1)):
	total = total + list1[i]
	i += 1
	
print(f"Sum of all elements in given list: {total}")

# Example 3: Recursive way 

def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)
	        
total = sumOfList(list1, len(list1))

print(f"Sum of all elements in given list: {total}")

# Example 4: Using sum() method 

total = sum(list1)

print(f"Sum of all elements in given list: {total}")

# Example 5: Using add() function of operator module

from operator import*

result = 0

for i in list1:
	result = add(i, 0)+result

print(f"Sum of all elements in given list: {result}")
