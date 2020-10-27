from .items import tools, food
from .map import rooms, roads, spots

inventory = { # temporary testing inventory
    "tools": ["batteries"],
    "food": []
}

# Start game at the lab 1 spot 1
current_room = spots["s1 laboratory 1"]

player_addplayername0 = {
    "name": "Character1",
    "Occupation": "fill in",
    "Strength": "100",
    "Oxygen": "123",
    "Energy": "100",
    "inventory": {
        "tools": {},
        "food": {}
    }
}

player_addplayername1 = {
    "name": "Character1",
    "Occupation": "fill in",
    "Strength": "100",
    "Oxygen": "123",
    "Energy": "100",
    "inventory": {
        "tools": {},
        "food": {}
    }
}

player_addplayername2 = {
    "name": "Character1",
    "Occupation": "fill in",
    "Strength": "100",
    "Oxygen": "123",
    "Energy": "100",
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