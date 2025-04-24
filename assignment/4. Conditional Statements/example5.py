# Write a Python program to find greater and less than a number using if_else. 
a= int(input("Enter the number 1 : "))
b=int(input("Enter the number 2 : "))
if a>b:
    print(a,"is greater than ",b)
elif a<b :
    print(a, "is less than ",b)
else:
    print(a , "and" , b ,"are equal ")