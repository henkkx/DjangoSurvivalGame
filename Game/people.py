from objects import *


class PC:
    def __init__(self, name, level, Room = None, hp=100):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.food = 50
        self.Room = Room
        self.level = level
        #self.inventory = {'stick': Objects('stick', "A simple stick", {'type': 'weapon', 'damage': 20})}

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
        return self.desc_S #returns a shorter description displayed upon entering the room.
