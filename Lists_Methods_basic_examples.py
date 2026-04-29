# Append adds to the end of the list
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

even_numbers = [2, 4, 6]
numbers.append(even_numbers)

print(numbers)
del numbers[6]

# Extends adds multiple items to the end of the list
numbers.extend(even_numbers)
print(numbers)

# Insert add items at a specific index of your choice.
add_number = 10
numbers.insert(4, add_number)
print(numbers)

# Remove an item, but only the first occurrence.
numbers.remove(10)
print(numbers)

# Pop, removes an item at a specific index, if you don't specify an index it removes the last element
numbers.pop(5)
numbers.pop()
print(numbers)

# Clear a list
new_numbers = numbers.copy()
new_numbers.clear()
print(new_numbers)

# Sort and Sorted - sort mutate the original list - sorted does not do it, it creates a new list.
numbers_to_sort = [2, 6, 1, 3, 10, 25, 11, 36]

new_sorted_numbers = sorted(numbers_to_sort)
print(new_sorted_numbers)
print(numbers_to_sort)
numbers_to_sort.sort()
print(numbers_to_sort)


# Index finds the index of a item
print(numbers_to_sort.index(10))
