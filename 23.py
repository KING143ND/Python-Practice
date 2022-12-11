# Q:23-Python program to swap two elements in a list


def swapList(newList):
  size = len(newList)
  
  temp = newList[0]
  newList[0] = newList[size - 2]
  newList[size - 2] = temp
  return newList
  
newList = [23, 65, 19, 90]

print(swapList(newList))