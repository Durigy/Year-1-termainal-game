# Tools --------------------------------------------------------
item_mask = {
    "id": "mask",

    "name": "Mask",

    "description":
    """A mask, used in a pandemic a long time
ago.""",
}

item_id_card = {
    "id": "id card",

    "name": "ID Card",

    "description":
    """An ID Card that can be used to get
into Laboratory 2.""",
}

item_torch = {
    "id": "torch",

    "name": "Torch",

    "description":
    """A battery powered torch that could come
in handy in dark places. It must have been a weapon
at one point - the end of it is covered in dried
blood.""",
}

item_syringes_bag = {
    "id": "syringes bag",

    "name": "Syringes Bag",

    "description":
    """A bag of syringes - clearly not sterilised.
You wonder if they were used for something other than
medicinal practices back when things were normal.""",
}

item_batteries = {
    "id": "batteries",

    "name": "Batteries",

    "description":
    """A pack of batteries that will be suitable
for a torch. It's amazing they haven't been taken
already.""",
}


item_laptop = {
    "id": "laptop",

    "name": "Laptop",

    "description":
    """This old thing used to be pioneering
technology, once upon a time. Maybe when the world
returns to normal, there will be such thing as
'new' technology again.""",
}

item_substance1 = {
    "id": "substance1",

    "name": "Chemical Substance 1",

    "description":
    """This chemical substance is something familiar to
Dr. Gavigan, but is rather elusive to you. One fact
remains; it's vital for the vaccine.""",
}

item_paper_passcode = {
    "id": "paper passcode",

    "name": "Passcode",

    "description":
    """A piece of old, yellow paper with a passcode
messily strewn on it. Whoever wrote this certainly
has horrible handwriting.""",
}

item_cleaning_product = {
    "id": "cleaning product",
    
    "name": "Disinfectant Spray",

    "description":
    """The disinfectant spray is definitely a go-to
for making disinfecting items easy. That is what it
does, after all.""",
}

item_axe = {
    "id": "axe",

    "name": "Axe",

    "description":
    """This axe would've been a very handy weapon for
someone outside of the gates. Unfortunately for them,
it's here.""",
}

item_beakers = { 
    "id": "beakers",

    "name": "Beakers",

    "description":
    """Beakers that can be used in the making of
chemicals and scientific experiments.""",
}


item_substance2 = {
    "id": "substance2",
    
    "name": "Chemical Substance 2",

    "description":
    """This chemical substance is something familiar to
Dr. Gavigan, but is rather elusive to you. One fact
remains; it's vital for the vaccine.""",
}

item_substance3 = {
    "id": "substance3",

    "name": "Chemical Substance 3",

    "description":
    """This cheMical substance is something familiar to
Dr. Gavigan, but is rather elusive to you. One fact
remains; it's vital for the vaccine.""",
}


# Food --------------------------------------------------------

item_salted_crisps = {
    "id": "salted crips",

    "name": "Bag of Salted Crisps",

    "description":
    """A pack of a famous brand's salted
crisps. Do crisps even go off?""",

    "energy" : 1, # we need to adjust the energy, currently it is either too low or too high.
}

item_chocolate_bar = {
    "id": "chocolate bar",

    "name": "Chocolate Bar",

    "description":
    """A chocolate bar - which looks very tempting
right about now. Will it taste just like it used to?""",

    "energy" : 1, # we need to adjust the energy, currently it is either too low or too high.
}

item_canned_beans = {
    "id": "canned beans",

    "name": "Canned Beans",

    "description":
    """An own-brand can of baked beans. They will be
edible cold, just not as nice. It takes you back to
beans on toast was your go-to meal when you were a
university student.""",

    "energy" : 3, # we need to adjust the energy, currently it is either too low or too high.
}

item_canned_potatoes = {
    "id": "canned potatoes",

    "name": "Canned Potatoes",
    
    "description":
    """An own-band can of potatoes. You're surprised
to find out they're well within their expiry date. A
filling so-called meal, nowadays.""",

    "energy" : 3, # we need to adjust the energy, currently it is either too low or too high.
}

item_pickles = {
    "id": "pickles",

    "name": "Jar of Pickles",

    "description":
    """A jar of pickles, Dr. Gavigan's favourite
snack. He seems to have an endless amount of them -
probably won't notice if one jar disappears. Afterall,
how else did it get here?""",

    "energy" : 4, # we need to adjust the energy, currently it is either too low or too high.
}

item_vodka = {
    "id": "vodka",

    "name": "Vodka",

    "description":
    """A bottle of vodka that seems a bit dusty on
the outside, but unopened - which will be useful as
a make-shift disinfectant.""",

    "energy" : 7, # we need to adjust the energy, currently it is either too low or too high.
}

# --------------------------------------------------------

tools = {
    "id card": item_id_card,
    "torch": item_torch,
    "syringes bag": item_syringes_bag,
    "batteries": item_batteries,
    "laptop": item_laptop,
    "substance1": item_substance1,
    "paper passcode": item_paper_passcode,
    "cleaning product": item_cleaning_product,
    "axe": item_axe,
    "beakers": item_beakers,
    "substance2": item_substance2,
    "substance3": item_substance3,
    "mask": item_mask
}

food = {
    "salted crisps": item_salted_crisps,
    "chocolate bar": item_chocolate_bar,
    "canned beans": item_canned_beans,
    "canned potatoes": item_canned_potatoes,
    "pickles": item_pickles,
    "vodka": item_vodka
}
