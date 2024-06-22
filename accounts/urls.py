from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
  path("register/", register_view, name="register_user"),
  path("login/", login_view, name="login_user"),
  path("logoutuser/", logout_view, name="logout_user"),
]
