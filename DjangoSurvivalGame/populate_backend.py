import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'DjangoSurvivalGame.settings')

import django
django.setup()
from Game.models import Badge

badges = [
    {'name': 'First Blood',
     'description': 'You have achieved your first kill in the game',
     'criteria': 1,
     'badge_type': 'kills'},
    {'name': 'Murderer',
     'description': 'You are crazy, you have made at least 10 kills',
     'criteria': 10,
     'badge_type': 'kills'},
    {'name': 'Murder Hobo',
     'description': 'Remind me never to play DnD with you',
     'criteria': 100,
     'badge_type': 'kills'},

    {'name': 'Welcome to the rest of your life',
     'description': 'You have entered a house for the first time',
     'criteria': 0,
     'badge_type': 'houses'},
    {'name': 'Again and again',
     'description': "You've been busy, hope you've taken your lesson",
     'criteria': 10,
     'badge_type': 'houses'},
    {'name': 'Well, you like the game...',
     'description': 'Never thought someone would play enough to get this.\
                    Seriously do you need help?',
     'criteria': 100,
     'badge_type': 'houses'},

    {'name': 'Beginning of the end',
     'description': 'You have started exploring the world',
     'criteria': 1,
     'badge_type': 'npcs'},
    {'name': 'Socialize',
     'description': 'You have met, or more accurately, remembered a lot of people',
     'criteria': 10,
     'badge_type': 'npcs'},
    {'name': 'Diplomat',
     'description': 'Seriously though, too much time spent on this game, get out get some air.',
     'criteria': 100,
     'badge_type': 'npcs'},


]

def populate():

    for badge in badges:
        add_badge(badge['name'], badge['description'], badge['criteria'], badge['type'])


def add_badge(name, desc, criteria, type_of):
    badge = Badge.objects.get_or_create(name=name, description=desc, criteria=criteria, type=type_of)
    return badge
