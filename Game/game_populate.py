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

        output['Silver Sword'] = Weapon("Silver Sword", "A beautifully crafted silver peice A monster slayers weapon of choice",1, 70, 5)
        output['Red Balloon'] = Weapon("Red Balloon", "A magical balloon it seems to have powers", 1, 300, 10)
        output['Toothbrush'] = Weapon("Toothbrush", "A standard toothbrush", 1, 1, 1)
        output['Baseball Bat'] = Weapon("Baseball Bat", "My old favourite, woody the baseball bat"
                                                        "hasn't aged a day", 1, 25, 5)

        output['Brick'] = Weapon("Brick", "A large red brick", 1, 30, 15)
        output['MetalShard'] = Weapon("MetalShard", "A sharp piece of metal, it resembles a shank", 1, 35, 5)
        output['TimberBark'] = Weapon("TimberBark", "A sharp piece of timber could be dangerous", 1, 15, 5)

        #Changed final arguments to match object constuctor parameters
        output["Bread"] = Food("Bread", "An apparently fresh loaf of bread, smells like it just came out...of the oven",
                           1, 40, 5)
        output["Health Potion"] = Food("Health Potion", "It's small, it's red, come on this is in every game. Hm, maybe ours is green.",
                           1, 50, 0)
        output["Burned note 1"] = Lore("Burned note #1", "A slightly burned piece of paper with scribbled writing. Looks like you wrote it",
                           1, "Why would I do that? How could I let this happen even?")
        output["Burned note 2"] = Lore("Burned note #2", "A slightly burned piece of paper with scribbled writing. Looks like you wrote it",
                           1, "Oh my god, the house burned out with the Doug still inside, and it's my fault")
        output["Tony's journal"] = Lore("Tony's journal", "The cover reads: 'My Journal' and below, in a kid's handwriting: 'By Tony'",
                           1, "Most of what Tony wrote show a kid who was bullied, nothing extreme that you don't see everyday, just kids havig fun in his expense</br>"
                              "You can clearly however, now, tell that his character wasn't equipped to take that. He mentions your name a few times.</br>"
                              "He says that you were good to him, helped him fell like he wasn't useless, says he could tell that sometimes,</br>"
                              "you didn't want to play with him because others you tease you for it, but you usually still did. He was more perceptive than you thought back then.")

        #------ Neibolt -------

        output["Jam Sandwich"] = Food("Jam Sandwich","A beautiful sandwich made with a mothers touch",1,45,10)

        output["Bedroom Note"] = Lore("Bedroom Note", "A small note written by your father", 1,
                                       "The note reads: My Dear Son, this is to protect you from the monsters in"
                                       " your dreams, Lots of Love Dad ")

        output["Paper Plane"] = Lore("Paper Plane", "A small paper plane, magnificantly built", 1,
                                      "There appears to be a small note written under the wing it "
                                      "reads : WELCOME HOME MY SWEET PIE, ARE YOU HERE TO JOIN THE CIRCUS THIS TIME ")

        output["Attic Photo"] = Lore("Attic Photo", "A ripped image of a young boy", 1,
                                     "The photo appears to have been ripped in half (something sharp must have done it)"
                                     " on closer inspection the boys head seems to be visible it closely resembles "
                                     " ME ME ME ")

        #------ Innocent ------

        output["Gravestone Note"] = Lore("Gravestone Note","A handwritten note it appears to be written by a child",1,
                                         "YOU ARE TO BLAME, YOU KILLED ME, YOU KILLED ALL OF US, MAY THIS MEMORY NEVER LEAVE"
                                         " YOU, I WILL FOREVER PLAGUE YOUR DREAMS, AND TAKE YOUR LIFE AS YOU DID MINE!")

        output["Bedroom Photo"] = Lore("Bedroom Photo", "The image of a young child", 1,
                                         "The photo is twisted, blood pours from her eyes, her face seems distored a bloodied ")

        output["Bedroom Book"] = Lore("Bedroom Book", "The cover reads: Harry Potter, Property of : Emma", 1,
                                       "Harry Potter was a highly unusual boy in many ways. For one thing, he"
                                        "hated the summer holidays more than any other time of year. For another,"
                                        "he really wanted to do his homework but was forced to do it in secret,"
                                        "in the dead of night. And he also happened to be a wizard.....")

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
        return output

    def init_rooms(self):
        output = {}
        output["Kitchen"] = Room("Kitchen", {"Doug": self.NPCs["Doug"]}, {}, {"Bread": self.objects["Bread"]}, "You can smell spices, and a hint of both \
        garlic & onion. There are utensils & plates all around",0)
        output["Bedroom"] = Room("Bedroom", {}, {"Charred fur rat": self.creatures['Charred fur rat']}, {"Health Potion": self.objects["Health Potion"]}, "You are in a bedroom, single bed. Sheets indicate a child\
        slept here. In the corner a rat is munching on something",0)
        output["Living room"] = Room("Living room", {"Tony": self.NPCs["Tony"]}, {}, {"Bread": self.objects['Bread']},
                                     "The room reminds you of the living room of a childhood friend of yours. You don't remember who though.",0)
        output["Attic"] = Room("Attic", {}, {},{"Tony's journal": self.objects["Tony's journal"]},
                               "A standard Attic, a poster reading 'Who Watches The Watchmen' halfs hangs on one side",1)

        #-----------------------------------------Neibolt House Rooms -----------------------------------------------------#

        output["Neibolt Hallway"] = Room("Neibolt Hallway", {}, {}, {"Red Balloon": self.objects["Red Balloon"]}, "You enter the Hallway, A beuatiful large opening "
                         "However, something feels wrong, A dim dark staircase ahead claw marks going towards the basement "
                                " A red ballon seems to be leading you there. Stairs lead to the second floor, they look unsafe"
                                                                        " falling apart",0)

        output["Neibolt Basement"] = Room("Neibolt Basement",{},{},{"Paper Plane":self.objects["Paper Plane"]},"The ballon leads you to the basement, there is a creature just in the shadow, he "
                                                                      "seems to be lying down, His eyes fiery yellow, teeth as sharp as claws, "
                                                                      "his voice soothing & inviting, he resembles the creature that plaged your dreams as"
                                                                      " a child, he throws a paperplane towards you",-1)

        output["Neibolt Bedroom"] = Room("Neibolt Bedroom", {}, {}, {"Bedroom Note":self.objects["Bedroom Note"],"Baseball Bat": self.objects["Baseball Bat"]},"This room, this room it seems so familiar, MY BEDROOM THIS IS MY BEDROOM!."
                                                                       " an image hangs on the wall an old drawing of yours, it seems to resemble a clown holding a red balloon"
                                                                       " Under the bed there appears to be a baseball bat & a note",1)

        output["Neibolt Lavatory"] = Room("Neibolt Lavatory", {}, {}, {"Toothbrush": self.objects["Toothbrush"]},
                                         "The toilet seems to be working, Hmmm intresting [FLUSH] blood appears to flowing instead of water, unnerving "
                                         "There seems to be some tooth paste and a brush here also",1)

        output["Neibolt Kitchen"] = Room("Neibolt Kitchen", {}, {}, {"Jam Sandwich": self.objects["Jam Sandwich"]},"Hmmm this kitchen, it reminds you of home, there seems to be a sandwich on the table, You look up "
                                        "BLOOD smeered all over roof, it reads Welcome Home, What could this mean" ,0)

        output["Neibolt Attic"] = Room("Neibolt Attic", {}, {}, {"Attic Photo": self.objects["Attic Photo"],"Silver Sword": self.objects["Silver Sword"]},
                                         "The attic creaks, you hear movement below like a dog pancing quickly, Thats no dog no that fast "
                                         "There appears to be something shining off in the distance, a silver glimmer & and a photo", 2)

        # ---------------------------------------Murder House (Innocent House)---------------------------------------------------#

        output["Innocent Hallway"] = Room("Innocent Hallway", {}, {}, {},
                                         "This hallway, it appears to be warped, portals seem to be placed at each stairway they appear "
                                         "to give off a reverberating humming sound", 0)

        output["Innocent Garden"] = Room("Innocent Garden", {}, {}, {},
                                         "The portal sent me to a garden, a memory seems to be playing, a young girl seems to be playing with her"
                                         " family their faces they seems so familiar, There seems to be another portal decending down",-1)

        output["Innocent Garage"] = Room("Innocent Garage", {}, {}, {"Brick": self.objects["Brick"]},
                                         "In an instance i've arrived in a garage, there is a car, violent RED, there seems"
                                         " to be a brick in the distance, A portal looms below", -2)

        output["Innocent Bedroom"] = Room("Innocent Bedroom", {}, {}, {"Bedroom Photo":self.objects["Bedroom Photo"],"Bedroom Book":self.objects["Bedroom Book"]},
                                         "A young girls bedroom, beautiful toys litter the room, there seems to be a photo &"
                                         " book in the room, Another portal becons from ceiling maybe i can make it with a jump ", 1)

        output["Innocent Road"] = Room("Innocent Road", {}, {}, {"TimberBark": self.objects["TimberBark"]},
                                          "I seem to be have transported to a blank rural road, headlights appear in the distance, another"
                                          " red car flies past, i just catch the glimpse of a young girl looking out the window, another portal hangs from"
                                          " a tree, i can make it with a short leap",
                                          2)

        output["Innocent Place"] = Room("Innocent Place", {}, {}, {"MetalShard": self.objects["MetalShard"]},
                                       "There seems to be an accident, The red car"
                                       " destroyed, the driver and front passanger appear to be impaled in the car, a young girls body seems"
                                       " to be thrown from the car, she appears lifeless, a young man seems to be distraught, ITS ME THATS ME,",
                                       3)

        output["Innocent Field"] = Room("Innocent Field", {}, {}, {"Gravestone Note":self.objects["Gravestone Note"]},
                                        "A simple Grave stone, the flowers have dried, the stone crumbling, it reads EMMA J RODRIK "
                                        " 1976 - 1979, a note is present on top of the gravestone",
                                        -3)

        return output

    def init_buildings(self):
        output = {}
        output["Roofless house"] = Building('Roofless house', "This house is made of stone. It's roof has fallen because it's old.",
                                [self.rooms["Kitchen"], self.rooms["Bedroom"]], [1, 0])
        output["Family house"] = Building("Family house", "This is a very standard family house. Looks relatively big, probably 3-4 bedrooms, maybe a guest house. Seems like it's freshly painted",
                                          [self.rooms["Living room"], self.rooms["Attic"]], [2, 0])
        output["TestBLD1"] = Building("TestBLD1", "Test house mate", [self.rooms["Attic"]], [1, 1])
        output["TestBLD2"] = Building("TestBLD2", "Test house mate", [self.rooms["Living room"]], [2, 1])
        output["Neibolt House"] = Building("Neibolt House", "The house on the left it seems so familiar, but also so vague, it seems so inviting", [self.rooms["Neibolt Hallway"],self.rooms["Neibolt Bedroom"]
            ,self.rooms["Neibolt Basement"], self.rooms["Neibolt Lavatory"], self.rooms["Neibolt Kitchen"], self.rooms["Neibolt Attic"]], [1, 2])
        output["Innocent House"] = Building("Innocent House",
                                           "The house on the right has beautiful stature to it, you glance towards it, a little girl appears"
                                           " at the window before fadding into the distance",
                                           [self.rooms["Innocent Hallway"], self.rooms["Innocent Garden"]
                                               , self.rooms["Innocent Garage"], self.rooms["Innocent Bedroom"],
                                            self.rooms["Innocent Road"], self.rooms["Innocent Place"],self.rooms["Innocent Field"]], [2, 2])
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
