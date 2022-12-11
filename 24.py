# Q:24-Python program to remove Nth occurrence of the given word


def RemoveWord(list1, word, N):
  newList = []
  count = 0

  for i in list1:
    if(i == word):
      count = count + 1
      if(count != N):
        newList.append(i)
    else:
      newList.append(i)
      
  list1 = newList
  
  if count == 0:
    print("Item not found")
  else:
    print(f"Updated list is: {list1}")
  
  return newList

list = ["one", "two", "one", "three"]
word = "one"
N = 2

RemoveWord(list, word, N)
