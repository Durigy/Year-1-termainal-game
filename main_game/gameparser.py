import string

skip_words = []

def filter_words(words, skip_words):
    for word in words[:]:
        for sWord in skip_words:
            if word == sWord:
                words.remove(word)
    return words
    
def remove_punct(text):
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct

def normalise_input(user_input):
    # Remove punctuation and convert to lower case
    return remove_punct(user_input).lower()