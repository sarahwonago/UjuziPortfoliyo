from django.contrib import admin
from django.contrib.auth.admin  import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserRegisterForm, UserModForm

User= get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form=UserRegisterForm
    form=UserModForm
    model=User
    list_display=[
        "email","username", "is_superuser",
    ]
admin.site.register(User, CustomUserAdmin)
