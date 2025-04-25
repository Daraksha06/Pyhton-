# 1) Write a Python program to skip 'banana' in a list using the continue  statement. List1 = ['apple', 'banana', 'mango'] 
list1= ['apple', 'banana', 'mango'] 
for i in list1 :
    if i=='banana':
        continue
    print(i)

# 2) Write a Python program to stop the loop once 'banana' is found using the break statement.
print("example 2")
for i in list1 :
    if i=='banana':
        break
    print(i)