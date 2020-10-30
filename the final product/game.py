#!/usr/bin/python3
from time import time
global run
global pub_code
from main_game import rooms, roads, spots, print_specialised_words, normalise_input, current_spot, tools, food, inventory, old_time, header, footer, info, access_code_minigame, scrambled_word

run = 0
pub_code = 0

# This function displays the current room/spot to the player
def print_room(room):
    header(room["name"].upper(), room["spot name"].upper(), str(inventory["health"]), str(energy_level()))
    print(room["map"])
    footer(inventory["tools"] + inventory["food"], room["tools"] + room["food"], room["description"])

# def exit_leads_to(exits, direction):
#     return spots[exits[direction]]["name"]

# This function works out how much energy and health the player has left
def energy_level():
    global inventory
    global old_time
    t = 45

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

    return inventory["energy"]

# This function determines where the given exit is real/exists or not
def is_valid_exit(exits, chosen_exit):
        return chosen_exit in exits

# This function displays the commands words on the screen for the user to see
def print_help():
    return print_specialised_words()

# This function determines if the player has the required item in their inventory to be able to move to that spot
def spot_item_needed(room):
    n = 0
    for i in spots[room]["items needed"]:
        for x in inventory["tools"]:
            if x == i:
                n += 1
    if n == len(spots[room]["items needed"]):
        return True
    elif len(spots[room]["items needed"]) == 0:
        return True
    else:
        return False

# This function moves the player around the maps from spot-to-spot
def execute_go(direction):
    global current_spot
    global run
    global pub_code

    if direction == "n":
        direction = "north"
    if direction == "e":
        direction = "east"
    if direction == "s":
        direction = "south"
    if direction == "w":
        direction = "west"

    if is_valid_exit(current_spot["exits"], direction):
        if spot_item_needed(current_spot["exits"][direction]):
            for i, x in current_spot["exits"].items():
                if i == direction and x == "lab 1 side entrance" or i == direction and x == "lab1 main entrance":
                    if run == 0:
                        access_code_minigame()
                        if True:
                            if i == direction:
                                run += 1
                                current_spot = spots[x]
                        else:
                            return
                    elif i == direction:
                        current_spot = spots[x]

                elif i == direction and x == "pub centre":  # or i == direction and x == "alley front":
                    if pub_code == 0:
                        scrambled_word()
                        if True:
                            if i == direction:
                                pub_code += 1
                                current_spot = spots[x]
                        else:
                            return
                    elif i == direction:
                        current_spot = spots[x]
                elif i == direction:
                    current_spot = spots[x]
                    pass
                elif i == direction:
                    current_spot = spots[x]
        else:
            info("You cannot go there with out the correct equipment.", 86, 85)
    else:
        info("You cannot go there.", 70, 70)

# This function check if the given item is a real one and returns if it is or not
def is_valid_item(room_item, chosen_item):
    for a in room_item:
        if chosen_item == a:
            return True
    return False

# This function check is the player's inventory is Full or not
def is_inventory_full():
    if len(inventory["tools"]+inventory["food"]) == 8:
        return True
    else:
        return False

# This function checks if the desired spot requires an item to move to it
def is_spot_critical(item):
    for i in current_spot["items needed"]:
        if item == i:
            return True
    return False

# This function removes the desired item from the spot location and places it in the player's inventory
def execute_take(item_id):
    global inventory
    global current_spot
    cRT = current_spot["tools"]
    cRF = current_spot["food"]
    if is_valid_item(current_spot["tools"], item_id):
        if not is_inventory_full():
            for i in current_spot["tools"]:
                if i == item_id:
                    inventory["tools"].append(i)
                    cRT.remove(i)
        elif is_inventory_full():
            info("You're not that strong, you can't carry any more items.", 85, 84)
    elif is_valid_item(current_spot["food"], item_id):
        if not is_inventory_full():
            for i in current_spot["food"]:
                if i == item_id:
                    inventory["food"].append(i)
                    cRF.remove(i)
        elif is_inventory_full():
            info("You're not that strong, you can't carry any more items.", 85, 84)
    else:
        info("You cannot take that.", 71, 70)

# This function removes the desired item from the player's inventory and places it in the spot location
def execute_drop(item_id):
    global inventory
    global current_spot
    cRT = current_spot["tools"]
    cRF = current_spot["food"]
    if is_valid_item(inventory["tools"], item_id):
        if not is_spot_critical(item_id):
            for i in inventory["tools"]:
                if i == item_id:
                    inventory["tools"].remove(i)
                    cRT.append(i)
        else:
            info("That item is too valuable, you can't drop it here.", 85, 85)
    elif is_valid_item(inventory["food"], item_id):
        if not is_spot_critical(item_id):
            for i in inventory["food"]:
                if i == item_id:
                    inventory["food"].remove(i)
                    cRF.append(i)
        else:
            info("That item is too valuable, you can't drop it here.", 86, 85)
    else:
        info("You cannot drop that.", 71, 70)

# This function removes the desired food item from the player's inventory and increases the energy upto a maximum of 10
def execute_eat(item_id):
    global inventory
    if is_valid_item(inventory["food"], item_id):
        for i in inventory["food"]:
            if i == item_id:
                inventory["food"].remove(i)
                if inventory["energy"] < 10:
                    if (inventory["energy"] + food[item_id]["energy"]) > 10:
                        inventory["energy"] = 10
                    else:
                        inventory["energy"] += food[item_id]["energy"]
    else:
        info("You cannot eat that.", 70, 70)

# This function allows the player to tell how much energy a desired food item contains
def execute_taste(item_id):
    global inventory
    global current_spot
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

# This function checks what command has been typed in
def execute_command(command):
    if command[0] == "go" or command[0] == "move":
        if len(command[1]) >= 1:
            execute_go(command[1])
        elif len(command[1]) <= 1:
            info("Go where?", 65, 64)


    elif command[0] == "take" or command[0] == "pick up":
        if len(command[1]) >= 1:
            execute_take(command[1])
        elif len(command[1]) <= 1:
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
            info("Eat what?", 65, 64)

    elif command[0] == "taste":
        if len(command[1]) >= 1:
            execute_taste(command[1])
        elif len(command[1]) <= 1:
            info("Taste what?", 66, 65)

    elif command[0] == "help":
        info("These are the commands you can type to use: " + print_help(), 114, 114)

    elif command[0] == "exit":
        check = normalise_input(input("Are you sure you want to exit the game. You will lose everything. (YES/NO): "), False)
        if check == "yes":
            death_screen()
        elif len(check) >= 0:
            info("The Game Continues", 69, 69)

    elif command[0] == "no" and len(command[1]) >= 1 :
        info("What would you like to do with that item?", 81, 80)

    elif command[0] == "no" and len(command[1]) <= 1 :
        info("Please type something useful", 74, 74)

    else:
        info("This makes no sense.", 70, 70)

# This function deals with the player's input and talks to the game_parser.py module
def user_input():
    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input

# This function returns the spot the player will move to
def move(exits, direction):
    # Next spot to go to
    return spots[exits[direction]]

# This function displays the Game over screen
def death_screen():
    #this_time = time()
    text = """
    
       
       
       
       
       
       
                                                                                                                                                                                            
                                    
                                                                                                                                                                     
                            CCCCCCCCCCCCC                                                                                                      tttt                           
                         CCC::::::::::::C                                                                                                   ttt:::t                           
                       CC:::::::::::::::C                                                                                                   t:::::t                           
                      C:::::CCCCCCCC::::C                                                                                                   t:::::t                           
                     C:::::C       CCCCCC   ooooooooooo   nnnn  nnnnnnnn       ggggggggg   gggggrrrrr   rrrrrrrrr     aaaaaaaaaaaaa   ttttttt:::::ttttttt        ssssssssss   
                    C:::::C               oo:::::::::::oo n:::nn::::::::nn    g:::::::::ggg::::gr::::rrr:::::::::r    a::::::::::::a  t:::::::::::::::::t      ss::::::::::s  
                    C:::::C              o:::::::::::::::on::::::::::::::nn  g:::::::::::::::::gr:::::::::::::::::r   aaaaaaaaa:::::a t:::::::::::::::::t    ss:::::::::::::s 
                    C:::::C              o:::::ooooo:::::onn:::::::::::::::ng::::::ggggg::::::ggrr::::::rrrrr::::::r           a::::a tttttt:::::::tttttt    s::::::ssss:::::s
                    C:::::C              o::::o     o::::o  n:::::nnnn:::::ng:::::g     g:::::g  r:::::r     r:::::r    aaaaaaa:::::a       t:::::t           s:::::s  ssssss 
                    C:::::C              o::::o     o::::o  n::::n    n::::ng:::::g     g:::::g  r:::::r     rrrrrrr  aa::::::::::::a       t:::::t             s::::::s      
                    C:::::C              o::::o     o::::o  n::::n    n::::ng:::::g     g:::::g  r:::::r             a::::aaaa::::::a       t:::::t                s::::::s   
                     C:::::C       CCCCCCo::::o     o::::o  n::::n    n::::ng::::::g    g:::::g  r:::::r            a::::a    a:::::a       t:::::t    ttttttssssss   s:::::s 
                      C:::::CCCCCCCC::::Co:::::ooooo:::::o  n::::n    n::::ng:::::::ggggg:::::g  r:::::r            a::::a    a:::::a       t::::::tttt:::::ts:::::ssss::::::s
                       CC:::::::::::::::Co:::::::::::::::o  n::::n    n::::n g::::::::::::::::g  r:::::r            a:::::aaaa::::::a       tt::::::::::::::ts::::::::::::::s 
                         CCC::::::::::::C oo:::::::::::oo   n::::n    n::::n  gg::::::::::::::g  r:::::r             a::::::::::aa:::a        tt:::::::::::tt s:::::::::::ss  
                            CCCCCCCCCCCCC   ooooooooooo     nnnnnn    nnnnnn    gggggggg::::::g  rrrrrrr              aaaaaaaaaa  aaaa          ttttttttttt    sssssssssss    
                                                                                        g:::::g                                                                               
                                                                            gggggg      g:::::g                                                                               
                                                                            g:::::gg   gg:::::g                                                                               
                                                                             g::::::ggg:::::::g                                                                               
                                                                              gg:::::::::::::g                                                                                
                                                                                ggg::::::ggg                                                                                  
                                                                                   gggggg                                                                                     
                                                                                                                                                                              
                                                                                                                                                                              
                    YYYYYYY       YYYYYYY                                        LLLLLLLLLLL                                                        tttt                !!!   
                    Y:::::Y       Y:::::Y                                        L:::::::::L                                                     ttt:::t               !!:!!  
                    Y:::::Y       Y:::::Y                                        L:::::::::L                                                     t:::::t               !:::!  
                    Y::::::Y     Y::::::Y                                        LL:::::::LL                                                     t:::::t               !:::!  
                    YYY:::::Y   Y:::::YYY   ooooooooooo   uuuuuu    uuuuuu         L:::::L                  ooooooooooo       ssssssssss   ttttttt:::::ttttttt         !:::!  
                       Y:::::Y Y:::::Y    oo:::::::::::oo u::::u    u::::u         L:::::L                oo:::::::::::oo   ss::::::::::s  t:::::::::::::::::t         !:::!  
                        Y:::::Y:::::Y    o:::::::::::::::ou::::u    u::::u         L:::::L               o:::::::::::::::oss:::::::::::::s t:::::::::::::::::t         !:::!  
                         Y:::::::::Y     o:::::ooooo:::::ou::::u    u::::u         L:::::L               o:::::ooooo:::::os::::::ssss:::::stttttt:::::::tttttt         !:::!  
                          Y:::::::Y      o::::o     o::::ou::::u    u::::u         L:::::L               o::::o     o::::o s:::::s  ssssss       t:::::t               !:::!  
                           Y:::::Y       o::::o     o::::ou::::u    u::::u         L:::::L               o::::o     o::::o   s::::::s            t:::::t               !:::!  
                           Y:::::Y       o::::o     o::::ou::::u    u::::u         L:::::L               o::::o     o::::o      s::::::s         t:::::t               !!:!!  
                           Y:::::Y       o::::o     o::::ou:::::uuuu:::::u         L:::::L         LLLLLLo::::o     o::::ossssss   s:::::s       t:::::t    tttttt      !!!   
                           Y:::::Y       o:::::ooooo:::::ou:::::::::::::::uu     LL:::::::LLLLLLLLL:::::Lo:::::ooooo:::::os:::::ssss::::::s      t::::::tttt:::::t            
                        YYYY:::::YYYY    o:::::::::::::::o u:::::::::::::::u     L::::::::::::::::::::::Lo:::::::::::::::os::::::::::::::s       tt::::::::::::::t      !!!   
                        Y:::::::::::Y     oo:::::::::::oo   uu::::::::uu:::u     L::::::::::::::::::::::L oo:::::::::::oo  s:::::::::::ss          tt:::::::::::tt     !!:!!  
                        YYYYYYYYYYYYY       ooooooooooo       uuuuuuuu  uuuu     LLLLLLLLLLLLLLLLLLLLLLLL   ooooooooooo     sssssssssss              ttttttttttt        !!!   


    
       
       
       
       
       
       
                                                                                                                                                                                            
                                                                                                                                                                                                                   
"""
    print(text)
    #if (time() - this_time) == 10:
    exit()

# This function check if the player has won and call the Winning screen function
def game_won():
    n = 0
    final_items = ["substance1", "substance2", "substance3", "laptop", "beakers", "syringes bag", "cleaning product"]
    for i in spots["tabletop"]["tools"]:
        for x in final_items:
            if x == i:
                n += 1
        if n == 7:
            win_screen()
    return

# This function displays the Winning screen
def win_screen():
    text = """
    
    
    
    
    
    
    
    
    
       
       
       
       
       
       
       
       
       
       
       
                                                                                                                                                                                            
                                                                                                                                              
                YYYYYYY       YYYYYYY                                        WWWWWWWW                           WWWWWWWW  iiii                          !!! 
                Y:::::Y       Y:::::Y                                        W::::::W                           W::::::W i::::i                        !!:!!
                Y:::::Y       Y:::::Y                                        W::::::W                           W::::::W  iiii                         !:::!
                Y::::::Y     Y::::::Y                                        W::::::W                           W::::::W                               !:::!
                YYY:::::Y   Y:::::YYY   ooooooooooo   uuuuuu    uuuuuu        W:::::W           WWWWW           W:::::W iiiiiii nnnn  nnnnnnnn         !:::!
                   Y:::::Y Y:::::Y    oo:::::::::::oo u::::u    u::::u         W:::::W         W:::::W         W:::::W  i:::::i n:::nn::::::::nn       !:::!
                    Y:::::Y:::::Y    o:::::::::::::::ou::::u    u::::u          W:::::W       W:::::::W       W:::::W    i::::i n::::::::::::::nn      !:::!
                     Y:::::::::Y     o:::::ooooo:::::ou::::u    u::::u           W:::::W     W:::::::::W     W:::::W     i::::i nn:::::::::::::::n     !:::!
                      Y:::::::Y      o::::o     o::::ou::::u    u::::u            W:::::W   W:::::W:::::W   W:::::W      i::::i   n:::::nnnn:::::n     !:::!
                       Y:::::Y       o::::o     o::::ou::::u    u::::u             W:::::W W:::::W W:::::W W:::::W       i::::i   n::::n    n::::n     !:::!
                       Y:::::Y       o::::o     o::::ou::::u    u::::u              W:::::W:::::W   W:::::W:::::W        i::::i   n::::n    n::::n     !!:!!
                       Y:::::Y       o::::o     o::::ou:::::uuuu:::::u               W:::::::::W     W:::::::::W         i::::i   n::::n    n::::n      !!! 
                       Y:::::Y       o:::::ooooo:::::ou:::::::::::::::uu              W:::::::W       W:::::::W         i::::::i  n::::n    n::::n          
                    YYYY:::::YYYY    o:::::::::::::::o u:::::::::::::::u               W:::::W         W:::::W          i::::::i  n::::n    n::::n      !!! 
                    Y:::::::::::Y     oo:::::::::::oo   uu::::::::uu:::u                W:::W           W:::W           i::::::i  n::::n    n::::n     !!:!!
                    YYYYYYYYYYYYY       ooooooooooo       uuuuuuuu  uuuu                 WWW             WWW            iiiiiiii  nnnnnn    nnnnnn      !!! 
                                                                                                                                                                                            
           
           
           
           
           
                                                                                                                                                                                            
              
              
          
          
          
          
          
          
          
          
          
          
                                                                                                                                                                                            
                                                                                                                                                                                            
                                                                                                                                                                                            
                                                                                                                                                                                            
                                                                                                                                                                                            
"""
    print(text)
    exit()

# This function checks what difficulty the play wants to play at and sent the help level appropriately
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

# This function displays the Start screen
def display_head():
    head = """
    
    
    
    
    
    
    
       
       
       
       
       
       
       
       
       
       
       
       
                                                                                                                                                                                            
                                                                                                                                                                                            
                   SSSSSSSSSSSSSSS                       ffffffffffffffff                           HHHHHHHHH     HHHHHHHHH                                                                                 
                 SS:::::::::::::::S                     f::::::::::::::::f                          H:::::::H     H:::::::H                                                                                 
                S:::::SSSSSS::::::S                    f::::::::::::::::::f                         H:::::::H     H:::::::H                                                                                 
                S:::::S     SSSSSSS                    f::::::fffffff:::::f                         HH::::::H     H::::::HH                                                                                 
                S:::::S              aaaaaaaaaaaaa     f:::::f       ffffff    eeeeeeeeeeee           H:::::H     H:::::H    aaaaaaaaaaaaa   vvvvvvv           vvvvvvv    eeeeeeeeeeee    nnnn  nnnnnnnn    
                S:::::S              a::::::::::::a    f:::::f               ee::::::::::::ee         H:::::H     H:::::H    a::::::::::::a   v:::::v         v:::::v   ee::::::::::::ee  n:::nn::::::::nn  
                 S::::SSSS           aaaaaaaaa:::::a  f:::::::ffffff        e::::::eeeee:::::ee       H::::::HHHHH::::::H    aaaaaaaaa:::::a   v:::::v       v:::::v   e::::::eeeee:::::een::::::::::::::nn 
                  SS::::::SSSSS               a::::a  f::::::::::::f       e::::::e     e:::::e       H:::::::::::::::::H             a::::a    v:::::v     v:::::v   e::::::e     e:::::enn:::::::::::::::n
                    SSS::::::::SS      aaaaaaa:::::a  f::::::::::::f       e:::::::eeeee::::::e       H:::::::::::::::::H      aaaaaaa:::::a     v:::::v   v:::::v    e:::::::eeeee::::::e  n:::::nnnn:::::n
                       SSSSSS::::S   aa::::::::::::a  f:::::::ffffff       e:::::::::::::::::e        H::::::HHHHH::::::H    aa::::::::::::a      v:::::v v:::::v     e:::::::::::::::::e   n::::n    n::::n
                            S:::::S a::::aaaa::::::a   f:::::f             e::::::eeeeeeeeeee         H:::::H     H:::::H   a::::aaaa::::::a       v:::::v:::::v      e::::::eeeeeeeeeee    n::::n    n::::n
                            S:::::Sa::::a    a:::::a   f:::::f             e:::::::e                  H:::::H     H:::::H  a::::a    a:::::a        v:::::::::v       e:::::::e             n::::n    n::::n
                SSSSSSS     S:::::Sa::::a    a:::::a  f:::::::f            e::::::::e               HH::::::H     H::::::HHa::::a    a:::::a         v:::::::v        e::::::::e            n::::n    n::::n
                S::::::SSSSSS:::::Sa:::::aaaa::::::a  f:::::::f             e::::::::eeeeeeee       H:::::::H     H:::::::Ha:::::aaaa::::::a          v:::::v          e::::::::eeeeeeee    n::::n    n::::n
                S:::::::::::::::SS  a::::::::::aa:::a f:::::::f              ee:::::::::::::e       H:::::::H     H:::::::H a::::::::::aa:::a          v:::v            ee:::::::::::::e    n::::n    n::::n
                 SSSSSSSSSSSSSSS     aaaaaaaaaa  aaaa fffffffff                eeeeeeeeeeeeee       HHHHHHHHH     HHHHHHHHH  aaaaaaaaaa  aaaa           vvv               eeeeeeeeeeeeee    nnnnnn    nnnnnn
                                                                                                                                                                                            
           
           
           
           
                                                                                                                                                                                            
              
              
          
          
          
          
          
          
          
          
          
          
                                                                                                                                                                                            
                                                                                                                                                                                            
                                                                                                                                                                                            
                                                                                                                                                                                            
                                                                                                                                                                                            
"""
    print(head)

# This is the entry point of our program
def main():
    # This part displays the start screen
    display_head()

    # This part loops until the player picks a valid difficulty level
    dif_chosen = False
    while not dif_chosen:
        dif_chosen = difficulty(normalise_input(input("Please choose a difficulty: EASY, MEDIUM or HARD: "), False))

    # Main game loop
    while int(inventory["health"]) > 0:
        print_room(current_spot)

        # Execute the player's command
        execute_command(user_input())

        game_won()
    if int(inventory["health"]) <= 0:
        death_screen()


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

