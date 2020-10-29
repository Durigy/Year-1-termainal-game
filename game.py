#!/usr/bin/python3
from time import time
from main_game import rooms, roads, spots, print_specialised_words, normalise_input, current_room, tools, food, inventory, old_time, header, footer, info
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
    return print_specialised_words()


def execute_go(direction):
    global current_room
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
            if i == direction:
                current_room = spots[x]
    else:
        info("You cannot go there.", 70, 70)


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
    elif is_valid_item(current_room["food"], item_id):
        for i in current_room["food"]:
            if i == item_id:
                inventory["food"].append(i)
                cRF.remove(i)
    else:
        info("You cannot take that.", 71, 70)


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
        info("You cannot drop that.", 71, 70)


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
        info("You cannot eat that.", 70, 70)

def execute_taste(item_id):
    global inventory
    global current_room
    if is_valid_item(inventory["food"], item_id):
        for i in inventory["food"]:
            if i == item_id:
                info("The item you tasted was goooood. Also, it has " + str(food[item_id]["energy"]) + " energy.", 88, 87)
    elif is_valid_item(inventory["tools"], item_id):
        for i in inventory["tools"]:
            if i == item_id:
                info("Ewwww! Don't lick that, that is disgusting.", 82, 81)
    else:
        info("You cannot taste that.", 71, 71)


def execute_command(command):
    if command[0] == "go" or command[0] == "move":
        if len(command[1]) >= 1:
            execute_go(command[1])
        elif len(command[1]) <= 1:
            #print("\n" + "-"*90 + "\n\nGo where?")
            info("Go where?", 65, 64)


    elif command[0] == "take" or command[0] == "pick up":
        if len(command[1]) >= 1:
            execute_take(command[1])
        elif len(command[1]) <= 1:
            print("\n" + "-"*90 + "\n\nTake what?")
            info("Take what?", 65, 65)

    elif command[0] == "drop" or command[0] == "release":
        if len(command[1]) >= 1:
            execute_drop(command[1])
        elif len(command[1]) <= 1:
            info("Drop what?", 65, 65)

    elif command[0] == "eat":
        if len(command[1]) >= 1:
            execute_eat(command[1])
        elif len(command[1]) <= 1:
            #print("\n" + "-"*90 + "\n\nEat what?")
            info("Eat what?", 65, 64)

    elif command[0] == "taste":
        if len(command[1]) >= 1:
            execute_taste(command[1])
        elif len(command[1]) <= 1:
            info("Taste what?", 66, 65)

    elif command[0] == "help":
        info("These are the commands you can type to use: " + print_help(), 120, 119)

    elif command[0] == "exit":
        check = normalise_input(input("Are you sure you want to exit the game. You will lose everything. (YES/NO): "), False)
        if check == "yes":
            exit()
        elif len(check) >= 0:
            info("The Game Continues", 65, 65)

    elif command[0] == "no" and len(command[1]) >= 1 :
        info("What would you like to do with that item?", 81, 80)

    elif command[0] == "no" and len(command[1]) <= 1 :
        info("Please type something useful", 65, 65)

    else:
        info("This makes no sense.", 70, 70)


def user_input():
    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    # Next room to go to
    return spots[exits[direction]]

def death_screen():
    print("\n" + "-"*90 + "\n\nYou died, tray again later.\n\n" + "-"*90 + "\n")

def win_screen():
    print("\n" + "-"*90 + "\n\nYou died, tray again later.\n\n" + "-"*90 + "\n")

def difficulty(level):
    global inventory
    if level == "easy" or level == "e":
        inventory["health"] = 5
        return True
    elif level == "medium" or level == "m":
        inventory["health"] = 3
        return True
    elif level == "hard" or level == "h":
        inventory["health"] = 1
        return True
    elif len(level) >= 0:
        return False



# This is the entry point of our program
def main():
    dif_chosen = False
    while not dif_chosen:
        dif_chosen = difficulty(normalise_input(input("Please choose a difficulty: EASY, MEDIUM or HARD: "), False))

    # Main game loop
    while int(inventory["health"]) > 0:
        new_print_room(current_room, current_room["tools"], current_room["food"])

        # Show the menu with possible actions and ask the player
        #command = menu(current_room["exits"], current_room["tools"], current_room["food"], inventory)
        command = user_input()


        # Execute the player's command
        execute_command(command)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

