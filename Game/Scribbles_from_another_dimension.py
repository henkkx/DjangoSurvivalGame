"""
functions:
enter
converse
fight
interact
"""
try:
    from buildings import Building, Room
    from people import PC, NPC
    from creatures import Zombie, Spider
    from objects import Weapon, Lore, Food
    from game_populate import MasterOfPuppets
    from models import *
except:
    # imports are different on Mac & on Windows so we have to do this
    from Game.buildings import Building, Room
    from Game.people import PC, NPC
    from Game.creatures import Zombie, Spider
    from Game.objects import Weapon, Lore
    from Game.game_populate import MasterOfPuppets
    from Game.models import *
import json
from django.http import HttpResponse

'''
The player starts on a road. They can only see & enter 2 buildings. In each building there are rooms,
sometimes in different floors that they can enter. In the rooms they may fight creatures, converse with NPCs,
interact with objects. They may only exit when on the ground floor. When exiting a "fog" forces them to the
next row of another 2 buildings, until they either die of hunger ( on exit of building hunger is reduced) or in a fight
or reach the end ( the end is wherever there are no more buildings)
.
All of the functions that run the game are practically here, they are not a lot but it's still a long file,
Brace yourselves

NOTE: The input parameters of the functions will be explained at the handle() function as it's the one
which uses all of these
'''
player = PC("PC") # global, the player of the game ( not Django Player model)
world = None # the dictionary the world exists in
# the following two booleans are just for checks in the game, game_over means we died,
# end_was_reached means we finished the game
game_over = False
end_was_reached = False
response = "Welcome to our world, adventurer" # global, the text printed on the screen of the website
player_model = None # the Django Model for the Player which is connected to a User


def initialise(inp):
    '''This functions initializes the player_model, and then the game itself
    In other words, we now know which user is playing'''
    global player_model
    player_model = Player.objects.get_or_create(user=User.objects.get(username=inp))[0]
    # if not player_model.most_people:
    #     player_model.most_people = 0
    # if not player_model.most_exp:
    #     player_model.most_exp = 0
    # if not player_model.most_days_survived:
    #     player_model.most_days_survived = 0
    # if not player_model.most_kills:
    #     player_model.most_kills = 0
    print("initialised")
    game_initialisation()


def fight(creature):
    ''' This function runs the fight between the player & parameter creature.
    '''
    global response, game_over, player
    for c in player.room.creatures.values():
        if c.name == creature:
            creature = c
            break
    player_damage = 5 # default player damage if the player holds no weapon
    print(player.hp, player_damage, creature.hp, creature.ap) # just for reference in the console if we need to
    for weapon in player.inventory["Weapon"]:
        # will take the stronger weapon in the inventory are the one used
        if weapon.dmg > player_damage:
            player_damage = weapon.dmg
    if not (player_damage <= 0 and creature.ap <= 0):
        while True:
            # runs the fight, player strikes first, one by one with the creature, whoever dies first loses
            creature.hp -= player_damage
            if creature.hp <= 0:
                response = "You killed a {0} and gained {2} xp points.</br> You now have {1} hp.".format(creature.name, player.hp, creature.xp)
                player_model.stats["exp"] += creature.xp
                player.room.creatures.pop(creature.name)
                if player_model.stats["kills"] != 0:
                    player_model.stats["kills"] += 1
                else:
                    player_model.stats["kills"] = 1
                return True
            player.hp -= creature.ap
            if player.hp <= 0:
                response = "YOU DIED"
                game_over = True
                return False
    else:
        response = "You can't fight with that creature because you both deal no damage," \
                   " as in you literally heal each other, odd."
        # the above should never happen, just in case though


# Allows the user to pick_up an item from the current room
def pick_up(object_name):
    global player, response
    if player.room is None:
        return "You are not in a room"
    room_objects = player.room.objects

    # Checks the room actually contains objects
    if room_objects:
        for objec in room_objects.values():
            if objec.name.lower() == object_name.lower():
                valid = player.add_item(objec)

                #player.add_item() returns true or false depending on whether or not the object could be added.
                if valid:
                    room_objects.pop(object_name)
                    response = "Added {0} to inventory.".format(object_name)
                    break
                else:
                    response = "You already have a {0} in your inventory.".format(object_name)
            
        return "No object with that name in the current room\nYou can see the name of objects by inspecting them using inspect <object_type>"
    else:
        return "There are no objects to pick up"


# Allows the player to drop an object to the floor
def drop(object_name):
    global response, player
    if player.room is None:
        return "You must be within a room to drop an item"

    # if the players inventory is empty stop here
    if player.inventory_empty():
        return "Your inventory is empty. There is nothing drop"

    objec = player.remove_item(object_name)

    #player.remove_item() returns true or false depending on whether or not the object could be removed.
    if objec:
        player.room.objects[objec.name] = objec
        response = "You dropped {0}.".format(object_name)
    else:
        return "You dont have an object called {0} in your inventory".format(object_name)



def available():
    '''Gives the available buildings where we currently are'''
    current_buildings_avail = []
    if player.position[0] == 0:
        for building in world["buildings"].values():
            if building.position[1] == player.position[1]:
                current_buildings_avail.append(building)
    else:
        return "Already in a building"

    return current_buildings_avail


def enter(building):
    '''Makes the player enter a building'''
    global response, player_model, player, world
    response = ""
    try:
        for bld in world["buildings"].values():
            if bld.name in building:
                building = bld
                break
    except:
        game_initialisation()  # will re-initialise the game if world is empty, the error came up randomly

    if building in available():
        new_pos = building.position[:]
        new_pos.append(0)
        player.position = new_pos
        response = "In {0} there are the following rooms:</br>".format(building.name)
        for room in building.rooms:
            if room.pos == 0:
                response += room.name + "</br>"
        return True
        # so enter the building the player chose , on ground floor, hence the append 0 for floor number
    return False


def exit_current():
    ''' Makes the player exit the building & sets the position to the next row of buildings'''
    global response, player_model, game_over, end_was_reached
    bld_check = True  # this will check that there are buildings available , so we haven't reached the end of the world
    if player.position[2] == 0:  # if on ground floor
        player.position = [0, player.position[1]+1, 0]
        player.room = None
        player.hunger -= 20
        if player.hunger < 0: # checks that the player hasn't died of hunger
            response = "You died of hunger"
            game_over = True
            return;

        # below we show the buildings that are in the place we just exit to
        response = "You are now on the street. </br>" \
                   "The fog is advancing as you step out of the building, you have to move forward in order to escape it.</br>" \
                   "You can see what seems like a sun ever so slightly raising  itself up in the horizon, you keep walking, the fog keeps guiding.</br>" \
                   "As the sun sets and the fog gets darker due to the lack of light, it starts to open up in front of you.</br>" \
                   "You can now see two more buildings on your left and right.</br>" \
                   "You can feel your belly rumbling. Your hunger is now {0}/{1}</br> ".format(player.hunger, player.max_hunger)
        player_model.stats["days"] += 1

        for bld in world["buildings"].values():
            if bld.position[1] == player.position[1]:
                bld_check = False
                response += bld.description + "</br>"
    if bld_check:
        end_was_reached = True
    print(bld_check)
    player.room = world['rooms']['default']  # error prevention

    # below we create a checkpoint for the user to load
    to_store = {"position": player.position[:], "inventory": player.inventory.copy(),
                "hunger": player.hunger, "hp": player.hp, "stats": player_model.stats, "text": response}
    player_model.current_game = to_store
    player_model.save()
    check_achievements()
    check_stats()
        # which means back to main road (0) on the level we are (player.position), placeholder ground floor (0)


def move_room(room):
    ''' Moves the player to another parameter room. Room is the name so we have to go through the objects to find it'''
    global response
    for bld in world["buildings"].values():
        if player.position[:-1] == bld.position:
            for r in bld.rooms:
                if room == r.name:
                    player.room = r
                    response = str(r.desc)
                    return True
    return False


def move_floor(move):
    ''' Moves the player either one floor up or down, indicated by parameter move ( = "up" or "down"'''
    global response
    response = "You move floor, now you see the following rooms:</br>"
    for bld in world["buildings"].values():
        if bld.position == player.position[:-1]:
            building = bld
    if move == "up":
        if building.can_go_up(player.position[2]):
            player.position[2] += 1
            response = ""
    if move == "down":
        if building.can_go_down(player.position[2]):
            player.position[2] -= 1
            response = ""
    for room in building.rooms:
        response += room.name + ", "
    player.room = world["rooms"]["default"]


def converse(npc):
    '''Will display the conversation text with the NPC specified, again NPC is a name, we have to go through the objects
    to find them'''
    global response
    for n in world["NPCs"].values():
        if npc == n.name:
            response = n.conversation
            if player_model.stats["npcs"] != 0:
                player_model.stats["npcs"] += 1
            else:
                player_model.stats["npcs"] = 1


def consume(food_name):
    ''' Consume food with name food_name, runs PC.eat(food) in file people.py to do it '''
    global response, player
    response = "Got into consume"
    if player.inventory["Food"] == []:
        response = "You aren't carrying any food."

    food_list = player.inventory["Food"]
    for food in food_list:
        if food.name == food_name:
            response = player.eat(food)
        
    return "You dont have any food items with the name {0}".format(food_name)


def handle(text_in):
    ''' :param text_in is a string received from the web-app. We split by space, index 0 is the commands, everything else are the parameters
    Some like Move, come in as Move to (room name) hence the parameters are from index 2 and onward.'''
    global world, player, response, player_model
    cmds = text_in.decode("utf-8").split(" ")
    if cmds[0] == "Move":
        move_room(" ".join(cmds[2:]))
    elif cmds[0] == "Enter":
        enter(" ".join(cmds[1:]))
    elif cmds[0] == "Fight":
        fight(" ".join(cmds[1:]))
    elif cmds[0] == "Exit":
        exit_current()
    elif cmds[0] == "Pick":
        pick_up(" ".join(cmds[1:]))
    elif cmds[0] == "Talk":
        converse(" ".join(cmds[2:]))
    elif cmds[0] == "Drop":
        drop(" ".join(cmds[1:]))
    elif cmds[0] == "Consume":
        consume(" ".join(cmds[1:]))
    elif cmds[0] == "New":
        game_initialisation()
    elif cmds[0] == "Load":
        load_game()
        print(player.position, "This is the player Load is using")
    elif cmds[0] == "Inventory":
        response = player.get_inventory()
    elif cmds[0] == "Floor":
        move_floor(cmds[1])
    elif cmds[0] == "Game":
        response = "The game is over. Click new game to start another"
    elif cmds[0] == "Read":
        response = world["objects"][" ".join(cmds[1:])].text


def check_stats():
    ''' This function checks & updates the statistic of the Player model ( so the User)'''
    if player_model.most_kills < player_model.stats["kills"]:
        player_model.most_kills = player_model.stats["kills"]
    player_model.stats["kills"] = 0
    if player_model.most_people < player_model.stats["npcs"]:
        player_model.most_people = player_model.stats["npcs"]
    player_model.stats["npcs"] = 0
    if player_model.most_days_survived < player_model.stats["days"]:
        player_model.most_days_survived = player_model.stats["days"]
    player_model.stats["days"] = 0
    if player_model.most_exp < player_model.stats["exp"]:
        player_model.most_exp = player_model.stats["exp"]
    player_model.stats["exp"] = 0
    player_model.games_played += 1
    player_model.save()


def game_initialisation():
    ''' Initialises the game'''
    global world, game_over, player, response, end_was_reached
    check_stats()
    __ = MasterOfPuppets()
    world = __.build_game()
    game_over = False
    end_was_reached = False
    if world["player"]:
        player = world["player"]
        player.inventory = {"Weapon": [world['objects']['Stick']], "Lore": [], "Food": []}
        player.position = [0, 0, 0]
        player.room = world['rooms']['default']
        player.hunger = player.max_hunger
        player.hp = player.max_hp
    else:
        player = PC("PC")
    response = "You are in a... place, surrounded by fog.</br>" \
               "The fog doesn't look very thick but you can still see nothing through it.</br>" \
               "You try walking through it only to appear 10 metres on the opposite side you entered from, like a portal</br>" \
               "It slowly opens, creating a path which you follow.</br>" \
               "After a few minutes of walking, you see the fog opening up a bit wider. You can see two buildings.</br>" \
                "{0} </br> {1} </br>".format(world['buildings']["Roofless house"], world["buildings"]["Family house"])




def load_game():
    '''Loads the last checkpoint the player(User) was at'''
    global player, world, response, player_model
    game_initialisation()
    player_model.games_played -= 1
    if player_model.current_game is not None:
        player = PC("PC", position=player_model.current_game["position"][:],
                    inventory=player_model.current_game["inventory"].copy(),
                    hunger=player_model.current_game['hunger'],
                    hp=player_model.current_game["hp"])
        player_model.stats = player_model.current_game["stats"]
        response = player_model.current_game["text"]
    else:
        response = "No game to load"
    player_model.save()

# player = build_game()
# player.position = [0, 0, 0]


def available_actions():
    ''' This function will go through the whole world. It will return a json of all the available actions
    that the player can currently perform
    For details of how it works, it's better to look at game_populate.py for the datatypes of all the data'''
    global player_model, response\

    if game_over:  # if the player has died
        return json.dumps({"Game over": " ", "text": response})

    if end_was_reached:  # if the player has reached the end of the world
        response = "As you traverse through the fog, you suddenly see a light.</br>" \
                   "The light comes closer to reveal 2 figures, about 40cm tall each, levitating in front of you.</br>" \
                   "One is dressed in a white robe, fair skinned with long, light brown hair. The other had red skin, no hair and horns</br>" \
                   "An angel and a demon.</br>" \
                   "They both ask, saying one word each:</br>" \
                   "So, soul, where do you think you have to go from here on. Up or Down?</br>" \
                   "The figures smile.</br>"
        return json.dumps({"text": response})

    check_achievements()
    data_post = {}
    '''REMEMBER TO CHANGE THE TOWER POSITION BELOW '''
    data_post["Inventory"] = " "
    data_post["text"] = response
    if player.position[0] != 0 or player.position[:-1] == [0, 5]:  # so if the player is in a building.
        data_post["Move to"] = []
        if player.room is not None:  # these are only done if we actually are in a room
            if not (player.room.objects == {} or player.room.objects is None):
                data_post["Pick"] = []
                for obj in player.room.objects:
                    data_post["Pick"].append(obj)
            if not player.room.creatures == {}:
                data_post["Fight"] = []
                for creature in player.room.creatures.values():
                    data_post["Fight"].append(creature.name)
            if not player.room.NPCs == {}:
                data_post["Talk to"] = []
                for npc in player.room.NPCs.values():
                    data_post["Talk to"].append(npc.name)
        # from here on out, it's where we can move IF in a room, so it doesn't matter if we are in a room ,
        # just that we are in a building
        for bld in world["buildings"].values():
            if player.position[:-1] == bld.position:
                current_building = bld
        for room in current_building.rooms:
            current_room = "default"
            try:
                current_room = player.room.name
            except:
                print("Player is not in a building/room") # this error should never happen anymore
            if room.pos == player.position[2] and room.name != current_room:
                data_post['Move to'].append(room.name)
        if current_building.can_go_up(player.position[2]):
            data_post['Floor up'] = ' '
        if current_building.can_go_down(player.position[2]):
            data_post['Floor down'] = ' '
        data_post["Drop"] = []
        for cat in player.inventory:
            if player.inventory[cat] != [] and current_room != "default":
                for item in player.inventory[cat]:
                    data_post["Drop"].append(item.name)
        if player.inventory["Lore"] != {}:
            data_post["Read"] = []
            for item in player.inventory["Lore"]:
                data_post['Read'].append(item.name)
        if player.inventory["Food"] != {}:
            data_post['Consume'] = []
            for item in player.inventory["Food"]:
                data_post['Consume'].append(item.name)
    else:  # if not in a building ( so in the main road )
        if player.position[0] == 0:
            data_post['Enter'] = []
            for building in world["buildings"].values():
                if building.position[1] == player.position[1]:
                    data_post["Enter"].append(building.name)
    if player.position[2] == 0 and player.position[0] != 0:
        data_post["Exit"] = " "
    return json.dumps(data_post)


def can_enter_buildings():
    ''' Self-explanatory, if we can enter a building'''
    output = []
    for bld in world["buildings"]:
        if bld.position == player.position[:-1]:
            output.append(bld)
    return output


def check_achievements():
    '''This function will update the achievments of the player depending on their stats'''
    global player_model
    for bdg in Badge.objects.all():
        if player_model.stats[bdg.badge_type] >= bdg.criteria:
            Achievement.objects.get_or_create(player=player_model, badge=bdg)