# ==== Q:26-Check if element exists in list in Python ===


my_list = [ 1, 6, 3, 5, 3, 42, 4 ]

print("Checking if 4 exists in list ( using loop ) : ")

for i in my_list:
	if(i == 4):
		print ("Element Exists")
print("Checking if 4 exists in list ( using in ) : ")

if (4 in my_list):
	print ("Element Exists")
else:
    print("Element Does not Exist")
    

#  =========== Example 2 ==========

from bisect import bisect_left ,bisect

test_list_set = [ 1, 6, 3, 5, 3, 4 ]
test_list_bisect = [ 1, 6, 3, 5, 3, 4 ]

print("Checking if 4 exists in list ( using set() + in) : ")

test_list_set = set(test_list_set)
if 4 in test_list_set :
	print ("Element Exists")

print("Checking if 4 exists in list ( using sort() + bisect_left() ) : ")

test_list_bisect.sort()
if bisect_left(test_list_bisect, 4)!=bisect(test_list_bisect, 4):
	print ("Element Exists")
else:
	print("Element doesnt exist")
