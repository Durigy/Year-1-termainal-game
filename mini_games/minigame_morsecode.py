#placeholder for the room that the player is supposed to go to next
next_room="Herod Close"
#list of the rooms and corresponding morse codes for the rooms
morse_roomlist=["herod close",".... . .-. --- -.. / -.-. .-.. --- ... .","herod street",".... . .-. --- -.. / ... - .-. . . -","carpark","-.-. .- .-. .--. .- .-. -.-","labratory 1",".-.. .- -... --- .-. .- - --- .-. -.-- / .----","main street","-- .- .. -. / ... - .-. . . -","shop","... .... --- .--.","the plough","- .... . / .--. .-.. --- ..- --. ....","alleyway",".- .-.. .-.. . -.-- .-- .- -.--","isiah road",".. ... .. .- .... / .-. --- .- -..","laboratory 2",".-.. .- -... --- .-. .- - --- .-. -.-- / ..---","willow park",".-- .. .-.. .-.. --- .-- / .--. .- .-. -.-","windy path",".-- .. -. -.. -.-- / .--. .- - ....","library",".-.. .. -... .-. .- .-. -.--"]
print("A	.-		B	-...\nC	-.-.	D	-..\nE	.		F	..-.\nG	--.		H	....\nI	..		J	.---\nK	-.-		L	.-..\nM	--		N	-.\nO	---		P	.--.\nQ	--.-	R	.-.\nS	...		T	-\nU	..-		V	...-\nW	.--		X	-..-\nY	-.--	Z	--..\n1.----	2	..---\nSPACE	/\n\n\nIf you answer incorrectly, you will be prompted to answer again.\nUse the above table to translate the following:")
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