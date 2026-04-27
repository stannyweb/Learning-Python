
# Upper case
my_upper_str = "..Hello...Magic"
my_upperCase_str = my_upper_str.upper()
print(my_upperCase_str)

# Lower Case
my_LowerCase_str = my_upper_str.lower()
print(my_LowerCase_str)

# Strip
# Left + right strip
my_stripped_str = my_upper_str.strip(".")
print(my_stripped_str)

my_left_stripped_str = my_upper_str.lstrip(".")
print(my_left_stripped_str)

my_right_stripped_str = my_upper_str.rstrip(".")
print(my_right_stripped_str)

# Replaced
my_replaced_str = my_upper_str.replace(".", "_")
print(my_replaced_str)

# Split(separated)
my_split_str = my_upper_str.split(".")
print(len(my_split_str), my_split_str)
print(my_split_str)

# Join 99% for lists
my_list = ["Stan", "Loves", "Maria"]
my_joined_list = "/".join(my_list)
print(my_joined_list)

# Starts with check returns boolean
my_starting_str = "Stan is awesome"
str_starts_with = my_starting_str.startswith("Stan")
print(str_starts_with)

# Ends with
my_ending_str = my_starting_str.endswith("some")
print(my_ending_str)


# find index
my_indexed_str = "Learning is fun"
find_index = my_indexed_str.find("fun", 10, 15)
print(find_index)

# count ( how many times a substring appear in a string)
my_str = "Hello Stanny, Do you love learning Python?"
my_counted_str = my_str.count("l")
print(my_counted_str)

# Title each word first letter capitalized

my_none_cap_str = "this is a regular string"
my_capped_str = my_none_cap_str.title()
print(my_capped_str)