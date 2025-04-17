t1=0
t2=1
n=10
print(t1,"\n", t2, "\n")
for i in range(3,n+1):
    next=t1+t2
    print(next,"\n")
    t1=t2
    t2=next
