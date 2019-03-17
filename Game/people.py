try:
    from objects import *
except:
    from Game.objects import *


class PC:
    def __init__(self, name, level, position=None, hp=100,):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.hunger = 50
        self.max_hunger = 50
        self.position = position
        self.room = None
        self.level = level
        self.inventory = {"Weapon": [], "Lore": [], "Food": []}

    def __str__(self):
        return "Player {0} has {1}/{2} hp".format(self.name, self.hp, self.max_hp)

    #adds item to inventory unless it is already stored.
    def add_item(self, item):
        if item not in self.inventory[item.get_type()] or item.get_type() == "Food":
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
                output.append("You have {0} {1} item(s):".format(len(items), kind))
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

    def eat(self, food):
        self.remove_item(food.name)
        if (self.hunger + food.nutrients) > self.max_hunger:
            self.hunger = self.max_hunger
        else:
            self.hunger += food.nutrients

        if (self.hp + food.hp_regen) > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += food.hp_regen
        
        return "Ate {0}. Hunger is now {1}/{2}. Health is now {3}/{4}".format(food.name, self.hunger, self.max_hunger, self.hp, self.max_hp)


class NPC:
    def __init__(self, name, short_description, long_description, hp, allegiance, inventory):
        self.name = name
        self.desc_S = short_description
        self.desc_L = long_description
        self.hp = hp
        self.allegiance = allegiance
        self.inventory = inventory
        try:
            if inventory is None:
                self.ap = 10
            else:
                self.ap = inventory["Weapon"][0]
        except:
            self.ap = 10
    def __str__(self):
        return self.description  # returns the description since we shouldn't know names, just how they look

    def get_short(self):
        return self.desc_S #returns a shorter description displayed upon entering the room.

player = PC("Ban", 10)
sword = Weapon("Sword of 1000 Truths", "It was foretold, that one day, heroes who could wield the sword might reveal themselves.", 2, 10, 2)
cake = Food("Cake", "A delicious sponge cake", 1, 5, 10)
print(player.add_item(sword))
print(player.add_item(sword))
print(player.add_item(cake))
print(player.add_item(cake))
player.hp -= 15
player.hunger -= 10
print(player.get_inventory())
print(player.eat(cake))
print(player.get_inventory())
