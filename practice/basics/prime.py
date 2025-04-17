num=int(input("enter the number "))
flag=0
for i in range(2,num):
    if num%i==0:
        flag=1
        break
if flag==1:
    print(num,"is a not prime number ")
else:
    print(num,"is a prime number")