import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'DjangoSurvivalGame.settings')

import django
django.setup()
from Game.models import Player, Badge, Achievement


def populate():
    badges = [
        {'name': 'First Blood',
         'description': 'You have achieved your first kill in the game',
         'criteria': 'kills > 0',
         }
    ]