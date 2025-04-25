# Write a Python program to create a list with elements of multiple data types (integers, strings, floats, etc.). 
mylist=[12.3 ,True , 'daraksha', 23455,None, "hellloooo"]
print(mylist)


# Write a Python program to access elements at different index positions.
for i in range(len(mylist)):
    print(mylist[i], "is element at index " , i)


# 2. Write a Python program to find the length of a list using the len() function
print(len(mylist), "is the length of my list ")


#  3) Write a Python program to update a list using insert() and append(). 
mylist.append('Lizzz')
print(mylist)
# list.insert(index, element)
mylist.insert(5, 'she')
print(mylist)


# 4) Write a Python program to remove elements from a list using pop() and remove().
mylist.pop(5)
print(mylist)
mylist.pop()
print(mylist)
mylist.remove(12.3)
print(mylist)
