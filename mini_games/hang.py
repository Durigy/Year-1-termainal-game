import random

def random_word(word_list):
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]

def print_hangman():
        print(picture[len(missing_letters)])

def Showcase(missing_letters, correct_letters, secret_word):
    print_hangman()

    print("Wrong letters:", end=' ')
    for letter in missing_letters:
        print(letter, end=' ')
    print("\n")
    blanks = ''
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks += secret_word[i]
        else:
            blanks += '_'
    print("Current Guess:", end=' ')
    for letter in blanks:
        print(letter, end=' ')
    print()


def aquire_guess(guessed):
    while True:
        print()

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print('Please input a single letter, or number')
        elif guess in guessed:
            print('You have already guessed that letter. Please choose again')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter')
        else:
            return guess
def play_again():
    global play
    print_hangman()

    play_this = input('Do you want to try again (yes/no): ')

    if play_this == 'yes':
        print('Good Luck')

    else:
        play = False

words = ["asdfghjkl"]

guesses = 0
missing_letters = ''
correct_letters = ''
secret_word = random_word(words)
game_over = False

# Hangman pictures for incorrect guesses.
picture = [
'''
 --------------------
 |                  |
 |                  |
 |                  |
 |                  |
 |                  |
 |                  |
 |                  |
 |                  |
 |                  |
 --------------------
''',

'''
 --------------------
 |                  |
 |                  |
 |                  |
 |                  |
 |                  |
 |                  |
 |                  |
 |     ========     |
 |                  |
 --------------------
''',

'''
 --------------------
 |                  |
 |                  |
 |                  |
 |                  |
 |     |            |
 |     |            |
 |     |            |
 |     ========     |
 |                  |
 --------------------
''',

'''
 --------------------
 |                  |
 |     +            |
 |     |            |
 |     |            |
 |     |            |
 |     |            |
 |     |            |
 |     ========     |
 |                  |
 --------------------
''',

'''
 --------------------
 |                  |
 |     +---+        |
 |     |            |
 |     |            |
 |     |            |
 |     |            |
 |     |            |
 |     ========     |
 |                  |
 --------------------
''',

'''
 --------------------
 |                  |
 |     +---+        |
 |     |   |        |
 |     |   o        |
 |     |   |        |
 |     |            |
 |     |            |
 |     ========     |
 |                  |
 --------------------
''',

'''
 --------------------
 |                  |
 |     +---+        |
 |     |   |        |
 |     |   o        |
 |     |  /|\       |
 |     |            |
 |     |            |
 |     ========     |
 |                  |
 --------------------
''',

'''
 --------------------
 |                  |
 |     +---+        |
 |     |   |        |
 |     |   o        |
 |     |  /|\       |
 |     |  / \       |
 |     |            |
 |     ========     |
 |                  |
 --------------------
''',

''
]
def fun():
    guesses = 0
    missing_letters = ''
    correct_letters = ''
    secret_word = random_word(words)
    game_over = False

def hang_game():
    print('\n' * 10)
    print('Lets Go')
    global guesses
    global missing_letters
    global correct_letters
    global secret_word
    global game_over
    while guesses < 7:
        Showcase(missing_letters, correct_letters, secret_word)
        guess = aquire_guess(missing_letters + correct_letters)

        if guess in secret_word:
            correct_letters += guess

            found_all_letters = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break

            if found_all_letters:
                print('Well done you have won. The secret word is:', secret_word)
                game_over = True
                break


        else:
            missing_letters += guess
            guesses += 1

            if guesses == 7:
                Showcase(missing_letters, correct_letters, secret_word)
                print("\n", 'You have ran out of guesses, you have had', len(missing_letters), 'missed guesses and', len(correct_letters), 'correct guess.')
                print(secret_word)
    play_again()

hang_game()