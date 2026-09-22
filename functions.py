#Functions

#1.Write a function to print "Hello, World!".

def hello():
    print("Hello, World!")

hello()

#2.Write a function that takes a name and prints a greeting.

def greet(name):
    print("Hello,", name)

greet("Rahul")

#3.Write a function to add two numbers.

def add(a, b):
    return a + b

result = add(10, 20)
print("Sum =", result)

#4.Write a function to find the square of a number.

def square(n):
    return n * n

result = square(5)
print("Square =", result)

#5.Write a function to check whether a number is even or odd.

def check_even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd(8)

#6.Write a function to find the maximum of two numbers.

def maximum(a, b):
    if a > b:
        return a
    else:
        return b

result = maximum(10, 30)
print("Maximum =", result)

#7.Write a function to convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

result = celsius_to_fahrenheit(25)
print("Fahrenheit =", result)

#8.Write a function to calculate the area of a circle.

def area_of_circle(radius):
    return 3.14 * radius * radius

result = area_of_circle(5)
print("Area of circle =", result)

#9.Write a function to calculate the factorial of a number.

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

num = 5
print("Factorial =", factorial(num))

#10.Write a function to check whether a number is positive, negative, or zero.

def check_number(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

check_number(5)

#11.Write a function to find the maximum of three numbers.

def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(maximum(10, 25, 45))

#12.Write a function to count vowels in a string.

def count_vowels(text):
    count = 0

    for char in text:
        if char.lower() in "aeiou":
            count += 1

    return count

print(count_vowels("Hello World"))

#13.Write a function to reverse a string.

def reverse_string(text):
    return text[::-1]

print(reverse_string("Mahek"))

#14.Write a function to check whether a string is a palindrome.

def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

print(is_palindrome("madam"))

#15.Write a function to find the sum of all elements in a list.

def sum_list(numbers):
    total = 0

    for num in numbers:
        total += num

    return total

numbers = [10, 20, 30, 40, 50]
print(sum_list(numbers))

#16.Write a function to find the largest element in a list.

def largest_element(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

numbers = [10, 25, 15, 40, 30]
print(largest_element(numbers))

#17.Write a function to remove duplicate elements from a list.

def remove_duplicates(numbers):
    result = []

    for num in numbers:
        if num not in result:
            result.append(num)

    return result

numbers = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(numbers))

#18.Write a function to count how many times an element appears in a list.

def count_element(numbers, element):
    count = 0

    for num in numbers:
        if num == element:
            count += 1

    return count

numbers = [1, 2, 2, 3, 2, 2, 4, 5]
print(count_element(numbers, 2))

#19.Write a function to check whether a number is prime.

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

num = 8

if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")

#20.Write a function to return all prime numbers between two numbers.

def prime_numbers(start, end):
    primes = []

    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)

    return primes

print(prime_numbers(10, 30))

#21.Write a function to calculate Fibonacci numbers.

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)

#22.Write a function to find the second-largest number in a list.

def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()

    return unique_numbers[-2]

numbers = [10, 20, 5, 40, 30]
print("Second largest =", second_largest(numbers))

#23.Write a function to sort a list without using sort().

def sort_list(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers

numbers = [5, 2, 8, 1, 3]
print(sort_list(numbers))

#24.Write a function to merge two lists and remove duplicates.

def merge_lists(list1, list2):
    result = []

    for item in list1 + list2:
        if item not in result:
            result.append(item)

    return result

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print(merge_lists(list1, list2))





