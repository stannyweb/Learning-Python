# Count how many times an item appears in th tuple.
my_tuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'po')
print(my_tuple)
print(my_tuple.count('apple'))

# Index
print(my_tuple.index('cherry', 1, 3))

# Sorted with key values
sorted_tuple = sorted(my_tuple, key=len, reverse=True)
print(sorted_tuple)
print(sorted_tuple)