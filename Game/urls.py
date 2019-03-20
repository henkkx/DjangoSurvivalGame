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
    url(r'^game', views.game, name='game'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^get_actions', views.get_actions, name="get_actions"),
    url(r'^post_data', views.post_data, name="post_data"),
    url(r'^initialise', views.initialise, name="initialise"),
]

'''
/home
/signup
/learnmore
/game
/myprofile
'''
