from django.test import TestCase
from django.contrib.staticfiles import finders
from django.urls import reverse
from Game.models import *
from Game.forms import *
from Game.views import *
from django.contrib.auth.models import User
from Game.people import *


class DatabaseTests(TestCase):

    def setUp(self):
        test_user_1 = User.objects.create_user(username="test user 1",
                                                email='test1@mail.com',
                                               password='limbo')
        test_user_2 = User.objects.create_user(username="test user 2",
                                                email='test2@mail.com',
                                                password='limbo')
        PC.objects.create(user=test_user_1, picture=None, games_played=10,
                          most_days_survived=10, most_kills=10,
                          most_people=10, most_exp=10)
        PC.objects.create(user=test_user_2, picture=None, games_played=20,
                          most_days_survived=20, most_kills=20,
                          most_people=20, most_exp=20)

    def test_players_have_no_stats_on_create(self):
        user_no = 1
        test_player = PC.objects.get(user=User.objects.get(username="test user {0}".format(user_no)))
        for statistic in test_player.stats:
            self.assertTrue(expr=statistic == 0)

    def test_players_have_data(self):
        user_no = 1
        test_player = PC.objects.get(user=User.objects.get(username="test user {0}".format(user_no)))
        self.assertTrue(expr=test_player.games_played == user_no*10 and
                        test_player.most_days_survived == user_no*10 and
                        test_player.most_kills == user_no*10 and
                        test_player.most_people == user_no*10 and
                        test_player.most_exp == user_no*10)

    def test_players_earn_achievements(self):
        user_nos = [1,2]
        value = 3
        for players_no in user_nos:
            pl = PC(user=User.objects.get(username="test user {0}".format(players_no)))
            for i in pl.stats:
                pl.stats[i] += value
                pl.stats[i] += value
                pl.stats[i] += value
            '''Check achievements will be the function that checks & gives out the achievements, implemented later'''
            # check_achievements(pl)
            for i in pl.stats:
                self.assertTrue(expr=pl.stats[i] == value)

    def test_home(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_landing_page(self):
        url = reverse('landing_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_sign_up(self):
        url = reverse('sign_up')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_instructions(self):
        url = reverse('instructions')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # TESTING KEY STATIC IMAGES

    def test_dunkey_image(self):
        result = finders.find('images/dunkey.jpg')
        self.assertIsNotNone(result)

    def test_ig_image(self):
        result = finders.find('images/ig logo.png')
        self.assertIsNotNone(result)

    def test_landing_image(self):
        result = finders.find('images/landing.jpg')
        self.assertIsNotNone(result)

    def test_mayhem_image(self):
        result = finders.find('images/mayhem.jpg')
        self.assertIsNotNone(result)

    def test_ign_image(self):
        result = finders.find('images/ign.jpg')
        self.assertIsNotNone(result)

    def test_tunnel_image(self):
        result = finders.find('images/tunnel.jpg')
        self.assertIsNotNone(result)

    def test_landing_to_home(self):
        try:
            response = self.client.get(reverse('home'))
        except:
            response = False
        return response

    # Population Script Check

    def test_population_script(self):

        try:
            from Game import game_populate
            game_populate()
        except ImportError:
            print('does not exist')
        except NameError:
            print('game_populate() does not exist or is not correct')
        except:
            print('Something went wrong with the game_populate file')


    







