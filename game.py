#!/usr/bin/python3
from time import time
<<<<<<< HEAD
from main_game import rooms, roads, spots, print_specialised_words, normalise_input, current_room, tools, food, inventory, old_time

def print_room_items(tools, food):
    temp = []  # room tools
    for i in tools:
        temp.append(i)
    rtool = ", ".join(temp)

    temp = []  # room food
    for i in food:
        temp.append(i)
    rfood = ", ".join(temp)

    if rtool and rfood:
        print("There is,", rtool + ",", rfood + ", in this part of the room.\n")
    elif rtool:
        print("There is,", rtool + ", in this part of the room.\n")
    elif rfood:
        print("There is,", rfood + ", in this part of the room.\n")
    else:
        print("There isn't anything in this part of the room.\n")


def print_inventory_items(players_inverntory):
    temp = []  # inventory tools
    for i in players_inverntory["tools"]:
        temp.append(i)
    itool = ", ".join(temp)

    temp = []  # inventory food
    for i in inventory["food"]:
        temp.append(i)
    ifood = ", ".join(temp)

    if itool and ifood:
        print("You have,", itool + ",", ifood + ", in your inventory.\n")
    elif itool:
        print("You have,", itool + ", in your inventory.\n")
    elif ifood:
        print("You have,", ifood + ", in your inventory.\n")
    else:
        print("You don't have anything in you inventory.\n")
=======
from main_game import rooms, roads, spots, print_specialised_words, normalise_input, current_room, tools, food, inventory, old_time, header, footer,  go_wh, take_wh, eat_wh, taste_wh, go_ct, take_ct, eat_ct, taste_ct, taste_info, taste_ew, access_code_minigame, scrambled_word, morse_code_minigame
>>>>>>> master

global run
global pub_code
global library_code

run = 0
pub_code = 0
library_code = 0


def new_print_room(room, tools, food):
    header(room["name"].upper(), room["spot name"].upper(), str(inventory["health"]), str(energy_level()))
    print(room["map"])
    footer(inventory["tools"] + inventory["food"], room["tools"] + room["food"], room["description"])

def print_player_info():
    print_inventory_items(inventory)
    energy_level()

def exit_leads_to(exits, direction):
    return spots[exits[direction]]["name"]

def energy_level():
    global inventory
    global old_time
    t = 20
    if (time() - old_time) >= t*10:
        inventory["energy"] -= 10
        old_time = time()
    elif (time() - old_time) >= t*9:
        inventory["energy"] -= 9
        old_time = time()
    elif (time() - old_time) >= t*8:
        inventory["energy"] -= 8
        old_time = time()
    elif (time() - old_time) >= t*7:
        inventory["energy"] -= 7
        old_time = time()
    elif (time() - old_time) >= t*6:
        inventory["energy"] -= 6
        old_time = time()
    elif (time() - old_time) >= t*5:
        inventory["energy"] -= 5
        old_time = time()
    elif (time() - old_time) >= t*4:
        inventory["energy"] -= 4
        old_time = time()
    elif (time() - old_time) >= t*3:
        inventory["energy"] -= 3
        old_time = time()
    elif (time() - old_time) >= t*2:
        inventory["energy"] -= 2
        old_time = time()
    elif (time() - old_time) >= t*1:
        inventory["energy"] -= 1
        old_time = time()

    if inventory["energy"] <= 0:
        inventory["health"] -= 1
        inventory["energy"] = 10

    if inventory["health"] <= 0:
        death_screen()
        exit()

    return inventory["energy"]


def is_valid_exit(exits, chosen_exit):
        return chosen_exit in exits

def print_help():
    print_specialised_words()


def execute_go(direction):
    global current_room
    global run
    global library_code
    global pub_code
    
    if direction == "n":
        direction = "north"
    if direction == "e":
        direction = "east"
    if direction == "s":
        direction = "south"
    if direction == "w":
        direction = "west"

    if is_valid_exit(current_room["exits"], direction):
        for i, x in current_room["exits"].items():
            # Minigame in lab 1 (access_code)
            
            if i == direction and x == "lab 1 side entrance" or i == direction and x == "lab1 main entrance":
                if run == 0:
                    access_code_minigame()
                    if True:
                        if i == direction:
                            run += 1
                            current_room = spots[x]
                    else:
                        return
                elif i == direction:
                    current_room = spots[x]
                    
            # Minigame in in Library (Herold Close Section)

            #elif i == direction and x == "contam area centre": # or i == direction and x == "mystery aisle":
                #if library_code == 0:
                    #morse_code_minigame()
                    #if True:
                        #if i == direction:
                            #library_code += 1
                            #current_room = spots[x]
                    #else:
                        #return
                    
            elif i == direction and x == "pub centre": #or i == direction and x == "alley front":
                if pub_code == 0:
                    scrambled_word()
                    if True:
                        if i == direction:
                            pub_code += 1
                            current_room = spots[x]
                    else:
                        return
                elif i == direction:
                    current_room = spots[x]
            elif i == direction:
                current_room = spots[x]
                pass


            # Minigame 3

            
            elif i == direction:
                current_room = spots[x]
    else:
        go_ct("You cannot go there.")


def is_valid_item(room_item, chosen_item):
    for a in room_item:
        if chosen_item == a:
            return True
    return False


def execute_take(item_id):
    global inventory
    global current_room
    cRT = current_room["tools"]
    cRF = current_room["food"]
    if is_valid_item(current_room["tools"], item_id):
        for i in current_room["tools"]:
            if i == item_id:
                inventory["tools"].append(i)
                cRT.remove(i)
                print("\n" + "-"*90 + "\n\nYou took the", item_id.capitalize())
                take_ct("You cannot go there.")
    elif is_valid_item(current_room["food"], item_id):
        for i in current_room["food"]:
            if i == item_id:
                inventory["food"].append(i)
                cRF.remove(i)
    else:
        take_ct("You cannot take that.")


def execute_drop(item_id):
    global inventory
    global current_room
    cRT = current_room["tools"]
    cRF = current_room["food"]
    if is_valid_item(inventory["tools"], item_id):
        for i in inventory["tools"]:
            if i == item_id:
                inventory["tools"].remove(i)
                cRT.append(i)
    elif is_valid_item(inventory["food"], item_id):
        for i in inventory["food"]:
            if i == item_id:
                inventory["food"].remove(i)
                cRF.append(i)
    else:
        take_ct("You cannot drop that.")


def execute_eat(item_id):
    global inventory
    global current_room
    cRF = current_room["food"]
    if is_valid_item(inventory["food"], item_id):
        for i in inventory["food"]:
            if i == item_id:
                inventory["food"].remove(i)
                if inventory["energy"] < 10:
                    if (inventory["energy"] + food[item_id]["energy"]) > 10:
                        inventory["energy"] = 10
                    else:
                        inventory["energy"] += food[item_id]["energy"]
                #print("\n" + "-"*90 + "\n\nYou ate the", item_id.capitalize(), "which had", food[item_id]["energy"], "energy.")
    else:
        eat_ct("You cannot eat that.")

def execute_taste(item_id):
    global inventory
    global current_room
    if is_valid_item(inventory["food"], item_id):
        for i in inventory["food"]:
            if i == item_id:
                i = "You tasted the", item_id.capitalize(), "and it is goooood. Also, it has", food[item_id]["energy"], "energy."
                taste_info(str(i).strip("()''"))
    elif is_valid_item(inventory["tools"], item_id):
        for i in inventory["tools"]:
            if i == item_id:
                taste_ew("Ewwww! Don't lick that, that is disgusting.")
    else:
        taste_ct("You cannot taste that.")


def execute_command(command):
    if command[0] == "go" or command[0] == "move":
        if len(command[1]) >= 1:
            execute_go(command[1])
        elif len(command[1]) <= 1:
            #print("\n" + "-"*90 + "\n\nGo where?")
            go_wh("Go where?")


    elif command[0] == "take" or command[0] == "pick up":
        if len(command[1]) >= 1:
            execute_take(command[1])
        elif len(command[1]) <= 1:
            print("\n" + "-"*90 + "\n\nTake what?")
            take_wh("Take what?")

    elif command[0] == "drop" or command[0] == "release":
        if len(command[1]) >= 1:
            execute_drop(command[1])
        elif len(command[1]) <= 1:
            take_wh("Drop what?")

    elif command[0] == "eat":
        if len(command[1]) >= 1:
            execute_eat(command[1])
        elif len(command[1]) <= 1:
            #print("\n" + "-"*90 + "\n\nEat what?")
            eat_wh("Eat what?")

    elif command[0] == "taste":
        if len(command[1]) >= 1:
            execute_taste(command[1])
        elif len(command[1]) <= 1:
            taste_wh("Taste what?")

    elif command[0] == "help":
        print_help()

    elif command[0] == "exit":
        check = normalise_input(input("Are you sure you want to exit the game. You will lose everything. (YES/NO): "), False)
        if check == "yes":
            exit()
        elif len(check) >= 0:
            print("\n" + "-"*90 + "\n\nThe Game Continues")

    elif command[0] == "no" and len(command[1]) >= 1 :
        print("\n" + "-"*90 + "\n\nWhat would you like to do with the:", command[1].capitalize())

    elif command[0] == "no" and len(command[1]) <= 1 :
        print("\n" + "-"*90 + "\n\nPlease type something useful")

    else:
        print("\n" + "-"*90 + "\n\nThis makes no sense.")


def menu(exits, tools, food, inv):
    # Display menu
    #print_menu(exits, tools, food, inv)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    # Next room to go to
    return spots[exits[direction]]

def death_screen():
    from game_menu import youdied

def win_screen():
    print("\n" + "-"*90 + "\n\nYou died, tray again later.\n\n" + "-"*90 + "\n")

def difficulty(level):
    global inventory
    if level == "easy" or level == "e":
        inventory["health"] = 5
        #print("\n" + "-"*90 + "\n\nyou chose easy, you have, 5 lives.")
        return True
    elif level == "medium" or level == "m":
        inventory["health"] = 3
        #print("\n" + "-"*90 + "\n\nyou chose medium, you have, 3 lives.")
        return True
    elif level == "hard" or level == "h":
        inventory["health"] = 1
        #print("\n" + "-"*90 + "\n\nyou chose hard, you have, 1 live, don't waste it.")
        return True
    elif len(level) >= 0:
        #print("\n" + "-"*90 + "\n\nType a difficulty: easy, medium or hard.")
        return False



# This is the entry point of our program
def main():
    dif_chosen = False
    while not dif_chosen:
        dif_chosen = difficulty(normalise_input(input("Please choose a difficulty: EASY, MEDIUM or HARD: "), False))

    # Main game loop
<<<<<<< HEAD
    Intro
    while inventory["health"] > 0:
        # Display game status (room description, inventory etc.)
        print_room(current_room, current_room["tools"], current_room["food"])
        print_player_info()
=======
    while int(inventory["health"]) > 0:

        #Prints UI
        new_print_room(current_room, current_room["tools"], current_room["food"])

>>>>>>> master

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["tools"], current_room["food"], inventory)
        
        # Execute the player's command
        execute_command(command)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

