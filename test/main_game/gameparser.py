import string
from .items import tools, food

# # specialised_words = ["go", "take","drop","look","open","close","enter","leave","menu","eat","north","east","south","west","inventory","use"] # don't think we need all these anymore
specialised_words = ["go", "take","drop","look","open","close","eat","use"]
direction = ["north","east","south","west"]

# List of "unimportant" words (feel free to add more)
# skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
#               'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
#               'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
#               'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
#               'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
#               'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
#               'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
#               'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
#               'wish', 'with', 'would']


# def filter_words(words):
#     com = ""
#     item = ""
#
#     if len(words) != 0:
#         for word in words[:]:
#             for sWord in specialised_words:
#                 if word == sWord:
#                     com = word
#
#
#             for sWord in skip_words:
#                 if word == sWord:
#                     if com != "no":
#                         words.remove(word)
#     else:
#         com = "no"
#
#     if com != "no":
#         if len(com) != 0:
#             words.remove(com)
#
#     new_word = [com, words]
#
#     return new_word

def filter_words(words):
    com = ""
    n = ""
    s = words.split()
    for word in s:
        for sWord in specialised_words:
            if word == sWord:
                com = word
        if len(com) == 0:
            com = "no"

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
    # if filtered:
    #     filtered_words = filter_words(words.split(), specialised_words)
    # else:
    #     filtered_words = words

    filtered_words = filter_words(words) #filter_words(words.split())
    return filtered_words
