# ===== Q:30-Multiply all numbers in the list ======


# Method 1: Traversal

def multiplyList(myList) :
	
	result = 1
	for x in myList:
		result = result * x
	return result
	
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))

# Method 2: Using numpy.prod()

import numpy

result1 = numpy.prod(list1)
result2 = numpy.prod(list2)
print(result1)
print(result2)

# Method 3 Using lambda function

from functools import reduce

result1 = reduce((lambda x, y: x * y), list1)
result2 = reduce((lambda x, y: x * y), list2)
print(result1)
print(result2)

# Method 4 Using prod function of math library

import math

result1 = math.prod(list1)
result2 = math.prod(list2)
print(result1)
print(result2)
