"""
functions:
enter
converse
fight
interact
"""
import time
try:
    from buildings import Building, Room
    from people import PC, NPC
    from creatures import Zombie, Spider
    from objects import Weapon, Lore, Food
except:
    # imports are different on Mac & on Windows so we have to do this
    from Game.buildings import Building, Room
    from Game.people import PC, NPC
    from Game.creatures import Zombie, Spider
    from Game.objects import Weapon, Lore


houses = {}
road_objects = {}  # probably won't use this, but better have it and delete later
road_people = {}  # again, probably won't be used we'll see
world = {'buildings': houses, 'objects': road_objects, 'people': road_people}


#This function displays information about the specified object or creature.
#If no arguments are passed the current room will be described.
#It makes use of the get_description method in the rooms class. Take a look.
def inspect(player, entity=None):
    room = player.room
    pl = player.level
    if room is None:
        return "You are on the street"
    if entity is None:
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


def fight(weapon, creatures, launch):

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


# Temporary Method To Get Command line input
def getcmd(cmdlist):
    cmd = input('\nYou:> ')
    if cmd in cmdlist:
        return cmd
    else:
        print('\n   error. invalid command-\n')
        return getcmd(cmdlist)


# Allows the user to pick_up an item from the current room
def pick_up(player, object_name):
    if player.room == None:
        return "You are not in a room"
    room_objects = player.room.objects
    # Checks the room actually contains objects
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

    if player.room == None:
        return "You must be within a room to drop an item"

    #if the players inventory is empty stop here
    if player.inventory_empty():
        return "Your inventory is empty. There is nothing drop"

    #
    objec = player.remove_item(object_name)
    
    #player.remove_item() returns true or false depending on whether or not the object could be removed.
    if objec:
        player.room.objects.append(objec)
        return "You dropped {0}.".format(object_name)
    else:
        return "You dont have an object called {0} in your inventory".format(object_name)


def view_inventory(player):
    return player.get_inventory()

'''
Below are all the functions related to moving. For now we will have:
 "available" which will return the available buildings to enter when on the road
 "enter" which is to enter either building on your sides
 "exit_current" which is to exit the building you are currently in ( if on the ground floor)
 "move_room" which moves you between rooms,
 "move_floor" which is to either go a floor up or a floor down
 
 Might be better if we move some of these in the Building class so we don't need to pass building,
  we'll then need to pass player though
  
  Although they don't need to return True or False, it'll help debuggins so at least for now they do
 '''


def available():
    current_buildings_avail = []
    if player.position[0] == 0:
        for building in world["buildings"]:
            if building.position[1] == player.position[1]:
                current_buildings_avail.append(building)
    else:
        return "Already in a building"

    return current_buildings_avail


def enter(building):
    if building in available():
        player.position = building.position.append(0)
        return True
        # so enter the building the player chose , on ground floor, hence the append 0 for floor number
    return False


def exit_current():
    if player.position[2] == 0: # if on ground floor
        player.position = [0, player.position[1]+1, 0]
        player.room = None
        return True
        # which means back to main road (0) on the level we are (player.position), placeholder ground floor (0)
    return False


def move_room(room):
    if room.name in Building.objects.get(position=player.position[:-1]): # so if the room is in the floor the player is currently in
        player.room = room
        return True
    return False


def move_floor(building, move):
    if move == "up":
        if building.can_go_up(player.position[2]):
            player.position[2] += 1
            return True
    if move == "down":
        if building.can_go_down(player.position[2]):
            player.position[2] -= 1
            return True
    return False


def converse(player, NPC):

    enemyometer = 5  # NPC anger levels

    print("You are conversing with " + NPC.name ,"\n")

    #Dialogue For Characaters And User Responses

    edict = {"Billy": {0: ["My Name is Billy"], 1: ["you cheeky bugger", -11, "nice to meet you", 12,
                                "Would you like some Vbucks kid"], 99: ["You bastard I will destroy you "], 101: 1}}

    udict = {"Billy": {0: ["Nah mate leave me alone", "Hi there sir"]}}
    dpos = 0  # Position in Conversation, User response indexed in dict using dpos, In edict npc responses
              # indexed using dpos+1 because of inital message from character when conversation starts

    print(NPC.name, ": ", edict[NPC.name][dpos][0])  # initial message at index 0 from NPC when conversing
    lengthofconvo = edict[NPC.name][101]             # length of the conversation kept in dict with key value 101

    while dpos < lengthofconvo:

        print("1-" , udict[NPC.name][dpos][0])
        print("2-", udict[NPC.name][dpos][1])
        print("3- Attack")
        cmdlist = ['1', '2', '3']
        cmd = getcmd(cmdlist)

        if cmd == '1':
            print("You : ", udict[NPC.name][dpos][0], "\n")
            print(NPC.name, ": ", edict[NPC.name][dpos+1][0])

            enemyometer += edict[NPC.name][dpos+1][0+1]

        if cmd == '2':
            print("You : ", udict[NPC.name][dpos][1], "\n")
            print(NPC.name, ": ", edict[NPC.name][dpos+1][2])

            enemyometer += edict[NPC.name][dpos+1][1+2]

        if cmd == '3':
            fight(player.inventory["Weapon"][0], NPC, True)
            return

        print(NPC.name, ": ", edict[NPC.name][dpos+1][-1])
        dpos += 1

        if enemyometer < 1:
            break

        continue

    if enemyometer < 1:
        print(NPC.name + " : " + edict[NPC.name][99][0] + "\n") # dict with key value 99 shows pre fight message
        fight(player.inventory["Weapon"][0], NPC, False)

    if enemyometer > 8:
        print(NPC.name + " Really likes you, Would you like to recruit " + NPC.name + " Into your party\n")
        print("1- Yes")
        print("2- Nae Chance")

        cmdlist = ['1', '2']
        cmd = getcmd(cmdlist)

        if cmd == 1:
            #Method that handles parties
            return
        elif cmd == 2:
            return

def consume(player, food_name):
    if player.inventory["Food"] == []:
        return "You arent carrying any food."

    food_list = player.inventory["Food"]
    for food in food_list:
        if food.name == food_name:
            return player.eat(food)
        
    return "You dont have any food items with the name {0}".format(food_name)
    



"""
#Test data
# Zombie1 = Zombie("timmy",10)
# Zombie2 = Zombie("tommy",3)
# Spider = Spider("Shelob", 5)
# weapon1 = Weapon("Sword of 1000 Truths", "It was foretold, that one day, heroes who could wield the sword might reveal themselves.", 2, 10, 2)
# lore1 = Lore("Necronomicon", "Book of dead names. Read at your own peril", 1, "Ph\'nglui mglw\'nafh Cthulhu R\'lyeh wgah\'nagl fhtagn")
# Barney = NPC("Barney", "A tall, fat man.", "long description", 100, "Chaotic Neutral", None)
# Billy = NPC("Billy", "A short, thin man.", "long description", 100, "Chaotic Neutral", None)
# dark_room = Room("Spooky Room", [Barney, Billy], [Zombie1, Spider, Zombie2], [weapon1, lore1], " a dark dillapidated room with no windows", None)
# player = PC("username", 6, position = None)
#player.room = dark_room
player = PC("username", 6, position=None)

#Tests
#print(inspect(player.room))
#print(inspect(player.room, player.level, "apple"))

#Inventory test

print("\nInventory Tests:\n")
print(view_inventory(player))
print(drop(player, "iten"))
print(inspect(player, "Lore"))
print(pick_up(player, "Necronomicon"))
print(view_inventory(player))
print(inspect(player, "Lore"))
print(drop(player, "Necro"))
print(drop(player, "Necronomicon"))
print(inspect(player, "Lore"))
print(inspect(player))
print(inspect(player, "Food"))
print(view_inventory(player))
print(pick_up(player, "Cake"))
print(view_inventory(player))
player.hp -= 15
player.hunger -= 10
print(consume(player, "Apple"))
print(consume(player, "Cake"))
print(view_inventory(player))
print(consume(player, "Apple"))
print(inspect(player))
#fight(weapon1,Zombie1,True)


# Converse Tests
'''
player = PC("username", 6, None)

#player = PC("username", 6, None)
player.add_item(Weapon("na","na",12,12,22))
converse(player, Billy)
'''
"""
