import string

specialised_words = ["go", "take","drop","look","open","close","enter","leave","menu","eat","north","east","south","west","inventory","use"]

def filter_words(words, specialised_words):
    filtered = []
    for word in words:
        if word in specialised_words:
            filtered.append(word)
    
    words = filtered
    return words

    
def remove_punct(text):
    punct = '''!()@£$%&*-+_€\|][}{.,`~:;'''
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char

    return no_punct

def normalise_input(user_input):
    # Remove punctuation and convert to lower case
    words = remove_punct(user_input).lower()
    filtered_words = filter_words(words.split(), specialised_words)
    return filtered_words
