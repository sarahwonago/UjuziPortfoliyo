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
        # Alternatively, you can use exclude to specify which fields not to include
        # exclude = ('password', 'field_to_exclude_1', 'field_to_exclude_2')

    def __init__(self, *args, **kwargs):
        super(UserModForm, self).__init__(*args, **kwargs)
        # Exclude password field
        self.fields.pop('password')