#  Write a Python program to calculate grades based on percentage using if-else ladder. 


percentage = float(input("Enter your percentage: "))


if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
else:
    print("Grade: E")
