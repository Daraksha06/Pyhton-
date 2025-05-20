i=1
j=1
for i in range(0,3):
    for k in range(0,4-i,-2):
        print(" " , end="")
    for j in range(0,i+1):
        print(" *", end="")
    print("\n")
i=2
j=2
for i in range(2,0,-1):
    for j in range(i,0,-1):
        print(" *", end="")
    print("\n")




# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1


# 1  
# 0 1 
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1