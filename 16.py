#============== Q:16-Python Program to find sum of array =================


def arraysum(arr):
	
	sum=0
	for i in arr:
		sum = sum + i		
	return(sum)

arr=[]
arr = [12, 3, 4, 15]
n = len(arr)

ans = arraysum(arr)

print ('Sum of the array is ', ans)
