# f=open("Test.txt",'w')
# f.write("Daraksha , hello")
# f.close()
f1 = open("Test.txt", 'r')
d = f1.readlines()
print(d)
f1.close()
# for i in d:
#     if d[i] == 't':
#          print(d[i]) 