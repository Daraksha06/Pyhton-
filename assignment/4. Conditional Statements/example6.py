#  Write a Python program to check if a number is prime using if_else. 

num = int(input("Enter the number : "))
count=0
if num <= 1 :
    print(num , "is not prime ")
else:
    for i in range(2,num+1):
        if num%i==0:
            count+=1
            
    if count>2:
        print(num ,"is not prime ")
    else:
        print(num , "is prime")

