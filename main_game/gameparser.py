import string
from time import time
from .items import tools, food

# # specialised_words = ["go", "take","drop","look","open","close","enter","leave","menu","eat","north","east","south","west","inventory","use"] # don't think we need all these anymore
specialised_words = ["go", "move", "take", "pick up","drop", "release", "look", "eat", "taste", "use", "help"]
direction = ["north","east","south","west"]
#difficulty = ["easy","medium","hard"]

old_time = time()

def print_specialised_words():
    print("\n" + "-"*90 + "\n")
    print("You can type these commands: ", end='')
    for i in specialised_words:
        print(i.upper() + ", ", end='')
    print()

def filter_words(words):
    com = ""
    n = ""
    s = words.split()
    # for word in s:
    #     for sWord in specialised_words:
    #         if word == sWord:
    #             com = word
    #     if len(com) == 0:
    #         com = "no"

    for x in specialised_words:
        if x in words:
            com = x
        if len(com) == 0:
            com = "no"

    # for word in s:
    #     for sWord in difficulty:
    #         if word == sWord:
    #             n = word
    #             com = "difficulty"

    for word in s:
        for sWord in direction:
            if word == sWord:
                n = word

    for x, y in tools.items():
        if x in words:
            n = x

    for x, y in food.items():
        if x in words:
            n = x

    new_word = [com, n]
    return new_word

    
def remove_punct(text):
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct

def normalise_input(user_input, filtered = True):
    # Remove punctuation and convert to lower case
    words = remove_punct(user_input).lower()
    if filtered:
        filtered_words = filter_words(words)
    else:
        filtered_words = words

    #filtered_words = filter_words(words) #filter_words(words.split())
    return filtered_words
