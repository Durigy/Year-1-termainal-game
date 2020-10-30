from .items import tools, food
from .map import rooms, roads
from .spots import spots

# This dictionary is used to hold the players data through out the game
inventory = {
    "energy": 10,
    "health": 1,
    "tools": [],
    "food": ["chocolate bar"]
}

# This variable stores location of where the player is and is used to determine the start location of the player on game load
current_spot = spots["lab2 main entrance"]
