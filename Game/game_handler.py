
import json

try:
    from buildings import Building, Room
    from people import PC, NPC
    from creatures import Zombie, Spider
    from objects import Weapon, Lore
    from Scribbles_from_another_dimension import *
except:
    # imports are different on Mac & on Windows so we have to do this
    from Game.buildings import Building, Room
    from Game.people import PC, NPC
    from Game.creatures import Zombie, Spider
    from Game.objects import Weapon, Lore
    from Game.Scribbles_from_another_dimension import *


def handle(text_in):
    cmds = text_in.split(",")
    output_dict = {}
    if cmds[0] == "move":
        move_room(cmds[1])
    elif cmds[0] == "enter":
        enter(Building.objects.get(name=cmds[1]))
    elif cmds[0] == "fight":
        fight(cmds[1], cmds[2], True)
    elif cmds[0] == "exit":
        exit_current()
    elif cmds[0] == "pick":
        pick_up(player, player.room.objects.get(name=cmds[1]))
    elif cmds[0] == "talk":
        converse(player, NPC.objects.get(name=cmds[1]))
    elif cmds[0] == "drop":
        drop(player, player.room.objects.get(name=cmds[1]))

    json.dump(output_dict)


def available_actions():
    data_post = {}
    '''REMEMBER TO CHANGE THE TOWER POSITION BELOW '''
    tower = 5
    if player.position[0] != 0 or player.position[:-1] == [0,5]: # so if the player is in a building.
        data_post["move"] = {}
        if player.room is not None: # these are only done if we actually are in a room
            if not (player.room.objects == {}):
                for obj in player.room.objects:
                    data_post["objects"][obj.name] = obj.name
            if not player.room.creatures == {}:
                for creature in player.room.creatures:
                    data_post["fight"][creature.name] = {creature.description}
            if not player.room.NPC == {}:
                for npc in player.room.NPCs:
                    data_post["npcs"][NPC.name] = NPC.desc_L
        # from here on out, it's where we can move IF in a room, so it doesn't matter if we are in a room ,
        # just that we are in a building
        current_building = Building.objects.get(position=player.position[:-1])
        for room in current_building.rooms:
            if room.pos == player.position[2]:
                data_post['move'][room.name] = [room.name]
        if current_building.can_go_up(player.position[2]):
            data_post['floor up']
        if current_building.can_go_down(player.position[2]):
            data_post['floor down']
        data_post["exit"]
        for item in player.inventory["Lore"]:
            data_post['read'][item.name] = [item.text]
        for item in player.inventory["Food"]:
            data_post['consume'][item.name] = [item.name]
    else:  # if not in a building ( so in the main road )
        for building in Building.objects.get(position=player.position[:-1]):
            data_post["enter"][building.name] = building.description






