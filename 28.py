# ============= Q:28-Reversing a List in Python ==============


# Reversing a list using insert() function

lst=[10, 11, 12, 13, 14, 15]

l=[]

for i in lst:
    l.insert(0,i)
print(l)

# Using the reversed() built-in function

def Reverse(lst):
	return [i for i in reversed(lst)]
	
print(Reverse(lst))

# Using the reverse() built-in function

def Reverse(lst):
	lst.reverse()
	return lst
	
print(Reverse(lst))

# Using the slicing technique

def Reverse(lst):
	new_lst = lst[::-1]
	return new_lst
	
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))
