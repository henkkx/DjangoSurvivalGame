from Game.buildings import Building, Room
from Game.objects import *
from Game.people import PC, NPC
from Game.creatures import *

"""
Will try to include the names of all the objects ( by category) here, or in another file later so that we actually know
what is going on without reading the whole script

Buildings:
roofless house

NPCS:
doug

Creatures:
rat

Objects:
bread
health potion
stick
sword
burned note (x2)
"""
zack = PC("Zack", 100)

def init_objects():
    output = {}
    output["stick"]= Weapon("Stick", "A wooden stick, sturdy.", 1, 20, 5)
    output["sword"] = Weapon("Sword", "A simple, standard medival sword", 1, 30, 5)
    output["bread"] = Food("Bread", "An apparently fresh loaf of bread, smells like it just came out...of the oven",
                       1, [40, 5, ""])
    output["health potion"] = Food("Health Potion", "It's small, it's red, come on this is in every game. Hm, maybe ours is green.",
                       1, [50, 0, "all"])
    output["burned note 1"] = Lore("Burned note #1", "A slightly burned piece of paper with scribbled writing. Looks like you wrote it",
                       1, "Why would I do that? How could I let this happen even?")
    output["burned note 2"] = Lore("Burned note #2", "A slightly burned piece of paper with scribbled writing. Looks like you wrote it",
                       1, "Oh my god, the house burned out with the Doug still inside, and it's my fault")
    return output


def init_NPCs():
    output = {}
    output['doug'] = NPC("Doug", "Your childhood dog, Doug", "Doug is a cross-breed labrador with german shepherd. Very playful",
                      150, "friendly", [Lore("Doug's collar", "It looks like it is painted red over green.",
                                             1, "It used to be green, but as a kid you thought I'd be collar\
                                                             if it was red, so you painted over it with a marker")])
    return output


def init_creatures():
    output = {}
    output['charred rat'] = Rat("Charred fur rat", zack.get_level())
    return output


def init_rooms():
    output = {}
    output["kitchen"] = Room("kitchen", NPCs["Doug"], {}, objects["bread"], "You can smell spices, and a hint of both \
    garlic & onion. There are utensils & plates all around")
    output["bedroom"] = Room("bedroom", {}, creatures['rat'], objects["health potion"], "You are in a bedroom, single bed. Sheets indicate a child\
    slept here. In the corner a rat is munching on something")
    return output


def init_buildings():
    output = []
    output['roofless house'] = Building('Roofless House', "This house is made of stone. It's roof has fallen because it's old.",
                          [rooms["kitchen"], rooms["bedroom"]], [1, 1])
    return output


objects = init_objects()
NPCs = init_NPCs()
creatures = init_creatures()
rooms = init_rooms()
buildings = init_buildings()


def build_game():
    objects = init_objects()
    NPCs = init_NPCs()
    creatures = init_creatures()
    rooms = init_rooms()
    buildings = init_buildings()
    world = {"objects": objects, "NPCs": NPCs, "creatures": creatures, "rooms": rooms, "buildings": buildings}
    return world