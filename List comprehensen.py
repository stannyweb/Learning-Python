even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print(even_numbers)

my_list = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in my_list]
print(result)

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']


def is_long_word(word):
    return len(word) > 4


long_words = list(filter(is_long_word, words))
print(long_words)

# alternative

longer_word = list(filter(lambda word: len(word) > 4, words))
print(longer_word)

short_word = [word for word in words if len(word) > 3]
print(short_word)

# Map function
celsius = [0, 10, 20, 30, 40]


def to_fahrenheit(temp):
    return (temp * 9 / 5) + 32


fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit)

another_fahrenheit = list(map(lambda c: (c * 9 / 5 + 32), celsius))
print(another_fahrenheit)

# With List comprehension
list_Celsius = [(c * 9 / 5 + 32) for c in celsius]
print(list_Celsius)

sum_list = [10, 20, 30, 40, 50]
results = sum(sum_list)
print(results)

sum_list = [10, 20, 30, 40, 50]
results = sum(sum_list, start=-50)
print(results)

sum_list = sum([num for num in sum_list if num > 25]) + 25
print(sum_list)