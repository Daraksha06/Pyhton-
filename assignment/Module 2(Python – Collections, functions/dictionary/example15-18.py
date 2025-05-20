#  15) Write a Python program to update a value at a particular key in a dictionary. 
mydict={"name" : "daraksha" , 
        "age" : 20,
        "gender" : "female"
         }
print(mydict)
mydict.update({"name" : "liz"})
mydict['age']= 20
print(mydict)
# or 
mydict = {"name": "daraksha", "age": 20, "gender": "female"}

keys = list(mydict.keys())
values = list(mydict.values())

print("Keys:", keys)
print("Values:", values)


# 16) Write a Python program to separate keys and values from a dictionary using keys() and values() methods.
mydict={"name" : "daraksha" , 
        "age" : 20,
        "gender" : "female"
         }
keylist=[]
vallist=[]
for key,val in mydict.items():
    keylist.append(key)
    vallist.append(val)
print(keylist)
print(vallist)



# 17) Write a Python program to convert two lists into one  dictionary using a for loop.
l1=['name', 'age', 'gender']
l2=['daraksha', 20, 'female']
dict={}
for i in range(len(l1)):
    dict[l1[i]] = l2[i]
print(dict , "is my new dictionary from 2 lists ")


#  18) Write a Python program to count how many times each  character appears in a string. 
mystr= input("enter the string : ")
for ch in set(mystr):
    print(f" {ch}  appears {mystr.count(ch)} times")

# or
mydict={}
for i in mystr:
    if i in mydict:
        mydict[i]= mydict[i]+1
    else:
           mydict[i]= 1

for key,val in mydict.items():
     print(key, "appears" , val, "times") 