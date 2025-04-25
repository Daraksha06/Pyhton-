#  1) Write a Python program to print "Hello" using a string.
str="hello"
print(str)

#  2) Write a Python program to allocate a string to a variable and print it. 
msg="hello i am pursuing btech !!!"
print(msg)

#  3) Write a Python program to print a string using triple quotes. 
print('''
Hello this is illustartion of string in double quotes.
      It will print the output as how exactly it is typed inside triple quotes considering spaces too .
    hope that you understand.....
''')

# 4) Write a Python program to access the first character of a string using index value.
mystr="daraksha"
print(mystr[0], "is the first character of " , mystr)

#  5) Write a Python program to access the string from the second position onwards using slicing. 
mystr1="liz is cool"
print(mystr1[1:] , "is the string from 2nd posn onwards ")


# 6) Write a Python program to access a string up to the fifth character. 

print(mystr1[:5])


#  7) Write a Python program to print the substring between index values 1 and 4.
print(mystr1[1:5], "is the string between index values 1 to 4 ")

#  8) Write a Python program to print a string from the last character. 

print(mystr1[: : -1])

# 9) Write a Python program to print every alternate character from the string starting from index 1. 

print(mystr1[1::2])