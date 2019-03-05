from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Count
from Game.forms import UserForm, Profile
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from Game.models import Player
import json

def home(request):
    # if the request is a POST, pull the info & log the user in

    playerList = Player.objects.order_by('-most_kills')[:5]


    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        can_continue = False
        # this variable may not be needed, we can check straight from the .html file to render
        # the "Continue" button, we'll see
        if user:
            if user.is_active:
                login(request, user)
                # if user.has_save_file:
                #     can_continue = True
                return render(request, 'Game/home.html', {'can_continue': can_continue})
            else:
                return HttpResponse("Account disabled, you cheater")

        else:
            '''
            WATCH IT HERE, will probably put this 'print' into the context_dict
            so that we can write this out on the page where we want instead of printing
            '''
            print("Invalid login details: {0}, {1}".format(username, password))

    else:

        return render(request, 'Game/home.html', {"players":playerList})

def landing_page(request):
    return render(request, "Game/landing_page.html")



def learn_more(request):
    return render(request, "Game/learn_more.html")

def instructions(request):
    return render(request, "Game/instructions.html")


def about(request):
    # line below SHOULD count total number of users
    all_user_count = Count(User.objects.all())
    context_dict = {'user_count': all_user_count}
    return render(request, 'Game/about.html', context_dict)


def sign_up(request):
    registered = False

    if request.method == "POST":
        # display the forms ( waiting for models)
        user_form = UserForm(data=request.POST)
        profile_form = Profile(data=request.POST)
        if user_form.is_valid and profile_form.is_valid:
            # save user data
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            # save profile data
            profile = profile_form.save(commit=False)
            profile.user = user
            # if the user provided a picture save that
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = Profile()
    return render(request, 'registration/registration_form.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def game(request):
    if not request.user.is_authenticated():
        return HttpResponse("Whoops, must be logged in to play")
    else:
        return render(request, 'Game/game.html', {'user': request.user})


# @login_required
def my_profile(request):
    return render(request, 'Game/my_profile.html', {})


def test_view(request):
    return render(request, "Game/game.html", json.dump({"Hello World": "Hello Henrik"}))
