my_languages = ['English', 'French', 'Swedish']

for index, language in enumerate(my_languages):
    print(f'The {index} index is a {language} language.')


# With optional start parameter
for index, language in enumerate(my_languages, 1):
    print(f'The {index} index is a {language} language.')


# Working with zip, they convert lists into tuples.

my_games = ['GTA5', 'GOD OF WAR', 'RDR2', 'CRIMSON DESERT']
my_rating = [8, 10, 9, 10]

for game, rating in zip(my_games, my_rating):

    if rating == 10:
        print(f'This {game} has {rating} rating and it is a masterpiece.')
    else:
        print(f'This {game} has {rating} rating and it is a okay.')