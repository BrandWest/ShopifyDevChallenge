from django.db import models
from django.contrib import auth
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#Custom Forms
from .models import Images

# Sign Up Form
class UserProfile(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            ]


#Image upload form
class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('caption', 'images', 'current_user')