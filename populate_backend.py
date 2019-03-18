import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'DjangoSurvivalGame.settings')

import django
django.setup()
from Game.models import Badge, Player, Achievement
from django.contrib.auth.models import User

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

players = []
for i in range(0,10):
    players.append({"username":"Player{0}".format(i), "email": "{0:06d}{1}@student.gla.ac.uk".format(i, chr(65+i)),
                "password": "{0}{1}{2}{3}{4}{5}{6}{7}".format(chr(i+65),chr(i+65),chr(i+66),chr(i+67),chr(i+68),chr(i+69),chr(i+70),chr(i+71)),
                 "games_played": i*10, "most_days_survived": i*5, "most_kills": i*4, "most_people": i*2, "most_exp": 100*i})

#Main populate function.
#Generates ten players with increasing stats, badges and awards achievements to worthy players
def populate():

    #Create badges
    for badge in badges:
        add_badge(badge['name'], badge['description'], badge['criteria'], badge['badge_type'])

    #create badges and award achievements if deserving
    for player in players:
        new_player = add_player(player["username"], player["email"], player["password"], player["games_played"], player["most_days_survived"], player["most_kills"],
                       player["most_people"], player["most_exp"])

        #if add_player returns none then the player already exists so move on.
        if new_player == None:
            continue

        #else for each badge check if the criteria is met and award and achievement if so.
        for badge in list(Badge.objects.all()):
            if badge.badge_type == "kills" and badge.criteria <= new_player.most_kills:
                add_achievement(player = new_player, badge = badge)

            elif badge.badge_type == "npcs" and badge.criteria <= new_player.most_people:
                add_achievement(player = new_player, badge = badge)
                


def add_badge(name, desc, criteria, type_of):
    badge = Badge.objects.get_or_create(name=name, description=desc, criteria=criteria, badge_type=type_of)
    return badge

def add_player(username, email, password, games_played, most_days_survived, most_kills,
               most_people, most_exp, picture = None):
    try:
        new_user = User.objects.create_user(username=username,
                                                    email=email,
                                                   password=password)

        return Player.objects.create(user=new_user, picture=picture, games_played=games_played,
                              most_days_survived=most_days_survived, most_kills=most_kills,
                              most_people=most_people, most_exp=most_exp)
    except:
        return None

def add_achievement(player, badge):
    return Achievement.objects.get_or_create(player = player, badge = badge)

if __name__ == "__main__":
    populate()
