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

        #-----------------------------Neibolt-----------------------------------------

        output["Pennywise"] = NPC("Pennywise","Pennywise the clown","Pennywise the familiar monster that plauged your dreams as"
                                    " a child, trying to lure you in untill one night it stopped",1000,"Menacing",[]
                                  ,"The clown slowly turns and stares directly at me, his eyes so vivid, his tongue like that of a"
                                   " lizard licks his shark like teeth. 'Welcome back, its been a while' he remarks '27 years, 27 long"
                                   " years, i've been lusting for your blood ever since you escaped my grasp as a child, but the master"
                                   " has a plan for you'. What could that mean who is the master, why does he still remember me, what is this place,"
                                   " he speaks up once again 'Don't worry once the master is done with you, ill be coming for you', in an instance"
                                   " he runs towards me teeth gleaning and mouth wide open, i'm startled scared but then as quick as he sprinted towards"
                                   " me, he vanishes into thin air leaving behind a mysterious shawdow repeating the conversation we just had")

        output["Playing Girl"] = NPC("Playing Girl","A young girl playing in the garden","A small young girl, about 3 years old"
                                    " dressed in red with a flower headband",10,"friendly",[],"I attempt to speak to her, she turns around swiftly,"
                                    " 'hi there my names Emma, and im playing with my mummy & daddy, we are going to my auntie Jills house tonight to see"
                                    " all my friends i can't wait, whats your name', you hear a bang, you look away, you turn back she is not there anymore"
                                    " all that remains is a little red flower resembling the one on her head band ")

        output["Dead Girl"] = NPC("Dead Girl","The lifeless body of a young girl","A young girl thrown from the car she looks lifeless & numb",1,"Evil"
                                  ,[],"you rush over to the lifeless body, in an instance it turns and faces you, it begins"
                                            " to laugh menacingly before uttering the words, 'You killed them,you have taken what is not yours"
                                            " to take, i will be seeing you' and in an instance your startled as the life appears to return to the young girl"
                                            " briefly she mutters 'Am i okay, wheres mummy & daddy', you try to comfort her as she passes away, tears"
                                            " raining from your eyes")

        return output

    def init_creatures(self):
        output = {}
        # yes in the end there is no correlation between creature name & class, we are using it for stats though
        output['Charred fur rat'] = Rat("Charred fur rat", player.level)
        output["The Hound of Buskerville"] = Ghoul("The Hound of Buskerville", player.level)
<<<<<<< HEAD
        output["Ghoul"] = Ghoul("A.., humanoid that walks with it's hands? A ghoul or something? It screams 'STOP IT' in a childlike voice." , player.level)
        output["Android"] = Vampire("An hostile android", player.level)
=======
        output['Ghost Girl'] = Ghoul("Ghost Girl",player.level+2,"The ghost of a young girl in a red dress & flower headband")
        output['Large Red Spider'] = Ghoul("Large Red Spider",player.level,"A large red spider, probably the size of a ruller")
        output['Raven'] = Rat("Raven",player.level)
        output['Sphinx'] = Ghoul("Sphinx",player.level)
>>>>>>> a8837dfaaab465deb087ee67355a432ace6e0da7
        return output

    def init_rooms(self):
        output = {}
        # place holder in order to avoid errors
        output["default"] = Room("default", {}, {}, {}, "", -100)

        '''Burned house rooms'''
        output["Burned Kitchen"] = Room("Burned Kitchen", {"Doug": self.NPCs["Doug"]}, {}, {"Bread": self.objects["Bread"]}, "You can smell spices, and a hint of both \
        garlic & onion. There are utensils & plates all around",0)
        output["Burned Bedroom"] = Room("Burned Bedroom", {}, {"Charred fur rat": self.creatures['Charred fur rat']}, {"Health Potion": self.objects["Health Potion"]}, "You are in a bedroom, single bed. Sheets indicate a child\
        slept here. In the corner a rat is munching on something",0)
        output["Burned Roof"] = Room("Burned Roof", {}, {"The Hound of Burskerville": self.creatures["The Hound of Buskerville"]}, {"Spear": self.objects["Spear"]},
                                 "The roof of the house is hardly there, since it was burned down. The far side is however is still there. You can see a dog playing with what looks like a stick.",1 )

        '''Family house rooms'''
        output["Living room"] = Room("Living room", {"Tony": self.NPCs["Tony"]}, {}, {"Bread": self.objects['Bread']},
                                     "The room reminds you of the living room of a childhood friend of yours. You don't remember who though.",0)
        output["Attic"] = Room("Attic", {}, {},{"Tony's journal": self.objects["Tony's journal"]},
                               "A standard Attic, a poster reading 'Who Watches The Watchmen' half hangs on one side",1)
        output["Game room"] = Room("Game room", {}, {"Ghoul": self.creatures["Ghoul"]},{},
                                   "Tony's game room. He used to have a lot of games as a kid."
                                   " Now that you are older you realise that's what you get for your parents not giving you enough of their time."
                                   " You hope you were a good enough friend to somehow make up for that")

        '''Bar rooms'''
        output["Main room"] = Room("Main room", {"Barwoman": self.NPCs["Barwoman"]}, {}, {"Pint of beer": self.objects["Pint of beer"]})

        '''University building rooms'''

        #-----------------------------------------Neibolt House Rooms -----------------------------------------------------#

        output["Neibolt Hallway"] = Room("Neibolt Hallway", {}, {}, {"Red Balloon": self.objects["Red Balloon"]}, "You enter the Hallway, A beuatiful large opening "
                         "However, something feels wrong, A dim dark staircase ahead claw marks going towards the basement "
                                " A red ballon seems to be leading you there. Stairs lead to the second floor, they look unsafe"
                                                                        " falling apart",0)

        output["Neibolt Basement"] = Room("Neibolt Basement",{"Pennywise": self.NPCs["Pennywise"]},{},{"Paper Plane":self.objects["Paper Plane"]},"The ballon leads you to the basement, there is a creature just in the shadow, he "
                                                                      "seems to be lying down, His eyes fiery yellow, teeth as sharp as claws, "
                                                                      "his voice soothing & inviting, he resembles the creature that plaged your dreams as"
                                                                      " a child, he throws a paperplane towards you",-1)

        output["Neibolt Bedroom"] = Room("Neibolt Bedroom", {}, {}, {"Bedroom Note":self.objects["Bedroom Note"],"Baseball Bat": self.objects["Baseball Bat"]},"This room, this room it seems so familiar, MY BEDROOM THIS IS MY BEDROOM!."
                                                                       " an image hangs on the wall an old drawing of yours, it seems to resemble a clown holding a red balloon"
                                                                       " Under the bed there appears to be a baseball bat & a note",1)

        output["Neibolt Lavatory"] = Room("Neibolt Lavatory", {}, {}, {"Toothbrush": self.objects["Toothbrush"]},
                                         "The toilet seems to be working, Hmmm intresting [FLUSH] blood appears to flowing instead of water, unnerving "
                                         "There seems to be some tooth paste and a brush here also",1)

        output["Neibolt Kitchen"] = Room("Neibolt Kitchen", {}, {"Large Red Spider": self.creatures['Large Red Spider']}, {"Jam Sandwich": self.objects["Jam Sandwich"]},"Hmmm this kitchen, it reminds you of home, there seems to be a sandwich on the table, You look up "
                                        "BLOOD smeered all over roof, it reads Welcome Home, What could this mean, "
                                        "A large red spider, probably the size of a ruller, lays on the table moving around the room, it seems strong"
                                                                                                                   " best to keep away" ,0)

        output["Neibolt Attic"] = Room("Neibolt Attic", {}, {"Sphinx": self.creatures['Sphinx']}, {"Attic Photo": self.objects["Attic Photo"],"Silver Sword": self.objects["Silver Sword"]},
                                         "The attic creaks, you hear movement below like a dog pancing quickly, Thats not a dog not that fast "
                                         " Your startled in front of you there a appears to be sphinx muttering a riddle, "
                                         "There appears to be something shining off in the distance, a silver glimmer & and a photo", 2)

        # ---------------------------------------Murder House (Innocent House)---------------------------------------------------#

        output["Innocent Hallway"] = Room("Innocent Hallway", {}, {"Raven":self.creatures["Raven"]}, {},
                                         "This hallway, it appears to be warped, portals seem to be placed at each stairway they appear "
                                         "to give off a reverberating humming sound, A raven stands strong its pupils a glistening red", 0)

        output["Innocent Garden"] = Room("Innocent Garden", {"Playing Girl": self.NPCs["Playing Girl"]}, {}, {},
                                         "The portal sent me to a garden, a memory seems to be playing, a young girl seems to be playing with her"
                                         " family their faces they seems so familiar, There seems to be another portal decending down",-1)

        output["Innocent Garage"] = Room("Innocent Garage", {}, {}, {"Brick": self.objects["Brick"]},
                                         "In an instance i've arrived in a garage, there is a car, violent RED, there seems"
                                         " to be a brick in the distance, A portal looms below", -2)

        output["Innocent Bedroom"] = Room("Innocent Bedroom", {}, {"Ghost Girl": self.creatures['Ghost Girl']}, {"Bedroom Photo":self.objects["Bedroom Photo"],"Bedroom Book":self.objects["Bedroom Book"]},
                                         "A young girls bedroom, beautiful toys litter the room, there seems to be a photo &"
                                         " book in the room,In the corner of your eye you catch the glipse of what appears to be a young girl"
                                         " hovering above the ground, dressed fully in red & wearing a flower headband"
                                         "Another portal becons from ceiling maybe i can make it with a jump ", 1)

        output["Innocent Road"] = Room("Innocent Road", {}, {}, {"TimberBark": self.objects["TimberBark"]},
                                          "I seem to be have transported to a blank rural road, headlights appear in the distance, another"
                                          " red car flies past, i just catch the glimpse of a young girl looking out the window, another portal hangs from"
                                          " a tree, i can make it with a short leap",
                                          2)

        output["Innocent Place"] = Room("Innocent Place", {"Dead Girl": self.NPCs["Dead Girl"]}, {}, {"MetalShard": self.objects["MetalShard"]},
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
                                [self.rooms["Burned Kitchen"], self.rooms["Burned Bedroom"], self.rooms["Burned Roof"]], [1, 0])
        output["Family house"] = Building("Family house", "This is a very standard family house. Looks relatively big, probably 3-4 bedrooms, maybe a guest house. Seems like it's freshly painted",
                                          [self.rooms["Living room"], self.rooms["Attic"], self.rooms["Game room"]], [2, 0])
        output["Bar"] = Building("Bar", "A modern bar, the road-side walls are mostly glass. It seems almost empty", [self.rooms["Attic"]], [1, 1])
        output["University building"] = Building("University building", "It's a small building with only a few rooms you can recall, but you used to be in it a LOT for assignments during your studies",
                                                     [self.rooms["Living room"]], [2, 1])

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
