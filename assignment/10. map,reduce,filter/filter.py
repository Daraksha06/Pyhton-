# Write a Python program that filters out even numbers using the filter() function.
num=[1,2,3,44,5,77,8,11,33,4,5,6]
res= list(filter(lambda x: x%2==0,num))
print(res)