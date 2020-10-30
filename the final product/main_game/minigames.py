import random

def user_interface(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)

def access_code_minigame():
    print("\n"*70)

    #Setting up the variables values
    run = 0
    access_code = ""
    completed = False
    
    #Information printed out to user
    print("┌----  ------  ------  -------  ------  ------  ------  ------  -----  -----  ----┐")
    print("|                                                                                 |")
    print("   Looks as if the door is locked.                                                 ")
    print("|  Hmmm, it seems here that the keypad only has numbers five numbers!             |")
    print("   Maybe taking a guess isn't a bad shout?                                         ")
    print("|                                                                                 |")
    print("└----  ------  ------  -------  ------  ------  ------  ------  -----  -----  ----┘")
    print("")
    
    #While loop that starts of the program and randomly generates a number
    while completed is False:
        number = random.randint(1,5)
        number = int(number)
        guesses = 1
        test = ("                       |")
        #Loop that checks whether the users guesses remains below 3
        #and that they do not enter a value outside of 1-5.
        while guesses < 5:
            try:

                print("|                                                                                 |")
                guess = int(input("   A guess between 1-5, shouldn't be too hard?:"))
                
                if guess > 5:
                    print("|                                                                                 |")
                    print("   Hmmm, could've sworn there was only five numbers on the keypad                 ")
                    guesses +=1
                elif guess < 1:
                    print("|                                                                                 |")
                    print("   Didn't know you could have negative numbers on a keypad")
                    guesses +=1
                else:

                    #If/ Elif statements that check whether the user's guess is correct,
                    #then provides hints.
                    if guess == (number):
                        print("|                                                                                 |")
                        print("   Ahaha! looks like we have got it right                                         ")
                        print("|                                                                                 |")
                        print("└----  ------  ------  -------  ------  ------  ------  ------  -----  -----  ----┘")
                        run += 1
                        guesses = 5
                        number = str(number)
                        access_code = str(access_code) + number
                        number = int(number)
                        if run == 4:
                            completed = True
                    elif guesses > 2:
                        print("")
                        print("|  INTRUDER ALERT,INTRUDER ALERT, RESETTING CODE NOW...                           |")
                        print("")
                        print("|                                                                                 |")
                        print("└----  ------  ------  -------  ------  ------  ------  ------  -----  -----  ----┘")
                        return access_code_minigame()
                    elif guess > number:
                        print("|                                                                                 |")
                        print("   Something feels wrong about this guess. It must be lower                        ")
                        #print("|                                                                                 |")
                        guesses +=1
                    elif guess < number:
                        print("|                                                                                 |")
                        print("   Hmmm, My spidy senses tells me this number is higher                           ")
                        guesses +=1
            except ValueError:
                print("|                                                                                 |")
                print("   There are only numbers on the keypad")

    #Setting variable values and telling the user the access code.
    print("|                                                                                 |")
    print("   ACCESS CODE: " + access_code + "                                                               ")
    print("|                                                                                 |")
    code_rejected = 1
    access_granted = False

    #Loop to check whether the user has entered the correct value,
    #and if not returning them back to the necessary section.
    while access_granted is False:
        user_input = input("   Enter the code here:")
        if user_input == access_code:
            print("|                                                                                 |")
            print("   AT LAST WERE IN!                                                               ")
            print("|                                                                                 |")
            print("└----  ------  ------  -------  ------  ------  ------  ------  -----  -----  ----┘")
            
            access_granted = True
            run += 1
            return True
        elif code_rejected > 2:
            print("|                                                                                 |")
            print("   CODE REJECTED, RESETTING CODE NOW...                                           ")
            print("|                                                                                 |")
            return access_code_minigame()
        else:
            print("|                                                                                 |")
            print("   CODE REJECTED                                                                    ")
            print("|                                                                                 |")
            code_rejected += 1


#access_code_minigame()

def scrambled_word():
    print("\n"*70)

    #List of words
    words = ["password", "street", "secure", "control", "alleyway"]
    #Randomly selecting a word from the list
    #random_number = random.randint(0, len(words))
    random_word = random.choice(words)
    n = len(random_word)
    chars = list(random_word)
    #"Randomising it"
    for i in range(0, n-1):
        pos = random.randint(i+1,n-1)
        chars[pos], chars[i] = chars[i], chars[pos]
    result = ""
    for i in range(n):
        result += chars[i]

    remaining_spaces = 48 - len(result)
    
    #Printing the result
    print("┌----  ------  ------  -------  ------  ------  ------  ------  -----  -----  ----┐")
    print("                                                                                   ")
    print("|                                 "+result+ " " * remaining_spaces + "|")
    print("                                                                                   ")
    print("└----  ------  ------  -------  ------  ------  ------  ------  -----  -----  ----┘")  
    print("")
    print("|                                                                                 |")
    print("      Seems like some word we need to unscramble... Doesn't seem that hard,        ")
    completed = False
    guesses = 1
    #Looping around until the user unscrambles the word or runs out of attempts
    while completed is False:
        print("|                                                                                 |")
        user_input = str(input("                 I think we can word this one out:"))
        if user_input == random_word:
            print("|                                                                                 |")
            print("                 Ahaha, were in! That wasn't so hard!")
            print("|                                                                                 |")
            print("")
            print("└----  ------  ------  -------  ------  ------  ------  ------  -----  -----  ----┘")
            return True
        
        elif guesses >4:
            print("|                                                                                 |")
            print("                     BREECH DETECTED, RESETTING CODE...")
            print("|                                                                                 |")
            print("")
            print("└----  ------  ------  -------  ------  ------  ------  ------  -----  -----  ----┘")
            return scrambled_word()
        
        else:
            guesses = guesses + 1
            print("|                                                                                 |")
            print("                 Hmmm, well we know its not that then.")
                     







