# Write a Python program to sort a list using both sort() and sorted(). 

mylist1= [50, 20, 40, 10, 30]

# Sorting the list in place using sort()
mylist1.sort()
print("List sorted using sort():", mylist1)

# Sorting the list without modifying the original list using sorted() ; The original list remains unchanged after using sorted()
mylist2 = [50, 20, 40, 10, 30]
sorted = sorted(mylist2)
print("List sorted using sorted():", sorted)

print("Original list after sorted():", mylist2)


# Examples: 5) Write a Python program to iterate through a list and print each element. 
mylist = [10, 20, 30, 40, 50]
for i in mylist:
    print(i , end="\t")

# Example : 6) Write a Python program to insert elements into an empty list using a for loop and append().
elist=[]
ele=[1,2,3,4,5,6,7]
for i in ele:
    elist.append(i)
print("\nList after adding elements using append():", elist)