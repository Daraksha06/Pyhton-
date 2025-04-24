# Practical Example 4: How to check the type of a variable dynamically using type()


# Numeric Types
integer_num = 42
float_num = 3.14
complex_num = 2 + 3j

# Sequence Types
string_text = "Hello, Python!"
list_data = [1, 2, 3, "a"]
tuple_data = (1, 2, 3, "b")
range_data = range(5)

# Set Types
set_data = {1, 2, 3}

# Mapping Type
mydict= {"name": "DARAKSHA", "age": 21}

# Boolean
bool_value = True

# None Type
none_value = None

print("Integer:", integer_num, "\t Data Type is : " , type(integer_num))
print("Float:", float_num, "\t Data Type is : " , type(float_num))
print("Complex:", complex_num,"\t Data Type is : " , type(complex_num))
print("String:", string_text,"\t Data Type is : " , type(string_text))
print("List:", list_data,"\t Data Type is : " , type(list_data))
print("Tuple:", tuple_data,"\t Data Type is : " , type(tuple_data))
print("Range:", list(range_data), "\t Data Type is : " , type(range_data))  
print("Set:", set_data,"\t Data Type is : " , type(set_data))
print("Dictionary:", mydict,"\t Data Type is : " , type(mydict))
print("Boolean:", bool_value,"\t Data Type is : " , type(bool_value))
print("None:", none_value,"\t Data Type is : " , type(none_value))

