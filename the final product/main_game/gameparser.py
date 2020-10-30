import string
from time import time
from .items import tools, food

# These are the lists of key words used in the game
specialised_words = ["go", "move", "take", "pick up","drop", "release", "eat", "taste", "help", "exit"]
direction = ["north","east","south","west", "n","e","s","w"]

old_time = time()

# This function turns the command list into a comma separated string and returns it so it can be displayed to the player as helpful commands
def print_specialised_words():
    text = ''
    for i in specialised_words:
        text += i.upper() + ", "
    return text

# This function filters out all the unneeded words
def filter_words(words):
    com = ""
    n = ""
    s = words.split()

    # This part takes out the command word and stores it as a variable and if there isn't one then it stores no - as in no command word found
    for x in specialised_words:
        if x in words:
            com = x
        if len(com) == 0:
            com = "no"

    # This part takes out the direction key word and stores it as a variable - n
    for word in s:
        for sWord in direction:
            if word == sWord:
                n = word

    # This part checks the know tools list from items.py and if one is found it over writes the variable - n
    for x, y in tools.items():
        if x in words:
            n = x

    # This part checks the know food list from items.py and if one is found it over writes the variable - n
    for x, y in food.items():
        if x in words:
            n = x

    # This part combines the command work with the item/direction in a list then returns the list
    new_word = [com, n]
    return new_word

# This function removers all the punctuation from any part of the string
def remove_punct(text):
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct
# This function takes the user input and returns it without all the unneeded words
def normalise_input(user_input, filtered = True):
    # Remove punctuation and convert to lower case
    words = remove_punct(user_input).lower()
    if filtered:
        filtered_words = filter_words(words)
    else:
        filtered_words = words

    return filtered_words
