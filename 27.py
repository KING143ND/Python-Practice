# ======== Q:27-Different ways to clear a list in Python =========


# Method 1 : Using clear() method

MY_list = [6, 0, 4, 1]
print('MY_list before clear:', MY_list)

MY_list.clear()
print('MY_list after clear:', MY_list)

# Method 2 : Reinitializing the list 

list1 = [1, 2, 3]
list2 = [5, 6, 7]

print ("List1 before deleting is : "
+ str(list1))

list1.clear()

print ("List1 after clearing using clear() : "
+ str(list1))

print ("List2 before deleting is : "
+ str(list2))

list2 = []

print ("List2 after clearing using reinitialization : "
+ str(list2))

# Method 3 : Using “*= 0” 

list1 = [1, 2, 3]

print ("List1 before deleting is : " + str(list1))

list1 *= 0

print ("List1 after clearing using *= 0: " + str(list1))

# Method 4 : Using del

list1 = [1, 2, 3]
list2 = [5, 6, 7]

print ("List1 before deleting is : " + str(list1))

del list1[:]
print ("List1 after clearing using del : " + str(list1))

print ("List2 before deleting is : " + str(list2))

del list2[:]
print ("List2 after clearing using del : " + str(list2))
