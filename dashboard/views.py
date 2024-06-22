from django.shortcuts import render
from userportfoliyo.forms import *

def dashboard(request):
    return render(request, "dashboard/dashboard.html")

def profile_view(request):
    form = ProfileForm()
    context = {
        "form":form,
    }
    return render(request, "dashboard/profile.html", context)


def socials_view(request):
    form = SocialsForm()
    context = {
        "form":form,
    }
    return render(request, "dashboard/socials.html", context)

def professional_info_view(request):
    form = ProfessionalProfileForm()
    context = {
        "form":form,
    }
    return render(request, "dashboard/professional.html", context)

def add_work_view(request):
    form = WorkExperienceForm()
    context = {
        "form":form,
    }
    return render(request, "dashboard/add_work.html", context)


def view_work_view(request):
   
    return render(request, "dashboard/view_work.html")


def edit_work_view(request):
 
    return render(request, "dashboard/edit_work.html")

def add_profession_view(request):
    form = ProfessionForm()
    context = {
        "form":form,
    }
    return render(request, "dashboard/add_profession.html", context)

def view_proffesion_view(request):
   
    return render(request, "dashboard/view_profession.html")


def edit_profession_view(request):
 
    return render(request, "dashboard/edit_profession.html")

def add_project_view(request):
    form = ProjectForm()
    context = {
        "form":form,
    }
    return render(request, "dashboard/add_project.html", context)

def view_project_view(request):
   
    return render(request, "dashboard/view_project.html")


def edit_project_view(request):
 
    return render(request, "dashboard/edit_project.html")

def add_blog_view(request):
    form = BlogForm()
    context = {
        "form":form,
    }
    return render(request, "dashboard/add_blog.html", context)

def view_blog_view(request):
   
    return render(request, "dashboard/view_blogs.html")


def edit_blog_view(request):
 
    return render(request, "dashboard/edit_blog.html")

def add_review_view(request):
    form = ReviewForm()
    context = {
        "form":form,
    }
    return render(request, "dashboard/add_review.html", context)

def view_review_view(request):
   
    return render(request, "dashboard/view_review.html")


def edit_review_view(request):
 
    return render(request, "dashboard/edit_review.html")