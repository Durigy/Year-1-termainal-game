from .items import tools, food

# rooms --------------------------------------------------------------
room_carpark = {
    "name": "Car Park",

    "description":
    """You are standing in the desolate car park;
cars have begun to rust - unusable now the
necessities have been stripped from them. There
are three of them, a blue car, a silver car and
a black car.
You can go into Lab 1 through the side entrance to the west,
or make your way back north to Herod Street."""
}

room_lab1 = {
    "name": "Laboratory 1",

    "description":
    """You are now in the Lab 1 building,
it may be a bit dirty and dingy, but what
needs to be clean is clean. A old, blocky
laptop is sat on the desk - turned on. In
the lab, there is a chemical cupboard,
syringe cupboard, a bookshelf and a desk.
You can leave through the side entrance, into
the car park, or leave east onto Herod Street."""
}

# roads --------------------------------------------------------------
road_herod = {
    "name": "Herod Street",
    "description":
    """You are standing in front of Lab 1, which
has seen better days. The air is empty and cold -
life beyond survival is non-existent.
You can make your way to Lab 1, the car park or turn
east onto Main Street."""
}

# spots --------------------------------------------------------------
spot1_carpark = {
    "name": room_carpark["name"],

    "main description": room_carpark["description"],

    "description":
    """This is Car Park Spot #1.""",

    #"spot name": "",

    "exits": {"north" : "s2 laboratory 1", "south" : "s2 car park"},

    "tools": ["torch"],

    "food": []
}

spot2_carpark = {
    "name": room_carpark["name"],

    "main description": room_carpark["description"],

    "description":
    """This is Car Park Spot #2.""",

    #"spot name": "",

    "exits": {"east" : "s2 herod close", "north" : "s1 car park"},

    "tools": [],

    "food": ["salted crisps"]
}

spot1_lab1 = {
    "name": room_lab1["name"],

    "main description": room_lab1["description"],

    "description":
    """This is laboratory 1 Spot #1.""",

    #"spot name": "",

    "exits": {"east" : "s1 herod close", "south" : "s2 laboratory 1" },

    "tools": ["syringes bag", "torch"],

    "food": ["mars bar"]

    #"spots": [spot_lamppost],
    # Torch used to explore dark areas. Doesn't have batteries.
    # "items": [item_torch]
}

spot2_lab1 = {
    "name": room_lab1["name"],

    "main description": room_lab1["description"],

    "description":
    """This is laboratory 1 Spot #2.""",

    #"spot name": "",

    "exits": {"south" : "s1 car park", "north" : "s1 laboratory 1"},

    "tools": [],

    "food": []
}

spot1_herod = {
    "name": road_herod["name"],

    "main description" : road_herod["description"],

    #"spot name": "",

    "description":
    """This is Herod Close Spot #1.""",

    "exits": {"west" : "s1 laboratory 1", "south" : "s2 herod close"},

    "tools": [],

    "food": ["mars bar"]
}

spot2_herod = {
    "name": road_herod["name"],

    "main description": road_herod["description"],

    #"spot name": "",

    "description":
    """This is Herod Close Spot #2.""",

    "exits": {"west" : "s2 car park", "north" : "s2 herod close"},

    "tools": [],

    "food": []
}


rooms = {
    "laboratory 1": room_lab1,
    "car park": room_carpark,
}

roads = {
    "herod street": road_herod,
}

spots = {
    "s1 car park" : spot1_carpark,
    "s2 car park" : spot2_carpark,
    "s1 laboratory 1" : spot1_lab1,
    "s2 laboratory 1" : spot2_lab1,
    "s1 herod close" : spot1_herod,
    "s2 herod close" : spot2_herod,
}