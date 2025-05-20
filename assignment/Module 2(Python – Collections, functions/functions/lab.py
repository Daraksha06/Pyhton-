# Write a Python program to create a calculator using functions.
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def quotient(x, y):
    return x // y

def rem(x, y):
    return x % y

def exp(x, y):
    return x ** y
print("---- Simple Calculator ----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Quotient (//)")
print("6. Remainder (%)")
print("7. Exponentiation (**)")

choice = input("Enter your choice (1-7): ")
x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))


if choice == '1':
    print("Result:", add(x, y))
elif choice == '2':
    print("Result:", sub(x, y))
elif choice == '3':
    print("Result:", mul(x, y))
elif choice == '4':
    print("Result:", div(x, y))
elif choice == '5':
    print("Result:", quotient(x, y))
elif choice == '6':
    print("Result:", rem(x, y))
elif choice == '7':
    print("Result:", exp(x, y))
else:
    print("Invalid choice")
