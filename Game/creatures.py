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

    @abstractmethod
    def __str__(self):
        pass

    def get_type(self):
        return self.__class__.__name__

class Spider(Creature):

    def __init__(self, name, pl):
        hp = 10 * pl
        ap = 2 * pl
        super().__init__(name, hp, ap, ["Fire"], ["Water"], pl)
        

    def __str__(self):
        return ("{0} (Name: {1}, Health Points: {2},  Attack Points: {3}, Weaknesses: {4}, Strengths: {5}, Level: {6})".format(self.__class__.__name__, self.name, self.hp, self.ap, self.vulnerability, self.immune, self.power_level))


#Class Tests
spider = Spider("Shelob", 5)
print(spider.__str__())
print(spider.get_type())


    
