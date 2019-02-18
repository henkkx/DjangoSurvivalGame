from django.db import models
from django.contrib.auth.models import User
import pickle
import datetime

class Player(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    games_played = models.IntegerField(default=0)
    most_dayes_survived = models.IntegerField(default=0)
    most_kills = models.IntegerField(default=0)
    most_people = models.IntegerField(default=0)
    current_game = {'inventory': [], 'stats': {}, 'maps': {}}

    '''
    Just have this to remember how to pickle in & out when I create the function later
    pickle_out = open("dict.pickle","wb")
    pickle.dump(example_dict, pickle_out)
    pickle_out.close()
    pickle_in = open("dict.pickle","rb")
    example_dict = pickle.load(pickle_in)
    '''

    def save_game(self):
        # pickle out data
        pass

    def load_game(self):
        # pickle in data
        pass

    def __str__(self):
        return self.user.username


class Badge:
    name = models.CharField(max_length=64, required=True)
    description = models.CharField(max_length=254)
    criteria = models.IntegerField(default=10)
    badge_type = models.CharField(max_length=32)
    icon = models.ImageField(upload_to='badge_icons', blank=True)

    # def __init__(self, name, desc, criteria, badge_type, icon_path):
    #     self.name = name
    #     self.description = desc
    #     self.criteria = criteria
    #     self.badge_type = badge_type
    #     self.icon = icon_path

    def __str__(self):
        return self.name


class Achievement:
    player = models.OneToOneField(Player)
    badge = models.ManyToOneRel(Badge)
    # following should save current DD-MM-YYYY date
    now = datetime.datetime.now()
    date_awarded = models.DateField(default=now.strftime("%d-%m-%Y"))

    def __str__(self):
        return "Player {0} has the {1} badge. Achieved on {2}".format(self.player,
                                                                      self.badge,
                                                                      self.date_awarded)





