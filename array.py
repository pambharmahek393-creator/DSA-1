#Array

#1. Create and print an array

'''from array import array

numbers = array('i', [10, 20, 30, 40, 50])

print(numbers)

#2. Access elements of an array

from array import array

numbers = array('i', [10, 20, 30, 40, 50])

print(numbers[0])
print(numbers[2])

#3. Add an element to an array

from array import array

numbers = array('i', [10, 20, 30])

numbers.append(40)

print(numbers)

#4. Insert an element

from array import array

numbers = array('i', [10, 20, 30])

numbers.insert(1, 15)

print(numbers)

#5. Remove an element

from array import array

numbers = array('i', [10, 20, 30, 40])

numbers.remove(30)

print(numbers)

#6. Find the length of an array

from array import array

numbers = array('i', [10, 20, 30, 40, 50])

print("Length =", len(numbers))

#7. Find the sum of array elements

from array import array

numbers = array('i', [10, 20, 30, 40, 50])

total = 0

for num in numbers:
    total += num

print("Sum =", total)

#8. Find the largest element

from array import array

numbers = array('i', [10, 50, 20, 40, 30])

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest =", largest)

#9. Reverse an array

from array import array

numbers = array('i', [10, 20, 30, 40, 50])

numbers.reverse()

print(numbers)'''

#10. Search for an element

from array import array

numbers = array('i', [10, 20, 30, 40, 50])

element = 34

if element in numbers:
    print("Element found")
else:
    print("Element not found")





















