# Print this pattern using nested for loop:  
# * 
# ** 
# *** 
# **** 
# ***** 
for i in range(6):
    print("*"*i)
# another way:
for i in range(6):
    for j in range (i):
        print("*" ,end="")
    print()