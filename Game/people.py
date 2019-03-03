try:
    from objects import *
except:
    from Game.objects import *


class PC:
    def __init__(self, name, level, position=None, hp=100,):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.food = 50
        self.position = position
        self.room = None
        self.level = level
        self.inventory = {"Weapon": [], "Lore": [], "Food": []}

    def __str__(self):
        return "Player {0} has {1}/{2} hp".format(self.name, self.hp, self.max_hp)

    #adds item to inventory unless it is already stored.
    def add_item(self, item):
        if item not in self.inventory[item.get_type()]:
            self.inventory[item.get_type()].append(item)
            return True
        else:
            return False

    #removes a currently stored item. returns the removed object or None
    def remove_item(self, item_name):
        for item in self.get_inventory_as_list():
            if item.name == item_name:
                self.inventory[item.get_type()].remove(item)
                return item
        return None

    #For each object type, print objects of this type in the players inventory.
    def get_inventory(self):
        if self.inventory_empty():
            return "You have nothing in your inventory"
        
        output = []
        for kind in self.inventory:
            items = self.inventory[kind]
            if items:
                output.append("You have {0} {1}(s):".format(len(items), kind))
                for item in items:
                    output.append(item.__str__())
                output.append("")
            #else:
                #output.append("You have no {0} items".format(kind))

        return "\n".join(output)

    #Returns whether or not the players inventory is empty
    def inventory_empty(self):
        if not self.get_inventory_as_list():
            return True

        return False

    #returns the objects in the the players inventory as a list.
    def get_inventory_as_list(self):
        inventory_list = []
        for item_list in self.inventory.values():
            inventory_list.extend(item_list)

        return inventory_list
        

    

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

player = PC("Ban", 10)
sword = Weapon("Sword of 1000 Truths", "It was foretold, that one day, heroes who could wield the sword might reveal themselves.", 2, 10, 2)
print(player.add_item(sword))
print(player.add_item(sword))
print(player.get_inventory())
