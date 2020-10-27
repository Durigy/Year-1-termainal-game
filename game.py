#!/usr/bin/python3

from main_game import rooms, roads, spots, normalise_input, current_room, tools, food, inventory

def print_room_items(tools, food):
    temp = []  # room tools
    for i in tools:
        temp.append(i)
    rtool = ", ".join(temp)

    temp = []  # room food
    for i in food:
        temp.append(i)
    rfood = ", ".join(temp)

    if (rtool and rfood):
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

    if (itool and ifood):
        print("You have,", itool + ",", ifood + ", in your inventory.\n")
    elif itool:
        print("You have,", itool + ", in your inventory.\n")
    elif ifood:
        print("You have,", ifood + ", in your inventory.\n")
    else:
        print("You don't have anything in you inventory.\n")


def print_room(room, tools, food):
    print("\n------------------------------------------------------------------------------------------\n")
    print(room["name"].upper(), "\n")
    # Display room description
    print(room["description"], "\n")

    print_room_items(tools, food)


def exit_leads_to(exits, direction):
    return spots[exits[direction]]["name"]

def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")


def tool_is(exits, direction):
     return tools[exits[direction]]["name"]


def print_menu(exits, tools, food, inv):

    print("You can:")

    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for i in tools:
        print("TAKE", i.upper(), "to take", i + ".")

    for i in food:
        print("TAKE", i.upper(), "to take", i + ".")

    for i in inv["tools"]:
        print("DROP", i.upper(), "to take", i + ".")

    for i in inv["food"]:
        print("DROP", i.upper(), "to take", i + ".")

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
        return chosen_exit in exits


def execute_go(direction):
    global current_room
    if is_valid_exit(current_room["exits"], direction):
        for i, x in current_room["exits"].items():
            if i == direction:
                print("\n" + "You are moving to", spots[x]["name"])
                current_room = spots[x]
    else:
        print("\n" + "You cannot go there.")

def is_valid_tool(room_tools, chosen_tool):
    for a in room_tools:
        if chosen_tool == a:
            return True
    return False

def is_valid_food(room_food, chosen_food):
    for a in room_food:
        if chosen_food == a:
            return True
    return False

def execute_take(item_id):
    global inventory
    global current_room
    cRT = current_room["tools"]
    cRF = current_room["food"]
    if is_valid_tool(current_room["tools"], item_id):
        for i in current_room["tools"]:
            if i == item_id:
                inventory["tools"].append(i)
                cRT.remove(i)
                print("\n" + "You took the", item_id)
    elif is_valid_tool(current_room["food"], item_id):
        for i in current_room["food"]:
            if i == item_id:
                inventory["food"].append(i)
                cRF.remove(i)
                print("\n" + "You took the", item_id)
    else:
        print("\n" + "You cannot take that.")



def execute_drop(item_id):
    global inventory
    global current_room
    cRT = current_room["tools"]
    cRF = current_room["food"]
    if is_valid_tool(inventory["tools"], item_id):
        for i in inventory["tools"]:
            if i == item_id:
                inventory["tools"].remove(i)
                cRT.append(i)
                print("\n" + "You dropped the", item_id)
    elif is_valid_tool(inventory["food"], item_id):
        for i in inventory["food"]:
            if i == item_id:
                inventory["food"].remove(i)
                cRF.append(i)
                print("\n" + "You dropped the", item_id)
    else:
        print("\n" + "You cannot drop that.")

def execute_command(command):
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command[1]) >= 1:
            execute_go(command[1])
        elif len(command[1]) <= 1:
            print("\nGo where?")

    elif command[0] == "take":
        if len(command[1]) >= 1:
            execute_take(command[1])
        elif len(command[1]) <= 1:
            print("\nTake what?")

    elif command[0] == "drop":
        if len(command[1]) >= 1:
            execute_drop(command[1])
        elif len(command[1]) <= 1:
            print("\nDrop what?")

    elif command[0] == "no" and len(command[1]) >= 1 :
        print("\nPlease type something")
    else:
        print("\nThis makes no sense.")


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
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["tools"], current_room["food"], inventory)
        # Execute the player's command
        execute_command(command)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()