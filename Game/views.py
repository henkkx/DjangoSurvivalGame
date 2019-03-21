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



def WrongPage(request):
    return render(request, 'Game/WrongPage.html')

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
        if user == request.user.username:
            return HttpResponseRedirect(reverse("profile"))
        try:
            player = Player.objects.get(user=User.objects.get(username=user))
        except:
            return HttpResponseRedirect(reverse("WrongPage"))
            
        
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

        image = request.FILES.get('file-input', False)

        if image is False:
            if player.picture:
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



def get_actions(request):
    return HttpResponse(available_actions())


@csrf_exempt
def post_data(request):
    if request.method == "POST":
        handle(request.body)
    return HttpResponse("Placeholder")
