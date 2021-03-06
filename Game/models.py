from django.db import models
from django.contrib.auth.models import User
import pickle
import datetime
from picklefield.fields import PickledObjectField


class Player(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    games_played = models.IntegerField(default=0)
    most_days_survived = models.IntegerField(default=0)
    most_kills = models.IntegerField(default=0)
    most_people = models.IntegerField(default=0)
    most_exp = models.IntegerField(default=0)
    current_game = PickledObjectField(null=True)
    stats = {"kills": 0, "days": 0, "npcs": 0, "exp": 0}

    def __str__(self):
        return self.user.username


class Badge(models.Model):
    name = models.CharField(max_length=64)
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


class Achievement(models.Model):
    player = models.ForeignKey(Player)
    badge = models.ForeignKey(Badge)
    # following should save current DD-MM-YYYY date
    now = datetime.datetime.now()
    date_awarded = models.DateField(default=now.strftime("%Y-%m-%d"))

    def __str__(self):
        return "Player {0} has the {1} badge. Achieved on {2}".format(self.player,
                                                                      self.badge,
                                                                      self.date_awarded)
