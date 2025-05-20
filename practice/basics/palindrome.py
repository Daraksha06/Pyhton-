no=int(input("Enter the number : "))
# 121
num=no
rev=0
while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
if rev==no:
    print("Number is plaindrome ")
else:
    print("Number is not plaindrome ")