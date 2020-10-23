
def access_code_minigame():
        
    import random

    run = 0
    access_code = ""
    completed = False
    print("Looks as if the door is locked.")
    print("Hmmm, it seems here that the keypad only has numbers five number!")
    print("Maybe taking a guess isn't a bad shout?" + "\n")
    while completed is False:
        number = random.randint(1,5)
        number = int(number)
        guesses = 0
        while guesses < 4:  
            guess = int(input("A guess between 1-5, shouldn't be too hard?:"))
            if guess > 5:
                print("Hmmm, could've sworn there was only five numbers on the keypad")
                guesses +=1
            elif guess < 1:
                print("Didn't know you could have negative numbers on a keypad")
                guesses +=1
            else:
                if guess == (number):
                    print ("Ahaha! looks like we have got it right" + "\n")
                    run += 1
                    guesses = 4
                    number = str(number)
                    access_code = str(access_code) + number
                    number = int(number)
                    if run == 4:
                        completed = True
                elif guess > number:
                    print ("Something feels wrong about this guess. It must be lower" + "\n")
                    guesses +=1
                elif guess < number:
                    print ("Hmmm, My spidy senses tells me this number is higher" + "\n")
                    guesses +=1
                    
    print("ACCESS CODE: " + access_code)                
    code_rejected = 1
    access_granted = False
    while access_granted is False:
        user_input = input("Enter the code here:")
        print (access_code)
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
