from .items import tools, food
from .map import rooms, roads

# These are npc which you meet and talk to in game

character_0 = {
    "name": "Dr. Gavigan",
    "Occupation": "Biological Scientist",
    "back story":
    """Dr. Gavigan is a brilliant but mad
scientist who's managed to survive the
world we current live in. He may have lost
his wife, but the work he's doing will
prevent the virus from spreading to
unbitten people ever again.""", 
    "inventory": []
}

character_1 = {
    "name": "Mrs. Gavigan",
    "Occupation": "Undead",
    "back story":
    """Mrs. Gavigan, in her life, was
married to Dr. Gavigan. But, like most
deaths now-a-days, she was bitten by one
of the undead and faced the price that
came with it. However, Dr. Gavigan
couldn't let her go - and here she remains.""", 
    "inventory": []
}

character_2 = {
    "name": "Finnegan",
    "Occupation": "Guard",
    "back story":
    """Finnegan was just a teen when the
virus began - he's lost his entire family.
As most people have, by this point. He's
sworn himself to keep the safe haven safe,
so that Dr. Gavigan can put an end to this
virus.""",
    "inventory": []
}

characters = {
    "Character" : character_0,
    "Character1": character_1,
    "Character2": character_2
}
