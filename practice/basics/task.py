# calculator
while True:
    print("-------Select-------\n")
    print("-------1) Addition------\n")
    print("-------2) Subtraction------\n")
    print("-------3) Multiplication------\n")
    print("-------4) Division------\n")
    print("-------5) Modulo------\n")
    print("-------6) Exponent------\n")
    print("-------7) Floor Division------\n")
    print("-------Press x to exit\n")
    inp=input("Enter your choice : ")
    if inp=="1" :
        a=int(input("\nEnter 1st operand : "))
        b=int(input("\nEnter 2nd operand : "))
        # print(a,"+",b , "=" , a+b)
        c=a+b
        print(f"{a} + {b} = {c}")
    elif inp=="2" :
        a=int(input("\nEnter 1st operand : "))
        b=int(input("\nEnter 2nd operand : "))
        c=a-b
        print(f"{a} - {b} = {c}")
    elif inp=="3" :
        a=int(input("\nEnter 1st operand : "))
        b=int(input("\nEnter 2nd operand : "))
        c=a*b
        print(f"{a} * {b} = {c}")
    elif inp=="4" :
        a=int(input("\nEnter 1st operand : "))
        b=int(input("\nEnter 2nd operand : "))
        c=a/b
        print(f"{a} / {b} = {c}")
    elif inp=="5" :
        a=int(input("\nEnter 1st operand : "))
        b=int(input("\nEnter 2nd operand : "))
        c=a%b
        print(f"{a} % {b} = {c}")
    elif inp=="6" :
        a=int(input("\nEnter 1st operand : "))
        b=int(input("\nEnter 2nd operand : "))
        c=a**b
        print(f"{a} ^ {b} = {c}")
    elif inp=="7" :
        a=int(input("\nEnter 1st operand : "))
        b=int(input("\nEnter 2nd operand : "))
        c=a//b
        print(f"{a} // {b} = {c}")
    elif inp=="x" or inp=="X" :
       break
    else :
        print("\nEnter the valid choice !!! ")
    
1

        


