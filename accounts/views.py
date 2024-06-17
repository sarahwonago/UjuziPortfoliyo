from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def logout_view(request):
    logout(request)
    return redirect("ujuziwebsite:home")

def login_view(request):

    if request.user.is_authenticated:
        return redirect("ujuziwebsite:home")
    
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("ujuziwebsite:home")
    
    return render(request, "accounts/registration/login.html")

def register_view(request):

    if request.user.is_authenticated:
        return redirect("ujuziwebsite:home")
       
    
    return render(request, "accounts/registration/user_registration.html")