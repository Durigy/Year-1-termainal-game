import random

def access_code_minigame():

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
            try:
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
            except ValueError:
                print("There are only numbers on the keypad")

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


#access_code_minigame()

def scrambled_word():

    #List of words
    words = ["hello", "this", "test", "temp", "issue"]
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
                     
    
#scrambled_word()

def morse_code_minigame():
    
	#placeholder for the room that the player is supposed to go to next
	next_room="Windy Path"
	#list of the rooms and corresponding morse codes for the rooms
	morse_roomlist=["Windy Path",".... . .-. --- -.. / -.-. .-.. --- ... .","herod street",".... . .-. --- -.. / ... - .-. 	. . -","carpark","-.-. .- .-. .--. .- .-. -.-",
                        "labratory 1",".-.. .- -... --- .-. .- - --- .-. -.-- / .----","main 		street","-- .- .. -. / ... - .-. . . -","shop","... .... --- .--.",
                        "the plough","- .... . / .--. .-.. --- ..- --. ....",	"alleyway",".- .-.. .-.. . -.-- .-- .- -.--","isiah road",".. ... .. .- .... / .-. --- .- -..",
                        "laboratory 2",".-.. .- -.	.. --- .-. .- - --- .-. -.-- / ..---","willow park",".-- .. .-.. .-.. --- .-- / .--. .- .-. -.-",
                        "windy path",".-- .. -. 	-.. -.-- / .--. .- - ....","library",".-.. .. -... .-. .- .-. -.--"]
	
	print("A	.-		B	-...\nC	-.-.		D	-..\nE	.		F	..-.\nG	--.		H	....\nI	..		J	.---\nK	-.-		L	.-..\nM	--		N	-.\nO	---		P	.--.\nQ	--.-		R	.-.\nS	...		T	-\nU	..-		V	...-\nW	.--		X	-..-\nY	-.--		Z	--..\n1.----	2	..---\nSPACE	/\n\n\nIf you answer incorrectly, you will be prompted to 		answer again.\nUse the above table to translate the following:")
	#searches for the next room in the list above and sets a variable to the element's position in the list
	where=morse_roomlist.index(next_room.lower())

	#begins loop to run until the minigame is completed correctly
	morse_complete=False
	while morse_complete!=True:
		#assigns a variable to the morse-translated version of the next room
		morse_room=morse_roomlist[where+1]
		#prints the morse version of the next room
		print(morse_room)
		#calls for user's answer
		morse_attempt=input()
		#checks the user's answer against the element in the correct position in the roomlist
		if morse_attempt.lower()==morse_roomlist[where]:
			morse_complete=True
		else:
			print("Incorrect\n")

morse_code_minigame()
