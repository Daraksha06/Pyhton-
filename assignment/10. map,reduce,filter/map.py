# Write a Python program to apply the map() function to square a list of numbers. 
num= [1,2,3,4,5,6,7,8,44,3]
def myfunc(x):
    return x*x
res= map(myfunc,num)
print(list(res))