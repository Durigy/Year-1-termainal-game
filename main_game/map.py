#from .spots import spots

road_library = {
    "name": "Herod Close",

    "description":
    """You are in a littered, dimly lit street;
blood plastered along the wall of Laboratory 1.
The Library - boarded up in an attempt to keep
the hoards out. They needn't bother, though, as
the end of the street is blocked off with a large,
stone gate long ago.""",

    "spots": {"library entrance": "l_entrance_hc", "entrance": "entrance_hc"},
}

road_lab1 = {
    "name": "Herod Street",

    "description":
    """You are standing in Herod Street, which
has undoubtedly seen better days. The air is
empty and cold - life beyond survival is
non-existent.""",

    "spots": {"lab 1 entrance": "lab1_entrance_hs", "carpark main str entrance": "ms_cp_entrance"}   
}

room_carpark = {
    "name": "Car Park",

    "description":
    "",

    "spots": {"cp lab 1 side entrance": "cp_lab1_side_entrance", "carpark entrance": "carpark_entrance", "car": "spot_car"},
    
}

room_lab1 = {
    "name": "Laboratory 1",

    "description":
    "",

    "spots": {"lab1 main entrance": "lab1_main_entrance", "lab 1 side entrance": "lab1_side_entrance", "desk": "spot_desk", "syringe cupboard": "syringe_cupboard"},
    
}

road_public = {
    "name": "Main Street",

    "description":
    """You are standing in Main Street - which
used to be full of life. It now stands eerily
still. You can't even hear the refugees in
the houses.""",

    "spots": {"shop front": "front_shop", "pub front": "front_pub", "alley front": "front_alley"},
    
}

room_shop = {
    "name" : "Shop",

    "description":
    "",

    "spots": {"shop entrance": "shop_entrance", "cleaning aisle": "cleaning_aisle"},
    
}

room_pub = {
    "name": "The Plough",

    "description":
    "",

    "spots": {"centre": "pub_centre", "behind bar": "behind_bar"},

}

room_alleyway = {
    "name": "Alleyway",

    "description":
    "",

    "spots": {"alley entrance": "alley_entrance", "pub back entrance": "pub_back_entrance"},
}

road_lab2 = {
    "name": "Isiah Road",

    "description":
    """You now stand in Isiah Street, broken down
and harrassed cars are dotted around the street. At
the end is another one of the stone gates - keeping
the undead out.""",

    "spots": {"centre": "ir_centre", "north centre": "north_ir_centre"},
}

room_lab2 = {
    "name": "Laboratory 2",

    "description":
    "",

    "spots": {"lab2 main entrance": "lab2_main_entrance", "tabletop": "spot_tabletop"},
    
}

room_contaminated_area = {
    "name": "Contaminated Area",

    "description":
    """You're now standing in a dingy room, light has
abandoned it, as the windows have been blackened out.
A single, gas-powered lamp allows you to see. In the
corner, held by chains, is a dead body. You step
forward to investigate, and it springs to life - an
undead. They clearly want to kill you, but cannot
with the chains holding them back.
This is supposed to be a safe haven! The undead aren't
supposed to be within the walls - so why is she here?
A second glance and you realise that the undead is, in
fact, Dr. Gavigan's wife...
Will you put her out of her misery?""",

    "spots": {"centre": "contam_area"}
}
    
room_park = {
    "name": "Willow Park",

    "description":
    "",
    
    "spots": {"park entrance": "park_entrance", "willow tree": "willow_tree", "p lab2 side entrance": "p_lab2_side_entrance"},
    
}

road_windy = {
    "name": "Windy Path",

    "description":
    """You are now walking along a windy, cobblestone
path. Beside you are a row of trees that have bloomed
in the lack of CO2 emissions - you even spot a pigeon
and her nest. There's a box by the fence build around
the houses, half-open.""",

    "spots": {"w centre": "windy_centre", "birds nest": "birds_nest", "box": "spot_box"},
    

}

room_library = {
    "name": "Library",

    "description":
    "",
    
    # A torch is needed to see in the mystery aisle.
    "spots": {"library side entrance": "l_side_entrance", "mystery aisle": "mystery_aisle"},
    
}

roads = {
    "herod close": road_library,
    "herod street": road_lab1,
    "main street": road_public,
    "isiah road": road_lab2,
    "windy path": road_windy,
    
}

rooms = {
    "laboratory 1": room_lab1,
    "car park": room_carpark,
    "shop": room_shop,
    "the plough": room_pub,
    "alleyway": room_alleyway,
    "library": room_library,
    "willow park": room_park,
    "laboratory 2": room_lab2,
    "contaminated area": room_contaminated_area
}
