# for loop
list_for_loop = ['first', 'second', 'third']

for item in list_for_loop:
    print(item)

for ch in 'loop':
    print(ch)

# Nested for loop
fruits = ['apple', 'banana']
vegetables = ['cucumber', 'tomato', 'carrot']

for fruit in fruits:
    for vegetable in vegetables:
        print(fruit[0], vegetable[-1])

# While Loop

secret_number = 3
guess = 0

# while guess != secret_number:
#     guess = int(input('Guess the numnber (1 - 5)'))
#     if(guess != secret_number):
#         print("Wrong, try again")
# print("You guessed the number")\

developer_names = ['Stan', 'Mary', "Michael"]

# for name in developer_names:
#     if name == 'Mary':
#         break
#     print(name)


for new_name in developer_names:
    if new_name == 'Mary':
        continue
    print(new_name)

words = ['apple', 'banana', 'helicopter', 'tomato', 'car', 'rhythm']

for word in words:
    found_vowels = []

    for letter in word:
        if letter.lower() in 'aeiou':
            found_vowels.append(letter)

    if len(found_vowels) > 0:
        print(f'{word} contains {len(found_vowels)} vowels {", ".join(found_vowels)}')

    else:
        print(f'{word} does not contain any vowels')


for num in range(40, 0, -5):
    print(num)

# Generate a List with even numbers

numbers = list(range(2, 11, 2))
print('|'.join(str(numbers)))