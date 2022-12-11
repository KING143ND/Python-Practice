#=== Q:20-Python Program for Find remainder of array multiplication divided by n ===


from functools import reduce

def find_remainder(arr, n):
	arr_sum = reduce(lambda x, y: x*y, arr)
	remainder = arr_sum % n
	print(remainder)

arr = [100, 10, 5, 25, 35, 14]
n = 11
find_remainder(arr, n)
print(type(arr))
