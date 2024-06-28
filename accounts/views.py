from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def logout_view(request):
    logout(request)
    return redirect("login")


def register_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard:dashboard")
       
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect("login")


    else:
        form = UserRegisterForm()
        
    context={
        "form":form,
    }
    return render(request, "accounts/user_registration.html", context)

@login_required
def delete_account_view(request, username):

    if request.user.username != username:
        return redirect("dashboard:forbidden")
    
    user = request.user

    if request.method == 'POST':
        user.delete()
        return redirect("/")
    
    return render(request, "accounts/delete_account.html")
