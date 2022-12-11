#=== Q:19-Python Program to Split the array and add the first part to the end ====


def splitArr(a, n, k):
    b = a[:k]
    return (a[k::]+b[::])
		
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
position = 2
arr = splitArr(arr, n, position)
for i in range(0, n):
	print(arr[i], end = ' ')
