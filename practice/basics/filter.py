# python code to find the perfect square numbers from a list 
import math
l1=[1,2,3,4,9,5,7,16,77,121]
k=list(filter(lambda num: math.sqrt(num).is_integer(),l1))
print(k)



# wap to find the name from list that starts with a 
l1=["darkasha", "anas", "madiha", "zoya", "nasir"]
k1=filter(lambda a: a[0].lower()=='a' ,l1)
print(list(k1))



# wap to find names starting with same alphabet 
l6= ["darkasha", "anas", "madiha", "zoya", "nasir", "danish", "anaya"]

same_start = list(filter(lambda x: l1.count(x[0]) > 1, l6))
same_start = list(set(same_start))

print(same_start)



# wap to find max number using reduce 
from functools import reduce
l3=[12,2,4,5,6,44]
k3= reduce(lambda x,y: x if x>y else y, l3)
print(k3) 