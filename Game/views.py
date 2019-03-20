from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Count
from Game.forms import UserForm, Profile
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from Game.models import Player, Achievement
from Game.game_handler import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Count
from Game.forms import UserForm, Profile
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from Game.models import Player, Achievement
from Game.game_handler import *
import json
from django.views.decorators.csrf import csrf_exempt
from Game.Scribbles_from_another_dimension import available_actions, handle, initialise
from Game.Scribbles_from_another_dimension import available_actions, handle
from django.shortcuts import redirect
import os


def home(request):
    # if the request is a POST, pull the info & log the user in

    # playerList = PC.objects.order_by('-most_kills')[:5]

    context_dict = {}

    context_dict["players_kills"] = Player.objects.order_by('-most_kills')[:5]
    context_dict["players_survived"] = Player.objects.order_by('-most_days_survived')[:5]

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        context_dict["can_continue"] = False


        # this variable may not be needed, we can check straight from the .html file to render
        # the "Continue" button, we'll see
        if user:
            if user.is_active:
                login(request, user)
                # if user.has_save_file:
                #     can_continue = True
                return render(request, 'Game/home.html', context_dict)
            else:
                return HttpResponse("Account disabled, you cheater")
        else:
            '''
            WATCH IT HERE, will probably put this 'print' into the context_dict
            so that we can write this out on the page where we want instead of printing
            '''
            print("Invalid login details: {0}, {1}".format(username, password))

    else:

        return render(request, 'Game/home.html', context_dict)


def landing_page(request):
    return render(request, "Game/landing_page.html")


def learn_more(request):
    return render(request, "Game/learn_more.html")


def instructions(request):
    return render(request, "Game/instructions.html")


def about(request):
    # line below SHOULD count total number of users
    all_user_count = len(User.objects.all())
    context_dict = {'user_count': all_user_count}
    return render(request, 'Game/about.html', context_dict)


# def sign_up(request):
#     registered = False

#     if request.method == "POST":
#         # display the forms ( waiting for models)
#         user_form = UserForm(data=request.POST)
#         profile_form = Profile(data=request.POST)
#         if user_form.is_valid and profile_form.is_valid:
#             # save user data
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#             # save profile data
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             # if the user provided a picture save that
#             if 'picture' in request.FILES:
#                 profile.picture = request.FILES['picture']
#             profile.save()
#             registered = True
#         else:
#             print(user_form.errors, profile_form.errors)
#     else:
#         user_form = UserForm()
#         profile_form = Profile()
#     return render(request, 'registration/registration_form.html',
#                   {'user_form': user_form,
#                    'profile_form': profile_form,
#                    'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def game(request):
    initialise(request.user.username)
    return render(request, 'Game/gamePage.html', {'user': request.user})


@login_required
def profile(request, user=None):

    print(user)
    contxt = {}
    #retrieve associated player object and pass important stats to template
    if not user:
        player = Player.objects.get_or_create(user=request.user)[0]
    else:
        try:
            player = Player.objects.get(user=User.objects.get(username=user))
        except:
            return HttpResponse("The Player whose profile you are looking for does not exist.")
            
        
    #print(player)
    contxt["name"] = player.user.username
    contxt["games"] = player.games_played
    contxt["kills"] = player.most_kills
    contxt["exp"] = player.most_exp
    contxt["days"] = player.most_days_survived
    print(contxt, "CONTEXT DICT")
    contxt["achievements"] = list(Achievement.objects.filter(player=player))
    if player.picture:
        contxt["picture"] = player.picture

    form = Profile({'picture': player.picture})

    if request.method == 'POST':

        image = request.FILES.get('picture', False)

        if image is False:
            os.remove(player.picture.path)
            player.picture = None
            player.save()
            return HttpResponseRedirect(reverse("profile"))

        player.picture = image
        player.save()
        return HttpResponseRedirect(reverse("profile"))
    else:
        print(form.errors)

    contxt["form"] = form

    return render(request, 'Game/profile.html', contxt)

# @csrf_exempt
# def initialise(request):
#     # print(request.user, " initalise here")
#     # retrieve associated player object and pass important stats to template
#     initialise(request.user.username)
#     if request.user.is_authenticated:
#         player_temp = Player.objects.get_or_create(user=request.user)[0]
#         print(player_temp, "___----")
#         initialise(request.user.username)

    # form = Profile({'picture': player.picture})
    #
    # if request.method == 'POST':
    #
    #     image = request.FILES.get('picture', False)
    #
    #     if image is False:
    #         return HttpResponseRedirect(reverse("my_profile"))
    #
    #     player.picture = image
    #     player.save()
    #     return HttpResponseRedirect(reverse("my_profile"))
    # else:
    #     print(form.errors)
    #
    # contxt["form"] = form
    #
    # return render(request, 'Game/my_profile.html', contxt)


# def my_test(request):
#     return render(request, "Game/gamePage.html", {})


def get_actions(request):
    return available_actions()


@csrf_exempt
def post_data(request):
    if request.method == "POST":
        handle(request.body)
    return HttpResponse("Placeholder")
