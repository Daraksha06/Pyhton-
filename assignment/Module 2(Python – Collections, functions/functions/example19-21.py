#  19) Write a Python program to print a string using a function.
def myfunct():
    x=input("enter a string : ")
    print(x)
myfunct()


# 20) Write a Python program to create a parameterized function that takes two arguments and prints their sum.
def add(x,y):
    print( f" {x+y} is  the sum of {x} and {y}")
add(2,3)


# 21) Write a Python program to create a lambda function with one expression. 
add= lambda x,y : x+y
print(f"{add(5,6)} is the sum . ")
square = lambda x: x * x
print(square(5))  


# 22) Write a Python program to create a lambda function with two expressions.
myfunc = lambda x: (x + 2, x * 3)
print(myfunc(4))  # Output: (6, 12)
