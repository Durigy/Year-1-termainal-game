def user_interface(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)


def header(room, lives, energy):

    length_remaining = 41 - len(room)
    left_remaining = 35 - len(energy)
    remaining = 34 - len(lives)
    text= "ROOM: " + room + " " * length_remaining + "ENERGY: " + energy + " " * left_remaining + "LIVES: " + lives + " " * remaining

    print (user_interface(text))

def show_inventory(inventory):
    #inventory = player_inventory["items"]
    show_inventory = True

    spaces_remaining = 130
    display_inv = ""
    split_inv = ""
    remaining = ""
    if show_inventory is True:
        
        for i in inventory:
            display_inv = display_inv +"," + i
            if len(display_inv) > 130:
                print("You can't hold that many items")
                
            elif len(i) < 130:
                spaces_remaining = spaces_remaining - len(display_inv)
                remaining = remaining + i + ", "
        left_spaces = 130 - (25 + len(remaining))       
        inventory_output = ("inventory (DROP/EAT/USE): " + remaining + split_inv + " " * left_spaces)
        print(user_interface(inventory_output.upper()))
        
def show_items_in_room(current_room_items):
    
    show_items_in_room = True

    spaces_remaining = 130
    display_room = ""
    split_inv = ""
    remaining = ""
    if show_items_in_room is True:
        
        for i in current_room_items:
            display_room = display_room +"," + i
            if len(display_room) > 130:
                spaces_remaining = spaces_remaining - len(display_room)
                remaining = remaining + i + ","
                
            elif len(i) < 130:
                spaces_remaining = spaces_remaining - len(display_room)
                remaining = remaining + i + ","
        left_spaces = 130 - (5 + len(remaining))       
        room_output = ("Take: " + remaining + split_inv + " " * left_spaces)
        print(user_interface(room_output.upper()))

        
def show_description(words):
    #text= room["main location"]
    words = words.split()
    i = 0
    split_sentences = ""
    text = ""
    line = " "
    remaining_spaces = 130
    for word in words:
                        
            text = text + " " + word
            if len(text) > 120:
                total_chars = len(text)
                remaining_spaces = 130 - total_chars - i
                total = 1 + i + len(text) + remaining_spaces      
                split_sentences = split_sentences + "\n" + text + " " * remaining_spaces + " "
                text = ""
            elif len(text) < 130:
                left_over = text
    text = (" ROOM DESCRIPTION: \n" + split_sentences + "\n" + left_over + " " * remaining_spaces)
    print(user_interface(text))



def footer(inventory, current_room_items, words):
    show_inventory(inventory)
    show_items_in_room(current_room_items)
    show_description(words)



