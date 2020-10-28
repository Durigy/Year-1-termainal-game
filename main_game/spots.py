from .items import tools, food
from .map import rooms, roads


# Roads --------------------------------------------------------------------

# Herod Close
lamppost_herodclose = {
    "name": roads["herod close"]["name"],

    "main description": roads["herod close"]["description"],

    "spot name": "Lamppost",

    "description":
    """The lamppost is on, but not very
bright. It seems to be reaching the end
of it's life. Below it, abandoned, is a
torch - empty of batteries.
You can go east to make your way back to
the centre of the street.""",

    "exits": {"east": "hc centre"},

    "tools": ["torch"],

    "food": [],

    "passcode": []
}

herodclose_centre = {
    "name": roads["herod close"]["name"],

    "main description": roads["herod close"]["description"],

    "spot name": "HC Centre",

    "description":
    """You can go west to the lamppost,
or leave east onto Herod Street.""",
    
    "exits": {"west": "lamppost", "east": "hs centre"},

    "tools": [],

    "food": [],

    "passcode": []
}

# Herod Street
herodstreet_centre = {
    "name": roads["herod street"]["name"],

    "main description": roads["herod street"]["description"],

    "spot name": "HS Centre",

    "description":
    "",

    "exits": {"north": "hc centre", "east": "m centre", "south": "c centre", "west": "desk"},

    "tools": [],

    "food": [],

    "passcode": ["answer"]
}

# Main Street
main_centre = {
    "name": roads["main street"]["name"],

    "main description": roads["main street"]["description"],

    "spot name": "M Centre",
    
    "description":
    """You are standing in the centre of
Main Street. You can either make your way
to the front of the shop, or the front of
the pub (The Plough.)""",
    
    "exits": {"west": "shop front", "east": "pub front"},

    "tools": [],

    "food": [],

    "passcode": []
}

front_shop = {
    "name": roads["main street"]["name"],

    "main description": roads["main street"]["description"],

    "spot name": "Shop Front",
    
    "description":
    """Standing in front of the shop,
you see a binbag in front of one of the
houses - to your north. You can see
a wooden handle protruding from it.
If you go south, you'll enter the shop,
and east will take you back to the centre
of the street.""",
    
    "exits": {"north": "binbag", "south": "shop entrance", "east": "m centre"},

    "tools": [],

    "food": [],

    "passcode": []
}

spot_binbag = {
    "name": roads["main street"]["name"],

    "main description": roads["main street"]["description"],

    "spot name": "Binbag",

    "description":
    """You're now in front of the binbag,
which smells like rot. The wooden handle is
definitely connected to something.
Going south will take you to the shop front,
and east directly to the centre.""",

    "exits": {"south": "shop front", "east": "m centre"},

    "tools": ["hammer"],

    "food": [],

    "passcode": []
}

front_pub = {
    "name": roads["main street"]["name"],

    "main description": roads["main street"]["description"],

    "spot name": "Pub Front",
    
    "description":
    """You're standing in front of The
Plough, which used to be creepy old men's
go to place when they can't be bothered
to argue with their wife.
To enter it, you go south. Going west
takes you back to the centre, and east
to the front of the alley.""",

    "exits": {"east": "alley front", "south": "p centre", "west": "m centre"},

    "tools": [],

    "food": [],

    "passcode": []
}

front_alley = {
    "name": roads["main street"]["name"],

    "main description": roads["main street"]["description"],

    "spot name": "Alley Front",
    
    "description":
    """You're now on the corner of
Main Street, standing by an alley way
and the cusp of Isiah Road.
To enter the alleyway, go south. Or,
you can go north onto Isiah Road or
west to the pub front.""",

    "exits": {"south": "street entrance", "north": "ir centre", "west": "pub front"},

    "tools": [],

    "food": [],

    "passcode": []
}

# Isiah Road
ir_centre = {
    "name": roads["isiah road"]["name"],

    "main description": roads["isiah road"]["description"],

    "spot name": "IR Centre",

    "description":
        """You're now standing in Isiah Road.
    To your right (east) is the park, and your
    south is Main Street. North will take you
    to the north of Isiah Road.""",

    "exits": {"east": "pa centre", "north": "ir north centre", "south": "alley front"},

    "tools": [],

    "food": [],

    "passcode": []
}

north_ir_centre = {
    "name": roads["isiah road"]["name"],

    "main description": roads["isiah road"]["description"],

    "spot name": "IR North Centre",

    "description":
        """You're now at the north part of
    Isiah road. Here, to the east is
    Laboratory 2 - you'll need a passcode to
    enter, however. South takes you to the
    southern part of the road. To the west
    will take you down a windy, cobblestone
    path - behind the houses.""",

    "exits": {"east": "lab2 centre", "south": "ir centre", "west": "w centre"},

    "tools": [],

    "food": [],

    "passcode": ["answer"]
}

# Windy Path
windy_centre = {
    "name": roads["windy path"]["name"],

    "main description": roads["windy path"]["description"],

    "spot name": "W Centre",

    "description":
        """You can either go north, to the
    base of a tree. East will take you to Isiah
    Road, south to the garden fence and west
    goes straight to the library.""",

    "exits": {"north": "tree", "east": "ir north centre", "south": "garden fence", "west": "entrance"},

    "tools": [],

    "food": [],

    "passcode": []
}

tree_base = {
    "name": roads["windy path"]["name"],

    "main description": roads["windy path"]["description"],

    "spot name": "Tree",

    "description":
        """The tree looks young, but has
    thrived in the past few years - its
    leaves are a vibrant green. Going east
    will take you to the pigeon's nest,
    and south will take you back to the
    path.""",

    "exits": {"east": "birds nest", "south": "w centre"},
    # Substance2 can be found under the tree (here), in the birds nest or in the box by the garden fence.
    "tools": [],

    "food": [],

    "passcode": []
}

birds_nest = {
    "name": roads["windy path"]["name"],

    "main description": roads["windy path"]["description"],

    "spot name": "Birds Nest",

    "description":
        """The pigeon gives you a glare
    as you approach it, unsettled by
    your presence. Is it worth bothering
    the bird as she sits on - presumably -
    her eggs?
    Going east will take you straight to
    Isiah Road, west to the tree you came
    from and south to the path.""",

    "exits": {"east": "ir north centre", "west": "tree", "south": "w centre"},

    "tools": [],

    "food": [],

    "passcode": []
}

garden_fence = {
    "name": roads["windy path"]["name"],

    "main description": roads["windy path"]["description"],

    "spot name": "Garden Fence",

    "description":
        """You're now standing at the garden
    fence, by the half-opened box. It seems
    quiet, so you're certain there's no rats
    in there. You can't be bothered to catch
    a disease, quite honestly.
    Going north will take you back onto the
    path, west to cut across to the library
    and east to cut across to Isiah Road.""",

    "exits": {"north": "w centre", "east": "ir north centre", "west": "entrance"},

    "tools": [],

    "food": [],

    "passcode": []
}


# Rooms --------------------------------------------------------------------

# Car park
car_lab1_side_entrance = {
    "name": rooms["car park"]["name"],

    "main description": rooms["car park"]["description"],

    "spot name": "1 Side Entrance",

    "description":
        """The side entrance to Laboratory 1,
    slowly rusting. It requires a passcode to
    get inside.
    You can attempt to enter the laboratory
    by going north, or return east to the blue
    car.""",

    "exits": {"east": "blue car", "north": "lab 1 side entrance"},

    "tools": [],

    "food": [],

    "passcode": ["answer"]
}

blue_car = {
    "name": rooms["car park"]["name"],

    "main description": rooms["car park"]["description"],

    "spot name": "Blue Car",

    "description":
        """The blue car's door is wide open -
    like someone left in a rush. Hanging from
    the mirror are two fluffy dice - they might've
    produced a smell at once point.
    You can go east to the centre of the car park,
    or south to the silver car.""",

    "exits": {"east": "c centre", "south": "silver car"},

    # syringes bag can be in all of the cars
    # batteries can be in - any of the 3 cars, any of the 3 aisles in the shop or behind the bar.
    "tools": [],

    "food": [],

    "passcode": []
}

silver_car = {
    "name": rooms["car park"]["name"],

    "main description": rooms["car park"]["description"],

    "spot name": "Silver Car",

    "description":
        """The silver car was the most old
    out of all of the cars, it was a mystery
    to how it was running even before times...
    changed.
    You can go north to the blue car, or east
    to the black car.""",

    "exits": {"north": "blue car", "east": "black car"},

    "tools": [],

    "food": [],

    "passcode": []
}

black_car = {
    "name": rooms["car park"]["name"],

    "main description": rooms["car park"]["description"],

    "spot name": "Black Car",

    "description":
        """The black car is shut, with a broken
    window. You open it from the inside, to
    avoid broken glass harming you.
    You can go north to the centre of the car park,
    or west to the silver car.""",

    "exits": {"north": "c centre", "west": "silver car"},

    "items": [],

    "food": [],

    "passcode": []
}

carpark_centre = {
    "name": rooms["car park"]["name"],

    "main description": rooms["car park"]["description"],

    "spot name": "C Centre",

    "description":
        """You are now in the centre of the
    car park. You can go east onto Herod Street,
    or west to the blue car.""",

    "exits": {"west": "blue car", "east": "hs centre"},

    "tools": [],

    "food": [],

    "passcode": []
}

# Laboratory 1

spot_desk = {
    "name": rooms["laboratory 1"]["name"],

    "main description": rooms["laboratory 1"]["description"],

    "spot name": "Desk",

    "description":
        """You're standing in front of the
    desk, which is right by the front entrance.
    To the north of you there is a syringe
    cupboard, to the south a bookshelf.
    Alternatively, you could turn east to enter
    Herod Street.""",

    "exits": {"north": "syringe cupboard", "east": "hs centre", "south": "bookshelf"},

    "tools": ["laptop"],

    "food": [],

    "passcode": []
}

syringe_cupboard = {
    "name": rooms["laboratory 1"]["name"],

    "main description": rooms["laboratory 1"]["description"],

    "spot name": "Syringe Cupboard",

    "description":
        """The syringe cupboard lays half open,
    dark inside. If you open it, you'll be able
    to see it contents.
    You can explore the chemical cupboard to the
    west, your left, or return to the desk in the
    south.""",

    "exits": {"west": "chemical cupboard", "south": "desk"},

    # Substance1 can be in the syringe cupboard, the chemical cupboard, or the cans aisle in the shop.
    "tools": [],

    "food": [],

    "passcode": []
}

chemical_cupboard = {
    "name": rooms["laboratory 1"]["name"],

    "main description": rooms["laboratory 1"]["description"],

    "spot name": "Chemical Cupboard",

    "description":
        """The chemical cupboard is shut, but
    not locked.
    From here, you can make your
    way to the side entrance of the lab in the
    south, or return to the syringe cupboard
    in the east.""",

    "exits": {"south": "lab 1 side entrance", "east": "syringe cupboard"},
    # Paper passcode can be in the chemical cupboard or the bookshelf.
    "tools": [],

    "food": [],

    "passcode": []
}

lab1_side_entrance = {
    "name": rooms["laboratory 1"]["name"],

    "main description": rooms["laboratory 1"]["description"],

    "spot name": "Lab 1 Side Entrance",

    "description":
        """You are standing in front of the
    door that leads to the car park.
    You can go south to enter it, or east to check
    out the bookshelf""",

    "exits": {"south": "car park lab 1 side entrance", "east": "bookshelf"},

    "tools": [],

    "food": [],

    "passcode": []
}

spot_bookshelf = {
    "name": rooms["laboratory 1"]["name"],

    "main description": rooms["laboratory 1"]["description"],

    "spot name": "Bookshelf",

    "description":
        """The bookshelf is dusty - documents and
    books of science have laid still for many
    years.
    To move, you can go north to the desk or
    west""",

    "exits": {"north": "desk", "west": "lab 1 side entrance"},

    "tools": ["substance1", "paper passcode"],

    "food": [],

    "passcode": []
}

# Shop
shop_entrance = {
    "name": rooms["shop"]["name"],

    "main description": rooms["shop"]["description"],

    "spot name": "Shop Entrance",
    
    "description":
    """There are three aisles that seem
to contain things.
On your far left, the west, is the
cleaning aisle. In front of you, south,
is the crisps aisle and the east has the
cans aisle.""",
    
    "exits": {"north": "m centre", "east": "cans aisle", "south": "crisps aisle", "west": "cleaning aisle"},

    "tools": [],

    "food": [],

    "passcode": []
}

cleaning_aisle = {
    "name": rooms["shop"]["name"],

    "main description": rooms["shop"]["description"],

    "spot name": "Cleaning Aisle",

    "description":
    """The cleaning aisle is the most
full - it's rather unlikely people would
want limescale remover in a zombie
apocalypse, after all.
You can go to the next aisle by going
east, or north to the entrance.""",

    "exits": {"east": "crisps aisle", "north": "shop entrance"},

    "tools": ["cleaning product"],

    "food": [],

    "passcode": []
}

crisps_aisle = {
    "name": rooms["shop"]["name"],

    "main description": rooms["shop"]["description"],

    "spot name": "Crisps Aisle",
    
    "description":
    """The crisps aisle is lost of fan
favourites, like walkers. The more
expensive brands, like Kettle, were left.
Even though they were the nicest!
You can go west to the cleaning aisle,
east to the canned goods aisle or north to
the entrance.""",

    "exits": {"north": "shop entrance", "west": "cleaning aisle", "east": "cans aisle"},

    "tools": [],

    "food": [],

    "passcode": []
}

cans_aisle = {
    "name": rooms["shop"]["name"],

    "main description": rooms["shop"]["description"],

    "spot name": "Cans Aisle",
    
    "description":
    """The canned goods aisle is
undoubtedly the most empty in all the
occupied aisles. In fact, it doesn't
seem there's any 'canned' goods at all.
There might be something about, though.
From here, you can go west to the crisps
aisle, or north to the shop entrance.""",

    "exits": {"west": "crisps aisle", "north": "shop entrance"},

    "tools": [],

    "food": [],

    "passcode": []
}

# The Plough (Pub)
pub_centre = {
    "name": rooms["the plough"]["name"],

    "main description": rooms["the plough"]["description"],

    "spot name": "P Centre",
    
    "description":
    """You can go north onto Main
Street, go east to get behind the bar or
go south to leave into the alleyway.""",
    
    "exits": {"north": "pub front", "east": "behind bar", "south": "dog kennel"},

    "tools": [],

    "food": [],

    "passcode": []
}

behind_bar = {
    "name": rooms["the plough"]["name"],

    "main description": rooms["the plough"]["description"],

    "spot name": "Behind Bar",
    
    "description":
    """The bar has been scrounged for
liquor, people wanting a break from reality.
To your luck, and surprise, there is an
untouched bottle of Vodka and a can of
baked beans.""",

    "exits": {"west": "p centre"},

    "tools": [],

    "food": [],

    "passcode": []
}

# Alleyway
alley_centre = {
    "name": rooms["alleyway"]["name"],

    "main description": rooms["alleyway"]["description"],

    "spot name": "A Centre",
    
    "description":
    """To investigate the bin, you can go
west. North takes you to the dog kennel,
and therefore the pub entrance, and
east will take you to just before Main
Street.""",
    
    "exits": {"east": "street entrance", "north": "dog kennel", "west": "industrial bin"},

    "tools": [],

    "food": [],

    "passcode": []
}

industrial_bin = {
    "name": rooms["alleyway"]["name"],

    "main description": rooms["alleyway"]["description"],

    "spot name": "Industrial Bin",
    
    "description":
    """The industrial bin still makes an
unsettling noise as you edge closer to it.
It remains closed, but there's a scratching
noise from the inside. The top remains
closed.
From here, you can only return east to the
centre.""",

    "exits": {"east": "a centre"},
    # notebook can either be in the industrial bin or the dog kennel.
    "tools": ["axe"],

    "food": [],

    "passcode": []
}

dog_kennel = {
    "name": rooms["alleyway"]["name"],

    "main description": rooms["alleyway"]["description"],

    "spot name": "Dog Kennel",
    
    "description":
    """The dog kennel is now abandoned,
dirty and damp from years of rain. You
wonder what breed of dog occupied it.
If you go north, you'll enter the pub.
South will take you back to the centre,
and east to the corner by Main Street.""",

    "exits": {"north": "p centre", "south": "a centre", "east": "street entrance"},

    "tools": [],

    "food": [],

    "passcode": []
}

entrance_street = {
    "name": rooms["alleyway"]["name"],

    "main description": rooms["alleyway"]["description"],

    "spot name": "Street Entrance",

    "description":
    """You are now standing just by the
entrance of Main Street - the light
warms you from the dark of the alley.
To enter Main Street, go north. Going west
will take you to the centre of the alley.""",
    
    "exits": {"west": "a centre", "north": "alley front"},

    "tools": [],

    "food": [],

    "passcode": []
}

# Laboratory 2
lab2_centre = {
    "name": rooms["laboratory 2"]["name"],

    "main description": rooms["laboratory 2"]["description"],

    "spot name": "Lab 2 Centre",
    
    "description":
    """You can go north to investigate
the cupboard, south to visit the side
entrance of west to re-enter Isiah Road.""",

    "exits": {"north": "cupboard", "south": "side entrance", "west": "ir north centre"},

    "tools": [],

    "food": [],

    "passcode": []
}

top_cupboard = {
    "name": rooms["laboratory 2"]["name"],

    "main description": rooms["laboratory 2"]["description"],

    "spot name": "Cupboard",
    
    "description":
    """You're now in front of the
opened cupboard - it's full of jars of
pickles. Where on earth did Dr. Gavigan
get them from? It rather unsettled you.
From here, you can go east to check out
the beaker tray - or south to the centre
of the lab, where Dr. Gavigan is.""",

    "exits": {"east": "beaker tray", "south": "lab2 centre"},

    "tools": [],

    "food": [],

    "passcode": []
}

beaker_tray = {
    "name": rooms["laboratory 2"]["name"],

    "main description": rooms["laboratory 2"]["description"],

    "spot name": "Beaker Tray",
    
    "description":
    """A beaker tray sits in front of
you, on the desk. The beakers seem to
have been recently sterilised - but
Dr. Gavigan still needs them.""",

    "exits": {"south": "side entrance", "west": "cupboard"},

    "tools": ["beakers"],

    "food": [],

    "passcode": []
}

side_entrance = {
    "name": rooms["laboratory 2"]["name"],

    "main description": rooms["laboratory 2"]["description"],

    "spot name": "Side Entrance",
    
    "description":
    """You're now standing in front of
a door, that seems harmless enough. Not
so different from the door in Lab 1.
However, when you go to reach for the handle,
Dr. Gavigan calls out in a rushed voice,
'It's blocked from the outside! Don't
bother messing with it.' He looked
suspicious, but you didn't want to
question it.
Going north will take you to the
beaker tray, and west to the centre of
the Lab.""",
    
    "exits": {"north": "beaker tray", "west": "lab2 centre"},

    "tools": [],

    "food": [],

    "passcode": []
}

# Willow Park
park_centre = {
    "name": rooms["willow park"]["name"],

    "main description": rooms["willow park"]["description"],

    "spot name": "PA Centre",
    
    "description":
    """From here, going north will
take you to the hollybush. South will
take you to the lonely bench, and
west will take you back onto Isiah Road.""",
    
    "exits": {"north": "bush", "south": "bench", "west": "ir centre"},

    "tools": [],

    "food": [],

    "passcode": []
}

spot_bench = {
    "name": rooms["willow park"]["name"],

    "main description": rooms["willow park"]["description"],

    "spot name": "Bench",
    
    "description":
    """The bench sits, overlooking the
pond - unused. If you could, it'd be nice
to take a moment just to breathe and be
with nature - forget the current world.
There were things to be done, however.
On the bench, something gold catches your
eye - a pocket watch.
From here, going east will take you to the
crooked Willow Tree. North will take you
back to the centre of the park.""",

    "exits": {"north": "pa centre", "east": "willow tree"},
    # watch can either be on the park bench, on the bookshelf or in the mystery aisle of the library.
    "tools": [],

    "food": [],

    "passcode": []
}

willow_tree = {
    "name": rooms["willow park"]["name"],

    "main description": rooms["willow park"]["description"],

    "spot name": "Willow Tree",
    
    "description":
    """The willow tree twists over the pond,
some of the branches brush the water - like
a greeting. It looks like it was standing
here for a while - but it also looks tired.
Beneath it, you're shocked to find a...
pickle jar? You suppose even Dr. Gavigan
needs somewhere away from the lab to eat his
pickles.
You can see the side entrance to the north,
you may even be able to access it! To the
west will take you to the bench.""",

    "exits": {"north": "lab 2 side entrance", "west": "bench"},
    # Pickles will be under the willow tree or in the box (windy path - garden fence)
    # NOTE: Pickles in "cupboard" are not take-able.
    "tools": [],

    "food": [],

    "passcode": []
}
# To access here, you need an axe to break down the barrier.
lab2_side_entrance = {
    "name": rooms["willow park"]["name"],

    "main description": rooms["willow park"]["description"],

    "spot name": "Lab 2 Side Entrance",
    
    "description":
    """Finally, you've managed to access
the little side entrance. Why is it blocked,
anyway? The barriers leave a box shape
within, and stepping in it you almost die
from fright when an undead being throws
itself toward you - but it's yanked back
by a chain.""",
    # If you've collected the pocket watch, you recognise the zombie to be Dr. Gavigan's wife.
    # I'm putting this here cause i want it to be in the story, it may need to be placed somewhere else and that's fine
    "event1":
    """You chuckle at the undead - it
hasn't got you and you live to see another
day. But...why was it here? Then, it clicks.
You take out the golden pocket watch, and
confirm that the undead being is Dr. Gavigan's
spouse.
He's kept her. But for what?""", # You can choose to put her out of her misery, or leave like nothing's happened.
    # If you choose to kill her, you're caught by gavigan and explains that he used her cells to create the vaccine. He becomes distraught after she's dead (again) and can't bring himself to make the vaccine.
    # if not, you can question him and he'll tell you that it's because he couldn't let go of her - but her cells helped create the vaccines.

    "event2":
    """You chuckle at the undead - it
hasn't got you and you live to see another
day. But...why was it here? It doesn't
matter - this is supposed to be a safe
haven from the undead, and yet here is
one inside these walls.
But, it is chained up...it's stayed here
this long, after all.""",
    
    "exits": {"north": "side entrance", "south": "willow tree", "west": "bush"},

    "tools": [],

    "food": [],

    "passcode": ["answer"]
}

spot_bush = {
    "name": rooms["willow park"]["name"],

    "main description": rooms["willow park"]["description"],

    "spot name": "Bush",

    "description":
    """You go over to the bush to play
with the kitten, but it simply hisses
at you - it's feral. In fact, you even
get scratched with tiny, sharp claws.
Perhaps it's time to just turn back,
south to the centre. """,

    "exits": {"south": "pa centre"},

    "tools": [],

    "food": [],

    "passcode": []
}

# Library
library_centre = {
    "name": rooms["library"]["name"],

    "main description": rooms["library"]["description"],

    "spot name": "L Centre",

    "description":
    """You're now standing in the
centre of the library - drops of water
drip from the tiles above.
Going east will take you to the entrance,
north to the fiction aisle and west
to the non-fiction aisle.""",
    
    "exits": {"east": "entrance", "north": "fiction aisle", "west": "non-fiction aisle"},

    "tools": [],

    "food": [],

    "passcode": []
}

library_entrance = {
    "name": rooms["library"]["name"],

    "main description": rooms["library"]["description"],

    "spot name": "Entrance",

    "description":
    """You're now at the entrance of
the library, where you came from in
the first place. To leave, you can go
east. However, north will take you to
the mystery aisle, and west to the
centre of the library.""",
    
    "exits": {"east": "w centre", "north": "mystery aisle", "west": "l centre"},

    "tools": [],

    "food": [],

    "passcode": []
}

fiction_aisle = {
    "name": rooms["library"]["name"],

    "main description": rooms["library"]["description"],

    "spot name": "Fiction Aisle",

    "description":
    """You stand in the fiction aisle,
and you find yourself lost in the thought
of escaping to one of the non-postapocalyptic
universes kept within the pages. The thought
only gives you gloom.
Going east will take you to venture the
mystery aisle, and south will take you back
to the centre.""",

    "exits": {"east": "mystery aisle", "south": "l centre"},
    # substance 3 can be in any of the three aisles in the library.
    "tools": [],

    "food": [],

    "passcode": []
}

mystery_aisle = {
    "name": rooms["library"]["name"],

    "main description": rooms["library"]["description"],

    "spot name": "Mystery Aisle",

    "description":
    """The mystery aisle is filled with
murder mystery books, set in a modern
world or one from decades ago - it felt
like there was no in between. Death was a
familiar concept, nowadays. Everyone you
know, will, or have known has lost someone.
You hope that Dr. Gavigan's vaccine will
do the trick - otherwise untimely death
from being cannibalized and turned will
continue to be the norm.
From here, you can go east to go back
onto the windy path. West will take you
to the fiction aisle, and south to the
centre of the library.""",

    "exits": {"east": "w centre", "west": "fiction aisle", "south": "l centre"},

    "tools": [],

    "food": [],

    "passcode": []
}

nonfic_aisle = {
    "name": rooms["library"]["name"],

    "main description": rooms["library"]["description"],

    "spot name": "Non-Fiction Aisle",
    
    "description":
    """The non-fiction aisle is in a dark corner,
the window boarded up - which would usually
look out onto Herod Close. It'd be impossible
to search here without some kind of light source.
You can only return east, to the centre, where
you originally came from.""",

    "exits": {"east": "l centre"},

    "tools": [],

    "food": [],

    "passcode": []
}


# References --------------------------------------------------------------------

spots = {
    "lamppost": lamppost_herodclose,
    "hc centre": herodclose_centre,
    "hs centre": herodstreet_centre,
    "car park lab 1 side entrance": car_lab1_side_entrance,
    "blue car": blue_car,
    "silver car": silver_car,
    "black car": black_car,
    "c centre": carpark_centre,
    "desk": spot_desk,
    "syringe cupboard": syringe_cupboard,
    "chemical cupboard": chemical_cupboard,
    "lab 1 side entrance": lab1_side_entrance,
    "bookshelf": spot_bookshelf,
    "m centre": main_centre,
    "shop front": front_shop,
    "pub front": front_pub,
    "binbag": spot_binbag,
    "alley front": front_alley,
    "shop entrance": shop_entrance,
    "cleaning aisle": cleaning_aisle,
    "crisps aisle": crisps_aisle,
    "cans aisle": cans_aisle,
    "p centre": pub_centre,
    "behind bar": behind_bar,
    "a centre": alley_centre,
    "industrial bin": industrial_bin,
    "dog kennel": dog_kennel,
    "street entrance": entrance_street,
    "ir centre": ir_centre,
    "ir north centre": north_ir_centre,
    "lab2 centre": lab2_centre,
    "cupboard": top_cupboard,
    "beaker tray": beaker_tray,
    "side entrance": side_entrance,
    "pa centre": park_centre,
    "bench": spot_bench,
    "bush": spot_bush,
    "willow tree": willow_tree,
    "lab 2 side entrance": lab2_side_entrance,
    "w centre": windy_centre,
    "tree": tree_base,
    "birds nest": birds_nest,
    "garden fence": garden_fence,
    "l centre": library_centre,
    "entrance": library_entrance,
    "fiction aisle": fiction_aisle,
    "mystery aisle": mystery_aisle,
    "non-fiction aisle": nonfic_aisle
}


