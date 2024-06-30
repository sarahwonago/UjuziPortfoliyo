from django.contrib import admin
from django.contrib.auth.admin  import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserRegisterForm, UserModForm

User= get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form=UserRegisterForm
    form=UserModForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'first_name', 'last_name', 'profilephoto',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        # Add other fieldsets if necessary
    )
    model=User
    list_display=[
        "email","username", "is_superuser",
    ]
admin.site.register(User, CustomUserAdmin)
