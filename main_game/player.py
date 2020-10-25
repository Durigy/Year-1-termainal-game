from .items import tools, food
from .map import rooms, roads

inventory = tool["id"]

# Start game at the reception
current_room = rooms["laboratory 1"]

player_character = {
    "name": "Character1",
    "Occupation": "fill in",
    "Strength": "100",
    "Oxygen": "123",
    "Energy": "100",
    "inventory": []
}

player_character1 = {
    "name": "Character1",
    "Occupation": "fill in",
    "Strength": "100",
    "Oxygen": "123",
    "Energy": "100",
    "inventory": []
}

player_character2 = {
    "name": "Character1",
    "Occupation": "fill in",
    "Strength": "100",
    "Oxygen": "123",
    "Energy": "100",
    "inventory": []
}

characters = {
    "Character" : player_character,
    "Character1": player_character1,
    "Character2": player_character2
}