#from .spots import spots

road_library = {
    "name": "Herod Close",

    "description":
    """You are in a littered, dimly lit street;
blood plastered along the wall of Laboratory 1.
The Library - boarded up in an attempt to keep
the hoards out. They needn't bother, though, as
the end of the street is blocked off with a large,
stone gate long ago. A single lamppost, who produces
no light, stands in front of the library window.""",

    "spots": {"lamppost": "lamppost_herodclose", "centre": "herodclose_centre"},
}

road_lab1 = {
    "name": "Herod Street",

    "description":
    """You are standing in front of Lab 1, which
has seen better days. The air is empty and cold -
life beyond survival is non-existent.""",

    "spots": {"centre": "herodstreet_centre"}   
}

room_carpark = {
    "name": "Car Park",

    "description":
    """You are standing in the desolate car park;
cars have begun to rust - unusable now the
necessities have been stripped from them. The
closest to you is a blue car.""",

    "spots": {"side entrance": "lab1_side_entrance", "blue car": "blue_car", "silver car": "silver_car", "black car": "black_car", "centre": "carpark_centre"},
    
}

room_lab1 = {
    "name": "Laboratory 1",

    "description":
    """You are now in the Lab 1 building,
it may be a bit dirty and dingy, but what
needs to be clean is clean. A old, blocky
laptop is sat on the desk - turned on. In
the lab, there is a chemical cupboard,
syringe cupboard, a bookshelf and the side
entrance.""",

    "spots": {"chemical cupboard": "chemical_cupboard", "syringe cupboard": "syringe_cupboard", "desk": "spot_desk", "side entrance": "lab1_side_entrance", "bookshelf": "spot_bookshelf"},
    
}

road_public = {
    "name": "Main Street",

    "description":
    """You are standing in Main Street - which
used to be full of life. It now stands eerily
still. You can't even hear the refugees in
the houses.""",

    "spots": {"centre": "main_centre", "shop front": "front_shop", "binbag": "spot_binbag", "pub front": "front_pub", "alleyway front": "front_alley"},
    
}

room_shop = {
    "name" : "Shop",

    "description":
    """You're now standing in the
shop, at the entrance. A few of the
aisles are blocked, and some are just
clean empty.""",

    "spots": {"shop entrance": "shop_entrance", "crisps aisle": "crisps_aisle", "cleaning aisle": "cleaning_aisle", "cans aisle": "cans_aisle"},
    
}

room_pub = {
    "name": "The Plough",

    "description":
    """You are now inside the pub, where all the
expensive brands of the past have laid there,
relatively untouched. Now, you can go behind the
bar without having someone shout at you.""",

    "spots": {"centre": "pub_centre", "behind bar": "behind_bar"},

}

room_alleyway = {
    "name": "Alleyway",

    "description":
    """You are now in the alleyway, which
has likely never seen better days. At the far
end, there is a rustling noise in the industrial
bin that unsettles you greatly. For some
reason, there's an empty dog kennel by the
pub's back door.""",

    "spots": {"centre": "alley_centre", "bin": "industrial_bin", "dog kennel": "dog_kennel", "street entrance": "entrance_street"},
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
    """Standing in Lab 2, which is well-lit and tidy,
there is Dr. Gavigan in front of you,  madly writing
notes down that would likely be read in history books
in the distant future. In the lab, the only cupboard
you are not familiar with is the one at the top. In
the corner lays a tray, usually used for beakers.
There is a side entrance, which could take you to the
park.""",

    "spots": {"centre": "lab2_centre", "cupboard": "top_cupboard", "beaker tray": "beaker_tray", "side entrance": "side_entrance"},
    
}

room_park = {
    "name": "Willow Park",

    "description":
    """You are now in the once well-kept Willow Park.
Although no longer well-kept, nature and life was found
all around. A clear pond lies below an ancient looking
Willow tree that bends above it. A lone bench sits,
overlooking the now still pond. A hollybush lives in
the corner, and you're surprised to see a kitten playing
under it.""",
    
    "spots": {"centre": "park_centre", "bench": "spot_bench", "willow tree": "willow_tree", "side entrance": "lab2_side_entrance", "bush":  "spot_bush"},
    
}

road_windy = {
    "name": "Windy Path",

    "description":
    """You are now walking along a windy, cobblestone
path. Beside you are a row of trees that have bloomed
in the lack of CO2 emissions - you even spot a pigeon
and her nest. There's a box by someone's garden fence,
half-open. """,

    "spots": {"centre": "windy_centre", "tree": "tree_base", "birds nest": "birds_nest", "garden fence": "garden_fence"},
    

}

room_library = {
    "name": "Library",

    "description":
    """You are now inside the library - which
has a few toppled over bookshelves. They have been
collecting dust ever since the last residents left.
A smell of damp lingers in the air; the roof seems to
have been leaking. The mystery aisle is dark, you'd
need some light to be able to see it. The fiction aisle
is blocked off - someone must have made their last
stand in it. At least the non-fiction aisle is already
accessible for you.""",
    
    # A torch is needed to see in the non-fiction aisle.
    "spots": {"centre": "library_centre", "entrance": "library_entrance", "fiction": "fiction_aisle", "mystery": "mystery_aisle", "non-fiction": "nonfic_aisle"},
    
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
}
