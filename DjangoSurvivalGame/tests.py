from django.test import TestCase
from Game.models import *
from Game.forms import *
from Game.views import *
from django.contrib.auth.models import User


class DatabaseTests(TestCase):

    def setUp(self):
        test_user_1 = User.objects.create_user(username="test user 1",
                                                email='test1@mail.com',
                                               password='limbo')
        test_user_2 = User.objects.create_user(username="test user 2",
                                                email='test2@mail.com',
                                                password='limbo')
        Player.objects.create(user=test_user_1, picture=None, games_played=10,
                              most_days_survived=10, most_kills=10,
                              most_people=10, most_exp=10)
        Player.objects.create(user=test_user_2, picture=None, games_played=20,
                              most_days_survived=20, most_kills=20,
                              most_people=20, most_exp=20)

    def test_players_have_no_stats_on_create(self):
        user_no = 1
        test_player = Player.objects.get(user=User.objects.get(username="test user {0}".format(user_no)))
        for statistic in test_player.stats:
            self.assertTrue(expr=statistic == 0)

    def test_players_have_data(self):
        user_no = 1
        test_player = Player.objects.get(user=User.objects.get(username="test user {0}".format(user_no)))
        self.assertTrue(expr=test_player.games_played == user_no*10 and
                        test_player.most_days_survived == user_no*10 and
                        test_player.most_kills == user_no*10 and
                        test_player.most_people == user_no*10 and
                        test_player.most_exp == user_no*10)

    def test_players_earn_achievements(self):
        user_nos = [1,2]
        value = 3
        for players_no in user_nos:
            pl = Player(user=User.objects.get(username="test user {0}".format(players_no)))
            for i in pl.stats:
                pl.stats[i] += value
                pl.stats[i] += value
                pl.stats[i] += value
            '''Check achievements will be the function that checks & gives out the achievements, implemented later'''
            # check_achievements(pl)
            for i in pl.stats:
                self.assertTrue(expr=pl.stats[i] == value)