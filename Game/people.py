from Game.objects import *

class PC:
    def __init__(self, name, hp=100, room=[0, 0]):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.food = 50
        self.room = room
        self.level = 1
        # self.inventory = {'stick': Objects('stick', "A simple stick", {'type': 'weapon', 'damage': 20})}

    def get_room(self):
        return self.room

    def get_level(self):
        return self.level

    def __str__(self):
        return "Player {0} has {1}/{2} hp".format(self.name, self.hp, self.max_hp)

class NPC:
    def __init__(self, name, short_description,long_description, hp, allegiance, inventory):
        self.name = name
        self.desc_S = short_description
        self.desc_L = long_description
        self.hp = hp
        self.allegiance = allegiance
        self.inventory = inventory

    def __str__(self):
        return self.description  # returns the description since we shouldn't know names, just how they look

    def get_short(self):
        return self.desc_S
