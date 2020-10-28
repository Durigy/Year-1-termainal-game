#!/usr/bin/python3

from main_game import rooms, roads, spots, print_specialised_words, normalise_input, current_room, tools, food, inventory

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


def print_room(room, tools, food):
    print("\n" + "-"*90 + "\n")
    print(room["name"].upper(), "-", room["spot name"].upper(), "\n")
    # Display room description
    print("--- Room Description ---\n" + room["main description"], "\n\n" + "--- Location Description ---\n" + room["description"], "\n")

    print_room_items(tools, food)


def print_player_info():
    print_inventory_items(inventory)
    print("Your energy level is:", inventory["energy"], "\n")


def exit_leads_to(exits, direction):
    return spots[exits[direction]]["name"]

def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, tools, food, inv):

    print("You can:")

    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for i in tools:
        print("TAKE", i.upper(), "to take the", i + ".")

    for i in food:
        print("TAKE", i.upper(), "to take the", i + ".")

    for i in inv["tools"]:
        print("DROP", i.upper(), "to drop the", i + ".")

    for i in inv["food"]:
        print("DROP", i.upper(), "to drop the", i , "or\n" + "EAT", i.upper(), "to eat the", i + ".")

    print("What would you like to do?")


def is_valid_exit(exits, chosen_exit):
        return chosen_exit in exits

def print_help():
    print_specialised_words()


def execute_go(direction):
    global current_room
    if is_valid_exit(current_room["exits"], direction):
        for i, x in current_room["exits"].items():
            if i == direction:
                print("\n" + "-"*90 + "\n\nYou are moving to", spots[x]["name"].capitalize())
                current_room = spots[x]
    else:
        print("\n" + "-"*90 + "\n\nYou cannot go there.")


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
    elif is_valid_item(current_room["food"], item_id):
        for i in current_room["food"]:
            if i == item_id:
                inventory["food"].append(i)
                cRF.remove(i)
                print("\n" + "-"*90 + "\n\nYou took the", item_id.capitalize())
    else:
        print("\n" + "-"*90 + "\n\nYou cannot take that.")


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
                print("\n" + "-"*90 + "\n\nYou dropped the", item_id.capitalize())
    elif is_valid_item(inventory["food"], item_id):
        for i in inventory["food"]:
            if i == item_id:
                inventory["food"].remove(i)
                cRF.append(i)
                print("\n" + "-"*90 + "\n\nYou dropped the", item_id.capitalize())
    else:
        print("\n" + "-"*90 + "\n\nYou cannot drop that.")


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
                print("\n" + "-"*90 + "\n\nYou ate the", item_id.capitalize(), "which had", food[item_id]["energy"], "energy.")
    else:
        print("\n" + "-"*90 + "\n\nYou cannot eat that.")

def execute_taste(item_id):
    global inventory
    global current_room
    if is_valid_item(inventory["food"], item_id):
        for i in inventory["food"]:
            if i == item_id:
                print("\n" + "-"*90 + "\n\nYou tasted the", item_id.capitalize(), "and it is goooood. Also, it has", food[item_id]["energy"], "energy.")
    elif is_valid_item(inventory["tools"], item_id):
        for i in inventory["tools"]:
            if i == item_id:
                print("\n" + "-"*90 + "\n\nEwwww! Don't lick that, that is disgusting.")
    else:
        print("\n" + "-"*90 + "\n\nYou cannot taste that.")


def execute_command(command):
    if command[0] == "go" or command[0] == "move":
        if len(command[1]) >= 1:
            execute_go(command[1])
        elif len(command[1]) <= 1:
            print("\n" + "-"*90 + "\n\nGo where?")


    elif command[0] == "take" or command[0] == "pick up":
        if len(command[1]) >= 1:
            execute_take(command[1])
        elif len(command[1]) <= 1:
            print("\n" + "-"*90 + "\n\nTake what?")

    elif command[0] == "drop" or command[0] == "release":
        if len(command[1]) >= 1:
            execute_drop(command[1])
        elif len(command[1]) <= 1:
            print("\n" + "-"*90 + "\n\nDrop what?")

    elif command[0] == "eat":
        if len(command[1]) >= 1:
            execute_eat(command[1])
        elif len(command[1]) <= 1:
            print("\n" + "-"*90 + "\n\nEat what?")

    elif command[0] == "taste":
        if len(command[1]) >= 1:
            execute_taste(command[1])
        elif len(command[1]) <= 1:
            print("\n" + "-"*90 + "\n\nTaste what?")

    elif command[0] == "help":
            print_help()

    elif command[0] == "no" and len(command[1]) >= 1 :
        print("\n" + "-"*90 + "\n\nWhat would you like to do with the:", command[1].capitalize())

    elif command[0] == "no" and len(command[1]) <= 1 :
        print("\n" + "-"*90 + "\n\nPlease type something")

    else:
        print("\n" + "-"*90 + "\n\nThis makes no sense.")


def menu(exits, tools, food, inv):
    # Display menu
    print_menu(exits, tools, food, inv)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    # Next room to go to
    return spots[exits[direction]]


# This is the entry point of our program
def main():
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room, current_room["tools"], current_room["food"])
        print_player_info()

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["tools"], current_room["food"], inventory)
        # Execute the player's command
        execute_command(command)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()