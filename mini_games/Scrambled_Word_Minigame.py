import random

def scrambled_word():

    #List of words
    words = ["hello", "this", "test", "temp"]
    #Randomly selecting a word from the list
    random_number = random.randint(0, len(words))
    random_word = words[random_number]
    n = len(random_word)
    chars = list(random_word)
    #"Randomising it"
    for i in range(0, n-1):
        pos = random.randint(i+1,n-1)
        chars[pos], chars[i] = chars[i], chars[pos]
    result = ""
    for i in range(n):
        result += chars[i]

    #Printing the result
    print(result)
    print()
    print("Seems like some word we need to unscramble...")
    completed = False
    guesses = 1
    #Looping around until the user unscrambles the word or runs out of attempts
    while completed is False:
        user_input = str(input("Doesn't seem that hard, I think we can word this one out:"))
        if user_input == random_word:
            print("Ahaha, were in! That wasn't so hard!")
            return
        elif guesses >4:
            
            print("BREECH DETECTED, RESETTING CODE...")
            print()
            return scrambled_word()
        
        else:
            guesses = guesses + 1
            print("Hmmm, well we know its not that then.")
                     
    
scrambled_word()
