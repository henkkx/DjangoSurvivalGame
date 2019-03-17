from django import forms
from Game.models import PC
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = {'username', 'email', 'password'}


class Profile(forms.ModelForm):

    class Meta:
        model = PC
        fields = {'picture'}
