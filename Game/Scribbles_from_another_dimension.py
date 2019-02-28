"""
functions:
enter
converse
fight
interact
"""
from buildings import Building, Room
from people import PC, NPC
from creatures import Zombie, Spider
from objects import Weapon, Lore

houses = {}
road_objects = {}  # probably won't use this, but better have it and delete later
road_people = {}  # again, probably won't be used we'll see
world = {'main road': houses, 'objects': road_objects, 'people': road_people}


#This function displays information about the specified object or creature.
#If no arguments are passed the current room will be described.
#It makes use of the get_description method in the rooms class. Take a look.
def inspect(room, entity = None):
    if room == None:
        return "You are on the street"
    if entity == None:
        return room.get_description()

    #Get all creatures with matching type
    creatures = room.get_creatures(entity)

    output = ["There are {0} {1}(s):".format(len(creatures), entity)]
    for creature in creatures:
        output.append(creature.__str__())

    return "\n".join(output)



#Test data
Zombie1 = Zombie("timmy",10)
Zombie2 = Zombie("tommy",10)
Spider = Spider("Shelob", 5)
weapon1 = Weapon("Sword of 1000 Truths", "It was foretold, that one day, heroes who could wield the sword might reveal themselves.", 2, 1000, 2)
lore1 = Lore("Necronomicon", "Book of dead names. Read at your own peril", 1, "Ph\'nglui mglw\'nafh Cthulhu R\'lyeh wgah\'nagl fhtagn")
Barney = NPC("Barney", "A tall, fat man.", "long description", 100, "Chaotic Neutral", None)
Billy = NPC("Billy", "A short, thin man.", "long description", 100, "Chaotic Neutral", None)
dark_room = Room("Spooky Room", [Barney, Billy], [Zombie1, Zombie2, Spider], [weapon1, lore1], " a dark dillapidated room with no windows")
player = PC("username", Room = dark_room)

print(inspect(player.Room))
print(inspect(player.Room, "Zombie"))
