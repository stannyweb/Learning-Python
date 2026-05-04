def your_mood():
    user_input = input('How do you feel today?').strip().lower()

    if user_input == 'bad':
        print('You should play something.')
    elif user_input == 'good':
        print('Learn something new.')
    else:
        print('You are the boss. Do Whatever you want.')

your_mood()
