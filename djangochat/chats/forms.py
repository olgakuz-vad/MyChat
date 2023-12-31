from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import Textarea

from .models import *

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'avatar']


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class AddRoomForm(forms.Form):
    name = forms.CharField(max_length=100, label='Название')
    slug = forms.SlugField(max_length=100, label='URL')


class AddChatForm(forms.Form):
    name = forms.CharField(max_length=100, label='Название')
    slug = forms.SlugField(max_length=100, label='URL')