from django.test import TestCase
from django.contrib.staticfiles import finders
from django.urls import reverse
from Game.models import *
from Game.forms import *
from Game.views import *
from django.contrib.auth.models import User
from Game.people import *
from population_script import populate



class DatabaseTests(TestCase):

    def setUp(self):
        populate()

    def test_correct_number_of_badges(self):
        self.assertEqual(len(list(Badge.objects.all())), 12)

    def test_correct_number_of_players(self):
        self.assertEqual(len(list(Badge.objects.all())), 12)


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


        
        
        




    







