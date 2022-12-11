# Q:22-Python program to interchange first and last elements in a list


def swapList(newList):
  size = len(newList)
  
  temp = newList[0]
  newList[0] = newList[size - 1]
  newList[size - 1] = temp
  return newList
  
newList = [12, 35, 9, 56, 24]

print(swapList(newList))
# print(newList[-1])
# print(newList[0])

# ======== Example 2 =========

def swapList(newList):
     
    newList[0], newList[-1] = newList[-1], newList[0]
 
    return newList
     
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

# ======== Example 3 =========

def swapList(list):
  
  get = list[-1], list[0]
  
  list[0], list[-1] = get
  
  return list
  
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

# ======== Example 4 =========

def swapList(list):
  
  start, *middle, end = list
  list = [end, *middle, start]
  
  return list
  
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

# ======== Example 5 =========

def swapList(list):
  
  first = list.pop(0)
  last = list.pop(-1)
  
  list.insert(0, last)
  list.append(first)
  
  return list
  
newList = [12, 35, 9, 56, 24]

print(swapList(newList))
