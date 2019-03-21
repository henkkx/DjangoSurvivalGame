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
        player1 = Player.objects.create(user=test_user_1, picture=None, games_played=10,
                          most_days_survived=10, most_kills=10,
                          most_people=10, most_exp=10, stats={"kills": 10, "days": 10, "npcs": 10, "exp": 10})
        player2 = Player.objects.create(user=test_user_2, picture=None, games_played=20,
                          most_days_survived=20, most_kills=20,
                          most_people=20, most_exp=20, stats={"kills": 20, "days": 20, "npcs": 20, "exp": 20})
        return player1, player2

    #The changes this made to the stats field of the player objects seemed to persist for some reason.
    #Even after deletion of the player object.
    """
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
    """

class ViewTests(TestCase):

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
        url = reverse('registration_register')
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

    def test_landing_image(self):
        result = finders.find('images/landing.jpg')
        self.assertIsNotNone(result)

    def test_mayhem_image(self):
        result = finders.find('images/mayhem.jpg')
        self.assertIsNotNone(result)

    def test_tunnel_image(self):
        result = finders.find('images/tunnel.jpg')
        self.assertIsNotNone(result)

    def test_landing_to_home(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_count_for_zero_users(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user_count'], 0)


    def test_about_count_returns_correct_number(self):
        User.objects.create_user(username="test user 1",email='test1@mail.com', password='limbo')
        User.objects.create_user(username="test user 2", email='test2@mail.com', password='limbo')
        
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user_count'], 2)


        
        
        




    







