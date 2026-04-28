full_dot = '●'
empty_dot = '○'


def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        return 'The character name should be a string'
    if not character_name:
        return 'The character should have a name'
    if len(character_name) > 10:
        return 'The character name is too long'
    if " " in character_name:
        return 'The character name should not contain spaces'
    if not all(isinstance(stat, int) for stat in [strength, intelligence, charisma]):
        return 'All stats should be integers'
    if any(stat < 1 for stat in [strength, intelligence, charisma]):
        return 'All stats should be no less than 1'
    if any(stat > 4 for stat in [strength, intelligence, charisma]):
        return 'All stats should be no more than 4'
    if not (strength + intelligence + charisma) == 7:
        return 'The character should start with 7 points'

    str_empty, int_empty, cha_empty = [10 - stat for stat in [strength, intelligence, charisma]]

    return f'{character_name}\nSTR {full_dot * strength}{empty_dot * str_empty}\nINT {full_dot * intelligence}{empty_dot * int_empty}\nCHA {full_dot * charisma}{empty_dot * cha_empty}'


print(create_character('Stan', 4, 2, 1))