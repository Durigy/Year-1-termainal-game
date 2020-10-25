#!/usr/bin/python3

from main_game import rooms
from main_game import characters
from main_game import tools
from main_game import food
from main_game import normalise_input


def list_of_items(items):
    temp = []
    for i in items:
        temp.append(i["name"])
    return ", ".join(temp)


def print_room_items(room):
    if len(room["items"]) != 0:
        temp = []
        for i in room["items"]:
            temp.append(i["name"])
        result = ", ".join(temp)
        print("There is", result, "here." + "\n")


def print_inventory_items(items):
    if len(inventory) != 0:
        temp = []
        for i in inventory:
            temp.append(i["name"])
        result = ", ".join(temp)
        print("You have", result + "." + "\n")


def print_room(room):
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()

    print_room_items(room)

def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for i in room_items:
        print("TAKE", i["id"].upper(), "to take", i["name"] + ".")

    for i in inv_items:
        print("DROP", i["id"].upper(), "to drop", i["name"] + ".")

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


def execute_go(direction):
    global current_room
    if is_valid_exit(current_room["exits"], direction):
        for i, x in current_room["exits"].items():
            if i == direction:
                print("\n" + "You are moving to", rooms[x]["name"])
                current_room = rooms[x]
    else:
        print("\n" + "You cannot go there.")


def execute_take(item_id):
    global inventory
    global current_room
    cR = current_room["items"]
    found = False
    for i in cR:
        # print(i)
        for x, y in i.items():
            if x == "id":
                if y == item_id:
                    found = True
                    inventory.append(i)
                    cR.remove(i)

    if not found:
        print("\n" + "You cannot take that.")


def execute_drop(item_id):
    global inventory
    global current_room
    cR = current_room["items"]
    found = False
    for i in inventory:
        # print(i)
        for x, y in i.items():
            if x == "id":
                if y == item_id:
                    found = True
                    inventory.remove(i)
                    cR.append(i)

    if not found:
        print("\n" + "You cannot drop that.")


def execute_command(command):
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    # Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main():
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()