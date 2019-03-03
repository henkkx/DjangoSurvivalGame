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

    #Returns the type of the creature i.e Spider.
    def get_type(self):
        return self.__class__.__name__


    """ This can be used if monsters are to be fought individually
    returns a string which can be used to inform the player of the monsters
    strngth compraed to their own.
    """

    def level_comp(self, player_level):
        difference = player_level - self.power_level
        if difference in range(-1, 2):
            return "You seem to be similar in strength"
        elif difference > 1:
            return "They look weak"
        elif difference < 1:
            return "They look tough"

    
    @abstractmethod
    def __str__(self):
        return "{0} ({1}, Health Points : {2}, Difficulty : {3} )".format(self.name, self.type, self.hp
                                                                          ,self.power_level)
        #       BoatyMcBoatface (Spider, Health Points : 1000, Difficulty : Hard)


class Spider(Creature):

    def __init__(self, name, pl):
        hp = 10 * pl
        ap = 2 * pl
        super().__init__(name, hp, ap, ["Fire"], ["Water"], pl)

    def __str__(self):
        return ("{0} (Name: {1}, Health Points: {2},  Attack Points: {3}, Weaknesses: {4}, Strengths: {5}, Level: {6})".format(self.__class__.__name__, self.name, self.hp, self.ap, self.vulnerability, self.immune, self.power_level))


class hellhound(Creature):

    def __init__(self, name, pl):
        hp = 5 * pl
        ap = 6 * pl
        super().__init__(name, hp, ap, ["Silver","Water"], ["Fire"], pl)

    def __str__(self):
        return (
            "{0} (Name: {1}, Health Points: {2},  Attack Points: {3}, Weaknesses: {4}, Strengths: {5}, Level: {6})".format(
                self.__class__.__name__, self.name, self.hp, self.ap, self.vulnerability, self.immune,
                self.power_level))


class Ghoul(Creature):

    def __init__(self, name, pl):
        hp = 4 * pl
        ap = 3 * pl
        super().__init__(name, hp, ap, ["Silver","Fire"], ["Magic"], pl)

    def __str__(self):
        return (
            "{0} (Name: {1}, Health Points: {2},  Attack Points: {3}, Weaknesses: {4}, Strengths: {5}, Level: {6})".format(
                self.__class__.__name__, self.name, self.hp, self.ap, self.vulnerability, self.immune,
                self.power_level))


class Witch(Creature):

    def __init__(self, name, pl):
        hp = 7 * pl
        ap = 6 * pl
        super().__init__(name, hp, ap, ["Silver", "Fire"], ["Water", "Magic"], pl)

    def __str__(self):
        return (
            "{0} (Name: {1}, Health Points: {2},  Attack Points: {3}, Weaknesses: {4}, Strengths: {5}, Level: {6})".format(
                self.__class__.__name__, self.name, self.hp, self.ap, self.vulnerability, self.immune,
                self.power_level))


class Vampire(Creature):

    def __init__(self, name, pl):
        hp = 7 * pl
        ap = 4 * pl
        super().__init__(name, hp, ap, ["Silver", "Water", "Garlic", "Fire"], ["Magic", "Poison"], pl)

    def __str__(self):
        return (
            "{0} (Name: {1}, Health Points: {2},  Attack Points: {3}, Weaknesses: {4}, Strengths: {5}, Level: {6})".format(
                self.__class__.__name__, self.name, self.hp, self.ap, self.vulnerability, self.immune,
                self.power_level))


class Rat(Creature):

    def __init__(self, name, pl):
        hp = 1 * pl
        ap = 1 * pl
        super().__init__(name, hp, ap, ["None"], ["None"], pl)

    def __str__(self):
        return (
            "{0} (Name: {1}, Health Points: {2},  Attack Points: {3}, Weaknesses: {4}, Strengths: {5}, Level: {6})".format(
                self.__class__.__name__, self.name, self.hp, self.ap, self.vulnerability, self.immune,
                self.power_level))


class Zombie(Creature):

    def __init__(self, name, pl):
        hp = 4 * pl
        ap = 3 * pl
        super().__init__(name, hp, ap, ["Fire","Magic","Silver","Poison"], ["None"], pl)

    def __str__(self):
        return (
            "{0} (Name: {1}, Health Points: {2},  Attack Points: {3}, Weaknesses: {4}, Strengths: {5}, Level: {6})".format(
                self.__class__.__name__, self.name, self.hp, self.ap, self.vulnerability, self.immune,
                self.power_level))


#Class Tests
"""
spider = Spider("Shelob", 5)
print(spider.__str__())
hellhound = hellhound("buster",10)
print(hellhound.__str__())
ghoul = ghoul("hy",10)
print(ghoul.__str__())
Vampire = Vampire("er",10)
print(Vampire.__str__())
Witch = Witch("sd",10)
print(Witch.__str__())
Rat = Rat("3d",10)
print(Rat.__str__())
Zombie = Zombie("timmy",10)
print(Zombie.__str__())
print(Zombie.get_type())
"""
