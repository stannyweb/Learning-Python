# If you want an empty SET you gotta write set() not just empty {}, cause Python will think that this is a dictionary

my_set = {1, 2, 3, 4, 5}

my_set.add(6)
print(my_set)

# If you want to remove or discard - Diff = Discard will NOT throw an error if the element is not present.
# if you use remove, it will throw error if the element is not present

my_set.discard(7)
# my_set.remove(7)

# clear removes all elements from the set
my_new_set = {2, 5, 6, 9}
my_new_set.clear()
print(my_new_set)

#The .issubset() and the .issuperset() methods check if a set is a subset or superset of another set, respectively.
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set)) # False
print(my_set.issuperset(your_set)) # False

# The .isdisjoint() method checks if two sets are disjoint, which means they don't have any elements in common.
# In this case, that's False because my_set and your_set do have common elements – 2, 3, and 4

# The union operator | returns a new set with all the elements from both sets:
print(my_set | your_set)

# The intersection operator & returns a new set with only the elements that the sets have in common:
print(my_set & your_set)

# The difference operator - returns a new set with the elements of the first set that are not in the other sets.
# In this example, the numbers 1 and 5 are in my_set but NOT in your_set:
print(my_set - your_set)

# The symmetric difference operator ^ returns a new set with the elements that are either in the first or the second set, but not both. In this case, 1 and 5 are in my_set but not in your_set, so they are included. And the number 6 is in your_set but not in my_set, so it's included as well:
print(my_set ^ your_set)

# Each one of these operators also has its corresponding compound assignment operator if you add the equal sign next to it. These operators automatically assign the resulting set to the first set in the expression:
print('|= &= -= ^=')

# For example, the -= operator finds the difference between the sets and updates the first set with that result:
my_set -= your_set
print(my_set)

# You can check if an element is in a set or not with the in operator. Here, we are checking if 5 is in my_set. The result will be a boolean value True or False:
print(5 in my_set)