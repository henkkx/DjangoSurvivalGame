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

#The following are all subclasses for the Objects superclass

class Weapon(Objects):
    def __init__(self, name, desc, size, dmg, raange):
        super().__init__(name, desc, size)
        self.dmg = dmg
        self.raange = raange
        #range stat which could be used depending on how combat works

        
    #self.__name__ prints the class name.
    def __str__(self):
        print("Type: {0}, Name: {1}, damage: {2} range: {3}\nDescripition: {4}".format(self.__class__.__name__, self.name, self.dmg, self.raange, self.desc))

    def read(self):
              print("Not sure how you plan on reading a weapon")

#Tests
weapon1 = Weapon("Sword of 1000 Truths", "It was foretold, that one day, heroes who could wield the sword might reveal themselves.", 2, 1000, 2)
weapon1.__str__()
weapon1.read()

            
