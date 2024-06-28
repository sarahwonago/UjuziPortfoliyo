from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
  path("", register_view, name="register_user"),
  path("logoutuser/", logout_view, name="logout_user"),
  path("delete-account/<str:username>/", delete_account_view, name="delete_account"),
]
