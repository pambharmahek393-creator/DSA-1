#Operators

#1. Perform addition, subtraction, multiplication, and division.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#2. Find the remainder and quotient of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

remainder = a % b
quotient = a // b

print("Remainder:", remainder)
print("Quotient:", quotient)

#3. Check whether a number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

#4. Compare two numbers using relational operators.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

#5. Demonstrate logical operators (and, or, not).

# Demonstrate logical operators

a = 10
b = 5

print("a > 5 and b < 10:", a > 5 and b < 10)
print("a > 15 or b < 10:", a > 15 or b < 10)
print("not(a > b):", not(a < b))

#6. Demonstrate assignment operators (+=, -=, *=, /=).

# Demonstrate assignment operators

a = 10

a += 5
print("After += :", a)

a -= 3
print("After -= :", a)

a *= 2
print("After *= :", a)

a /= 4
print("After /= :", a)

#7. Find the largest of two numbers using comparison operators.

# Find the largest of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number:", a)
elif b > a:
    print("Largest number:", b)
else:
    print("Both numbers are equal")
