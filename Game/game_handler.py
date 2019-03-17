
import json
from django.shortcuts import render
from django.http import HttpResponse

try:
    from buildings import Building, Room
    from people import PC, NPC
    from creatures import Zombie, Spider
    from objects import Weapon, Lore
    from Scribbles_from_another_dimension import *
    from game_populate import build_game

except:
    # imports are different on Mac & on Windows so we have to do this
    from Game.buildings import Building, Room
    from Game.people import PC, NPC
    from Game.creatures import Zombie, Spider
    from Game.objects import Weapon, Lore
    from Game.Scribbles_from_another_dimension import *
    from Game.game_populate import build_game

player = PC("name", 1, [0, 0, 0])


def test_handle(text_in):
    print(text_in)
    output_dict = {"button1": "1", "button2": "2"}

    return HttpResponse(json.dumps(output_dict))


def handle(text_in):
    print("\n\nHERE BOI", text_in, "HERE BOI")
    print(text_in.decode("utf-8") + '\n\n')
    # cmds = text_in.split(",")
    # output_dict = {}
    # if cmds[0] == "move":
    #     move_room(cmds[1])
    # elif cmds[0] == "enter":
    #     enter(Building.objects.get(name=cmds[1]))
    # elif cmds[0] == "fight":
    #     fight(cmds[1], cmds[2], True)
    # elif cmds[0] == "exit":
    #     exit_current()
    # elif cmds[0] == "pick":
    #     pick_up(player, player.room.objects.get(name=cmds[1]))
    # elif cmds[0] == "talk":
    #     converse(player, NPC.objects.get(name=cmds[1]))
    # elif cmds[0] == "drop":
    #     drop(player, player.room.objects.get(name=cmds[1]))
    output_dict = {"this": "that"}
    # return render(HttpResponse, "Game/gamePage.html", json.dump(output_dict))


world = build_game()
player = world['player']
player.room = world["rooms"]["kitchen"]
player.position = [1, 1, 0]


def available_actions():
    data_post = {}
    '''REMEMBER TO CHANGE THE TOWER POSITION BELOW '''
    tower = Building.tower
    if player.position[0] != 0 or player.position[:-1] == [0, 5]:  # so if the player is in a building.
        data_post["move"] = []
        if player.room is not None:  # these are only done if we actually are in a room
            if not (player.room.objects == {} or player.room.objects is None):
                data_post["pick"] = []
                for obj in player.room.objects:
                    data_post["pick"].append(obj)
            if not player.room.creatures == {}:
                for creature in player.room.creatures:
                    data_post["fight"][creature.name] = {creature.description}
            if not player.room.NPCs == {}:
                data_post["npcs"] = []
                for npc in player.room.NPCs.values():
                    data_post["npcs"].append(npc.name)
        # from here on out, it's where we can move IF in a room, so it doesn't matter if we are in a room ,
        # just that we are in a building
        current_building = world["buildings"]["roofless house"]
        for room in current_building.rooms:
            if room.pos == player.position[2]:
                data_post['move'].append(room.name)
        if current_building.can_go_up(player.position[2]):
            data_post['floor up'] = '__'
        if current_building.can_go_down(player.position[2]):
            data_post['floor down'] = '__'
        data_post[" exit"] = ' '
        data_post["drop"] = []
        for cat in player.inventory:
            if player.inventory[cat] != []:
                for item in cat:
                    data_post["drop"].append(item)
        if player.inventory["Lore"] != {}:
            data_post["read"] = []
            for item in player.inventory["Lore"]:
                data_post['read'].append(item.text)
        if player.inventory["Food"] != {}:
            data_post['consume'] = []
            for item in player.inventory["Food"]:
                data_post['consume'].append(item.name)
    else:  # if not in a building ( so in the main road )
        if player.position[0] == 0:
            for building in world["buildings"].values():
                data_post['enter'] = []
                if building.position == player.position[:-1]:
                    data_post["enter"].append(building.name)
    print(json.dumps(data_post), "THIS DA DATA dumps")
    return HttpResponse(json.dumps(data_post))


def can_enter_buildings():
    output = []
    for bld in world["buildings"]:
        if bld.position == player.position[:-1]:
            output.append(bld)
    return output



