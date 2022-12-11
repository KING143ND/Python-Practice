#========= Q:17-Python Program to find largest element in an array ==========


def largestElement(arr, num):
    max = arr[0]
    
    for i in range(1, num):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [-34, -45, -57, -67, -99, -88, -13, -18, -34, 13, 4, 11, 8]
num = len(arr)
ans = largestElement(arr, num)
print(f"Largest Element in given Array: {ans}")
