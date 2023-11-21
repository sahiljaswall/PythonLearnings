# Day 1: Lists and Arrays

# Task 1: Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Task 2: Access and print elements from the list
print("Original list:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Task 3: Add an element to the end of the list
numbers.append(6)
print("List after appending 6:", numbers)

# Task 4: Remove an element from the list
numbers.remove(3)
print("List after removing 3:", numbers)

# Task 5: Iterate through the list and double each element
doubled_numbers = [x * 2 for x in numbers]
print("Doubled numbers:", doubled_numbers)
