import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'DjangoSurvivalGame.settings')

import django
django.setup()
from Game.models import Badge


def populate():
    badges = [
        {'name': 'First Blood',
         'description': 'You have achieved your first kill in the game',
         'criteria': 0,
         'badge_type': 'kills'},
        {'name': 'Welcome to the rest of your life',
         'description': 'You have entered a house for the first time',
         'criteria': 0,
         'badge_type': 'houses'},
        {'name': 'Crescendo',
         'description': "That's a lot of houses having been explored, nice",
         'criteria': 5,
         'badge_type': 'houses'},
        {'name': 'Murderer',
         'description': 'You are crazy, you have made at least 10 kills',
         'criteria': 10,
         'badge_type': 'kills'},
        {'name': 'Beginning of the end',
         'description': 'You have started exploring the world',
         'criteria': 0,
         'badge_type': 'npcs'},
    ]

    for badge in badges:
        add_badge(badge['name'], badge['description'], badge['criteria'], badge['type'])


def add_badge(name, desc, criteria, type_of):
    badge = Badge.objects.get_or_create(name=name, description=desc, criteria=criteria, type=type_of)
    return badge
