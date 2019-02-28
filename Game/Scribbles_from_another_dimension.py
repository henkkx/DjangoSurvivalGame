"""
functions:
enter
converse
fight
interact
"""
from Game.buildings import Building, Room
from Game.people import PC, NPC
from Game.creatures import Creature
from Game.objects import Objects

houses = {}
road_objects = {}  # probably won't use this, but better have it and delete later
road_people = {}  # again, probably won't be used we'll see
world = {'main road': houses, 'objects': road_objects, 'people': road_people}



#This function displays information about the specified object or creature.
#If no arguments are passed the current room will be described.
#It makes use of the get_description method in the rooms class. Take a look.
def inspect(entity = None):
    if entity == None:
        pass
