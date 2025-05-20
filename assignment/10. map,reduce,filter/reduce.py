# Write a Python program that uses reduce() to find the product of a list of numbers. 
from functools import reduce
num= [1,2,3,4,5,6,7,8,9]
def myfunc(x,y):
    return x*y
res= reduce(myfunc,num)
print(res)