from abc import ABC, abstractmethod
class Creature(ABC):

    def __init__(self, name, hp, ap, vulnerability, immune, pl):

        self.name = name
        self.hp = hp
        self.ap = ap
        self.vulnerability = vulnerability
        self.immune = immune
        self.power_level = pl
        super().__init__()

    @abstarctmethod
    def __str__(self):
        pass
        

