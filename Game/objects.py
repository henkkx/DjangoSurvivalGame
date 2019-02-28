#These are needed to define an abstract class and method
from abc import ABC, abstractmethod


class Objects(ABC):
    def __init__(self, name, desc, size):
        self.name = name
        self.desc = desc
        self.size = size
        super().__init__()
        #size could be used for a limited inventory space requirement

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def read(self):  
        pass

    def get_type(self):
        return self.__class__.__name__

#The following are all subclasses for the Objects superclass

class Weapon(Objects):
    def __init__(self, name, desc, size, dmg, range):
        super().__init__(name, desc, size)
        self.dmg = dmg
        self.range = range
        #range stat which could be used depending on how combat works

        
    #self.__name__ prints the class name.
    def __str__(self):
        return("Type: {0}, Name: {1}, damage: {2} range: {3} size: {4}\nDescripition: {5}".format(self.__class__.__name__, self.name, self.dmg, self.raange, self.size, self.desc))

    def read(self):
        return super.desc   #("Not sure how you plan on reading a weapon")

class Lore(Objects):
    def __init__(self, name, desc, size, text):
        super().__init__(name, desc, size)
        self.text = text
        #text holds the readable text
        

        
    #self.__name__ prints the class name.
    def __str__(self):
        return("Type: {0} item, Name: {1}, Size: {2} \nDescription: {3}".format(self.__class__.__name__, self.name, self.size, self.desc))

    def read(self):
        return (self.text)

class Food(Objects):
    def __init__(self, name, desc, size, nutrients):
        super().__init__(name, desc, size)
        self.nutrients = nutrients # LIST, [0] is the HP recovered, [1] is hunger recovered, [2] is a string, split by " " to get cured status when eaten
        #nutrients is a place holder until we work out how the eating sytem works
        
    #self.__name__ prints the class name.
    def __str__(self):
        return("Type: {0} item, Name: {1}, Size: {2}, Nutrional Value: {3}\nDescription: {4}".format(self.__class__.__name__, self.name, self.size, self.nutrients, self.desc))

    def read(self):
        return("How are you gonna read a {0}?".format(self.name))

"""
weapon1 = Weapon("Sword of 1000 Truths", "It was foretold, that one day, heroes who could wield the sword might reveal themselves.", 2, 1000, 2)
print("Weapon Example: ")
weapon1.__str__()
weapon1.read()
print()
print("Lore Object Example")
lore1 = Lore("Necronomicon", "Book of dead names. Read at your own peril", 1, "Ph\'nglui mglw\'nafh Cthulhu R\'lyeh wgah\'nagl fhtagn")
lore1.__str__()
lore1.read()
print()
print("Food Example: ")
food1 = Food("Cake", "A delicious sponge cake", 1, 5)
food1.__str__()
food1.read()
"""         
