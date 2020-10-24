def access_code_minigame():
        
    import random

    #Setting up the variables values
    run = 0
    access_code = ""
    completed = False
    
    #Information printed out to user
    print("Looks as if the door is locked.")
    print("Hmmm, it seems here that the keypad only has numbers five number!")
    print("Maybe taking a guess isn't a bad shout?" + "\n")

    #While loop that starts of the program and randomly generates a number
    while completed is False:
        number = random.randint(1,5)
        number = int(number)
        guesses = 1

        #Loop that checks whether the users guesses remains below 3
        #and that they do not enter a value outside of 1-5.
        while guesses < 5:  
            guess = int(input("A guess between 1-5, shouldn't be too hard?:"))
            if guess > 5:
                print("Hmmm, could've sworn there was only five numbers on the keypad" + "\n")
                guesses +=1
            elif guess < 1:
                print("Didn't know you could have negative numbers on a keypad" + "\n")
                guesses +=1
            else:

                #If/ Elif statements that check whether the user's guess is correct,
                #then provides hints.
                if guess == (number):
                    print ("Ahaha! looks like we have got it right" + "\n")
                    run += 1
                    guesses = 5
                    number = str(number)
                    access_code = str(access_code) + number
                    number = int(number)
                    if run == 4:
                        completed = True
                elif guesses > 2:
                    print("INTRUDER ALERT,INTRUDER ALERT, RESETTING CODE NOW..." + "\n")
                    return access_code_minigame()
                elif guess > number:
                    print ("Something feels wrong about this guess. It must be lower" + "\n")
                    guesses +=1
                elif guess < number:
                    print ("Hmmm, My spidy senses tells me this number is higher" + "\n")
                    guesses +=1

    #Setting variable values and telling the user the access code.                
    print("ACCESS CODE: " + access_code)                
    code_rejected = 1
    access_granted = False

    #Loop to check whether the user has entered the correct value,
    #and if not returning them back to the necessary section.
    while access_granted is False:
        user_input = input("Enter the code here:")
        if user_input == access_code:
            print("AT LAST WERE IN!")
            access_granted = True
            return
        elif code_rejected > 2:
            print("CODE REJECTED, RESETTING CODE NOW..." + "\n")
            return access_code_minigame()
        else:
            print("CODE REJECTED")
            code_rejected += 1


access_code_minigame()               
