"""
functions:
enter
converse
fight
interact
"""
from Game.buildings import Building, Room
from Game.people import PC, NPC
from Game.creatures import Zombie, Spider
from Game.objects import Weapon, Lore
from Game.game_populate import build_game

houses = {}
road_objects = {}  # probably won't use this, but better have it and delete later
road_people = {}  # again, probably won't be used we'll see
world = {'main road': houses, 'objects': road_objects, 'people': road_people}


#This function displays information about the specified object or creature.
#If no arguments are passed the current room will be described.
#It makes use of the get_description method in the rooms class. Take a look.
def inspect(room, entity = None):
    if entity == None:
        return room.get_description()



#Test data
Zombie1 = Zombie("timmy",10)
Zombie2 = Zombie("tommy",10)
Spider = Spider("Shelob", 5)
weapon1 = Weapon("Sword of 1000 Truths", "It was foretold, that one day, heroes who could wield the sword might reveal themselves.", 2, 1000, 2)
lore1 = Lore("Necronomicon", "Book of dead names. Read at your own peril", 1, "Ph\'nglui mglw\'nafh Cthulhu R\'lyeh wgah\'nagl fhtagn")
Barney = NPC("Barney", "A tall, fat man.", "long description", 100, "Chaotic Neutral", None)
Billy = NPC("Billy", "A short, thin man.", "long description", 100, "Chaotic Neutral", None)
dark_room = Room("Spooky Room", [Barney, Billy], [Zombie1, Zombie2, Spider], [weapon1, lore1], " a dark dillapidated room with no windows")
player = PC("username", Room=dark_room)

world = build_game()


print(inspect(player.Room))
