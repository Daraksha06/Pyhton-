# Write a Python program that manipulates and prints strings using various string methods.
words = "My name is Daraksha "

len_words = len(words)
print(len_words)

words_lower = words.lower()
print(words_lower)

words_upper = words.upper()
print(words_upper)

words_cap = words.capitalize()
print(words_cap)

words_title = words.title()
print(words_title)

words_strip = words.strip()  #Removes spaces from the beginning and end of the string.
print(words_strip)

words_replace = words.replace("s", "k", 2)
print(words_replace)

words_find = words.find("is")
print(words_find)

words_starts = words.startswith("My ")
print(words_starts)

words_ends = words.endswith("a")
print(words_ends)

words_split = words.split(" ") #Split the string into a list based on spaces.
print(words_split)

words_join = " ".join(["Hello"]) #Join the words with a dash
print(words_join)

is_alpha = "words".isalpha()
print(is_alpha)

is_digit = "123".isdigit()
print(is_digit)

words_zfill = "Hello".zfill(10)
print(words_zfill)

words_center = words.center(50, '*')
print(words_center)

words_ljust = words.ljust(50, '*')
print(words_ljust)



