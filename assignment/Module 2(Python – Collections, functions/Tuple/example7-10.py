#  7) Write a Python program to convert a list into a tuple. 
l=[1,2,34234,344,55,"she", True]
tup=tuple(l)
print(tup)


# 8) Write a Python program to create a tuple with multiple data types.
tup1=(1,2,34234,344,55,"she", True,[1,3,4], {"a":1})
print(tup1)


#  9) Write a Python program to  concatenate two tuples into one. 
tup1=(1,2,34234,344,55,"she", True,[1,3,4], {"a":1})
tup2= (2,3,"liz")
res= tup1+tup2
print(res)


# 10) Write a Python program to access the value of the first index in a tuple.
tup1=(1,2,34234,344,55,"she", True,[1,3,4], {"a":1})
print(tup1[0])