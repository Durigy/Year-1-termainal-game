from .items import tools, food
from .map import rooms, roads
from .spots import spots

inventory = { # temporary testing inventory
    "energy": 10,
    "health": 1,
    "tools": ["batteries"],
    "food": ["mars bar"]
}

# Start game at the lab 1 spot 1
current_room = spots["lab2 centre"]

player_addplayername0 = {
    "name": "Character1",
    "occupation": "fill in",
    "strength": "100",
    "oxygen": "123",
    "energy": "100",
    "inventory": {
        "tools": {},
        "food": {}
    }
}

player_addplayername1 = {
    "name": "Character1",
    "occupation": "fill in",
    "strength": "100",
    "oxygen": "123",
    "energy": "100",
    "inventory": {
        "tools": {},
        "food": {}
    }
}

player_addplayername2 = {
    "name": "Character1",
    "occupation": "fill in",
    "strength": "100",
    "oxygen": "123",
    "energy": "100",
    "inventory": {
        "tools": {},
        "food": {}
    }
}

characters = {
    "addplayername0" : player_addplayername0,
    "addplayername1": player_addplayername1,
    "addplayername2": player_addplayername2
}