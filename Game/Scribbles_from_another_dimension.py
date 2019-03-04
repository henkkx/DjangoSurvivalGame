"""
functions:
enter
converse
fight
interact
"""
import time
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
def inspect(room, pl = 1, entity = None):
    if room == None:
        return "You are on the street"
    if entity == None:
        return room.get_description()

    #if there are creatures in the room that match the entity then output info about these creatures
    #if not move on to objects
    if room.creatures:
        
        #Get all creatures with matching type
        creatures = room.get_creatures(entity)
        if creatures:
            
            #Display information for all creatures whose type matches entity. Includes level comparison for each
            output = ["There are {0} {1}(s):".format(len(creatures), entity)]
            for creature in creatures:
                output.append("{0}.  {1}".format(creature.__str__(), creature.level_comp(pl)))

            return "\n".join(output)

    if room.objects:
        
        #Get all objects with matching type
        objects = room.get_objects(entity)
        if objects:
            
            #Display information for all creatures whose type matches entity. Includes level comparison for each
            output = ["There are {0} {1}(s):".format(len(objects), entity)]
            for objec in objects:
                output.append("{0}.".format(objec.__str__()))
            return "\n".join(output)

    return "There are no entities matching {0}".format(entity)


def fight(weapon, creatures,launch):

    enemyap = 0
    enemyhp = 0
    userap = weapon.dmg
    userhp = player.hp

    # Methods can be altered to introduce block,dodge etc
    def enemyattack(userhp,usertype = None):
        print("The enemy launches a quick attack dealing " + str(enemyap) + " damage to you\n")
        userhp -= enemyap
        return userhp

    def attack(enemyhp,usertype = None):
        print("You launch a stunning attack, majestic in motion dealing " + str(userap) + " damage with your weapon\n")
        enemyhp -= userap
        return enemyhp

    # Fight Start Dependant On Person Who Starts It
    if launch is True:
        print("You have launched an attack\n")
    else:
        print("You are stunned as a barrage of quick strikes are directed towards you\n")
        userhp -= 20

    # If Multiple Creatures are involved in the fight
    if type(creatures) == list:
        for creature in creatures:
            enemyhp += creature.hp
            enemyap += creature.ap
            enemyap *= (3/4) # To ensure not scale enemy damage up 1 to 1
    else:
        enemyap = creatures.ap
        enemyhp = creatures.hp

        print("Fight Time.")

    while enemyhp > 0 and player.hp > 0:

        if userhp < 1:
            print("A disgraceful showing, a place in hell is reserved for the likes of you")
            return

        print("Your HP: " + str(userhp))
        print("Enemy HP: " + str(enemyhp))

        print(".........\n")
        time.sleep(0.5)  # Maybe we could do something with time.sleep in combat
        print("1 - Attack")
        print("2 - Leave")

        #print("3 - Block")
        #print("4 - Dodge")

        cmdlist = ['1', '2'] #,'3','4']
        cmd = getcmd(cmdlist)

        if cmd == "1":
            enemyhp = attack(enemyhp)
        elif cmd == "2":
            print("You leave as fast as you can, leonidas appears, hurling abuse towards you"
                  " COWARD HE SCREAMS, COWARD as you panter away head hung in shame")
            return

        if enemyhp > 0:
            userhp = enemyattack(userhp)
        elif enemyhp < 1:
            print("A swift an decisive slaughter Ghandi would be honored to witness such a spectacle")

# Temporary Method To Get Comand line input
def getcmd(cmdlist):
    cmd = input('\nYou:> ')
    if cmd in cmdlist:
        return cmd
    else:
        print('\n   error. invalid command-\n')
        return getcmd(cmdlist)

#Allows the user to pick_up an item from the current room
def pick_up(player, object_name):
    room_objects = player.Room.objects
    #Checks the room actually contains objects
    if room_objects:
        for objec in room_objects:
            if objec.name == object_name:
                valid = player.add_item(objec)

                #player.add_item() returns true or false depending on whether or not the object could be added.
                if valid:
                    room_objects.remove(objec)
                    return "Added {0} to inventory.".format(object_name)
                else:
                    return "You already have a {0} in your inventory.".format(object_name)
            
        return "No object with that name in the current room\nYou can see the name of objects by inspecting them using inspect <object_type>"
    else:
        return "There are no objects to pick up"

#Allows the player to drop an object to the floor
def drop(player, object_name):

    #if the players inventory is empty stop here
    if player.inventory_empty():
        return "Your inventory is empty. There is nothing drop"

    #
    objec = player.remove_item(object_name)
    
    #player.remove_item() returns true or false depending on whether or not the object could be removed.
    if objec:
        player.Room.objects.append(objec)
        return "You dropped {0}.".format(object_name)
    else:
        return "You dont have an object called {0} in your inventory".format(object_name)


def view_inventory(player):
    return player.get_inventory()


def converse(player,NPC):

    enemyometer = 5

    print(" You are conversing with " + NPC.name)

    # SQL Dialogue Tree?

    udict = {"Billy": ["Go AWAY Billy" , "Nice to meet you Billy", "Billy can you just leave please i don't like you","what do you call a white tiger, a tiger"]}
    edict = {"Billy":["hi my names billy", "you cheeky bugger", "Nice to meet you too","go f*** yourself","nice joke pal"]}

    dpos = 0

    uresponse = udict[NPC.name]
    edict = edict[NPC.name]


    

    print("3- Attack")
    chattree = {"Billy": [" "]}
    cmdlist = ['1', '2', '3']
    cmd = getcmd(cmdlist)





    if enemyometer < 1:
        fight(player.inventory["Weapon"][0], NPC, False)

    if enemyometer > 8:
        print("Would you like to recruit " + NPC.name + "Into your party\n")
        print("1- Yes")
        print("2- Nae Chance")

        cmdlist = ['1', '2']
        cmd = getcmd(cmdlist)

        if cmd == 1:
            #Method that handles parties
            return
        elif cmd == 2:
            return




#Test data
Zombie1 = Zombie("timmy",10)
Zombie2 = Zombie("tommy",3)
Spider = Spider("Shelob", 5)
weapon1 = Weapon("Sword of 1000 Truths", "It was foretold, that one day, heroes who could wield the sword might reveal themselves.", 2, 10, 2)
lore1 = Lore("Necronomicon", "Book of dead names. Read at your own peril", 1, "Ph\'nglui mglw\'nafh Cthulhu R\'lyeh wgah\'nagl fhtagn")
Barney = NPC("Barney", "A tall, fat man.", "long description", 100, "Chaotic Neutral", None)
Billy = NPC("Billy", "A short, thin man.", "long description", 100, "Chaotic Neutral", None)
dark_room = Room("Spooky Room", [Barney, Billy], [Zombie1, Spider, Zombie2], [weapon1, lore1], " a dark dillapidated room with no windows")
player = PC("username", 6, Room = dark_room)

#Tests
print(inspect(player.Room))
print(inspect(player.Room, player.level, "apple"))

#Inventory test
print("\nInventory Tests:\n")
print(view_inventory(player))
print(drop(player, "iten"))
print(inspect(player.Room, player.level, "Lore"))
print(pick_up(player, "Necronomicon"))
print(view_inventory(player))
print(inspect(player.Room, player.level, "Lore"))
print(drop(player, "Necro"))
print(drop(player, "Necronomicon"))
print(inspect(player.Room, player.level, "Lore"))
#fight(weapon1,Zombie1,True)
