import os

from my_termo.raffle import raffle_word


COLORS = {
    'yellow': '🟨',
    'green': '🟩',
    'black': '⬛'
}


def clear():
    """This function clear console"""
    os.system('cls' if os.name=='nt' else 'clear')


def show_instructions():
    """This function print a help text to teach how to play"""
    print("""
    Termo is a game to guess a word of the day.
    Colors help:
    - 🟩: This color is showned when the letter exist in the word and the position is correctly too.
    - 🟨: This color is showned when the letter exist in the word bot the position is not correctly.
    - ⬛: This color is showned when the letter does not exist in the word.

    You have 6 attempts.

    If you get the word right, TERMO will show the historic of attempts.
    """)
    input('Type any key to back...')
    clear()



def bold(message: str):
    return f'\033[1m{message}\033[0m'


def termo():
    """The TERMO game. Type help any moment to show instructions
    >>> termo
    Welcome to TERMO Command Line 😆
    (type "help" any moment to show instructions)

    Type a word: 
    ...
    """

    daily_word = raffle_word()
    attempts = 6
    count = 0
    message = ''
    final_message = ''

    try:
        print('Welcome to TERMO Command Line 😆')
        print('(type "help" any moment to show instructions)\n')
        
        while count < attempts:
            while len(word := input("Type a word: ")) != 5:
                if word == 'help':
                    show_instructions()
                else:
                    print('Only words with 5 letters!')

            for i, letter in enumerate(word):
                if letter in daily_word and word[i] == daily_word[i]:
                    message += COLORS.get('green')
                elif letter in daily_word:
                    message += COLORS.get('yellow')
                else:
                    message += COLORS.get('black')

            final_message += f'{message}\n{" ".join(list(word))}\n'
            clear()
            print(final_message)
            message = ''
            count += 1

            if word == daily_word:
                clear()
                print(f'\tThe word is {bold(daily_word)}')
                print(f'\nThank you for playing my termo 🥳👏\n{final_message}')
                exit()
        print('Sorry 💀 Try again later.')

    except KeyboardInterrupt:
        print("\nBye 😊👋")
