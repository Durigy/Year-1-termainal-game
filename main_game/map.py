from items import *

road_library = {
    "name": "Herod Close",

    "description":
    """You are in a littered, dimly lit street;
blood plastered along the wall of Labratory 1.
The Library - boarded up in an attempt to keep
the hoards out. They needn't bother, though, as
the end of the street is blocked off with a large,
stone gate long ago.
You can only turn back onto Herod Street.""",

    "exits": {"herod street" : "Herod Street"},

    "items": []
}

road_lab1 = {
    "name": "Herod Street",

    "description":
    """You are standing in front of Lab 1, which
has seen better days. The air is empty and cold -
life beyond surival is non-existent.
You can make your way to Lab 1, the carpark or turn
onto Main Street.""",

    "exits":  {"carpark": "Carpark", "lab 1": "Labratory 1", "main street": "Main Street"},

    "items": []

    "passcode": []
}

room_carpark = {
    "name": "Carpark",

    "description":
    """You are standing in the desolate carpark;
cars have begun to rust - useless now the
necessities have been stripped from them.
You can go into Lab 1 through the side entrance,
or make your way back to Herod Street.""",

    "exits": {"lab 1": "Labratory 1", "herod street": "Herod Street"},

    "items": [],

    "passcode": []
}

room_lab1 = {
    "name": "Labratory 1",

    "description":
    """You are now in the Lab 1 building,
it may be a bit dirty and dingy, but what
needs to be clean is clean. A old, blocky
laptop is sat on the desk - turned on.
You can leave through the side entrance, into
the carpark, or leave onto Herod Street.""",

    "exits": {"carpark": "Carpark", "herod street": "Herod Street"},

    "items": [],

    "passcode": []
}

road_public = {
    "name": "Main Street",

    "description":
    """You are standing in Main Street - which
used to be full of life. To your left, a row of
houses - now occupied by refugees that pray for
a vaccine.
you can go into the shop, the pub next to it or
the alleyway. Or, you can make your way onto Isiah
Road or Herod Street.""",

    "exits": {"shop": "Shop", "pub": "The Plough", "alleyway": "Alleyway", "isiah road": "Isiah Road", "herod street": "Herod Street"},

    "items": [],

    "passcode": []
}

room_shop = {
    "name" : "Shop",

    "description":
    """You are standing in the shop, the shelves
lay empty of long-life products, and only a few
household products remain.
The only available exit is onto Main Street.""",

    "exits": {"main street": "Main Street"}

    "items": [],

    "passcode": []
}

room_pub = {
    "name": "The Plough",

    "description":
    """You are now inside the pub, where all the
expensive brands of the past have been stolen, and
only the cheap beer no one wants remains - like
Strongbow.
To leave, you can either go onto Main Street or
go into the alleyway.""",

    "exits": {"main street": "Main Street", "alleyway": "Alleyway"},

    "items": [],

    "passcode": []
}

room_alleyway = {
    "name": "Alleyway",

    "description":
    """You are now in the alleyway, which
has likely never seen better days. At the far
end, there is a rustling noise in the industrial
bin that unsettles you greatly.
You can either leave onto Main Street, or go
into the pub through the back entrance.""",

    "exits": {"pub": "The Plough", "main street": "Main Street"},
    
    "items": [],

    "passcode": []
}

road_lab2 = {
    "name": "Isiah Road",

    "description":
    """You now stand in Isiah Street, broken down
and harrassed cars are dotted around the street. At
the end is another one of the stone gates - keeping
the undead out.
You can either enter Lab 2, if you have the necessary
passcode, enter the park or go down a windy path behind
the houses.""",

    "exits": {"lab 2": "Labratory 2", "park": "Willow Park", "windy path": "Windy Path"},

    "items": []

    "passcode": []
}

room_lab2 = {
    "name": "Labratory 2",

    "description":
    """Standing in Lab 2, which is well-lit and tidy,
there is Dr. Gavigan in the corner,  madly writing
notes down that would likely be read in history books
in the distant future.
To leave, you can leave from where you came - Isiah
Road. The side enterance is blocked.""",

    "exits": {"isiah road": "Isiah Road"},

    "items": [],

    "passcode": []
}

room_park = {
    "name": "Willow Park",

    "description":
    """You are now in the once well-kept Willow Park.
Although no longer well-kept, nature and life was found
all around. A clear pond lies below an ancient looking
Willow tree that bends above it.
The side entrance to Lab 2 is closed off by overgrown
shrubbery, so you can only leave back onto Isiah Road.""",

    "exits": {"isiah road": "Isiah Road"},

    "items": [],

    "passcode": []
}

road_windy = {
    "name": "Windy Path",

    "description":
    """You are now walking along a windy, cobblestone
path. Beside you are a row of trees that have bloomed
in the lack of CO2 emmissions - you even spot a pigeon
and her nest.
You can go into the library, or onto Isiah Road.""",

    "exits": {"library": "Library", "isiah road": "Isiah Road"},

    "items": [],

    "passcode": []
}

room_library = {
    "name": "Library",

    "description":
    """You are now inside the library - which
has a few toppled over bookshelves. They have been
collecting dust ever since the last residents left.
A smell of damp lingers in the air; the roof seems to
have been leaking.
You can only leave onto the windy path, as the front
entrance has been boardered up.""",

    "exits": {"windy path": "Windy Path"},

    "items": [],

    "passcode": []
}

rooms_roads = {
    "Herod Close": road_library,
    "Herod Street": road_lab1,
    "Labratory 1": room_lab1,
    "Carpark": room_carpark,
    "Main Street": road_public,
    "Shop": room_shop,
    "The Plough": room_pub,
    "Alleyway": room_alleyway
    "Isiah Road": road_lab2,
    "Willow Park": room_park,
    "Labratory 2": room_lab2,
    "Windy Path": road_windy,
    "Library": room_library
}
