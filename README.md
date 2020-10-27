Team 6 Game Project!

Couple quick updates on what still needs to be completed:

Commands to be added:

"eat" command - will be similar to the ones that are already in place, with the exeception 
being that the keyword will have to be changed from take, go etc. to be "eat".

following that there will also have to be a function created called execute_eat:
This function will be what the user will have to regain energy, thus the item will be removed
from the users inventory using .remove(item name). Then take item_name["energy"] value and add
it onto the users current energy level. Note: energy can't go over a hundred so its going to 
have to be rounded off if it goes over 100.

"enter" command - will be the same method as the eat command.

Similarly again, the enter command is going to need a function execute_enter:
This will be pretty much the same as the already existing go function with the exeception that
you will be entering "spots" rather than rooms.

Mass:

Has been added into the dictionary of the items but still needs to be added into take/drop 
command, where item_id["mass"] is added/ subtracted from total respectively.

Integrating the map:

When the user interface has been completed the function simply has to be called in the main body
of the code (print_room) to be exact.

Potential addition of characters:

Dependent on time, but if there is spare the characters could be added into "spots" and then add
a dictionary with a character and a discription etc. (Maybe even items), or even you talk to the 
doctor first who assigns you tasks?

Integrating the mini games created:

This will go in the enter function, and before they are transfered you will call a minigame function
which the user has to complete to be let through/ enter the building.

ASCII art for start of game:

Completed by justin but a working UI is required still.



