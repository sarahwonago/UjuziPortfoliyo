from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username',)

class UserModForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("username","first_name","last_name","email","profilephoto", "phone_number", "country","fb_link","instagram_link","x_link","github_link","linkedin_link")
         