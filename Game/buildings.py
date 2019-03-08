
# from objects import Weapon, Lore, Food
# from people import NPC
# from creatures import Zombie, Spider
'''
Imports have been commented out, we shouldn't need them 
'''


class Building:
    tower = 5

    def __init__(self, name, desc, rooms, pos):
        self.name = name
        self.description = desc
        self.rooms = rooms
        self.position = pos
        self.floors = {}
        # for loop below: dict of floors, floor number maps to list of rooms in that floor
        for room in self.rooms:
            if room.pos in self.floors.keys():
                self.floors[room.pos].append(room)
            else:
                self.floors[room.pos] = [room]

    def add_room(self, room):
        self.rooms[room.name] = room
        # minor repetition of constructor above
        if room.pos in self.floors.keys():
            self.floors[room.pos].append(room)
        else:
            self.floors[room.pos] = [room]

    def can_go_up(self, pos):
        return pos + 1 in self.floors.keys()

    def can_go_down(self, pos):
        return pos - 1 in self.floors.keys()

    def structure(self, pos):
        message = ""
        # since not completely sure how (in terms of data structure) player position in , I assume we pass it in
        # this method as a single integer which is the floor at which the player is at.
        if self.can_go_down(pos):
            "".join((message, "You can move one floor down.\n"))
        elif self.can_go_up(pos):
            message = "".join((message, "You can move one floor up.\n"))
        if self.floors[pos] in self.floors.keys():
            message = "".join((message, "You can enter the following rooms:\n"))
            for room in self.floors[pos]:  # for room in the floor the player in is
                message = "\n".join((message, room.name)) # only want the names, description come after we've got in the room
        return message

    def __str__(self):
        return "{0}\n{1}".format(self.name, self.description)


class Room:
    def __init__(self, name, NPCs, creatures, objects, description, pos):
        self.name = name
        self.NPCs = NPCs
        self.creatures = creatures
        self.objects = objects
        self.desc = description
        self.pos = pos

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

        #Get monster types and there numbers
        if self.creatures:
            counter = self.count_creatures()
            

            for creature in counter.keys():
                output.append("There are {0} {1}(s).\n".format(counter[creature], creature))

        #Show which objects are present.
        if self.objects:
            for objec in self.objects:
                output.append("You see a {0} item. {1}\n".format(objec.get_type(), objec.desc))

        return "".join(output)

    #show which monsters are present and how many of each kind there are
    def count_creatures(self):
        counter = {}
        for creature in self.creatures:
            if creature.get_type() in counter:
                counter[creature.get_type()] += 1
            else:
                counter[creature.get_type()] = 1

        return counter

    #helper method which returns a list of creatures in the room of the same type.
    def get_creatures(self, kind):
        creature_list =[]
        for creature in self.creatures:
            if creature.get_type() == kind:
                creature_list.append(creature)

        return creature_list

    #helper method which returns a list of objects in the room of the same type.
    def get_objects(self, kind):
        objects_list =[]
        for objec in self.objects:
            if objec.get_type() == kind:
                objects_list.append(objec)

        return objects_list

    

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
'''
Zombie1 = Zombie("timmy",10)
Zombie2 = Zombie("tommy",10)
Spider = Spider("Shelob", 5)
weapon1 = Weapon("Sword of 1000 Truths", "It was foretold, that one day, heroes who could wield the sword might reveal themselves.", 2, 1000, 2)
lore1 = Lore("Necronomicon", "Book of dead names. Read at your own peril", 1, "Ph\'nglui mglw\'nafh Cthulhu R\'lyeh wgah\'nagl fhtagn")
Barney = NPC("Barney", "A tall, fat man.", "long description", 100, "Chaotic Neutral", None)
Billy = NPC("Billy", "A short, thin man.", "long description", 100, "Chaotic Neutral", None)
Room = Room("Spooky Room", [Barney, Billy], [Zombie1, Zombie2, Spider], [weapon1, lore1], " a dark dillapidated room with no windows")
print(Room.get_description())
'''

