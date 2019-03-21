import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'DjangoSurvivalGame.settings')

import django
django.setup()
from Game.models import Badge, Player, Achievement
from django.contrib.auth.models import User

badges = [
    #These are the badges associated with achievements awraded for kills.
    {'name': 'First Blood',
     'description': 'You have achieved your first kill in the game',
     'criteria': 1,
     'badge_type': 'kills',
     'icon': "badge_icons/ZombieHunterBadge1.png"},
    {'name': 'Murderer',
     'description': 'You are crazy, you have made at least 10 kills',
     'criteria': 3,
     'badge_type': 'kills',
     'icon': "badge_icons/ZombieHunterBadge2.png"},
    {'name': 'Murder Hobo',
     'description': 'Remind me never to play DnD with you',
     'criteria': 10,
     'badge_type': 'kills',
     'icon': "badge_icons/ZombieHunterBadge3.jpg"},

    #These are the badges associated with achievements awraded for days.
    {'name': 'Welcome to the rest of your life',
     'description': 'You have spent 1 in game day, or in other words managed to click the exit button',
     'criteria': 1,
     'badge_type': 'days',
     'icon': "badge_icons/Survivor1.png"},
    {'name': 'Again and again',
     'description': "You've been busy, hope you've taken your lesson",
     'criteria': 2,
     'badge_type': 'days',
     'icon': "badge_icons/Survivor2.png"},
    {'name': 'Well, you like the game...',
     'description': 'Never thought someone would play enough to get this.\
                    Seriously do you need help?',
     'criteria': 3,
     'badge_type': 'days',
     'icon': "badge_icons/Survivor3.png"},

    #npc badges
    {'name': 'Beginning of the end',
     'description': 'You have started exploring the world.',
     'criteria': 1,
     'badge_type': 'npcs',
     'icon': "badge_icons/Saviour1.png"},
    {'name': 'Socialize',
     'description': 'You have met, or more accurately, remembered a lot of people.',
     'criteria': 3,
     'badge_type': 'npcs',
     'icon': "badge_icons/Saviour2.png"},
    {'name': 'Diplomat',
     'description': 'Seriously though, too much time spent on this game, get out get some air.',
     'criteria': 5,
     'badge_type': 'npcs',
     'icon': "badge_icons/Saviour3.png"},

     #exp badges
    {'name': 'Novice Explorer',
     'description': 'You have aquired 100 experience in one game.',
     'criteria': 100,
     'badge_type': 'exp',
     'icon': "badge_icons/Experience1.png"},
    {'name': 'Journeyman',
     'description': 'You have aquired a respectable amount of experience in a single game.',
     'criteria':300,
     'badge_type': 'exp',
     'icon': "badge_icons/Experience2.png"},
    {'name': 'Master',
     'description': 'You have aquired a ridiculous amount of experience. Well done.',
     'criteria': 500,
     'badge_type': 'exp',
     'icon': "badge_icons/Experience3.png"},


]

#Generate ten players with stats increasing as i increases.
#username based on i. username is Player'i'.
#e.g. i =0: username = "Player0".
players = []
for i in range(0,10):
    players.append({"username":"Player{0}".format(i), "email": "{0:06d}{1}@student.gla.ac.uk".format(i, chr(65+i)),
                "password": "TestPass",
                 "games_played": i*10, "most_days_survived": min(round(i*0.5),3), "most_kills": i*1, "most_people": round(i*0.5), "most_exp": 40*i})

#Main populate function.
#Generates ten players with increasing stats, badges and awards achievements to worthy players
def populate():

    #Create badges
    for badge in badges:
        add_badge(badge['name'], badge['description'], badge['criteria'], badge['badge_type'], badge['icon'])

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

            elif badge.badge_type == "days" and badge.criteria <= new_player.most_days_survived:
                add_achievement(player = new_player, badge = badge)

            elif badge.badge_type == "exp" and badge.criteria <= new_player.most_exp:
                add_achievement(player = new_player, badge = badge)
                


def add_badge(name, desc, criteria, type_of, icon):
    badge = Badge.objects.get_or_create(name=name, description=desc, criteria=criteria, badge_type=type_of)[0]
    badge.icon = icon
    badge.save()
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
        try:
            new_player = Player.objects.get(user=User.objects.get(username=username))
            new_player.games_played = games_played
            new_player.most_days_survived = most_days_survived
            new_player.most_kills = most_kills
            new_player.most_people = most_people
            new_player.most_exp = most_exp
            new_player.picture = picture
            new_player.save()
            return new_player
            
        except:
            return None

def add_achievement(player, badge):
    return Achievement.objects.get_or_create(player = player, badge = badge)[0]

if __name__ == "__main__":
    populate()
