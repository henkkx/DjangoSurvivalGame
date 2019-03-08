"""DjangoSurvivalGame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Game import views

urlpatterns = [
    url(r'^$', views.landing_page, name='landing_page'),
    url(r'^landing_page', views.landing_page, name=''),
    url(r'^home', views.home, name="home"),
    url(r'^about', views.about, name='about'),
    url(r'^instructions', views.instructions, name='instructions'),
    url(r'^sign_up', views.sign_up, name='sign_up'),
    url(r'^game', views.my_test, name='game'),
    url(r'^my_profile', views.my_profile, name='my_profile'),
    url(r'^test', views.test_view, name="test"),
    url(r'^test2', views.test_view2, name="test"),
]

'''
/home
/signup
/learnmore
/game
/myprofile
'''
