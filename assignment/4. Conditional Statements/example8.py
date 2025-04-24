# Write a Python program to check if a person is eligible to donate blood using a nested if. 

age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
ques=input("If you have any blood or inherent disease??? \t (Write Y for yes  | N for no )")
if ques.upper()=='N':
    if age>18:
        if age< 60:
            if weight>50:
                print("You are eligible to to donate blood  !! ")
            else:
                print("Your weight is insufficient to donate blood ")
        else:
            print("Due to your old age , you cannot donate  ")
    else: 
        print("You are too young to donate the blood !!")
else :
    print("Due to your disease you cant donate blood !! ")