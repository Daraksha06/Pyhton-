num=int(input("Enter the number "))
temp=num
count=0
while num!= 0:
    num//=10
    count+=1
print(temp,"is a ",count,"digit number ")
sum=0
num=temp
while temp!=0:
    rem=temp%10
    sum+= pow(rem,count)
    temp//=10
# print(sum)
if sum==num:
    print(num," is an armstrong number ")
else:
    print(num , "is not an armstrong number ")