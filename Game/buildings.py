from Game.objects import Weapon, Lore, Food
from Game.people import NPC
from Game.creatures import Zombie, Spider


class Building:

    def __init__(self, name, desc, rooms, pos):
        self.name = name
        self.description = desc
        self.rooms = rooms
        self.position = pos

    def __str__(self):
        return "{0}\n{1}".format(self.name, self.description)


class Room:

    def __init__(self, name, NPCs, creatures, objects, description):
        self.name = name
        self.NPCs = NPCs
        self.creatures = creatures
        self.objects = objects
        self.desc = description

    #This function returns a description of the room and everything in it.
    #This is not a perfect implementation but shoudl work fine for our demo.
    #Feel free to improve it.
    def get_description(self):
        output = ["You find yourself in ", self.desc, "\n"]

        #provide short description of human characters in the room
        if len(self.NPCs) == 1:
            output.append("You see a lone human in the room. {0} They are named {1}\n".format(self.NPCs[0].get_short,self.NPCs[0].name))
        elif len(self.NPCs) > 1:
            output.append("You see a group of humans in the room. \n")
            for NPC in self.NPCs:
                output.append("{0} They are named: {1}\n".format(NPC.get_short(),NPC.name))

        #show which monsters are present
        counter = {}
        for creature in self.creatures:
            if creature.get_type() in counter:
                counter[creature.get_type()] += 1
            else:
                counter[creature.get_type()] = 1

        for creature in counter.keys():
            output.append("There are {0} {1}(s).\n".format(counter[creature], creature))

        #Show which objects are present.
        for objec in self.objects:
            output.append("You see a {0} item. {1}\n".format(objec.get_type(), objec.desc))

        return "".join(output)

    def __str__(self):
        '''
        The following loops are to create a more readable version of the people & objects in the room.
         The if statements make sure that we don't add extra commas or whitespace characters ( which we would if we
         were to use .join() without the if)
        '''
        persons_text = ""
        for person in self.people:
            if persons_text is "":
                persons_text = person
            else:
                "\n".join((persons_text, person))

        objects_text = ""
        for obj in self.objects:
            if objects_text is "":
                objects_text = obj
            else:
                ", ".join((objects_text, obj))

        if len(self.people) == 0:
            return "{0}. Inside are the following items:{1}".format(self.name, objects_text)
        elif len(self.people) == 1:
            return "{0}. Inside is {1}\nAlso the following items:{2}".format(self.name, persons_text, objects_text)
        # not necessary to check for just 1 item, definitely won't be 0 ( not point having the room)
        return "{0}. Inside are:\n{1}\nAlso the following items:{2}".format(self.name, persons_text, objects_text)


#room test
Zombie1 = Zombie("timmy",10)
Zombie2 = Zombie("tommy",10)
Spider = Spider("Shelob", 5)
weapon1 = Weapon("Sword of 1000 Truths", "It was foretold, that one day, heroes who could wield the sword might reveal themselves.", 2, 1000, 2)
lore1 = Lore("Necronomicon", "Book of dead names. Read at your own peril", 1, "Ph\'nglui mglw\'nafh Cthulhu R\'lyeh wgah\'nagl fhtagn")
Barney = NPC("Barney", "A tall, fat man.", "long description", 100, "Chaotic Neutral", None)
Billy = NPC("Billy", "A short, thin man.", "long description", 100, "Chaotic Neutral", None)
Room = Room("Spooky Room", [Barney, Billy], [Zombie1, Zombie2, Spider], [weapon1, lore1], " a dark dillapidated room with no windows")
print(Room.get_description())
"""
