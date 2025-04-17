# find 3 digit and 4 digit armstrong numbers 
for i in range(100,10000):
        count=0
        temp=i
        while i!= 0:
            i//=10
            count+=1
        sum=0
        i=temp
        while temp!=0:
            rem=temp%10
            sum+= pow(rem,count)
            temp//=10
        if sum==i:
             if count==3:
                   print(i," is a 3 digit armstrong number ")
             elif count==4:
                   print(i," is a 4 digit armstrong number ")
               
 
        