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
or make your way back north to Herod Street.""",

    "exits": {"lab 1": "Laboratory 1", "north": "Herod Street"},

    #"spots": [lab1_side_entrance, blue_car, silver_car, black_car, carpark_centre],
    # A bag of syringes used to applicate the vaccine.
    # Batteries for torch
    "tools": {"syringes bag": "item_syringes_bag", "batteries": "item_batteries"} #,

    # "food": {"lab 1": "Laboratory 1", "north": "Herod Street"}

    # "passcode": [passcode_lab1]
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
the car park, or leave east onto Herod Street.""",

    "exits": {"carpark": "Car Park", "east": "Herod Street"}#,

    #"spots": [chemical_cupboard, syringe_cupboard, desk, side_entrance, bookshelf],
    # item_paper_passcode could perhaps be a piece of paper that tells the passcode to lab 2? Accessible via minigame
    # item_laptop is how we opened the game to talk to the scientist. Doesn't need to be taken. passcode for lab 1 is on there.
    # item_substance1 is vital for the creation of vaccine.
    #"items": [item_laptop, item_substance1, item_paper_passcode],

    # "passcode": []
}

room_shop = {
    "name" : "Shop",

    "description":
    """You are standing in the shop, the shelves
lay empty of long-life products, and only a few
household products remain. There are three aisles
that seem to have some things in it; the crisps
aisle, the cleaning products aisle and the -
surprisingly - canned goods aisle.
The only available exit of thee store is north
onto Main Street.""",

    "exits": {"north": "Main Street"}#,

    #"spots": [crisps_aisle, cleaning_aisle, cans_aisle],
    # Sterilisation
    #"items": [item_cleaning_product, item_batteries]
}

room_pub = {
    "name": "The Plough",

    "description":
    """You are now inside the pub, where all the
expensive brands of the past have laid there,
relatively untouched. Now, you can go behind the
bar without having someone shout at you.
To leave, you can either go onto north Main Street or
go into the alleyway.""",

    "exits": {"north": "Main Street", "alleyway": "Alleyway"}#,

    #"spots": [pub_centre, behind_bar],
    # Alternative sterilisation
    #"items": [item_vodka]
}

room_alleyway = {
    "name": "Alleyway",

    "description":
    """You are now in the alleyway, which
has likely never seen better days. At the far
end, there is a rustling noise in the industrial
bin that unsettles you greatly. For some
reason, there's an empty dog kennel by the
pub's back door.
You can either leave north onto Main Street, or go
into the pub through the back entrance.""",

    "exits": {"pub": "The Plough", "north": "Main Street"}#,

    #"spots": [alley_centre, industrial_bin, dog_kennel],
    # item_axe = another weapon. item_notebook could be vital dr's notes.
    #"items": [item_axe, item_notebook],

    # "passcode": []
}

room_lab2 = {
    "name": "Laboratory 2",

    "description":
    """Standing in Lab 2, which is well-lit and tidy,
there is Dr. Gavigan in the corner,  madly writing
notes down that would likely be read in history books
in the distant future. In the lab, the only cupboard
you are not familiar with is the one at the top. In
the corner lays a tray, usually used for beakers.
There is a side entrance, which could take you to the
park.
To leave, you can leave from where you came - Isiah
Road in the west.""",

    "exits": {"west": "Isiah Road"}#,

    #"spots": [lab2_centre, top_cupboard, beaker_tray, lab2_side_entrance],
    # Beakers used in making the vaccine.
    #"items": [item_beakers],

    # "passcode": []
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
under it.
The side entrance to Lab 2 is closed off by overgrown
shrubbery, so you can only leave west back onto Isiah Road.""",

    "exits": {"west": "Isiah Road"}#,

    #"spots": [park_centre, bench, willow_tree, lab2_side_entrance, bush],

    # An old watch that contains a picture of the scientist n his late wife.
    # Becomes important if you look in the corner - where the side entrance is.
    # "items": [item_watch]
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
accessible for you.
You can only leave east onto the windy path, as the front
entrance has been boarded up.""",

    "exits": {"east": "Windy Path"}#,
    # An axe is needed to break down a barrier made in the past to access the fiction_aisle.
    #"spots": [library_entrance, fiction_aisle, mystery_aisle, nonfic_aisle],

    # Substance 3, used in vaccine.
    # Batteries for torch.
    # Torch can then be used to check dark corner (aka nonfic_aisle)
    # "items": [item_substance3, item_batteries]
}



# roads --------------------------------------------------------------
road_library = {
    "name": "Herod Close",

    "description":
    """You are in a littered, dimly lit street;
blood plastered along the wall of Laboratory 1.
The Library - boarded up in an attempt to keep
the hoards out. They needn't bother, though, as
the end of the street is blocked off with a large,
stone gate long ago. A single lamppost, who produces
no light, stands in front of the library window.
You can only turn back East onto Herod Street.""",

    "exits": {"east" : "Herod Street"}#,

    # "spots": [spot_lamppost],

    # Torch used to explore dark areas. Doesn't have batteries.
    # "items": [item_torch]
}

road_lab1 = {
    "name": "Herod Street",

    "description":
    """You are standing in front of Lab 1, which
has seen better days. The air is empty and cold -
life beyond survival is non-existent.
You can make your way to Lab 1, the carpark or turn
east onto Main Street.""",

    "exits":  {"carpark": "Car Park", "lab 1": "Laboratory 1", "east": "Main Street"}#,

    # "passcode": [passcode_lab1]
}

road_public = {
    "name": "Main Street",

    "description":
    """You are standing in Main Street - which
used to be full of life. To your left, a row of
houses - now occupied by refugees that pray for
a vaccine. There is a bin-bag with a peculiar
wooden handle sticking out.
You can go into the shop, the pub next to it or
the alleyway. You can go west onto Herod Street
or north onto Isiah Road.""",

    "exits": {"shop": "Shop", "pub": "The Plough", "alleyway": "Alleyway", "north": "Isiah Road", "west": "Herod Street"}#,

    #"spots": [main_centre, binbag],

    # Could be used as a weapon/to break through somewhere.
    # "items": [item_hammer]
}

road_lab2 = {
    "name": "Isiah Road",

    "description":
    """You now stand in Isiah Street, broken down
and harrassed cars are dotted around the street. At
the end is another one of the stone gates - keeping
the undead out.
You can either enter Lab 2, if you have the necessary
passcode, enter the park or go west down a windy path behind
the houses.""",

    "exits": {"lab 2": "Laboratory 2", "park": "Willow Park", "west": "Windy Path"}#,

    # "passcode": [passcode_lab2]
}


road_windy = {
    "name": "Windy Path",

    "description":
    """You are now walking along a windy, cobblestone
path. Beside you are a row of trees that have bloomed
in the lack of CO2 emissions - you even spot a pigeon
and her nest. There's a box by someone's garden fence,
half-open. 
You can go into the library, or east onto Isiah Road.""",

    "exits": {"library": "Library", "east": "Isiah Road"}#,

    #"spots": [windy_centre, tree_base, birds_nest, garden_fence],
    # Substance 2, used in vaccine.
    # "items": [item_substance2]

}

# spots --------------------------------------------------------------
# road_library = {
#     "name": "Herod Close",
#
#     "description":
#     """You are in a littered, dimly lit street;
# blood plastered along the wall of Laboratory 1.
# The Library - boarded up in an attempt to keep
# the hoards out. They needn't bother, though, as
# the end of the street is blocked off with a large,
# stone gate long ago. A single lamppost, who produces
# no light, stands in front of the library window.
# You can only turn back East onto Herod Street.""",
#
#     "exits": {"east" : "Herod Street"},
#
#     #"spots": [spot_lamppost],
#     # Torch used to explore dark areas. Doesn't have batteries.
#     "items": [item_torch]
# }
#
# road_lab1 = {
#     "name": "Herod Street",
#
#     "description":
#     """You are standing in front of Lab 1, which
# has seen better days. The air is empty and cold -
# life beyond survival is non-existent.
# You can make your way to Lab 1, the carpark or turn
# east onto Main Street.""",
#
#     "exits":  {"carpark": "Car Park", "lab 1": "Laboratory 1", "east": "Main Street"},
#
#     "passcode": [passcode_lab1]
# }
#
# road_public = {
#     "name": "Main Street",
#
#     "description":
#     """You are standing in Main Street - which
# used to be full of life. To your left, a row of
# houses - now occupied by refugees that pray for
# a vaccine. There is a bin-bag with a peculiar
# wooden handle sticking out.
# You can go into the shop, the pub next to it or
# the alleyway. You can go west onto Herod Street
# or north onto Isiah Road.""",
#
#     "exits": {"shop": "Shop", "pub": "The Plough", "alleyway": "Alleyway", "north": "Isiah Road", "west": "Herod Street"},
#
#     #"spots": [main_centre, binbag],
#     # Could be used as a weapon/to break through somewhere.
#     "items": [item_hammer]
# }
#
# road_lab2 = {
#     "name": "Isiah Road",
#
#     "description":
#     """You now stand in Isiah Street, broken down
# and harrassed cars are dotted around the street. At
# the end is another one of the stone gates - keeping
# the undead out.
# You can either enter Lab 2, if you have the necessary
# passcode, enter the park or go west down a windy path behind
# the houses.""",
#
#     "exits": {"lab 2": "Laboratory 2", "park": "Willow Park", "west": "Windy Path"},
#
#     "passcode": [passcode_lab2]
# }
#
#
# road_windy = {
#     "name": "Windy Path",
#
#     "description":
#     """You are now walking along a windy, cobblestone
# path. Beside you are a row of trees that have bloomed
# in the lack of CO2 emissions - you even spot a pigeon
# and her nest. There's a box by someone's garden fence,
# half-open.
# You can go into the library, or east onto Isiah Road.""",
#
#     "exits": {"library": "Library", "east": "Isiah Road"},
#
#     #"spots": [windy_centre, tree_base, birds_nest, garden_fence],
#     # Substance 2, used in vaccine.
#     "items": [item_substance2]
#
# }


rooms = {
    "laboratory 1": room_lab1,
    "car park": room_carpark,
    "shop": room_shop,
    "the plough": room_pub,
    "alleyway": room_alleyway,
    "library": room_library,
    "willow park": room_park,
    "laboratory 2": room_lab2
}

roads = {
    "Herod Close": road_library,
    "Herod Street": road_lab1,
    "Main Street": road_public,
    "Isiah Road": road_lab2,
    "Windy Path": road_windy
}

spots = {
    # "laboratory 1": room_lab1,
    # "car park": room_carpark,
    # "shop": room_shop,
    # "the plough": room_pub,
    # "alleyway": room_alleyway,
    # "library": room_library,
    # "willow park": room_park,
    # "laboratory 2": room_lab2
}