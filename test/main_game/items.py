# Tools --------------------------------------------------------

item_torch = {
    "id": "torch",

    "name": "Torch",

    "description":
    """A battery powered torch that could come
in handy in dark places. Perhaps it could even
be used as a weapon? It must have been at one
point - the end of it is covered in dried
blood.""",

    "mass" : "25"  # we need to adjust the mass, currently it is either too low or too high.
}

item_syringes_bag = {
    "id": "syringes bag",

    "name": "Syringes Bag",

    "description":
    """A bag of syringes - clearly not sterilised.
You wonder if they were used for something other than
medicinal practices back when things were normal.""",

    "mass" : "40" # we need to adjust the mass, currently it is either too low or too high.
}

item_batteries = {
    "id": "batteries",

    "name": "Batteries",

    "description":
    """A pack of batteries that will be suitable
for a torch. It's amazing they haven't been taken
already.""",

    "mass" : "130" # we need to adjust the mass, currently it is either too low or too high.
}

# Food --------------------------------------------------------

item_salted_crisps = {
    "id": "salted crips",

    "name": "Bag of Salted Crisps",

    "description":
    """A pack of Kettle Salted Crisps. You wonder if
crisps go out of date.""",

    "energy" : "1", # we need to adjust the energy, currently it is either too low or too high.

    "mass" : "10" # we need to adjust the mass, currently it is either too low or too high.
}

item_mars_bar = {
    "id": "mars bar",

    "name": "Mars Bar",

    "description":
    """A mars bar - which looks very tempting right
about now. Will it taste just like it used to?""",

    "energy" : "1", # we need to adjust the energy, currently it is either too low or too high.

    "mass" : "10" # we need to adjust the mass, currently it is either too low or too high.
}

# --------------------------------------------------------

tools = {
    "torch": item_torch,
    "syringes bag": item_syringes_bag,
    "batteries": item_batteries
}

food = {
    "salted crisps": item_salted_crisps,
    "mars bar": item_mars_bar
}
