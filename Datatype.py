#Data Types

#1. Demonstrate int, float, str, bool, and complex.

# Integer
a = 10
print("Integer:", a)
print("Type:", type(a))

# Float
b = 10.5
print("Float:", b)
print("Type:", type(b))

# String
c = "Hello Python"
print("String:", c)
print("Type:", type(c))

# Boolean
d = True
print("Boolean:", d)
print("Type:", type(d))

# Complex
e = 3 + 4j
print("Complex:", e)
print("Type:", type(e))


#2. Accept two numbers and display their data types.

num1 = int(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("First number:", num1)
print("Data type:", type(num1))

print("Second number:", num2)
print("Data type:", type(num2))

#3. Convert a string number into an integer and float.

num = "25"

integer_num = int(num)
float_num = float(num)

print("String:", num)
print("Integer:", integer_num)
print("Data type:", type(integer_num))

print("Float:", float_num)
print("Data type:", type(float_num))

#4. Find the length of a string.

# Find the length of a string

text = input("Enter a string: ")

length = len(text)

print("String:", text)
print("Length:", length)

#5. Create a list, tuple, set, and dictionary and display their types.

# Create list, tuple, set, and dictionary

my_list = [10, 20, 30]
my_tuple = (10, 20, 30)
my_set = {10, 20, 30}
my_dict = {"name": "Mahek", "age": 21}

print("List:", my_list)
print("Type:", type(my_list))

print("Tuple:", my_tuple)
print("Type:", type(my_tuple))

print("Set:", my_set)
print("Type:", type(my_set))

print("Dictionary:", my_dict)
print("Type:", type(my_dict))
