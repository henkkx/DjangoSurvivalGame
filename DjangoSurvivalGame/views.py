from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime


def landing_page(request):
    # if the request is a POST, pull the info & log the user in
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
                return render(request, 'DjangoSurvivalGame/langing_page.html', {'can_continue': can_continue})
            else:
                return HttpResponse("Account disabled, you cheater")

        else:
            '''
            WATCH IT HERE, will probably put this 'print' into the context_dict
            so that we can write this out on the page where we want instead of printing
            '''
            print("Invalid login details: {0}, {1}".format(username, password))

    else:

        return render(request, 'DjangoSurvivalGame/landing_page.html', {})


def home(request):
    # line below SHOULD count total number of users
    all_user_count = Count(User.objects.all())
    context_dict = {'user_count': all_user_count}
    return render(request, 'DjangoSurvivalGame/learn_more.html', context_dict)


def sign_up(request):
    registered = False

    if request.method == "POST":
        # display the forms ( waiting for models)

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
        profile_form = UserProfileForm()
    return render(request, 'DjangoSurvivalGame/sign_up.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('landing_page'))


@login_required
def game(request):
    if not request.user.is_authenticated():
        return HttpResponse("Whoops, must be logged in to play")
    else:
        return render(request, 'DjangoSurvivalGame/game.html', {'user': request.user})


@login_required
def my_profile(request):
    return render(request, 'DjangoSurvivalGame/my_account.html', {})
