class Creature:

    def __init__(self, name, type, hp, ap, vulnerability, immune, pl):

        self.name = name
        self.type = type
        self.hp = hp
        self.ap = ap
        self.vulnerability = vulnerability
        self.immune = immune
        self.power_level = pl

    def __str__(self):
        return "{0} ({1}, Health Points : {2}, Difficulty : {3} )".format(self.name, self.type, self.hp
                                                                          ,self.power_level)
        #       BoatyMcBoatface (Spider, Health Points : 1000, Difficulty : Hard)
