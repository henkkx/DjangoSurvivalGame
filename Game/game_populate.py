try:
    from Game.buildings import Building, Room
    from Game.objects import *
    from Game.people import PC, NPC
    from Game.creatures import *
except:
    from buildings import Building, Room
    from objects import *
    from people import PC, NPC
    from creatures import *

player = PC("PC")


class MasterOfPuppets:
    def __init__(self):
        self.objects = self.init_objects()
        self.NPCs = self.init_NPCs()
        self.creatures = self.init_creatures()
        self.rooms = self.init_rooms()
        self.buildings = self.init_buildings()

    def init_objects(self):
        output = {}
        output["Stick"]= Weapon("Stick", "A wooden stick, sturdy.", 1, 20, 5)
        output["Sword"] = Weapon("Sword", "A simple, standard medival sword", 1, 30, 5)
        output['Spear'] = Weapon("Spear", "A 2m long spear, steel tip, wooden shaft.", 1, 40, 10)
        output['Pipe'] = Weapon("Pipe", "A straight, steel pipe.", 1, 25, 5)

        #Changed final arguments to match object constuctor parameters
        output["Bread"] = Food("Bread", "An apparently fresh loaf of bread, smells like it just came out...of the oven",
                           1, 40, 20)
        output["Health Potion"] = Food("Health Potion", "It's small, it's red, come on this is in every game. Hm, maybe ours is green.",
                           1, 50, 0)
        output["Oat bar"] = Food("Oat bar", "An oat bar with raisins", 1, 20, 15)
        output["Burned note 1"] = Lore("Burned note #1", "A slightly burned piece of paper with scribbled writing. Looks like you wrote it",
                           1, "Why would I do that? How could I let this happen even?")
        output["Burned note 2"] = Lore("Burned note #2", "A slightly burned piece of paper with scribbled writing. Looks like you wrote it",
                           1, "Oh my god, the house burned out with the Doug still inside, and it's my fault")
        output["Tony's journal"] = Lore("Tony's journal", "The cover reads: 'My Journal' and below, in a kid's handwriting: 'By Tony'",
                           1, "Most of what Tony wrote show a kid who was bullied, nothing extreme that you don't see everyday, just kids havig fun in his expense</br>"
                              "You can clearly however, now, tell that his character wasn't equipped to take that. He mentions your name a few times.</br>"
                              "He says that you were good to him, helped him fell like he wasn't useless, says he could tell that sometimes,</br>"
                              "you didn't want to play with him because others you tease you for it, but you usually still did. He was more perceptive than you thought back then.")
        output["Crumbled note"] = Lore("Crumbled note", "A piece of paper with something written in it, crumbled up in a ball",
                                       1, "You recognise the handwritting but you are not sure where from:</br>"
                                          "Today was one of the bad days again, all the other kids made fun of me.</br>"
                                          "All except one, the one kid that has been good to me")


        return output

    def init_NPCs(self):
        output = {}
        output['Doug'] = NPC("Doug", "Your childhood dog, Doug", "Doug is a cross-breed labrador with german shepherd. Very playful",
                          150, "friendly", [Lore("Doug's collar", "It looks like it is painted red over green.",
                                                 1, "It used to be green, but as a kid you thought I'd be cooler\
                                                                 if it was red, so you painted over it with a marker")],
                             "Doug is very happy to see you, he is wagging his tail.</br>"
                             "You recall that you use to be an unreliable kid. You were playing with Doug once around the house and you threw the ball</br>"
                             "in the road, Doug chased it, hit the hob. The hob started hissing but you though nothing of it..</br>"
                             "Until a half hour later, thankfully there wasn't enough gas for an explosion out yet, but it did burn the whole house down.</br>"
                             "Doug didn't make it.")
        output["Tony"] = NPC("Tony", "Tony was your neighbour when you were kids, he lived two houses over", "Tony was a short, chubby and weak kid, shy although not a nerd or anything.",
                             70, "friendly", [],
                             "Tony turns around and looks at you. His face brights up as he sees you.</br>"
                             "You smile back as you see him and reach to shake his hand.</br>"
                             "He shakes your hand, then goes in for a hug</br>"
                             "'You cannot begin to understand how good it is to see you' he says.</br>"
                             "'Likewise', you reply, 'how have you been Tony?'</br>"
                             "'Very good, just wanted to let you know, when we were kids you helped me a lot, with the others messing with me and all that.</br>"
                             "You are confused, Tony looks just like you remembered him when you were kids, but talks of that time as if it was the past.</br>"
                             "As finished his sentence he turns back around, as if he doesn't realise you are there anymore.")

        return output

    def init_creatures(self):
        output = {}
        output['Charred fur rat'] = Rat("Charred fur rat", player.level)
        output["The Hound of Buskerville"] = Ghoul("The Hound of Buskerville", player.level)
        return output

    def init_rooms(self):
        output = {}
        output["default"] = Room("default", {}, {}, {}, "", -100)
        output["Kitchen"] = Room("Kitchen", {"Doug": self.NPCs["Doug"]}, {}, {"Bread": self.objects["Bread"]}, "You can smell spices, and a hint of both \
        garlic & onion. There are utensils & plates all around",0)
        output["Bedroom"] = Room("Bedroom", {}, {"Charred fur rat": self.creatures['Charred fur rat']}, {"Health Potion": self.objects["Health Potion"]}, "You are in a bedroom, single bed. Sheets indicate a child\
        slept here. In the corner a rat is munching on something",0)
        output["Living room"] = Room("Living room", {"Tony": self.NPCs["Tony"]}, {}, {"Bread": self.objects['Bread']},
                                     "The room reminds you of the living room of a childhood friend of yours. You don't remember who though.",0)
        output["Attic"] = Room("Attic", {}, {},{"Tony's journal": self.objects["Tony's journal"]},
                               "A standard Attic, a poster reading 'Who Watches The Watchmen' halfs hangs on one side",1)
        output[""]
        return output

    def init_buildings(self):
        output = {}
        output["Roofless house"] = Building('Roofless house', "This house is made of stone. It's roof has fallen because it's old.",
                                [self.rooms["Kitchen"], self.rooms["Bedroom"]], [1, 0])
        output["Family house"] = Building("Family house", "This is a very standard family house. Looks relatively big, probably 3-4 bedrooms, maybe a guest house. Seems like it's freshly painted",
                                          [self.rooms["Living room"], self.rooms["Attic"]], [2, 0])
        output["TestBLD1"] = Building("TestBLD1", "Test house mate", [self.rooms["Attic"]], [1, 1])
        output["TestBLD2"] = Building("TestBLD2", "Test house mate", [self.rooms["Living room"]], [2, 1])
        return output

    def build_game(self):
        self.objects = self.init_objects()
        self.NPCs = self.init_NPCs()
        self.creatures = self.init_creatures()
        self.rooms = self.init_rooms()
        self.buildings = self.init_buildings()
        world = {"objects": self.objects, "NPCs": self.NPCs, "creatures": self.creatures, "rooms": self.rooms,
                 "buildings": self.buildings, "player": player}
        world["player"].position = [0, 0, 0]
        return world
