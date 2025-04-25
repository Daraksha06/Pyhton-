#  Write a Python program to find a specific string in the list using a simple for loop and if condition. 
find=input("Enter the string to find  from the list : ")
mylist= ['daraksha', 'liz', 'rose', 'curiousity','humbleness']
print("Our list of string is below: \n" , mylist)
for i in mylist:
    if i==find.lower():
        index=mylist.index(i)
        print(find,"found in the list at index ", index)

