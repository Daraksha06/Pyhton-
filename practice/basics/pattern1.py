# *****
# ****
# ***
# **
# *
# lines=5
# for i in range(1,lines+1):
#     for j in range(5,i-1,-1):
#         print("*", end="")
#     print()
#     lines+=1

#     *
#    **
#   ***
#  ****
# *****
for i in range(5,1,-1):
    for j in range(5-i):
        print(" ", end="")
    for k in range(i):
        print("*")   
